
_Technology='SS28nm'
_Night_mode = True
_Snap_mode = 'orthogonal' # orthogonal or any_angle
DEBUG = False
MIN_SNAP_SPACING = 1
GDS2GEN = True
MULTI_THREAD = True
MULTI_THREAD_NUM = 5
FTP_UPLOAD = True
AUTO_IMPORT = True

CALCULATOR_MODE = 'Arithmetic'  # or 'Calculator'

generator_model_path = None # If none, default path will be set.
# generator_model_path = './generatorLib/generator_models/rx_project' # If none, default path will be set.

project_file_path = None # If none, default path will be set.
# project_file_path = './PyQTInterface/Project/rx_project' # If none, default path will be set.

#########################################################
# for cell detector model setup #
DL_FEATURE = False
DDL_FEATURE = False
DL_Parameter = False
DL_DETECTION = False
min_step_size = 10


matrix_x_step = 100
matrix_y_step = 100

layer_list = ['DIFF','PIMP','POLY','METAL1', 'METAL2', 'METAL3', 'METAL4', 'METAL5', 'PRES','METAL6','METAL7', 'NWELL']
data_type_list = ['Inverter','NSubRing','PSubRing','NMOSWithDummy','PMOSWithDummy','NbodyContact','PbodyContact','ViaPoly2Met1','ViaMet12Met2', 'ViaMet22Met3','ViaMet32Met4','ViaMet42Met5','ViaMet52Met6',
                  'ViaMet62Met7', 'PolyResistor','SRLatch','StrongArmLatch','TransmissionGate','Slicer','ResistorBankUnit']

exp_data = False



def update_user_setup(key, value):
    glo = globals()
    if key in glo:
        if value in ["True", "False"] or value.isdigit() or (value[0] == '[' and value[-1] == ']'):
            value = eval(value)
        glo[key] = value
