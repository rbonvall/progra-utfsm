#!/bin/bash

BOOK=_libro

#if [ -e $BOOK ]
#then
#    echo $BOOK ya existe
#    exit
#fi

find -name '*.rst' | while read page
do
    mkdir -p $BOOK/$(dirname $page)
#    rstex.py $page $BOOK/${page%.rst}.tex
    pandoc -t latex $page > $BOOK/${page%.rst}.tex
done



