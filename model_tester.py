import copy
import os
dir_check=os.getcwd()


batch_size = 16

if 'PyQTInterface' in dir_check:
    os.chdir('..')



import sys
import time
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import traceback
import warnings
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

try:
    sys.path.append('./powertool')
    import topAPI
except:
    traceback.print_exc()
    sys.stderr.write("topAPI support failed\n")
    print("GDS2GEN topAPI module does not exist.")

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from powertool.model import element_predictor


from PyCodes import QTInterfaceWithAST

##################
import user_setup
DEBUG = user_setup.DEBUG
subnanoMinimumScale =5 # 5 means(default)
subnanoViewScale = 1  #
minimum_render = 5
                      # 1 means(default): coordinates default unit is 1nm,
                      # 0.1 means: coordinates default unit is 0.1nm
                      # 10 means: coordinates default unit is 10nm
EasyDebugFileName = ''


dl_inference_time = 0
dl_count = 0


def loadGDS( filename=None, false_class=False, only_get_label=False):
    qtproject = QTInterfaceWithAST.QtProject(_name='project')

    if not topAPI.element_predictor.model:
        topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model(user_setup.model_dir)

    _moduleName = filename.replace(".gds", "")
    _moduleName = _moduleName.split('/')[-1]
    print(f"file load: {filename}")
    try:
        qtproject._loadDesignsFromGDSlegacy(_file=filename, _topModuleName=_moduleName, ignore_non_element=True)
    except:
        import collections
        qtproject._DesignParameter = collections.OrderedDict()
        qtproject._loadDesignsFromGDSlegacy(_file=filename, _topModuleName=_moduleName, _reverse=True, ignore_non_element=True)

    entireHierarchy = qtproject._getEntireHierarchy()


    top_cell_name, sub_cell_dict = list(entireHierarchy.items())[0]
    sub_cell_list = [qtproject._DesignParameter[top_cell_name][sub_cell_name.split('/')[-1]]._DesignParameter['_DesignObj'] for sub_cell_name in sub_cell_dict.keys()]
    inference_list = [0] * len(sub_cell_list)
    sub_cell_mat_list = [cell_to_matrix(sub_cell) for sub_cell in sub_cell_list]


    if only_get_label is not True:
        dataset = tf.data.Dataset.from_generator(read_matrix_data,
                                                 (tf.float64),
                                                 (tf.TensorShape([element_predictor.matrix_x_step, element_predictor.matrix_y_step, len(element_predictor.layer_list)])),
                                                 args=(sub_cell_mat_list,))
        dataset = dataset.batch(batch_size)
        # if not topAPI.element_predictor.model:
        #     topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model(user_setup.model_dir)
        result = topAPI.element_predictor.model.predict(dataset)

        positive_check = np.nonzero(np.greater(result, user_setup.DL_threshold))
        for i in range(len(sub_cell_list)):
            if i not in positive_check[0]: # and false_class==False:
                inference_list[i] = 'Negative'
            else:
                # idx = np.where(positive_check[0] == i)[0]
                # prediction_idx = positive_check[1][idx]
                idx = np.argmax(result[i])
                try:
                    inference_list[i] = element_predictor.generator_name_mapping(element_predictor.data_type_list[idx], False)
                except:
                    # print('dbg for original with false class')
                    inference_list[i] = 'Negative'
    else:
        inference_list = None

    sub_cell_name_list = [sub_cell_name.split('/')[-1] for sub_cell_name in sub_cell_dict.keys()]

    text_inference = [topAPI.gds2generator.CellInspector.convert_pcell_name_to_generator_name(sub_cell_name)
                      if 'extStacked' not in sub_cell_name else
                      topAPI.gds2generator.CellInspector.inspect_via_stack(qtproject._DesignParameter[top_cell_name][sub_cell_name], False)
                      for sub_cell_name in sub_cell_name_list]

    return inference_list, text_inference, sub_cell_name_list



