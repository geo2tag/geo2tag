#!/bin/bash

echo
echo "==================== INTEGRATIONTESTS ====================="
echo

MYPATH="$PWD"
PATH1="$PWD/src"
PATH2="$PWD/src/plugins/ok_import"
PATH3="$PWD/src/open_data_import"
PATH4="$PWD/src/geocoders"
PATH5="$PWD/src/plugins/geocoder"
PATH6="$PWD/src/plugin_api"
eval 'export PYTHONPATH="$PYTHONPATH$PATH1:$PATH2:$PATH3:$PATH4:$PATH5:$PATH6"'
echo "$PYTHONPATH"

set -e
DB_SCRIPTS_PATH='scripts/db/';

# Clean testdb
./${DB_SCRIPTS_PATH}/drop_test_db.sh

# Import testdb
./${DB_SCRIPTS_PATH}/import_test_db.sh

cd src/tst_integration/

python main.py ${1:-http://geomongo/}
