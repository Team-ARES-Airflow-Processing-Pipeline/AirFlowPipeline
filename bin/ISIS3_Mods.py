# Python 3 Enums for ISIS3 Modules

# Import dependencies ==========================================================
from enum import Enum

# Declare variables ============================================================
MOD_PREFIX = 'isis_'

# Declare functions ============================================================
class isis_mroctx2isis():
    def __init__():
        self.MODULE_NAME = 'isis.mroctx2isis'
        self.from_ = ''
        self.to = ''

class isis_catlab():
    def __init__():
        self.MODULE_NAME = 'isis.catlab'
        self.from_ = ''
        self.to = ''

class isis_spiceinit():
    def __init__():
        self.MODULE_NAME = 'isis.spiceinit'
        self.from_ = ''
        self.cknadir = ''
        self.cksmithed = ''

class isis_footprintinit():
    def __init__():
        self.MODULE_NAME = 'isis.footprintinit'
        self.from_ = ''
        self.increaseprecision = ''
        self.inctype = ''
        self.numvertices = ''
        self.maxemission = ''
        self.maxincidence = ''

class isis_caminfo():
    def __init__():
        self.MODULE_NAME = 'isis.caminfo'
        self.from_ = ''
        self.to = ''
        self.geometry = ''
        self.isislabel = ''
        self.originallabel = ''
        self.statistics = ''
        self.camstats = ''
        self.linc = ''
        self.sinc = ''
        self.polygon = ''
        self.inctype = ''
        self.increaseprecision = ''
        self.numverticies = ''
        self.maxemission = ''
        self.maxincidence = ''
        self.spice = ''

class isis_ctxcal():
    def __init__():
        self.MODULE_NAME = 'isis.ctxcal'
        self.from_ = ''
        self.to = ''

class isis_ctxevenodd():
    def __init__():
        self.MODULE_NAME = 'isis.ctxevenodd'
        self.from_ = ''
        self.to = ''

class cube_rename():
    def __init__():
        self.MODULE_NAME = 'cube.rename'
        self.src = ''
        self.dest = ''

class isis_cam2map():
    def __init__():
        self.MODULE_NAME = 'isis.cam2map'
        self.from_ = ''
        self.to = ''
        self.map = ''
        self.matchmap = ''
        self.pixres = ''
        self.defaultrange = ''

class gdal_translate():
    def __init__():
        self.MODULE_NAME = 'gdal.translate'
        self.outputType = ''
        self.format = ''
        self.scaleParams = ''
        self.width = ''
        self.height = ''
        self.src = ''
        self.dest = ''
