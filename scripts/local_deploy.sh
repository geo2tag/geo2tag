#!/bin/bash

HOSTS_STRING="127.0.0.1 geomongo"
if ! grep -Fxq "$HOSTS_STRING" /etc/hosts
then
	echo "$HOSTS_STRING" >> /etc/hosts
fi

rm -rf /var/www/geomongo

mkdir /var/www/geomongo

cp src/* config/config.ini /var/www/geomongo
cp config/geomongo.conf /etc/apache2/sites-available/ 

./scripts/setup_pip_dependencies.sh

chown -R www-data:www-data /var/www/geomongo

a2ensite geomongo.conf

service apache2 restart
