# README #

## Как подготовить среду  ##
Для ubuntu 14.04

sudo apt-get install mongodb python-pip python-dev git apache2 libapache2-mod-wsgi
git clone git@bitbucket.org:osll/geomongo.git

## Как локально развертывать ##

sudo ./scripts/local_deploy.sh

## Как проверить, что все развернулось ##

Выполнение команды
curl http://geomongo/instance/status

должно вернуть 
```
#!python

"OK"
```