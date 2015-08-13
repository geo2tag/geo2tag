#!/usr/bin/python
import argparse
from pymongo import MongoClient
from subprocess import Popen, PIPE
import datetime
import sys


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


def usage():
    print "-n [container name] -p [ports range]"
    sys.exit(1)


def write_log(name, log_str):
    file_name = "/tmp/" + name  + LOG_NAME
    with open(file_name, 'ab') as log_file:
        log_file.write(log_str)


def manage_script(name, args):
    child = Popen(args, stdout=PIPE, stderr=PIPE)
    output = child.stdout.read()
    err = child.stderr.read()
    streamdata = child.communicate()[0]
    rc = child.returncode
    if rc == 0:
        print output
        write_log(name, output)
    else:
        print err
        write_log(name, err)
    return rc


def start_container(name, port):
    rc = manage_script(name, [CREATE_CONTAINER, '-p', str(port), '-n', name])
    if rc != 0:
        sys.exit(rc)


def stop_container(name):
    rc = manage_script(name, [MANAGE_CONTAINER, 'kill', name])
   # if rc != 0:
       # sys.exit(rc)


def run_unit_tests(name):
    rc_unit = manage_script(name, [MANAGE_CONTAINER, 'tunit', name])
    return rc_unit


def run_int_tests(name):
    rc_int = manage_script(name, [MANAGE_CONTAINER, 'tint', name])
    return rc_int


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name')
    parser.add_argument('-p', '--ports')
    args = parser.parse_args()

    if (args.name or args.ports) is None:
        usage()
    else:
        file_name = "/tmp/" + args.name + LOG_NAME
        print file_name
        collection = db[COLLECTION_NAME]
        container = collection.find_one({CONTAINER_NAME: args.name})
        if container is None:
            ports_range = args.ports.split('-')
            for i in range(int(ports_range[0]), int(ports_range[1]) + 1):
                container_on_port = collection.find_one({CONTAINER_PORT: i})
                if container_on_port is None:
                    collection.save({CONTAINER_NAME: args.name, CONTAINER_PORT: i})
                    start_container(args.name, i)
                    break
        else:
            stop_container(args.name)
            start_container(args.name, container[CONTAINER_PORT])
    t_unit = run_unit_tests(args.name)
    t_int = run_int_tests(args.name)
    if t_int != 0 or t_unit != 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
