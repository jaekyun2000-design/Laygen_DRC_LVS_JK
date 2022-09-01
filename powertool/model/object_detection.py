import user_setup
import sys, os
import numpy as np

import sys

sys.path.append('../mAP/mAP')
ground_truth_path = './object_detection/gt'
prediction_path = './object_detection/prediction'


if 'DL_DETECTION' in user_setup.__dir__() and user_setup.DL_DETECTION and True:
    #add path
    project_path = '/Users/sun/Library/CloudStorage/GoogleDrive-sun9uu@gmail.com/내 드라이브/object_detection_data'
    model_dir = f'{project_path}/model/class3a_mid_laytina2'
    sys.path.append(project_path)
    # import laytina_py2 as laytina_py
    import laytina_py2 as laytina_py
    # import laytina_py3 as laytina_py
    import pickle
    import tensorflow as tf

    with open(f'{model_dir}/class_list.bin', 'rb') as f:
        class_list = pickle.load(f)
    with open(f'{model_dir}/layer_list.bin', 'rb') as f:
        layer_list = pickle.load(f)
    # layer_list = ['METAL1', 'METAL2', 'METAL3', 'METAL4', 'METAL5', 'METAL6', 'METAL7', 'NWELL', 'DIFF', 'POLY', 'PRES',
    #               'CONT', 'VIA12', 'VIA23', 'VIA34', 'VIA45', 'VIA56', 'VIA67', 'PIMP', 'OP']

    backbone = laytina_py.get_backbone(layer_list)
    model = laytina_py.RetinaNet(len(class_list), backbone)

    latest_checkpoint = tf.train.latest_checkpoint(model_dir)
    model.load_weights(latest_checkpoint)
    image = tf.keras.Input(shape=[None, None, len(layer_list)], name='image')
    predictions = model(image, training=False)
    detections = laytina_py.DecodePredictions(confidence_threshold=0.5)(image, predictions)
    inference_model = tf.keras.Model(inputs=image, outputs=detections)

    # laytina_py.inf(inference_model, 10)
def prepare_image(image):
    image, _, ratio = laytina_py.resize_and_pad_image(image, jitter=None)
    return tf.expand_dims(image, 0), ratio

def transform_to_inf(matrix_reader=None, dat=None):
    stacked_matrix = None
    if dat == None:
        dat = matrix_reader.matrix_by_layer

    shape = list(dat.values())[0].shape
    # layer_list = ['METAL1', 'METAL2', 'METAL3', 'METAL4', 'METAL5', 'METAL6', 'CONT', 'DIFF', 'POLY', 'PIMP']
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
#
# def transform_to_inf_by_proprocessing(matrix_reader, divider_factor=2):
#     stacked_matrix = None
#     dat = matrix_reader.matrix_by_layer
#     for dat in matrix_reader.divide_matrix(divider_factor):
#         transform_to_inf(dat=dat)
#

def inference(matrix_reader=None, stacked_matrix=None, image_shape=None, ratio=None):
    print(list(matrix_reader.matrix_by_layer.values())[0].shape)

    if matrix_reader:
        stacked_matrix, image_shape, ratio = transform_to_inf(matrix_reader)
    # print(stacked_matrix.shape)
    # print(image_shape)
    # print(stacked_matrix.shape[0]/ratio, stacked_matrix.shape[1]/ratio)
    # print(image_shape[0]/ratio, image_shape[1]/ratio)
    # input_image, ratio = laytina_py.prepare_image(stacked_matrix)
    input_image = tf.expand_dims(stacked_matrix, axis=0)
    detections = inference_model.predict(input_image)
    num_detections = detections.valid_detections[0]
    class_names = [
        laytina_py.int2str(int(x)) for x in detections.nmsed_classes[0][:num_detections]
    ]
    laytina_py.visualize_detections(
        stacked_matrix,
        detections.nmsed_boxes[0][:num_detections] ,
        class_names,
        detections.nmsed_scores[0][:num_detections],
    )
    final_shape = input_image.shape
    export_inference(detections, num_detections, ratio, image_shape, final_shape)
    oneshot_mAP()

def inference_by_proprocessing(matrix_reader):
    for dat in matrix_reader.divide_matrix(2):
        # print(dat)
        stacked_matrix, image_shape, ratio =transform_to_inf(dat=dat)
        inference(stacked_matrix=stacked_matrix, image_shape=image_shape, ratio=ratio)

def export_inference(detections, num_detections, ratio, image_shape, final_shape):
    # x_ratio = final_shape[1]/image_shape[0] * ratio
    # y_ratio = final_shape[2]/image_shape[1] * ratio
    prediction_boxes = detections.nmsed_boxes[0][:num_detections]
    prediction_scores = detections.nmsed_scores[0][:num_detections]
    class_names = [class_list[int(x)] for x in detections.nmsed_classes[0][:num_detections]]
    # prediction_boxes = prediction_boxes[:image_shape[0], :image_shape[1],:]/ratio
    file = open(f'{prediction_path}/0.txt', 'w')
    for i, box in enumerate(prediction_boxes):
        if prediction_scores[i] >= 0.5:
            print(box)
            print(ratio)
            file.write(f'{class_names[i]} {prediction_scores[i]}'
                       f' {box[0]/ratio*user_setup.min_step_size}'
                       f' {box[1]/ratio*user_setup.min_step_size}'
                       f' {box[2]/ratio*user_setup.min_step_size}'
                       f' {box[3]/ratio*user_setup.min_step_size}\n')
    file.close()

def oneshot_mAP():
    os.system(f'python ../mAP/mAP/main_mAP.py "{os.path.abspath(prediction_path)}" "{os.path.abspath(ground_truth_path)}"')