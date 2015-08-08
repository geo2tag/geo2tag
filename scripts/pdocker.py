#!/usr/bin/python
import argparse
from pymongo import MongoClient
import pymongo
from pymongo import Connection

HOST = 'localhost'
PORT = 27017
DBNAME = 'docker-client'
COLLECTION_NAME = "ports"
db = MongoClient(HOST, PORT)[DBNAME]


def usage():
    print "-n [container name] -p [ports range]"


def start_container(name, port):
    return 1


def stop_container(name):
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
        ports_range = args.ports.split('-')
        for i in range(int(ports_range[0]), int(ports_range[1]) + 1):
            collection.save(dict(name=args.name, port=i))
            break


if __name__ == "__main__":
    main()
