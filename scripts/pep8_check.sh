#!/bin/bash

echo
echo "===================== PEP8 CHECK ======================"
echo

pep8 `find ./ | grep .py$`
