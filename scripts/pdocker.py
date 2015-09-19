#!/usr/bin/python
import argparse
from pymongo import MongoClient
from subprocess import Popen, PIPE
import datetime
import sys
from time import sleep
import time
import re


HOST = 'localhost'
PORT = 27017
DBNAME = 'docker-client'
COLLECTION_NAME = "ports"
LOG_NAME = datetime.datetime.now().strftime("-%d-%m-%y-%H:%M:%S") + ".log"
db = MongoClient(HOST, PORT)[DBNAME]

# scripts
CREATE_CONTAINER = "scripts/docker_create.sh"
MANAGE_CONTAINER = "scripts/docker_manage.sh"

# keys
CONTAINER_NAME = "name"
CONTAINER_PORT = "port"
CONTAINER_START = "start"
CONTAINER_ID = "_id"


def usage():
    print "-n [container name] -p [ports range]"
    sys.exit(1)


def write_log(name, log_str):
    file_name = "/tmp/" + name + LOG_NAME
    print log_str
    with open(file_name, 'ab') as log_file:
        log_file.write(log_str)


def manage_script(name, args):
    child = Popen(args, stdout=PIPE, stderr=PIPE)
    output = child.stdout.read()
    err = child.stderr.read()
    streamdata = child.communicate()[0]
    rc = child.returncode
    if rc == 0:
        write_log(name, output)
    else:
        write_log(name, err)
    return rc


def start_container(name, port):
    rc = manage_script(name, [CREATE_CONTAINER, '-p', str(port), '-n', name])
    if rc != 0:
        sys.exit(rc)


def stop_container(name):
    rc = manage_script(name, [MANAGE_CONTAINER, 'kill', name])


def run_unit_tests(name):
    rc_unit = manage_script(name, [MANAGE_CONTAINER, 'tunit', name])
    return rc_unit


def run_int_tests(name):
    rc_int = manage_script(name, [MANAGE_CONTAINER, 'tint', name])
    return rc_int


def wait_mongo_start(name):
    child = Popen(['docker', 'exec', name, 'mongo'], stdout=PIPE, stderr=PIPE)
    streamdata = child.communicate()[0]
    return child.returncode


def mongo_start_waiter(name):
    counter_start = 0
    while 1:
        counter_start += 1
        if wait_mongo_start(name) == 0:
            write_log(name, "Mongo start")
            break
        elif counter_start == 10:
            write_log(name, "Container start fail")
            sys.exit(1)
        else:
            write_log(name, "Waiting mongo")
            sleep(3)


def find_port_and_start(container_start_name, ports):
    container_start_port = 0
    container_start_result = False
    collection = db[COLLECTION_NAME]
    container = collection.find_one({CONTAINER_NAME: container_start_name})
    # if container not found search for free port
    if container is None:
        ports_range = ports.split('-')
        for i in range(int(ports_range[0]), int(ports_range[1]) + 1):
            container_on_port = collection.find_one({CONTAINER_PORT: i})
            if container_on_port is None:
                collection.save({CONTAINER_NAME: container_start_name, CONTAINER_PORT: i,
                                 CONTAINER_START: int(round(time.time() * 1000))})
                start_container(container_start_name, i)
                container_start_port = i
                container_start_result = True
                break
    else:
        container[CONTAINER_START] = int(round(time.time()))
        collection.update({CONTAINER_ID: container[CONTAINER_ID]}, container, True)

        stop_container(container_start_name)
        start_container(container_start_name, container[CONTAINER_PORT])
        container_start_port = container[CONTAINER_PORT]
        container_start_result = True

    return [container_start_result, container_start_port]


def kill_old_containers(kill_time=0):
    time_pass = 0
    if kill_time != 0:
        time_pass = int(round(time.time())) - kill_time
    else:
        time_pass = int(round(time.time())) - (168 * 60 * 60)
    collection = db[COLLECTION_NAME]
    containers = collection.find({CONTAINER_START: {"$lte": time_pass}})
    if containers is None:
        return

    for container in containers:
        print container[CONTAINER_NAME] + " on port " + str(container[CONTAINER_PORT]) + " stop"
        stop_container(container[CONTAINER_NAME])
        collection.remove({CONTAINER_ID: container[CONTAINER_ID]})


def parse_string_time_to_timestamp(str):
    p = re.compile(u'(\d+\w)')
    time_list = re.findall(p, str)
    result = 0
    for time_unit in time_list:
        s = time_unit[-1:]
        t = int(time_unit[:-1])
        if s == 'y':
            result += t * 31556926  # second in year
        elif s == 'M':
            result += t * 2629743  # seconds in month
        elif s == 'w':
            result += t * (168 * 60 * 60)
        elif s == 'd':
            result += t * (24 * 60 * 60)
        elif s == 'h':
            result += t * (60 * 60)
        elif s == 'm':
            result += t * 60
        elif s == 's':
            result += t

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name')
    parser.add_argument('-p', '--ports')

    parser.add_argument('-k', '--kill', action='store_true')
    parser.add_argument('-t', '--time')
    args = parser.parse_args()

    if args.kill is not False:
        timestamp = 0
        if args.time is not None:
            timestamp = parse_string_time_to_timestamp(args.time)
        kill_old_containers(timestamp)
    elif (args.name or args.ports) is None:
        usage()
    else:
        container_start_name = args.name

        file_name = "/tmp/" + container_start_name + LOG_NAME
        print file_name

        container_start_result, container_start_port = find_port_and_start(args.name, args.ports)
        if not container_start_result:
            write_log(args.name, "Free port not found exit")
            sys.exit(1)

        # waiting for mongo
        mongo_start_waiter(container_start_name)
        write_log(container_start_name,
                  "Container " + container_start_name + " started on port %d" % container_start_port)

        write_log(container_start_name, "Run Unit tests")
        t_unit = run_unit_tests(container_start_name)

        write_log(container_start_name, "Run int tests")
        t_int = run_int_tests(container_start_name)

        if t_int != 0 or t_unit != 0:
            sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
