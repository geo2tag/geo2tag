#!/bin/bash
docker build -t osll/geomongo .
docker run -d -p 54333:80 -v `pwd`/src:/app/src -v `pwd`/scripts:/app/scripts -v `pwd`/config:/app/config -v `pwd`/master_db_template:/app/master_db_template -v `pwd`/testdump:/app/testdump  --name geomongo osll/geomongo


