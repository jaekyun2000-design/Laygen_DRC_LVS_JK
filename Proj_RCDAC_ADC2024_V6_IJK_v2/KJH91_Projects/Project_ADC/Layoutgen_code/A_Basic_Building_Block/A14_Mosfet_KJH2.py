from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math
#from SthPack import CoordCalc


from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3

## ########################################################################################################################################################## Class_HEADER
class _Mosfet(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        # Mosfet

        # PMOS/NMOS
        _MosType='PMOS',  # 'NMOS'/'PMOS'

        # MOS Up/Dn
        _MosUpDn='Dn',  # 'Up'/'Dn'

        # Physical dimension
        _NumberofGate	= 5,       # Number
        _ChannelWidth	            = 100,      # Number
        _ChannelLength	            = 30,       # Number
        _GateSpacing		        = None,     # None/Number
        _SDWidth			        = None,     # None/Number
        _XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
        _PCCrit				        = True,     # None/True

        # Source_node setting
        # Via setting
        _Source_Via_TF              = True,     # True/False
        # Via close to POpin
        _Source_Via_Close2POpin_TF  = True,     # True/False
        # Comb setting: If Via is True
        _Source_Comb_TF             = True,     # True/False
        # Comb POPinward
        _Source_Comb_POpinward_TF   = True,     # True/False
        # Comb vertical_length
        _Source_Comb_Length         = None,     # None/Number

        # Drain_node_setting
        # Via setting
        _Drain_Via_TF               = True,     # True/False
        # Via close to POpin
        _Drain_Via_Close2POpin_TF   = True,     # True/False
        # Comb setting: If Via is True
        _Drain_Comb_TF              = True,     # True/False
        # Comb POPinward
        _Drain_Comb_POpinward_TF    = True,     # True/False
        # Comb vertical_length
        _Drain_Comb_Length          = None,     # None/Number

        # POLY dummy setting
        _PODummy_TF                 = True,  # TF
        # if _NMOSDummy == True
        _PODummy_Length             = None,  # None/Value
        _PODummy_Placement          = None,  # None/'Up'/'Dn'/

        # XVT setting
        # XVT setting : Exten XVT area if area is min
        _Xvt_MinExten_TF            = True,     # True/False
        # XVT setting : None(Cent), Up, Dn
        _Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

        # Poly Gate setting
        # Poly Gate setting
        _POGate_Comb_TF             = True,     # True/False
        # Poly Gate setting : vertical length
        _POGate_Comb_length         = None,     # None/Number
        # Poly Gate Via setting
        _POGate_Via_TF              = True,     # None/'Up'/'Dn'/
        # Poly Gate Via setting :
        _POGate_ViaMxMx             = [0 ,1]     # Ex) [1,5] -> ViaM1M5

                                        )

    ## Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                                            _Name=self._NameDeclaration(_Name=_Name),
                                            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                            _XYcoordAsCent=dict(_XYcoordAsCent=0),
                                        )

    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameter(self,

                                  # Mosfet

                                  # PMOS/NMOS
                                  _MosType='PMOS',  # 'NMOS'/'PMOS'

                                  # MOS Up/Dn
                                  _MosUpDn='Dn',  # 'Up'/'Dn'

                                  # Physical dimension
                                  _NumberofGate	= 5,  # Number
                                  _ChannelWidth	            = 100,  # Number
                                  _ChannelLength	            = 30,  # Number
                                  _GateSpacing		        = None,  # None/Number
                                  _SDWidth			        = None,  # None/Number
                                  _XVT				        = 'SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
                                  _PCCrit				        = True,  # None/True

                                  # Source_node setting
                                  # Via setting
                                  _Source_Via_TF              = True,  # True/False
                                  # Via close to POpin
                                  _Source_Via_Close2POpin_TF  = True,  # True/False
                                  # Comb setting: If Via is True
                                  _Source_Comb_TF             = True,  # True/False
                                  # Comb POPinward
                                  _Source_Comb_POpinward_TF   = True,  # True/False
                                  # Comb vertical_length
                                  _Source_Comb_Length         = None,  # None/Number

                                  # Drain_node_setting
                                  # Via setting
                                  _Drain_Via_TF               = True,  # True/False
                                  # Via close to POpin
                                  _Drain_Via_Close2POpin_TF   = True,  # True/False
                                  # Comb setting: If Via is True
                                  _Drain_Comb_TF              = True,  # True/False
                                  # Comb POPinward
                                  _Drain_Comb_POpinward_TF    = True,  # True/False
                                  # Comb vertical_length
                                  _Drain_Comb_Length          = None,  # None/Number

                                  # POLY dummy setting
                                  _PODummy_TF                 = True,  # TF
                                  # if _NMOSDummy == True
                                  _PODummy_Length             = None,  # None/Value
                                  _PODummy_Placement          = None,  # None/'Up'/'Dn'/

                                  # XVT setting
                                  # XVT setting : Exten XVT area if area is min
                                  _Xvt_MinExten_TF            = True,  # True/False
                                  # XVT setting : None(Cent), Up, Dn
                                  _Xvt_Placement              = 'Up',  # None/'Up'/'Dn'/

                                  # Poly Gate setting
                                  # Poly Gate setting
                                  _POGate_Comb_TF             = True,  # True/False
                                  # Poly Gate setting : vertical length
                                  _POGate_Comb_length         = None,  # None/Number
                                  # Poly Gate Via setting
                                  _POGate_Via_TF              = True,  # None/'Up'/'Dn'/
                                  # Poly Gate Via setting :
                                  _POGate_ViaMxMx             = [0 ,1]  # Ex) [1,5] -> ViaM1M5

                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## POLY_Layer
        #Define Boundary_element
        self._DesignParameter['BND_POLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer']['_YWidth'] = _ChannelWidth + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_ChannelLength)

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_POLayer']['_XWidth'] = _ChannelLength

        #Define Boundary_element _XYCoordinates
            #Define _LengthNMOSBtwPO
        _LengthBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj.DRCPolyMinSpace(_Width=_ChannelWidth, _ParallelLength=_ChannelLength)) + _ChannelLength
                #Applying GateSpacing
        if _GateSpacing != None:
            if (_GateSpacing + _ChannelLength) < _LengthBtwPO:
                raise NotImplementedError(f"Invalid input arg: GateSpacing({_GateSpacing})")
            else:
                _LengthNMOSBtwPO = _GateSpacing + _ChannelLength
        elif _GateSpacing == None:
            _GateSpacing = _DRCObj._PolygateMinSpace

            #Calculate Sref XYcoord
                #initialize coordinate
        self._DesignParameter['BND_POLayer']['_XYCoordinates'] = [[0,0]]
        tmpXY=[[0,0]]
        for i in range(0,_NumberofGate-1):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH4('BND_POLayer')
            target_coord = tmp1[i][0]['_XY_down_left']
                    #Approaching_coord
            tmp2 = self.get_param_KJH4('BND_POLayer')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                    #Sref coord
            tmp3 = self.get_param_KJH4('BND_POLayer')
            Scoord = tmp3[0][0]['_XY_origin']
                    #Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
            New_Scoord[0] = New_Scoord[0] + _LengthBtwPO
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['BND_POLayer']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## POLY Dummy Layer

        #Define Boundary_element
        self._DesignParameter['BND_PODummyLayer'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
            #SS28nm DRC(a varies depending on channel width)
        a = 16
            #SS28nm If dummy or not
        if _PODummy_TF == False:
            self._DesignParameter['BND_PODummyLayer']['_YWidth'] = 0
        elif _PODummy_TF:
            self._DesignParameter['BND_PODummyLayer']['_YWidth'] = _ChannelWidth + 2 * a

        #Define Boundary_element _XWidth
        if _PODummy_TF == False:
            self._DesignParameter['BND_PODummyLayer']['_XWidth'] = 0
        elif _PODummy_TF:
            self._DesignParameter['BND_PODummyLayer']['_XWidth'] = _ChannelLength

            #Calculate Sref XYcoord
                #initialized Sref coordinate
        self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = [[0,0]]
        tmpXY=[]
        for i in [0,-1]:
            if i == 0:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH4('BND_POLayer')
                target_coord = tmp1[i][0]['_XY_cent']
                        #Approaching_coord
                tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                approaching_coord = tmp2[0][0]['_XY_cent']
                        #Sref coord
                tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                Scoord = tmp3[0][0]['_XY_origin']
                        #Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                New_Scoord[0] = New_Scoord[0] - _LengthBtwPO
                tmpXY.append(New_Scoord)
            else:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH4('BND_POLayer')
                target_coord = tmp1[i][0]['_XY_cent']
                        #Approaching_coord
                tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                approaching_coord = tmp2[0][0]['_XY_cent']
                        #Sref coord
                tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                Scoord = tmp3[0][0]['_XY_origin']
                        #Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                New_Scoord[0] = New_Scoord[0] + _LengthBtwPO
                tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## POLY Dummy Layer
        #Define Boundary_element
        self._DesignParameter['BND_ODLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayer']['_YWidth'] = _ChannelWidth

        #Define Boundary_element _XWidth
        XWidth_OD = _LengthBtwPO * _NumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['BND_ODLayer']['_XWidth'] = XWidth_OD

        #Calculate Sref XYcoord
            #initialize coordinate
        self._DesignParameter['BND_ODLayer']['_XYCoordinates'] = [[0,0]]
        tmpXY=[]

            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('BND_POLayer')
                    #Target_coordx
        target_coordx = 0.5 * ( tmp1[-1][0]['_XY_right'][0] + tmp1[0][0]['_XY_left'][0] )
                    #Target_coordy
        target_coordy = 0.5 * ( tmp1[0][0]['_XY_up'][1] + tmp1[0][0]['_XY_down'][1] )
        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ODLayer')
        approaching_coord = tmp2[0][0]['_XY_cent']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ODLayer')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ODLayer']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## METAL1 Layer
        #Define Boundary_element
        self._DesignParameter['BND_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        _tmpCOYNum = int(float(self._DesignParameter['BND_ODLayer']['_YWidth'] - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2])  + _DRCObj._CoMinSpace) / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth))
        self._DesignParameter['BND_Met1Layer']['_YWidth'] = (_tmpCOYNum - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2

        #Define Boundary_element _XWidth
            #SDWidth
        if _SDWidth == None:
            XWidth_Met1 = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        else:
            if _SDWidth < _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO:
                raise NotImplementedError(f"Invalid Value _SDWidth({_SDWidth})")
            else:
                XWidth_Met1 = _SDWidth
        self._DesignParameter['BND_Met1Layer']['_XWidth'] = XWidth_Met1


        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
                #Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        target_coord = tmp1[0][0]['_XY_cent']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Met1Layer')
        approaching_coord = tmp2[0][0]['_XY_cent']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

        _XYCoordinateOfNMOS = [New_Scoord]
            #get _LengthNMOSBtwMet1
        _LengthBtwMet1 = _LengthBtwPO
            #Cal coord
        tmpXYs = []
        for i in range(0, _NumberofGate + 1):
            XY = [_XYCoordinateOfNMOS[0][0] - _NumberofGate / 2 * _LengthBtwMet1 + i * _LengthBtwMet1,
                  _XYCoordinateOfNMOS[0][1]]
            tmpXYs.append(XY)
            #Define coord
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = tmpXYs





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## CONT_Layer
        # Define Boundary_element
        self._DesignParameter['BND_COLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['CONT'][0],
            _Datatype=DesignParameters._LayerMapping['CONT'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = [[0, 0]]

        # Calculate Sref XYcoord
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_COLayer')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_COLayer')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        # Get _XYCoordinateOfNMOS
        _XYCoordinateOfNMOS = [New_Scoord]

        # CONT XNum/YNum Calculation
        _XNumberOfCOInNMOS = _NumberofGate + 1
        _YNumberOfCOInNMOS = _tmpCOYNum
        # Check the number of CO On NMOS TR
        if _XNumberOfCOInNMOS == 0 or _YNumberOfCOInNMOS == 0:
            print(
                '************************* Error occurred in {} Design Parameter Calculation******************************'.format(
                    self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0

            # Define _LengthNMOSBtwCO
        _LengthBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth

        # Cal coord
        tmpXYs = []
        for i in range(0, _XNumberOfCOInNMOS):
            for j in range(0, _YNumberOfCOInNMOS):
                XY = [_XYCoordinateOfNMOS[0][0] - (
                            _XNumberOfCOInNMOS - 1) / 2 * _LengthBtwMet1 + i * _LengthBtwMet1,
                      _XYCoordinateOfNMOS[0][1] - (
                                  _YNumberOfCOInNMOS - 1) / 2 * _LengthBtwCO + j * _LengthBtwCO]
                tmpXYs.append(XY)

            # Define coord
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmpXYs





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## CONT_Layer
        try:
            if (DesignParameters._Technology == '028nm') and _XVT in ('SLVT', 'LVT', 'RVT', 'HVT'):
                _XVTLayer = 'BND_' + _XVT + 'Layer'
                _XVTLayerMappingName = _XVT

            elif DesignParameters._Technology in ('028nm'):
                raise NotImplementedError(f"Invalid '_XVT' argument({_XVT}) for {DesignParameters._Technology}")

            else:
                raise NotImplementedError(f"Not Yet Implemented in other technology : {DesignParameters._Technology}")

            if _XVTLayer != None:
                # Define Boundary_element
                self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[_XVTLayerMappingName][0],
                    _Datatype=DesignParameters._LayerMapping[_XVTLayerMappingName][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )

                # Define Boundary_element _YWidth and _XWidth
                if _Xvt_MinExten_TF == True:
                    area = (self._DesignParameter['BND_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY ) * (self._DesignParameter['BND_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX)

                    if area > 160000:
                        # Define Boundary_element _YWidth
                        self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY
                        # Define Boundary_element _XWidth
                        self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['BND_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX
                    else:
                        #Define Boundary_element _XWidth
                        self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['BND_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX
                        #Define Boundary_element _YWidth
                        self._DesignParameter[_XVTLayer]['_YWidth'] = np.ceil(160000 / np.array(self._DesignParameter[_XVTLayer]['_XWidth']))

                else:
                    # Define Boundary_element _YWidth
                    self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY
                    # Define Boundary_element _XWidth
                    self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['BND_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX

                # Define coord
                self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [[0, 0]]

                # Calculate Sref XYcoord
                    # Target_coord
                tmp1 = self.get_param_KJH4('BND_ODLayer')
                if _Xvt_Placement == None:
                    target_coord = tmp1[0][0]['_XY_cent']
                elif _Xvt_Placement == 'Up':
                    target_coord = tmp1[0][0]['_XY_up']
                elif _Xvt_Placement == 'Dn':
                    target_coord = tmp1[0][0]['_XY_down']
                else:
                    target_coord = tmp1[0][0]['_XY_cent']

                    # Approaching_coord
                tmp2 = self.get_param_KJH4(_XVTLayer)
                if _Xvt_Placement == None:
                    approaching_coord = tmp2[0][0]['_XY_cent']
                elif _Xvt_Placement == 'Up':
                    approaching_coord = tmp2[0][0]['_XY_up']
                elif _Xvt_Placement == 'Dn':
                    approaching_coord = tmp2[0][0]['_XY_down']
                else:
                    approaching_coord = tmp2[0][0]['_XY_cent']

                    # Sref coord
                tmp3 = self.get_param_KJH4(_XVTLayer)
                Scoord = tmp3[0][0]['_XY_origin']

                    # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

                if _Xvt_Placement == None:
                    New_Scoord[0] = New_Scoord[0]
                    New_Scoord[1] = New_Scoord[1]
                elif _Xvt_Placement == 'Up':
                    New_Scoord[0] = New_Scoord[0]
                    New_Scoord[1] = New_Scoord[1] + _DRCObj._XvtMinEnclosureOfODY
                elif _Xvt_Placement == 'Dn':
                    New_Scoord[0] = New_Scoord[0]
                    New_Scoord[1] = New_Scoord[1] - _DRCObj._XvtMinEnclosureOfODY
                else:
                    New_Scoord[0] = New_Scoord[0]
                    New_Scoord[1] = New_Scoord[1]

                # Define coord
                self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [New_Scoord]

        except Exception as e:
            import traceback
            traceback.print_exc()
            print('Error Occurred', e)
            raise NotImplementedError





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PIMP (PP/BP) Layer
        if _MosType == 'PMOS':
            #Define Boundary_element
            self._DesignParameter['BND_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

            #Define Boundary_element _YWidth
            self._DesignParameter['BND_PPLayer']['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPactiveY

            #Define Boundary_element _XWidth
            if (DesignParameters._Technology == 'TSMC65nm') and (_PODummy_TF == True):
                XWidth_PP_byPODummy = self._DesignParameter['BND_PODummyLayer']['_XWidth'] + (self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'][0][0]) + 2 * _DRCObj._PpMinEnclosureOfPo
            else:
                XWidth_PP_byPODummy = 0

            XWidth_PP_byOD = self._DesignParameter['BND_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinEnclosureOfPactiveX

            self._DesignParameter['BND_PPLayer']['_XWidth'] = max(XWidth_PP_byPODummy, XWidth_PP_byOD)

            #Define coord
            self._DesignParameter['BND_PPLayer']['_XYCoordinates'] = [[0,0]]

            # Calculate Sref XYcoord
            # Target_coord
            tmp1 = self.get_param_KJH4('BND_ODLayer')
            target_coord = tmp1[0][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_PPLayer')
            approaching_coord = tmp2[0][0]['_XY_cent']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_PPLayer')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

            # Define coord
            self._DesignParameter['BND_PPLayer']['_XYCoordinates'] = [New_Scoord]

        # If NMOS, do not generate PPLayer
        else:
            pass





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PIMP (PP/BP) Layer
        # If pccrit
        if DesignParameters._Technology == '028nm' and _PCCrit != False:

            # Make PCCrit if gatelentgh is either 30 or 34
            if self._DesignParameter['BND_POLayer']['_XWidth'] in (30, 34):

                # Define Boundary_element
                self._DesignParameter['BND_PCCRITLayer'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                    _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                    _XWidth=None,
                    _YWidth=None,
                    _XYCoordinates=[],
                )

                # Define Boundary_element _YWidth
                self._DesignParameter['BND_PCCRITLayer']['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension

                # Define Boundary_element _XWidth
                self._DesignParameter['BND_PCCRITLayer']['_XWidth'] = _LengthBtwMet1 * _NumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension

                self._DesignParameter['BND_PCCRITLayer']['_XYCoordinates'] = [[0, 0]]
                # Define coord
                # Calculate Sref XYcoord
                # Target_coord
                tmp1 = self.get_param_KJH4('BND_ODLayer')
                target_coord = tmp1[0][0]['_XY_cent']
                # Approaching_coord
                tmp2 = self.get_param_KJH4('BND_PCCRITLayer')
                approaching_coord = tmp2[0][0]['_XY_cent']
                # Sref coord
                tmp3 = self.get_param_KJH4('BND_PCCRITLayer')
                Scoord = tmp3[0][0]['_XY_origin']
                # Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

                self._DesignParameter['BND_PCCRITLayer']['_XYCoordinates'] = [New_Scoord]

                if self._DesignParameter['BND_POLayer']['_XWidth'] == 30:
                    if _GateSpacing not in (96, 222, 100, 230):
                        raise NotImplementedError
                elif self._DesignParameter['BND_POLayer']['_XWidth'] == 34:
                    if _GateSpacing not in (96, 226):
                        raise NotImplementedError

            # Do not make PCcrit if gatelenght is not either 30 or 34
            else:
                pass





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _METAL1PINDrawing
        #Define Boundary_element
        self._DesignParameter['BND_METAL1PINDrawing'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_METAL1PINDrawing']['_YWidth'] = self._DesignParameter['BND_Met1Layer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_METAL1PINDrawing']['_XWidth'] = self._DesignParameter['BND_Met1Layer']['_XWidth']

        #Define coord
        self._DesignParameter['BND_METAL1PINDrawing']['_XYCoordinates'] = self._DesignParameter['BND_Met1Layer']['_XYCoordinates']





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _ODLayerPINDrawing
        # Define Boundary_element
        self._DesignParameter['BND_ODLayerPINDrawing'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['RXPIN'][0],
            _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth']

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        tmp2 = self.get_param_KJH4('BND_POLayer')

        self._DesignParameter['BND_ODLayerPINDrawing']['_XWidth'] = abs( tmp1[0][0]['_XY_right'][0] - tmp2[-1][0]['_XY_right'][0])

        # Define coord
        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['BND_ODLayerPINDrawing']['_XYCoordinates'] = [[0, 0]]

        # Calculate1
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ODLayerPINDrawing')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_ODLayerPINDrawing')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Calculate2
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        target_coord = tmp1[0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ODLayerPINDrawing')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_ODLayerPINDrawing')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_ODLayerPINDrawing']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _POLayerPINDrawing
        #Define Boundary_element
        self._DesignParameter['BND_POLayerPINDrawing'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['PCPIN'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayerPINDrawing']['_YWidth'] = (self._DesignParameter['BND_POLayer']['_YWidth'] - self._DesignParameter['BND_ODLayer']['_YWidth']) / 2

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_POLayerPINDrawing']['_XWidth'] = self._DesignParameter['BND_POLayer']['_XWidth']

        # Initialized coordinates
        self._DesignParameter['BND_POLayerPINDrawing']['_XYCoordinates'] = [[0, 0]]

        tmp = self.get_param_KJH4('BND_POLayer')
        tmpxy = []
        for i in range(0,len(tmp)):
            # Define coord
            # Calculate Sref XYcoord
            # Target_coord
            tmp1 = self.get_param_KJH4('BND_POLayer')
            target_coord = tmp1[i][0]['_XY_up_left']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_POLayerPINDrawing')
            approaching_coord = tmp2[0][0]['_XY_up_left']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_POLayerPINDrawing')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpxy.append(New_Scoord)

        tmpxy1 = []
        for i in range(0, len(tmp)):
            # Define coord
            # Calculate Sref XYcoord
            # Target_coord
            tmp1 = self.get_param_KJH4('BND_POLayer')
            target_coord = tmp1[i][0]['_XY_down_left']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_POLayerPINDrawing')
            approaching_coord = tmp2[0][0]['_XY_down_left']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_POLayerPINDrawing')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpxy1.append(New_Scoord)

        if _NumberofGate == 1:
            self._DesignParameter['BND_POLayerPINDrawing']['_XYCoordinates'] = tmpxy + tmpxy1
        else:
            if _MosUpDn == 'Up':
                self._DesignParameter['BND_POLayerPINDrawing']['_XYCoordinates'] = tmpxy
            else:
                self._DesignParameter['BND_POLayerPINDrawing']['_XYCoordinates'] = tmpxy1





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Met1Layer_Source
        #Define Boundary_element
        self._DesignParameter['BND_Source_M1'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_Source_M1']['_YWidth'] = self._DesignParameter['BND_Met1Layer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_Source_M1']['_XWidth'] = self._DesignParameter['BND_Met1Layer']['_XWidth']

        #Define coord
            #For num of M1 in Nmos
        tmp1 = self.get_param_KJH4('BND_Met1Layer')

        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if i%2 == 0 :
                tmp3 = tmp1[i][0]['_XY_down_left']
                tmpXY.append(tmp3)
            #Drain
            else:
                pass

        self._DesignParameter['BND_Source_M1']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Met1Layer_Drain
        #Define Boundary_element
        self._DesignParameter['BND_Drain_M1'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_Drain_M1']['_YWidth'] = self._DesignParameter['BND_Met1Layer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_Drain_M1']['_XWidth'] = self._DesignParameter['BND_Met1Layer']['_XWidth']

        #Define coord
            #For num of M1 in Nmos
        tmp1 = self.get_param_KJH4('BND_Met1Layer')

        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if i%2 != 0 :
                tmp3 = tmp1[i][0]['_XY_down_left']
                tmpXY.append(tmp3)
            #Drain
            else:
                pass

        self._DesignParameter['BND_Drain_M1']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Source_ViaM1M2
        if _Source_Via_TF == True:

            # NotImplementedError
            if _Drain_Via_TF == True:
                if ( _Source_Via_Close2POpin_TF == _Drain_Via_Close2POpin_TF ):
                    print('Error Occurred: Drain Source Via conflict')
                    raise NotImplementedError
                else:
                    pass
            else:
                pass

            #Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] 	= 1
            _Caculation_Parameters['_Layer2'] 	= 2
            _Caculation_Parameters['_COX'] 		= None
            _Caculation_Parameters['_COY'] 		= None

            #Sref ViaX declaration
            self._DesignParameter['SRF_Source_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Source_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_Source_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_Source_ViaM1M2']['_Angle'] = 0

            #Calcuate _COX
            _Caculation_Parameters['_COX'] = 1

            #Calcuate _COY
                #Calculate Number of V1
            tmp   		= self.get_param_KJH4('BND_Met1Layer')
            M1_ywidth	= tmp[0][0]['_Ywidth']
            Num_V1      = int( ( M1_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) ) + 0
                #Define Num of V1
            if Num_V1<2:
                _Caculation_Parameters['_COY'] = 2
            else:
                _Caculation_Parameters['_COY'] = Num_V1

            #Generate Metal(x), Metal(x+1) and C0(Viax) layer
            self._DesignParameter['SRF_Source_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['SRF_Source_ViaM1M2']['_XYCoordinates'] = [[0,0]]

                #Define flag
            flag = 1

                #For num of M1 in Nmos
            tmp1 = self.get_param_KJH4('BND_Met1Layer')
            tmpXY = []
            for i in range(0,len(tmp1)):

                #Source
                if flag == 1:
                        #Calculate
                            #Target_coord
                    if _MosUpDn == 'Up':
                        if _Source_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('BND_Met1Layer')
                            target_coord = tmp1[i][0]['_XY_up']
                        else:
                            tmp1 = self.get_param_KJH4('BND_Met1Layer')
                            target_coord = tmp1[i][0]['_XY_up']
                            target_coord[1] = target_coord[1] - 64
                    else:
                        if _Source_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('BND_Met1Layer')
                            target_coord = tmp1[i][0]['_XY_down']
                        else:
                            tmp1 = self.get_param_KJH4('BND_Met1Layer')
                            target_coord = tmp1[i][0]['_XY_down']
                            target_coord[1] = target_coord[1] + 64

                            #Approaching_coord
                    if _MosUpDn == 'Up':
                        if _Source_Via_Close2POpin_TF == True:
                            tmp2 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
                            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                        else:
                            tmp2 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
                            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    else:
                        if _Source_Via_Close2POpin_TF == True:
                            tmp2 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
                            approaching_coord = tmp2[0][0][0][0]['_XY_down']
                        else:
                            tmp2 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
                            approaching_coord = tmp2[0][0][0][0]['_XY_down']

                            #Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Source_ViaM1M2')
                    Scoord = tmp3[0][0]['_XY_origin']
                            #Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                    tmpXY.append(New_Scoord)

                    flag = -1
                #Drain
                else:
                    flag = +1

            self._DesignParameter['SRF_Source_ViaM1M2']['_XYCoordinates'] = tmpXY



        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Drain_ViaM1M2
        if _Drain_Via_TF == True:

            # NotImplementedError
            if _Source_Via_TF == True:
                if ( _Source_Via_Close2POpin_TF == _Drain_Via_Close2POpin_TF ):
                    print('Error Occurred: Drain Source Via conflict')
                    raise NotImplementedError
                else:
                    pass
            else:
                pass

            #Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] 	= 1
            _Caculation_Parameters['_Layer2'] 	= 2
            _Caculation_Parameters['_COX'] 		= None
            _Caculation_Parameters['_COY'] 		= None

            #Sref ViaX declaration
            self._DesignParameter['SRF_Drain_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Drain_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_Drain_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_Drain_ViaM1M2']['_Angle'] = 0

            #Calcuate _COX
            _Caculation_Parameters['_COX'] = 1

            #Calcuate _COY
                #Calculate Number of V1
            tmp   		= self.get_param_KJH4('BND_Met1Layer')
            M1_ywidth	= tmp[0][0]['_Ywidth']
            Num_V1      = int( ( M1_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) ) + 0
                #Define Num of V1
            if Num_V1<2:
                _Caculation_Parameters['_COY'] = 2
            else:
                _Caculation_Parameters['_COY'] = Num_V1

            #Generate Metal(x), Metal(x+1) and C0(Viax) layer
            self._DesignParameter['SRF_Drain_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['SRF_Drain_ViaM1M2']['_XYCoordinates'] = [[0,0]]

                #Define flag
            flag = 1

                #For num of M1 in Nmos
            tmp1 = self.get_param_KJH4('BND_Met1Layer')
            tmpXY = []
            for i in range(0,len(tmp1)):

                #Source
                if flag == 1:
                    flag = -1
                #Drain
                else:
                    #Calculate
                        #Target_coord
                    if _MosUpDn == 'Up':
                        if _Drain_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('BND_Met1Layer')
                            target_coord = tmp1[i][0]['_XY_up']
                        else:
                            tmp1 = self.get_param_KJH4('BND_Met1Layer')
                            target_coord = tmp1[i][0]['_XY_up']
                            target_coord[1] = target_coord[1] - 64
                    else:
                        if _Drain_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('BND_Met1Layer')
                            target_coord = tmp1[i][0]['_XY_down']
                        else:
                            tmp1 = self.get_param_KJH4('BND_Met1Layer')
                            target_coord = tmp1[i][0]['_XY_down']
                            target_coord[1] = target_coord[1] + 64

                        #Approaching_coord
                    if _MosUpDn == 'Up':
                        if _Drain_Via_Close2POpin_TF == True:
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
                            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                        else:
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
                            approaching_coord = tmp2[0][0][0][0]['_XY_up']
                    else:
                        if _Drain_Via_Close2POpin_TF == True:
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
                            approaching_coord = tmp2[0][0][0][0]['_XY_down']
                        else:
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
                            approaching_coord = tmp2[0][0][0][0]['_XY_down']

                        #Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Drain_ViaM1M2')
                    Scoord = tmp3[0][0]['_XY_origin']
                            #Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                    tmpXY.append(New_Scoord)

                    flag = +1

            self._DesignParameter['SRF_Drain_ViaM1M2']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Source_Comb_TF
        if (_Source_Comb_TF == True) and (_Source_Via_TF ==True):

            # NotImplementedError
            if _Drain_Via_TF == True:
                if _Drain_Comb_TF == True:
                    if (_Drain_Comb_POpinward_TF == _Source_Comb_POpinward_TF):
                        print('Error Occurred: Drain Source Via conflict')
                        raise NotImplementedError
                    else:
                        pass
                else:
                    pass
            else:
                pass

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Source_Comb_TF : Vtc M2
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Source_Vtc_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth : ViaYmin 기준
                # Check Pinward
            if _MosUpDn == 'Up':
                POpinward   = 'up'
                POpinwardB  = 'down'
            else:
                POpinward   = 'down'
                POpinwardB  = 'up'

                ## _YWidth
            if _Source_Comb_Length ==None:
                if _Source_Comb_POpinward_TF == True:
                    if _Drain_Via_TF == True:
                        # length(x),Pinward,DrainVia(o),SourceVia to pin
                        if _Source_Via_Close2POpin_TF == True:
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _DRCObj._MetalxMinSpace41
                        # length(x),Pinward,DrainVia to pin,SourceVia
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Source_M1')
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _DRCObj._MetalxMinSpace41 + abs( tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1] - tmp2[0][0]['_XY_{}'.format(POpinward)][1] )
                    else:
                        # length(x),Pinward,DrainVia(x),SourceVia to pin
                        if _Source_Via_Close2POpin_TF == True:
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _DRCObj._MetalxMinSpace41
                        # length(x),Pinward,DrainVia(x),SourceVia
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Source_M1')
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _DRCObj._MetalxMinSpace41 + abs( tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1] - tmp2[0][0]['_XY_{}'.format(POpinward)][1] )
                else:
                    if _Drain_Via_TF == True:
                        # length(x),PinwardB,DrainVia(o),SourceVia to pin
                        if _Source_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']+ _DRCObj._MetalxMinSpace41 + abs( tmp1[0][0][0][0]['_XY_{}'.format(POpinwardB)][1] - tmp2[0][0][0][0]['_XY_{}'.format(POpinwardB)][1] )
                        # length(x),PinwardB,DrainVia to pin,SourceVia
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp3 = self.get_param_KJH4('BND_Source_M1')
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = abs(tmp3[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1]) \
                                                                                    + tmp1[0][0][0][0]['_Ywidth'] +( _DRCObj._MetalxMinSpace41 - abs( tmp1[0][0][0][0]['_XY_{}'.format(POpinwardB)][1] - tmp2[0][0][0][0]['_XY_{}'.format(POpinwardB)][1] ) )
                    else:
                        # length(x),PinwardB,DrainVia(x),SourceVia to pin
                        if _Source_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']
                        # length(x),PinwardB,DrainVia(x),SourceVia
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Source_M1')
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth'] + abs(tmp2[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])
            else:
                if _Source_Comb_POpinward_TF == True:
                    if _Drain_Via_TF == True:
                        # length(o),Pinward,DrainVia(o),SourceVia to pin
                        if _Source_Via_Close2POpin_TF == True:
                            if _DRCObj._MetalxMinSpace41 > _Source_Comb_Length:
                                raise NotImplementedError
                            else:
                                self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _Source_Comb_Length
                        # length(o),Pinward,DrainVia to pin,SourceVia
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Source_M1')
                            if (_DRCObj._MetalxMinSpace41+ abs(tmp2[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])) > _Source_Comb_Length:
                                raise NotImplementedError
                            else:
                                self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _Source_Comb_Length + abs(tmp2[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])
                    else:
                        # length(o),Pinward,DrainVia(x),SourceVia to pin
                        if _Source_Via_Close2POpin_TF == True:
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _Source_Comb_Length
                        # length(o),Pinward,DrainVia(x),SourceVia
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Source_M1')
                            self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _Source_Comb_Length + abs( tmp2[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])
                else:
                    if _Drain_Via_TF == True:
                        # length(o),PinwardB,DrainVia(o),SourceVia to pin
                        if _Source_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            if _Source_Comb_Length < (_DRCObj._MetalxMinSpace41 + abs(tmp2[0][0][0][0]['_XY_{}'.format(POpinwardB)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])):
                                raise NotImplementedError("Source and Drain short error")
                            else:
                                self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _Source_Comb_Length

                        # length(o),PinwardB,DrainVia to pin,SourceVia
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp3 = self.get_param_KJH4('BND_Source_M1')
                            if _Source_Comb_Length < (tmp2[0][0][0][0]['_Ywidth'] + _DRCObj._MetalxMinSpace41):
                                raise NotImplementedError("Source and Drain short error")
                            else:
                                self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _Source_Comb_Length
                    else:
                        # length(o),PinwardB,DrainVia(x),SourceVia to pin
                        if _Source_Via_Close2POpin_TF == True:
                            if _Source_Comb_Length < 50:
                                raise NotImplementedError("too short")
                            else:
                                self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _Source_Comb_Length
                        # length(o),PinwardB,DrainVia(x),SourceVia
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp3 = self.get_param_KJH4('BND_Source_M1')
                            if _Source_Comb_Length < (50 + abs(tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1] - tmp3[0][0]['_XY_{}'.format(POpinward)][1])):
                                raise NotImplementedError("too short")
                            else:
                                self._DesignParameter['BND_Source_Vtc_M2']['_YWidth'] = _Source_Comb_Length

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            self._DesignParameter['BND_Source_Vtc_M2']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Source_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            tmp = self.get_param_KJH4('BND_Source_M1')
            for i in range(0, len(tmp)):
                ## Calculate Sref XYcoord
                ## Calculate
                    ## Target_coord: _XY_type1
                if _Source_Via_Close2POpin_TF == True:
                    tmp1 = self.get_param_KJH4('BND_Source_M1')
                    target_coord = tmp1[i][0]['_XY_{}_left'.format(POpinward)]
                else:
                    tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                    target_coord = tmp1[i][0][0][0]['_XY_{}_left'.format(POpinward)]

                    ## Approaching_coord: _XY_type2
                if _Source_Comb_POpinward_TF == True:
                    tmp2 = self.get_param_KJH4('BND_Source_Vtc_M2')
                    approaching_coord = tmp2[0][0]['_XY_{}_left'.format(POpinwardB)]
                else:
                    tmp2 = self.get_param_KJH4('BND_Source_Vtc_M2')
                    approaching_coord = tmp2[0][0]['_XY_{}_left'.format(POpinward)]

                    ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Source_Vtc_M2')
                Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_Source_Vtc_M2']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Source_Comb_TF : Hrz M2
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Source_Hrz_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth :
            self._DesignParameter['BND_Source_Hrz_M2']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_Source_Vtc_M2')
            self._DesignParameter['BND_Source_Hrz_M2']['_XWidth'] = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Source_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []
                ## Calculate Sref XYcoord
                    ## Calculate
                        ## Target_coord: _XY_type1
            if _Source_Comb_POpinward_TF == True:
                tmp1 = self.get_param_KJH4('BND_Source_Vtc_M2')
                target_coord = tmp1[0][0]['_XY_{}_left'.format(POpinward)]
            else:
                tmp1 = self.get_param_KJH4('BND_Source_Vtc_M2')
                target_coord = tmp1[0][0]['_XY_{}_left'.format(POpinwardB)]

                        ## Approaching_coord: _XY_type2
            if _Source_Comb_POpinward_TF == True:
                tmp2 = self.get_param_KJH4('BND_Source_Hrz_M2')
                approaching_coord = tmp2[0][0]['_XY_{}_left'.format(POpinwardB)]
            else:
                tmp2 = self.get_param_KJH4('BND_Source_Hrz_M2')
                approaching_coord = tmp2[0][0]['_XY_{}_left'.format(POpinward)]

                        ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Source_Hrz_M2')
            Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                ## Define coordinates
            self._DesignParameter['BND_Source_Hrz_M2']['_XYCoordinates'] = tmpXY





        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Drain_Comb_TF
        if (_Drain_Comb_TF == True) and (_Drain_Via_TF ==True):

            # NotImplementedError
            if _Source_Via_TF == True:
                if _Source_Comb_TF == True:
                    if (_Drain_Comb_POpinward_TF == _Source_Comb_POpinward_TF):
                        print('Error Occurred: Drain Source Via conflict')
                        raise NotImplementedError
                    else:
                        pass
                else:
                    pass
            else:
                pass

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Drain_Comb_TF : Vtc M2
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth : ViaYmin 기준
            # Check Pinward
            if _MosUpDn == 'Up':
                POpinward = 'up'
                POpinwardB = 'down'
            else:
                POpinward = 'down'
                POpinwardB = 'up'

                ## _YWidth
            if _Drain_Comb_Length == None:
                if _Drain_Comb_POpinward_TF == True:
                    if _Source_Via_TF == True:
                        # length(x),Pinward,DrainVia to pin,SourceVia(o)
                        if _Drain_Via_Close2POpin_TF == True:
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _DRCObj._MetalxMinSpace41
                        # length(x),Pinward,DrainVia(o),SourceVia to pin
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Drain_M1')
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _DRCObj._MetalxMinSpace41 + abs(tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1] - tmp2[0][0]['_XY_{}'.format(POpinward)][1])
                    else:
                        # length(x),Pinward,DrainVia to pin,SourceVia(x)
                        if _Drain_Via_Close2POpin_TF == True:
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _DRCObj._MetalxMinSpace41
                        # length(x),Pinward,DrainVia(o),SourceVia(x)
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Drain_M1')
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _DRCObj._MetalxMinSpace41 + abs(tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1] - tmp2[0][0]['_XY_{}'.format(POpinward)][1])
                else:
                    if _Source_Via_TF == True:
                        # length(x),PinwardB,DrainVia to pin,SourceVia(o)
                        if _Drain_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth'] + _DRCObj._MetalxMinSpace41 + abs( tmp1[0][0][0][0]['_XY_{}'.format(POpinwardB)][1] - tmp2[0][0][0][0]['_XY_{}'.format(POpinwardB)][1])
                        # length(x),PinwardB,DrainVia(o),SourceVia to pin
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp3 = self.get_param_KJH4('BND_Drain_M1')
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = abs( tmp3[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1]) \
                                                                                    + tmp1[0][0][0][0]['_Ywidth'] + ( _DRCObj._MetalxMinSpace41 - abs( tmp1[0][0][0][0]['_XY_{}'.format(POpinwardB)][1] - tmp2[0][0][0][0]['_XY_{}'.format(POpinwardB)][1]))
                    else:
                        # length(x),PinwardB,DrainVia to pin,SourceVia(x)
                        if _Drain_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']
                        # length(x),PinwardB,DrainVia(o),SourceVia(x)
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Drain_M1')
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth'] + abs( tmp2[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])
            else:
                if _Drain_Comb_POpinward_TF == True:
                    if _Source_Via_TF == True:
                        # length(o),Pinward,DrainVia to pin,SourceVia(o)
                        if _Drain_Via_Close2POpin_TF == True:
                            if _DRCObj._MetalxMinSpace41 > _Drain_Comb_Length:
                                raise NotImplementedError
                            else:
                                self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _Drain_Comb_Length
                        # length(o),Pinward,DrainVia(o),SourceVia to pin
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Drain_M1')
                            if (_DRCObj._MetalxMinSpace41+ abs( tmp2[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])) > _Drain_Comb_Length:
                                raise NotImplementedError
                            else:
                                self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _Drain_Comb_Length + abs( tmp2[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])
                    else:
                        # length(o),Pinward,DrainVia to pin,SourceVia(x)
                        if _Drain_Via_Close2POpin_TF == True:
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _Drain_Comb_Length
                        # length(o),Pinward,DrainVia(o),SourceVia(x)
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('BND_Drain_M1')
                            self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _Drain_Comb_Length + abs( tmp2[0][0]['_XY_{}'.format(POpinward)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])
                else:
                    if _Source_Via_TF == True:
                        # length(o),PinwardB,DrainVia to pin,SourceVia(o)
                        if _Drain_Via_Close2POpin_TF == True:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            if _Drain_Comb_Length < (_DRCObj._MetalxMinSpace41 +  abs(tmp2[0][0][0][0]['_XY_{}'.format(POpinwardB)][1] - tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1])):
                                raise NotImplementedError("Source and Drain short error")
                            else:
                                self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _Drain_Comb_Length

                        # length(o),PinwardB,DrainVia(o),SourceVia to pin
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp3 = self.get_param_KJH4('BND_Drain_M1')
                            if _Drain_Comb_Length < tmp1[0][0][0][0]['_Ywidth'] + _DRCObj._MetalxMinSpace41 :
                                raise NotImplementedError("Source and Drain short error")
                            else:
                                self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _Drain_Comb_Length
                    else:
                        # length(o),PinwardB,DrainVia to pin,SourceVia(x)
                        if _Drain_Via_Close2POpin_TF == True:
                            if _Drain_Comb_Length < 50:
                                raise NotImplementedError("too short")
                            else:
                                self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _Drain_Comb_Length
                        # length(o),PinwardB,DrainVia(o),SourceVia(x)
                        else:
                            tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                            tmp3 = self.get_param_KJH4('BND_Drain_M1')
                            if _Drain_Comb_Length < (50 + abs(tmp1[0][0][0][0]['_XY_{}'.format(POpinward)][1] - tmp3[0][0]['_XY_{}'.format(POpinward)][1])):
                                raise NotImplementedError("too short")
                            else:
                                self._DesignParameter['BND_Drain_Vtc_M2']['_YWidth'] = _Drain_Comb_Length

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
            self._DesignParameter['BND_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

            tmpXY = []
            tmp = self.get_param_KJH4('BND_Drain_M1')
            for i in range(0, len(tmp)):
                ## Calculate Sref XYcoord
                ## Calculate
                ## Target_coord: _XY_type1
                if _Drain_Via_Close2POpin_TF == True:
                    tmp1 = self.get_param_KJH4('BND_Drain_M1')
                    target_coord = tmp1[i][0]['_XY_{}_left'.format(POpinward)]
                else:
                    tmp1 = self.get_param_KJH4('SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
                    target_coord = tmp1[i][0][0][0]['_XY_{}_left'.format(POpinward)]

                ## Approaching_coord: _XY_type2
                if _Drain_Comb_POpinward_TF == True:
                    tmp2 = self.get_param_KJH4('BND_Drain_Vtc_M2')
                    approaching_coord = tmp2[0][0]['_XY_{}_left'.format(POpinwardB)]
                else:
                    tmp2 = self.get_param_KJH4('BND_Drain_Vtc_M2')
                    approaching_coord = tmp2[0][0]['_XY_{}_left'.format(POpinward)]

                    ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Drain_Vtc_M2')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
            ## Define coordinates
            self._DesignParameter['BND_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## _Drain_Comb_TF : Hrz M2
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth :
            self._DesignParameter['BND_Drain_Hrz_M2']['_YWidth'] = 50

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_Drain_Vtc_M2')
            self._DesignParameter['BND_Drain_Hrz_M2']['_XWidth'] = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
            tmpXY = []
                ## Calculate Sref XYcoord
                    ## Calculate
                        ## Target_coord: _XY_type1
            if _Drain_Comb_POpinward_TF == True:
                tmp1 = self.get_param_KJH4('BND_Drain_Vtc_M2')
                target_coord = tmp1[0][0]['_XY_{}_left'.format(POpinward)]
            else:
                tmp1 = self.get_param_KJH4('BND_Drain_Vtc_M2')
                target_coord = tmp1[0][0]['_XY_{}_left'.format(POpinwardB)]

                        ## Approaching_coord: _XY_type2
            if _Drain_Comb_POpinward_TF == True:
                tmp2 = self.get_param_KJH4('BND_Drain_Hrz_M2')
                approaching_coord = tmp2[0][0]['_XY_{}_left'.format(POpinwardB)]
            else:
                tmp2 = self.get_param_KJH4('BND_Drain_Hrz_M2')
                approaching_coord = tmp2[0][0]['_XY_{}_left'.format(POpinward)]

                        ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Drain_Hrz_M2')
            Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                ## Define coordinates
            self._DesignParameter['BND_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY






        if _POGate_Comb_TF == True:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Poly combine
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Poly combine : Vtc
            ## Pre-defined
            if _POGate_Comb_length == None:
                Ywidth_0 = 150
            else:
                Ywidth_0 = _POGate_Comb_length

            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_Gate_Vtc_poly']['_YWidth'] = Ywidth_0

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_POLayer')
            self._DesignParameter['BND_Gate_Vtc_poly']['_XWidth'] = tmp[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['BND_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            tmp = self.get_param_KJH4('BND_POLayer')
            for i in range(0, len(tmp)):
                ## Target_coord: _XY_type1
                if _MosUpDn == 'Up':
                    tmp1 = self.get_param_KJH4('BND_POLayer')
                    target_coord = tmp1[i][0]['_XY_up_left']
                else:
                    tmp1 = self.get_param_KJH4('BND_POLayer')
                    target_coord = tmp1[i][0]['_XY_down_left']

                ## Approaching_coord: _XY_type2
                if _MosUpDn == 'Up':
                    tmp2 = self.get_param_KJH4('BND_Gate_Vtc_poly')
                    approaching_coord = tmp2[0][0]['_XY_down_left']
                else:
                    tmp2 = self.get_param_KJH4('BND_Gate_Vtc_poly')
                    approaching_coord = tmp2[0][0]['_XY_up_left']

                ## Sref coord
                tmp3 = self.get_param_KJH4('BND_Gate_Vtc_poly')
                Scoord = tmp3[0][0]['_XY_origin']
                ## Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                tmpXY.append(New_Scoord)
                ## Define coordinates
            self._DesignParameter['BND_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Poly combine : Hrz
            ## Pre-defined
            Ywidth_1 = 50

            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            self._DesignParameter['BND_Gate_Hrz_poly']['_YWidth'] = Ywidth_1

            ## Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH4('BND_POLayer')
            self._DesignParameter['BND_Gate_Hrz_poly']['_XWidth'] = abs( tmp1[0][0]['_XY_left'][0] - tmp1[-1][0]['_XY_right'][0])

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
                ## initialized Sref coordinate
            self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord: _XY_type1
            if _MosUpDn == 'Up':
                tmp1 = self.get_param_KJH4('BND_Gate_Vtc_poly')
                target_coord = tmp1[0][0]['_XY_up_left']
            else:
                tmp1 = self.get_param_KJH4('BND_Gate_Vtc_poly')
                target_coord = tmp1[0][0]['_XY_down_left']

                    ## Approaching_coord: _XY_type2
            if _MosUpDn == 'Up':
                tmp2 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                approaching_coord = tmp2[0][0]['_XY_down_left']
            else:
                tmp2 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                approaching_coord = tmp2[0][0]['_XY_up_left']

                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Gate_Hrz_poly')
            Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                ## Define coordinates
            self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY





            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Gate _ViaM0M1
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaMxMx : Metalx
            ## Boundary_element Generation
            ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['BND_Gate_Hrz_Mx'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL{}'.format(_POGate_ViaMxMx[1])][0],
                _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_POGate_ViaMxMx[1])][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            ## Define Boundary_element _YWidth
            tmp = self.get_param_KJH4('BND_Gate_Hrz_poly')
            self._DesignParameter['BND_Gate_Hrz_Mx']['_YWidth'] = tmp[0][0]['_Ywidth']

            ## Define Boundary_element _XWidth
            tmp = self.get_param_KJH4('BND_Gate_Hrz_poly')
            self._DesignParameter['BND_Gate_Hrz_Mx']['_XWidth'] = tmp[0][0]['_Xwidth']

            ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_Gate_Hrz_Mx']['_XYCoordinates'] = [[0, 0]]

            ## Calculate Sref XYcoord
            tmpXY = []
                ## initialized Sref coordinate
            self._DesignParameter['BND_Gate_Hrz_Mx']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord: _XY_type1
            tmp1 = self.get_param_KJH4('BND_Gate_Hrz_poly')
            target_coord = tmp1[0][0]['_XY_down_left']
                    ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
            Scoord = tmp3[0][0]['_XY_origin']
                    ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                ## Define coordinates
            self._DesignParameter['BND_Gate_Hrz_Mx']['_XYCoordinates'] = tmpXY

            if _POGate_Via_TF == True:
                ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaMxMx : _ViaMxMx
                ## Sref generation: ViaX
                    ## Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] = 0
                _Caculation_Parameters['_Layer2'] = _POGate_ViaMxMx[1]
                _Caculation_Parameters['_COX'] = None
                _Caculation_Parameters['_COY'] = None

                    ## Sref ViaX declaration
                self._DesignParameter['SRF_Gate_ViaM0Mx'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_Gate_ViaM0Mx'.format(_Name)))[0]

                    ## Define Sref Relection
                self._DesignParameter['SRF_Gate_ViaM0Mx']['_Reflect'] = [0, 0, 0]

                    ## Define Sref Angle
                self._DesignParameter['SRF_Gate_ViaM0Mx']['_Angle'] = 0

                    ## Calcuate Overlapped XYcoord
                tmp1 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
                tmp2 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

                    ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
                _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

                ## Define _COX and _COY
                if _COX < 2:
                    ## Finger = 1
                    if _NumberofGate == 1:
                        _Caculation_Parameters['_COX'] = 2
                        _Caculation_Parameters['_COY'] = 1
                        flag = 1
                        ## Finger = 2
                    else:
                        _Caculation_Parameters['_COX'] = 2
                        _Caculation_Parameters['_COY'] = _COY
                        flag = 1
                else:
                    _Caculation_Parameters['_COX'] = _COX
                    _Caculation_Parameters['_COY'] = _COY
                    flag = 0

                if flag == 0:
                    ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_DesignObj']._CalculateDesignParameterYmin( **_Caculation_Parameters)

                    ## Calculate Sref XYcoord
                    tmpXY = []
                        ## initialized Sref coordinate
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord
                    if _MosUpDn == 'Up':
                        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
                        target_coord = tmp1[0][0]['_XY_down']
                    else:
                        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
                        target_coord = tmp1[0][0]['_XY_up']

                            ## Approaching_coord
                    if _MosUpDn == 'Up':
                        #tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M{}'.format(_POGate_ViaMxMx[1]),'BND_POLayer')
                        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]),'BND_POLayer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_down']
                    else:
                        #tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M{}'.format(_POGate_ViaMxMx[1]),'BND_POLayer')
                        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]),'BND_POLayer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_up']

                            ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0Mx')
                    Scoord = tmp3[0][0]['_XY_origin']
                            ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                        ## Define
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_XYCoordinates'] = tmpXY

                    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaM0Mx : _ViaM0Mx : Poly Exten
                    ## Define Boundary_element _YWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1', 'BND_POLayer')
                    self._DesignParameter['BND_Gate_Hrz_poly']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                    ## Define Boundary_element _XYCoordinates
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
                    tmpXY = []
                        ## initialized Sref coordinate
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1', 'BND_POLayer')
                    target_coord = tmp1[0][0][0][0]['_XY_down']

                            ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                    approaching_coord = tmp2[0][0]['_XY_down']

                            ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                    Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                        ## Define coordinates
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY


                    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaM0Mx : _ViaM0Mx : Mx Exten
                    ## Define Boundary_element _YWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]), 'BND_Met{}Layer'.format(_POGate_ViaMxMx[1]))
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                    ## Define Boundary_element _XYCoordinates
                    ## Calculate Sref XYcoord
                    tmpXY = []
                        ## initialized Sref coordinate
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]), 'BND_Met{}Layer'.format(_POGate_ViaMxMx[1]))
                    target_coord = tmp1[0][0][0][0]['_XY_cent']

                            ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
                    approaching_coord = tmp2[0][0]['_XY_cent']

                            ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
                    Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                        ## Define coordinates
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_XYCoordinates'] = tmpXY

                if flag == 1:
                    ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_DesignObj']._CalculateDesignParameterYmin( **_Caculation_Parameters)

                    ## Calculate Sref XYcoord
                    tmpXY = []
                    ## initialized Sref coordinate
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord
                    if _MosUpDn == 'Up':
                        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                        target_coord = tmp1[0][0]['_XY_down']
                    else:
                        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                        target_coord = tmp1[0][0]['_XY_up']

                            ## Approaching_coord
                    if _MosUpDn == 'Up':
                        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1','BND_POLayer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_down']
                    else:
                        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1','BND_POLayer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_up']

                            ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0Mx')
                    Scoord = tmp3[0][0]['_XY_origin']
                            ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                        ## Define
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_XYCoordinates'] = tmpXY

                    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaM0Mx : _ViaM0Mx : Poly Exten
                    ## Define Boundary_element _XWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1', 'BND_POLayer')
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']+40

                    ## Define Boundary_element _YWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1', 'BND_POLayer')
                    self._DesignParameter['BND_Gate_Hrz_poly']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                    ## Define Boundary_element _XYCoordinates
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
                    tmpXY = []
                        ## initialized Sref coordinate
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1', 'BND_POLayer')
                    target_coord = tmp1[0][0][0][0]['_XY_down']

                            ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                    approaching_coord = tmp2[0][0]['_XY_down']

                            ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                    Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                        ## Define coordinates
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

                    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaM0Mx : _ViaM0Mx : Mx Exten
                    ## Define Boundary_element _XWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]), 'BND_Met{}Layer'.format(_POGate_ViaMxMx[1]))
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth'] + 40

                    ## Define Boundary_element _YWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]), 'BND_Met{}Layer'.format(_POGate_ViaMxMx[1]))
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                    ## Define Boundary_element _XYCoordinates
                    ## Calculate Sref XYcoord
                    tmpXY = []
                        ## initialized Sref coordinate
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]), 'BND_Met{}Layer'.format(_POGate_ViaMxMx[1]))
                    target_coord = tmp1[0][0][0][0]['_XY_cent']

                            ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
                    approaching_coord = tmp2[0][0]['_XY_cent']

                            ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_Gate_Hrz_Mx')
                    Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                        ## Define coordinates
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_XYCoordinates'] = tmpXY


                if flag == 2:
                    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaM0Mx : _ViaM0Mx
                    ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_DesignObj']._CalculateDesignParameter( **_Caculation_Parameters)

                    ## Calculate Sref XYcoord
                    tmpXY = []
                        ## initialized Sref coordinate
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord
                    if _MosUpDn == 'Up':
                        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                        target_coord = tmp1[0][0]['_XY_down']
                    else:
                        tmp1 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                        target_coord = tmp1[0][0]['_XY_up']

                            ## Approaching_coord
                    if _MosUpDn == 'Up':
                        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1','BND_POLayer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_down']
                    else:
                        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1','BND_POLayer')
                        approaching_coord = tmp2[0][0][0][0]['_XY_up']

                            ## Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0Mx')
                    Scoord = tmp3[0][0]['_XY_origin']
                            ## Calculate
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                        ## Define
                    self._DesignParameter['SRF_Gate_ViaM0Mx']['_XYCoordinates'] = tmpXY

                    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaM0Mx : _ViaM0Mx : Poly Exten
                    ## Define Boundary_element _XWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1','BND_POLayer')
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

                    ## Define Boundary_element _YWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1','BND_POLayer')
                    self._DesignParameter['BND_Gate_Hrz_poly']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                    ## Define Boundary_element _XYCoordinates
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
                    tmpXY = []
                        ## initialized Sref coordinate
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
                    tmp1_1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM0M1','BND_POLayer')
                    target_coord = tmp1_1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
                    tmp2 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                    approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
                    tmp3 = self.get_param_KJH4('BND_Gate_Hrz_poly')
                    Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                    tmpXY.append(New_Scoord)
                        ## Define coordinates
                    self._DesignParameter['BND_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

                    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## Gate _ViaM0Mx : _ViaM0Mx : Mx Exten
                    ## Define Boundary_element _XWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]),'BND_Met{}Layer'.format(_POGate_ViaMxMx[1]))
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

                    ## Define Boundary_element _YWidth
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]),'BND_Met{}Layer'.format(_POGate_ViaMxMx[1]))
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

                    ## Define Boundary_element _XYCoordinates
                    tmp1 = self.get_param_KJH4('SRF_Gate_ViaM0Mx', 'SRF_ViaM{}M{}'.format(_POGate_ViaMxMx[1]-1,_POGate_ViaMxMx[1]),'BND_Met{}Layer'.format(_POGate_ViaMxMx[1]))
                    self._DesignParameter['BND_Gate_Hrz_Mx']['_XYCoordinates'] = [tmp1[0][0][0][0]['_XY_down_left']]


            if _PODummy_TF == True:
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## POLY_Dummy_Layer2:manual setting
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## POLY_Dummy_Layer2:manual setting:dummy_length
                if _PODummy_Length == None:

                    # Poly minimum area constraint
                    tmp = self.get_param_KJH4('BND_PODummyLayer')
                    area = np.array(tmp[0][0]['_Ywidth']) * np.array(tmp[0][0]['_Xwidth'])
                    if area < 11000:
                        self._DesignParameter['BND_PODummyLayer']['_YWidth'] = np.ceil( 11000 / np.array(tmp[0][0]['_Xwidth']))
                        flag = 1
                    else:
                        flag = 0
                else:
                    self._DesignParameter['BND_PODummyLayer']['_YWidth'] = _PODummy_Length
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## POLY_Dummy_Layer2:manual setting:dummy_placement
                if _PODummy_Placement == None:

                    ## Poly minimum area constraint: Place to 'Up'
                    if flag ==1:
                        self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = [[0, 0]]

                        # Check Gate Polylength
                        tmp = self.get_param_KJH4('BND_POLayer')
                        POLayer_Ywidth = tmp[0][0]['_Ywidth']
                        if POLayer_Ywidth > self._DesignParameter['BND_PODummyLayer']['_YWidth']:
                            tmpXY = []
                            for i in [0, -1]:
                                if i == 0:
                                    # Calculate
                                    # Target_coord
                                    tmp1 = self.get_param_KJH4('BND_POLayer')
                                    target_coord = tmp1[i][0]['_XY_cent']
                                    # Approaching_coord
                                    tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                                    approaching_coord = tmp2[0][0]['_XY_cent']
                                    # Sref coord
                                    tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                                    Scoord = tmp3[0][0]['_XY_origin']
                                    # Cal
                                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                                    New_Scoord[0] = New_Scoord[0] - _LengthBtwPO
                                    tmpXY.append(New_Scoord)

                                else:
                                    # Calculate
                                    # Target_coord
                                    tmp1 = self.get_param_KJH4('BND_POLayer')
                                    target_coord = tmp1[i][0]['_XY_cent']
                                    # Approaching_coord
                                    tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                                    approaching_coord = tmp2[0][0]['_XY_cent']
                                    # Sref coord
                                    tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                                    Scoord = tmp3[0][0]['_XY_origin']
                                    # Cal
                                    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                                    New_Scoord[0] = New_Scoord[0] + _LengthBtwPO
                                    tmpXY.append(New_Scoord)

                        else:
                            if _MosUpDn == 'Up':
                                tmpXY = []
                                for i in [0, -1]:
                                    if i == 0:
                                        # Calculate
                                        # Target_coord
                                        tmp1 = self.get_param_KJH4('BND_POLayer')
                                        target_coord = tmp1[i][0]['_XY_up']
                                        # Approaching_coord
                                        tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                                        approaching_coord = tmp2[0][0]['_XY_up']
                                        # Sref coord
                                        tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                                        Scoord = tmp3[0][0]['_XY_origin']
                                        # Cal
                                        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                                        New_Scoord[0] = New_Scoord[0] - _LengthBtwPO
                                        tmpXY.append(New_Scoord)
                                    else:
                                        # Calculate
                                        # Target_coord
                                        tmp1 = self.get_param_KJH4('BND_POLayer')
                                        target_coord = tmp1[i][0]['_XY_up']
                                        # Approaching_coord
                                        tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                                        approaching_coord = tmp2[0][0]['_XY_up']
                                        # Sref coord
                                        tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                                        Scoord = tmp3[0][0]['_XY_origin']
                                        # Cal
                                        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                                        New_Scoord[0] = New_Scoord[0] + _LengthBtwPO
                                        tmpXY.append(New_Scoord)
                            else:
                                tmpXY = []
                                for i in [0, -1]:
                                    if i == 0:
                                        # Calculate
                                        # Target_coord
                                        tmp1 = self.get_param_KJH4('BND_POLayer')
                                        target_coord = tmp1[i][0]['_XY_down']
                                        # Approaching_coord
                                        tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                                        approaching_coord = tmp2[0][0]['_XY_down']
                                        # Sref coord
                                        tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                                        Scoord = tmp3[0][0]['_XY_origin']
                                        # Cal
                                        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                                        New_Scoord[0] = New_Scoord[0] - _LengthBtwPO
                                        tmpXY.append(New_Scoord)
                                    else:
                                        # Calculate
                                        # Target_coord
                                        tmp1 = self.get_param_KJH4('BND_POLayer')
                                        target_coord = tmp1[i][0]['_XY_down']
                                        # Approaching_coord
                                        tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                                        approaching_coord = tmp2[0][0]['_XY_down']
                                        # Sref coord
                                        tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                                        Scoord = tmp3[0][0]['_XY_origin']
                                        # Cal
                                        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                                        New_Scoord[0] = New_Scoord[0] + _LengthBtwPO
                                        tmpXY.append(New_Scoord)

                    # Place to cent
                    else:
                        # Place in the middle
                        tmpXY = []
                        for i in [0, -1]:
                            if i == 0:
                                # Calculate
                                # Target_coord
                                tmp1 = self.get_param_KJH4('BND_POLayer')
                                target_coord = tmp1[i][0]['_XY_cent']
                                # Approaching_coord
                                tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                                approaching_coord = tmp2[0][0]['_XY_cent']
                                # Sref coord
                                tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                                Scoord = tmp3[0][0]['_XY_origin']
                                # Cal
                                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                                New_Scoord[0] = New_Scoord[0] - _LengthBtwPO
                                tmpXY.append(New_Scoord)
                            else:
                                # Calculate
                                # Target_coord
                                tmp1 = self.get_param_KJH4('BND_POLayer')
                                target_coord = tmp1[i][0]['_XY_cent']
                                # Approaching_coord
                                tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                                approaching_coord = tmp2[0][0]['_XY_cent']
                                # Sref coord
                                tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                                Scoord = tmp3[0][0]['_XY_origin']
                                # Cal
                                New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
                                New_Scoord[0] = New_Scoord[0] + _LengthBtwPO
                                tmpXY.append(New_Scoord)

                        # Define
                    self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = tmpXY

                elif _PODummy_Placement == 'Up':
                        #Calculate Sref XYcoord
                            #initialized Sref coordinate
                    self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = [[0,0]]

                    tmpXY=[]
                    for i in [0,-1]:
                        if i == 0:
                                #Calculate
                                    #Target_coord
                            tmp1 = self.get_param_KJH4('BND_POLayer')
                            target_coord = tmp1[i][0]['_XY_up']
                                    #Approaching_coord
                            tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                            approaching_coord = tmp2[0][0]['_XY_up']
                                    #Sref coord
                            tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                            Scoord = tmp3[0][0]['_XY_origin']
                                    #Cal
                            New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                            New_Scoord[0] = New_Scoord[0] - _LengthBtwPO
                            tmpXY.append(New_Scoord)
                        else:
                                #Calculate
                                    #Target_coord
                            tmp1 = self.get_param_KJH4('BND_POLayer')
                            target_coord = tmp1[i][0]['_XY_up']
                                    #Approaching_coord
                            tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                            approaching_coord = tmp2[0][0]['_XY_up']
                                    #Sref coord
                            tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                            Scoord = tmp3[0][0]['_XY_origin']
                                    #Cal
                            New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                            New_Scoord[0] = New_Scoord[0] + _LengthBtwPO
                            tmpXY.append(New_Scoord)

                        #Define
                    self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = tmpXY

                elif _PODummy_Placement == 'Dn':

                        #Calculate Sref XYcoord
                            #initialized Sref coordinate
                    self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = [[0,0]]

                    tmpXY=[]
                    for i in [0,-1]:
                        if i == 0:
                                #Calculate
                                    #Target_coord
                            tmp1 = self.get_param_KJH4('BND_POLayer')
                            target_coord = tmp1[i][0]['_XY_down']
                                    #Approaching_coord
                            tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                            approaching_coord = tmp2[0][0]['_XY_down']
                                    #Sref coord
                            tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                            Scoord = tmp3[0][0]['_XY_origin']
                                    #Cal
                            New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                            New_Scoord[0] = New_Scoord[0] - _LengthBtwPO
                            tmpXY.append(New_Scoord)
                        else:
                                #Calculate
                                    #Target_coord
                            tmp1 = self.get_param_KJH4('BND_POLayer')
                            target_coord = tmp1[i][0]['_XY_down']
                                    #Approaching_coord
                            tmp2 = self.get_param_KJH4('BND_PODummyLayer')
                            approaching_coord = tmp2[0][0]['_XY_down']
                                    #Sref coord
                            tmp3 = self.get_param_KJH4('BND_PODummyLayer')
                            Scoord = tmp3[0][0]['_XY_origin']
                                    #Cal
                            New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                            New_Scoord[0] = New_Scoord[0] + _LengthBtwPO
                            tmpXY.append(New_Scoord)

                        #Define
                    self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = tmpXY

                else:
                    pass

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_A_building_block_KJH'
    cellname = 'A14_Mosfet_v1_498'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

#Mosfet

    # PMOS/NMOS
    _MosType                    = 'NMOS',   # 'NMOS'/'PMOS'

    # MOS Up/Dn
    _MosUpDn                    = 'Up',     # 'Up'/'Dn'

    # Physical dimension
    _NumberofGate	            = 3,       # Number
    _ChannelWidth	            = 400,      # Number
    _ChannelLength	            = 30,       # Number
    _GateSpacing		        = None,     # None/Number
    _SDWidth			        = None,     # None/Number
    _XVT				        = 'SLVT',   # 'XVT' ex)SLVT/LVT/RVT/HVT
    _PCCrit				        = True,     # None/True

    #Source_node setting
        #Via setting
    _Source_Via_TF              = True,     # True/False
            # Via close to POpin
    _Source_Via_Close2POpin_TF  = True,     # True/False
        #Comb setting: If Via is True
    _Source_Comb_TF             = True,     # True/False
            #Comb POPinward
    _Source_Comb_POpinward_TF   = False,     # True/False
            #Comb vertical_length
    _Source_Comb_Length         = None,     # None/Number

    #Drain_node_setting
        # Via setting
    _Drain_Via_TF               = True,     # True/False
            # Via close to POpin
    _Drain_Via_Close2POpin_TF   = False,     # True/False
        #Comb setting: If Via is True
    _Drain_Comb_TF              = True,     # True/False
            # Comb POPinward
    _Drain_Comb_POpinward_TF    = True,     # True/False
            # Comb vertical_length
    _Drain_Comb_Length          = None,     # None/Number

    #POLY dummy setting
    _PODummy_TF                 = True,     #TF
        #if _NMOSDummy == True
    _PODummy_Length             = None,     #None/Value
    _PODummy_Placement          = None,     #None/'Up'/'Dn'/

    # XVT setting
        # XVT setting : Exten XVT area if area is min
    _Xvt_MinExten_TF            = True,     # True/False
        # XVT setting : None(Cent), Up, Dn
    _Xvt_Placement              = 'Up',     # None/'Up'/'Dn'/

    # Poly Gate setting
        # Poly Gate setting
    _POGate_Comb_TF             = True,     # True/False
            # Poly Gate setting : vertical length
    _POGate_Comb_length         = 100,     # None/Number
        # Poly Gate Via setting
    _POGate_Via_TF              = True,     # None/'Up'/'Dn'/
            # Poly Gate Via setting :
    _POGate_ViaMxMx             = [0,1]     # Ex) [1,5] -> ViaM1M5


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
    LayoutObj = _Mosfet(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

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
    #Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------




