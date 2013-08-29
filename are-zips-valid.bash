#!/bin/bash

## old
#for file in `grep ".zip\";" $1 | sed 's/[^"]*"\([^"]*\)";.*/\1/g'`; do 
#    ls $file 2> /dev/null > /dev/null; echo $? $file;
#done

## new
files=`sed -ne 's/.*"\(.*\.zip\)".*/\1/p' xmls/EAP6.xml | sort -u`
for file in $files; do 
  ls $file > /dev/null 2> /dev/null; echo "$?   $file";
done
