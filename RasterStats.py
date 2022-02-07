# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:41:54 2022
@author: mwooten3

Given a geopandas dataframe, raster, and label/stats dictionary (optional),
    return dataframe with the stats, appended or otherwise


Cribbed RasterStats name from rasterstats package because it's the only thing 
    that really makes sense
    - https://github.com/perrygeo/python-rasterstats
    - This code mainly wraps around rasterstats package but does a few extra
      things to return a nice geopandas dataframe rather than dict/etc
    - Also adds some methods/options for writing to .csv/.shp
    



"""

