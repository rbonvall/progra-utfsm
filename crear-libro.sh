#!/bin/bash

BOOK=_libro
CHAPTERS=$BOOK/capitulos.tex

rm -rf $CHAPTERS
find materia ejercicios c -name '*.rst' | while read page
do
    mkdir -p $BOOK/$(dirname $page)
    doc=$BOOK/${page%.rst}.tex
    pandoc -t latex --listings $page > $doc
    sed -e '
      /multiplicacion\.gif/ {
        s/^/%/
      }
      /begin{enumerate}/ {
        s/\[.*\]$//
      }
    ' -i $doc
    echo "\\input{${doc#*/}}" >> $CHAPTERS
done



