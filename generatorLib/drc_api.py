import sys, inspect
import re
from generatorLib import DRC

tmp = DRC
class_members = inspect.getmembers(tmp, inspect.isclass)
# elements = inspect.getmembers(tmp)
drc_dict = dict()
func_dict = dict()
drc_classified_dict = dict()

for name, obj in inspect.getmembers(tmp):
    if inspect.isclass(obj):
        drc_dict[name] = obj
        # drc_dict[name] = dict()
        for func_name, func_obj in inspect.getmembers(obj, inspect.isfunction):
            func_dict[func_name] = func_obj
            drc_dict[func_name] = dict(func_obj = func_obj, motherClass = name)
        # for func_name, objects in (obj.__dict__).items():
        #     if inspect.isfunction(objects) and re.search('DRC', func_name):
        #         func_dict[func_name] = objects
        #         drc_dict[func_name] = objects

for drcName, obj in drc_dict.items():
    if type(obj) != dict:
        temp = drc_dict[drcName]().__dict__
        drc_classified_dict[drcName] = temp
    else:
        pass

for drcName, obj in drc_dict.items():
    if type(obj) == dict:
        drc_classified_dict[obj['motherClass']][drcName] = obj['func_obj']


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
del drc_classified_dict['DRC']
