#!/bin/sh

iterator=100
populations=0
generations=0
while [ "$iterator" -le 1000 ]
do 
    repetition=0
    while [ "$repetition" -lt 1 ]
    do
        populations=`expr $iterator \* 8`
        populations=`expr $populations / 10`
        python3 test_run.py -p parameters.json -s $iterator -n 1 -pop $populations
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 100`
done