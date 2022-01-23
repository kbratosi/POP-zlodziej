#!/bin/sh

iterator=0

weight=1000
size=100
populations=2000
generations=180
# crossover=0.0
# mutation=0.0
while [ "$iterator" -le 50 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        python3 mut_test_rep_one.py -p parameters.json -n 1 -w $weight -s $size -pop $populations -g $generations -m $iterator
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 1`
done