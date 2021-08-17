_Technology='TSMC65nm'
_Night_mode = True
DEBUG = True
MIN_SNAP_SPACING = 5

import os.path

if os.path.exists('./powertool/topAPI.py'):
    GDS2GEN = True
else:
    GDS2GEN = False
