#!/bin/sh

# iterator=1000
# populations=2000
# generations=200
# weight=0
while [ "$iterator" -le 10000 ]
do 
    repetition=0
    while [ "$repetition" -lt 5 ]
    do
        # populations=`expr $iterator \* 8`
        # populations=`expr $populations / 10`
        python3 test_run.py -p parameters.json -s 100 -w $iterator -n 1
        repetition=`expr  $repetition + 1`
    done
    iterator=`expr $iterator + 1000`
done