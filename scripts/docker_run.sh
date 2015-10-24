#!/bin/bash

#start mongo
exec mongod --smallfiles --noprealloc &
./scripts/papache_conf_generator.py -n localhost -o 000-default
#deploy app
./scripts/local_deploy.sh -c 000-default.conf
#start service
cp config/supervisord.conf /etc/supervisord.conf
supervisord -n
