import traceback
import warnings

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import random as rd

from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn.preprocessing import RobustScaler
from sklearn.manifold import MDS, LocallyLinearEmbedding
from sklearn.decomposition import PCA
from PyQTInterface.layermap import LayerReader
from powertool.model import routing_geo_searching
import re

import copy

class clustering():
    def __init__(self, _DesignParameters = None, _qtDesignParameters=None):
        self._DesignParameter = copy.deepcopy(_DesignParameters)
        self._qtDesignParameters = copy.deepcopy(_qtDesignParameters)
        self.qt_dp_layer_conversion()
        self.array_groups = []
        self.routing_groups = []
        self.geo_searching = routing_geo_searching.GeometricField()
        self.intersection_matching_dict_by_name = dict()
        if '_Name' in self._DesignParameter:
            del self._DesignParameter['_Name']
        if '_GDSFile' in self._DesignParameter:
            del self._DesignParameter['_GDSFile']

    def load_dp_dict(self,dp_dict):
        self._DesignParameter = dp_dict
        if '_Name' in self._DesignParameter:
            del self._DesignParameter['_Name']
        if '_GDSFile' in self._DesignParameter:
            del self._DesignParameter['_GDSFile']

    def qt_dp_layer_conversion(self):

        if self._qtDesignParameters:
            layer_converter = LayerReader._LayerMapping
            for qt_dp in self._qtDesignParameters.values():
                item = qt_dp._DesignParameter
                if item['_DesignParametertype'] == 1 or item['_DesignParametertype'] == 2:
                    layer = item['_Layer']
                    if type(layer) == str:
                        item['_Layer'] = layer_converter[layer][0]
                    else:
                        continue
            _DesignParameters = dict()
            for key, value in self._qtDesignParameters.items():
                _DesignParameters[key] = value._DesignParameter
            self._DesignParameter = copy.deepcopy(_DesignParameters)

                    # layer_num = item['_Layer']
                    # if layer_num in self.layer_based_group:
                    #     self.layer_based_group[layer_num].append(key)
                    # else:
                    #     self.layer_based_group[layer_num] = [key]


    def build_layer_ist_qt(self):
        self.geo_searching.xy_projection_to_main_coordinates_system_qt(self._qtDesignParameters)
        self.geo_searching.build_IST_qt(self._qtDesignParameters)
        return self._qtDesignParameters

    def build_layer_ist(self):
        self.geo_searching.xy_projection_to_main_coordinates_system(self._DesignParameter)
        self.geo_searching.build_IST(self._DesignParameter)
        return self._DesignParameter

    def delete_solo_element_group(self):
        delete_index_list = []
        for i, group in enumerate(self.array_groups):
            if len(group) == 1:
                delete_index_list.append(i)
        for idx in reversed(delete_index_list):
            del self.array_groups[idx]

        delete_index_list = []
        for i, group in enumerate(self.routing_groups):
            if len(group) == 1 :
                delete_index_list.append(i)
        for idx in reversed(delete_index_list):
            del self.routing_groups[idx]

    def find_ref(self, array_group):
        ref_list = []
        try:
            for id_list in array_group:
                if self._qtDesignParameters[id_list[0]]._type == 1:
                    ref_list.append(self.find_ref_for_boundary_qt(id_list))
                elif self._qtDesignParameters[id_list[0]]._type == 2:
                    ref_list.append(self.find_ref_for_path_qt(id_list))
                elif self._qtDesignParameters[id_list[0]]._type == 3:
                    ref_list.append(self.find_ref_for_sref_qt(id_list))
            return ref_list
        except:
            traceback.print_exc()
            print("Unable to recognize Array References; Rearrange the design appropriately!")
            return ref_list



    def find_ref_for_path_qt(self,id_list):
        x_offset = None
        y_offset = None
        col = None
        row = None
        layer = None
        index = None
        source_reference = None
        target_reference = None

        try:
            qt_dp_list = [self._qtDesignParameters[id] for id in id_list]
            x_list = [qt_dp._DesignParameter['_XYCoordinates'][0][0][0] for qt_dp in qt_dp_list]
            y_list = [qt_dp._DesignParameter['_XYCoordinates'][0][0][1] for qt_dp in qt_dp_list]
            # layer = LayerReader._LayerName_unified[str(qt_dp_list[0]._DesignParameter['_Layer'])]
            layer = qt_dp_list[0]._DesignParameter['_LayerUnifiedName']
            x_list.sort()
            y_list.sort()
            x_offset = int(x_list[1] - x_list[0])
            y_offset = int(y_list[1] - y_list[0])
            if x_offset == 0:
                col = 1
                row = len(y_list)
            else:
                col = len(x_list)
                row = 1
            connection_layer_list = []
            for id in id_list:
                connection_layer_list.extend([intersection_info for intersection_info in self.intersection_matching_dict_by_name[id]])
            if connection_layer_list:
                connection_wo_last_idx = copy.deepcopy(connection_layer_list)
                for idx, _ in enumerate(connection_wo_last_idx):
                    connection_wo_last_idx[idx][-1] = copy.deepcopy(connection_wo_last_idx[idx][-1].split('[')[0])
                    # cutting_idx = connection_wo_last_idx[idx][-1].find('[')
                    # connection_wo_last_idx[idx][-1] = connection_wo_last_idx[idx][-1][:cutting_idx]

                set1 = set(map(tuple,connection_layer_list))
                connection_top_name = [connection_hierarchy[0] for connection_hierarchy in connection_layer_list]
                set2 = set(connection_top_name)

                count_list = []
                for set1_ele in set1:
                    count_list.append(connection_layer_list.count(list(set1_ele)))
                max_idx_list = [idx for idx, ele in enumerate(count_list) if ele == max(count_list)]
                for max_idx in max_idx_list:
                    if len(list(set1)[max_idx]) == 1:
                        set2.remove(list(set1)[max_idx][0])

                max_idx_candi_len_list = [len(list(set1)[idx_cand]) for idx_cand in max_idx_list]
                final_idx2 = max_idx_candi_len_list.index(min(max_idx_candi_len_list))
                max_idx = max_idx_list[final_idx2]
                # max_idx = count_list.index(max(count_list))
                target_reference = list(list(set1)[max_idx])

                count_list = []
                # set2.remove(target_reference[0])
                for set2_ele in set2:
                    count_list.append(connection_top_name.count(set2_ele))
                max_idx = count_list.index(max(count_list))
                top_cell_name = list(set2)[max_idx]
                hierarchy_idx = connection_top_name.index(top_cell_name)
                source_reference = copy.deepcopy(connection_layer_list[hierarchy_idx])
                source_reference[-1] = copy.deepcopy(source_reference[-1].split('[')[0])

                # cutting_idx = source_reference[-1].find('[')
                # source_reference[-1] = source_reference[-1][:cutting_idx]

                connection_layer_idx_of_source = []
                for i, ele in enumerate(connection_wo_last_idx):
                    if ele == source_reference:
                        connection_layer_idx_of_source.append(i)
                source_reference_list = [connection_layer_list[idx] for idx in connection_layer_idx_of_source]
                index = 'Custom'
                source_dp = self.get_hierarchy_item(source_reference_list[0])
                if type(source_dp) != dict:
                    warnings.warn('WARNING: Trying to inspect index by item whose type is not generator.')
                else:
                    if len(source_dp['_XYCoordinates']) == len(qt_dp_list):
                        index = 'All'
                    else:
                        source_index_list = [re.search('\[[0-9]*\]',source_ref[-1]).group()[1:-1] for source_ref in source_reference_list]
                        even_filter = list(filter(lambda x: int(x)%2 == 0, source_index_list))
                        odd_filter = list(filter(lambda x: int(x)%2 == 1, source_index_list))
                        if len(even_filter) == len(source_index_list):
                            index = 'Even'
                        elif len(odd_filter) == len(source_index_list):
                            index = 'Odd'


            return dict(x_offset=x_offset, y_offset=y_offset, col=col, row=row, layer=layer, index=index,
                        XY_source_ref=source_reference, XY_target_ref=target_reference)
        except:

            return dict(x_offset=x_offset, y_offset=y_offset, col=col, row=row, layer=layer, index=index,
                        XY_source_ref=source_reference, XY_target_ref=target_reference)

    def find_ref_for_boundary_qt(self, id_list):
        qt_dp_list = [self._qtDesignParameters[id] for id in id_list]
        x_list = [qt_dp._DesignParameter['_XYCoordinates'][0][0] for qt_dp in qt_dp_list]
        y_list = [qt_dp._DesignParameter['_XYCoordinates'][0][1] for qt_dp in qt_dp_list]
        layer = LayerReader._LayerName_unified[str(qt_dp_list[0]._DesignParameter['_Layer'])]
        x_list.sort()
        y_list.sort()
        x_offset = int(x_list[1] - x_list[0])
        y_offset = int(y_list[1] - y_list[0])
        if x_offset == 0:
            col = 1
            row = len(y_list)
        else:
            col = len(x_list)
            row = 1
        connection_layer_list = []
        for id in id_list:
            # print(self.intersection_matching_dict_by_name[id][0])
            # tmp = [intersection_info[0] for intersection_info in self.intersection_matching_dict_by_name[id]]
            connection_layer_list.extend(
                [copy.deepcopy(intersection_info[0]) for intersection_info in self.intersection_matching_dict_by_name[id]])
            # connection_layer_list.extend(self.intersection_matching_dict_by_name[id])
        # connection_layer_list.extend([self.intersection_matching_dict_by_name[id] for id in id_list])
        connection_wo_last_idx = copy.deepcopy(connection_layer_list)
        for idx, _ in enumerate(connection_wo_last_idx):
            cutting_idx = connection_wo_last_idx[idx][-1].find('[')
            connection_wo_last_idx[idx][-1] = connection_wo_last_idx[idx][-1][:cutting_idx]
        set2 = set(map(tuple,connection_wo_last_idx))

        count_list = []
        for set2_ele in set2:
            count_list.append(connection_wo_last_idx.count(list(set2_ele)))
        max_idx = count_list.index(max(count_list)) if count_list else 0
        ##### if set is empty ####
        if not set2:
            return dict(x_offset=x_offset, y_offset=y_offset, col=col, row=row, layer=layer, index=None,
                        XY_source_ref=None)
        top_cell_name = list(set2)[max_idx]
        hierarchy_idx = connection_wo_last_idx.index(list(top_cell_name))
        source_reference = connection_wo_last_idx[hierarchy_idx]
        # source_reference = connection_layer_list[hierarchy_idx]

        connection_layer_idx_of_source = []
        for i, ele in enumerate(connection_wo_last_idx):
            if ele == source_reference:
                connection_layer_idx_of_source.append(i)
        source_reference_list = [connection_layer_list[idx] for idx in connection_layer_idx_of_source]
        index = 'Custom'
        source_dp = self.get_hierarchy_item(source_reference_list[0])
        if type(source_dp) != dict:
            warnings.warn('WARNING: Trying to inspect index by item which type is not generator.')
        else:
            if len(source_dp['_XYCoordinates']) == len(qt_dp_list):
                index = 'All'
            else:
                source_index_list = [re.search('\[[0-9]*\]',source_ref[-1]).group()[1:-1] for source_ref in source_reference_list]
                even_filter = list(filter(lambda x: int(x)%2 == 0, source_index_list))
                odd_filter = list(filter(lambda x: int(x)%2 == 1, source_index_list))
                if len(even_filter) == len(source_index_list):
                    index = 'Even'
                elif len(odd_filter) == len(source_index_list):
                    index = 'Odd'

        return dict(x_offset=x_offset, y_offset=y_offset, col=col, row=row, layer=layer, index = index,
                    XY_source_ref=source_reference)

    def find_ref_for_sref_qt(self, id_list):
        qt_dp_list = [self._qtDesignParameters[id] for id in id_list]
        x_list = [qt_dp._DesignParameter['_XYCoordinates'][0][0] for qt_dp in qt_dp_list]
        y_list = [qt_dp._DesignParameter['_XYCoordinates'][0][1] for qt_dp in qt_dp_list]
        x_list.sort()
        y_list.sort()
        x_offset = int(x_list[1] - x_list[0])
        y_offset = int(y_list[1] - y_list[0])
        if x_offset == 0:
            col = 1
            row = len(y_list)
        else:
            col = len(x_list)
            row = 1
        connection_layer_list = []
        for id in id_list:
            connection_layer_list.extend(
                [copy.deepcopy(intersection_info[0]) for intersection_info in self.intersection_matching_dict_by_name[id]])
        connection_layer_list = list(set(map(tuple,connection_layer_list)))        # idx 도 똑같이 중복되는 element 를 제거
        connection_layer_list = [list(tupled_data) for tupled_data in connection_layer_list]
        connection_wo_last_idx = copy.deepcopy(connection_layer_list)
        for idx, _ in enumerate(connection_wo_last_idx):
            cutting_idx = connection_wo_last_idx[idx][-1].find('[')
            connection_wo_last_idx[idx][-1] = connection_wo_last_idx[idx][-1][:cutting_idx]
        set2 = set(map(tuple, connection_wo_last_idx))

        count_list = []
        for set2_ele in set2:
            count_list.append(connection_wo_last_idx.count(list(set2_ele)))
        max_idx = count_list.index(max(count_list)) if count_list else 0
        if not set2:
            return dict(x_offset=x_offset, y_offset=y_offset, col=col, row=row, index=None,
                        XY_source_ref=None)
        top_cell_name = list(set2)[max_idx]
        hierarchy_idx = connection_wo_last_idx.index(list(top_cell_name))
        source_reference = connection_wo_last_idx[hierarchy_idx]
        # source_reference = connection_layer_list[hierarchy_idx]

        connection_layer_idx_of_source = []
        for i, ele in enumerate(connection_wo_last_idx):
            if ele == source_reference:
                connection_layer_idx_of_source.append(i)
        source_reference_list = [connection_layer_list[idx] for idx in connection_layer_idx_of_source]
        index = 'Custom'
        source_dp = self.get_hierarchy_item(source_reference_list[0])
        if type(source_dp) != dict:
            warnings.warn('WARNING: Trying to inspect index by item which type is not generator.')
        else:
            if len(source_dp['_XYCoordinates']) == len(qt_dp_list):
                index = 'All'
            else:
                source_index_list = [re.search('\[[0-9]*\]',source_ref[-1]).group()[1:-1] for source_ref in source_reference_list]
                even_filter = list(filter(lambda x: int(x)%2 == 0, source_index_list))
                odd_filter = list(filter(lambda x: int(x)%2 == 1, source_index_list))
                if len(even_filter) == len(source_index_list):
                    index = 'Even'
                elif len(odd_filter) == len(source_index_list):
                    index = 'Odd'

        return dict(x_offset=x_offset, y_offset=y_offset, col=col, row=row, index= index,
                    XY_source_ref=source_reference)

    def get_hierarchy_item(self, hierarchy_list):
        """
        ex) hierarchy_list = [INV28[0], _Met1Layer[2]]
        output -> self._DesignParameter['INV28']['_DesignObj']._DesignParameter['_Met1Layer']
        """
        if type(hierarchy_list) != list:
            hierarchy_list = list(hierarchy_list)
        hierarchy_list = [element.split('[')[0] for element in hierarchy_list]

        item = self._DesignParameter
        while hierarchy_list:
            element_name = hierarchy_list.pop(0)
            if not hierarchy_list:
                item = item[element_name]
            else:
                if type(item[element_name]['_DesignObj']) == dict:
                    item = item[element_name]['_DesignObj']
                else:
                    item = item[element_name]['_DesignObj']._DesignParameter
        return item

    def get_array_groups(self):
        return self.array_groups

    def get_routing_groups(self):
        return self.routing_groups




