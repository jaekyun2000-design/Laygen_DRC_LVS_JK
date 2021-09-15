import tensorflow

from powertool.model.layer_to_matrix import LayerToMatrix
from keras import models, layers
import numpy as np
import user_setup
import os

nmos_model = tensorflow.keras.models.load_model('powertool/dl_models/nmos_tsmc65')