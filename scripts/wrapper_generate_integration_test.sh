#!/bin/bash

PYSCRIPT="$PWD/scripts/generate_integration_test.py"
NEWPATH="$PWD/src/"

eval "export PYTHONPATH=${PYTHONPATH}${NEWPATH}"
echo ${PYTHONPATH}

python ${PYSCRIPT} ${@}

