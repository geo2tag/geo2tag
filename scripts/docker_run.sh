#!/bin/bash
#start mongo
exec mongod --smallfiles --noprealloc &
#./scripts/papache_conf_generator.py -n localhost -o 000-default.conf
#deploy app
./scripts/local_deploy.sh -e 000-default.conf -s localhost 2>&1 | tee /tmp/local_deploy.log

#start service
cp config/supervisord.conf /etc/supervisord.conf
supervisord -n
