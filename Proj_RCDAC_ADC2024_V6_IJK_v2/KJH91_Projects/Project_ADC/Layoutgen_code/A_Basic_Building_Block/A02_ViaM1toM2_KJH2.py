from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math
#from SthPack import CoordCalc

## ########################################################################################################################################################## Class_HEADER
class _ViaM1toM2_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_COX=None,
_COY=None

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

_COX=None,
_COY=None

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

        ##  Pre-defined: Coordination
        _XYOrigin = [[0, 0]]

        ##  NotImplemented condition
        if _COX == 0 or _COY == 0:
            print(('**** Error occured in {} Design Parameter Calculation****'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

        ## CONT Layer
            # Define Boundary_element
        self._DesignParameter['BND_COLayer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['VIA12'][0],
        _Datatype=DesignParameters._LayerMapping['VIA12'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

            # Define Boundary_element _YWidth
        self._DesignParameter['BND_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth

            # Define Boundary_element _XWidth
        self._DesignParameter['BND_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth

            # Define _LengthViaPoly2Met1BtwCO
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element Coordinates
                # Initialized coordinate
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = _XYOrigin
        tmp = []
        for i in range(0, _COY):
            for j in range(0, _COX):
                if j == 0:
                    if i == 0:
                        _xycoordinatetmp = [0,0]
                    else:
                        tmp1 = self.get_param_KJH4('BND_COLayer')
                        refcoord = tmp1[-1-1*(_COX-1)][0]['_XY_down_left']
                        _xycoordinatetmp = np.array(refcoord) - np.array([0,_DistanceViaCent2Cent])
                else:
                    tmp1 = self.get_param_KJH4('BND_COLayer')
                    refcoord = tmp1[-1][0]['_XY_down_left']
                    _xycoordinatetmp = np.array(refcoord) + np.array([_DistanceViaCent2Cent,0])
                tmp.append(_xycoordinatetmp)
                self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp
                # Define coordinates
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp

        ##  METAL1 Layer
            # Define Boundary_element
        self._DesignParameter['BND_Met1Layer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
            # Define _LengthViaPoly2Met1BtwCO: Co center to center distance
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        tmpww = tmp[0][0]['_XY_up']
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_Met1Layer']['_YWidth'] = _Via_YWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

            # Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_Met1Layer']['_XWidth'] = _Via_XWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

            # Define Boundary_element Coordinates
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Met1Layer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        New_Scoord[1] = New_Scoord[1] + max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = tmpXY



        ##  METAL2 Layer
            # Define Boundary_element
        self._DesignParameter['BND_Met2Layer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
            # Define _LengthViaPoly2Met1BtwCO: Co center to center distance
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_Met2Layer']['_YWidth'] = _Via_YWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

            # Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_Met2Layer']['_XWidth'] = _Via_XWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

            # Define Boundary_element Coordinates
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Met2Layer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Met2Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        New_Scoord[1] = New_Scoord[1] + max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')












    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterXmin(self,

_COX=None,
_COY=None

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

        ##  Pre-defined: Coordination
        _XYOrigin = [[0, 0]]

        ##  NotImplemented condition
        if _COX == 0 or _COY == 0:
            print(('**** Error occured in {} Design Parameter Calculation****'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

        ## CONT Layer
            # Define Boundary_element
        self._DesignParameter['BND_COLayer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['VIA12'][0],
        _Datatype=DesignParameters._LayerMapping['VIA12'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

            # Define Boundary_element _YWidth
        self._DesignParameter['BND_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth

            # Define Boundary_element _XWidth
        self._DesignParameter['BND_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth

            # Define _LengthViaPoly2Met1BtwCO
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element Coordinates
                # Initialized coordinate
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = _XYOrigin
        tmp = []
        for i in range(0, _COY):
            for j in range(0, _COX):
                if j == 0:
                    if i == 0:
                        _xycoordinatetmp = [0,0]
                    else:
                        tmp1 = self.get_param_KJH4('BND_COLayer')
                        refcoord = tmp1[-1-1*(_COX-1)][0]['_XY_down_left']
                        _xycoordinatetmp = np.array(refcoord) - np.array([0,_DistanceViaCent2Cent])
                else:
                    tmp1 = self.get_param_KJH4('BND_COLayer')
                    refcoord = tmp1[-1][0]['_XY_down_left']
                    _xycoordinatetmp = np.array(refcoord) + np.array([_DistanceViaCent2Cent,0])
                tmp.append(_xycoordinatetmp)
                self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp
                # Define coordinates
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp

        ##  METAL1 Layer
            # Define Boundary_element
        self._DesignParameter['BND_Met1Layer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
            # Define _LengthViaPoly2Met1BtwCO: Co center to center distance
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        tmpww = tmp[0][0]['_XY_up']
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_Met1Layer']['_YWidth'] = _Via_YWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

            # Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_Met1Layer']['_XWidth'] = _Via_XWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

            # Define Boundary_element Coordinates
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Met1Layer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        New_Scoord[1] = New_Scoord[1] + max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = tmpXY



        ##  METAL2 Layer
            # Define Boundary_element
        self._DesignParameter['BND_Met2Layer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
            # Define _LengthViaPoly2Met1BtwCO: Co center to center distance
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_Met2Layer']['_YWidth'] = _Via_YWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

            # Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_Met2Layer']['_XWidth'] = _Via_XWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

            # Define Boundary_element Coordinates
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Met2Layer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Met2Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        New_Scoord[1] = New_Scoord[1] + max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')












    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterYmin(self,

_COX=None,
_COY=None

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

        ##  Pre-defined: Coordination
        _XYOrigin = [[0, 0]]

        ##  NotImplemented condition
        if _COX == 0 or _COY == 0:
            print(('**** Error occured in {} Design Parameter Calculation****'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

        ## CONT Layer
            # Define Boundary_element
        self._DesignParameter['BND_COLayer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['VIA12'][0],
        _Datatype=DesignParameters._LayerMapping['VIA12'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

            # Define Boundary_element _YWidth
        self._DesignParameter['BND_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth

            # Define Boundary_element _XWidth
        self._DesignParameter['BND_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth

            # Define _LengthViaPoly2Met1BtwCO
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element Coordinates
                # Initialized coordinate
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = _XYOrigin
        tmp = []
        for i in range(0, _COY):
            for j in range(0, _COX):
                if j == 0:
                    if i == 0:
                        _xycoordinatetmp = [0,0]
                    else:
                        tmp1 = self.get_param_KJH4('BND_COLayer')
                        refcoord = tmp1[-1-1*(_COX-1)][0]['_XY_down_left']
                        _xycoordinatetmp = np.array(refcoord) - np.array([0,_DistanceViaCent2Cent])
                else:
                    tmp1 = self.get_param_KJH4('BND_COLayer')
                    refcoord = tmp1[-1][0]['_XY_down_left']
                    _xycoordinatetmp = np.array(refcoord) + np.array([_DistanceViaCent2Cent,0])
                tmp.append(_xycoordinatetmp)
                self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp
                # Define coordinates
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp

        ##  METAL1 Layer
            # Define Boundary_element
        self._DesignParameter['BND_Met1Layer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
            # Define _LengthViaPoly2Met1BtwCO: Co center to center distance
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        tmpww = tmp[0][0]['_XY_up']
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_Met1Layer']['_YWidth'] = _Via_YWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

            # Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_Met1Layer']['_XWidth'] = _Via_XWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

            # Define Boundary_element Coordinates
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Met1Layer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        New_Scoord[1] = New_Scoord[1] + max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = tmpXY



        ##  METAL2 Layer
            # Define Boundary_element
        self._DesignParameter['BND_Met2Layer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
            # Define _LengthViaPoly2Met1BtwCO: Co center to center distance
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_Met2Layer']['_YWidth'] = _Via_YWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

            # Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_Met2Layer']['_XWidth'] = _Via_XWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

            # Define Boundary_element Coordinates
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Met2Layer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Met2Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        New_Scoord[1] = New_Scoord[1] + max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')










    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterXYsame(self,

_COX=None,
_COY=None,

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

        ##  Pre-defined: Coordination
        _XYOrigin = [[0, 0]]

        ##  NotImplemented condition
        if _COX == 0 or _COY == 0:
            print(('**** Error occured in {} Design Parameter Calculation****'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

        ## CONT Layer
            # Define Boundary_element
        self._DesignParameter['BND_COLayer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['VIA12'][0],
        _Datatype=DesignParameters._LayerMapping['VIA12'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

            # Define Boundary_element _YWidth
        self._DesignParameter['BND_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth

            # Define Boundary_element _XWidth
        self._DesignParameter['BND_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth

            # Define _LengthViaPoly2Met1BtwCO
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element Coordinates
                # Initialized coordinate
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = _XYOrigin
        tmp = []
        for i in range(0, _COY):
            for j in range(0, _COX):
                if j == 0:
                    if i == 0:
                        _xycoordinatetmp = [0,0]
                    else:
                        tmp1 = self.get_param_KJH4('BND_COLayer')
                        refcoord = tmp1[-1-1*(_COX-1)][0]['_XY_down_left']
                        _xycoordinatetmp = np.array(refcoord) - np.array([0,_DistanceViaCent2Cent])
                else:
                    tmp1 = self.get_param_KJH4('BND_COLayer')
                    refcoord = tmp1[-1][0]['_XY_down_left']
                    _xycoordinatetmp = np.array(refcoord) + np.array([_DistanceViaCent2Cent,0])
                tmp.append(_xycoordinatetmp)
                self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp
                # Define coordinates
        self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp

        ##  METAL1 Layer
            # Define Boundary_element
        self._DesignParameter['BND_Met1Layer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
            # Define _LengthViaPoly2Met1BtwCO: Co center to center distance
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        tmpww = tmp[0][0]['_XY_up']
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_Met1Layer']['_YWidth'] = _Via_YWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

            # Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_Met1Layer']['_XWidth'] = _Via_XWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

            # Define Boundary_element Coordinates
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Met1Layer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        New_Scoord[1] = New_Scoord[1] + max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = tmpXY



        ##  METAL2 Layer
            # Define Boundary_element
        self._DesignParameter['BND_Met2Layer'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
            # Define _LengthViaPoly2Met1BtwCO: Co center to center distance
        _DistanceViaCent2Cent = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_COX, NumOfVIAxY=_COY)

            # Define Boundary_element _YWidth
        tmp = self.get_param_KJH4('BND_COLayer')
        _Via_YWidth = abs(tmp[0][0]['_XY_up'][1] - tmp[-1][0]['_XY_down'][1])
        self._DesignParameter['BND_Met2Layer']['_YWidth'] = _Via_YWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

            # Define Boundary_element _XWidth
        _Via_XWidth = abs(tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0])
        self._DesignParameter['BND_Met2Layer']['_XWidth'] = _Via_XWidth + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

            # Define Boundary_element Coordinates
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = [[0, 0]]

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('BND_COLayer')
        target_coord = tmp1[0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Met2Layer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Met2Layer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] - max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        New_Scoord[1] = New_Scoord[1] + max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['BND_Met2Layer']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')














## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_A_building_block_KJH'
    cellname = 'A11_ViaM1toM2_KJH2_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_COX = 2 ,
_COY = 4 ,

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
    LayoutObj = _ViaM1toM2_KJH(_DesignParameter=None, _Name=cellname)
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




