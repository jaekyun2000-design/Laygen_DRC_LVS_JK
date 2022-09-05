import warnings
import math
from powertool.model import gds2generator
import numpy as np
class LayerToMatrix:
    def __init__(self, row=100, column=100, layer_list=None, generator_list=None):
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
        self.bounding_box=dict(matrix=np.empty((0,4)), label=np.array([]))
        self.generator_list = generator_list

    def load_qt_parameters(self, qt_parameters, minimum_step_size = None, matrix_size = None, bb =False):
        '''
        This is for legacy function for just classification purpose
        '''
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

    def calculate_bounding_box(self, target_dp):
        '''
        Args:
            target_dp:

        Returns:
            output: x start idx, y start idx, w, h
        '''
        cell_name = target_dp['_DesignObj'].__class__.__name__
        if cell_name in self.generator_list:
            label_idx = self.generator_list.index(cell_name)
        else:
            Exception ('{} is not in generator list'.format(cell_name))
        lb_xy = [target_dp['bounding_box'][0] + target_dp['_XYCoordinates'][0][0],
                 target_dp['bounding_box'][1] + target_dp['_XYCoordinates'][0][1]]
        x_width = target_dp['bounding_box'][2] - target_dp['bounding_box'][0]
        y_width = target_dp['bounding_box'][3] - target_dp['bounding_box'][1]
        xy_shifted_s = [a + b for a, b in zip(lb_xy, self.offset)]
        xy_shifted_e = [a + b for a, b in zip(xy_shifted_s, [x_width, y_width])]
        x_start_idx = int(xy_shifted_s[0] / self.x_step_size)
        y_start_idx = int(xy_shifted_s[1] / self.y_step_size)
        x_end_idx = math.ceil(xy_shifted_e[0] / self.x_step_size)
        y_end_idx = math.ceil(xy_shifted_e[1] / self.y_step_size)
        # self.bounding_box['matrix'].append([x_start_idx, y_start_idx, x_end_idx, y_end_idx])
        self.bounding_box['matrix'] = np.append(self.bounding_box['matrix'], np.array([[x_start_idx, y_start_idx, x_end_idx-x_start_idx, y_end_idx-y_start_idx]]), axis=0)
        self.bounding_box['label'] = np.append(self.bounding_box['label'], label_idx)

    def calculate_bounding_box_ratio(self, target_dp):
        cell_name = target_dp['_DesignObj'].__class__.__name__
        if cell_name in self.generator_list:
            label_idx = self.generator_list.index(cell_name)
        else:
            Exception('{} is not in generator list'.format(cell_name))
        lb_xy = [target_dp['bounding_box'][0] + target_dp['_XYCoordinates'][0][0],
                 target_dp['bounding_box'][1] + target_dp['_XYCoordinates'][0][1]]
        x_width = target_dp['bounding_box'][2] - target_dp['bounding_box'][0]
        y_width = target_dp['bounding_box'][3] - target_dp['bounding_box'][1]
        xy_shifted_s = [a + b for a, b in zip(lb_xy, self.offset)]
        xy_shifted_e = [a + b for a, b in zip(xy_shifted_s, [x_width, y_width])]
        x_start_idx = int(xy_shifted_s[0] / self.x_step_size)
        y_start_idx = int(xy_shifted_s[1] / self.y_step_size)
        x_end_idx = math.ceil(xy_shifted_e[0] / self.x_step_size)
        y_end_idx = math.ceil(xy_shifted_e[1] / self.y_step_size)
        x_start = x_start_idx/self.matrix_size[1]
        y_start = y_start_idx/self.matrix_size[0]
        x_end = x_end_idx/self.matrix_size[1]
        y_end = y_end_idx/self.matrix_size[0]
        # self.bounding_box['matrix'].append([x_start_idx, y_start_idx, x_end_idx, y_end_idx])
        self.bounding_box['matrix'] = np.append(self.bounding_box['matrix'], np.array(
            [[x_start, y_start, x_end, y_end]]), axis=0)
        self.bounding_box['label'] = np.append(self.bounding_box['label'], label_idx)


    def get_cell_size(self):
        return dict(width=self.cell_width, height=self.cell_height)

    def load_dp(self, dp, minimum_step_size = None, matrix_size = None, bb=True):
        '''
        Args:
            dp: DesignParameter from generator
            size_option ->
        Returns:
            output : not fixed matrix size
        '''
        reader = gds2generator.LayoutReader()
        reader.load_dp(dp)
        if minimum_step_size:
            self.y_step_size = minimum_step_size
            self.x_step_size = minimum_step_size
            self.matrix_size = (math.ceil((reader.y_max - reader.y_min)/self.y_step_size), math.ceil((reader.x_max - reader.x_min)/self.x_step_size))
        elif matrix_size:
            self.matrix_size = matrix_size
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

        if bb:
            for dp in dp.values():
                if dp['_DesignParametertype'] != 3:
                    continue
                # self.calculate_bounding_box(dp)
                self.calculate_bounding_box_ratio(dp)

    def divide_matrix(self, ratio):
        '''
        Args:
            # matrix: matrix to be divided
            ratio: ratio of division
        Returns:
            divided matrix
        '''
        # self.matrix_by_layer
        # shape = list(self.matrix_by_layer.values())[0].shape
        x_shape = self.matrix_size[0]
        y_shape = self.matrix_size[1]
        x_step = int(x_shape / ratio)
        y_step = int(y_shape / ratio)

        x_divided_iter = round(x_shape / x_step + 0.5) #ceil
        y_divided_iter = round(y_shape / y_step + 0.5) #ceil
        print(x_divided_iter, y_divided_iter)


        for x_div in range(x_divided_iter):
            for y_div in range(y_divided_iter):
                tmp_dictionary = {layer: matrix[x_div*x_step:x_div*x_step+x_step, y_div*y_step:y_div*y_step+y_step] for layer, matrix in self.matrix_by_layer.items()}
                yield tmp_dictionary
                # yield matrix[x_step*x_div:x_step*(x_div+1), y_step*y_div:y_step*(y_div+1), :]
        yield self.matrix_by_layer

    def convert_coordinate(self, original_xy, sref_xy):
        sref_shifted_xy = [a + b for a, b in zip(original_xy, sref_xy)]
        offset_shifted_xy = [a + b for a, b in zip(sref_shifted_xy, self.offset)]
        x_idx = int(offset_shifted_xy[0] / self.x_step_size)
        y_idx = int(offset_shifted_xy[1] / self.y_step_size)
        x = x_idx / self.matrix_size[1]
        y = y_idx / self.matrix_size[0]
        return x, y

