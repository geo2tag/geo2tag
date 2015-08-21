#!/bin/bash

#start mongo
exec mongod --smallfiles --noprealloc &
#deploy app
./scripts/local_deploy.sh
#start service
cp config/supervisord.conf /etc/supervisord.conf
supervisord -n
