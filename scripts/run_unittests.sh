#!/bin/bash
set -e
DB_SCRIPTS_PATH='scripts/db/';

# Clean testdb
./${DB_SCRIPTS_PATH}/drop_test_db.sh

# Import testdb
./${DB_SCRIPTS_PATH}/import_test_db.sh

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
