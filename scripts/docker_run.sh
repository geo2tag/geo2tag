#!/bin/bash

#start mongo
exec mongod --smallfiles --noprealloc &
#create link
ln -s config/geomongo.conf config/000-default.conf
#deploy app
./scripts/local_deploy.sh 000-default.conf
#start service
cp config/supervisord.conf /etc/supervisord.conf
supervisord -n
