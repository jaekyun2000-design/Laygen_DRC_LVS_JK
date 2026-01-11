## Import Basic Modules
    ## Engine
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

    ## Library
import copy
import numpy as np
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST.Trash.H00_CDAC import H00_04_CDAC


class _CDACWithLabel(StickDiagram_KJH1._StickDiagram_KJH) :
    _ParametersForDesignCalculation = dict(
        _MetalType=None,
        _MetalWidth=None,
        _MetalLength=None,
        _MetalNumber=None,  ##Vector Type
        _DummyNumber=None,  ##Vector Type
    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    ## DesignParameter Calculation
    def _CalculateDesignParameter(self,
                                  ##Ground_Shielding
                                  _MetalType=None,
                                  _MetalWidth=None,
                                  _MetalLength=None,
                                  _MetalNumber=None,
                                  _DummyNumber=None,
                                  ):
        _DRCobj = DRC.DRC()
        ## Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        _Caculation_Parameters = copy.deepcopy(H00_04_CDAC._CDAC._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_MetalType'] = _MetalType
        _Caculation_Parameters['_MetalWidth'] = _MetalWidth
        _Caculation_Parameters['_MetalLength'] = _MetalLength
        _Caculation_Parameters['_MetalNumber'] = _MetalNumber
        _Caculation_Parameters['_DummyNumber'] = _DummyNumber

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CDAC_Labeling'] = self._SrefElementDeclaration(
            _DesignObj=H00_04_CDAC._CDAC(_DesignParameter=None, _Name='{}:SRF_CDAC_Labeling'.format(_Name)))[
            0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CDAC_Labeling']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Labeling']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Labeling']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CDAC_Labeling']['_XYCoordinates'] = [[0, 0]]


        ## Labeling: ex)METAL1PIN, METAL2PIN, METAL3PIN, METAL4PIN, METAL5PIN, METAL6PIN, METAL7PIN, METAL8PIN(IA), METAL9PIN(IB),
            #Top label Generation
        self._DesignParameter['BND_CDAC_Label_M'+str(_MetalType+1)] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType + 1) + 'PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType + 1) + 'PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

                # Portname
        self._DesignParameter['BND_CDAC_Label_M'+str(_MetalType+1)]['_TEXT'] = 'Top'

                ## Calculate Sref XYcoord
        tmp = self.get_outter_KJH4('SRF_CDAC_Labeling')
        x_coord= tmp['_Mostright']['coord'][0]/2
        y_coord= tmp['_Mostup']['coord'][0]/2
        self._DesignParameter['BND_CDAC_Label_M'+str(_MetalType+1)]['_XYCoordinates'] = [0,0]
        self._DesignParameter['BND_CDAC_Label_M'+str(_MetalType+1)]['_XYCoordinates'] = [[x_coord,y_coord]]

            ## VSS Label Generation
        self._DesignParameter['BND_CDAC_Label_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType - 2) + 'PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType - 2) + 'PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )

        # Portname
        self._DesignParameter['BND_CDAC_Label_VSS']['_TEXT'] = 'VSS'

        ## Calculate Sref XYcoord
        self._DesignParameter['BND_CDAC_Label_VSS']['_XYCoordinates'] = [[x_coord, y_coord]]


            ## Bottom label Generation
        self._DesignParameter['BND_CDAC_Label_M'+str(_MetalType)] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL' + str(_MetalType) + 'PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL' + str(_MetalType) + 'PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.1, _Angle=0, _TEXT=None,
            _XYCoordinates=None,
        )
        # print(1)

                # Portname
        self._DesignParameter['BND_CDAC_Label_M'+str(_MetalType)]['_TEXT'] = 'Bottom'

                ## Calculate Sref XYcoord
        y_coord2=tmp['_Mostdown']['coord'][0] +100
        # print(1)
        self._DesignParameter['BND_CDAC_Label_M'+str(_MetalType)]['_XYCoordinates'] = [[x_coord,y_coord2]]
        # print(1)




############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_KJB
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'H00_Simul'
    cellname = 'H00_04_driver_v17'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
        # # Unit CDAC
        _MetalType=6, #Poly:0, M1:1, M2:2 ...
        _MetalWidth=50,
        _MetalLength=1414,
        _MetalNumber=np.array([2]),  ##Vector Type
        _DummyNumber=np.array([0,0]),  ##Vector Type
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
    LayoutObj = _CDACWithLabel(_DesignParameter=None, _Name=cellname)
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