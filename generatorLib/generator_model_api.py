import glob, os, sys, platform
import sys, inspect

sys.path.append('./generatorLib/generator_models')
print("*********Generator Library Loading Start")

generator_list = []
class_dict = dict()
class_name_dict = dict()
class_function_dict = dict()
libraries = dict()
for generator in glob.iglob('./generatorLib/generator_models/*.py'):
    if platform.system() == 'Linux' or 'Darwin':
        generator_class_name = generator.split('/')[-1][:-3]
    else:
        generator_class_name = generator.split('\\')[1][:-3]
    generator_list.append(generator_class_name)
    tmp = __import__(generator_class_name)
    for name,obj in inspect.getmembers(tmp):
        if inspect.isclass(obj):
            # class_dict[generator_class_name] = dict(name=name,object=obj)
            class_dict[generator_class_name] = obj
            class_name_dict[generator_class_name] = name
            libraries[generator_class_name] = tmp
            # fcn_list = list(filter(lambda cal_fcn : "Calculate" in cal_fcn, [name for name, _ in inspect.getmembers(obj)]))
            fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if "Calculate" in fcn_name]
            class_function_dict[generator_class_name] = dict()
            for fcn_name, fcn_obj in fcn_list:
                args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                class_function_dict[generator_class_name][fcn_name] = args
                # class_function_dict[generator_class_name][fcn_name] = inspect.signature(fcn_obj)


            # class_function_dict[generator_class_name]
            # print([name for name, obj in inspect.getmembers(obj)])



print("************Generator Library Loading Complete")
