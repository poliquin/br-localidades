#!/bin/bash

# Download shapefile of Brazilian locations from IBGE for 2010

server="ftp://geoftp.ibge.gov.br/organizacao_territorial/localidades"
opts="-m -N -nd -np -nv --wait=0.5 --random-wait -P data/"

mkdir -p data

wget $opts ${server}/cadastro_localidades_selecionadas.pdf
wget $opts ${server}/descritivo_campos_localidades_2010.xls
wget $opts ${server}/Shapefile_SHP

echo "Finished mirroring localidades shapefiles"
