#!/bin/bash

'''Random Number Generator'''
'''Author Santhosh Bheeman'''

for i in {0..9}
do
  echo $i, $((RANDOM%100+50)) >> inputFile
done
