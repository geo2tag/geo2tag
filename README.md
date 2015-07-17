# README #

## Как подготовить среду  ##
Для ubuntu 12.04

Установить mongodb 2.6.0
https://geo2tag.atlassian.net/wiki/pages/viewpage.action?pageId=38207537
Установить все остальное 
sudo apt-get install python-pip python-dev git vim apache2 libapache2-mod-wsgi

Для ubuntu 14.04

sudo apt-get install mongodb python-pip python-dev git vim apache2 libapache2-mod-wsgi


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
