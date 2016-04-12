#!/bin/bash 

# This script require installed autopep8 util 

autopep8 --in-place --aggressive --aggressive --aggressive `find ./ | grep '\.py$'` 
