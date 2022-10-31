import user_setup
import sys
import pickle
if user_setup.DL_FEATURE or user_setup.DDL_FEATURE:
    from powertool.model.layer_to_matrix import LayerToMatrix
    from keras import models, layers
    import numpy as np
    import os
    import tensorflow as tf



if user_setup.DL_FEATURE:
    model_dir = user_setup.model_dir
    with open(f'{model_dir}/matrix_size.bin', 'rb') as f:
        matrix_size = pickle.load(f)
    with open(f'{model_dir}/layer_list.bin', 'rb') as f:
        layer_list = pickle.load(f)
    with open(f'{model_dir}/class_list.bin', 'rb') as f:
        data_type_list = pickle.load(f)
    matrix_x_step = matrix_size[0]
    matrix_y_step = matrix_size[1]


    def create_element_detector_model_old():
        if user_setup.matrix_x_step == 128:
            if user_setup._Technology == 'TSMC65nm':
                # return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/cell_detection')
                return tf.keras.models.load_model('powertool/dl_models/tsmc65/128_model')
            elif user_setup._Technology == 'SS28nm':
                # return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/small_dataset_model_keras')
                # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/100_dataset_model_size2')
                # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/1000_dataset_model_size1_6M')
                return tf.keras.models.load_model('powertool/dl_models/tsmc65/128_model')
                # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/100_dataset_220418_100x100_keras')
        elif user_setup.matrix_x_step == 100:
            # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/100_dataset_220418_100x100_keras')
            return tf.keras.models.load_model('powertool/dl_models/ss28/1000_dataset_220418_100x100_keras')
            # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/500_dataset_100b100_keras')
        else:
            # return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/cell_detection_256')
            if user_setup._Technology == 'TSMC65nm':
                return tf.keras.models.load_model('powertool/dl_models/tsmc65/small_dataset_model_keras')
            # elif user_setup._Technology == 'SS28nm':
            #     return tensorflow.keras.models.load_model('powertool/dl_models/tsmc65/small_dataset_model_keras')
                # return tensorflow.keras.models.load_model('powertool/dl_models/ss28/100_dataset_model_size2_keras')

    def create_element_detector_model(model_dir='./powertool/dl_models/ss28/128b_class3a'):
        with open(f'{model_dir}/class_list.bin', 'rb') as f:
            class_list = pickle.load(f)
        with open(f'{model_dir}/matrix_size.bin', 'rb') as f:
            matrix_size = pickle.load(f)
        with open(f'{model_dir}/layer_list.bin', 'rb') as f:
            layer_list = pickle.load(f)
        return create_model(class_list, matrix_size, layer_list, model_dir)

    def create_model(class_list, matrix_size, layer_list, model_dir):
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Conv2D(8, (1, 1), activation='relu', input_shape=(matrix_size[0], matrix_size[1], len(layer_list))))
        model.add(tf.keras.layers.Conv2D(16, (3, 3), activation='relu'))
        model.add(tf.keras.layers.MaxPooling2D((2, 2)))
        model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu'))
        model.add(tf.keras.layers.MaxPooling2D((2, 2)))
        model.add(tf.keras.layers.Conv2D(16, (1, 1), activation='relu'))
        model.add(tf.keras.layers.Dropout(0.4))
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(len(class_list), activation='sigmoid'))
        latest_checkpoint = tf.train.latest_checkpoint(model_dir)
        model.load_weights(latest_checkpoint)
        return model


    model = None
elif user_setup.DDL_FEATURE:
    project_path = '/Users/sun/Library/CloudStorage/GoogleDrive-sun9uu@gmail.com/내 드라이브/object_detection_data/LayCNN'
    model_dir = f'{project_path}/models/100b_t3'
    sys.path.append(project_path)
    import layCNN_model


    with open(f'{model_dir}/matrix_size.bin', 'rb') as f:
        matrix_size = pickle.load(f)
    with open(f'{model_dir}/layer_list.bin', 'rb') as f:
        layer_list = pickle.load(f)
    with open(f'{model_dir}/class_list.bin', 'rb') as f:
        class_list = pickle.load(f)
    model = layCNN_model.get_model(matrix_size, layer_list, len(class_list))

    # latest_checkpoint =