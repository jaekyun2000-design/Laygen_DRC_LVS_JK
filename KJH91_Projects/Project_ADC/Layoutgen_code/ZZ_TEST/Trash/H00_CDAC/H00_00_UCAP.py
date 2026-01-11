## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import math
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2

############################################################################################################################################################ Class_HEADER
class _UCAP(StickDiagram_KJH1._StickDiagram_KJH):

    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
                                        _MetalType=None,
                                        _MetalWidth=None,
                                        _MetalLength=None,
    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,
                                  # # Unit Capacitor (0.5fF)
                                  _MetalType= None,
                                  _MetalWidth=None,
                                  _MetalLength= None,
                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ############################################################################################################################################################ CALCULATION START
        print( '#########################################################################################################')
        print( '                                      Calculation Start                                                  ')
        print( '#########################################################################################################')

        ## Boundary_element Generation
             ## TOP LEFT Metal1 (Part of Top(left) plate at Unitcap)
        self._DesignParameter['BND_UCAP_TLEFT_VTC_M'+str(_MetalType)] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType)][0],
        _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType)][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_UCAP_TLEFT_VTC_M'+ str(_MetalType)]['_YWidth'] = _MetalLength
                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_UCAP_TLEFT_VTC_M'+ str(_MetalType)]['_XWidth'] = _MetalWidth
                ## Define Boundary_element _XYCoordinates
        _CapSpacing = 50
        _ExtraLength = 228
        self._DesignParameter['BND_UCAP_TLEFT_VTC_M'+ str(_MetalType)]['_XYCoordinates'] = [[0 , 0]]

            ## TOP LEFT Metal2 for generating via(want to generate via only at top plate)
        self._DesignParameter['BND_UCAP_TLEFT_VTC_M' + str(_MetalType + 1)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType + 1)][0],
            _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType + 1)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_UCAP_TLEFT_VTC_M' + str(_MetalType + 1)]['_YWidth'] = _MetalLength
                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_UCAP_TLEFT_VTC_M' + str(_MetalType + 1)]['_XWidth'] = _MetalWidth
                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_UCAP_TLEFT_VTC_M' + str(_MetalType + 1)]['_XYCoordinates'] = [[0, 0]]

             ## Bottom plate Metal
        self._DesignParameter['BND_UCAP_Bottom_VTC_M' + str(_MetalType)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType)][0],
            _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_UCAP_Bottom_VTC_M' + str(_MetalType)]['_YWidth']  = _MetalLength + _ExtraLength
                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_UCAP_Bottom_VTC_M' + str(_MetalType)]['_XWidth']  = _MetalWidth
                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_UCAP_Bottom_VTC_M' + str(_MetalType)]['_XYCoordinates'] = [[0, 0]]
                ## Calculating Bottom plate metal coordinates
                     ## Target_coord: _XY_type1
        tmpXY = []
        tmp1 = self.get_param_KJH4('BND_UCAP_TLEFT_VTC_M'+ str(_MetalType))
        target_coord = tmp1[0][0]['_XY_down_right']
                     ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_UCAP_Bottom_VTC_M' + str(_MetalType))
        approaching_coord = tmp2[0][0]['_XY_down_left']

                     ## Sref coord
        tmp3 = self.get_param_KJH4('BND_UCAP_Bottom_VTC_M' + str(_MetalType))
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        New_Scoord[0] = New_Scoord[0] + _CapSpacing
        New_Scoord[1] = New_Scoord[1] - _ExtraLength
        tmpXY.append(New_Scoord)
        self._DesignParameter['BND_UCAP_Bottom_VTC_M' + str(_MetalType)]['_XYCoordinates'] = tmpXY


            ## TOP RIGHT Metal1 (Part of Top(right) plate at Unitcap)
        self._DesignParameter['BND_UCAP_TRIGHT_VTC_M'+str(_MetalType)] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType)][0],
        _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType)][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_UCAP_TRIGHT_VTC_M'+str(_MetalType)]['_YWidth'] = _MetalLength
                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_UCAP_TRIGHT_VTC_M'+str(_MetalType)]['_XWidth'] = _MetalWidth
                ## Define Boundary_element _XYCoordinates
        bottom_plate_x = tmpXY[0][0]
        self._DesignParameter['BND_UCAP_TRIGHT_VTC_M'+str(_MetalType)]['_XYCoordinates'] = [[2*bottom_plate_x, 0]]

             ##TOP RIGHT Metal2 for generating via(want to generate via only at top plate)
        self._DesignParameter['BND_UCAP_TRIGHT_VTC_M'+str(_MetalType+1)] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType + 1)][0],
        _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType + 1)][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_UCAP_TRIGHT_VTC_M'+str(_MetalType+1)]['_YWidth'] = _MetalLength
                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_UCAP_TRIGHT_VTC_M'+str(_MetalType+1)]['_XWidth'] = _MetalWidth
                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_UCAP_TRIGHT_VTC_M'+str(_MetalType+1)]['_XYCoordinates'] = [[2*bottom_plate_x, 0]]

        ## Via Generation (top plate)
            ## Sref generation: ViaX 1
                ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = _MetalType
        _Caculation_Parameters['_Layer2'] = _MetalType+1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

                ## Sref ViaX declaration 1
        self._DesignParameter['SRF_UCAP_LVIA_VTC_V'+str(_MetalType)] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_UCAP_LVIA_VTC_V{}'.format(_Name,_MetalType)))[0]

                ## Define Sref Relection
        self._DesignParameter['SRF_UCAP_LVIA_VTC_V'+str(_MetalType)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
        self._DesignParameter['SRF_UCAP_LVIA_VTC_V'+str(_MetalType)]['_Angle'] = 0

                ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_UCAP_TLEFT_VTC_M' + str(_MetalType))
        tmp2 = self.get_param_KJH4('BND_UCAP_TLEFT_VTC_M' + str(_MetalType+1))
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

                ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureX')

                ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

                ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_UCAP_LVIA_VTC_V'+str(_MetalType)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
        self._DesignParameter['SRF_UCAP_LVIA_VTC_V'+str(_MetalType)]['_XYCoordinates'] = [[_MetalWidth/2, _MetalLength/2]] ##Orgin of Via SREF is [0,0]

            ## Sref generation: ViaX 2
                ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = _MetalType
        _Caculation_Parameters['_Layer2'] = _MetalType + 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

               ## Sref ViaX declaration 2
        self._DesignParameter['SRF_UCAP_RVIA_VTC_V'+str(_MetalType)] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                        _Name='{}:SRF_UCAP_RVIA_VTC_V{}'.format(_Name,_MetalType)))[0]

               ## Define Sref Relection
        self._DesignParameter['SRF_UCAP_RVIA_VTC_V'+str(_MetalType)]['_Reflect'] = [0, 0, 0]

               ## Define Sref Angle
        self._DesignParameter['SRF_UCAP_RVIA_VTC_V'+str(_MetalType)]['_Angle'] = 0

               ## Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH4('BND_UCAP_TRIGHT_VTC_M' + str(_MetalType))
        tmp2 = self.get_param_KJH4('BND_UCAP_TRIGHT_VTC_M' + str(_MetalType + 1))
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

               ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
        _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureX')

               ## Define _COX and _COY
        _Caculation_Parameters['_COX'] = _COX
        _Caculation_Parameters['_COY'] = _COY

               ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_UCAP_RVIA_VTC_V'+str(_MetalType)]['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

               ## Calculate Sref XYcoord
        top_right_plate_x=2 * bottom_plate_x
        self._DesignParameter['SRF_UCAP_RVIA_VTC_V'+str(_MetalType)]['_XYCoordinates'] = [[_MetalWidth/2 + top_right_plate_x, _MetalLength / 2]]

        print('#########################################################################################################')
        print('                                      Calculation Start                                                  ')
        print('#########################################################################################################')

      #Driving node connecting




############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_KJB
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'H00_01_CAP'
    cellname = 'H00_00_driver_v0'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _MetalType=6, #Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        # _MetalNumber=3,

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
    LayoutObj = _UCAP(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_KJB.USER(DesignParameters._Technology)
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
    # end of 'main():' ---------------------------------------------------------------------------------------------