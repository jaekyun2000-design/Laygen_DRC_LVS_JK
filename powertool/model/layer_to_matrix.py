import warnings
import math
from powertool.model import gds2generator
import numpy as np
class LayerToMatrix:
    def __init__(self, row, column, layer_list=None):
        self.matrix_size = (row,column)
        self.matrix_by_layer = dict()
        if not layer_list:
            warnings.warn('If you do not describe layer list, then dimension problem might happens at dl stage')
        else:
            for layer in layer_list:
                self.matrix_by_layer[layer] = np.zeros(self.matrix_size)
        self.y_step_size = None
        self.x_step_size = None
        self.offset = None
        self.cell_width=None
        self.cell_height=None

    def load_qt_parameters(self, qt_parameters):
        reader = gds2generator.LayoutReader()
        reader.load_qt_design_parameters(qt_parameters)
        self.y_step_size = (reader.y_max - reader.y_min) / self.matrix_size[0]
        self.x_step_size = (reader.x_max - reader.x_min) / self.matrix_size[1]
        self.offset = (-reader.x_min, -reader.y_min)
        self.cell_width = reader.x_max - reader.x_min
        self.cell_height = reader.y_max - reader.y_min
        for layer_name, node_list in reader.layer_elements.items():
            if layer_name not in self.matrix_by_layer:
                self.matrix_by_layer[layer_name] = np.zeros(self.matrix_size)

            for node in node_list:
                col_idx, row_idx = self.calculate_row_col(node)
                self.matrix_by_layer[layer_name][row_idx[0]:row_idx[1], col_idx[0]:col_idx[1]] = 1


    def load_gds(self, gds_name, cell_name):
        reader = gds2generator.LayoutReader()
        reader.load_gds(gds_name, cell_name)
        self.y_step_size = (reader.y_max - reader.y_min) / self.matrix_size[0]
        self.x_step_size = (reader.x_max - reader.x_min) / self.matrix_size[1]
        self.offset = (-reader.x_min, -reader.y_min)
        self.cell_width = reader.x_max - reader.x_min
        self.cell_height = reader.y_max - reader.y_min
        for layer_name, node_list in reader.layer_elements.items():
            if layer_name not in self.matrix_by_layer:
                self.matrix_by_layer[layer_name] = np.zeros(self.matrix_size)

            for node in node_list:
                col_idx, row_idx = self.calculate_row_col(node)
                self.matrix_by_layer[layer_name][row_idx[0]:row_idx[1],col_idx[0]:col_idx[1]] = 1



    def calculate_row_col(self,node):
        xy_shifted_s = [a + b for a,b in zip(node.lb_xy, self.offset)]
        xy_shifted_e = [a + b for a,b in zip(xy_shifted_s, [node.x_width, node.y_width])]
        x_start_idx = int(xy_shifted_s[0]/self.x_step_size)
        y_start_idx = int(xy_shifted_s[1]/self.y_step_size)
        x_end_idx = math.ceil(xy_shifted_e[0]/self.x_step_size)
        y_end_idx = math.ceil(xy_shifted_e[1]/self.y_step_size)
        return [x_start_idx,x_end_idx], [y_start_idx,y_end_idx]

    def get_cell_size(self):
        return dict(width=self.cell_width, height=self.cell_height)
        # return dict(width=self.offset[0] + self.x_step_size*self.matrix_size[1],
        #             height=self.offset[1] + self.y_step_size*self.matrix_size[0])


if __name__ == '__main__':
    # reader = gds2generator.LayoutReader()
    # reader.load_gds('./layout_rand_gen/dataset/NMOS/0.gds', root_cell_name='0')
    # len(reader)
    lay_to_mat = LayerToMatrix(100,100)
    lay_to_mat.load_gds('./layout_rand_gen/dataset/C2FF/0.gds', '0')