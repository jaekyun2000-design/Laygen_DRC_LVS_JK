import tensorflow

from powertool.model.layer_to_matrix import LayerToMatrix
from keras import models, layers
import numpy as np
import user_setup
import os

def convert_org_value(predict, ms=None, scale=None, cell_size=None):
    def inverse(k, mean, std):
        return k*std + mean

    if ms:
        result = inverse(predict,**ms).flatten()
    else:
        result = predict.flatten()

    if scale:
        if not cell_size:
            raise Exception('No information about cell size!')
        result = np.multiply(result,cell_size[scale])
    result = np.rint(result).astype(np.int64)
    return result

def transform_outputs(predict_list, cell_size=None, model=None ):
    import powertool.dl_models.nmos_tsmc65.info as info
    output_dict = dict()
    for i, output in enumerate(info.outputs):
        predict = predict_list[i]
        ms = info.ms_dicts[i]
        scale = info.scales[i]
        output_dict[output] = convert_org_value(predict, ms, scale, cell_size)
    return output_dict

nmos_model = tensorflow.keras.models.load_model('powertool/dl_models/nmos_tsmc65')