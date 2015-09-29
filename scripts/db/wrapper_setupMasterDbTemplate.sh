#!/bin/bash

PYSCRIPT="$PWD/scripts/db/setupMasterDbTemplate.py"
NEWPATH="$PWD/src/"

eval "export PYTHONPATH=${PYTHONPATH}${NEWPATH}"
echo ${PYTHONPATH}

python ${PYSCRIPT} ${@}