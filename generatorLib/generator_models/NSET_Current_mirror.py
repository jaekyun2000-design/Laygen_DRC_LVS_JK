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
                                  nmos_stack_coarse_param1={'nmos1_width':2000,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_stack_fine_param2={'nmos1_width':500,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_stack_non_diode_param={'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False,'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30,'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False,'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2,'guardring_width': None, 'guardring_height': None, 'diode_connect': False},\
                                  guardring_width=None, guardring_height=None, input_matrix=[[]]):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']


        self._DesignParameter['nmos_tail_stack1'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_tail_stack1In{}'.format(_Name)))[0]
        self._DesignParameter['nmos_tail_stack1']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param1))

        self._DesignParameter['nmos_tail_stack2'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_tail_stack2In{}'.format(_Name)))[0]
        self._DesignParameter['nmos_tail_stack2']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param2))

        self._DesignParameter['nmos_tail_stack_non_diode'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_tail_stack_non_diodeIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_tail_stack_non_diode']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_non_diode_param))

        if guardring_width==None :
            max_guardring_width=max(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_tail_single']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_tail_single']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_tail_stack1']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_tail_stack1']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_tail_stack2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_tail_stack2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_tail_stack_non_diode']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_tail_stack_non_diode']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0])

        elif guardring_width!=None :
            max_guardring_width=guardring_width

        if guardring_height==None :
            max_guardring_height=max(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_tail_single']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_tail_single']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_tail_stack1']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_tail_stack1']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_tail_stack2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_tail_stack2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_tail_stack_non_diode']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_tail_stack_non_diode']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1])

        elif guardring_height!=None :
            max_guardring_height=guardring_height

        nmos_stack_coarse_param1['guardring_width']=max_guardring_width
        nmos_stack_coarse_param1['guardring_height']=max_guardring_height
        nmos_stack_coarse_param1['diode_connect']=True

        nmos_stack_fine_param2['guardring_width']=max_guardring_width
        nmos_stack_fine_param2['guardring_height']=max_guardring_height
        nmos_stack_fine_param2['diode_connect']=True

        nmos_stack_non_diode_param['guardring_width']=max_guardring_width
        nmos_stack_non_diode_param['guardring_height']=max_guardring_height
        nmos_stack_non_diode_param['diode_connect']=False


        self._DesignParameter['nmos_tail_stack1'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_tail_stack1In{}'.format(_Name)))[0]
        self._DesignParameter['nmos_tail_stack1']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param1))

        self._DesignParameter['nmos_tail_stack2'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_tail_stack2In{}'.format(_Name)))[0]
        self._DesignParameter['nmos_tail_stack2']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param2))

        self._DesignParameter['nmos_tail_stack_non_diode'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_tail_stack_non_diodeIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_tail_stack_non_diode']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_non_diode_param))


        _tmpwidth=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]
        _tmpheight=self._DesignParameter['nmos_tail_single']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_tail_single']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]


        self._DesignParameter['nmos']['_XYCoordinates'] = [[-_tmpwidth/2, 0],[_tmpwidth/2, 0]]



