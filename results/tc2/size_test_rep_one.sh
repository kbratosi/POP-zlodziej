#!/bin/sh

iterator=100
populations=2000
generations=180
weight=1000
while [ "$iterator" -le 500 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        python3 size_test_rep_one.py -p parameters.json -w $weight -s $iterator -n 1 -pop $populations -g $generations
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 50`
done