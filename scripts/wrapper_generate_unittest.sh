#!/bin/bash

PYSCRIPT="$PWD/scripts/generate_unittest.py"
NEWPATH="$PWD/src/"

eval "export PYTHONPATH=${PYTHONPATH}${NEWPATH}"
echo ${PYTHONPATH}

python ${PYSCRIPT} ${@}