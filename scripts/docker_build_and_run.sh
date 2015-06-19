#!/bin/bash

docker build -t osll/geomongo .
docker run -d -p 54333:80 --name geomongo osll/geomongo