class determinstic_clustering(clustering):
    def __init__(self, _DesignParameters = None, _qtDesignParameters=None):
        super().__init__(_DesignParameters,_qtDesignParameters)
        self.layer_based_group = dict()
        self.design_obj_based_group = dict()
        self.pregrouping_by_layer()
            # self.pregrouping_by_layer_qt()
        # self.layer_matching()

    def pregrouping_by_layer_qt(self):
        for key, qt_item in self._qtDesignParameters.items():
            item = qt_item._DesignParameter
            if item['_DesignParametertype'] == 1 or item['_DesignParametertype'] == 2:
                layer_num = item['_Layer']
                if layer_num in self.layer_based_group:
                    self.layer_based_group[layer_num].append(key)
                else:
                    self.layer_based_group[layer_num] = [key]
            elif item['_DesignParametertype'] == 3:
                class_name = item['_DesignObj'].__class__.__name__
                if class_name in self.design_obj_based_group:
                    self.design_obj_based_group[class_name].append(key)
                else:
                    self.design_obj_based_group[class_name] = [key]

    def pregrouping_by_layer(self):
        for key, item in self._DesignParameter.items():
            if item['_DesignParametertype'] == 1 or item['_DesignParametertype'] == 2:
                layer_num = item['_Layer']
                if layer_num in self.layer_based_group:
                    self.layer_based_group[layer_num].append(key)
                else:
                    self.layer_based_group[layer_num] = [key]
            elif item['_DesignParametertype'] == 3:
                try:
                    class_name = item['_DesignObj'].__class__.__name__
                except:
                    pass
                if class_name == 'dict':
                    if item['_DesignObj_Name'] in self.design_obj_based_group:
                        self.design_obj_based_group[item['_DesignObj_Name']].append(key)
                    else:
                        self.design_obj_based_group[item['_DesignObj_Name']] = [key]
                elif class_name in self.design_obj_based_group:
                    self.design_obj_based_group[class_name].append(key)
                else:
                    self.design_obj_based_group[class_name] = [key]

    def layer_matching(self,matching_num_of_boundary=3, matching_num_of_path=3, matching_num_of_sref=1):

        for layer_number, layer_group_items in self.layer_based_group.items():
            tmp_groups = []
            """
            tmp_groups data examples...
            tmp_groups = [  [ele1_of_grp1, ele2_of_grp1, ... , eleN_of_grp1]  -> tmp_groups[0] = tmp_group...
                            [ele1_of_grp2, ele2_of_grp2, ... , eleN_of_grp2]
                            [ele1_of_grp3, ele2_of_grp3, ... , eleN_of_grp3]
                            ... ... ... ... ... ... ... ... ... ... ... ...
                            [ele1_of_grpN, ele2_of_grpN, ... , eleN_of_grpN]   ]
            """
            for layer_item_name in layer_group_items:
                if not tmp_groups:
                    tmp_groups.append([layer_item_name])
                else:
                    for i, tmp_group in enumerate(tmp_groups):
                        matching_num, design_type= self.compare_two_elements(tmp_group[0],layer_item_name)
                        if design_type == 'boundary':
                            if matching_num >= matching_num_of_boundary:
                                tmp_groups[i].append(layer_item_name)
                                break
                        elif design_type == 'path':
                            if matching_num >= matching_num_of_path:
                                tmp_groups[i].append(layer_item_name)
                                break
                        elif design_type == 'sref':
                            if matching_num >= matching_num_of_sref:
                                tmp_groups[i].append(layer_item_name)
                                break

                        #When all trials fail, create new group.
                        if len(tmp_groups)-1 == i:
                            tmp_groups.append([layer_item_name])
                            break
            self.array_groups.extend(tmp_groups)

    def sref_matching(self,matching_num_of_sref=1):
        for generator_name, generator_group_items in self.design_obj_based_group.items():
            tmp_groups = []
            for generator_instance_name in generator_group_items:
                if not tmp_groups:
                    tmp_groups.append([generator_instance_name])
                else:
                    for i, tmp_group in enumerate(tmp_groups):
                        matching_num = self.compare_two_srefs(tmp_group[0],generator_instance_name)
                        if matching_num == -1:
                            continue
                        elif matching_num == -2:
                            break
                        # matching_num, design_type = self.compare_two_srefs(tmp_group[0],generator_instance_name)

                        if matching_num >= matching_num_of_sref:
                            tmp_groups[i].append(generator_instance_name)
                            break

                        if len(tmp_groups) -1 == i:
                            tmp_groups.append([generator_instance_name])
                            break
            self.array_groups.extend(tmp_groups)



    def compare_two_elements(self, element1_name:str, element2_name:str) -> int :
        type1 = self._DesignParameter[element1_name]['_DesignParametertype']
        type2 = self._DesignParameter[element2_name]['_DesignParametertype']
        if len(self._DesignParameter[element1_name]['_XYCoordinates']) == 0 or len(self._DesignParameter[element2_name]['_XYCoordinates']) == 0:
            return -1, 'None'

        if type1 == type2 == 1:
            return self.compare_two_boundaries(element1_name, element2_name), 'boundary'
        elif type1 == type2 == 2:
            return self.compare_two_paths(element1_name, element2_name), 'path'
        elif type1 == type2 == 3:
            ref_structure_name1= self._DesignParameter[element1_name]['_DesignObj']._DesignParameter['_Name']['_Name']
            ref_structure_name2= self._DesignParameter[element2_name]['_DesignObj']._DesignParameter['_Name']['_Name']
            if ref_structure_name1 == ref_structure_name2:
                return self.compare_two_srefs(element1_name, element2_name), 'sref'
            else:
                return -1 , 'None'
        else:
            return -1, 'None'


    def compare_two_boundaries(self, bound1_name, bound2_name):
        x = self._DesignParameter[bound1_name]['_XYCoordinates'][0][0] == self._DesignParameter[bound2_name]['_XYCoordinates'][0][0]
        y = self._DesignParameter[bound1_name]['_XYCoordinates'][0][1] == self._DesignParameter[bound2_name]['_XYCoordinates'][0][1]
        xwidth = self._DesignParameter[bound1_name]['_XWidth'] == self._DesignParameter[bound2_name]['_XWidth']
        ywidth = self._DesignParameter[bound1_name]['_YWidth'] == self._DesignParameter[bound2_name]['_YWidth']
        return x+y+xwidth+ywidth

    def compare_two_paths(self,path1_name, path2_name):
        if not len(self._DesignParameter[path1_name]['_XYCoordinates'][0]) == len(self._DesignParameter[path2_name]['_XYCoordinates'][0]):
            return -1
        if self._DesignParameter[path1_name]['_XYCoordinates'][0][0][0] == self._DesignParameter[path1_name]['_XYCoordinates'][0][-1][0]:
            #vertical case
            x1, x2 = 0, 0
            y1 = self._DesignParameter[path1_name]['_XYCoordinates'][0][0][1] == self._DesignParameter[path2_name]['_XYCoordinates'][0][0][1]
            y2 = self._DesignParameter[path1_name]['_XYCoordinates'][0][-1][1] == \
                 self._DesignParameter[path2_name]['_XYCoordinates'][0][-1][1]
        else:
            x1 = self._DesignParameter[path1_name]['_XYCoordinates'][0][0][0] == \
                 self._DesignParameter[path2_name]['_XYCoordinates'][0][0][0]
            x2 = self._DesignParameter[path1_name]['_XYCoordinates'][0][-1][0] == \
                 self._DesignParameter[path2_name]['_XYCoordinates'][0][-1][0]
            y1, y2 = 0, 0

        # x1 = self._DesignParameter[path1_name]['_XYCoordinates'][0][0][0] == self._DesignParameter[path2_name]['_XYCoordinates'][0][0][0]
        # y1 = self._DesignParameter[path1_name]['_XYCoordinates'][0][0][1] == self._DesignParameter[path2_name]['_XYCoordinates'][0][0][1]
        # x2 = self._DesignParameter[path1_name]['_XYCoordinates'][0][-1][0] == self._DesignParameter[path2_name]['_XYCoordinates'][0][-1][0]
        # y2 = self._DesignParameter[path1_name]['_XYCoordinates'][0][-1][1] == self._DesignParameter[path2_name]['_XYCoordinates'][0][-1][1]
        width = self._DesignParameter[path1_name]['_Width'] == self._DesignParameter[path2_name]['_Width']
        return x1+y1+x2+y2+width

    def compare_two_srefs(self, sref1_name, sref2_name):
        #assumption... two sref has same design obj
        if len(self._DesignParameter[sref1_name]['_XYCoordinates']) == 0:
            return -1
        elif len(self._DesignParameter[sref2_name]['_XYCoordinates']) == 0:
            return -2
        x = self._DesignParameter[sref1_name]['_XYCoordinates'][0][0] == self._DesignParameter[sref2_name]['_XYCoordinates'][0][0]
        y = self._DesignParameter[sref1_name]['_XYCoordinates'][0][1] == self._DesignParameter[sref2_name]['_XYCoordinates'][0][1]
        return  x+y

    def intersection_matching_qt(self):
        intersection_matching_dict_by_name = dict()

        for key, qt_dp in self._qtDesignParameters.items():
            dp = qt_dp._DesignParameter
            # if dp['_DesignParametertype'] == 2 or dp['_DesignParametertype'] == 1:
            intersection_info = self.geo_searching.search_intersection(dp)
            if intersection_info is None:
                # return None
                continue
            self.routing_groups.append(intersection_info)
            intersection_matching_dict_by_name[intersection_info[0]['_ElementName']] = intersection_info[1:]
            # if intersection_matching_dict_by_name[intersection_info[0]['_id']]:
            #     intersection_matching_dict_by_name[intersection_info[0]['_id']].pop(0)
            # self.routing_groups.append(self.geo_searching.search_intersection(dp))
        self.intersection_matching_dict_by_name = intersection_matching_dict_by_name
        return intersection_matching_dict_by_name
        # return self.routing_groups

    def intersection_matching(self):
        for key, dp in self._DesignParameter.items():
            self.routing_groups.append(self.geo_searching.search_intersection(dp))

        return self.routing_groups


    def intersection_matching_path(self):
        path_routing_group = []
        for key, dp in self._DesignParameter.items():
            if dp['_DesignParametertype'] == 2:
                path_routing_group.append(self.geo_searching.search_intersection(dp))
        self.routing_groups.extend(path_routing_group)
                # self.routing_groups.append(self.geo_searching.search_intersection(dp))

        return path_routing_group

    def intersection_matching_boundary(self):
        boundary_reference_group = []
        for key, dp in self._DesignParameter.items():
            if dp['_DesignParametertype'] == 1:
                boundary_reference_group.append(self.geo_searching.search_intersection(dp))
                # self.routing_groups.append(self.geo_searching.search_intersection(dp))
        self.routing_groups.extend(boundary_reference_group)
        return boundary_reference_group

    def search_path_intersection_points(self, dp):
        return self.geo_searching.search_path_intersection_points(dp)

    def search_path_vertex_intersction(self, dp):
        return self.geo_searching.search_path_intersection_at_vertex(dp)

    def divide_false_pre_group(self):
        '''
        when the elements of pre-group have different interval, then seperate it two groups
        '''
        def find_min_value(list):
            min_value = list[0]
            for i in list:
                if i < min_value:
                    min_value = i
            return min_value

        def find_max_value(list):
            max_value = list[0]
            for i in list:
                if i > max_value:
                    max_value = i
            return max_value

        processed_group = []
        while self.array_groups:
            group_candidate = self.array_groups.pop(0)
            if 'precharge_left_pmos_supply' in group_candidate:
                print('debug')
            if len(group_candidate) == 1:
                continue
            dp_type = self._DesignParameter[group_candidate[0]]['_DesignParametertype']
            if dp_type == 1 or dp_type == 3:
                dp_x_coordinates = [self._DesignParameter[dp_name]['_XYCoordinates'][0][0] for dp_name in group_candidate]
                dp_y_coordinates = [self._DesignParameter[dp_name]['_XYCoordinates'][0][1] for dp_name in group_candidate]
            elif dp_type == 2:
                dp_x_coordinates = [self._DesignParameter[dp_name]['_XYCoordinates'][0][0][0] for dp_name in
                                    group_candidate]
                dp_y_coordinates = [self._DesignParameter[dp_name]['_XYCoordinates'][0][0][1] for dp_name in
                                    group_candidate]
                #check every elements of dp_x_coordinates has same value
            x_check = len(set(dp_x_coordinates))
            y_check = len(set(dp_y_coordinates))
            if x_check == 1 and y_check != 1:# same x value, different y value
                sorting_list = [(coord, name) for coord, name in zip(dp_y_coordinates, group_candidate)]
                sorting_list.sort(key=lambda x: x[0])
                # group_candidate.sort(key=lambda x: dp_y_coordinates)
                # dp_y_coordinates.sort()
                group_candidate = [name for coord, name in sorting_list]
                dp_y_coordinates = [coord for coord, name in sorting_list]
                # find dp_y_coordinates's element's value difference for every index
                dp_y_coordinates_diff = [dp_y_coordinates[i+1] - dp_y_coordinates[i] for i in range(len(dp_y_coordinates)-1)]
                # find the index of dp_y_coordinates_diff which has the differnt value
                diff_list = list(set(dp_y_coordinates_diff))
                if len(diff_list) == 1:
                    processed_group.append(group_candidate)
                    continue
                # elif len(diff_list) == 2:
                #     seperate_index = dp_y_coordinates_diff.index(find_min_value(dp_y_coordinates_diff))
                #     processed_group.append(group_candidate[:seperate_index])
                #     processed_group.append(group_candidate[seperate_index:])
                else:
                    diff_set=list(set(dp_y_coordinates_diff))
                    diff_count = [dp_y_coordinates_diff.count(diff_set[i]) for i in range(len(diff_set))]
                    min_count_value = find_min_value(diff_count)
                    if diff_set.count(min_count_value) == 1:
                        min_freq_value = diff_set[diff_count.index(find_min_value(diff_count))]
                        seperate_index = dp_y_coordinates_diff.index(min_freq_value)
                        processed_group.append(group_candidate[:seperate_index+1])
                        self.array_groups.append(group_candidate[seperate_index+1:])
                    else:
                        min_count_values = [diff_set[i] for i, x in enumerate(diff_count) if x == min_count_value]
                        seperate_index_list = [dp_y_coordinates_diff.index(x) for x in min_count_values]
                        seperate_index = find_min_value(seperate_index_list)
                        # processed_group.append(group_candidate[:seperate_index+1])
                        self.array_groups.append(group_candidate[:seperate_index+1])
                        self.array_groups.append(group_candidate[seperate_index+1:])

                    # idx_list = [dp_y_coordinates_diff.index(value) for value in diff_list]
                    # for i in range(len(idx_list)-1):
                    #     processed_group.append(group_candidate[idx_list[i]:idx_list[i+1]])
            elif x_check != 1 and y_check == 1:
                sorting_list = [(coord, name) for coord, name in zip(dp_x_coordinates, group_candidate)]
                sorting_list.sort(key=lambda x: x[0])
                group_candidate = [name for coord, name in sorting_list]
                dp_x_coordinates = [coord for coord, name in sorting_list]
                # group_candidate.sort(key=lambda x: dp_x_coordinates)
                # dp_x_coordinates.sort()
                dp_x_coordinates_diff = [dp_x_coordinates[i+1] - dp_x_coordinates[i] for i in range(len(dp_x_coordinates)-1)]
                diff_list = list(set(dp_x_coordinates_diff))
                if len(diff_list) == 1:
                    processed_group.append(group_candidate)
                    continue
                # elif len(diff_list) == 2:
                #     seperate_index = dp_x_coordinates_diff.index(find_min_value(dp_x_coordinates_diff))
                #     processed_group.append(group_candidate[:seperate_index])
                #     processed_group.append(group_candidate[seperate_index:])
                else:
                    diff_set=list(set(dp_x_coordinates_diff))
                    diff_count = [dp_x_coordinates_diff.count(diff_set[i]) for i in range(len(diff_set))]
                    min_count_value = find_min_value(diff_count)
                    if diff_set.count(min_count_value) == 1:
                        min_freq_value = diff_set[diff_count.index(find_min_value(diff_count))]
                        seperate_index = dp_x_coordinates_diff.index(min_freq_value)
                        processed_group.append(group_candidate[:seperate_index+1])
                        self.array_groups.append(group_candidate[seperate_index+1:])
                    else:
                        min_count_values = [diff_set[i] for i, x in enumerate(diff_count) if x == min_count_value]
                        seperate_index_list = [dp_x_coordinates_diff.index(x) for x in min_count_values]
                        seperate_index = find_min_value(seperate_index_list)
                        self.array_groups.append(group_candidate[:seperate_index+1])
                        self.array_groups.append(group_candidate[seperate_index+1:])

            else:
                continue
        self.array_groups = processed_group



# file = './smaple.csv'
# df_data = pd.read_csv(file)
# df_data.drop('Unnamed: 0',1, inplace=True)
# df_data.drop('element',1, inplace=True)
# df_data.drop('SNAME',1, inplace=True)
# df_data.fillna(0, inplace=True)
# # pca = PCA(n_components=2) # number of componenets
# pca = PCA(n_components=0.95) # variance ratio
# df_data = pca.fit_transform(df_data)
# df_data = RobustScaler().fit_transform(df_data)
# # df_data = RobustScaler().fit_transform(df_data)
# mds = MDS(n_components=2)
# # df_data = mds.fit_transform(df_data)
# dbscam = DBSCAN(eps=0.3, min_samples=2)
# dbscam.fit(df_data)
# print(dbscam.labels_)
#
# plt.scatter(x=df_data[:,0], y=df_data[:,1], c = dbscam.labels_)
# plt.show()
