#!/bin/bash

scripts/db/mongo.sh -H localhost:27017 geomongo
scripts/db/mongo.sh -H localhost:27017 testservice
