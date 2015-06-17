#!/bin/bash

cd src/tst_integration/

python main.py ${1:-http://geomongo/}
