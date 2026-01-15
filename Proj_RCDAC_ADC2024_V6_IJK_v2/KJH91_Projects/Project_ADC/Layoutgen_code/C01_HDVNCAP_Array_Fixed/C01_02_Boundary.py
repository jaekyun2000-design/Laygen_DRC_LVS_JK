
## Import Basic Modules
    ## Engine
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time
import re

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2


    ## Building blocks
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.C01_HDVNCAP_Array_Fixed import C01_01_FingerArray



## Define Class
class _Boundary(StickDiagram_KJH1._StickDiagram_KJH):

    ## Input Parameters for Design Calculation: Used when import Sref
    _ParametersForDesignCalculation = dict(

    _Length = None,
    _LayoutOption = None,
    _NumFigPair = None,

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

    _Length = None,
    _LayoutOption = None,
    _NumFigPair = None,

    ):

        ## Class_HEADER: Pre Defined Parameter Before Calculation
            ## Load DRC library
        _DRCobj = DRC.DRC()
            ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        start_time = time.time()
        # end_time = time.time()
        # self.elapsed_time = end_time - start_time
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')





            ## SREF Generation: SRF_FingerArray
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(C01_01_FingerArray._FingerArray._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Length']          = _Length
        _Caculation_Parameters['_LayoutOption']     = _LayoutOption
        _Caculation_Parameters['_NumFigPair']       = _NumFigPair

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_FingerArray'] = self._SrefElementDeclaration(_DesignObj=C01_01_FingerArray._FingerArray(_DesignParameter=None, _Name='{}:SRF_FingerArray'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_FingerArray']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_FingerArray']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_FingerArray']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_FingerArray']['_XYCoordinates'] = [[0, 0]]






           ## Boundary_element Generation: PortA_Hrz
        for i in _LayoutOption:
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_PortA_Hrz_METAL{}'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                    ## Define Boundary_element _YWidth
            self._DesignParameter['BND_PortA_Hrz_METAL{}'.format(i)]['_YWidth'] = 100

                    ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('SRF_FingerArray','SRF_FingerPair','BND_PortA_METAL{}'.format(_LayoutOption[0]))
            tmp2 = self.get_param_KJH4('SRF_FingerArray','SRF_FingerPair','BND_PortB_METAL{}'.format(_LayoutOption[0]))
            FingerArrayWidth = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][-1][0][0]['_XY_right'][0])

            self._DesignParameter['BND_PortA_Hrz_METAL{}'.format(i)]['_XWidth'] = FingerArrayWidth + _DRCobj._FingertoBoundary +  _DRCobj._FingerWidth

                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PortA_Hrz_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_PortA_Hrz_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_FingerArray','SRF_FingerPair','BND_PortA_METAL{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][0][0][0]['_XY_up_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                                ## Define coordinates
            self._DesignParameter['BND_PortA_Hrz_METAL{}'.format(i)]['_XYCoordinates'] = tmpXY






           ## Boundary_element Generation: PortA_Vtc
        for i in _LayoutOption:
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_PortA_Vtc_METAL{}'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                    ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(i))
            tmp2 = self.get_param_KJH4('SRF_FingerArray', 'SRF_FingerPair','BND_PortA_METAL{}'.format(i))
            tmp_length = abs(tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1])
            self._DesignParameter['BND_PortA_Vtc_METAL{}'.format(i)]['_YWidth'] = tmp_length

                    ## Define Boundary_element _XWidth
            self._DesignParameter['BND_PortA_Vtc_METAL{}'.format(i)]['_XWidth'] = _DRCobj._FingerWidth

                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PortA_Vtc_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_PortA_Vtc_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(i))
            target_coord = tmp1[0][0]['_XY_up_right']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PortA_Vtc_METAL{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_up_right']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PortA_Vtc_METAL{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                                ## Define coordinates
            self._DesignParameter['BND_PortA_Vtc_METAL{}'.format(i)]['_XYCoordinates'] = tmpXY






           ## Boundary_element Generation: PortB_Hrz
        for i in _LayoutOption:
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_PortB_Hrz_METAL{}'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                    ## Define Boundary_element _YWidth
            self._DesignParameter['BND_PortB_Hrz_METAL{}'.format(i)]['_YWidth'] = 100

                    ## Define Boundary_element _XWidth
            self._DesignParameter['BND_PortB_Hrz_METAL{}'.format(i)]['_XWidth'] = self._DesignParameter['BND_PortA_Hrz_METAL{}'.format(i)]['_XWidth']

                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PortB_Hrz_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_PortB_Hrz_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('SRF_FingerArray','SRF_FingerPair','BND_PortB_METAL{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][-1][0][0]['_XY_down_right']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_up_right']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                                ## Define coordinates
            self._DesignParameter['BND_PortB_Hrz_METAL{}'.format(i)]['_XYCoordinates'] = tmpXY






           ## Boundary_element Generation: PortB_Vtc
        for i in _LayoutOption:
                    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_PortB_Vtc_METAL{}'.format(i)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(i)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(i)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                    ## Define Boundary_element _YWidth
            self._DesignParameter['BND_PortB_Vtc_METAL{}'.format(i)]['_YWidth'] = self._DesignParameter['BND_PortA_Vtc_METAL{}'.format(i)]['_YWidth']

                    ## Define Boundary_element _XWidth
            self._DesignParameter['BND_PortB_Vtc_METAL{}'.format(i)]['_XWidth'] = _DRCobj._FingerWidth

                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_PortB_Vtc_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]

                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['BND_PortB_Vtc_METAL{}'.format(i)]['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(i))
            target_coord = tmp1[0][0]['_XY_down_left']
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_PortB_Vtc_METAL{}'.format(i))
            approaching_coord = tmp2[0][0]['_XY_down_left']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('BND_PortB_Vtc_METAL{}'.format(i))
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                                ## Define coordinates
            self._DesignParameter['BND_PortB_Vtc_METAL{}'.format(i)]['_XYCoordinates'] = tmpXY







            ## Sref generation: BND_PortA_Hrz via
        for i in range(0,len(_LayoutOption)-1):
                ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = _LayoutOption[i]
            _Caculation_Parameters['_Layer2'] = _LayoutOption[i]+1
            _Caculation_Parameters['_COX'] = None
            _Caculation_Parameters['_COY'] = None

                ## Sref ViaX declaration
            self._DesignParameter['SRF_Via{}_PortA_Hrz'.format(i+1)] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Via{}_PortA_Hrz'.format(_Name,i)))[0]

                ## Define Sref Relection
            self._DesignParameter['SRF_Via{}_PortA_Hrz'.format(i+1)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
            self._DesignParameter['SRF_Via{}_PortA_Hrz'.format(i+1)]['_Angle'] = 0

                ## Calcuate Overlapped XYcoord
            tmp1 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(_LayoutOption[i]))
            tmp2 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(_LayoutOption[i+1]))
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

                ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

                ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin
            self._DesignParameter['SRF_Via{}_PortA_Hrz'.format(i+1)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
            tmpXY = []
                    ## initialized Sref coordinate
            self._DesignParameter['SRF_Via{}_PortA_Hrz'.format(i+1)]['_XYCoordinates'] = [[0, 0]]
                    ## Calculate
                        ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][0]['_XY_cent']
                        ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Via{}_PortA_Hrz'.format(i+1),'SRF_ViaM{}M{}'.format(_LayoutOption[i],_LayoutOption[i]+1),'BND_Met{}Layer'.format(_LayoutOption[i]) )
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                        ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Via{}_PortA_Hrz'.format(i+1))
            Scoord = tmp3[0][0]['_XY_origin']
                        ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                    ## Define
            self._DesignParameter['SRF_Via{}_PortA_Hrz'.format(i+1)]['_XYCoordinates'] = tmpXY










            ## Sref generation: BND_PortB_Hrz via
        for i in range(0,len(_LayoutOption)-1):
                ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = _LayoutOption[i]
            _Caculation_Parameters['_Layer2'] = _LayoutOption[i]+1
            _Caculation_Parameters['_COX'] = None
            _Caculation_Parameters['_COY'] = None

                ## Sref ViaX declaration
            self._DesignParameter['SRF_Via{}_PortB_Hrz'.format(i+1)] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Via{}_PortB_Hrz'.format(_Name,i)))[0]

                ## Define Sref Relection
            self._DesignParameter['SRF_Via{}_PortB_Hrz'.format(i+1)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
            self._DesignParameter['SRF_Via{}_PortB_Hrz'.format(i+1)]['_Angle'] = 0

                ## Calcuate Overlapped XYcoord
            tmp1 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[i]))
            tmp2 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[i+1]))
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

                ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

                ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin
            self._DesignParameter['SRF_Via{}_PortB_Hrz'.format(i+1)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
            tmpXY = []
                    ## initialized Sref coordinate
            self._DesignParameter['SRF_Via{}_PortB_Hrz'.format(i+1)]['_XYCoordinates'] = [[0, 0]]
                    ## Calculate
                        ## Target_coord
            tmp1 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][0]['_XY_cent']
                        ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Via{}_PortB_Hrz'.format(i+1),'SRF_ViaM{}M{}'.format(_LayoutOption[i],_LayoutOption[i]+1),'BND_Met{}Layer'.format(_LayoutOption[i]))
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                        ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Via{}_PortB_Hrz'.format(i+1))
            Scoord = tmp3[0][0]['_XY_origin']
                        ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                    ## Define
            self._DesignParameter['SRF_Via{}_PortB_Hrz'.format(i+1)]['_XYCoordinates'] = tmpXY






            ## Boundary_element Generation: PortB_Vtc
        for i in range(0,len(_LayoutOption)):
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_M{}_HDVNCAP'.format(_LayoutOption[i])] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['M{}_HDVNCAP'.format(_LayoutOption[i])][0],
            _Datatype=DesignParameters._LayerMapping['M{}_HDVNCAP'.format(_LayoutOption[i])][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )

                ## Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(_LayoutOption[0]))
            tmp2 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[0]))
            tmp_ywidth = abs( tmp1[0][0]['_XY_down'][1] - tmp2[0][0]['_XY_up'][1] )
            self._DesignParameter['BND_M{}_HDVNCAP'.format(_LayoutOption[i])]['_YWidth'] = tmp_ywidth

                ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('BND_PortB_Vtc_METAL{}'.format(_LayoutOption[0]))
            tmp2 = self.get_param_KJH4('BND_PortA_Vtc_METAL{}'.format(_LayoutOption[0]))
            tmp_xwidth = abs( tmp1[0][0]['_XY_right'][0] - tmp2[0][0]['_XY_left'][0] )
            self._DesignParameter['BND_M{}_HDVNCAP'.format(_LayoutOption[i])]['_XWidth'] = tmp_xwidth

                ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_M{}_HDVNCAP'.format(_LayoutOption[i])]['_XYCoordinates'] = [[0, 0]]

                ## Calculate Sref XYcoord
            tmpXY = []
                    ## initialized Sref coordinate
            self._DesignParameter['BND_M{}_HDVNCAP'.format(_LayoutOption[i])]['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                                #Ycoord
            tmp1_1 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[0]))
            target_coordy = tmp1_1[0][0]['_XY_up'][1]
                                #Xcoord
            tmp1_2 = self.get_param_KJH4('BND_PortB_Vtc_METAL{}'.format(_LayoutOption[0]))
            target_coordx = tmp1_2[0][0]['_XY_right'][0]

            target_coord = [target_coordx,target_coordy]
                            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_M{}_HDVNCAP'.format(_LayoutOption[i]))
            approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_M{}_HDVNCAP'.format(_LayoutOption[i]))
            Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                            ## Define coordinates
            self._DesignParameter['BND_M{}_HDVNCAP'.format(_LayoutOption[i])]['_XYCoordinates'] = tmpXY







        ## Boundary_element Generation: HDVNCAP drawing
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_HDVNCAP_drawing'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['HDVNCAP_drawing'][0],
        _Datatype=DesignParameters._LayerMapping['HDVNCAP_drawing'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

            ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(_LayoutOption[0]))
        tmp2 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[0]))
        tmp_ywidth = abs( tmp1[0][0]['_XY_up'][1] - tmp2[0][0]['_XY_down'][1] )
        self._DesignParameter['BND_HDVNCAP_drawing']['_YWidth'] = tmp_ywidth

            ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_PortA_Vtc_METAL{}'.format(_LayoutOption[0]))
        tmp2 = self.get_param_KJH4('BND_PortB_Vtc_METAL{}'.format(_LayoutOption[0]))
        tmp_xwidth = abs( tmp1[0][0]['_XY_right'][0] - tmp2[0][0]['_XY_left'][0] )
        self._DesignParameter['BND_HDVNCAP_drawing']['_XWidth'] = tmp_xwidth

            ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_HDVNCAP_drawing']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['BND_HDVNCAP_drawing']['_XYCoordinates'] = [[0, 0]]
                    ## Calculate
                        ## Target_coord: _XY_type1
                            #Ycoord
        tmp1_1 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[0]))
        target_coordy = tmp1_1[0][0]['_XY_down'][1]
                            #Xcoord
        tmp1_2 = self.get_param_KJH4('BND_PortB_Vtc_METAL{}'.format(_LayoutOption[0]))
        target_coordx = tmp1_2[0][0]['_XY_left'][0]

        target_coord = [target_coordx,target_coordy]
                        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_HDVNCAP_drawing')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_HDVNCAP_drawing')
        Scoord = tmp3[0][0]['_XY_origin']
                        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                        ## Define coordinates
        self._DesignParameter['BND_HDVNCAP_drawing']['_XYCoordinates'] = tmpXY


        ## Boundary_element Generation: HDVNCAP parm
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_HDVNCAP_parm'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['HDVNCAP_parm'][0],
        _Datatype=DesignParameters._LayerMapping['HDVNCAP_parm'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

            ## Define Boundary_element _YWidth
        self._DesignParameter['BND_HDVNCAP_parm']['_YWidth'] = 10

            ## Define Boundary_element _XWidth
        self._DesignParameter['BND_HDVNCAP_parm']['_XWidth'] = 10

            ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_HDVNCAP_parm']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for i in range(0, _LayoutOption[0]) :
                ## Calculate Sref XYcoord
                    ## initialized Sref coordinate
                        ## Calculate
                            ## Target_coord: _XY_type1
            if i == 0:
                                    #Ycoord
                tmp1_1 = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[0]))
                target_coordy = tmp1_1[0][0]['_XY_up'][1]
                                    #Xcoord
                tmp1_2 = self.get_param_KJH4('BND_PortB_Vtc_METAL{}'.format(_LayoutOption[0]))
                target_coordx = tmp1_2[0][0]['_XY_right'][0]

                target_coord = [target_coordx,target_coordy]
            else:
                tmp1 = self.get_param_KJH4('BND_HDVNCAP_parm')
                target_coord = tmp1[-1][0]['_XY_down_right']

                            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_HDVNCAP_parm')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_HDVNCAP_parm')
            Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] + 10
            tmpXY.append(New_Scoord)
                            ## Define coordinates
            self._DesignParameter['BND_HDVNCAP_parm']['_XYCoordinates'] = tmpXY




        
        ## Boundary_element Generation: HDVNCAP count
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_HDVNCAP_count'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['HDVNCAP_count'][0],
        _Datatype=DesignParameters._LayerMapping['HDVNCAP_count'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

            ## Define Boundary_element _YWidth
        self._DesignParameter['BND_HDVNCAP_count']['_YWidth'] = 10

            ## Define Boundary_element _XWidth
        self._DesignParameter['BND_HDVNCAP_count']['_XWidth'] = 10

            ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_HDVNCAP_count']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        for i in range(0, len( _LayoutOption)) :
                ## Calculate Sref XYcoord
                    ## initialized Sref coordinate
                        ## Calculate
                            ## Target_coord: _XY_type1
            if i == 0:
                                    #Ycoord
                tmp1_1 = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(_LayoutOption[0]))
                target_coordy = tmp1_1[0][0]['_XY_down'][1]
                                    #Xcoord
                tmp1_2 = self.get_param_KJH4('BND_PortA_Vtc_METAL{}'.format(_LayoutOption[0]))
                target_coordx = tmp1_2[0][0]['_XY_left'][0]

                target_coord = [target_coordx,target_coordy]
            else:
                tmp1 = self.get_param_KJH4('BND_HDVNCAP_count')
                target_coord = tmp1[-1][0]['_XY_up_left']

                            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_HDVNCAP_count')
            approaching_coord = tmp2[0][0]['_XY_up_right']
                            ## Sref coord
            tmp3 = self.get_param_KJH4('BND_HDVNCAP_count')
            Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[0] = New_Scoord[0] - 10
            tmpXY.append(New_Scoord)
                            ## Define coordinates
            self._DesignParameter['BND_HDVNCAP_count']['_XYCoordinates'] = tmpXY



        ''' # Array 내용 이동
        ## Labeling:    PortA     ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
        self._DesignParameter['TXT_PortA_Met{}Layer'.format(_LayoutOption[-1])] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}PIN'.format(_LayoutOption[-1])][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}PIN'.format(_LayoutOption[-1])][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

            # Portname
        self._DesignParameter['TXT_PortA_Met{}Layer'.format(_LayoutOption[-1])]['_TEXT'] = 'PortA'

            ## Define Coordinates
        tmp = self.get_param_KJH4('BND_PortA_Hrz_METAL{}'.format(_LayoutOption[-1]))
        tmpXY = tmp[0][0]['_XY_cent']
        self._DesignParameter['TXT_PortA_Met{}Layer'.format(_LayoutOption[-1])]['_XYCoordinates'] = [tmpXY]



        ## Labeling:    PortB     ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
        self._DesignParameter['TXT_PortB_Met{}Layer'.format(_LayoutOption[-1])] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}PIN'.format(_LayoutOption[-1])][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}PIN'.format(_LayoutOption[-1])][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

            # Portname
        self._DesignParameter['TXT_PortB_Met{}Layer'.format(_LayoutOption[-1])]['_TEXT'] = 'PortB'

            ## Define Coordinates
        tmp = self.get_param_KJH4('BND_PortB_Hrz_METAL{}'.format(_LayoutOption[-1]))
        tmpXY = tmp[0][0]['_XY_cent']
        self._DesignParameter['TXT_PortB_Met{}Layer'.format(_LayoutOption[-1])]['_XYCoordinates'] = [tmpXY]
        '''



        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        # start_time = time.time()
        end_time = time.time()
        self.elapsed_time = end_time - start_time

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    ## LibraryName: ex)Proj_ADC_A_my_building_block
    libname = 'Proj_ZZ01_C01_02_Boundary'
    ## CellName: ex)C01_cap_array_v2_84
    cellname = 'C01_02_Boundary_v0_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

    _Length = 5000,
    _LayoutOption = [3,4,5,6,7], # Writedown
    _NumFigPair = 11,

    )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck = 1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    ## Gen Object:
    LayoutObj = _Boundary(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
    username=My.ID,
    password=My.PW,
    WorkDir=My.Dir_Work,
    DRCrunDir=My.Dir_DRCrun,
    libname=libname,
    cellname=cellname,
    GDSDir=My.Dir_GDS
    )
    Checker.lib_deletion()
    # Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()



    print('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))
# end of 'main():' ---------------------------------------------------------------------------------------------
