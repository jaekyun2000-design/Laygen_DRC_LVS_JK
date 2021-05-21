import glob, os, sys, platform
import sys, inspect

sys.path.append('./generatorLib/generator_models')
print("*********************Generator Library Loading Start")

generator_list = []
class_dict = dict()
class_name_dict = dict()
libraries = dict()
for generator in glob.iglob('./generatorLib/generator_models/*.py'):
    if platform.system() == 'Linux':
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

print("************************Generator Library Loading Complete")
