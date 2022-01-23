#!/bin/sh

iterator=0

weight=2500
size=250
populations=5000
generations=450
# crossover=0.0
# mutation=0.0
while [ "$iterator" -le 50 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        python3 mut_test_rep_two.py -p parameters.json -n 1 -w $weight -s $size -pop $populations -g $generations -m $iterator
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 1`
done