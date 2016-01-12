#!/bin/bash


./scripts/pep8_check.sh 
codePep8=$?;
./scripts/pylint_check.sh 
codePylint=$?;

if [ $codePep8 -ne "0" ] || [ $codePylint -ne "0" ]
then
	exit 1
fi
