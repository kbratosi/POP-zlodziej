#!/bin/sh

iterator=500
generations=180
weight=1000
size=100
while [ "$iterator" -le 5000 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        python3 pop_test_rep_one.py -p parameters.json -s $size -w $weight -n 1 -pop $iterator -g $generations
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 500`
done