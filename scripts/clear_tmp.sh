#!/bin/bash
df -h
LIST=`find /tmp -mtime +7 -print0 -name 'tmp*' -exec rm -fr "{}" \;`
#echo $LIST | sed 's/\r/ /g' | wc -c
df -h
