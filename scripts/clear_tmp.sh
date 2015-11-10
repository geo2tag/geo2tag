#!/bin/bash

AGE=${1:-7}

echo "Before cleaning /tmp/"
df -h
echo "Removed files"
find /tmp -type f  -name 'tmp*' -mtime +$AGE -print | sed -e 's|/tmp/|\n/tmp/|' 
echo "`find /tmp -type f  -name 'tmp*' -mtime +$AGE -print | wc -l` files where deleted"
LIST=`find /tmp -mtime +$AGE -print0 -name 'tmp*' -exec rm -fr "{}" \;`
echo "Disk space statistics after old files removing"
df -h
