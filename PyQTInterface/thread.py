from PyQt5.QtCore import QThread, QObject, pyqtSignal, QRunnable
from PyQt5.QtWidgets import QProgressDialog
import threading
from generatorLib import generator_model_api
from DesignManager import ElementManager
from PyQTInterface import VisualizationItem
import user_setup


thread_result = [None] * user_setup.MULTI_THREAD_NUM
finished_work = [0] * user_setup.MULTI_THREAD_NUM

class WorkerSignal(QObject):
    one_job_progress_signal = pyqtSignal()
    every_job_doen_signal = pyqtSignal()

class VSItemRunnable(QRunnable):
    def __init__(self, n, target_cells_dict):
        super(VSItemRunnable, self).__init__()
        self.name = n
        self.topcell = target_cells_dict
        self.signal = WorkerSignal()

    def run(self):
        vs_item_dict = dict()
        layer_dict = dict()
        id_layer_dict = dict()
        for element_name, _element in self.topcell.items():
            ####################################### Visual Item Creation ##########################################
            if self.topcell[element_name]._DesignParameter['_DesignParametertype'] != 3:
                visual_item = VisualizationItem._VisualizationItem()
                visual_item.updateDesignParameter(self.topcell[element_name])
                visual_item.setBoundingRegionGranularity(1)
                vs_item_dict[element_name] = visual_item
                visual_item.setToolTip(element_name + '\n' + str(self.topcell[element_name]._type))
                layer = visual_item._ItemTraits['_LayerUnifiedName']
                if layer in layer_dict:
                    layer_dict[layer].append(visual_item)
                else:
                    layer_dict[layer] = [visual_item]
                id_layer_dict[element_name] = layer
            else:
                sref_vi = VisualizationItem._VisualizationItem()
                sref_vi.updateDesignParameter(_element)
                vs_item_dict[element_name] = sref_vi
                layer_dict = sref_vi.returnLayerDict()
            finished_work[int(self.name)] += 1
            self.signal.one_job_progress_signal.emit()

        thread_result[int(self.name)] = vs_item_dict, layer_dict, id_layer_dict
        print(f'worker {self.name} job done')
        self.signal.every_job_doen_signal.emit()

class VSItemRunnableManager(QRunnable):
    def __init__(self, total_worker):
        super(VSItemRunnableManager, self).__init__()
        self.workers = total_worker
        self.signal = WorkerSignal()

    def add_job_done(self):
        self.workers -= 1
        # if self.workers == 0:
        #     self.signal.every_job_doen_signal.emit()
        #     print(f'Every work is done')

    def run(self):
        while self.workers != 0:
            pass
        self.signal.every_job_doen_signal.emit()
        print(f'Every work is done')


class VSitemWorker(threading.Thread):
    def __init__(self, name, target_cells_dict):
        super(VSitemWorker, self).__init__()
        self.name = name
        self.topcell = target_cells_dict

    def run(self):
        vs_item_dict = dict()
        layer_dict = dict()
        id_layer_dict = dict()
        for element_name, _element in self.topcell.items():
            ####################################### Visual Item Creation ##########################################
            if self.topcell[element_name]._DesignParameter['_DesignParametertype'] != 3:
                visual_item = VisualizationItem._VisualizationItem()
                visual_item.updateDesignParameter(self.topcell[element_name])
                visual_item.setBoundingRegionGranularity(1)
                vs_item_dict[element_name] = visual_item
                visual_item.setToolTip(element_name + '\n' + str(self.topcell[element_name]._type))
                layer = visual_item._ItemTraits['_LayerUnifiedName']
                if layer in layer_dict:
                    layer_dict[layer].append(visual_item)
                else:
                    layer_dict[layer] = [visual_item]
                id_layer_dict[element_name] = layer
            else:
                sref_vi = VisualizationItem._VisualizationItem()
                sref_vi.updateDesignParameter(_element)
                vs_item_dict[element_name] = sref_vi
                layer_dict = sref_vi.returnLayerDict()
            finished_work[int(self.name)] += 1

        thread_result[int(self.name)] = vs_item_dict, layer_dict, id_layer_dict
        # return vs_item_dict, layer_dict, id_layer_dict


def create_vs_items(topcell, flattening_dict):
    vs_item_dict = dict()
    layer_dict = dict()
    id_layer_dict = dict()
    for element_name, _element in topcell.items():
        ####################################### Visual Item Creation ##########################################
        if topcell[element_name]._DesignParameter['_DesignParametertype'] != 3:
            visual_item = VisualizationItem._VisualizationItem()
            visual_item.updateDesignParameter(topcell[element_name])
            visual_item.setBoundingRegionGranularity(1)
            vs_item_dict[element_name] = visual_item
            visual_item.setToolTip(element_name+ '\n' + str(topcell[element_name]._type))
            layer = visual_item._ItemTraits['_LayerUnifiedName']
            if layer in layer_dict:
                layer_dict[layer].append(visual_item)
            else:
                layer_dict[layer] = [visual_item]
            id_layer_dict[element_name] = layer
        else:
            sref_vi = VisualizationItem._VisualizationItem()
            sref_vi.updateDesignParameter(element_name)
            vs_item_dict[element_name] = sref_vi
            layer_dict = sref_vi.returnLayerDict()
    return vs_item_dict, layer_dict, id_layer_dict
        # self.dockContentWidget1_2.layer_table_widget.updateLayerList(self._layerItem)

class MultiThreadQProgressBar(QProgressDialog):
    def __init__(self, label, cancel, min, max, parent):
        super(MultiThreadQProgressBar, self).__init__(label, cancel, min, max, parent)

    def add_count(self):
        self.setValue(self.value()+1)

    def set_max(self):
        self.setValue(self.maximum())