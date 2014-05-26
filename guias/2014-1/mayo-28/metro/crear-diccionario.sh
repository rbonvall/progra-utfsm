#!/bin/bash

while read URL
do
  ARTICLE=$(mktemp)
  wget "$URL" -O $ARTICLE
  TITLE=$(grep '<title>' $ARTICLE | perl -pe 's/<title>(.*) \(.*/\1/')
  COORDS=$(grep 'Coordenadas_geo' $ARTICLE)
  LAT=$(perl -pe 's!.*<span class="latitude">(.*?),</span>.*!\1!' <<< $COORDS)
  LON=$(perl -pe 's!.*<span class="longitude">(.*?)</span>.*!\1!' <<< $COORDS)
  echo "  '$TITLE': ($LAT, $LON),"
  rm $ARTICLE
done < articulos-estaciones.txt
