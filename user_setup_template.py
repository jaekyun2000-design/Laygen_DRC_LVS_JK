
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

# generator_model_path = None # If none, default path will be set.
generator_model_path = './generatorLib/generator_models/rx_project' # If none, default path will be set.

# project_file_path = None # If none, default path will be set.
project_file_path = './PyQTInterface/Project/rx_project' # If none, default path will be set.

#########################################################
# for cell detector model setup #
DL_FEATURE = True
DL_threshold = 0.95
DDL_FEATURE = False
DL_Parameter = False
DL_DETECTION = False
min_step_size = 10

model_dir = './powertool/dl_models/ss28/c5_sigmoid_wf'

exp_data = True



