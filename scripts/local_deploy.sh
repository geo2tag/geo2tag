#!/bin/bash
# use option -f without arguments to keep config.ini file
# use option -c <catalog_name> to change /geomongo catalog
HOSTS_STRING="127.0.0.1 geomongo"
DEBUG_FILE="/var/www/geomongo/DEBUG"
CONFIG_FILE=${1:-"geomongo.conf"}
FLAG_KEEP_CONFIG_INI=false
CATALOG='geomongo'

while getopts ":c:f" opt ;
do
    case $opt in
        c) CATALOG=$OPTARG;
            ;;
        f) FLAG_KEEP_CONFIG_INI=true;
            ;;
        *) echo "the option is incorrect";
            exit 1
            ;;
        esac
done

if ! grep -Fxq "$HOSTS_STRING" /etc/hosts
then
	echo "$HOSTS_STRING" >> /etc/hosts
fi

rm -rf /var/www/"$CATALOG"

mkdir /var/www/"$CATALOG"

cp src/*.py  /var/www/"$CATALOG"
cp src/*.wsgi /var/www/"$CATALOG"
if ! $FLAG_KEEP_CONFIG_INI
then
    cp config/config.ini /var/www/"$CATALOG"
fi
cp -r src/static /var/www/"$CATALOG"/static/
cp -r src/templates /var/www/"$CATALOG"/templates/
cp -r src/plugins /var/www/"$CATALOG"/plugins/
cp config/"$CONFIG_FILE" /etc/apache2/sites-available/

./scripts/setup_pip_dependencies.sh

COMMIT=$(git rev-parse HEAD)
BRANCH=$(git status |head -1| cut -d' ' -f 3)
DATE=$(date -R)
VERSION=$(git tag | tail -1)
[ ${#VERSION} == 0 ] && VERSION="no version" 
echo "{ 
'commit' : '$COMMIT' 
'date' : '$DATE'
'branch' : '$BRANCH'
'version' : '$VERSION'
}" > $DEBUG_FILE

chown -R www-data:www-data /var/www/"$CATALOG"

a2ensite $CONFIG_FILE

service apache2 restart