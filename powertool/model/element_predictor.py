import user_setup
if user_setup.DL_FEATURE or user_setup.DDL_FEATURE:
    from powertool.model.layer_to_matrix import LayerToMatrix
    from keras import models, layers
    import numpy as np
    import os
    import tensorflow

def create_element_detector_model():
    if user_setup.matrix_x_step == 128:
        if user_setup._Technology == 'TSMC65nm':
            # return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/cell_detection')
            return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/128_model')
        elif user_setup._Technology == 'SS28nm':
            # return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/small_dataset_model_keras')
            # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/100_dataset_model_size2')
            # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/1000_dataset_model_size1_6M')
            return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/128_model')
            # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/100_dataset_220418_100x100_keras')
    elif user_setup.matrix_x_step == 100:
        # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/100_dataset_220418_100x100_keras')
        return tensorflow.keras.models.load_model('powertool/dl_models/ss28/1000_dataset_220418_100x100_keras')
        # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/500_dataset_100b100_keras')
    else:
        # return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/cell_detection_256')
        if user_setup._Technology == 'TSMC65nm':
            return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/small_dataset_model_keras')
        # elif user_setup._Technology == 'SS28nm':
        #     return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/small_dataset_model_keras')
            # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/100_dataset_model_size2_keras')


model = None