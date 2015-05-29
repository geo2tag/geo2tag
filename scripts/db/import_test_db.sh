#!/bin/bash

scripts/db/mongo.sh -l -H localhost:27017 geomongo
scripts/db/mongo.sh -l -H localhost:27017 testservice
