# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 02:03:17 2020
@author: mwooten3

# *NOTE*: This version is specific for Zonal Stats version 3, see HRSI
    directory/repo for v2 (ATL08 v003) version code
    
RasterStack describes a raster geoTIFF or VRT with mutliple layers
Inherits from Raster,
With methods designed specifically for 3DSI Zonal Stats process

RasterStack inherits the following from Raster:
    self.filePath; self.extension; self.baseName; self.baseDir; self.dataset
    self.noDataValue; self.ogrDataType; self.ogrGeotransform; self.ogrProjection
    self.nColumns; self.nRows; self.nLayers   
    
    convertExtent(self, targetEpsg)
    epsg(self)
    extent(self)
    extractBand(self, bandN, outTif = None)
    toArray(self) 
"""

import os

from Raster import Raster

#------------------------------------------------------------------------------
# class RasterStack
#------------------------------------------------------------------------------
class RasterStack(Raster):
    
    #--------------------------------------------------------------------------
    # __init__
    #--------------------------------------------------------------------------
    def __init__(self, filePath):
        
        # Initialize the base class
        super(RasterStack, self).__init__(filePath)
        
        """
        # Check that the file is TIF or VRT            
        if self.extension != '.vrt' and self.extension != '.tif':
            raise RuntimeError('{} is not a VRT or TIF file'.format(filePath))
        """
        
        self.stackName = self.baseName.strip('_stack')     

    #--------------------------------------------------------------------------
    # noDataLayer()
    #--------------------------------------------------------------------------
    def noDataLayer(self):
        
        noDataLayer = self.filePath.replace('stack.vrt', 'mask.tif')
        
        if os.path.isfile(noDataLayer):
            return noDataLayer
        
        else:
            return None
        
    #--------------------------------------------------------------------------
    # outDir()
    #--------------------------------------------------------------------------
    def outDir(self, baseDir):

        # zonalStatsDir --> zonalType --> DSM/LVIS/GLiHT --> stackIdentifier
        outDir = os.path.join(baseDir, self.stackType(), self.stackName)
        
        os.system('mkdir -p {}'.format(outDir))
        
        return outDir
        
    #--------------------------------------------------------------------------
    # stackKey()
    #--------------------------------------------------------------------------
    def stackKey(self):
        
        stackKey = self.filePath.replace('.vrt', '_Log.txt')
        
        if os.path.isfile(stackKey):
            return stackKey
        
        else:
            return None
        
    #--------------------------------------------------------------------------
    # stackType()
    #--------------------------------------------------------------------------
    def stackType(self):
        
        # SGM, LVIS, GLiHT, Landsat, Auxiliary
        # only one updated is GLiHT
        
        if 'Out_SGM' in self.baseDir or 'Out_EA' in self.baseDir: # TEMP UNTIL WILL FIXES STACKDIRs
            return 'SGM'
        
        elif 'out_lvis' in self.baseDir:
            return 'LVIS'
        
        elif 'gliht' in self.baseDir:
            return 'GLiHT'
        
        elif 'esta_year' in self.baseDir:
            return 'Landsat'
        
        elif 'TDM1_DEM' in self.baseDir:
            return 'Tandemx'
        
        else:
            return None
        
    #--------------------------------------------------------------------------
    # xmlLayer()
    #--------------------------------------------------------------------------
    def xmlLayer(self):
        
        xmlLayer = self.filePath.replace('_stack.vrt', '.xml')
        
        if os.path.isfile(xmlLayer):
            return xmlLayer
        
        else:
            return None    
        
        