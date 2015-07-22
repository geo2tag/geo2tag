#!/bin/bash
docker build -t osll/geomongo .
docker run -d -p 54333:80 -v `pwd`/src:/var/www/geomongo --name geomongo osll/geomongo

