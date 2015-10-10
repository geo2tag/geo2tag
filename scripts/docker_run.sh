#!/bin/bash

#start mongo
exec mongod --smallfiles --noprealloc &
#deploy app
./scripts/local_deploy.sh
#create link
#rm -f /etc/apache2/sites-enabled/000-default.conf
rm -f /etc/apache2/sites-available/000-default.conf
#ln -s config/geomongo.conf /etc/apache2/sites-enabled/000-default.conf
cp -s config/geomongo.conf /etc/apache2/sites-available/000-default.conf
#start service
cp config/supervisord.conf /etc/supervisord.conf
supervisord -n
