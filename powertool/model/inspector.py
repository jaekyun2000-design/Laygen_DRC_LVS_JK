from powertool import topAPI



class inspector:
    def __init__(self, qt_design_parameters):
        self.load_qt_design_parameters(qt_design_parameters)

    def load_qt_design_parameters(self, qt_design_parameters):
        pass

    def inspect(self):
        pass

    

class array_inspector(inspector):
    def __init__(self, qt_design_parameters):
        super(array_inspector, self).__init__(qt_design_parameters)
        self.cluster_model = topAPI.clustering.determinstic_clustering(_qtDesignParameters=qt_design_parameters)
        self.cluster_model.layer_matching()
        self.cluster_model.sref_matching()
        self.cluster_model.build_layer_ist_qt()
        self.cluster_model.intersection_matching_qt()
        self.cluster_model.delete_solo_element_group()

    def inspect(self):
        group_list = self.cluster_model.get_array_groups()
        reference_list = self.cluster_model.find_ref(group_list)
        return dict(group_list = group_list, reference_list=reference_list)

    def get_all_connection_info(self):
        return self.cluster_model.get_routing_groups()


