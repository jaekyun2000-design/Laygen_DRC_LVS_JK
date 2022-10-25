import user_setup
import sys, os
import numpy as np

import sys
from intervaltree import IntervalTree

sys.path.append('../mAP/mAP')
ground_truth_path = './object_detection/gt'
prediction_path = './object_detection/prediction'


if 'DL_DETECTION' in user_setup.__dir__() and user_setup.DL_DETECTION and True:
    #add path
    project_path = '/Users/sun/Library/CloudStorage/GoogleDrive-sun9uu@gmail.com/내 드라이브/object_detection_data'
    model_dir = f'{project_path}/model/Hydra3head_10k'
    hydra = 2
    sys.path.append(project_path)
    # import laytina_py2 as laytina_py
    # import laytina_py2 as laytina_py
    # import hydra_laytina_py2 as laytina_py
    import hydra2nd_laytina_py2 as laytina_py
    # import laytina_py3 as laytina_py
    import pickle
    import tensorflow as tf

    with open(f'{model_dir}/class_list.bin', 'rb') as f:
        class_list = pickle.load(f)
    with open(f'{model_dir}/layer_list.bin', 'rb') as f:
        layer_list = pickle.load(f)
    if hydra >=2:
        with open(f'{model_dir}/via_class_list.bin', 'rb') as f:
            via_class_list = pickle.load(f)
        n3 = len(via_class_list)
    n1 = len(class_list)
    n2 = 1

    # layer_list = ['METAL1', 'METAL2', 'METAL3', 'METAL4', 'METAL5', 'METAL6', 'METAL7', 'NWELL', 'DIFF', 'POLY', 'PRES',
    #               'CONT', 'VIA12', 'VIA23', 'VIA34', 'VIA45', 'VIA56', 'VIA67', 'PIMP', 'OP']

    backbone = laytina_py.get_backbone(layer_list)
    if hydra <= 1:
        model = laytina_py.RetinaNet(len(class_list), backbone)
    elif hydra >= 2:
        model = laytina_py.RetinaNet(len(class_list), num_via_classes=len(via_class_list), backbone= backbone)

    latest_checkpoint = tf.train.latest_checkpoint(model_dir)
    model.load_weights(latest_checkpoint)
    image = tf.keras.Input(shape=[None, None, len(layer_list)], name='image')
    predictions = model(image, training=False)
    # if hydra >=1:
    #     detections_array = laytina_py.DecodePredictions(confidence_threshold=0.5)(image, predictions[:, :, -5:])
    #     inference_model_array = tf.keras.Model(inputs=image, outputs=detections_array)
    #     predictions = predictions[:, :, :-5]
    # detections = laytina_py.DecodePredictions(confidence_threshold=0.5)(image, predictions)
    # inference_model = tf.keras.Model(inputs=image, outputs=detections)
    predictions_1st = predictions[:, :, :4 + n1]
    detections = laytina_py.DecodePredictions(confidence_threshold=0.5, num_classes=len(class_list))(image,
                                                                                                     predictions_1st)
    inference_model = tf.keras.Model(inputs=image, outputs=detections)
    if hydra >= 1:
        predictions_2nd = predictions[:, :, 4 + n1: 8 + n1 + n2]
        detections_2nd = laytina_py.DecodePredictions(confidence_threshold=0.5, num_classes=1)(image, predictions_2nd)
        inference_model_2nd = tf.keras.Model(inputs=image, outputs=detections_2nd)
    if hydra >= 2:
        # predictions_3rd = predictions[:,:,8+n1+n2: 12+n1+n2+n3]
        predictions_3rd = predictions[:, :, 8 + n1 + n2:]
        detections_3rd = laytina_py.DecodePredictions(confidence_threshold=0.5, num_classes=len(via_class_list))(image,
                                                                                                                 predictions_3rd)
        inference_model_3rd = tf.keras.Model(inputs=image, outputs=detections_3rd)

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

def inference(matrix_reader=None, input_image=None, image_shape=None, ratio=None, oneshot_mAP_f=True):

    if matrix_reader:
        stacked_matrix, image_shape, ratio = transform_to_inf(matrix_reader)
        input_image = tf.expand_dims(stacked_matrix, axis=0)

    # print(stacked_matrix.shape)
    # print(image_shape)
    # print(stacked_matrix.shape[0]/ratio, stacked_matrix.shape[1]/ratio)
    # print(image_shape[0]/ratio, image_shape[1]/ratio)
    # input_image, ratio = laytina_py.prepare_image(stacked_matrix)
    detections = inference_model.predict(input_image)
    num_detections = detections.valid_detections[0]
    class_names = [
        laytina_py.int2str(int(x), class_list) for x in detections.nmsed_classes[0][:num_detections]
    ]

    prediction_boxes = detections.nmsed_boxes[0][:num_detections]
    prediction_scores = detections.nmsed_scores[0][:num_detections]

    if hydra >=1:
        detections_array = inference_model_2nd.predict(input_image)
        num_detections_array = detections_array.valid_detections[0]

        class_names.extend(['boundary_array']*num_detections_array)
        prediction_boxes = tf.concat([prediction_boxes, detections_array.nmsed_boxes[0][:num_detections_array]], axis=0)
        prediction_scores = tf.concat([prediction_scores, detections_array.nmsed_scores[0][:num_detections_array]], axis=0)
        num_detections += num_detections_array
    if hydra >=2:
        via_detections = inference_model_3rd.predict(input_image)
        num_detections = via_detections.valid_detections[0]
        class_names.extend([via_class_list[int(x)] for x in via_detections.nmsed_classes[0][:num_detections]])
        prediction_boxes = tf.concat([prediction_boxes, via_detections.nmsed_boxes[0][:num_detections]], axis=0)
        prediction_scores = tf.concat([prediction_scores, via_detections.nmsed_scores[0][:num_detections]], axis=0)


    laytina_py.visualize_detections(
        input_image[0,:],
        prediction_boxes,
        class_names,
        prediction_scores,
    )



    if oneshot_mAP_f:

        final_shape = input_image.shape
        export_inference(detections, num_detections, ratio)
        oneshot_mAP()
    else:
        return detections, num_detections

