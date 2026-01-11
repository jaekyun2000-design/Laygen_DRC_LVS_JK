## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3

############################################################################################################################################################ Class_HEADER
class _ECAP(StickDiagram_KJH1._StickDiagram_KJH):

    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
                                        _LayoutOption=None,
                                        _MetalWidth=None,
                                        _MetalLength=None,
                                        _MetalSpacing=None,
    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,
                                  # # Element Capacitor (0.27fF)
                                  _LayoutOption=None,
                                  _MetalWidth=None,
                                  _MetalLength= None,
                                  _MetalSpacing=None,
                                  ):

        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        # Predefined variable
        _ExtraBottomLength = 300  # default
        ############################################################################################################################################################ CALCULATION START
        print( '#########################################################################################################')
        print( '                                      Calculation Start                                                  ')
        print( '#########################################################################################################')


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Top, Bottom Metal Gen:
        ## Boundary_element Generation
                ##Top left Metal Gen
        TopMetalList = _LayoutOption.copy()
        BotMetalList = _LayoutOption.copy()
        TopMetalList.append(7)
        if _LayoutOption[-1] + 1 > 7:
            raise Exception(f"CDAC cannot be constructed with more than M7 layers.")
        for _MetalType in TopMetalList:
                 ## TOP Metal (Part of Top(left) plate of Unitcap)
            self._DesignParameter['BND_ECAP_Top_VTC_M{}'.format(_MetalType)] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL{}'.format(_MetalType)][0],
            _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_MetalType)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
            )
                    ## Define Boundary_element _YWidth
            self._DesignParameter['BND_ECAP_Top_VTC_M{}'.format(_MetalType)]['_YWidth'] = _MetalLength
                    ## Define Boundary_element _XWidth
            self._DesignParameter['BND_ECAP_Top_VTC_M{}'.format(_MetalType)]['_XWidth'] = _MetalWidth
                    ## Define Boundary_element _XYCoordinates
            self._DesignParameter['BND_ECAP_Top_VTC_M{}'.format(_MetalType)]['_XYCoordinates'] = [[0 , 0]]

        for _MetalType in BotMetalList:
        ## Bottom Metal Gen
            self._DesignParameter['BND_ECAP_Bot_VTC_M{}'.format(_MetalType)] = self._BoundaryElementDeclaration(
                 _Layer=DesignParameters._LayerMapping['METAL{}'.format(_MetalType)][0],
                 _Datatype=DesignParameters._LayerMapping['METAL{}'.format(_MetalType)][1],
                 _XWidth=None,
                 _YWidth=None,
                 _XYCoordinates=[],
             )
                        ## Define Boundary_element _YWidth
            self._DesignParameter['BND_ECAP_Bot_VTC_M{}'.format(_MetalType)]['_YWidth'] = _MetalLength + _ExtraBottomLength
                        ## Define Boundary_element _XWidth
            self._DesignParameter['BND_ECAP_Bot_VTC_M{}'.format(_MetalType)]['_XWidth'] = _MetalWidth
             ## Define Boundary_element _XYCoordinates
            tmp = self.get_param_KJH4('BND_ECAP_Top_VTC_M{}'.format(_MetalType))
            target_coord= tmp[0][0]['_XY_down_right']
            target_coord[0]=target_coord[0] + _MetalSpacing
            target_coord[1]=target_coord[1] - _ExtraBottomLength
            self._DesignParameter['BND_ECAP_Bot_VTC_M{}'. format(_MetalType)]['_XYCoordinates'] = [target_coord]

            ## Top Right metal Gen
        for _MetalType in TopMetalList:
            tmpXY = [[0,0]]
                # Target_coord
            tmp1= self.get_param_KJH4('BND_ECAP_Bot_VTC_M{}'.format(BotMetalList[0]))
            target_coord = tmp1[0][0]['_XY_up_right']
                # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_ECAP_Top_VTC_M{}'.format(_MetalType))
            approaching_coord = tmp2[0][0]['_XY_up_left']
                # Sref coord
            tmp3 =self.get_param_KJH4('BND_ECAP_Top_VTC_M{}'.format(_MetalType))
            Scoord = tmp3[0][0]['_XY_origin']
            New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
            New_Scoord[0] = New_Scoord[0] + _MetalSpacing
            tmpXY.append(New_Scoord)
                    ## Define coordinates
            self._DesignParameter['BND_ECAP_Top_VTC_M{}'.format(_MetalType)]['_XYCoordinates'] = tmpXY


        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Top Metal Via Gen:
        tmpXY = []
        for i in range(2):
            ## Sref generation: ViaX
                ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = TopMetalList[0]
            _Caculation_Parameters['_Layer2'] = 7 # default
            _Caculation_Parameters['_COX'] = None
            _Caculation_Parameters['_COY'] = None

                ## Sref ViaX declaration
            self._DesignParameter['SRF_Top_ViaM{}M{}'.format(TopMetalList[0],7)] = self._SrefElementDeclaration(
                _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                            _Name='{}:SRF_Top_ViaM{}M{}'.format(_Name,TopMetalList[0],7)))[0]

                ## Define Sref Relection
            self._DesignParameter['SRF_Top_ViaM{}M{}'.format(TopMetalList[0],7)]['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle
            self._DesignParameter['SRF_Top_ViaM{}M{}'.format(TopMetalList[0],7)]['_Angle'] = 0

                ## Calcuate Overlapped XYcoord
            tmp1 = self.get_param_KJH4('BND_ECAP_Top_VTC_M{}'.format(TopMetalList[0]))
            tmp2 = self.get_param_KJH4('BND_ECAP_Top_VTC_M{}'.format(7))
            Ovlpcoord = self.get_ovlp_KJH2(tmp1[i][0], tmp2[i][0])

                ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
            #_COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureX')
            _COX, _COY = self._CalculateNumViaByXYWidth(_MetalWidth, _MetalLength, 'MinEnclosureX')
            #_COX, _COY = self._CalculateNumViaByXYWidth(50, 1414, 'MinEnclosureX')

            ## Define _COX and _COY
            _Caculation_Parameters['_COX'] = _COX
            _Caculation_Parameters['_COY'] = _COY
            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_Top_ViaM{}M{}'.format(TopMetalList[0], 7)]['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

                ## Calculate Sref XYcoord
                    ## initialized Sref coordinate
            self._DesignParameter['SRF_Top_ViaM{}M{}'.format(TopMetalList[0],7)]['_XYCoordinates'] = [[0, 0]]

                    ## Target_coord
            tmp1 = self.get_param_KJH4('BND_ECAP_Top_VTC_M{}'.format(TopMetalList[0]))
            target_coord = tmp1[i][0]['_XY_cent']
                    ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Top_ViaM{}M{}'.format(TopMetalList[0],7),'SRF_ViaM{}M{}'.format(TopMetalList[0],TopMetalList[0]+1),'BND_Met{}Layer'.format(TopMetalList[0]))
            approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Top_ViaM{}M{}'.format(TopMetalList[0],7))
            Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_Top_ViaM{}M{}'.format(TopMetalList[0],7)]['_XYCoordinates'] = tmpXY


        if _LayoutOption[0] < 6:
            ################################### Bottom metal Vtc Via
            ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Via Gen: Extended node via
            ## Sref generation: ViaX
            ## Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] = _LayoutOption[0]
            _Caculation_Parameters['_Layer2'] = max(6, _LayoutOption[-1])   #default
            _Caculation_Parameters['_COX'] = 1
            _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
            self._DesignParameter['SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0], max(6, _LayoutOption[-1]))] = \
            self._SrefElementDeclaration(
                _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                            _Name='{}:SRF_Bot_Vtc_ViaM{}M{}'.format(_Name,
                                                                                                   _LayoutOption[0],
                                                                                                   max(6, _LayoutOption[-1]) )))[0]
            ## Define Sref Relection
            self._DesignParameter['SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0], max(6, _LayoutOption[-1]))]['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
            self._DesignParameter['SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0], max(6, _LayoutOption[-1]))]['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
            self._DesignParameter['SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0], max(6, _LayoutOption[-1]))][
                '_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
            tmpXY = []
            ## initialized Sref coordinate
            self._DesignParameter['SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0], max(6, _LayoutOption[-1]))]['_XYCoordinates'] = [[0, 0]]

            ## Calculate
            ## Target_coord
            tmp1 = self.get_param_KJH4('BND_ECAP_Bot_VTC_M{}'.format(_LayoutOption[0]))
            target_coord = tmp1[0][0]['_XY_down']
            ## Approaching_coord
            tmp2 = self.get_param_KJH4('SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0], max(6, _LayoutOption[-1])),
                                       'SRF_ViaM{}M{}'.format(_LayoutOption[0], _LayoutOption[0] + 1),
                                       'BND_Met{}Layer'.format(_LayoutOption[0]))
            approaching_coord = tmp2[0][0][0][0]['_XY_up']
            ## Sref coord
            tmp3 = self.get_param_KJH4('SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0], max(6, _LayoutOption[-1])))
            Scoord = tmp3[0][0]['_XY_origin']
            ## Calculate
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            New_Scoord[1] = New_Scoord[1]
            # New_Scoord[1] = New_Scoord[1]
            tmpXY.append(New_Scoord)
            ## Define
            self._DesignParameter['SRF_Bot_Vtc_ViaM{}M{}'.format(_LayoutOption[0], max(6, _LayoutOption[-1]))]['_XYCoordinates'] = tmpXY



        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_H00_CDAC_v4'
    cellname = 'H00_00_CDAC_ECAP_13'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _LayoutOption=[2,3,4,5],
        _MetalWidth=50, # X_Width
        _MetalLength=1414, #Y_Width
        _MetalSpacing=50,
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
    LayoutObj = _ECAP(_DesignParameter=None, _Name=cellname)
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
    # end of 'main():' ---------------------------------------------------------------------------------------------