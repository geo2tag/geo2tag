#!/bin/bash
MYPATH="$PWD"
PATH1="$PWD/geomongo"
PATH2="$PWD/geomongo/src"
PATH3="$PWD/geomongo/src/plugins/ok_import"
PATH3="$PWD/geomongo/src/open_data_import"
PATH4="$PWD/geomongo/scripts/performance/od_performance"
PATH5="$PWD/geomongo/src/geocoders"
eval 'export PYTHONPATH="$PYTHONPATH:$PATH1:$PATH2:PATH3:PATH4:PATH5"'
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
