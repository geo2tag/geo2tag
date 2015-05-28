#!/bin/bash

mongo geomongo --eval "db.dropDatabase()"
mongo testservice --eval "db.dropDatabase()"
