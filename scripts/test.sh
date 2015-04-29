#!/bin/bash

SERVER='http://geomongo/';
PREFIX='instance';

echo "Service test";
curl -v "${SERVER}${PREFIX}/service/"-d '{"1":"0"}' 
curl -v "${SERVER}${PREFIX}/service/testService" 
curl -v "${SERVER}${PREFIX}/service/testService" -d '{"1":"2"}' -X PUT
curl -v "${SERVER}${PREFIX}/service/testService" -X DELETE
