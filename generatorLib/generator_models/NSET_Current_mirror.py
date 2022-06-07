from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import nmos_stack_current_mirror
from generatorLib.generator_models import nmos_single_current_mirror
from generatorLib.generator_models import nmos_single_tail_current_mirror



class EasyDebugModule(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  nmos_param={'nmos_gate':2,'nmos_width':1000,'nmos_length':30,'nmos_dummy':True,'xvt':'SLVT','pccrit':True,'guardring_right':2,'guardring_left':2,'guardring_bot':2,'guardring_top':2,'guardring_width':None,'guardring_height':None},
                                  nmos_tail_param={'nmos_gate':1,'nmos_width':2000,'nmos_length':500,'nmos_dummy':False,'xvt':'RVT','pccrit':False,'guardring_left':2,'guardring_right':2,'guardring_top':2,'guardring_bot':2,'guardring_width':None,'guardring_height':None},
                                  nmos_tail_stack_param1={'nmos1_width':2000,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_tail_stack_param2={'nmos1_width':2000,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_tail_stack_non_diode_param={'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False,'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30,'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False,'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2,'guardring_width': None, 'guardring_height': None, 'diode_connect': False}):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=nmos_single_current_mirror.EasyDebugModule(_Name='nmosIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_param))
        _tmplength=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]

        self._DesignParameter['nmos']['_XYCoordinates'] = [[-_tmplength/2, 0],[_tmplength/2, 0]]