def loadGDS_for_debug( filename=None):
    qtproject = QTInterfaceWithAST.QtProject(_name='project')
    if not topAPI.element_predictor.model:
        topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model(user_setup.model_dir)

    _moduleName = filename.replace(".gds", "")
    _moduleName = _moduleName.split('/')[-1]
    print(f"file load: {filename}")
    try:
        qtproject._loadDesignsFromGDSlegacy(_file=filename, _topModuleName=_moduleName, ignore_non_element=True)
    except:
        import collections
        qtproject._DesignParameter = collections.OrderedDict()
        qtproject._loadDesignsFromGDSlegacy(_file=filename, _topModuleName=_moduleName, _reverse=True, ignore_non_element=True)

    entireHierarchy = qtproject._getEntireHierarchy()


    top_cell_name, sub_cell_dict = list(entireHierarchy.items())[0]
    # sub_cell_list = [qtproject._DesignParameter[top_cell_name][sub_cell_name.split('/')[-1]]._DesignParameter['_DesignObj'] for sub_cell_name in sub_cell_dict.keys()]
    # sub_cell_for_debug = qtproject._DesignParameter[top_cell_name]['pch_lvt_CDNS_667720465882_0']._DesignParameter['_DesignObj']
    # mat=cell_to_matrix_visualize(sub_cell_for_debug)
    # print(topAPI.element_predictor.model.predict(np.array([mat])))

    sub_cell_for_debug = qtproject._DesignParameter[top_cell_name]['M4_M3_CDNS_6677242489165_14']._DesignParameter[
        '_DesignObj']
    mat=cell_to_matrix_visualize(sub_cell_for_debug)
    print(topAPI.element_predictor.model.predict(np.array([mat])))
    return topAPI.element_predictor.model.predict(np.array([mat]))


def build_layer_matrix_by_dps(qt_dp_dict):
    """
    input: dp_dictionary
    output: cell type prediction result str
    """
    lay_mat = topAPI.layer_to_matrix.LayerToMatrix(element_predictor.matrix_x_step, element_predictor.matrix_y_step, element_predictor.layer_list)
    dummy_dp = QTInterfaceWithAST.DummyDesignParameter()
    for name, qt_dp in qt_dp_dict.items():
        dummy_dp.restore_dp(name,qt_dp)

    # lay_mat.load_qt_parameters(qt_dp_dict)
    lay_mat.load_dp(dummy_dp._DesignParameter,minimum_step_size=None,matrix_size=(element_predictor.matrix_x_step,element_predictor.matrix_y_step),bb=False)
    detection = detect_cell(lay_mat.matrix_by_layer)
    return element_predictor.generator_name_mapping(detection)


def detect_cell( matrix_by_layer):
    stacked_matrix = None
    cell_data = None
    for layer in element_predictor.layer_list:
        if type(stacked_matrix) == np.ndarray:
            stacked_matrix = np.append(stacked_matrix, np.expand_dims(np.array(matrix_by_layer[layer]),2), axis=2)
        else:
            stacked_matrix = np.expand_dims(np.array(matrix_by_layer[layer]),2)

    cell_data = np.array([stacked_matrix])

    if not topAPI.element_predictor.model:
        topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model(user_setup.model_dir)

    start_time = time.time()
    result = topAPI.element_predictor.model.predict(cell_data)
    end_time = time.time()
    time_elapsed = end_time - start_time
    global dl_inference_time
    global dl_count
    dl_inference_time += time_elapsed
    dl_count += 1
    idx = np.argmax(result)
    positive_check = np.nonzero(np.greater(result, user_setup.DL_threshold))
    if positive_check[0].size == 0:
        warnings.warn('No cell type is detected.')
        return 'Negative'

    print(dl_inference_time, dl_count, dl_inference_time/dl_count)

    return element_predictor.data_type_list[idx]


def cell_to_matrix(cell):
    lay_mat = topAPI.layer_to_matrix.LayerToMatrix(element_predictor.matrix_x_step, element_predictor.matrix_y_step,
                                                   element_predictor.layer_list)
    dummy_dp = QTInterfaceWithAST.DummyDesignParameter()
    for name, qt_dp in cell.items():
        dummy_dp.restore_dp(name, qt_dp)

    lay_mat.load_dp(dummy_dp._DesignParameter, minimum_step_size=None,
                    matrix_size=(element_predictor.matrix_x_step, element_predictor.matrix_y_step), bb=False)
    matrix_by_layer = lay_mat.matrix_by_layer
    stacked_matrix = np.zeros(
        (element_predictor.matrix_x_step, element_predictor.matrix_y_step, len(element_predictor.layer_list)))
    for i, layer in enumerate(element_predictor.layer_list):
        if layer in matrix_by_layer.keys():
            stacked_matrix[:, :, i] = matrix_by_layer[layer]
    return stacked_matrix

