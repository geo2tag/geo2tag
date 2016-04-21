#!/bin/bash
# use option -f without arguments to keep config.ini file
# use option -c <catalog_name> to change /geomongo catalog
# use option -d <config_ini_file_name> to using new config ini file instead config/config.ini
# use option -e <config_file_name> to using new config file instead config/geomongo.conf
# use option -el <error_log_name> to using new apache error log name
# use option -s <server_name> to set server name
# use option -m without arguments to call drop_db.sh and setupMasterDbTemplate.py

CATALOG='geomongo'
ERROR_LOG_NAME='error'
SERVER_NAME='geomongo'
SERVER_PORT='80'
HOSTS_STRING="127.0.0.1 geomongo"
DEBUG_FILE="/var/www/geomongo/DEBUG"
CONFIG_FILE="geomongo.conf"
FLAG_KEEP_CONFIG_INI=false
CONFIG_INI_FILE='config/config.ini'
CONFIG_INI_FILE_FINAL='config.ini'
FLAG_DROP_DB_AND_SETUP_DB_TEMPLATE=false

while getopts ":c:d:e:f:ef:s:p:m" opt ;
do
    case $opt in
        c) CATALOG=$OPTARG;
            ;;
        f) FLAG_KEEP_CONFIG_INI=true;
            ;;
        d) CONFIG_INI_FILE=$OPTARG;
            ;;
        e) CONFIG_FILE=$OPTARG;
            ;;
        ef) ERROR_LOG_NAME=$OPTARG;
            ;;
        s) SERVER_NAME=$OPTARG;
            ;;
        p) SERVER_PORT=$OPTARG;
            ;;
        m) FLAG_DROP_DB_AND_SETUP_DB_TEMPLATE=true;
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

#generate config for apache
./scripts/papache_conf_generator.py -n "$SERVER_NAME" -o "$CONFIG_FILE" -f "$CATALOG" -e "$ERROR_LOG_NAME" -p "$SERVER_PORT"

rm -rf /var/www/"$CATALOG"

mkdir /var/www/"$CATALOG"

cp src/*.py  /var/www/"$CATALOG"
cp src/*.wsgi /var/www/"$CATALOG"
if ! $FLAG_KEEP_CONFIG_INI
then
    cp "$CONFIG_INI_FILE" /var/www/"$CATALOG"/"$CONFIG_INI_FILE_FINAL"
fi
cp -r src/static /var/www/"$CATALOG"/static/
cp -r src/templates /var/www/"$CATALOG"/templates/
cp -r src/plugins /var/www/"$CATALOG"/plugins/
cp -r src/open_data_import/ /var/www/"$CATALOG"/open_data_import/
cp -r src/plugin_api/ /var/www/"$CATALOG"/plugin_api/
cp config/"$CONFIG_FILE" /etc/apache2/sites-available/

./scripts/setup_pip_dependencies.sh

if $FLAG_DROP_DB_AND_SETUP_DB_TEMPLATE
then
    ./scripts/db/drop_test_db.sh
    python scripts/db/setupMasterDbTemplate.py --config ${CONFIG_INI_FILE}
fi

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
