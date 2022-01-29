#!/bin/sh

iterator=100
populations=10000
generations=900
weight=5000
while [ "$iterator" -le 500 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        python3 size_test_rep_two.py -p parameters.json -w $weight -s $iterator -n 1 -pop $populations -g $generations
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 50`
done