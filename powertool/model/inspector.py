import copy

from powertool import topAPI



class inspector:
    def __init__(self, qt_design_parameters):
        self.load_qt_design_parameters(qt_design_parameters)
        self.cluster_model = topAPI.clustering.determinstic_clustering(_qtDesignParameters=qt_design_parameters)
    def load_qt_design_parameters(self, qt_design_parameters):
        self.qt_design_parameters = copy.deepcopy(qt_design_parameters)

    def inspect(self):
        pass

    

class array_inspector(inspector):
    def __init__(self, qt_design_parameters):
        super(array_inspector, self).__init__(qt_design_parameters)

        self.cluster_model.layer_matching()
        self.cluster_model.sref_matching()
        self.cluster_model.build_layer_ist_qt()
        self.cluster_model.intersection_matching_qt()
        self.cluster_model.delete_solo_element_group()

    def inspect(self):
        group_list = self.cluster_model.get_array_groups()
        reference_list = self.cluster_model.find_ref(group_list)
        if reference_list == None:
            return
        else:
            return dict(group_list = group_list, reference_list=reference_list)

    def inspect_group(self, group:list):
        reference_list = self.cluster_model.find_ref([group])
        if reference_list:
            return reference_list[0]
        else:
            return None


    def get_all_connection_info(self):
        return self.cluster_model.get_routing_groups()

class path_point_inspector(inspector):
    def __init__(self, qt_design_parameters):
        super(path_point_inspector, self).__init__(qt_design_parameters)
        self.cluster_model.build_layer_ist_qt()
        self.path_list = []
        self._load_path_list()

    def _load_path_list(self):
        for qt_dp in self.qt_design_parameters.values():
            if qt_dp._type == 2:
                self.path_list.append(qt_dp._DesignParameter)

    def _inspect_path_connection(self, path):
        return self.cluster_model.search_path_intersection_points(path)


    def get_all_path_connection_info(self):
        path_connection_info_list = []
        for path in self.path_list:
            path_connection_info_list.append(self._inspect_path_connection(path))

        return dict(path_list = self.path_list, path_connection_info = path_connection_info_list)