outputs = ['_MOSChannelWidth', '_MOSChannellength', '_MOSNumberofGate', '_MOSDummy']

import pickle
import pathlib
cfw = pathlib.Path(__file__).parent.resolve()
ms_file = cfw / 'ms.pkl'
with open(ms_file, 'rb') as f:
    ms_dicts = pickle.load(f)

scales = ['height', 'width', None, None]