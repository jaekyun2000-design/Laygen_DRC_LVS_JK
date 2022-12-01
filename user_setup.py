
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
DL_threshold = 0.95
DDL_FEATURE = False
DL_Parameter = False
DL_DETECTION = False
min_step_size = 10

model_dir = './powertool/dl_models/ss28/c5_sigmoid_wf'

exp_data = False


def update_user_setup(key, value):
    glo = globals()
    if key in glo:
        if value in ["True", "False"] or value.isdigit() or (value[0] == '[' and value[-1] == ']'):
            value = eval(value)
        glo[key] = value

def import_user_setup_from_template():
    import user_setup_template
    glo = globals()
    for key in user_setup_template.__dict__:
        if key not in glo:
            glo[key] = user_setup_template.__dict__[key]

import_user_setup_from_template()
