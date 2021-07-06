import sys, inspect
from generatorLib import DRC

tmp = __import__('DRC')
class_members = inspect.getmembers(tmp, inspect.isclass)
print(class_members)
# iter_class_members = [iter_class for iter_class in class_members if iter_class[1].__base__ == IterationElement]
# generator_class_members = [iter_class for iter_class in class_members if iter_class[1].__base__ == GeneratorVariable]
