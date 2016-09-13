# ogr2osm translation for Canvec 2016

This is a translation file that will let [ogr2osm](https://wiki.openstreetmap.org/wiki/Ogr2osm) convert Canvec road segment shapefiles to OSM XML which you can load into JOSM.

The Canvec files this is tested with can be found [here](http://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/canvec/shp/Transport/). Only the 50k scale files have been tested. These are the ones tha start with `canvec_50k` :) These ZIP files contain a directory with many SHP files. The ones that start with `road_segment` are the ones this translation operates on. There may be more than one if there are disjoint networks in a Province.

The process is as follows:
* Download one of the 50k scale file packages from [the FTP site](http://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/canvec/shp/Transport/).
* Unzip
* Enter the resulting directory
* Locate a `road_segment_*.shp` file and note the path
* Install ogr2osm from [Paul Norman's repository](https://github.com/pnorman/ogr2osm)
* Download `canvec.py` from this repository.
* Run the translation: `/path/to/ogr2osm.py -t /path/to/canvec.py /path/to/road_segment_x.shp

Depending on the size of the shapefile and the machine you run it on, this will take a (long) while. The resulting OSM XML file can be loaded into JOSM or processed further with osmosis, etc. 

If you want to improve on this translation, please clone this repo and submit pull requests. If you don't know how that works, email me and I will help.
