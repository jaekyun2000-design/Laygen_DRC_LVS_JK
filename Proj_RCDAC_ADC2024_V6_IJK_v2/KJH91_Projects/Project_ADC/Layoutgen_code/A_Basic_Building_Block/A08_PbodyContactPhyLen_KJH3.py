from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A06_PbodyContact_KJH3

## ########################################################################################################################################################## Class_HEADER
class _PbodyContactPhyLen(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_Length		= None,
_NumCont	= None,
_Vtc_flag	= None, # True/False

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

_Length		= None,
_NumCont	= None,
_Vtc_flag	= None,

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

            ## ################################################################################################################### Pre-define Parameters
        #Calculation_Parameters
            #VTC
        if _Vtc_flag == True:
            _NumberOfPbodyCOX = _NumCont
            _NumberOfPbodyCOY = ((int(((_Length - (2 * _DRCObj._CoMinEnclosureByOD)) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))) ) + 0) #maximum number of contact

            #Hrz
        else:
            _NumberOfPbodyCOX = ((int(((_Length - (2 * _DRCObj._CoMinEnclosureByOD)) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))) ) + 0) #maximum number of contact
            _NumberOfPbodyCOY = _NumCont

        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A06_PbodyContact_KJH3._PbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_COX']  	= _NumberOfPbodyCOX
        _Caculation_Parameters['_COY']  	= _NumberOfPbodyCOY

        #Generate Sref
        self._DesignParameter['SRF_PbodyContactPhyLen'] = self._SrefElementDeclaration(_DesignObj=A06_PbodyContact_KJH3._PbodyContact( _DesignParameter=None, _Name='{}:SRF_PbodyContactPhyLen'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['SRF_PbodyContactPhyLen']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['SRF_PbodyContactPhyLen']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['SRF_PbodyContactPhyLen']['_XYCoordinates']=[[0, 0]]


            ## ################################################################################################################### Re-Caculate (OD/RX) Layer
                ## ##################################################################################################### Re-Caculate (OD/RX) Layer: Dummy OD Layer just for Cal
        #Define Boundary_element
        self._DesignParameter['BND_ODLayer_JustCal'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        if _Vtc_flag == True:
            self._DesignParameter['BND_ODLayer_JustCal']['_YWidth'] = _Length
        else:
            tmp = self.get_param_KJH4('SRF_PbodyContactPhyLen','BND_ODLayer')
            self._DesignParameter['BND_ODLayer_JustCal']['_YWidth'] = tmp[0][0][0]['_Ywidth']

            
        #Define Boundary_element _XWidth
        if _Vtc_flag == True:
            tmp = self.get_param_KJH4('SRF_PbodyContactPhyLen','BND_ODLayer')
            self._DesignParameter['BND_ODLayer_JustCal']['_XWidth'] = tmp[0][0][0]['_Xwidth']
        else:
            self._DesignParameter['BND_ODLayer_JustCal']['_XWidth'] = _Length
            
        #Define XYcoord.
                #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['BND_ODLayer_JustCal']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH4('SRF_PbodyContactPhyLen','BND_ODLayer')
        target_coord = tmp1[0][0][0]['_XY_cent']
                #Approaching_coord
        tmp2 = self.get_param_KJH4('BND_ODLayer_JustCal')
        approaching_coord = tmp2[0][0]['_XY_cent']
                #Sref coord
        tmp3 = self.get_param_KJH4('BND_ODLayer_JustCal')
        Scoord = tmp3[0][0]['_XY_origin']
                #Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['BND_ODLayer_JustCal']['_XYCoordinates'] = tmpXY
        
                ## ##################################################################################################### Re-Caculate (OD/RX) Layer: Substitute to real ODLayer
        #Define Boundary_element _XWidth
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_ODLayer']['_XWidth'] = self._DesignParameter['BND_ODLayer_JustCal']['_XWidth']
        #Define Boundary_element _YWidth
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_ODLayer']['_YWidth'] = self._DesignParameter['BND_ODLayer_JustCal']['_YWidth']
        #Define XYcoord.
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_ODLayer']['_XYCoordinates'] = [[0, 0]]

        # Define XYcoord.
        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_ODLayer']['_XYCoordinates'] = [[0, 0]]
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer_JustCal')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyContactPhyLen', 'BND_ODLayer')
        approaching_coord = tmp2[0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyContactPhyLen', 'BND_ODLayer')
        Scoord = tmp3[0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_ODLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Re-Caculate Metal1 Layer
        #Define Boundary_element _XWidth
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_Met1Layer']['_XWidth'] = self._DesignParameter['BND_ODLayer_JustCal']['_XWidth']
        #Define Boundary_element _YWidth
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_Met1Layer']['_YWidth'] = self._DesignParameter['BND_ODLayer_JustCal']['_YWidth']
        #Define XYcoord.
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]

        # Define XYcoord.
        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = [[0, 0]]
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer_JustCal')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        Scoord = tmp3[0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Re-Caculate BP Layer
        #Define Boundary_element _XWidth
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_PPLayer']['_XWidth'] = self._DesignParameter['BND_ODLayer_JustCal']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2
        #Define Boundary_element _YWidth
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_PPLayer']['_YWidth'] = self._DesignParameter['BND_ODLayer_JustCal']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2
        if self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_PPLayer']['_YWidth'] < 170:
            self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_PPLayer']['_YWidth'] = self._DesignParameter['BND_ODLayer_JustCal']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28
        #Define XYcoord.
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_PPLayer']['_XYCoordinates'] = [[0, 0]]

        # Define XYcoord.
        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_PPLayer']['_XYCoordinates'] = [[0, 0]]
        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_ODLayer_JustCal')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_PbodyContactPhyLen', 'BND_PPLayer')
        approaching_coord = tmp2[0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_PbodyContactPhyLen', 'BND_PPLayer')
        Scoord = tmp3[0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_PbodyContactPhyLen']['_DesignObj']._DesignParameter['BND_PPLayer']['_XYCoordinates'] = tmpXY


                ## ##################################################################################################### Delete
        del self._DesignParameter['BND_ODLayer_JustCal']



        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ADC_A_building_block_KJH'
    cellname = 'A05_PbodyContactPhyLen_KJH2_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_Length		= 2123,
_NumCont	= 5,
_Vtc_flag	= False,

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
    LayoutObj = _PbodyContactPhyLen(_DesignParameter=None, _Name=cellname)
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




