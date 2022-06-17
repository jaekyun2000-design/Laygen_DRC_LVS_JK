from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import nmos_stack_current_mirror



class EasyDebugModule(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  nmos_stack_coarse_param={'nmos1_width':2000,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_stack_fine_param={'nmos1_width':500,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_stack_mirror_param={'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False,'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30,'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False,'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2,'guardring_width': None, 'guardring_height': None, 'diode_connect': False},\
                                  guardring_width=None, guardring_height=None, coarse_num=3, fine_num=4, mirror_num=1, Xnum=3, Ynum=4):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        _OriginXY=[[0,0]]

        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_mirror_param))

        if guardring_width==None :
            max_guardring_width=max(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0])

        elif guardring_width!=None :
            max_guardring_width=guardring_width

        if guardring_height==None :
            max_guardring_height=max(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1])

        elif guardring_height!=None :
            max_guardring_height=guardring_height

        nmos_stack_coarse_param['guardring_width']=max_guardring_width
        nmos_stack_coarse_param['guardring_height']=max_guardring_height
        nmos_stack_coarse_param['diode_connect']=True

        nmos_stack_fine_param['guardring_width']=max_guardring_width
        nmos_stack_fine_param['guardring_height']=max_guardring_height
        nmos_stack_fine_param['diode_connect']=True

        nmos_stack_mirror_param['guardring_width']=max_guardring_width
        nmos_stack_mirror_param['guardring_height']=max_guardring_height
        nmos_stack_mirror_param['diode_connect']=False


        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_mirror_param))

        yoffset_coarse=(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1])
        yoffset_fine=(self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1])
        yoffset_mirror=(self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1])


        tmp_array=[]
        tmp_coarse=[]
        tmp_fine=[]
        tmp_mirror=[]

        for j in range(0, Ynum):
            for i in range(0, Xnum):
                tmp_array.append([_OriginXY[0][0]-(Xnum-1)/2*max_guardring_width+i*max_guardring_width,_OriginXY[0][1]+(Ynum-1)/2*max_guardring_height-j*max_guardring_height])

        for i in range(0, coarse_num) :
            tmp_coarse.append([tmp_array[i][0], tmp_array[i][1]-yoffset_coarse])

        for j in range(0, fine_num) :
            tmp_fine.append([tmp_array[coarse_num+j][0], tmp_array[coarse_num+j][1]-yoffset_fine])

        for k in range(0, mirror_num) :
            tmp_mirror.append([tmp_array[coarse_num+fine_num+k][0], tmp_array[coarse_num+fine_num+k][1]-yoffset_mirror])

        self._DesignParameter['nmos_coarse']['_XYCoordinates']=tmp_coarse
        self._DesignParameter['nmos_fine']['_XYCoordinates']=tmp_fine
        self._DesignParameter['nmos_mirror']['_XYCoordinates']=tmp_mirror

        del tmp_array
        del tmp_coarse
        del tmp_fine
        del tmp_mirror

        if coarse_num+fine_num+mirror_num > Xnum*Ynum :
            raise NotImplementedError