if __name__ == '__main__':
    # reader = gds2generator.LayoutReader()
    # reader.load_gds('./layout_rand_gen/dataset/NMOS/0.gds', root_cell_name='0')
    # len(reader)
    import os
    #print cwd
    lay_to_mat = LayerToMatrix(100,100)
    lay_to_mat.load_gds('./PyQTInterface/GDSFile/rdgen/via122.gds', '999')
    import matplotlib.pyplot as plt
    #
    for layer, value in lay_to_mat.matrix_by_layer.items():
        print(layer)
        plt.imshow(value[:, :])
        plt.show()
    layer_list = lay_to_mat.matrix_by_layer.keys()
    single_data = None
    stacked_matrix = None
    for layer in lay_to_mat.matrix_by_layer.keys():
        if type(stacked_matrix) == np.ndarray:
            stacked_matrix = np.append(stacked_matrix, np.expand_dims(np.array(lay_to_mat.matrix_by_layer[layer]), 2),
                                       axis=2)
        else:
            stacked_matrix = np.expand_dims(np.array(lay_to_mat.matrix_by_layer[layer]), 2)
    single_data = np.array([stacked_matrix])
    single_data = single_data.reshape(1, 100, 100, len(layer_list))
    import matplotlib.pyplot as plt

    for i in range(len(lay_to_mat.matrix_by_layer.keys())):
        plt.imshow(single_data[0, :, :, i])
        plt.show()