#!/bin/bash
echo "Before cleaning /tmp/"
df -h
echo "Removed files"
find /tmp -type f  -name 'tmp*' -mtime +7 -print 
LIST=`find /tmp -mtime +7 -print0 -name 'tmp*' -exec rm -fr "{}" \;`
echo "`find /tmp -type f  -name 'tmp*' -mtime +7 -print | wc -l` files where deleted"
echo "Disk space statistics after old files removing"
df -h
