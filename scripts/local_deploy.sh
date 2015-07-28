#!/bin/bash

HOSTS_STRING="127.0.0.1 geomongo"
DEBUG_FILE="/var/www/geomongo/DEBUG"
if ! grep -Fxq "$HOSTS_STRING" /etc/hosts
then
	echo "$HOSTS_STRING" >> /etc/hosts
fi

rm -rf /var/www/geomongo

mkdir /var/www/geomongo

cp src/*  /var/www/geomongo
cp config/config.ini /var/www/geomongo
cp -r src/static /var/www/geomongo/static/
cp -r src/templates /var/www/geomongo/templates/
cp -r src/plugins /var/www/geomongo/plugins/
cp config/geomongo.conf /etc/apache2/sites-available/ 

./scripts/setup_pip_dependencies.sh

COMMIT=$(git rev-parse HEAD)
BRANCH=$(git status |head -1| cut -d' ' -f 3)
DATE=$(date -R)
VERSION=$(git describe)
[ ${#VERSION} == 0 ] && VERSION="no version" 
echo "{ 
'commit' : '$COMMIT' 
'date' : '$DATE'
'branch' : '$BRANCH'
'version' : '$VERSION'
}" > $DEBUG_FILE

chown -R www-data:www-data /var/www/geomongo

a2ensite geomongo.conf

service apache2 restart



