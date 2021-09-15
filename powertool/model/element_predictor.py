from powertool.model.layer_to_matrix import LayerToMatrix
from keras import models, layers
import numpy as np
import user_setup
import os
import tensorflow

def create_element_detector_model():
    return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/cell_detection')

model = None