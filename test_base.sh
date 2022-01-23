#!/bin/sh

# iterator=1000

# weight=0
# size=0
# populations=2000
# generations=200
# crossover=0.0
# mutation=0.0
while [ "$iterator" -le 10000 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        python3 test_run.py -p parameters.json -n 1
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 1000`
done