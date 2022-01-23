#!/bin/sh

iterator=50

weight=2500
size=250
populations=5000
while [ "$iterator" -le 500 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        python3 gen_test_rep_two.py -p parameters.json -s $size -w $weight -n 1 -pop $populations -g $iterator
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 50`
done