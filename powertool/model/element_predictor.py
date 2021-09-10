from powertool.model.layer_to_matrix import LayerToMatrix
from keras import models, layers
import numpy as np
import user_setup
import os

def create_element_detector_model():
    x_size = user_setup.matrix_x_step
    y_size = user_setup.matrix_y_step
    layer_list = user_setup.layer_list
    data_type_list = user_setup.data_type_list


    model = models.Sequential()
    model.add(layers.Conv2D(16,(3,3), activation='relu', input_shape=(x_size,y_size,len(layer_list))))
    model.add(layers.Conv2D(32,(6,6), activation='relu'))
    model.add(layers.Conv2D(32,(6,6), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(len(data_type_list)+1, activation='softmax'))
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    cwd = os.getcwd()
    model_dir = 'powertool/variables/TSMC65/TSMC65_weights'
    weight_file = os.path.join(cwd, model_dir)
    print(weight_file)
    model.load_weights(weight_file)
    return model

model = None