def cell_to_matrix_visualize(cell):
    lay_mat = topAPI.layer_to_matrix.LayerToMatrix(element_predictor.matrix_x_step, element_predictor.matrix_y_step,
                                                   element_predictor.layer_list)
    dummy_dp = QTInterfaceWithAST.DummyDesignParameter()
    for name, qt_dp in cell.items():
        dummy_dp.restore_dp(name, qt_dp)

    lay_mat.load_dp(dummy_dp._DesignParameter, minimum_step_size=None,
                    matrix_size=(element_predictor.matrix_x_step, element_predictor.matrix_y_step), bb=False)
    matrix_by_layer = lay_mat.matrix_by_layer

    #visualization#
    for layer in matrix_by_layer.keys():
        plt.imshow(matrix_by_layer[layer], origin='lower')
        plt.title(layer)
        plt.axis('off')
        plt.show()
    ###############

    stacked_matrix = np.zeros(
        (element_predictor.matrix_x_step, element_predictor.matrix_y_step, len(element_predictor.layer_list)))
    for i, layer in enumerate(element_predictor.layer_list):
        if layer in matrix_by_layer.keys():
            stacked_matrix[:, :, i] = matrix_by_layer[layer]
    return stacked_matrix
def read_matrix_data(sub_cell_list):
    for stacked_matrix in sub_cell_list:
        yield stacked_matrix


def result_check(result, csv_file=None):
    positive_list = [True if p == l else False for p, l in zip(result[0], result[1]) if p != 'Negative'] #
    negative_list = [True if p == l else False for p, l in zip(result[0], result[1]) if p == 'Negative'] #
    tp = positive_list.count(True)
    tn = negative_list.count(True)
    fp = len(positive_list) - tp
    fn = len(negative_list) - tn
    print(f'TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}')

    if csv_file:
        file_name = f'./model_test_dat/csv/{csv_file}.csv'
        with open(file_name, 'w', newline='') as f:
            import csv
            writer = csv.writer(f)
            writer.writerow(['prediction', 'label', 'sub_cell_name'])
            writer.writerows(zip(result[0], result[1], result[2]))

    dict_for_class_result = class_wise_check(result)

    return positive_list, negative_list, (tp, tn, fp, fn), dict_for_class_result

def class_wise_check(result):
    gen_name_list = [element_predictor.generator_name_mapping(name, False) for name in element_predictor.data_type_list]
    # dict_for_class_result = dict.fromkeys(gen_name_list)
    dict_for_class_result = {key: [0,0,0,0] for key in gen_name_list}
    labels = result[1]
    predictions = result[0]
    for i, label in enumerate(labels):
        if label not in dict_for_class_result.keys() and label != 'Negative':
            # dict_for_class_result[label] = [0, 0, 0, 0]
            print(label)
            print(dict_for_class_result.keys())
            warnings.warn('Something Wrong')

        if label == 'Negative':
            if predictions[i] == 'Negative':
                for key in dict_for_class_result.keys():
                    dict_for_class_result[key][1] += 1
            else:
                for key in dict_for_class_result.keys():
                    if key == predictions[i]: # False Positive for the class
                        dict_for_class_result[key][2] += 1
                    else: #True negative for others
                        dict_for_class_result[key][1] += 1
        else:  # Label is positive
            if predictions[i] == label: # There is true positive
                for key in dict_for_class_result.keys():
                    if key == label: ## True Positive for the class
                        dict_for_class_result[key][0] += 1
                    else: #True negative for others
                        dict_for_class_result[key][1] += 1
            else:   # Wrong prediction for positive label
                for key in dict_for_class_result.keys():
                    if key == label:  # False Negative for the class
                        dict_for_class_result[key][3] += 1
                    elif key == predictions[i]: # False Positive for the class
                        dict_for_class_result[key][2] += 1
                    else: #True negative for others
                        dict_for_class_result[key][1] += 1


        # if label == 'Negative':
        #     if label == predictions[i]: #True Negative
        #         dict_for_class_result[label][1] += 1
        #     else:                       #False Positive
        #         dict_for_class_result[label][3] += 1
        # else:
        #     if label == predictions[i]: #True Positive
        #         dict_for_class_result[label][0] += 1
        #     else:                       #False Negative
        #         dict_for_class_result[label][2] += 1
    return dict_for_class_result

