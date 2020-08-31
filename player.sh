#!/bin/bash

if [[ "x" == "x$1" ]];
then
    echo "Error: you must specify field."
elif [[ "$1" =~ ^(browser_family|os_family|device_family)$ ]]; 
then
    echo "calculating number of unique sessions in each $1"
    python3 session_count.py $1
else
   echo "Error: wrong field to input."
fi
