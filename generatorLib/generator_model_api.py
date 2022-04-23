import glob, os, sys, platform, user_setup
import sys, inspect

dir_check=os.getcwd()
if 'generator_model_path' in user_setup.__dict__ and user_setup.generator_model_path:
    generator_model_path = user_setup.generator_model_path
else:
    generator_model_path = './generatorLib/generator_models'

if 'generatorLib' in dir_check or 'PyQTInterface' in dir_check:
    os.chdir('..')
# sys.path.append('./generatorLib/generator_models')
sys.path.append(generator_model_path)

class Parm:
    def __init__(self, name, default):
        self.name = name
        self.default = default
        self.check_value()

    def check_value(self):
        if type(self.default) == str:
            if (self.default[0] == '\'' and self.default[-1] == '\'') or (self.default[0] == '\"' and self.default[-1] == '\"'):
                return
            else:
                self.default = f"\'{self.default}\'"

print("*********Generator Library Loading Start")

generator_list = []
class_dict = dict()
class_name_dict = dict()
class_function_dict = dict()
libraries = dict()
for generator in glob.iglob(f'{generator_model_path}/*.py'):
    if platform.system() in ['Linux', 'Darwin']:
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
                args_list = [Parm(arg.name, arg.default) for arg in args]
                class_function_dict[generator_class_name][fcn_name] = args_list
                # class_function_dict[generator_class_name][fcn_name] = inspect.signature(fcn_obj)


            # class_function_dict[generator_class_name]
            # print([name for name, obj in inspect.getmembers(obj)])



print("************Generator Library Loading Complete")
