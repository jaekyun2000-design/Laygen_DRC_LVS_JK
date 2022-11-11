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


def loadGDS( filename=None, false_class=False):
    qtproject = QTInterfaceWithAST.QtProject(_name='project')


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

    dataset = tf.data.Dataset.from_generator(read_matrix_data,
                                             (tf.float64),
                                             (tf.TensorShape([element_predictor.matrix_x_step, element_predictor.matrix_y_step, len(element_predictor.layer_list)])),
                                             args=(sub_cell_mat_list,))
    dataset = dataset.batch(batch_size)
    if not topAPI.element_predictor.model:
        topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model(user_setup.model_dir)
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
                print('dbg for original with false class')
                inference_list[i] = 'Negative'

    sub_cell_name_list = [sub_cell_name.split('/')[-1] for sub_cell_name in sub_cell_dict.keys()]

    text_inference = [topAPI.gds2generator.CellInspector.convert_pcell_name_to_generator_name(sub_cell_name)
                      if 'extStacked' not in sub_cell_name else
                      topAPI.gds2generator.CellInspector.inspect_via_stack(qtproject._DesignParameter[top_cell_name][sub_cell_name], False)
                      for sub_cell_name in sub_cell_name_list]

    return inference_list, text_inference, sub_cell_name_list



def loadGDS_for_debug( filename=None):
    qtproject = QTInterfaceWithAST.QtProject(_name='project')


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
    if not topAPI.element_predictor.model:
        topAPI.element_predictor.model = topAPI.element_predictor.create_element_detector_model(user_setup.model_dir)
    # print(topAPI.element_predictor.model.predict(np.array([mat])))

    sub_cell_for_debug = qtproject._DesignParameter[top_cell_name]['M3_M2_CDNS_667720465881_0']._DesignParameter[
        '_DesignObj']
    mat=cell_to_matrix_visualize(sub_cell_for_debug)
    print(topAPI.element_predictor.model.predict(np.array([mat])))


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
        file_name = f'{csv_file}.csv'
        with open(file_name, 'w', newline='') as f:
            import csv
            writer = csv.writer(f)
            writer.writerow(['prediction', 'label', 'sub_cell_name'])
            writer.writerows(zip(result[0], result[1], result[2]))


    return positive_list, negative_list, (tp, tn, fp, fn)


def get_file_list(folder):
    file_list = []
    for file in os.listdir(folder):
        if file.endswith('.gds'):
            file_list.append(os.path.join(folder, file))
    return file_list


# if __name__ == '__main__':
#     loadGDS_for_debug('./PyQTInterface/GDSFile/ms_rx/comparator_strongArm_cms_TSMCN65TX2016_REV2.gds')

if __name__ == '__main__':

    '''
    Append model directory to model_list
    '''
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
    model_list.append('./powertool/dl_models/ss28/c1_fnoise_1kernel_sigmoid_loss_fclass')
    # model_list.append('./powertool/dl_models/ss28/c2_fnoise_1kernel_sigmoid_loss_fclass')
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
    # gds_list = get_file_list('./PyQTInterface/GDSFile/jy_rx')
    gds_list = get_file_list('./PyQTInterface/GDSFile/ms_rx')
    # gds_list = get_file_list('./PyQTInterface/GDSFile/ms_tx')
    # gds_list = ['./PyQTInterface/GDSFile/ms_rx/receiver_resistor_bank_v2_cms.gds']

    '''
    Test each model for each gds file
    '''
    for model_dir in model_list:
        user_setup.model_dir = model_dir
        start_time = time.time()
        result_list = []
        for gds_path in gds_list:
            result = loadGDS(filename=gds_path, false_class=True)
            result_list.append(result)
        for i, result in enumerate(result_list):
            '''
                If you want to save the result in csv format,
                you can use result_check function with csv_file parameter
                example: csv_file = f'{model_dir.split('/')[-1]}_{gds_path.split('/')[-1]}'
            '''
            result_check(result, csv_file = f'{model_dir.split("/")[-1]}_{gds_list[i].split("/")[-1]}')
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        del topAPI.element_predictor.model
        topAPI.element_predictor.model = None

    '''
    If you want to save the whole result, you can use below code
    '''
    import pickle
    # file_name = 'jy_tx.pkl'
    # with open(f'./model_test_dat/{file_name}', 'wb') as f:
    #     result_dict = dict(result_list=result_list, gds_list = gds_list)
    #     pickle.dump(result_dict, f)

