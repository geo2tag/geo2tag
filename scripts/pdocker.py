#!/usr/bin/python
import argparse
from pymongo import MongoClient
from subprocess import Popen, PIPE
import datetime
import sys
import os
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

# env variables
CONTAINER_ENV = "CONTAINER"
FAIL_REASON = "FAIL_REASON"

# fail reasons
SUCCESS_MSG = "SUCCESS"
TESTS_FAILED_MSG = "tests failed ( unit {}, integration {}, selenium {})"
NO_PORTS_MSG = "Free port not found exit"


def usage():
    print "-n [container name] -p [ports range]"
    sys.exit(1)


def write_log(name, log_str):
    file_name = "/tmp/" + name.replace('/', '_') + LOG_NAME
    print log_str
    with open(file_name, 'ab') as log_file:
        log_file.write(log_str)


def manage_script(name, args):
    child = Popen(args, stdout=PIPE, stderr=PIPE)
    output = child.stdout.read()
    err = child.stderr.read()
    child.communicate()
    rc = child.returncode
    if rc == 0:
        write_log(name, output)
    else:
        if err == '' and output != '':
            write_log(name, output)
        write_log(name, err)
    return rc


def start_container(name, port):
    rc = manage_script(
        name, [CREATE_CONTAINER, '-p', unicode(port), '-n', name])
    if rc != 0:
        sys.exit(rc)


def stop_container(name):
    manage_script(name, [MANAGE_CONTAINER, 'kill', name])


def run_unit_tests(name):
    rc_unit = manage_script(name, [MANAGE_CONTAINER, 'tunit', name])
    return rc_unit


def run_selenium_tests(name):
    rc_sel = manage_script(name, [MANAGE_CONTAINER, 'tsel', name])
    return rc_sel


def run_int_tests(name):
    rc_int = manage_script(name, [MANAGE_CONTAINER, 'tint', name])
    return rc_int


def wait_mongo_start(name):
    child = Popen(['docker', 'exec', name, 'mongo'], stdout=PIPE, stderr=PIPE)
    child.communicate()
    return child.returncode


def mongo_start_waiter(name):
    counter_start = 0
    while True:
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
                collection.save({CONTAINER_NAME: container_start_name,
                                 CONTAINER_PORT: i,
                                 CONTAINER_START: int(round(time.time()))})
                start_container(container_start_name, i)
                container_start_port = i
                container_start_result = True
                break
    else:
        container[CONTAINER_START] = int(round(time.time()))
        collection.update(
            {CONTAINER_ID: container[CONTAINER_ID]}, container, True)

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
        print container[CONTAINER_NAME] + " on port " + \
            unicode(container[CONTAINER_PORT]) + " stop"
        stop_container(container[CONTAINER_NAME])
        collection.remove({CONTAINER_ID: container[CONTAINER_ID]})


def parse_string_time_to_timestamp(parsing_str):
    p = re.compile(u'(\d+\w)')
    time_list = re.findall(p, parsing_str)
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


def create_container_env_var(container_start_port):
    container_env = "http://" + \
                    os.environ["SERVER"] + ":" \
                    + unicode(container_start_port) + \
                    "/instance/tests"
    return container_env


def write_env_var(variable, value):
    f = open('propsfile', 'aw')
    f.write(variable + '=' + value + '\n')
    f.close()


def build_test_fail_message(t_int, t_unit, t_sel):
    result = TESTS_FAILED_MSG.format(
        t_unit != 0, t_int != 0, t_sel != 0)
    return result


def main(name, ports):
    container_start_name = name.replace('/', '_')
    if "origin_" not in container_start_name:
        container_start_name = "origin_" + container_start_name

    file_name = "/tmp/" + container_start_name + LOG_NAME
    print file_name

    container_start_result, container_start_port = find_port_and_start(
        container_start_name, ports)
    if not container_start_result:
        write_log(container_start_name, NO_PORTS_MSG)
        write_env_var(FAIL_REASON, NO_PORTS_MSG)
        sys.exit(1)

    mongo_start_waiter(container_start_name)
    write_log(
        container_start_name,
        "Container " +
        container_start_name +
        " started on port %d" %
        container_start_port)

    write_log(container_start_name, "Run Unit tests")
    t_unit = run_unit_tests(container_start_name)

    write_log(container_start_name, "Run int tests")
    t_int = run_int_tests(container_start_name)

    write_log(container_start_name, "Run sel tests")
    t_sel = run_selenium_tests(container_start_name)

    container_value = create_container_env_var(container_start_port)

    write_env_var(CONTAINER_ENV, container_value)

    if t_int != 0 or t_unit != 0 or t_sel != 0:
        write_env_var(FAIL_REASON,
                      build_test_fail_message(t_int, t_unit, t_sel))
        try:
            sys.exit(1)  # Or something that calls sys.exit()
        except SystemExit:
            print '----EXIT----'
            f = open('propsfile', 'r')
            print f.read()
            f.close()
    write_log(container_start_name, container_value)

    write_log(container_start_name, "Done")
    write_env_var(FAIL_REASON, SUCCESS_MSG)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name')
    parser.add_argument('-p', '--ports')

    parser.add_argument('-k', '--kill', action='store_true')
    parser.add_argument('-t', '--time', default='1w')
    parsed_args = parser.parse_args()

    if parsed_args.kill is not False:
        timestamp = 0
        if parsed_args.time is not None:
            timestamp = parse_string_time_to_timestamp(parsed_args.time)
        kill_old_containers(timestamp)
    elif (parsed_args.name or parsed_args.ports) is None:
        usage()
    else:
        main(parsed_args.name, parsed_args.ports)
    sys.exit(0)
