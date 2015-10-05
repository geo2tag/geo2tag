#!/bin/bash

PYSCRIPT="$PWD/scripts/generate_class_resource.py"
NEWPATH="$PWD/src/"
NEWPATH="$PWD/src/"
SEPARATOR=""
if [ -z "${PYTHONPATH}" ]; then
    SEPARATOR=":"
fi
export PYTHONPATH="${PYTHONPATH}${PYTHONPATH}${NEWPATH}"
echo ${PYTHONPATH}

python ${PYSCRIPT} ${@}