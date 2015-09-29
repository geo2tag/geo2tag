#!/bin/bash

PYSCRIPT="$PWD/scripts/generate_class_resource.py"
NEWPATH="$PWD/src/"

eval "export PYTHONPATH=${PYTHONPATH}${NEWPATH}"
echo ${PYTHONPATH}

python ${PYSCRIPT} ${@}