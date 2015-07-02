#!/bin/bash

if [[ "$1" == "con" ]]; then
 runed=$(docker ps | grep osll/geomongo)
 exited=$(docker ps -l | grep osll/geomongo)
 echo -e "Running containers"
 echo -e "${runed}"
 echo -e "Exited containers"
 echo -e "${exited}"

elif [[ "$1" == "kill" ]]; then
 kill=$(docker rm -f $2 2>&1)
 if [[ $kill =~ "Error" || $kill =~ "rm" ]]; then
  echo -e "Error"
  echo -e "${kill}"
 else
  echo -e "Stoped $2"
 fi
else
 echo -e $"$0 [con] for containers list"
 echo -e $"$0 [kill %container_name%] stop container"
fi
