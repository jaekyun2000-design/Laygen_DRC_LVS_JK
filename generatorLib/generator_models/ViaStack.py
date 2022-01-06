from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import ViaMet42Met5
from generatorLib.generator_models import ViaMet52Met6
from generatorLib.generator_models import ViaMet72Met8
import inspect

class _ViaStack(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


    def _CalculateStack(self, COX=None, COY=None, start_layer=None, end_layer=None ):
        layer_list = range(start_layer, end_layer)
        for layer in layer_list:
            if layer == 0 :
                lib_name = 'ViaPoly2Met1'
            else:
                lib_name = f'ViaMet{layer}2Met{layer+1}'
            lib = __import__(lib_name)
            for name, obj in inspect.getmembers(lib):
                if inspect.isclass(obj):
                    class_obj = obj
                    fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if
                                "Calculate" in fcn_name]
                    fcn_list2 = list(
                        filter(lambda fcn: 'Enclosure' not in fcn[0] and 'DesignParameter' in fcn[0], fcn_list))
                    fcn_obj = fcn_list2[0][1]
                    fcn_name = fcn_list2[0][0]
                    args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                    args_name = [arg.name for arg in args]
                    break
            self._DesignParameter[lib_name] = self._SrefElementDeclaration(_DesignObj=class_obj(_Name=f"{lib_name}in{self._DesignParameter['_Name']['_Name']}"))[0]
            calculate_fcn = getattr(self._DesignParameter[lib_name]['_DesignObj'], fcn_name)
            cox = list(filter(lambda arg: 'COX' in arg, args_name))[0]
            coy = list(filter(lambda arg: 'COY' in arg, args_name))[0]
            parameters = {cox : COX, coy: COY}
            calculate_fcn(**parameters)
            self._DesignParameter[lib_name]['_XYCoordinates'] = [[0,0]]

    def _CalculateStackMinimumEnclosureX(self, COX=None, COY=None, start_layer=None, end_layer=None ):
        layer_list = range(start_layer, end_layer)
        for layer in layer_list:
            if layer == 0 :
                lib_name = 'ViaPoly2Met1'
            else:
                lib_name = f'ViaMet{layer}2Met{layer+1}'
            lib = __import__(lib_name)
            for name, obj in inspect.getmembers(lib):
                if inspect.isclass(obj):
                    class_obj = obj
                    fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if
                                "Calculate" in fcn_name]
                    fcn_list2 = list(
                        filter(lambda fcn: 'EnclosureX' in fcn[0] and 'DesignParameter' in fcn[0], fcn_list))
                    fcn_obj = fcn_list2[0][1]
                    fcn_name = fcn_list2[0][0]
                    args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                    args_name = [arg.name for arg in args]
                    break
            self._DesignParameter[lib_name] = self._SrefElementDeclaration(_DesignObj=class_obj(_Name=f"{lib_name}in{self._DesignParameter['_Name']['_Name']}"))[0]
            calculate_fcn = getattr(self._DesignParameter[lib_name]['_DesignObj'], fcn_name)
            cox = list(filter(lambda arg: 'COX' in arg, args_name))[0]
            coy = list(filter(lambda arg: 'COY' in arg, args_name))[0]
            parameters = {cox : COX, coy: COY}
            calculate_fcn(**parameters)
            self._DesignParameter[lib_name]['_XYCoordinates'] = [[0,0]]

    def _CalculateStackMinimumEnclosureY(self, COX=None, COY=None, start_layer=None, end_layer=None ):
        layer_list = range(start_layer, end_layer)
        for layer in layer_list:
            if layer == 0 :
                lib_name = 'ViaPoly2Met1'
            else:
                lib_name = f'ViaMet{layer}2Met{layer+1}'
            lib = __import__(lib_name)
            for name, obj in inspect.getmembers(lib):
                if inspect.isclass(obj):
                    class_obj = obj
                    fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if
                                "Calculate" in fcn_name]
                    fcn_list2 = list(
                        filter(lambda fcn: 'EnclosureY' in fcn[0] and 'DesignParameter' in fcn[0], fcn_list))
                    fcn_obj = fcn_list2[0][1]
                    fcn_name = fcn_list2[0][0]
                    args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                    args_name = [arg.name for arg in args]
                    break
            self._DesignParameter[lib_name] = self._SrefElementDeclaration(_DesignObj=class_obj(_Name=f"{lib_name}in{self._DesignParameter['_Name']['_Name']}"))[0]
            calculate_fcn = getattr(self._DesignParameter[lib_name]['_DesignObj'], fcn_name)
            cox = list(filter(lambda arg: 'COX' in arg, args_name))[0]
            coy = list(filter(lambda arg: 'COY' in arg, args_name))[0]
            parameters = {cox : COX, coy: COY}
            calculate_fcn(**parameters)
            self._DesignParameter[lib_name]['_XYCoordinates'] = [[0,0]]

