#!/usr/bin/python
import argparse
from pymongo import MongoClient
from subprocess import Popen, PIPE

HOST = 'localhost'
PORT = 27017
DBNAME = 'docker-client'
COLLECTION_NAME = "ports"
db = MongoClient(HOST, PORT)[DBNAME]
# keys
CONTAINER_NAME = "name"
CONTAINER_PORT = "port"


def usage():
    print "-n [container name] -p [ports range]"


def start_container(name, port):
    child = Popen(["scripts/docker_create.sh", '-p', str(port), '-n', name], stdout=PIPE, stderr=PIPE)
    output = child.stdout.read()
    err = child.stderr.read()
    streamdata = child.communicate()[0]
    rc = child.returncode
    print output, err
    print rc


def stop_container(name):
    return 1


def run_tests(name):
    return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name')
    parser.add_argument('-p', '--ports')
    args = parser.parse_args()

    if (args.name or args.ports) is None:
        usage()
    else:
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
    return 0


if __name__ == "__main__":
    main()