def class_result_check(list_for_dict_for_class_result):
    total_dict = None
    for dict_for_class_result in list_for_dict_for_class_result:
        if total_dict is None:
            total_dict = dict_for_class_result
            continue
        for key, value in dict_for_class_result.items():
            if key not in total_dict.keys():
                total_dict[key] = value
            else:
                total_dict[key] = [sum(x) for x in zip(total_dict[key], value)]
    return total_dict

def analyze_class_result(result_dict):
    for key, value in result_dict.items():
        tp, tn, fp, fn = value
        precision = tp / (tp + fp) if tp + fp != 0 else 1
        recall = tp / (tp + fn) if tp + fn != 0 else 1
        f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall != 0 else 1
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        # print(f'{key} Precision: {precision}, Recall: {recall}, F1 Score: {f1_score}, Accuracy: {accuracy}')
    tot_tp = sum([value[0] for value in result_dict.values()])
    tot_tn = sum([value[1] for value in result_dict.values()])
    tot_fp = sum([value[2] for value in result_dict.values()])
    tot_fn = sum([value[3] for value in result_dict.values()])
    tot_precision = tot_tp / (tot_tp + tot_fp) if tot_tp + tot_fp != 0 else 1
    tot_recall = tot_tp / (tot_tp + tot_fn) if tot_tp + tot_fn != 0 else 1
    tot_f1_score = 2 * (tot_precision * tot_recall) / (tot_precision + tot_recall) if tot_precision + tot_recall != 0 else 1
    tot_accuracy = (tot_tp + tot_tn) / (tot_tp + tot_tn + tot_fp + tot_fn)
    false_alarm = tot_fp / (tot_fp + tot_tn) if tot_fp + tot_tn != 0 else 1
    print(f'total tp: {tot_tp}, total tn: {tot_tn}, total fp: {tot_fp}, total fn: {tot_fn}')
    print(f'Total Precision: {tot_precision}, Recall: {tot_recall}, F1 Score: {tot_f1_score}, Accuracy: {tot_accuracy}, False Alarm: {false_alarm}')

def serialize_all_predictions(result_list):
    label = []
    prediction = []
    for result in result_list:
        prediction.extend(result[0])
        label.extend(result[1])
    return prediction, label

def cal_f1_score(predict, label):
    from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix
    # print(f"micro:{f1_score(label, predict, average='micro')}")
    # print(f"macro:{f1_score(label, predict, average='macro')}")
    print(f"weight:{f1_score(label, predict, average='weighted'):.3}")


    print('-----------------Precision-----------------')
    zero_div = 0
    # print(f"micro:{precision_score(label, predict, average='micro', zero_division=zero_div)}")
    # print(f"macro:{precision_score(label, predict, average='macro', zero_division=zero_div)}")
    print(f"weight:{precision_score(label, predict, average='weighted', zero_division=zero_div):.3}")

    print('-----------------Recall-----------------')
    # print(f"micro:{recall_score(label, predict, average='micro', zero_division=zero_div)}")
    # print(f"macro:{recall_score(label, predict, average='macro', zero_division=zero_div)}")
    print(f"weight:{recall_score(label, predict, average='weighted', zero_division=zero_div):.3}")

    # print('-----------------TP TN FP FN-----------------')
    # cm = confusion_matrix(label, predict)
    # TP = sum(np.diag(cm))
    # FP = sum(cm.sum(axis=0)) - TP
    # FN = sum(cm.sum(axis=1)) - TP
    # TN = cm.sum() - (FP + FN + TP)
    # tot = cm.sum()
    # TP =np.diag(cm)
    # FP = np.sum(cm, axis=0) - TP
    # FN = np.sum(cm, axis=1) - TP
    # TN = cm.values.sum() - (FP + FN + TP)
    # TP = np.sum(TP)
    # FP = np.sum(FP)
    # FN = np.sum(FN)
    # TN = np.sum(TN)
    # print(f'TP: {TP}, TN: {TN}, FP: {FP}, FN: {FN}, Total: {tot}')
    # print(confusion_matrix(label, predict))
    # print(cm)


