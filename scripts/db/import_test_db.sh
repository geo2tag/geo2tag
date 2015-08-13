#!/bin/bash

dbs=(geomongo testservice)

for db in ${dbs[*]}; do
    scripts/db/mongo.sh -l -H localhost:27017 ${db}
    if [ $? -gt 0 ]; then
        echo 'Error occured while imorting database: '${db}'.'
    fi
done
