outputs = ['_NMOSChannelWidth', '_NMOSChannellength', '_NMOSNumberofGate', '_NMOSDummy']

import pickle
import pathlib
cfw = pathlib.Path(__file__).parent.resolve()
ms_file = cfw / 'ms.pkl'
with open(ms_file, 'rb') as f:
    ms_dicts = pickle.load(f)
# ms_dicts = [dict(mean=0.3340751191994302, std=0.05648022750565867),
#             dict(mean=0.03390469042325812, std=0.030330695714379165),
#             dict(mean=10.266, std=5.725231087039195),
#             None]
# ms_dicts = data

scales = ['height', 'width', None, None]