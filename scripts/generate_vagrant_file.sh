#!/bin/bash

MEMORY=$1
CPUS=$2
BOX=$3
URL=$4
HD=$5
SOURCE=$6

cd vagrant
cp Vagrantfile.template Vagrantfile
sed -i -e 's/MEMORY/'"$MEMORY"'/g' -e 's/CPUS/'"$CPUS"'/g' -e 's/BOX/''"$BOX"''/g' -e 's|URL|''"$URL"''|g' -e 's/HD/''"$HD"''/g' -e 's|SOURCE|'"$SOURCE"'|g' Vagrantfile
