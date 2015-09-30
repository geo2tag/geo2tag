#!/bin/bash

PYSCRIPT="$PWD/scripts/db/setupMasterDbTemplate.py"
NEWPATH="$PWD/src/"
NEWPATH="$PWD/src/"
SEPARATOR=""
if [ -z "${PYTHONPATH}" ]; then
    SEPARATOR=":"
fi
export PYTHONPATH="${PYTHONPATH}${SEPARATOR}${NEWPATH}"
echo ${PYTHONPATH}

python ${PYSCRIPT} ${@}