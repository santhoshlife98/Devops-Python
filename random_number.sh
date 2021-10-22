#!/bin/bash

if [[ -f inputdata ]]; then
  rm -rf inputdata
  for i in {0..9}
  do
    echo $i, $((RANDOM%100+50)) >> inputdata
  done
fi
