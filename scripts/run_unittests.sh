#!/bin/bash

echo
echo "==================== UNITTESTS ====================="
echo

MYPATH="$PWD"
PATH1="$PWD/src"
PATH2="$PWD/src/plugins/ok_import"
PATH3="$PWD/src/open_data_import"
PATH4="$PWD/scripts/performance/od_performance"
PATH5="$PWD/src/geocoders"
PATH6="$PWD/src/plugins/geocoder"
PATH7="$PWD/src/plugin_api"
PATH8="$PWD/scripts"
PATH9="$PWD/src/plugins/smartm3"
eval 'export PYTHONPATH="$PYTHONPATH$PATH1:$PATH2:$PATH3:$PATH4:$PATH5:$PATH6:$PATH7:$PATH8:$PATH9"'
echo "$PYTHONPATH"
DB_SCRIPTS_PATH='scripts/db/';

# Clean testdb
./${DB_SCRIPTS_PATH}/drop_test_db.sh
if [ $? -gt 0 ]; then
    echo 'Error occured during drop_test_db.sh'
    exit 1
fi

# Import testdb
./${DB_SCRIPTS_PATH}/import_test_db.sh
if [ $? -gt 0 ]; then
    echo 'Error occured during import_test_db.sh'
    exit 1
fi

# Run tests

cd src/tst
result=`python -m unittest discover -v 2>&1`
exit_code=$?
echo "$result" 

testState=`echo "$result" | grep -iE "FAILED|Error|CRITICAL" || true` ;
if [[ -n $testState  ]]
then
        exit 1
fi
