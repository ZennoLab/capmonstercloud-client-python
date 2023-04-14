#!/bin/bash

for var in $(ls `pwd`/test)
do
if [[ $var =~ .*test.py.* ]]; then
    echo " run ---->> $var "
    python3 "`pwd`/test/$var"
else
    echo " miss --->> $var" 
fi
done