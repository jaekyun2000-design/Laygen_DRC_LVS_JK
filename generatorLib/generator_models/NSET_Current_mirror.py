from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import nmos_stack_current_mirror
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import nmos_single_current_mirror
from generatorLib.generator_models import nmos_single_tail_current_mirror

class EasyDebugModule(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter_v1(self,
                                  nmos_stack_coarse_param={'nmos1_width':2000,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_stack_fine_param={'nmos1_width':500,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_stack_mirror_param={'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False,'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30,'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False,'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2,'guardring_width': None, 'guardring_height': None, 'diode_connect': False},\
                                  guardring_width=None, guardring_height=None, coarse_num=3, fine_num=4, mirror_num=1, Xnum=3, Ynum=3):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing=drc._MinSnapSpacing

        _OriginXY=[[0,0]]

        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_mirror_param))

        if guardring_width==None :
            max_guardring_width=self.CeilMinSnapSpacing(max(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]), 2*MinSnapSpacing)

        elif guardring_width!=None :
            max_guardring_width=guardring_width

        if guardring_height==None :
            max_guardring_height=self.CeilMinSnapSpacing(max(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]), 2*MinSnapSpacing)

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
                tmp_array.append([self.CeilMinSnapSpacing(_OriginXY[0][0]-(Xnum-1)/2*max_guardring_width+i*max_guardring_width, 2*MinSnapSpacing),self.CeilMinSnapSpacing(_OriginXY[0][1]+(Ynum-1)/2*max_guardring_height-j*max_guardring_height, 2*MinSnapSpacing)])

        for i in range(0, coarse_num) :
            tmp_coarse.append([tmp_array[i][0], tmp_array[i][1]-yoffset_coarse])

        for j in range(0, fine_num) :
            tmp_fine.append([tmp_array[coarse_num+j][0], tmp_array[coarse_num+j][1]-yoffset_fine])

        for k in range(0, mirror_num) :
            tmp_mirror.append([tmp_array[coarse_num+fine_num+k][0], tmp_array[coarse_num+fine_num+k][1]-yoffset_mirror])

        self._DesignParameter['nmos_coarse']['_XYCoordinates']=tmp_coarse
        self._DesignParameter['nmos_fine']['_XYCoordinates']=tmp_fine
        self._DesignParameter['nmos_mirror']['_XYCoordinates']=tmp_mirror

        del tmp_coarse
        del tmp_fine
        del tmp_mirror

        self._DesignParameter['m3_connect_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=None)
        self._DesignParameter['m3_connect_y']['_Width']=2*drc._MetalxMinWidth

        gate_x=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates'][0][0]
        gate_y=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates'][0][1]-yoffset_coarse

        total_num=coarse_num+fine_num+mirror_num
        tmp_x=Xnum-(Xnum*Ynum - total_num)

        tmp1=[]
        for i in range(0,tmp_x):
            tmp1.append([[tmp_array[i][0]+gate_x, tmp_array[0][1]+gate_y], [tmp_array[i][0]+gate_x, tmp_array[-1][1]+gate_y]])

        tmp2=[]
        for i in range(tmp_x,Xnum):
            tmp2.append([[tmp_array[i][0]+gate_x, tmp_array[0][1]+gate_y], [tmp_array[i][0]+gate_x, tmp_array[total_num-Xnum][1]+gate_y]])

        self._DesignParameter['m3_connect_y']['_XYCoordinates']=tmp1+tmp2
        del tmp1
        del tmp2

        self._DesignParameter['Via_m3_m4']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='ViaMet32Met4In{}'.format(_Name)))[0]
        self._DesignParameter['Via_m3_m4']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2))
        tmp=[]

        for i in range(Xnum, total_num):
            tmp.append([tmp_array[i][0]+gate_x, tmp_array[i][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]])

        self._DesignParameter['Via_m3_m4']['_XYCoordinates']=tmp
        del tmp

        tmp=[]

        self._DesignParameter['m4_connect_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=None)
        self._DesignParameter['m4_connect_x']['_Width']=2*drc._MetalxMinWidth

        for j in range(0, Ynum-2):
            tmp.append([[tmp_array[0][0]+gate_x, tmp_array[Xnum*j][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]], [tmp_array[Xnum-1][0]+gate_x, tmp_array[Xnum*j][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]])

        tmp.append([[tmp_array[0][0]+gate_x, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][1]], [tmp_array[total_num-1][0]+gate_x, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][1]]])

        self._DesignParameter['m4_connect_x']['_XYCoordinates']=tmp
        del tmp

        if coarse_num+fine_num+mirror_num > Xnum*Ynum :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos1_length'] == nmos_stack_fine_param['nmos1_length'] == nmos_stack_mirror_param['nmos1_length']) == False :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos2_length'] == nmos_stack_fine_param['nmos2_length'] == nmos_stack_mirror_param['nmos2_length']) == False :
            raise NotImplementedError

        if (Xnum*Ynum) - total_num >= Xnum :
            raise NotImplementedError


    def _CalculateDesignParameter_v2(self,
                                  nmos_stack_coarse_param={'nmos1_width':2000,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_stack_fine_param={'nmos1_width':500,'nmos1_length':500,'nmos1_gate':1,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_gate':1,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None, 'diode_connect':True},
                                  nmos_stack_mirror_param={'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False,'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30,'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False,'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2,'guardring_width': None, 'guardring_height': None, 'diode_connect': False},\
                                  nmos_single_sw_param={'nmos_gate':2,'nmos_width':1000,'nmos_length':30,'nmos_dummy':True,'xvt':'SLVT','pccrit':True,'guardring_right':2,'guardring_left':2,'guardring_bot':2,'guardring_top':2,'guardring_width':None,'guardring_height':None},\
                                  nmos_single_tail_param={'nmos1_gate':1,'nmos1_width':2000,'nmos1_length':500,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'guardring_left':2,'guardring_right':2,'guardring_top':2,'guardring_bot':2,'guardring_width':None,'guardring_height':None},\
                                  ##nmos_single_cap_param={''},\
                                  guardring_width=None, guardring_height=None, mirror_num2=4, coarse_num=3, fine_num=4, mirror_num=1, Xnum=3, Ynum=4):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing=drc._MinSnapSpacing

        _OriginXY=[[0,0]]

        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_mirror_param))

        self._DesignParameter['nmos_sw'] = self._SrefElementDeclaration(_DesignObj=nmos_single_current_mirror.EasyDebugModule(_Name='nmos_swIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_sw']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_single_sw_param))

        nmos_single_tail_param['nmos2_gate']=nmos_stack_coarse_param['nmos2_gate']
        nmos_single_tail_param['nmos2_width']=nmos_stack_coarse_param['nmos2_width']
        nmos_single_tail_param['nmos2_length']=nmos_stack_coarse_param['nmos2_length']
        nmos_single_tail_param['nmos2_dummy']=nmos_stack_coarse_param['nmos2_dummy']
        nmos_single_tail_param['nmos2_pccrit']=nmos_stack_coarse_param['nmos2_pccrit']
        nmos_single_tail_param['nmos2_xvt']=nmos_stack_coarse_param['nmos2_xvt']

        self._DesignParameter['nmos_mirror_2'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_mirror2In{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror_2']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_single_tail_param))

        if guardring_width==None :
            max_guardring_width=self.CeilMinSnapSpacing(max(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0],\
                                    self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]-self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]), 2*MinSnapSpacing)

        elif guardring_width!=None :
            max_guardring_width=guardring_width

        if guardring_height==None :
            max_guardring_height=self.CeilMinSnapSpacing(max(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1],\
                                    self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]), 2*MinSnapSpacing)

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

        nmos_single_sw_param['guardring_width']=max_guardring_width

        nmos_single_tail_param['guardring_width']=max_guardring_width
        nmos_single_tail_param['guardring_height']=max_guardring_height


        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_mirror_param))

        self._DesignParameter['nmos_sw'] = self._SrefElementDeclaration(_DesignObj=nmos_single_current_mirror.EasyDebugModule(_Name='nmos_swIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_sw']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_single_sw_param))

        self._DesignParameter['nmos_mirror_2'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror.EasyDebugModule(_Name='nmos_mirror2In{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror_2']['_DesignObj']._CalculateDesignParameter_single(**dict(**nmos_single_tail_param))

        yoffset_coarse=(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1])
        yoffset_fine=(self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1])
        yoffset_mirror=(self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1])
        yoffset_mirror2=(self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1])

        xoffset_coarse=(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0])
        xoffset_fine=(self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0])
        xoffset_mirror=(self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0])
        xoffset_mirror2=(self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0])


        tmp_array=[]
        tmp_coarse=[]
        tmp_fine=[]
        tmp_mirror=[]
        tmp_mirror2=[]

        for j in range(0, Ynum):
            for i in range(0, Xnum):
                tmp_array.append([self.CeilMinSnapSpacing(_OriginXY[0][0]-(Xnum-1)/2*max_guardring_width+i*max_guardring_width, 2*MinSnapSpacing),self.CeilMinSnapSpacing(_OriginXY[0][1]+(Ynum-1)/2*max_guardring_height-j*max_guardring_height, 2*MinSnapSpacing)])

        for i in range(0, mirror_num2) :
            tmp_mirror2.append([tmp_array[i][0]-xoffset_mirror2, tmp_array[i][1]-yoffset_mirror2])

        for j in range(0, coarse_num) :
            tmp_coarse.append([tmp_array[mirror_num2+j][0]-xoffset_coarse, tmp_array[mirror_num2+j][1]-yoffset_coarse])

        for k in range(0, fine_num) :
            tmp_fine.append([tmp_array[mirror_num2+coarse_num+k][0]-xoffset_fine, tmp_array[mirror_num2+coarse_num+k][1]-yoffset_fine])

        for l in range(0, mirror_num) :
            tmp_mirror.append([tmp_array[mirror_num2+coarse_num+fine_num+l][0]-xoffset_mirror, tmp_array[mirror_num2+coarse_num+fine_num+l][1]-yoffset_mirror])

        self._DesignParameter['nmos_mirror_2']['_XYCoordinates']=tmp_mirror2
        self._DesignParameter['nmos_coarse']['_XYCoordinates']=tmp_coarse
        self._DesignParameter['nmos_fine']['_XYCoordinates']=tmp_fine
        self._DesignParameter['nmos_mirror']['_XYCoordinates']=tmp_mirror

        del tmp_coarse
        del tmp_fine
        del tmp_mirror
        del tmp_mirror2

        guardring_height_sw=self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]
        xoffset_sw=(self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0])
        yoffset_sw=(self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1])

        sw_coord_y=self.CeilMinSnapSpacing(self._DesignParameter['nmos_mirror_2']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]+guardring_height_sw/2, 2*MinSnapSpacing)

        tmp_sw=[[self.CeilMinSnapSpacing(_OriginXY[0][0]-1/2*max_guardring_width, 2*MinSnapSpacing)-xoffset_sw, sw_coord_y-yoffset_sw],[self.CeilMinSnapSpacing(_OriginXY[0][0]+1/2*max_guardring_width-xoffset_sw, 2*MinSnapSpacing), sw_coord_y-yoffset_sw]]

        self._DesignParameter['nmos_sw']['_XYCoordinates']=tmp_sw

        del tmp_sw

        self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]



        # self._DesignParameter['m3_connect_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=None)
        # self._DesignParameter['m3_connect_y']['_Width']=2*drc._MetalxMinWidth
        #
        # gate_x=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates'][0][0]
        # gate_y=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates'][0][1]-yoffset_coarse
        #
        # total_num=mirror_num2+coarse_num+fine_num+mirror_num
        # tmp_x=Xnum-(Xnum*Ynum - total_num)

        # tmp1=[]
        # for i in range(0,tmp_x):
        #     tmp1.append([[tmp_array[i][0]+gate_x, tmp_array[0][1]+gate_y], [tmp_array[i][0]+gate_x, tmp_array[-1][1]+gate_y]])
        #
        # tmp2=[]
        # for i in range(tmp_x,Xnum):
        #     tmp2.append([[tmp_array[i][0]+gate_x, tmp_array[0][1]+gate_y], [tmp_array[i][0]+gate_x, tmp_array[total_num-Xnum][1]+gate_y]])
        #
        # self._DesignParameter['m3_connect_y']['_XYCoordinates']=tmp1+tmp2
        # del tmp1
        # del tmp2
        #
        # self._DesignParameter['Via_m3_m4']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='ViaMet32Met4In{}'.format(_Name)))[0]
        # self._DesignParameter['Via_m3_m4']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2))
        # tmp=[]
        #
        # for i in range(Xnum, total_num):
        #     tmp.append([tmp_array[i][0]+gate_x, tmp_array[i][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]])
        #
        # self._DesignParameter['Via_m3_m4']['_XYCoordinates']=tmp
        # del tmp
        #
        # tmp=[]
        #
        # self._DesignParameter['m4_connect_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=None)
        # self._DesignParameter['m4_connect_x']['_Width']=2*drc._MetalxMinWidth
        #
        # for j in range(0, Ynum-2):
        #     tmp.append([[tmp_array[0][0]+gate_x, tmp_array[Xnum*j][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]], [tmp_array[Xnum-1][0]+gate_x, tmp_array[Xnum*j][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]])
        #
        # tmp.append([[tmp_array[0][0]+gate_x, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][1]], [tmp_array[total_num-1][0]+gate_x, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][1]]])
        #
        # self._DesignParameter['m4_connect_x']['_XYCoordinates']=tmp
        # del tmp

        if mirror_num2+coarse_num+fine_num+mirror_num > Xnum*Ynum :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos1_length'] == nmos_stack_fine_param['nmos1_length'] == nmos_stack_mirror_param['nmos1_length'] == nmos_single_tail_param['nmos1_length']) == False :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos2_length'] == nmos_stack_fine_param['nmos2_length'] == nmos_stack_mirror_param['nmos2_length']) == False :
            raise NotImplementedError

        # if Xnum*Ynum % total_num >= Xnum :
        #     raise NotImplementedError


