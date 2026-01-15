## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_00_ECAP
from KJH91_Projects.Project_ADC.Layoutgen_code.H00_CDAC_v2 import H00_01_UCAP_KJH_test

## Define Class
class _CapWithShield(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(
        # # Unit CDAC
        _LayoutOption=None,
        _ShieldingLayer=None,   # Poly:0, M1:1, M2:2 ...
        _MetalWidth=None,
        _MetalLength=None,
        _MetalSpacing=None,

        # #Unit Cap
        _NumOfElement=None,

        # # Shielding & Top Connect node
        _ConnectLength=None,
        _ExtendLength=None,
    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
            _Name=self._NameDeclaration(_Name=_Name),
            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,
                                  # # Unit CDAC
                                  _LayoutOption=None,
                                  _ShieldingLayer=None,# Poly:0, M1:1, M2:2 ...
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  _MetalSpacing=None,

                                  # # Unit Cap
                                  _NumOfElement=None,

                                  # # Shielding & Top Connect node
                                  _ConnectLength=None,
                                  _ExtendLength=None,
                                  ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Sref Gen: Unit Capacitor(1C)
        ## Generation of Top Shielding Metal
            ## SREF Generation
            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(H00_01_UCAP_KJH_test._UCAP._ParametersForDesignCalculation)
        _Caculation_Parameters['_LayoutOption'] = _LayoutOption
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalSpacing'] = _MetalSpacing
        _Caculation_Parameters['_NumOfElement'] = _NumOfElement

        # _Caculation_Parameters['_MetalNumber'] = _MetalNumber
            ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_UCAP'] = self._SrefElementDeclaration(_DesignObj=H00_01_UCAP_KJH_test._UCAP(_DesignParameter=None, _Name='{}:SRF_UCAP'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_UCAP']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_UCAP']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_UCAP']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_UCAP']['_XYCoordinates'] = [[0, 0]]

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: GND Shielding Metal

        if _ShieldingLayer >= _LayoutOption[0]:
            raise Exception(f"The shielding layer and the CDAC metal layer overlap.")
        elif _ShieldingLayer < 1:
            raise Exception(f"The shielding layer requires at least metal 1 or higher.")

        self._DesignParameter['BND_Shield_VTC_M{}'.format(_ShieldingLayer)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_ShieldingLayer)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_ShieldingLayer)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Shield_VTC_M{}'.format(_ShieldingLayer)]['_YWidth'] = _MetalLength
        ## Define Boundary_element _XWidth
            # Calculate
        self._DesignParameter['BND_Shield_VTC_M{}'.format(_ShieldingLayer)]['_XWidth'] = _MetalWidth
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Shield_VTC_M{}'.format(_ShieldingLayer)]['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
        for i in range(2 * _NumOfElement + 1):
            tmp = [i * (_MetalSpacing + _MetalWidth), 0]
            tmpXY.append(tmp)
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Shield_VTC_M{}'.format(_ShieldingLayer)]['_XYCoordinates'] = tmpXY

            ## Connector Gen
        self._DesignParameter['BND_Shield_Connect_VTC_M{}'.format(_ShieldingLayer)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_ShieldingLayer)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_ShieldingLayer)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Shield_Connect_VTC_M{}'.format(_ShieldingLayer)]['_YWidth'] = _ConnectLength
        ## Define Boundary_element _XWidth
        # Calculate
        tmp1 = self.get_outter_KJH4('SRF_UCAP')
        shield_xwidth = tmp1['_Mostright']['coord'][0]
        self._DesignParameter['BND_Shield_Connect_VTC_M{}'.format(_ShieldingLayer)]['_XWidth'] = shield_xwidth
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Shield_Connect_VTC_M{}'.format(_ShieldingLayer)]['_XYCoordinates'] = [[0, _MetalLength]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: Top node Metal
        self._DesignParameter['BND_Shield_Hrz_M{}'.format(_ShieldingLayer)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_ShieldingLayer)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_ShieldingLayer)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        Shield_Hrz_Width = 200
        self._DesignParameter['BND_Shield_Hrz_M{}'.format(_ShieldingLayer)]['_YWidth'] = Shield_Hrz_Width
        ## Define Boundary_element _XWidth
            # Calculate
        tmp2 = self.get_outter_KJH4('SRF_UCAP')
        shield_xwidth= tmp2['_Mostright']['coord'][0]
        self._DesignParameter['BND_Shield_Hrz_M{}'.format(_ShieldingLayer)]['_XWidth'] = shield_xwidth
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Shield_Hrz_M{}'.format(_ShieldingLayer)]['_XYCoordinates'] = [[0, - Shield_Hrz_Width]]


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## BND Gen: Extended node Metal
        for i in range(_ShieldingLayer , 7 + 1) :
            self._DesignParameter['BND_Shield_Extend_VTC_M{}'.format(i)] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )
            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_Shield_Extend_VTC_M{}'.format(i)]['_YWidth'] = _ExtendLength
            ## Define Boundary_element _XWidth
            self._DesignParameter['BND_Shield_Extend_VTC_M{}'.format(i)]['_XWidth'] = shield_xwidth
            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Shield_Extend_VTC_M{}'.format(i)]['_XYCoordinates'] = [[0, 0]]
            ## Calculate Sref XYcoord
            tmpXY = []
            ## Calculate
            ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_Shield_Connect_VTC_M{}'.format(_ShieldingLayer))
            target_coord = tmp1[0][0]['_XY_up_left']
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Shield_Extend_VTC_M{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_down_left']
            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Shield_Extend_VTC_M{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_Shield_Extend_VTC_M{}'.format(i)]['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Via Gen: Extended node via
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = _ShieldingLayer
        _Caculation_Parameters['_Layer2'] = 7
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        ## Sref ViaX declaration
        self._DesignParameter['SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,7)] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                        _Name='{}:SRF_Shield_ViaM{}M{}'.format(_Name,_ShieldingLayer,7)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,7)]['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,7)]['_Angle'] = 0


        ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(_MetalWidth, _ExtendLength, 'MinEnclosureX')

        ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,7)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,7)]['_XYCoordinates'] = [[0, 0]]

        for i in range(_NumOfElement) :
            for j in range(2) :
                ## Calculate
                ## Target_coord
                tmp1 = self.get_param_KJH4('SRF_UCAP','SRF_ECAP','SRF_Top_ViaM{}M{}'.format(_LayoutOption[0],7),'SRF_ViaM{}M{}'.format(_LayoutOption[-1],7),'BND_Met{}Layer'.format(_LayoutOption[-1]))
                tmp1_1 = self.get_param_KJH4('BND_Shield_Extend_VTC_M{}'.format(_LayoutOption[-1]))
                target_coord = [tmp1[0][i][j][0][0][0]['_XY_cent'][0], tmp1_1[0][0]['_XY_cent'][1]]
                ## Approaching_coord
                tmp2 = self.get_param_KJH4('SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,7),'SRF_ViaM{}M{}'.format(_LayoutOption[-1],7),'BND_Met{}Layer'.format(_LayoutOption[-1]))
                approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                ## Sref coord
                tmp3 = self.get_param_KJH4('SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,7))
                Scoord = tmp3[0][0]['_XY_origin']
                ## Calculate
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                # New_Scoord[1] = New_Scoord[1] + _ConnectLength
                tmpXY.append(New_Scoord)
                ## Define
                self._DesignParameter['SRF_Shield_ViaM{}M{}'.format(_ShieldingLayer,7)]['_XYCoordinates'] = tmpXY





if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_H00_CDAC_v4'
    cellname = 'H02_00_CDAC_CapWithShield_v12'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _LayoutOption=[2,3,4,5,6],        # Poly:0, M1:1, M2:2 ...
        _ShieldingLayer=1,
        _MetalWidth=50,
        _MetalLength=1414,
        _MetalSpacing=50,

        # #Unit Cap
        _NumOfElement=2,

        # # Shielding & Top Connect node
        _ConnectLength=400,
        _ExtendLength=400,
     )

    '''Mode_DRCCHECK '''

    Mode_DRCCheck = False
    Num_DRCCheck =1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _CapWithShield(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YJH.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
        GDSDir=My.Dir_GDS
    )
    #Checker.lib_deletion()
    #Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    #Checker_KJH0.DRCchecker()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time,60)
    h, m = divmod(m, 60)


    print ('#############################      Finished      ################################')
    # end of 'main():' -------------------------------------------------------------------------------------