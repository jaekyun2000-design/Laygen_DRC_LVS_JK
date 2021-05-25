_Technology='065nm'
DEBUG = True

import os.path

if os.path.exists('./powertool/topAPI.py'):
    GDS2GEN = True
else:
    GDS2GEN = False
