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

from model import routing_geo_searching

import copy

class clustering():
    def __init__(self, _DesignParameters = None):
        self._DesignParameter = copy.deepcopy(_DesignParameters)
        self.array_groups = []
        self.routing_groups = []
        self.geo_searching = routing_geo_searching.GeometricField()
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

    def build_layer_ist(self):
        self.geo_searching.xy_projection_to_main_coordinates_system(self._DesignParameter)
        self.geo_searching.build_IST(self._DesignParameter)
        return self._DesignParameter

    def delete_solo_element_group(self):
        delete_index_list = []
        for i, group in enumerate(self.array_groups):
            if len(group) is 1:
                delete_index_list.append(i)
        for idx in reversed(delete_index_list):
            del self.array_groups[idx]

        delete_index_list = []
        for i, group in enumerate(self.routing_groups):
            if len(group) is 1 :
                delete_index_list.append(i)
        for idx in reversed(delete_index_list):
            del self.routing_groups[idx]



    def get_array_groups(self):
        return self.array_groups

    def get_routing_groups(self):
        return self.routing_groups




class determinstic_clustering(clustering):
    def __init__(self, _DesignParameters = None):
        super().__init__(_DesignParameters)
        self.layer_based_group = dict()
        self.design_obj_based_group = dict()
        self.pregrouping_by_layer()
        # self.layer_matching()

    def pregrouping_by_layer(self):
        for key, item in self._DesignParameter.items():
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
                        if design_type is 'boundary':
                            if matching_num >= matching_num_of_boundary:
                                tmp_groups[i].append(layer_item_name)
                                break
                        elif design_type is 'path':
                            if matching_num >= matching_num_of_path:
                                tmp_groups[i].append(layer_item_name)
                                break
                        elif design_type is 'sref':
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
                        matching_num, design_type = self.compare_two_srefs(tmp_group[0],generator_instance_name)

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
        x1 = self._DesignParameter[path1_name]['_XYCoordinates'][0][0][0] == self._DesignParameter[path2_name]['_XYCoordinates'][0][0][0]
        y1 = self._DesignParameter[path1_name]['_XYCoordinates'][0][0][1] == self._DesignParameter[path2_name]['_XYCoordinates'][0][0][1]
        x2 = self._DesignParameter[path1_name]['_XYCoordinates'][0][-1][0] == self._DesignParameter[path2_name]['_XYCoordinates'][0][-1][0]
        y2 = self._DesignParameter[path1_name]['_XYCoordinates'][0][-1][1] == self._DesignParameter[path2_name]['_XYCoordinates'][0][-1][1]
        width = self._DesignParameter[path1_name]['_Width'] == self._DesignParameter[path2_name]['_Width']
        return x1+y1+x2+y2+width

    def compare_two_srefs(self, sref1_name, sref2_name):
        #assumption... two sref has same design obj
        x = self._DesignParameter[sref1_name]['_XYCoordinates'][0][0] == self._DesignParameter[sref2_name]['_XYCoordinates'][0][0]
        y = self._DesignParameter[sref1_name]['_XYCoordinates'][0][1] == self._DesignParameter[sref2_name]['_XYCoordinates'][0][1]
        return  x+y

    def intersection_matching_path(self):
        for key, dp in self._DesignParameter.items():
            if dp['_DesignParametertype'] == 2:
                self.routing_groups.append(self.geo_searching.search_intersection(dp))
        return self.routing_groups


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
