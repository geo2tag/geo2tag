#!/bin/bash

if [[ "$1" == "con" ]]; then
 runed=$(docker ps | grep osll/geomongo)
 echo -e "containers"
 echo -e "${runed}"

elif [[ "$1" == "kill" ]]; then
 kill=$(docker rm -f $2 2>&1)
 if [[ $kill =~ "Error" || $kill =~ "rm" ]]; then
  echo -e "Error"
  echo -e "${kill}"
 else
  echo -e "Stoped $2"
 fi
elif [[ "$1" == "tunit" ]]; then
 docker exec -t -i $2 /app/scripts/run_unittests.sh
elif [[ "$1" == "tint" ]]; then
 docker exec -t -i $2 /app/scripts/run_integration_tests.sh
else
 echo -e $"$0 [con] for containers list"
 echo -e $"$0 [kill %container_name%] stop container"
 echo -e $"$0 [tunit %container_name%] unit tests container"
 echo -e $"$0 [tint %container_name%] integration tests container"

fi
