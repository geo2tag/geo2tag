#!/bin/bash
#deploy app
./scripts/local_deploy.sh
#start services
exec mongod --smallfiles --noprealloc &
cp config/supervisord.conf /etc/supervisord.conf
supervisord -n