def inference_by_proprocessing(matrix_reader):
    prediction_boxes = []
    prediction_scores = []
    class_names = []
    for dat_and_offset in matrix_reader.divide_matrix(2):
        dat = dat_and_offset[0]
        offset = dat_and_offset[1]
        stacked_matrix,image_shape, ratio =transform_to_inf(dat=dat)
        input_image=tf.expand_dims(stacked_matrix, 0)
        detections, num_detections = inference(input_image=input_image, ratio=ratio, oneshot_mAP_f=False)
        tmp_boxes = detections.nmsed_boxes[0][:num_detections]
        tmp_boxes[:, 0] += offset[0]
        tmp_boxes[:, 1] += offset[1]
        tmp_boxes[:, 2] += offset[0]
        tmp_boxes[:, 3] += offset[1]
        prediction_boxes.extend(tmp_boxes)
        prediction_scores.extend(detections.nmsed_scores[0][:num_detections])
        class_names.extend([class_list[int(x)] for x in detections.nmsed_classes[0][:num_detections]])
    prediction_boxes, prediction_scores, class_names= merge_box(prediction_boxes, prediction_scores, class_names)
    export_inference(prediction_boxes=prediction_boxes, prediction_scores=prediction_scores, class_names=class_names, ratio=ratio)
    oneshot_mAP()
def export_inference(detections=None, num_detections=None, ratio=None, prediction_boxes=None, prediction_scores=None, class_names=None):
    prediction_boxes = detections.nmsed_boxes[0][:num_detections] if prediction_boxes == None else prediction_boxes
    prediction_scores = detections.nmsed_scores[0][:num_detections] if prediction_scores == None else prediction_scores
    class_names = [class_list[int(x)] for x in detections.nmsed_classes[0][:num_detections]] if class_names==None else class_names
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

def merge_box(prediction_boxes, prediction_scores, class_names):
    box_tree = BoxTree(direction='hor')
    for i, box in enumerate(prediction_boxes):
        box_tree.add_box(box, i)
    remove_idx = []
    for i, box in enumerate(prediction_boxes):
        dup_boxes = box_tree.search_intersection(box)
        for dup_box in dup_boxes:
            dbox, idx = dup_box.data[0], dup_box.data[1]
            if i == idx:
                continue
            if class_names[i] == class_names[idx]:
                if box_tree.enclosure_check(box, dbox)  and prediction_scores[i] > 0.8:
                    remove_idx.append(idx)
    # return list without specific idx
    prediction_boxes_after = [box for i, box in enumerate(prediction_boxes) if i not in remove_idx]
    prediction_scores_after = [score for i, score in enumerate(prediction_scores) if i not in remove_idx]
    class_names_after = [name for i, name in enumerate(class_names) if i not in remove_idx]
    return prediction_boxes_after, prediction_scores_after, class_names_after


def oneshot_mAP():
    os.system(f'python ../mAP/mAP/main_mAP.py "{os.path.abspath(prediction_path)}" "{os.path.abspath(ground_truth_path)}"')


class BoxTree(IntervalTree):
    def __init__(self, intervals=None, direction='hor'):
        super(BoxTree, self).__init__(intervals)
        self.direction = direction

    def add_box(self,box, idx):
        if self.direction == 'hor':
            lo, hi = float(box[0]), float(box[2])
            self.addi(lo, hi, (box,idx))
        else:
            lo, hi = float(box[1]), float(box[3])
            self.addi(lo, hi, (box,idx))

    def search_intersection(self, box):
        if self.direction == 'hor':
            tmp_tree = BoxTree(direction='ver')
            for intersected_box in sorted(self[float(box[0]): float(box[2])]):
                tmp_tree.add_box(intersected_box.data[0], intersected_box.data[1])
            intersection = sorted(tmp_tree[float(box[1]):float(box[3])])
        else:
            intersection = sorted(self[float(box[1]): float(box[3])])
        return intersection

    def enclosure_check(self, box1, box2):
        # if box1 enclude box2 then return True
        # 0 -> a < b,  1 -> a < b , 2 -> a > b, 3 -> a > b
        if box1[0] <= box2[0] and box1[1] <= box2[1] and box1[2] >= box2[2] and box1[3] >= box2[3]:
            return True
        else:
            return False