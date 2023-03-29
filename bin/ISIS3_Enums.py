# Python 3 Enums for ISIS3 Modules

# Import dependencies ==========================================================
from enum import Enum

# Declare variables ============================================================
MOD_PREFIX = 'isis_'

# Declare functions ============================================================
class ISIS_DAGS(Enum):
    def __str__(self):
        return str(self.value)
    
    isis_mroctx2isis = 1
    isis_catlab = 2
    isis_spiceinit = 3
    isis_footprintinit = 4
    isis_caminfo = 5
    isis_ctxcal = 6
    isis_ctxevenodd = 7
    cube_rename = 8
    isis_cam2map = 9
    gdal_translate = 10
