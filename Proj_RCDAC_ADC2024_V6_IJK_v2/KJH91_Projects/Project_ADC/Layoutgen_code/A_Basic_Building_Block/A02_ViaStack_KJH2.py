from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math

from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM0toM1_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM1toM2_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM2toM3_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM3toM4_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM4toM5_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM5toM6_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM6toM7_KJH2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaM7toM8_KJH2


## ########################################################################################################################################################## Class_HEADER
class _ViaStack_KJH2(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
    
_Layer1 = None, #Bottom metal layer
_Layer2 = None, #Top metal layer
_COX=None,
_COY=None,

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

_Layer1 = None,
_Layer2 = None,
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
            ## Pre-defined
        CenterCoord = [0, 0]

            ## ################################################################################################################### Not implemented condition
        if 0 > _Layer1 or 8 < _Layer2 :
            raise NotImplementedError

        if 0 >= _Layer1 and 0 < _Layer2 :
            ## ################################################################################################################### Gen ViaM0M1
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM0toM1_KJH2._ViaM0toM1_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM0toM1_KJH2._ViaM0toM1_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM0M1'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM0M1']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM0M1']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM0M1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates']=[[0, 0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM0M1','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates'] = tmpXY

        if 1 >= _Layer1 and 1 < _Layer2 :
            ## ################################################################################################################### Gen ViaM1M2
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM1toM2_KJH2._ViaM1toM2_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM1toM2_KJH2._ViaM1toM2_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM1M2']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM1M2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates']=[[0, 0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM1M2','BND_Met2Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates'] = tmpXY

        if 2 >= _Layer1 and 2 < _Layer2 :
            ## ################################################################################################################### Gen ViaM2M3
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM2toM3_KJH2._ViaM2toM3_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM2toM3_KJH2._ViaM2toM3_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM2M3'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM2M3']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM2M3']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM2M3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates']=[[0, 0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM2M3','BND_Met3Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM2M3')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates'] = tmpXY

        if 3 >= _Layer1 and 3 < _Layer2 :
            ## ################################################################################################################### Gen ViaM3M4
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM3toM4_KJH2._ViaM3toM4_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM3toM4_KJH2._ViaM3toM4_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM3M4'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM3M4']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM3M4']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM3M4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates']=[[0, 0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM3M4','BND_Met4Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM3M4')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates'] = tmpXY

        if 4 >= _Layer1 and 4 < _Layer2 :
            ## ################################################################################################################### Gen ViaM4M5
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM4toM5_KJH2._ViaM4toM5_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM4toM5_KJH2._ViaM4toM5_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM4M5'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM4M5']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM4M5']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM4M5']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates']=[[0, 0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM4M5','BND_Met5Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM4M5')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates'] = tmpXY

        if 5 >= _Layer1 and 5 < _Layer2 :
            ## ################################################################################################################### Gen ViaM5M6
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM5toM6_KJH2._ViaM5toM6_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM5toM6_KJH2._ViaM5toM6_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM5M6'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM5M6']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM5M6']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM5M6']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates']=[[0, 0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM5M6','BND_Met6Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM5M6')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates'] = tmpXY

        if 6 >= _Layer1 and 6 < _Layer2 :
            ## ################################################################################################################### Gen ViaM6M7
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM6toM7_KJH2._ViaM6toM7_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM6M7'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM6toM7_KJH2._ViaM6toM7_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM6M7'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM6M7']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM6M7']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM6M7']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates']=[[0, 0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM6M7','BND_Met7Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM6M7')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates'] = tmpXY

        if 7 >= _Layer1 and 7 < _Layer2 :
            ## ################################################################################################################### Gen ViaM7M8
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM7toM8_KJH2._ViaM7toM8_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM7M8'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM7toM8_KJH2._ViaM7toM8_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM7M8'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM7M8']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM7M8']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM7M8']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates']=[[0, 0]]
            
                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM7M8','BND_Met8Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM7M8')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates'] = tmpXY

    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterXmin(self,

_Layer1 = None,
_Layer2 = None,
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
            ## Pre-defined
        CenterCoord = [0, 0]

            ## ################################################################################################################### Not implemented condition
        if 0 > _Layer1 or 8 < _Layer2 :
            raise NotImplementedError

        if 0 >= _Layer1 and 0 < _Layer2 :
            ## ################################################################################################################### Gen ViaM0M1
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM0toM1_KJH2._ViaM0toM1_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM0toM1_KJH2._ViaM0toM1_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM0M1'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM0M1']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM0M1']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates']=[[0, 0]]

                    ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM0M1','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates'] = tmpXY

        if 1 >= _Layer1 and 1 < _Layer2 :
            ## ################################################################################################################### Gen ViaM1M2
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM1toM2_KJH2._ViaM1toM2_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM1toM2_KJH2._ViaM1toM2_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM1M2']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM1M2','BND_Met2Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates'] = tmpXY

        if 2 >= _Layer1 and 2 < _Layer2 :
            ## ################################################################################################################### Gen ViaM2M3
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM2toM3_KJH2._ViaM2toM3_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM2toM3_KJH2._ViaM2toM3_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM2M3'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM2M3']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM2M3']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM2M3','BND_Met3Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM2M3')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates'] = tmpXY

        if 3 >= _Layer1 and 3 < _Layer2 :
            ## ################################################################################################################### Gen ViaM3M4
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM3toM4_KJH2._ViaM3toM4_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM3toM4_KJH2._ViaM3toM4_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM3M4'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM3M4']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM3M4']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM3M4','BND_Met4Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM3M4')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates'] = tmpXY

        if 4 >= _Layer1 and 4 < _Layer2 :
            ## ################################################################################################################### Gen ViaM4M5
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM4toM5_KJH2._ViaM4toM5_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM4toM5_KJH2._ViaM4toM5_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM4M5'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM4M5']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM4M5']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM4M5']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM4M5','BND_Met5Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM4M5')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates'] = tmpXY

        if 5 >= _Layer1 and 5 < _Layer2 :
            ## ################################################################################################################### Gen ViaM5M6
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM5toM6_KJH2._ViaM5toM6_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM5toM6_KJH2._ViaM5toM6_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM5M6'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM5M6']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM5M6']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM5M6']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM5M6','BND_Met6Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM5M6')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates'] = tmpXY

        if 6 >= _Layer1 and 6 < _Layer2 :
            ## ################################################################################################################### Gen ViaM6M7
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM6toM7_KJH2._ViaM6toM7_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM6M7'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM6toM7_KJH2._ViaM6toM7_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM6M7'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM6M7']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM6M7']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM6M7']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM6M7','BND_Met7Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM6M7')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates'] = tmpXY

        if 7 >= _Layer1 and 7 < _Layer2 :
            ## ################################################################################################################### Gen ViaM7M8
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM7toM8_KJH2._ViaM7toM8_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM7M8'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM7toM8_KJH2._ViaM7toM8_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM7M8'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM7M8']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM7M8']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM7M8']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM7M8','BND_Met8Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM7M8')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates'] = tmpXY

            
    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterYmin(self,

_Layer1 = None,
_Layer2 = None,
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
            ## Pre-define
        CenterCoord = [0, 0]

            ## ################################################################################################################### Not implemented condition
        if 0 > _Layer1 or 8 < _Layer2 :
            raise NotImplementedError

        if 0 >= _Layer1 and 0 < _Layer2 :
            ## ################################################################################################################### Gen ViaM0M1
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM0toM1_KJH2._ViaM0toM1_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM0toM1_KJH2._ViaM0toM1_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM0M1'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM0M1']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM0M1']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM0M1','BND_Met1Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM0M1')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM0M1']['_XYCoordinates'] = tmpXY

        if 1 >= _Layer1 and 1 < _Layer2 :
            ## ################################################################################################################### Gen ViaM1M2
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM1toM2_KJH2._ViaM1toM2_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM1toM2_KJH2._ViaM1toM2_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM1M2']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM1M2','BND_Met2Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM1M2')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM1M2']['_XYCoordinates'] = tmpXY

        if 2 >= _Layer1 and 2 < _Layer2 :
            ## ################################################################################################################### Gen ViaM2M3
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM2toM3_KJH2._ViaM2toM3_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM2toM3_KJH2._ViaM2toM3_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM2M3'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM2M3']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM2M3']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM2M3','BND_Met3Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM2M3')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM2M3']['_XYCoordinates'] = tmpXY

        if 3 >= _Layer1 and 3 < _Layer2 :
            ## ################################################################################################################### Gen ViaM3M4
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM3toM4_KJH2._ViaM3toM4_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM3toM4_KJH2._ViaM3toM4_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM3M4'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM3M4']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM3M4']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM3M4','BND_Met4Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM3M4')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM3M4']['_XYCoordinates'] = tmpXY

        if 4 >= _Layer1 and 4 < _Layer2 :
            ## ################################################################################################################### Gen ViaM4M5
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM4toM5_KJH2._ViaM4toM5_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM4toM5_KJH2._ViaM4toM5_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM4M5'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM4M5']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM4M5']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM4M5']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM4M5','BND_Met5Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM4M5')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM4M5']['_XYCoordinates'] = tmpXY

        if 5 >= _Layer1 and 5 < _Layer2 :
            ## ################################################################################################################### Gen ViaM5M6
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM5toM6_KJH2._ViaM5toM6_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM5toM6_KJH2._ViaM5toM6_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM5M6'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM5M6']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM5M6']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM5M6']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM5M6','BND_Met6Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM5M6')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM5M6']['_XYCoordinates'] = tmpXY

        if 6 >= _Layer1 and 6 < _Layer2 :
            ## ################################################################################################################### Gen ViaM6M7
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM6toM7_KJH2._ViaM6toM7_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM6M7'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM6toM7_KJH2._ViaM6toM7_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM6M7'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM6M7']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM6M7']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM6M7']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates']=[[0, 0]]

                  ## Get_Scoord_v4.
                        ## Calculate Sref XYcoord
            tmpXY = []
                            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates'] = [[0, 0]]
                            ## Calculate
                                ## Target_coord: _XY_type1
            target_coord = CenterCoord
                                ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM6M7','BND_Met7Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
                                ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM6M7')
            Scoord = tmp3[0][0]['_XY_origin']
                                ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
                        ## Define Coordinates
            self._DesignParameter['SRF_ViaM6M7']['_XYCoordinates'] = tmpXY

        if 7 >= _Layer1 and 7 < _Layer2 :
            ## ################################################################################################################### Gen ViaM7M8
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A02_ViaM7toM8_KJH2._ViaM7toM8_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_COX']  = _COX
            _Caculation_Parameters['_COY']  = _COY

            #Generate Sref
            self._DesignParameter['SRF_ViaM7M8'] = self._SrefElementDeclaration(_DesignObj=A02_ViaM7toM8_KJH2._ViaM7toM8_KJH( _DesignParameter=None, _Name='{}:SRF_ViaM7M8'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['SRF_ViaM7M8']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['SRF_ViaM7M8']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['SRF_ViaM7M8']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates']=[[0, 0]]

            ## Get_Scoord_v4.
            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates'] = [[0, 0]]
            ## Calculate
            ## Target_coord: _XY_type1
            target_coord = CenterCoord
            ## Approaching_coord: _XY_type2
            tmp2 = self.get_param_KJH4('SRF_ViaM7M8', 'BND_Met8Layer')
            approaching_coord = tmp2[0][0][0]['_XY_cent']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_ViaM7M8')
            Scoord = tmp3[0][0]['_XY_origin']
            ## Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define Coordinates
            self._DesignParameter['SRF_ViaM7M8']['_XYCoordinates'] = tmpXY


            
## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_A_building_block_KJH'
    cellname = 'A18_ViaStack_KJH_95'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_Layer1 = 3,
_Layer2 = 4,
_COX    = 7,
_COY    = 4,

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
    LayoutObj = _ViaStack_KJH2(_DesignParameter=None, _Name=cellname)
    
    #LayoutObj._CalculateDesignParameter(**InputParams)
    #LayoutObj._CalculateDesignParameterXmin(**InputParams)
    LayoutObj._CalculateDesignParameterYmin(**InputParams)

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




