_Technology='SS28nm'
_Night_mode = True
_Snap_mode = 'orthogonal' # orthogonal or any_angle
DEBUG = True
MIN_SNAP_SPACING = 5
GDS2GEN = True




#########################################################
# for cell detector model setup #
DL_FEATURE = False

matrix_x_step = 256
matrix_y_step = 256
layer_list = ['DIFF','NIMP','PIMP','POLY','CONT','METAL1', 'METAL2', 'METAL3', 'METAL4', 'METAL5']
data_type_list = ['C2FF','XOR','NMOSWithDummy','PMOSWithDummy','NbodyContact','PbodyContact','ViaPoly2Met1','ViaMet12Met2', 'ViaMet22Met3','ViaMet32Met4','ViaMet42Met5']
#########################################################