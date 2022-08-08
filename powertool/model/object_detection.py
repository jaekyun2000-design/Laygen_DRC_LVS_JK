import user_setup
import sys, os
import numpy as np


if 'DL_DETECTION' in user_setup.__dir__() and user_setup.DL_DETECTION and True:
    #add path
    project_path = '/Users/sun/Library/CloudStorage/GoogleDrive-sun9uu@gmail.com/내 드라이브/object_detection_data'
    sys.path.append(project_path)
    import laytina_py
    import pickle
    import tensorflow as tf

    with open(f'{project_path}/class_list.bin', 'rb') as f:
        class_list = pickle.load(f)
    layer_list = ['METAL1', 'METAL2', 'METAL3', 'METAL4', 'METAL5', 'METAL6', 'CONT', 'DIFF', 'POLY', 'PIMP']

    model_dir = './model/laytinanet_2nd_training'
    backbone = laytina_py.get_backbone()
    model = laytina_py.RetinaNet(len(class_list), backbone)

    latest_checkpoint = tf.train.latest_checkpoint(model_dir)
    model.load_weights(latest_checkpoint)
    image = tf.keras.Input(shape=[None, None, len(layer_list)], name='image')
    predictions = model(image, training=False)
    detections = laytina_py.DecodePredictions(confidence_threshold=0.5)(image, predictions)
    inference_model = tf.keras.Model(inputs=image, outputs=detections)

    # laytina_py.inf(inference_model, 10)

def transform_to_inf(matrix_reader):
    stacked_matrix = None
    dat = matrix_reader.matrix_by_layer
    shape = list(dat.values())[0].shape
    layer_list = ['METAL1', 'METAL2', 'METAL3', 'METAL4', 'METAL5', 'METAL6', 'CONT', 'DIFF', 'POLY', 'PIMP']
    for layer in layer_list:
        layer = layer.decode('ascii') if type(layer) == bytes else layer
        layer_mat = dat[layer] if layer in list(dat.keys()) else np.zeros(shape)
        if type(stacked_matrix) == np.ndarray:
            stacked_matrix = np.append(stacked_matrix, np.expand_dims(layer_mat, 2), axis=2)
        else:
            stacked_matrix = np.expand_dims(layer_mat, 2)
    # bbox = dat.item()['matrix']
    # label = dat.item()['label']
    stacked_matrix, image_shape, ratio = laytina_py.resize_and_pad_image(stacked_matrix)
    return stacked_matrix, image_shape, ratio

def inference(matrix_reader):
    stacked_matrix, image_shape, ratio = transform_to_inf(matrix_reader)
    input_image, ratio = laytina_py.prepare_image(stacked_matrix)
    detections = inference_model.predict(input_image)
    num_detections = detections.valid_detections[0]
    class_names = [
        laytina_py.int2str(int(x)) for x in detections.nmsed_classes[0][:num_detections]
    ]
    laytina_py.visualize_detections(
        stacked_matrix,
        detections.nmsed_boxes[0][:num_detections] / ratio,
        class_names,
        detections.nmsed_scores[0][:num_detections],
    )