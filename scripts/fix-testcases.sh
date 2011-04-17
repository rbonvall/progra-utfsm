#!/bin/bash

for page in $(find _build -name '*.html')
do
    perl -p -i -e 's{`(.*?)`(</pre>)?$}{<b>\1</b>}g;' $page
done

