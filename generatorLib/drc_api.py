import sys, inspect
import re
from generatorLib import DRC
import user_setup

def run_for_process_update():

    global drc_classified_dict

    tmp = DRC
    tmp._Technology = user_setup._Technology
    class_members = inspect.getmembers(tmp, inspect.isclass)
    # elements = inspect.getmembers(tmp)
    drc_dict = dict()
    func_dict = dict()

    drc_classified_dict = dict()


    for name, obj in inspect.getmembers(tmp):
        arg_list = []
        if inspect.isclass(obj):
            drc_dict[name] = obj
            for func_name, func_obj in inspect.getmembers(obj, inspect.isfunction):
                func_dict[func_name] = func_obj
                func_args = inspect.getcallargs(func_obj, 'self')
                for key, value in func_args.items():
                    if key == 'self':
                        continue
                    arg_list.append(key)
                drc_dict[func_name] = dict(func_obj = func_obj, motherClass = name, arg_list = arg_list)
                arg_list.clear()


    for drcName, obj in drc_dict.items():
        if type(obj) != dict:
            """
            class object filtering
            """
            temp = drc_dict[drcName]().__dict__
            drc_classified_dict[drcName] = temp
        else:
            pass

    for drcName, obj in drc_dict.items():
        if type(obj) == dict:
            drc_classified_dict[obj['motherClass']][drcName] = obj['arg_list']


    # func_dict['DRCMETAL1MinSpace'](drc_dict['DRCMETAL1'](),None,None)
    drc_classified_dict['CONT'] = drc_classified_dict.pop('DRCCO')
    drc_classified_dict['NIMP'] = drc_classified_dict.pop('DRCNP')
    drc_classified_dict['NWELL'] = drc_classified_dict.pop('DRCNW')
    drc_classified_dict['PIMP'] = drc_classified_dict.pop('DRCPP')
    drc_classified_dict['DIFF'] = drc_classified_dict.pop('DRCOD')
    drc_classified_dict['RPO'] = drc_classified_dict.pop('DRCRPO')
    drc_classified_dict['POLY'] = drc_classified_dict.pop('DRCPOLYGATE')
    drc_classified_dict['METAL1'] = drc_classified_dict.pop('DRCMETAL1')
    drc_classified_dict['METALx'] = drc_classified_dict.pop('DRCMETALx')
    drc_classified_dict['MIN_SNAP_SPACING'] = drc_classified_dict.pop('DRCMinSnapSpacing')

    user_setup.MIN_SNAP_SPACING = drc_classified_dict['MIN_SNAP_SPACING']['_MinSnapSpacing']

    del drc_classified_dict['DRC']



run_for_process_update()
print("*DRC Load Done")