Latitude and Longitude of Brazilian Localities
==============================================

This repo downloads geo data for Brazilian localities from IBGE and
converts it to CSV. The resulting file has the latitude, longitude,
and altitude of places in Brazil along with the numeric identifiers
from IBGE.

Usage
-----

1. Download the data using the bash script:

    ./download.sh

2. Convert to CSV using the Python script:

    ./localpoints.py

The `download.sh` file will download everything to a `data/` folder.
The `localpoints.py` file will write a CSV file to an `out/` folder.
