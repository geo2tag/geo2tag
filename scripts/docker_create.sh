#!/bin/bash

red=$(tput setf 4)
green=$(tput setf 2)
reset=$(tput sgr0)
toend=$(tput hpa $(tput cols))$(tput cub 6)

if [[ $# -eq 4 && "$1" == "-p" && "$3" == "-n" ]]; then
 res=$(docker run -d -p $2:80 -v `pwd`/src:/app/src -v `pwd`/scripts:/app/scripts -v `pwd`/config:/app/config -v `pwd`/master_db_template:/app/master_db_template -v `pwd`/testdump:/app/testdump --name $4 osll/geomongo 2>&1)

  if [[ $res =~ "Error" || $res =~ "Invalid" ]]; then
	echo -n "${res}"
	echo -n "${red}${toend}[FAIL]"
  else
	echo -n "$4"
	echo -n "${green}${toend}[OK]"
  fi
else
  echo -n "$0 -p [port] -n [name]"
fi

echo -n "${reset}"
echo
