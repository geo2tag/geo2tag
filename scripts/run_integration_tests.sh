#!/bin/bash

DB_SCRIPTS_PATH='scripts/db/';

# Clean testdb
./${DB_SCRIPTS_PATH}/drop_test_db.sh

# Import testdb
./${DB_SCRIPTS_PATH}/import_test_db.sh

cd src/tst_integration/

python main.py ${1:-http://geomongo/}