def get_file_list(folder):
    file_list = []
    for file in os.listdir(folder):
        if file.endswith('.gds'):
            file_list.append(os.path.join(folder, file))
    return file_list

def inspect_label(labels):
    label_set = list(set(labels))
    label_count = {}
    for label in label_set:
        if 'Via' in label or 'Contact' in label:
            if 'Via' in label_count:
                label_count['Via'] += labels.count(label)
            else:
                label_count['Via'] = labels.count(label)
        elif 'MOS' in label:
            if 'MOS' in label_count:
                label_count['MOS'] += labels.count(label)
            else:
                label_count['MOS'] = labels.count(label)
        else:
            label_count[label] = labels.count(label)
    return label_count

if __name__ == '__main_3_':
    label_file_list = []
    label_file_list.append('./model_test_dat/jy_label.pkl')
    label_file_list.append('./model_test_dat/mg_label.pkl')
    label_file_list.append('./model_test_dat/ms_label.pkl')
    labels = []
    import pickle
    for label_file in label_file_list:
        with open(label_file, 'rb') as f:
            labels.extend(pickle.load(f)['label'])
    l_r = inspect_label(labels)




if __name__ == '__main__for_extract_label':
    gds_list = get_file_list('./PyQTInterface/GDSFile/gds_original_rx')
    # gds_list.extend(get_file_list('./PyQTInterface/GDSFile/jy_rx'))
    labels = []
    org_names = []
    for gds_file in gds_list:
        _,label,org_name = loadGDS(gds_file,only_get_label=True)
        labels.extend(label)
        org_names.extend(org_name)
    import pickle

    file_name = 'mg_label.pkl'
    result_dict = dict()
    result_dict['label'] = labels
    result_dict['org_name'] = org_names
    with open(f'./model_test_dat/{file_name}', 'wb') as f:
        pickle.dump(result_dict, f)

if __name__ == '__main__8':
    import pickle
    file_name_list = []
    file_name_list.append('jy_rx_semifinal.pkl')
    file_name_list.append('jy_tx_semifinal.pkl')
    file_name_list.append('ms_tx_semifinal.pkl')
    file_name_list.append('ms_rx_semifinal.pkl')
    model_list = []
    model_list.append('c2_wof_1kernel_softmax_loss_fclass')
    model_list.append('c2_f_1kernel_softmax_loss_fclass')
    model_list.append('c2_wof_1kernel_sigmoid_loss_fclass')
    model_list.append('c2_f_1kernel_sigmoid_loss_fclass')
    p_dict = {model: [] for model in model_list}
    l_dict = {model: [] for model in model_list}
    for file_name in file_name_list:
        with open(f'./model_test_dat/{file_name}', 'rb') as f:
            result_dict = pickle.load(f)
            for model in model_list:
                result_lists = result_dict[model]
                prediction, label = serialize_all_predictions(result_lists)
                p_dict[model].extend(prediction)
                l_dict[model].extend(label)

if __name__ == '__main_4_':
    import pickle
    file_name_list = []
    file_name_list.append('c5_ms_all.pkl')
    # file_name_list.append('c5_mg_all.pkl')
    # file_name_list.append('c5_jy_all.pkl')
    # file_name_list.append('jy_tx_semifinal.pkl')
    # file_name_list.append('ms_tx_semifinal.pkl')
    # file_name_list.append('ms_rx_semifinal.pkl')
    model_list = []
    model_list.append('c5_softmax_wof')
    model_list.append('c5_softmax_wf')
    model_list.append('c5_sigmoid_wof')
    model_list.append('c5_sigmoid_wf')
    p_dict = {model: [] for model in model_list}
    l_dict = {model: [] for model in model_list}
    for file_name in file_name_list:
        with open(f'./model_test_dat/{file_name}', 'rb') as f:
            result_dict = pickle.load(f)
            for model in model_list:
                result_lists = result_dict[model]
                prediction, label = serialize_all_predictions(result_lists)
                p_dict[model].extend(prediction)
                l_dict[model].extend(label)
    for model in model_list:
        print(f'===================={model}====================')
        cal_f1_score(p_dict[model], l_dict[model])
        # analyze_class_result(class_wise_check((p_dict[model], l_dict[model])))

