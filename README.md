# README #

## Как подготовить среду  ##

sudo apt-get install mongodb python-pip python-dev git vim apache2 libapache2-mod-wsgi
git clone git@bitbucket.org:osll/geomongo.git

## Как локально развертывать ##

sudo ./scripts/local_deploy.sh

## Как проверить, что все развернулось ##

Выполнение команды
curl http://geomongo/tags/111

должно вернуть 
```
#!python

{'errno':1}
```