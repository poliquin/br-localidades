#!/usr/bin/env python

import os
import csv
import shapefile

"""
Get information from IBGE shapefile, write data to csv file.
"""

# need an output folder
if not os.path.exists('out'):
    os.mkdir('out')

# files contain a field called "long", which is an invalid name
# in some statistical software (e.g. Stata); this dictionary is
# used for replacing field names.
FIELD_REPL = {
    'long': 'lng',
}

shp = open('data/BR_Localidades_2010_v1.shp', 'rb')
dbf = open('data/BR_Localidades_2010_v1.dbf', 'rb')
shx = open('data/BR_Localidades_2010_v1.shx', 'rb')

# determine field names
rdr = shapefile.Reader(shp=shp, dbf=dbf, shx=shx)
fieldnames = [i[0].lower() for i in rdr.fields[2:]]
fieldnames = [FIELD_REPL[i] if i in FIELD_REPL else i for i in fieldnames]

# convert to csv
with open('out/latlng_local.csv', 'w', encoding='utf-8') as fh:
    wtr = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction='ignore')
    wtr.writeheader()

    for s in rdr.iterShapeRecords():
        rec = (k.decode('iso8859-1').strip() if hasattr(k, 'decode') else k
               for k in s.record[1:])
        wtr.writerow(dict(zip(fieldnames, rec)))

shp.close()
dbf.close()
shx.close()
