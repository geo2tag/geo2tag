#!/bin/bash
echo "Before cleaning /tmp/"
df -h
LIST=`find /tmp -mtime +7 -print0 -name 'tmp*' -exec rm -fr "{}" \;`
echo ${LIST} | sed -e 's/\/tmp\/tmp/\n/g'
echo "`echo $LIST | grep -o '/tmp/tmp/' | wc -w` files where deleted"
echo "Disk space statistics after old files removing"
df -h