if __name__ == '__main__4':
    import pickle
    file_name = 'jy_rx_semifinal.pkl'
    with open(f'./model_test_dat/{file_name}', 'rb') as f:
        result_dict = pickle.load(f)
    model_list = []
    model_list.append('c2_wof_1kernel_softmax_loss_fclass')
    model_list.append('c2_f_1kernel_softmax_loss_fclass')
    model_list.append('c2_wof_1kernel_sigmoid_loss_fclass')
    model_list.append('c2_f_1kernel_sigmoid_loss_fclass')
    for model in model_list:
        result_lists = result_dict[model]
        prediction, label = serialize_all_predictions(result_lists)
        cal_f1_score(prediction, label)
        print('\n\n\n')

if __name__ == '__main__2':
    # loadGDS_for_debug('./PyQTInterface/GDSFile/ms_rx/comparator_strongArm_cms_TSMCN65TX2016_REV2.gds')
    o = loadGDS_for_debug('./PyQTInterface/GDSFile/ms_tx/driver_core_v5_cms.gds')

if __name__ == '__main_5_':

    '''
    Append model directory to model_list
    '''
    result_dict = dict()
    model_list =[]
    # model_list.append('./powertool/dl_models/ss28/128b_1000_basic_classification_sig_wfalse')
    # model_list.append('./powertool/dl_models/ss28/128b_1000_basic_classification_org_wfalse')
    # model_list.append('./powertool/dl_models/ss28/128b_1000_basic_classification_1kernel_wfalse')

    # model_list.append('./powertool/dl_models/ss28/c1_wof_softmax')
    # model_list.append('./powertool/dl_models/ss28/c1_f_softmax')
    # model_list.append('./powertool/dl_models/ss28/c1_wof_sigmoid')
    # model_list.append('./powertool/dl_models/ss28/c1_f_sigmoid')
    # model_list.append('./powertool/dl_models/ss28/c1_wof_1kernel_sigmoid')
    # model_list.append('./powertool/dl_models/ss28/c1_f_1kernel_sigmoid')
    # model_list.append('./powertool/dl_models/ss28/c1_wof_1kernel_sigmoid_first8')
    # model_list.append('./powertool/dl_models/s s28/c1_f_1kernel_sigmoid_first8')

    # model_list.append('./powertool/dl_models/ss28/c1_f_1kernel_sigmoid_loss_fclass')
    # model_list.append('./powertool/dl_models/ss28/c1_fnoise_1kernel_sigmoid_loss_fclass')
    # model_list.append('./powertool/dl_models/ss28/c2_f_1kernel_sigmoid_loss_fclass')
    # model_list.append('./powertool/dl_models/ss28/c2_wof_1kernel_softmax_loss_fclass')
    # model_list.append('./powertool/dl_models/ss28/c2_wof_1kernel_softmax_loss_fclass')

    # model_list.append('./powertool/dl_models/ss28/c2_wof_1kernel_softmax_loss')

    # model_list.append('./powertool/dl_models/ss28/c2_wof_1kernel_softmax_loss_fclass')
    # model_list.append('./powertool/dl_models/ss28/c2_f_1kernel_softmax_loss_fclass')
    # model_list.append('./powertool/dl_models/ss28/c2_wof_1kernel_sigmoid_loss_fclass')
    # model_list.append('./powertool/dl_models/ss28/c2_f_1kernel_sigmoid_loss_fclass')


    # model_list.append('./powertool/dl_models/ss28/c4_f_1kernel_sigmoid_loss_fclass_big')
    # model_list.append('./powertool/dl_models/ss28/c4_f_1kernel_sigmoid_loss_fclass_bbig_nw')
    # model_list.append('./powertool/dl_models/ss28/c4_f_1kernel_sigmoid_loss_fclass_nw')

    model_list.append('./powertool/dl_models/ss28/c5_softmax_wf')
    model_list.append('./powertool/dl_models/ss28/c5_softmax_wof')
    model_list.append('./powertool/dl_models/ss28/c5_sigmoid_wof')
    model_list.append('./powertool/dl_models/ss28/c5_sigmoid_wf')



    # model_list.append('./powertool/dl_models/ss28/c3_f_1kernel_sigmoid_loss_fclass_nologit')
    # model_list.append('./powertool/dl_models/ss28/c3_f_1kernel_sigmoid_loss_fclass_nologit')

    # c2_fnoise_1kernel_sigmoid_loss_fclass

    # c1_f_1kernel_sigmoid_wovia


    # model_list.append('./powertool/dl_models/ss28/c1_wof_softmax_fclass')
    # model_list.append('./powertool/dl_models/ss28/c1_f_softmax_fclass')


    '''
    Append test data (gds format) to gds_list
    you can use get_file_list function to get all gds files in a folder
    Or you can manually append gds files to gds_list
    '''
    # gds_list = get_file_list('./PyQTInterface/GDSFile/jy_tx')
    # gds_list.extend(get_file_list('./PyQTInterface/GDSFile/jy_rx'))
    # gds_list = get_file_list('./PyQTInterface/GDSFile/gds_original_rx')
    # gds_list = get_file_list('./PyQTInterface/GDSFile/ss_receiver')
    gds_list = get_file_list('./PyQTInterface/GDSFile/ms_rx')
    gds_list.extend(get_file_list('./PyQTInterface/GDSFile/ms_tx'))
    # gds_list = ['./PyQTInterface/GDSFile/ms_rx/receiver_resistor_bank_v2_cms.gds']
    # gds_list = ['./PyQTInterface/GDSFile/ms_tx/driver_dcc_core_cms.gds']

    '''
    Test each model for each gds file
    '''
    for model_dir in model_list:
        model_name = model_dir.split('/')[-1]
        result_dict[model_name] = []
        list_for_dict_for_class_result = []
        user_setup.model_dir = model_dir
        start_time = time.time()
        result_list = []
        for gds_path in gds_list:
            result = loadGDS(filename=gds_path, false_class=True)
            result_list.append(result)
        check_dict = [0,0,0,0]
        for i, result in enumerate(result_list):
            '''
                If you want to save the result in csv format,
                you can use result_check function with csv_file parameter
                example: csv_file = f'{model_dir.split('/')[-1]}_{gds_path.split('/')[-1]}'
            '''
            _,_,(tp, tn, fp, fn), dict_for_class_result = result_check(result, csv_file = f'{model_dir.split("/")[-1]}_{gds_list[i].split("/")[-1]}')
            check_dict[0] += tp
            check_dict[1] += tn
            check_dict[2] += fp
            check_dict[3] += fn
            list_for_dict_for_class_result.append(dict_for_class_result)
        c_out= class_result_check(list_for_dict_for_class_result)
        p,l = serialize_all_predictions(result_list)
        cal_f1_score(p,l)
        result_dict[model_name] = result_list
        result_dict[f'{model_name}/class'] =c_out
        analyze_class_result(c_out)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        print(f'{model_name} : {check_dict}')
        del topAPI.element_predictor.model
        topAPI.element_predictor.model = None

    '''
    If you want to save the whole result, you can use below code
    '''
    import pickle
    file_name = 'c5_ms_all.pkl'
    result_dict['gds_list'] = gds_list
    with open(f'./model_test_dat/{file_name}', 'wb') as f:
    #     result_dict = dict(result_list=result_list, gds_list = gds_list)
        pickle.dump(result_dict, f)

    # file_name = 'ms_all_final.pkl'
    # result_dict['gds_list'] = gds_list
    # with open(f'./model_test_dat/{file_name}', 'rb') as f:
    #     result_dict = pickle.load(f)

#make dict from list