import user_setup
if user_setup.DL_FEATURE:
    from powertool.model.layer_to_matrix import LayerToMatrix
    from keras import models, layers
    import numpy as np
    import os
    import tensorflow

def create_element_detector_model():
    if user_setup.matrix_x_step == 128:
        return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/cell_detection')
    else:
        return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/cell_detection_256')

model = None