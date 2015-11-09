#!/bin/bash

if [[ "$1" == "con" ]]; then
 runned=$(docker ps -a | grep osll/geomongo)
 echo -e "containers"
 echo -e "${runned}"
 exit 0
elif [[ "$1" == "kill" ]]; then
 kill=$(docker rm -f $2 2>&1)
 if [[ $kill =~ "Error" || $kill =~ "rm" ]]; then
  echo -e "Error"
  echo -e "${kill}"
  exit 1
 else
  echo -e "Stoped $2"
  exit 0
 fi
elif [[ "$1" == "tunit" ]]; then
 docker exec -t $2 /app/scripts/run_unittests.sh
 exit $?
elif [[ "$1" == "tint" ]]; then
 docker exec -t $2 /app/scripts/run_integration_tests.sh
 exit $?
elif [[ "$1" == "tsel" ]]; then
 docker exec -t $2 /app/scripts/run_docker_selenium_tests.sh
 exit $?
elif [[ "$1" == "clear" ]]; then
 docker exec -t $2 chmod 777 -R src/*
 exit $?
else
 echo -e $"$0 [con] for containers list"
 echo -e $"$0 [kill %container_name%] stop container"
 echo -e $"$0 [tunit %container_name%] unit tests container"
 echo -e $"$0 [tint %container_name%] integration tests container"
 echo -e $"$0 [tsel %container_name%] selenium tests container"
 exit 0
fi
