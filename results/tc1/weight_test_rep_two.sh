#!/bin/sh

iterator=1000
populations=10000
generations=900
size=500
while [ "$iterator" -le 10000 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        python3 weight_test_rep_two.py -p parameters.json -s $size -w $iterator -n 1 -pop $populations -g $generations
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 1000`
done