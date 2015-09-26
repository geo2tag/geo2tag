#!/bin/bash
MYPATH="$PWD"
PATH1=":$PWD/geomongo"
PATH2=":$PWD/geomongo/src"
eval 'export PYTHONPATH="$PYTHONPATH$PATH1$PATH2"'
echo "$PYTHONPATH"