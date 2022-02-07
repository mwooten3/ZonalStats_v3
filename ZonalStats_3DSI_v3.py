# -*- coding: utf-8 -*-
"""
Created on Fri Dec 3 10:53:09 2021
@author: mwooten3

Another redo of Zonal Stats for ATL08 v5, using Geopandas and .h5 files 
rather tham converting .h5 to .csv to .shp and making large .gdb

Call this ZonalStats_3DSI_v3.py to differentiate from previous iterations of ZS

PROCESS - still TBD:
    - 

Thoughts:
    - Classes ? Still use RasterStack.py, prob no need for ZFC.py. 
    - New classes?: ATL08 shot (attributes from cols, method convert to polygon); GPD DF?
    
Example call for one stack:
    python ZonalStats_3DSI_v3.py -r /att/gpfsfs/briskfs01/ppl/pmontesa/userfs02/projects/3dsi/stacks/zonal_gliht/AK_20180703_Kenai_FHP5/AK_20180703_Kenai_FHP5_stack.vrt 
    -z /att/gpfsfs/briskfs01/ppl/mwooten3/3DSI/ATL08_v005/extracted -o /att/gpfsfs/briskfs01/ppl/mwooten3/3DSI/ZonalStats_v3/ATL08-v5__GLiHT__ZonalStats.csv
    -mode polygon -log

Results will be appended to bigOutput (.csv, .shp, database*)
And also saved as .csv (or .shp) individually

"""
import os, sys
import numpy as np
import argparse
import pandas as pd
import time
import platform

from osgeo import ogr#gdal, osr#, ogr
#from osgeo.osr import SpatialReference
#from osgeo.osr import CoordinateTransformation

from rasterstats import zonal_stats

from RasterStack import RasterStack
from ZonalFeatureClass import ZonalFeatureClass

#* May move to ZDF
# Given a directory to input zonal .csv/.shp's~, and stack extent/projection,
# build a geodataframe of ATL08 shots - include all input attributes at this point
def buildZonalDataFrame(inZonalDir, stackExtent, stackEpsg):
    import pdb; pdb.set_trace()
    # Create shape from extent:
    #extentPoly = 
    
    # Makes sense to reproject shape to lat/lon since ATL08 .csv geometry is lat/lon
    
    # Find ATL08 files that intersect shape:
    
    # Iterate over them and read into gdf
    
    # But only read points whose lat/lon is within extent
    
    return zdf

    
    
    
    
    
# Not sure about this    
def checkZdfResults(zdf, activity):

    #print("\nZonal feature class after {}: {}".format(activity, zfc.filePath))

    if zdf.empty:
        print("\nThere were 0 features after {}. Exiting ({})".format(activity, time.strftime("%m-%d-%y %I:%M:%S")))
        return None

    print(" n features now = {}".format(len(zdf.index)))
    return 'continue'


#* Might move this to ZDF if it makes sense
def getZonalType(inZonalDir):
        
    if 'ATL08_v005' in inZonalDir: 
        zonalType = 'ATL08-v5'
    elif 'GLAS;' in inZonalDir: #?  
        zonalType = 'GLAS'
    else:
        print("Zonal type could not be determined from {}".format(inZonalDir))
        return None
    
    return zonalType

#* Need a better logging method!
def logOutput(logfile, mode):

    sys.stdout = open(logfile, mode)

    return sys.stdout

# Arguments: input stack, zonal .csv directory, polygon or point?, 
# output stats dir, output big .csv/db
    
def main():

    region = 'EU' # or NA (default) still TBD about splitting into regions or not
    
    ogr.UseExceptions() # Unsure about this, but pretty sure we want errors to cause exceptions
    # "export CPL_LOG=/dev/null" -- to hide warnings, must be set from shell or in bashrc

    # Start clock
    start = time.time()
    
    # Set main directory:
    baseDir = '/att/gpfsfs/briskfs01/ppl/mwooten3/3DSI/ZonalStats_v3/'
    #if region == 'EU': baseDir = os.path.join(baseDir, 'EU')

    # Unpack arguments   
    inRaster  = args['rasterStack']
    inZonalDir = args['zonalDir']
    bigOutput = args['bigOutput']
    logOut    = args['logOutput']
    
    stack   = RasterStack(inRaster)
    #inZones = ZonalFeatureClass(inZonalFc)

    # Set some variables from inputs
    stackExtent = stack.extent()
    stackEpsg   = stack.epsg()
    stackName   = stack.stackName

    # Get the output directory
    # outDir = baseDir / zonalType (ATL08_na or GLAS_buff30m) --> stackType / stackName
    zonalType = getZonalType(inZonalDir)
    outDir    = stack.outDir(os.path.join(baseDir, zonalType))
    
    # Create directory where output is supposed to go:
    os.system('mkdir -p {}'.format(os.path.dirname(bigOutput)))

    # Stack-specific outputs
    stackCsv = os.path.join(outDir, '{}__{}__zonalStats.csv'.format(zonalType, stackName))
    #stackShp = stackCsv.replace('.csv', '.shp') - done in RasterStats.py
    
    # Start stack-specific log if doing so
    if logOut: 
        logFile = stackCsv.replace('.csv', '__Log.txt')

        sys.stdout = logOutput(logFile, mode = "a")
        sys.stdout.flush()
        
    # print some info
    print("BEGIN: {}\n".format(time.strftime("%m-%d-%y %I:%M:%S")))
    print("Input zonal directory: {}".format(inZonalDir))
    print("Input raster stack: {}".format(inRaster))
    print("Output stack .csv: {}".format(stackCsv))
    print("Output aggregate .csv/.shp: {}".format(bigOutput))
    print(" n layers = {}".format(stack.nLayers))
    
    # inZones will be the ATL08(/GLAS?) geodataframe, not shapefile
    # for now, do everything in here. May eventually move logic to ZDF.py
    # Given a directory of files
    inZones = buildZonalDataFrame(inZonalDir, stackExtent, stackEpsg)

    #* INSERT FILTERING LOGIC?
    
    # Get stack log and map to stats/labels dict

# Build ATL08/zonal GDF using extent and zonal dir
    # Add ATL08 name field - actually its granule_name yeah?
# Filtering GDF:
    # Option for additional attribute filtering
    # ??? Maybe ??? Remove rows with unique IDs that are already in output .csv/db??
    # Convert geometry to EPSG of stack? - may need to wait on polygon step, but likely not

# Zonal Stats:
# If point option: send GDF, stack, and labels/stats dict to PointQuery
# If polygon option: convert points into polygons and send GDF, stack, and labels/stats dict to Zonal Stats
    
# Other possible args: include df attributes, write to .csv/.shp/db?
    
# Return a dataframe from zonal stats
    
# Add any other fields 
    
# Append dataframe to output .csv/db/whatever 
    return
    
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rasterStack", type=str, required=True, help="Input raster stack")
    parser.add_argument("-z", "--zonalDir", type=str, required=True, help="Directory to input zonal .csv files")
    parser.add_argument("-o", "--bigOutput", type=str, required=True, help="Output for all stacks. Must be a .csv file, .gdb/.shp, or database (coming soon)")
    parser.add_argument("-log", "--logOutput", action='store_true', help="Log the output")
    parser.add_argument("-mode", "--statsMode", type=str, required=True, help="'polygon' for zonal stats (default??) or 'point' for point query")
    
    args = vars(parser.parse_args())

    main(args)