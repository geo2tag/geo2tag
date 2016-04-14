#!/bin/bash

mongo geomongo --eval "db.dropDatabase()"
mongo testservice --eval "db.dropDatabase()"
mongo master_db_template --eval "db.dropDatabase()"
mongo geomongo --eval "db.dropDatabase()"
