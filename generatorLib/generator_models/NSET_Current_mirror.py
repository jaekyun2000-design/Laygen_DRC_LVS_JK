from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import nmos_stack_current_mirror
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import nmos_single_current_mirror
from generatorLib.generator_models import NCAP
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaStack

class _NSET_Current_Mirror(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='NSET_Current_Mirror'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter_v1(self,
                                  nmos_stack_coarse_param={'nmos1_width':2000,'nmos1_length':500,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None},
                                  nmos_stack_fine_param={'nmos1_width':500,'nmos1_length':500,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None},
                                  nmos_stack_mirror_param={'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_dummy': False,'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False,'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2,'guardring_width': None, 'guardring_height': None},\
                                  guardring_width=None, guardring_height=None, coarse_num=3, fine_num=4, mirror_num=1, Xnum=3, Ynum=3):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing=drc._MinSnapSpacing

        _OriginXY=[[0,0]]

        nmos_stack_coarse_param['nmos1_gate']=1
        nmos_stack_coarse_param['nmos2_gate']=1
        nmos_stack_fine_param['nmos1_gate']=1
        nmos_stack_fine_param['nmos2_gate']=1
        nmos_stack_mirror_param['nmos1_gate']=1
        nmos_stack_mirror_param['nmos2_gate']=1

        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
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


        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_mirror_param))

        tmp_height1=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self.getYWidth('nmos_coarse','guardring','top','_Met1Layer')/2-(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self.getYWidth('nmos_coarse','via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2)
        tmp_height2=self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self.getYWidth('nmos_fine','guardring','top','_Met1Layer')/2-(self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self.getYWidth('nmos_fine','via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2)
        tmp_height3=self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self.getYWidth('nmos_mirror','guardring','top','_Met1Layer')/2-(self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self.getYWidth('nmos_mirror','via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2)

        diff_height1=drc._Metal1MinSpace3-tmp_height1
        diff_height2=drc._Metal1MinSpace3-tmp_height2
        diff_height3=drc._Metal1MinSpace3-tmp_height3

        self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates']=[[self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0], self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+diff_height1]]
        self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates']=[[self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0], self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+diff_height2]]
        self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates']=[[self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0], self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+diff_height3]]

        self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates']=[[[self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][1]], [self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]]]
        self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates']=[[[self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][1]], [self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]]]
        self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates']=[[[self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][1]], [self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]]]

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


        gate_x=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates'][0][0]
        gate_y=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates'][0][1]-yoffset_coarse

        total_num=coarse_num+fine_num+mirror_num
        tmp_x=Xnum-(Xnum*Ynum - total_num)

        self._DesignParameter['Via_m3_m4']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='ViaMet32Met4In{}'.format(_Name)))[0]
        self._DesignParameter['Via_m3_m4']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2))
        tmp=[]

        if Ynum > 1 :
            for i in range(0, Xnum*(Ynum-1)):
                tmp.append([tmp_array[i][0]+gate_x, tmp_array[i][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]])

        if Ynum == 1 :
            for i in range(0,total_num):
                tmp.append([tmp_array[i][0]+gate_x, tmp_array[i][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]])

        self._DesignParameter['Via_m3_m4']['_XYCoordinates']=tmp
        del tmp

        self._DesignParameter['m3_connect_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=None)
        self._DesignParameter['m3_connect_y']['_Width']=min(2*drc._MetalxMinWidth, self.getXWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer'))

        if Ynum > 1 :
            tmp1=[]
            for i in range(0,tmp_x):
                tmp1.append([[tmp_array[i][0]+gate_x-self.getXWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer')/2+self._DesignParameter['m3_connect_y']['_Width']/2, tmp_array[0][1]+gate_y], [tmp_array[i][0]+gate_x-self.getXWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer')/2+self._DesignParameter['m3_connect_y']['_Width']/2, tmp_array[-1][1]+gate_y]])

            tmp2=[]
            for i in range(tmp_x,Xnum):
                tmp2.append([[tmp_array[i][0]+gate_x-self.getXWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer')/2+self._DesignParameter['m3_connect_y']['_Width']/2, tmp_array[0][1]+gate_y], [tmp_array[i][0]+gate_x-self.getXWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer')/2+self._DesignParameter['m3_connect_y']['_Width']/2, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][1]]])

        if Ynum == 1 :
            tmp1=[]
            for i in range(0,tmp_x):
                tmp1.append([[tmp_array[i][0]+gate_x, tmp_array[0][1]+gate_y], [tmp_array[i][0]+gate_x, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][1]]])
            tmp2=[]

        self._DesignParameter['m3_connect_y']['_XYCoordinates']=tmp1+tmp2
        del tmp1
        del tmp2

        tmp=[]

        self._DesignParameter['m4_connect_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=None)
        self._DesignParameter['m4_connect_x']['_Width']=2*drc._MetalxMinWidth

        if Ynum>1:
            for j in range(0, Ynum-1):
                tmp.append([[self._DesignParameter['Via_m3_m4']['_XYCoordinates'][0][0], self._DesignParameter['Via_m3_m4']['_XYCoordinates'][Xnum*j][1]], [self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][0], self._DesignParameter['Via_m3_m4']['_XYCoordinates'][Xnum*j][1]]])

        if Ynum == 1 :
                tmp.append([[self._DesignParameter['Via_m3_m4']['_XYCoordinates'][0][0], self._DesignParameter['Via_m3_m4']['_XYCoordinates'][0][1]], [self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][0], self._DesignParameter['Via_m3_m4']['_XYCoordinates'][0][1]]])

        self._DesignParameter['m4_connect_x']['_XYCoordinates']=tmp
        del tmp

        if self.getXWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet12Met2','_Met2Layer')*self.getYWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet12Met2','_Met2Layer') < drc._MetalxMinArea:
            self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet12Met2','_Met2Layer'),2*MinSnapSpacing)
            self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_fine','via_m1_m3_nmos1_gate','ViaMet12Met2','_Met2Layer'),2*MinSnapSpacing)
            self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_mirror','via_m1_m3_nmos1_gate','ViaMet12Met2','_Met2Layer'),2*MinSnapSpacing)

            self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer'),2*MinSnapSpacing)
            self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_fine','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer'),2*MinSnapSpacing)
            self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_mirror','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer'),2*MinSnapSpacing)

        if self.getXWidth('nmos_coarse','gate_1','_Met1Layer')*self.getYWidth('nmos_coarse','gate_1','_Met1Layer') < drc._MetalxMinArea:
            self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_coarse','gate_1','_Met1Layer'),2*MinSnapSpacing)
            self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_fine','gate_1','_Met1Layer'),2*MinSnapSpacing)
            self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getYWidth('nmos_mirror','gate_1','_Met1Layer'),2*MinSnapSpacing)

        if self.getXWidth('nmos_mirror','nmos2','_Met1Layer')*self.getYWidth('nmos_mirror','nmos2','_Met1Layer')<drc._Metal1MinArea:
            self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']=self.CeilMinSnapSpacing(drc._MetalxMinArea//self.getXWidth('nmos_mirror','nmos2','_Met1Layer'),2*MinSnapSpacing)


        if coarse_num+fine_num+mirror_num > Xnum*Ynum :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos1_length'] == nmos_stack_fine_param['nmos1_length'] == nmos_stack_mirror_param['nmos1_length']) == False :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos2_length'] == nmos_stack_fine_param['nmos2_length'] == nmos_stack_mirror_param['nmos2_length']) == False :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos2_gate'] == nmos_stack_fine_param['nmos2_gate'] == nmos_stack_mirror_param['nmos2_gate'] == 1) == False :
            raise NotImplementedError

        if (Xnum*Ynum) - total_num >= Xnum :
            raise NotImplementedError


    def _CalculateDesignParameter_v2(self,
                                  nmos_stack_coarse_param={'nmos1_width':2000,'nmos1_length':500,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None},
                                  nmos_stack_fine_param={'nmos1_width':500,'nmos1_length':500,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'nmos2_width':2000,'nmos2_length':30,'nmos2_dummy':False,'nmos2_xvt':'RVT','nmos2_pccrit':False,'guardring_bot':2,'guardring_top':2,'guardring_left':2,'guardring_right':2,'guardring_width':None,'guardring_height':None},
                                  nmos_stack_mirror_param={'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_dummy': False,'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False,'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2,'guardring_width': None, 'guardring_height': None},\
                                  nmos_single_sw_param={'nmos_gate':2,'nmos_width':1000,'nmos_length':30,'nmos_dummy':True,'xvt':'SLVT','pccrit':True,'guardring_right':2,'guardring_left':2,'guardring_bot':2,'guardring_top':2,'guardring_width':None,'guardring_height':None},\
                                  nmos_single_tail_param={'nmos1_gate':1,'nmos1_width':2000,'nmos1_length':500,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'guardring_left':2,'guardring_right':2,'guardring_top':2,'guardring_bot':2,'guardring_width':None,'guardring_height':None},\
                                  nmos_cap_param={'length':2500, 'width':1000, 'Xnum':1, 'Ynum':4, 'Guardring':True, 'guardring_height':None, 'guardring_width':None, 'guardring_right':2, 'guardring_left':2, 'guardring_top':2, 'guardring_bot':2},\
                                  guardring_width=None, guardring_height=None, mirror_num2=4, coarse_num=3, fine_num=4, mirror_num=1, Xnum=3, Ynum=4):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing=drc._MinSnapSpacing

        nmos_stack_coarse_param['nmos1_gate']=1
        nmos_stack_coarse_param['nmos2_gate']=1
        nmos_stack_fine_param['nmos1_gate']=1
        nmos_stack_fine_param['nmos2_gate']=1
        nmos_stack_mirror_param['nmos1_gate']=1
        nmos_stack_mirror_param['nmos2_gate']=1
        nmos_single_tail_param['nmos1_gate']=1

        _OriginXY=[[0,0]]

        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_mirror_param))

        self._DesignParameter['nmos_sw'] = self._SrefElementDeclaration(_DesignObj=nmos_single_current_mirror._nmos_single_current_mirror(_Name='nmos_swIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_sw']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_single_sw_param))

        nmos_single_tail_param['nmos2_gate']=nmos_stack_coarse_param['nmos2_gate']
        nmos_single_tail_param['nmos2_width']=nmos_stack_coarse_param['nmos2_width']
        nmos_single_tail_param['nmos2_length']=nmos_stack_coarse_param['nmos2_length']
        nmos_single_tail_param['nmos2_dummy']=nmos_stack_coarse_param['nmos2_dummy']
        nmos_single_tail_param['nmos2_pccrit']=nmos_stack_coarse_param['nmos2_pccrit']
        nmos_single_tail_param['nmos2_xvt']=nmos_stack_coarse_param['nmos2_xvt']

        self._DesignParameter['nmos_mirror_2'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_mirror2In{}'.format(_Name)))[0]
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


        self._DesignParameter['nmos_coarse'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_coarseIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_coarse']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_coarse_param))

        self._DesignParameter['nmos_fine'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_fineIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_fine']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_fine_param))

        self._DesignParameter['nmos_mirror'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_mirrorIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_stack_mirror_param))

        self._DesignParameter['nmos_sw'] = self._SrefElementDeclaration(_DesignObj=nmos_single_current_mirror._nmos_single_current_mirror(_Name='nmos_swIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos_sw']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_single_sw_param))

        self._DesignParameter['nmos_mirror_2'] = self._SrefElementDeclaration(_DesignObj=nmos_stack_current_mirror._nmos_stack_current_mirror(_Name='nmos_mirror2In{}'.format(_Name)))[0]
        self._DesignParameter['nmos_mirror_2']['_DesignObj']._CalculateDesignParameter_single(**dict(**nmos_single_tail_param))

        tmp_height1=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self.getYWidth('nmos_coarse','guardring','top','_Met1Layer')/2-(self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self.getYWidth('nmos_coarse','via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2)
        tmp_height2=self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self.getYWidth('nmos_fine','guardring','top','_Met1Layer')/2-(self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self.getYWidth('nmos_fine','via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2)
        tmp_height3=self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self.getYWidth('nmos_mirror','guardring','top','_Met1Layer')/2-(self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self.getYWidth('nmos_mirror','via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2)
        tmp_height4=self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self.getYWidth('nmos_mirror_2','guardring','top','_Met1Layer')/2-(self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['via_temp_m1']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['via_temp_m1']['_YWidth']/2)

        diff_height1=drc._Metal1MinSpace3-tmp_height1
        diff_height2=drc._Metal1MinSpace3-tmp_height2
        diff_height3=drc._Metal1MinSpace3-tmp_height3
        diff_height4=drc._Metal1MinSpace3-tmp_height4

        self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates']=[[self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0], self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+diff_height1]]
        self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates']=[[self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0], self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+diff_height2]]
        self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates']=[[self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0], self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+diff_height3]]
        self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates']=[[self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0], self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+diff_height4]]

        self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates']=[[[self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][1]], [self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]]]
        self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates']=[[[self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][1]], [self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]]]
        self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates']=[[[self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][1]], [self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]]]
        self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates']=[[[self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][1]], [self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['m1_vss']['_XYCoordinates'][0][0][0], self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]]]


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

        self._DesignParameter['ncap']=self._SrefElementDeclaration(_DesignObj=NCAP._NCap(_Name='ncap.In{}'.format(_Name)))[0]
        nmos_cap_param['guardring_width']=tmp_array[-1][0]-tmp_array[0][0]+max_guardring_width
        self._DesignParameter['ncap']['_DesignObj']._CalculateDesignParameter(**dict(**nmos_cap_param))
        self._DesignParameter['ncap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]

        ncap_guardring_height=self._DesignParameter['ncap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]-self._DesignParameter['ncap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]

        self._DesignParameter['ncap']['_XYCoordinates']=[[(tmp_array[-1][0]+tmp_array[0][0])/2, tmp_array[-1][1]-max_guardring_height/2-ncap_guardring_height/2]]

        self._DesignParameter['via_m1_m3_mirror2']=self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='viam1m3_mirror2In{}'.format(_Name)))[0]
        self._DesignParameter['via_m1_m3_mirror2']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=max(1,int(self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/(drc._VIAxMinWidth+drc._VIAxMinSpace))), start_layer=1, end_layer=3))

        tmp=[]
        for i in range(0, len(self._DesignParameter['nmos_mirror_2']['_XYCoordinates'])):
            tmp.append([self._DesignParameter['nmos_mirror_2']['_XYCoordinates'][i][0]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['nmos1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['nmos_mirror_2']['_XYCoordinates'][i][1]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['nmos1']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_mirror_2']['_DesignObj']._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][1]])

        self._DesignParameter['via_m1_m3_mirror2']['_XYCoordinates']=tmp
        del tmp

        self._DesignParameter['m3_mirror2_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=None)
        self._DesignParameter['m3_mirror2_y']['_Width']=self._DesignParameter['via_m1_m3_mirror2']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']

        tmp=[]
        for i in range(0, len(self._DesignParameter['nmos_mirror_2']['_XYCoordinates'])):
            tmp.append([self._DesignParameter['via_m1_m3_mirror2']['_XYCoordinates'][i], [self._DesignParameter['via_m1_m3_mirror2']['_XYCoordinates'][i][0], self.getXY('nmos_sw','guardring','bot')]])

        self._DesignParameter['m3_mirror2_y']['_XYCoordinates']=tmp
        del tmp

        self._DesignParameter['m4_mirror2_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=None)
        self._DesignParameter['m4_mirror2_sw_x']['_Width']=min(drc._MetalxMinWidth*3, self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['via_m1_m4_source']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'])
        self._DesignParameter['m4_mirror2_sw_x']['_XYCoordinates']=[[[min(self._DesignParameter['m3_mirror2_y']['_XYCoordinates'][0][0][0]-self._DesignParameter['m3_mirror2_y']['_Width']/2, self._DesignParameter['nmos_sw']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['via_m1_m4_drain']['_XYCoordinates'][0][0]), self.getXY('nmos_sw','guardring','bot')], [max(self._DesignParameter['nmos_sw']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['via_m1_m4_drain']['_XYCoordinates'][-1][0], ), self.getXY('nmos_sw','guardring','bot')]]]

        self._DesignParameter['Via_m3_m4_mirror2_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Via_m3_m4_mirror2_swIn{}'.format(_Name)))[0]
        self._DesignParameter['Via_m3_m4_mirror2_sw']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))

        tmp=[]
        for i in range(0, Xnum):
            tmp.append([self._DesignParameter['m3_mirror2_y']['_XYCoordinates'][i][0][0], self._DesignParameter['m4_mirror2_sw_x']['_XYCoordinates'][0][0][1]])

        self._DesignParameter['Via_m3_m4_mirror2_sw']['_XYCoordinates']=tmp
        del tmp

        gate_x=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates'][0][0]
        gate_y=self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates'][0][1]-yoffset_coarse
        total_num=mirror_num2+coarse_num+fine_num+mirror_num
        tmp_x=Xnum-(Xnum*Ynum - total_num)

        self._DesignParameter['Via_m3_m4']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='ViaMet32Met4In{}'.format(_Name)))[0]
        self._DesignParameter['Via_m3_m4']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2))
        tmp=[]

        if Ynum > 1 :
            for i in range(0, Xnum*(Ynum-1)):
                tmp.append([tmp_array[i][0]+gate_x, tmp_array[i][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]])

        if Ynum == 1 :
            for i in range(0,total_num):
                tmp.append([tmp_array[i][0]+gate_x, tmp_array[i][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]])

        self._DesignParameter['Via_m3_m4']['_XYCoordinates']=tmp
        del tmp


        self._DesignParameter['m3_connect_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=None)
        self._DesignParameter['m3_connect_y']['_Width']=min(2*drc._MetalxMinWidth, self.getXWidth('nmos_coarse','via_m1_m3_nmos1_gate','ViaMet22Met3','_Met3Layer'))



        tmp1=[]
        for i in range(0,tmp_x):
            tmp1.append([[tmp_array[i][0]+gate_x-xoffset_coarse, tmp_array[0][1]+gate_y], [tmp_array[i][0]+gate_x-xoffset_coarse, self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_XYCoordinates'][-1][1]]])

        self._DesignParameter['m3_connect_y']['_XYCoordinates']=tmp1
        del tmp1



        tmp=[]

        self._DesignParameter['m4_connect_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=None)
        self._DesignParameter['m4_connect_x']['_Width']=2*drc._MetalxMinWidth

        if Ynum==2:
             tmp.append([[tmp_array[0][0]+gate_x, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][0][1]], [self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][0], self._DesignParameter['Via_m3_m4']['_XYCoordinates'][0][1]]])
             self._DesignParameter['m4_connect_x']['_XYCoordinates']=tmp
             del tmp

        if Ynum>2:
            for j in range(0, Ynum-2):
                tmp.append([[tmp_array[0][0]+gate_x, tmp_array[Xnum*j][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]], [tmp_array[Xnum-1][0]+gate_x, tmp_array[Xnum*j][1]+self._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]]])

            tmp.append([[tmp_array[0][0]+gate_x, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][1]], [tmp_array[total_num-1][0]+gate_x, self._DesignParameter['Via_m3_m4']['_XYCoordinates'][-1][1]]])

            self._DesignParameter['m4_connect_x']['_XYCoordinates']=tmp
            del tmp

        self._DesignParameter['via_m1_m2_ncap']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_ncapIn{}'.format(_Name)))[0]
        num_via_ncap=max(1,int(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/(drc._VIAxMinWidth+drc._VIAxMinSpace)) - 1)
        self._DesignParameter['via_m1_m2_ncap']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=num_via_ncap, _ViaMet12Met2NumberOfCOY=1))

        tmp=[]
        for i in range(0, len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_XYCoordinates'])):
            tmp.append([self._DesignParameter['ncap']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_XYCoordinates'][i][0], self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_XYCoordinates'][i][1]])

        self._DesignParameter['via_m1_m2_ncap']['_XYCoordinates']=tmp
        del tmp

        self._DesignParameter['via_m2_m3_ncap']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via_m2_m3_ncapIn{}'.format(_Name)))[0]
        num_via_ncap=max(1,int(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/(drc._VIAxMinWidth+drc._VIAxMinSpace)) - 1)
        self._DesignParameter['via_m2_m3_ncap']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=num_via_ncap, _ViaMet22Met3NumberOfCOY=2))

        tmp=[]
        for i in range(0, len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_XYCoordinates'])):
            tmp.append([self._DesignParameter['ncap']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_XYCoordinates'][i][0], self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['via_poly_m1']['_XYCoordinates'][i][1]])

        self._DesignParameter['via_m2_m3_ncap']['_XYCoordinates']=tmp
        del tmp


        self._DesignParameter['M3_ncap_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth*6)
        self._DesignParameter['M3_ncap_y']['_XYCoordinates']=[[self._DesignParameter['via_m1_m2_ncap']['_XYCoordinates'][0], self._DesignParameter['via_m1_m2_ncap']['_XYCoordinates'][-1]]]

        self._DesignParameter['M3_ncap_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=self._DesignParameter['via_m2_m3_ncap']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])
        self._DesignParameter['M3_ncap_x']['_XYCoordinates']=[[[self._DesignParameter['m3_connect_y']['_XYCoordinates'][0][0][0]-self._DesignParameter['m3_connect_y']['_Width']/2, self._DesignParameter['via_m1_m2_ncap']['_XYCoordinates'][-1][1]], [self._DesignParameter['m3_connect_y']['_XYCoordinates'][-1][0][0]+self._DesignParameter['m3_connect_y']['_Width']/2, self._DesignParameter['via_m1_m2_ncap']['_XYCoordinates'][-1][1]]]]

        self._DesignParameter['M1_ncap_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=drc._MetalxMinWidth*10)
        self._DesignParameter['M1_ncap_x']['_Width']=min(drc._MetalxMinWidth*10, self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])

        tmp=[]
        for i in range(0, len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'])):
            tmp.append([[self._DesignParameter['ncap']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][1]], \
                        [self._DesignParameter['ncap']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][1]]])

        self._DesignParameter['M1_ncap_x']['_XYCoordinates']=tmp
        del tmp

        self._DesignParameter['M1_ncap_vss']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=drc._MetalxMinWidth*10)
        self._DesignParameter['M1_ncap_vss']['_Width']=self._DesignParameter['M1_ncap_x']['_Width']

        tmp=[]
        for i in range(0, len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'])):
            tmp.append([[self._DesignParameter['ncap']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][1]], \
                        [self._DesignParameter['ncap']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0], self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][1]]])
            tmp.append([[self._DesignParameter['ncap']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][1]], \
                        [self._DesignParameter['ncap']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0], self._DesignParameter['ncap']['_XYCoordinates'][0][1]+self._DesignParameter['ncap']['_DesignObj']._DesignParameter['nmos']['_XYCoordinates'][i][1]]])

        self._DesignParameter['M1_ncap_x']['_XYCoordinates']=tmp
        del tmp

        self._DesignParameter['via_m1_m4_mirror']=self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m4_mirrorIn{}'.format(_Name)))[0]
        num_via= max(1, (1 + int(((((self._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))) - 1)
        self._DesignParameter['via_m1_m4_mirror']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=num_via, start_layer=1, end_layer=4))
        self._DesignParameter['via_m1_m4_mirror']['_XYCoordinates']=[[self.getXY('nmos_mirror','nmos2','_Met1Layer')[-1][0], self.getXY('nmos_mirror','nmos2','_Met1Layer')[-1][1]-self.getYWidth('nmos_mirror','nmos2','_Met1Layer')/2+self.getYWidth('via_m1_m4_mirror','ViaMet12Met2','_Met1Layer')/2]]


        if mirror_num2+coarse_num+fine_num+mirror_num > Xnum*Ynum :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos1_length'] == nmos_stack_fine_param['nmos1_length'] == nmos_stack_mirror_param['nmos1_length'] == nmos_single_tail_param['nmos1_length']) == False :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos2_length'] == nmos_stack_fine_param['nmos2_length'] == nmos_stack_mirror_param['nmos2_length']) == False :
            raise NotImplementedError

        if (nmos_stack_coarse_param['nmos2_gate'] == nmos_stack_fine_param['nmos2_gate'] == nmos_stack_mirror_param['nmos2_gate'] == 1) == False :
            raise NotImplementedError


        # if Xnum*Ynum % total_num >= Xnum :
        #     raise NotImplementedError


