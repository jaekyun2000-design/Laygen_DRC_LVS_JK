from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math
#from SthPack import CoordCalc


from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2

## ########################################################################################################################################################## Class_HEADER
class _NmosWithDummy_KJH3(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

#NMOS
_NMOSNumberofGate	= None, #number
_NMOSChannelWidth	= None, #number
_NMOSChannellength	= None, #number
_GateSpacing		= None, #None/number
_SDWidth			= None, #None/number
_XVT				= None, #'XVT' ex)SLVT LVT RVT HVT
_PCCrit				= None, #None/True

#Source_node_ViaM1M2
_Source_Via_TF = False,  #True/False

#Drain_node_ViaM1M2
_Drain_Via_TF = False,   #True/False

#POLY dummy setting
_NMOSDummy = False,  #TF
    #if _PMOSDummy == True
_NMOSDummy_length = None, #None/number
_NMOSDummy_placement = None, #None/'Up'/'Dn'/

# XVT setting
# XVT setting : Exten XVT area if min area
_NMOSXvt_Minexten=True,  # True/False
# XVT setting : None(Cent), Up, Dn
_NMOSXvt_placement=None,  # None/'Up'/'Dn'/

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

                                  #NMOS
                                  _NMOSNumberofGate	= None,
                                  _NMOSChannelWidth	= None,
                                  _NMOSChannellength	= None,
                                  _GateSpacing		= None,
                                  _SDWidth			= None,
                                  _XVT				= None,
                                  _PCCrit				= None,

                                  #Source_node_ViaM1M2
                                  _Source_Via_TF = None,

                                  #Drain_node_ViaM1M2
                                  _Drain_Via_TF = None,

                                  #POLY dummy setting
                                  _NMOSDummy = None,  #TF
                                  #if _PMOSDummy == True
                                  _NMOSDummy_length = None,  #None/Value
                                  _NMOSDummy_placement = None,  #None/'Up'/'Dn'/

                                  # XVT setting
                                  # XVT setting : Exten XVT area if min area
                                  _NMOSXvt_Minexten=True,  # True/False
                                  # XVT setting : None(Cent), Up, Dn
                                  _NMOSXvt_placement=None,  # None/'Up'/'Dn'/
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

            ## ################################################################################################################### POLY_Layer
        #Define Boundary_element
        self._DesignParameter['BND_POLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer']['_YWidth'] = _NMOSChannelWidth + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_NMOSChannellength)

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_POLayer']['_XWidth'] = _NMOSChannellength

        #Define Boundary_element _XYCoordinates
            #Define _LengthNMOSBtwPO
        _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj.DRCPolyMinSpace(_Width=_NMOSChannelWidth, _ParallelLength=_NMOSChannellength)) + _NMOSChannellength
                #Applying GateSpacing
        if _GateSpacing != None:
            if (_GateSpacing + _NMOSChannellength) < _LengthNMOSBtwPO:
                raise NotImplementedError(f"Invalid input arg: GateSpacing({_GateSpacing})")
            else:
                _LengthNMOSBtwPO = _GateSpacing + _NMOSChannellength
        elif _GateSpacing == None:
            _GateSpacing = _DRCObj._PolygateMinSpace

            #Calculate Sref XYcoord
                #initialize coordinate
        self._DesignParameter['BND_POLayer']['_XYCoordinates'] = [[0,0]]
        tmpXY=[[0,0]]
        for i in range(0,_NMOSNumberofGate-1):
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
            New_Scoord[0] = New_Scoord[0] + _LengthNMOSBtwPO
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['BND_POLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### POLY_Dummy_Layer
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
        if _NMOSDummy == False:
            self._DesignParameter['BND_PODummyLayer']['_YWidth'] = 0
        elif _NMOSDummy:
            self._DesignParameter['BND_PODummyLayer']['_YWidth'] = _NMOSChannelWidth + 2 * a

        #Define Boundary_element _XWidth
        if _NMOSDummy == False:
            self._DesignParameter['BND_PODummyLayer']['_XWidth'] = 0
        elif _NMOSDummy:
            self._DesignParameter['BND_PODummyLayer']['_XWidth'] = _NMOSChannellength

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
                New_Scoord[0] = New_Scoord[0] - _LengthNMOSBtwPO
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
                New_Scoord[0] = New_Scoord[0] + _LengthNMOSBtwPO
                tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### DIFF(OD/RX)_Dummy_Layer
        #Define Boundary_element
        self._DesignParameter['BND_ODLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayer']['_YWidth'] = _NMOSChannelWidth

        #Define Boundary_element _XWidth
        XWidth_OD = _LengthNMOSBtwPO * _NMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
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

            ## ################################################################################################################### METAL1_Layer
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
        _LengthNMOSBtwMet1 = _LengthNMOSBtwPO
            #Cal coord
        tmpXYs = []
        for i in range(0, _NMOSNumberofGate + 1):
            XY = [_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                  _XYCoordinateOfNMOS[0][1]]
            tmpXYs.append(XY)
            #Define coord
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = tmpXYs

            ## ################################################################################################################### CONT_Layer
        #Define Boundary_element
        self._DesignParameter['BND_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
                #Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        target_coord = tmp1[0][0]['_XY_cent']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_COLayer')
        approaching_coord = tmp2[0][0]['_XY_cent']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_COLayer')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

            #Get _XYCoordinateOfNMOS
        _XYCoordinateOfNMOS = [New_Scoord]
        
            #CONT XNum/YNum Calculation
        _XNumberOfCOInNMOS = _NMOSNumberofGate + 1
        _YNumberOfCOInNMOS = _tmpCOYNum
                #Check the number of CO On NMOS TR
        if _XNumberOfCOInNMOS == 0 or _YNumberOfCOInNMOS == 0:
            print('************************* Error occurred in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
                
            #Define _LengthNMOSBtwCO
        _LengthNMOSBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth
                
            #Cal coord
        tmpXYs = []
        for i in range(0, _XNumberOfCOInNMOS):
            for j in range(0, _YNumberOfCOInNMOS):
                XY = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                      _XYCoordinateOfNMOS[0][1] - (_YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
                tmpXYs.append(XY)
                
            #Define coord
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmpXYs

            ## ################################################################################################################### XVT_Layer
        try:
            if (DesignParameters._Technology == '028nm') and _XVT in ('SLVT', 'LVT', 'RVT', 'HVT'):
                _XVTLayer = 'BND_' + _XVT + 'Layer'
                _XVTLayerMappingName = _XVT
                
            elif DesignParameters._Technology in ('028nm'):
                raise NotImplementedError(f"Invalid '_XVT' argument({_XVT}) for {DesignParameters._Technology}")
                
            else:
                raise NotImplementedError(f"Not Yet Implemented in other technology : {DesignParameters._Technology}")

            if _XVTLayer != None:

                ######################## Nominal
                #Define Boundary_element
                self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping[_XVTLayerMappingName][0],
                                                                                        _Datatype=DesignParameters._LayerMapping[_XVTLayerMappingName][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

                if _NMOSXvt_Minexten == True:
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

                #Define coord
                self._DesignParameter[_XVTLayer]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                        #Target_coord
                tmp1 = self.get_param_KJH4('BND_ODLayer')
                if _NMOSXvt_placement == None:
                    target_coord = tmp1[0][0]['_XY_cent']
                elif _NMOSXvt_placement == 'Up':
                    target_coord = tmp1[0][0]['_XY_up']
                elif _NMOSXvt_placement == 'Dn':
                    target_coord = tmp1[0][0]['_XY_down']
                else:
                    target_coord = tmp1[0][0]['_XY_cent']

                        #Approaching_coord
                tmp2 = self.get_param_KJH4(_XVTLayer)
                if _NMOSXvt_placement == None:
                    approaching_coord = tmp2[0][0]['_XY_cent']
                elif _NMOSXvt_placement == 'Up':
                    approaching_coord = tmp2[0][0]['_XY_up']
                elif _NMOSXvt_placement == 'Dn':
                    approaching_coord = tmp2[0][0]['_XY_down']
                else:
                    approaching_coord = tmp2[0][0]['_XY_cent']

                        #Sref coord
                tmp3 = self.get_param_KJH4(_XVTLayer)
                Scoord = tmp3[0][0]['_XY_origin']
                        #Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

                if _NMOSXvt_placement == None:
                    New_Scoord[0] = New_Scoord[0]
                    New_Scoord[1] = New_Scoord[1]
                elif _NMOSXvt_placement == 'Up':
                    New_Scoord[0] = New_Scoord[0]
                    New_Scoord[1] = New_Scoord[1] + _DRCObj._XvtMinEnclosureOfODY
                elif _NMOSXvt_placement == 'Dn':
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

            ## ################################################################################################################### PCCrit_Layer
        #If pccrit
        if DesignParameters._Technology == '028nm' and _PCCrit != False:
            
            #Make PCCrit if gatelentgh is either 30 or 34
            if self._DesignParameter['BND_POLayer']['_XWidth'] in (30, 34):
            
                #Define Boundary_element
                self._DesignParameter['BND_PCCRITLayer'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

                #Define Boundary_element _YWidth
                self._DesignParameter['BND_PCCRITLayer']['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension

                #Define Boundary_element _XWidth
                self._DesignParameter['BND_PCCRITLayer']['_XWidth'] = _LengthNMOSBtwMet1 * _NMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension

                self._DesignParameter['BND_PCCRITLayer']['_XYCoordinates'] =[[0,0]]
                #Define coord
                    #Calculate Sref XYcoord
                            #Target_coord
                tmp1 = self.get_param_KJH4('BND_ODLayer')
                target_coord = tmp1[0][0]['_XY_cent']
                            #Approaching_coord
                tmp2 = self.get_param_KJH4('BND_PCCRITLayer')
                approaching_coord = tmp2[0][0]['_XY_cent']
                            #Sref coord
                tmp3 = self.get_param_KJH4('BND_PCCRITLayer')
                Scoord = tmp3[0][0]['_XY_origin']
                            #Cal
                New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)

                self._DesignParameter['BND_PCCRITLayer']['_XYCoordinates'] = [New_Scoord]
            
            
                if self._DesignParameter['BND_POLayer']['_XWidth'] == 30 :
                    if _GateSpacing not in (96, 222, 100, 230) :
                        raise NotImplementedError
                elif self._DesignParameter['BND_POLayer']['_XWidth'] == 34 :
                    if _GateSpacing not in (96, 226) :
                        raise NotImplementedError
                        
            #Do not make PCcrit if gatelenght is not either 30 or 34
            else:
                pass

        '''
            ## ################################################################################################################### Not generated Layer but used in the Pindrawing: _XYCoordinateNMOSSupplyRouting/ _XYCoordinateNMOSOutputRouting/ _XYCoordinateNMOSGateRouting
                ## ##################################################################################################### _XYCoordinateNMOSSupplyRouting = M1 source coordinates
        #Define Boundary_element
        self._DesignParameter['_XYCoordinateNMOSSupplyRouting'] = dict(
                                                                        _DesignParametertype=7,
                                                                        _XYCoordinates=[ ],
                                                                       )
                                                                                       
        tmpXYs = []
        if (_NMOSNumberofGate % 2) == 0:
            for i in range(0, _NMOSNumberofGate // 2 + 1):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        else:
            for i in range(0, (_NMOSNumberofGate - 1) // 2 + 1):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5) * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        self._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'] = tmpXYs
        
                ## ##################################################################################################### _XYCoordinateNMOSOutputRouting = M1 drain coordinate
        #Define Boundary_element
        self._DesignParameter['_XYCoordinateNMOSOutputRouting'] = dict(
                                                                        _DesignParametertype=7,
                                                                        _XYCoordinates=[ ],
                                                                       )
                                                                                       
        tmpXYs = []
        if (_NMOSNumberofGate % 2) == 0:
            for i in range(0, _NMOSNumberofGate // 2):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        else:
            for i in range(0, (_NMOSNumberofGate - 1) // 2 + 1):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5) * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        self._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'] = tmpXYs
        
                ## ##################################################################################################### _XYCoordinateNMOSGateRouting = gate poly coordinate
       #Define Boundary_element
        self._DesignParameter['_XYCoordinateNMOSGateRouting'] = dict(
                                                                        _DesignParametertype=7,
                                                                        _XYCoordinates=[ ],
                                                                       )

        tmpXYs = []
        for i in range(0, _NMOSNumberofGate):
            tmpXYs.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                           _XYCoordinateOfNMOS[0][1]])
        self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'] = tmpXYs
        '''


            ## ################################################################################################################### _METAL1PINDrawing
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

            ## ################################################################################################################### _ODLayerPINDrawing
        #Define Boundary_element
        self._DesignParameter['BND_ODLayerPINDrawing'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['BND_ODLayer']['_YWidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        tmp2 = self.get_param_KJH4('BND_POLayer')

        self._DesignParameter['BND_ODLayerPINDrawing']['_XWidth'] = abs( tmp1[0][0]['_XY_right'][0] - tmp2[-1][0]['_XY_right'][0] )

        #Define coord
        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ODLayerPINDrawing']['_XYCoordinates'] = [[0,0]]

            #Calculate1
                #Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ODLayerPINDrawing')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ODLayerPINDrawing')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            
            #Calculate2
                #Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer')
        target_coord = tmp1[0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ODLayerPINDrawing')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ODLayerPINDrawing')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)		

            #Define
        self._DesignParameter['BND_ODLayerPINDrawing']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### _POLayerPINDrawing
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

        if _NMOSNumberofGate == 1:
            self._DesignParameter['BND_POLayerPINDrawing']['_XYCoordinates'] = tmpxy + tmpxy1
        else:
            self._DesignParameter['BND_POLayerPINDrawing']['_XYCoordinates'] = tmpxy

            ## ################################################################################################################### _Met1Layer_Source
        #Define Boundary_element
        self._DesignParameter['BND_Met1Layer_Source'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_Source']['_YWidth'] = self._DesignParameter['BND_Met1Layer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_Source']['_XWidth'] = self._DesignParameter['BND_Met1Layer']['_XWidth']

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

        self._DesignParameter['BND_Met1Layer_Source']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### _Met1Layer_Drain
        #Define Boundary_element
        self._DesignParameter['BND_Met1Layer_Drain'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_Drain']['_YWidth'] = self._DesignParameter['BND_Met1Layer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1Layer_Drain']['_XWidth'] = self._DesignParameter['BND_Met1Layer']['_XWidth']

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

        self._DesignParameter['BND_Met1Layer_Drain']['_XYCoordinates'] = tmpXY

        if _Source_Via_TF == True:
            ## ################################################################################################################### _Source_ViaM1M2
            #Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] 	= 1
            _Caculation_Parameters['_Layer2'] 	= 2
            _Caculation_Parameters['_COX'] 		= None
            _Caculation_Parameters['_COY'] 		= None

            #Sref ViaX declaration
            self._DesignParameter['SRF_Source_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Source_ViaM1M2'.format(_Name)))[0]

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
                    tmp1 = self.get_param_KJH4('BND_Met1Layer')
                    target_coord = tmp1[i][0]['_XY_up']
                            #Approaching_coord
                    tmp2 = self.get_param_KJH4('SRF_Source_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
                    approaching_coord = tmp2[0][0][0][0]['_XY_up']
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

        if _Drain_Via_TF == True:
            ## ################################################################################################################### _Drain_ViaM1M2
            #Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] 	= 1
            _Caculation_Parameters['_Layer2'] 	= 2
            _Caculation_Parameters['_COX'] 		= None
            _Caculation_Parameters['_COY'] 		= None

            #Sref ViaX declaration
            self._DesignParameter['SRF_Drain_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_Drain_ViaM1M2'.format(_Name)))[0]

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
                    tmp1 = self.get_param_KJH4('BND_Met1Layer')
                    target_coord = tmp1[i][0]['_XY_up']
                            #Approaching_coord
                    tmp2 = self.get_param_KJH4('SRF_Drain_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
                    approaching_coord = tmp2[0][0][0][0]['_XY_up']
                            #Sref coord
                    tmp3 = self.get_param_KJH4('SRF_Drain_ViaM1M2')
                    Scoord = tmp3[0][0]['_XY_origin']
                            #Cal
                    New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
                    New_Scoord[1] = New_Scoord[1] -64
                    tmpXY.append(New_Scoord)

                    flag = +1

            self._DesignParameter['SRF_Drain_ViaM1M2']['_XYCoordinates'] = tmpXY

        if _NMOSDummy == True:
            ## ################################################################################################################### POLY_Dummy_Layer2:manual setting

                ## ##################################################################################################### POLY_Dummy_Layer2:manual setting:dummy_length
            if _NMOSDummy_length == None:

                # Poly minimum area constraint
                tmp  = self.get_param_KJH4('BND_PODummyLayer')
                area = np.array(tmp[0][0]['_Ywidth']) * np.array(tmp[0][0]['_Xwidth'])
                if area < 11000:
                    self._DesignParameter['BND_PODummyLayer']['_YWidth'] = np.ceil(11000/ np.array(tmp[0][0]['_Xwidth']))
                    flag = 1
                else:
                    flag = 0
            else:
                self._DesignParameter['BND_PODummyLayer']['_YWidth'] = _NMOSDummy_length

                ## ##################################################################################################### POLY_Dummy_Layer2:manual setting:dummy_placement
            if _NMOSDummy_placement == None:

                ## Poly minimum area constraint: Place to 'Up'
                if flag ==1:
                    self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = [[0, 0]]

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
                            New_Scoord[0] = New_Scoord[0] - _LengthNMOSBtwPO
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
                            New_Scoord[0] = New_Scoord[0] + _LengthNMOSBtwPO
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
                            New_Scoord[0] = New_Scoord[0] - _LengthNMOSBtwPO
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
                            New_Scoord[0] = New_Scoord[0] + _LengthNMOSBtwPO
                            tmpXY.append(New_Scoord)

                    # Define
                self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = tmpXY

            elif _NMOSDummy_placement == 'Up':
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
                        New_Scoord[0] = New_Scoord[0] - _LengthNMOSBtwPO
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
                        New_Scoord[0] = New_Scoord[0] + _LengthNMOSBtwPO
                        tmpXY.append(New_Scoord)

                    #Define
                self._DesignParameter['BND_PODummyLayer']['_XYCoordinates'] = tmpXY

            elif _NMOSDummy_placement == 'Dn':

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
                        New_Scoord[0] = New_Scoord[0] - _LengthNMOSBtwPO
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
                        New_Scoord[0] = New_Scoord[0] + _LengthNMOSBtwPO
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
    cellname = 'A03_NmosWithDummy_KJH2_96'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(


#NMOS
_NMOSNumberofGate	= 15,
_NMOSChannelWidth	= 300,
_NMOSChannellength	= 30,
_GateSpacing		= None,
_SDWidth			= None,
_XVT				= 'SLVT',
_PCCrit				= None,

#Source_node_ViaM1M2
_Source_Via_TF = True,

#Drain_node_ViaM1M2
_Drain_Via_TF = True,

#POLY dummy setting
_NMOSDummy = True,  #TF
    #if _NMOSDummy == True
_NMOSDummy_length = None, #None/Value
_NMOSDummy_placement = None, #None/'Up'/'Dn'/

#XVT setting
    #XVT setting : Exten XVT area if min area
_NMOSXvt_Minexten = True, # True/False
    #XVT setting : None(Cent), Up, Dn
_NMOSXvt_placement = None, #None/'Up'/'Dn'/

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
    LayoutObj = _NmosWithDummy_KJH3(_DesignParameter=None, _Name=cellname)
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




