import StickDiagram
import DesignParameters
import copy
import DRC
import NMOSWithDummy
import PMOSWithDummy
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import SlicerWithSRLatch_test
import random
import math


class _SlicerWithSRLatchX4(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(
        _SRFinger1=None, _SRFinger2=None, _SRFinger3=None, _SRFinger4=None, \
        _SRNMOSChannelWidth1=None, _SRPMOSChannelWidth1=None, _SRNMOSChannelWidth2=None, _SRPMOSChannelWidth2=None,
        _SRNMOSChannelWidth3=None,
        _SRPMOSChannelWidth3=None, _SRNMOSChannelWidth4=None, _SRPMOSChannelWidth4=None, _SRChannelLength=None,
        _SRNPRatio=None, \
        _SRVDD2VSSHeightAtOneSide=None, _SRDummy=None, _SRNumSupplyCoX=None, _SRNumSupplyCoY=None, \
        _SRSupplyMet1XWidth=None, _SRSupplyMet1YWidth=None, _SRNumViaPoly2Met1CoX=None, \
        _SRNumViaPoly2Met1CoY=None, _SRNumViaPMOSMet12Met2CoX=None, _SRNumViaPMOSMet12Met2CoY=None, \
        _SRNumViaNMOSMet12Met2CoX=None, _SRNumViaNMOSMet12Met2CoY=None, _SRNumViaPMOSMet22Met3CoX=None,
        _SRNumViaPMOSMet22Met3CoY=None, \
        _SRNumViaNMOSMet22Met3CoX=None, _SRNumViaNMOSMet22Met3CoY=None, _SRXVT=None, _SRPowerLine=None,
        _SLCLKinputPMOSFinger1=None, _SLCLKinputPMOSFinger2=None, _SLPMOSFinger=None, _SLPMOSChannelWidth=None,
        _SLDATAinputNMOSFinger=None, _SLNMOSFinger=None, _SLCLKinputNMOSFinger=None, _SLNMOSChannelWidth=None,
        _SLCLKinputNMOSChannelWidth=None,
        _SLChannelLength=None, _SLDummy=False, _SLXVT=False, _SLGuardringWidth=None, _SLGuardring=False,
        _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
        _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None, _SLSupplyMet1YWidth=None,
        _SLVDD2VSSHeight=None,
        _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None, _SLNumVIAMet12COY=None,
        _SLPowerLine=None, _NumberofSlicerWithSRLatch=None, \
        _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None,
        _InvNPRatio=None, _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None,
        _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
        _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
        _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
        _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
        _InvNumViaNMOSMet12Met2CoY=None, _InvXVT=None, _InvPowerLine=None, _SLSRInvSupplyLineX4=None,
    )

    def __init__(self, _DesignParameter=None, _Name='SlicerWithSRLatchX4'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter

        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

    def _CalculateDesignParameter(self, _SRFinger1=None, _SRFinger2=None, _SRFinger3=None, _SRFinger4=None, \
                                  _SRNMOSChannelWidth1=None, _SRPMOSChannelWidth1=None, _SRNMOSChannelWidth2=None,
                                  _SRPMOSChannelWidth2=None, _SRNMOSChannelWidth3=None, _SRPMOSChannelWidth3=None,
                                  _SRNMOSChannelWidth4=None, _SRPMOSChannelWidth4=None, _SRChannelLength=None,
                                  _SRNPRatio=None, \
                                  _SRVDD2VSSHeightAtOneSide=None, _SRDummy=None, _SRNumSupplyCoX=None,
                                  _SRNumSupplyCoY=None, \
                                  _SRSupplyMet1XWidth=None, _SRSupplyMet1YWidth=None, _SRNumViaPoly2Met1CoX=None, \
                                  _SRNumViaPoly2Met1CoY=None, _SRNumViaPMOSMet12Met2CoX=None,
                                  _SRNumViaPMOSMet12Met2CoY=None, \
                                  _SRNumViaNMOSMet12Met2CoX=None, _SRNumViaNMOSMet12Met2CoY=None,
                                  _SRNumViaPMOSMet22Met3CoX=None, _SRNumViaPMOSMet22Met3CoY=None, \
                                  _SRNumViaNMOSMet22Met3CoX=None, _SRNumViaNMOSMet22Met3CoY=None, _SRXVT=None,
                                  _SRPowerLine=None,
                                  _SLCLKinputPMOSFinger1=None, _SLCLKinputPMOSFinger2=None, _SLPMOSFinger=None,
                                  _SLPMOSChannelWidth=None,
                                  _SLDATAinputNMOSFinger=None, _SLNMOSFinger=None, _SLCLKinputNMOSFinger=None,
                                  _SLNMOSChannelWidth=None, _SLCLKinputNMOSChannelWidth=None,
                                  _SLChannelLength=None, _SLDummy=False, _SLXVT=False, _SLGuardringWidth=None,
                                  _SLGuardring=False,
                                  _SLSlicerGuardringWidth=None, _SLSlicerGuardring=False,
                                  _SLNumSupplyCOY=None, _SLNumSupplyCOX=None, _SLSupplyMet1XWidth=None,
                                  _SLSupplyMet1YWidth=None, _SLVDD2VSSHeight=None,
                                  _SLNumVIAPoly2Met1COX=None, _SLNumVIAPoly2Met1COY=None, _SLNumVIAMet12COX=None,
                                  _SLNumVIAMet12COY=None, _SLPowerLine=None, _NumberofSlicerWithSRLatch=None, \
                                  _InvFinger=None, _InvChannelWidth=None, _InvChannelLength=None,
                                  _InvNPRatio=None, _InvVDD2VSSHeight=None, _InvDummy=None, _InvNumSupplyCoX=None,
                                  _InvNumSupplyCoY=None, _InvSupplyMet1XWidth=None,
                                  _InvSupplyMet1YWidth=None, _InvNumViaPoly2Met1CoX=None, \
                                  _InvNumViaPoly2Met1CoY=None, _InvNumViaPMOSMet12Met2CoX=None,
                                  _InvNumViaPMOSMet12Met2CoY=None, _InvNumViaNMOSMet12Met2CoX=None, \
                                  _InvNumViaNMOSMet12Met2CoY=None, _InvXVT=None, _InvPowerLine=None,
                                  _SLSRInvSupplyLineX4=None
                                  ):

        print(
            '#########################################################################################################')
        print(
            '                                {}  SlicerWithSRLatchX4Obj Calculation Start                                  '.format(
                self._DesignParameter['_Name']['_Name']))
        print(
            '#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = 'SlicerWithSRLatchX4'
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        print(
            '###############################        Supply Generation       #########################################')

        if _SLSRInvSupplyLineX4 == True:
            _SRPowerLine = False
            _SLPowerLine = False
            _InvPowerLine = False
            _SLSRInvSupplyLine = True

        elif _SLSRInvSupplyLineX4 == False:
            _SRPowerLine = False
            _SLPowerLine = False
            _InvPowerLine = False
            _SLSRInvSupplyLine = False

        # if _SLSRInvSupplyLineX4 != None :
        #     _SRPowerLine = False
        #     _SLPowerLine = False
        #     _InvPowerLine = False
        #
        # elif _SLSRInvSupplyLineX4 == None :
        #     _SRPowerLine = False
        #     _SLPowerLine = False
        #     _InvPowerLine = False

        print(
            '###############################        SlicerWithSRLatch Generation       #########################################')

        _SlicerWithSRLatchEdgeinputs = copy.deepcopy(SlicerWithSRLatch_test._SlicerWithSRLatch._ParametersForDesignCalculation)
        _SlicerWithSRLatchEdgeinputs['_SRFinger1'] = _SRFinger1
        _SlicerWithSRLatchEdgeinputs['_SRFinger2'] = _SRFinger2
        _SlicerWithSRLatchEdgeinputs['_SRFinger3'] = _SRFinger3
        _SlicerWithSRLatchEdgeinputs['_SRFinger4'] = _SRFinger4
        _SlicerWithSRLatchEdgeinputs['_SRNMOSChannelWidth1'] = _SRNMOSChannelWidth1
        _SlicerWithSRLatchEdgeinputs['_SRPMOSChannelWidth1'] = _SRPMOSChannelWidth1
        _SlicerWithSRLatchEdgeinputs['_SRNMOSChannelWidth2'] = _SRNMOSChannelWidth2
        _SlicerWithSRLatchEdgeinputs['_SRPMOSChannelWidth2'] = _SRPMOSChannelWidth2
        _SlicerWithSRLatchEdgeinputs['_SRNMOSChannelWidth3'] = _SRNMOSChannelWidth3
        _SlicerWithSRLatchEdgeinputs['_SRPMOSChannelWidth3'] = _SRPMOSChannelWidth3
        _SlicerWithSRLatchEdgeinputs['_SRNMOSChannelWidth4'] = _SRNMOSChannelWidth4
        _SlicerWithSRLatchEdgeinputs['_SRPMOSChannelWidth4'] = _SRPMOSChannelWidth4
        _SlicerWithSRLatchEdgeinputs['_SRChannelLength'] = _SRChannelLength
        _SlicerWithSRLatchEdgeinputs['_SRNPRatio'] = _SRNPRatio
        _SlicerWithSRLatchEdgeinputs['_SRVDD2VSSHeightAtOneSide'] = _SRVDD2VSSHeightAtOneSide
        _SlicerWithSRLatchEdgeinputs['_SRDummy'] = _SRDummy
        _SlicerWithSRLatchEdgeinputs['_SRNumSupplyCoX'] = _SRNumSupplyCoX
        _SlicerWithSRLatchEdgeinputs['_SRNumSupplyCoY'] = _SRNumSupplyCoY
        _SlicerWithSRLatchEdgeinputs['_SRSupplyMet1XWidth'] = _SRSupplyMet1XWidth
        _SlicerWithSRLatchEdgeinputs['_SRSupplyMet1YWidth'] = _SRSupplyMet1YWidth
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPoly2Met1CoX'] = _SRNumViaPoly2Met1CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPoly2Met1CoY'] = _SRNumViaPoly2Met1CoY
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPMOSMet12Met2CoX'] = _SRNumViaPMOSMet12Met2CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPMOSMet12Met2CoY'] = _SRNumViaPMOSMet12Met2CoY
        _SlicerWithSRLatchEdgeinputs['_SRNumViaNMOSMet12Met2CoX'] = _SRNumViaNMOSMet12Met2CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaNMOSMet12Met2CoY'] = _SRNumViaNMOSMet12Met2CoY
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPMOSMet22Met3CoX'] = _SRNumViaPMOSMet22Met3CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaPMOSMet22Met3CoY'] = _SRNumViaPMOSMet22Met3CoY
        _SlicerWithSRLatchEdgeinputs['_SRNumViaNMOSMet22Met3CoX'] = _SRNumViaNMOSMet22Met3CoX
        _SlicerWithSRLatchEdgeinputs['_SRNumViaNMOSMet22Met3CoY'] = _SRNumViaNMOSMet22Met3CoY
        _SlicerWithSRLatchEdgeinputs['_SRXVT'] = _SRXVT
        _SlicerWithSRLatchEdgeinputs['_SRPowerLine'] = _SRPowerLine

        _SlicerWithSRLatchEdgeinputs['_SLCLKinputPMOSFinger1'] = _SLCLKinputPMOSFinger1
        _SlicerWithSRLatchEdgeinputs['_SLCLKinputPMOSFinger2'] = _SLCLKinputPMOSFinger2
        _SlicerWithSRLatchEdgeinputs['_SLPMOSFinger'] = _SLPMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLPMOSChannelWidth'] = _SLPMOSChannelWidth
        _SlicerWithSRLatchEdgeinputs['_SLDATAinputNMOSFinger'] = _SLDATAinputNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLNMOSFinger'] = _SLNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLCLKinputNMOSFinger'] = _SLCLKinputNMOSFinger
        _SlicerWithSRLatchEdgeinputs['_SLNMOSChannelWidth'] = _SLNMOSChannelWidth
        _SlicerWithSRLatchEdgeinputs['_SLCLKinputNMOSChannelWidth'] = _SLCLKinputNMOSChannelWidth
        _SlicerWithSRLatchEdgeinputs['_SLChannelLength'] = _SLChannelLength
        _SlicerWithSRLatchEdgeinputs['_SLDummy'] = _SLDummy
        _SlicerWithSRLatchEdgeinputs['_SLXVT'] = _SLXVT
        _SlicerWithSRLatchEdgeinputs['_SLGuardringWidth'] = _SLGuardringWidth
        _SlicerWithSRLatchEdgeinputs['_SLGuardring'] = _SLGuardring
        _SlicerWithSRLatchEdgeinputs['_SLSlicerGuardringWidth'] = _SLSlicerGuardringWidth
        _SlicerWithSRLatchEdgeinputs['_SLSlicerGuardring'] = _SLSlicerGuardring
        _SlicerWithSRLatchEdgeinputs['_SLNumSupplyCOX'] = _SLNumSupplyCOX
        _SlicerWithSRLatchEdgeinputs['_SLNumSupplyCOY'] = _SLNumSupplyCOY
        _SlicerWithSRLatchEdgeinputs['_SLSupplyMet1XWidth'] = _SLSupplyMet1XWidth
        _SlicerWithSRLatchEdgeinputs['_SLSupplyMet1YWidth'] = _SLSupplyMet1YWidth
        _SlicerWithSRLatchEdgeinputs['_SLVDD2VSSHeight'] = _SLVDD2VSSHeight
        _SlicerWithSRLatchEdgeinputs['_SLNumVIAPoly2Met1COX'] = _SLNumVIAPoly2Met1COX
        _SlicerWithSRLatchEdgeinputs['_SLNumVIAPoly2Met1COY'] = _SLNumVIAPoly2Met1COY
        _SlicerWithSRLatchEdgeinputs['_SLNumVIAMet12COY'] = _SLNumVIAMet12COX
        _SlicerWithSRLatchEdgeinputs['_SLNumVIAMet12COY'] = _SLNumVIAMet12COY
        _SlicerWithSRLatchEdgeinputs['_SLPowerLine'] = _SLPowerLine

        _SlicerWithSRLatchEdgeinputs['_InvFinger'] = _InvFinger
        _SlicerWithSRLatchEdgeinputs['_InvChannelWidth'] = _InvChannelWidth
        _SlicerWithSRLatchEdgeinputs['_InvChannelLength'] = _InvChannelLength
        _SlicerWithSRLatchEdgeinputs['_InvNPRatio'] = _InvNPRatio
        _SlicerWithSRLatchEdgeinputs['_InvVDD2VSSHeight'] = _InvVDD2VSSHeight
        _SlicerWithSRLatchEdgeinputs['_InvDummy'] = _InvDummy
        _SlicerWithSRLatchEdgeinputs['_InvNumSupplyCoX'] = _InvNumSupplyCoX
        _SlicerWithSRLatchEdgeinputs['_InvNumSupplyCoY'] = _InvNumSupplyCoY
        _SlicerWithSRLatchEdgeinputs['_InvSupplyMet1XWidth'] = _InvSupplyMet1XWidth
        _SlicerWithSRLatchEdgeinputs['_InvSupplyMet1YWidth'] = _InvSupplyMet1YWidth
        _SlicerWithSRLatchEdgeinputs['_InvNumViaPoly2Met1CoX'] = _InvNumViaPoly2Met1CoX
        _SlicerWithSRLatchEdgeinputs['_InvNumViaPoly2Met1CoY'] = _InvNumViaPoly2Met1CoY
        _SlicerWithSRLatchEdgeinputs['_InvNumViaPMOSMet12Met2CoX'] = _InvNumViaPMOSMet12Met2CoX
        _SlicerWithSRLatchEdgeinputs['_InvNumViaPMOSMet12Met2CoY'] = _InvNumViaPMOSMet12Met2CoY
        _SlicerWithSRLatchEdgeinputs['_InvNumViaNMOSMet12Met2CoX'] = _InvNumViaNMOSMet12Met2CoX
        _SlicerWithSRLatchEdgeinputs['_InvNumViaNMOSMet12Met2CoY'] = _InvNumViaNMOSMet12Met2CoY
        _SlicerWithSRLatchEdgeinputs['_InvXVT'] = _InvXVT
        _SlicerWithSRLatchEdgeinputs['_InvPowerLine'] = _InvPowerLine

        _SlicerWithSRLatchEdgeinputs['_SLSRInvSupplyLine'] = _SLSRInvSupplyLine


        self._DesignParameter['_SlicerWithSRLatchX4'] = self._SrefElementDeclaration(_DesignObj=SlicerWithSRLatch_test._SlicerWithSRLatch(_DesignParameter=None, _Name="SlicerWithSRLatchIn{}".format(_Name)))[0]
        self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._CalculateDesignParameter(**_SlicerWithSRLatchEdgeinputs)

        print('#################################       Coordinates Settings      #########################################')
        _OriginXYCoordinateOfSlicerWithSRLatch = [[0, 0]]

        PMOS_toptmp = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore'], MinSnapSpacing)
        PMOS_bottomtmp = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore'], MinSnapSpacing)
        NMOS_toptmp = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore'], MinSnapSpacing)
        NMOS_bottomtmp = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore'], MinSnapSpacing)
        Guardring_top = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1], MinSnapSpacing)
        Guardring_bottom = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1], MinSnapSpacing)
        Guardring_left = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0], MinSnapSpacing)
        Guardring_right = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0], MinSnapSpacing)

        MinGuardringHeight = Guardring_top - Guardring_bottom
        GuardringHeight = MinGuardringHeight

        if (self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]) - (self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] - GuardringHeight) < _DRCObj._Metal1MinSpace3 + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2:
            GuardringHeight = self.CeilMinSnapSpacing(max((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]) - (self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]) + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, MinGuardringHeight + _SLSlicerGuardringWidth) + _DRCObj._Metal1MinSpace3, MinSnapSpacing)

        if GuardringHeight < MinGuardringHeight:
            GuardringHeight = MinGuardringHeight

        if MinGuardringHeight < GuardringHeight < MinGuardringHeight + _SLSlicerGuardringWidth:
            GuardringHeight = MinGuardringHeight + _SLSlicerGuardringWidth

        self._DesignParameter['_GuardringHeight'] = {'_Ignore': GuardringHeight, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_PMOS_toptmp'] = {'_Ignore': PMOS_toptmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_PMOS_bottomtmp'] = {'_Ignore': PMOS_toptmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_NMOS_toptmp'] = {'_Ignore': NMOS_bottomtmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_NMOS_bottomtmp'] = {'_Ignore': NMOS_bottomtmp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_Guardring_top'] = {'_Ignore': Guardring_top, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
        self._DesignParameter['_Guardring_bottom'] = {'_Ignore': Guardring_bottom, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}

        _VDD2VSSHeightAtOneSide = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]

        tmp = []

        YINp = self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1]
        self._DesignParameter['_YINp'] = {'_Ignore': YINp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}

        XINp = abs(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0])
        self._DesignParameter['_XINp'] = {'_Ignore': XINp, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}

        for i in range(0, _NumberofSlicerWithSRLatch):
            tmp.append([_OriginXYCoordinateOfSlicerWithSRLatch[0][0], self.CeilMinSnapSpacing(_OriginXYCoordinateOfSlicerWithSRLatch[0][1] - i * GuardringHeight, MinSnapSpacing)])

        self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'] = tmp
        del tmp


        self._DesignParameter['_AdditionalPPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=400)
        self._DesignParameter['_AdditionalPPLayer']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_PPLayer']['_Width'], 2 * MinSnapSpacing)

        tmp = []

        for i in range(0, _NumberofSlicerWithSRLatch - 1):
            tmp.append([[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] +  self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1][1], MinSnapSpacing)], \
                        [self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i + 1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0][1], MinSnapSpacing)]])

        self._DesignParameter['_AdditionalPPLayer']['_XYCoordinates'] = tmp

        print('#################################       Supply Line Routing      #########################################')
        if _SLSRInvSupplyLineX4 == True:
            self._DesignParameter['_Met3VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met3VDDRouting']['_Width'] = _SLGuardringWidth

            self._DesignParameter['_Met5VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met5VDDRouting']['_Width'] = 16 * _DRCObj._MetalxMinWidth

            self._DesignParameter['_Met6VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met6VDDRouting']['_Width'] = self.CeilMinSnapSpacing((self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] +
                                                                      self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2 - (Guardring_right + _SLSlicerGuardringWidth / 2) - _DRCObj._MetalxMinSpace11) / 2, 2 * MinSnapSpacing)

            if self._DesignParameter['_Met6VDDRouting']['_Width'] > _DRCObj._MetalxMaxWidth:
                self._DesignParameter['_Met6VDDRouting']['_Width'] = _DRCObj._MetalxMaxWidth

            self._DesignParameter['_Met4VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met4VDDRouting']['_Width'] = 8 * _DRCObj._MetalxMinWidth
            self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing(Guardring_left + self._DesignParameter['_Met4VDDRouting']['_Width'] / 2 - _SLSlicerGuardringWidth / 2, MinSnapSpacing), self.CeilMinSnapSpacing(Guardring_top + _SLSlicerGuardringWidth / 2 + self._DesignParameter['_Met5VDDRouting']['_Width'] / 2, MinSnapSpacing)], \
                                                                           [self.CeilMinSnapSpacing(Guardring_left + self._DesignParameter['_Met4VDDRouting']['_Width'] / 2 - _SLSlicerGuardringWidth / 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + Guardring_bottom - self._DesignParameter['_Met5VDDRouting']['_Width'] / 2, MinSnapSpacing)]], \
                                                                          [[self.CeilMinSnapSpacing(Guardring_right - self._DesignParameter['_Met4VDDRouting']['_Width'] / 2 + _SLSlicerGuardringWidth / 2, MinSnapSpacing), self.CeilMinSnapSpacing(Guardring_top + _SLSlicerGuardringWidth / 2 + self._DesignParameter['_Met5VDDRouting']['_Width'] / 2, MinSnapSpacing)], \
                                                                           [self.CeilMinSnapSpacing(Guardring_right - self._DesignParameter['_Met4VDDRouting']['_Width'] / 2 + _SLSlicerGuardringWidth / 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + Guardring_bottom - self._DesignParameter['_Met5VDDRouting']['_Width'] / 2, MinSnapSpacing)]]]

            self._DesignParameter['_Met5VSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met5VSSRouting']['_Width'] = 16 * _DRCObj._MetalxMinWidth

            self._DesignParameter['_Met6VSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met6VSSRouting']['_Width'] = self._DesignParameter['_Met6VDDRouting']['_Width']

            tmp = []
            for i in range(0, _NumberofSlicerWithSRLatch):
                tmp.append([[self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0], MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp, MinSnapSpacing)], \
                            [self.CeilMinSnapSpacing(self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0] - self._DesignParameter['_Met4VDDRouting']['_Width'] / 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp, MinSnapSpacing)]])

            self._DesignParameter['_Met3VDDRouting']['_XYCoordinates'] = tmp

            _ViaXMet32Met4forVDD = int((self._DesignParameter['_Met4VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaYMet32Met4forVDD = int((self._DesignParameter['_Met3VDDRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaXMet32Met4forVDD <= 1:
                _ViaXMet32Met4forVDD = 1
                _ViaYMet32Met4forVDD = int(
                    (self._DesignParameter['_Met3VDDRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaYMet32Met4forVDD <= 1:
                _ViaYMet32Met4forVDD = 1
                _ViaXMet32Met4forVDD = int((self._DesignParameter['_Met4VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet32Met4forVDD = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaMet32Met4forVDD['_ViaMet32Met4NumberOfCOX'] = _ViaXMet32Met4forVDD
            _ViaMet32Met4forVDD['_ViaMet32Met4NumberOfCOY'] = _ViaYMet32Met4forVDD
            self._DesignParameter['_ViaMet32Met4forVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4forVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet32Met4forVDD']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaMet32Met4forVDD)

            tmp = []
            for i in range(0, _NumberofSlicerWithSRLatch):
                tmp.append([self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0],
                            self._DesignParameter['_Met3VDDRouting']['_XYCoordinates'][i][0][1]])
                tmp.append([self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][1][0][0],
                            self._DesignParameter['_Met3VDDRouting']['_XYCoordinates'][i][0][1]])

            self._DesignParameter['_ViaMet32Met4forVDD']['_XYCoordinates'] = tmp

            del tmp

            tmp = []
            tmp.append([[self.CeilMinSnapSpacing(self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0] - self._DesignParameter['_Met4VDDRouting']['_Width'] / 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1], MinSnapSpacing)], \
                        [self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1], MinSnapSpacing)]])

            for i in range(0, _NumberofSlicerWithSRLatch // 2):
                tmp.append([[self.CeilMinSnapSpacing(self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0] - self._DesignParameter['_Met4VDDRouting']['_Width'] / 2, MinSnapSpacing),\
                             self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i + 1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1], MinSnapSpacing)], \
                            [self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2, MinSnapSpacing),
                             self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i + 1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1], MinSnapSpacing)]])

            self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'] = tmp

            del tmp

            _ViaXMet52Met6forVSS = int((self._DesignParameter['_Met6VSSRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaYMet52Met6forVSS = int((self._DesignParameter['_Met5VSSRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaXMet52Met6forVSS <= 1:
                _ViaXMet52Met6forVSS = 1
                _ViaYMet52Met6forVSS = int((self._DesignParameter['_Met5VSSRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaYMet52Met6forVSS <= 1:
                _ViaYMet52Met6forVSS = 1
                _ViaXMet52Met6forVSS = int((self._DesignParameter['_Met6VSSRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet52Met6forVSS = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaMet52Met6forVSS['_ViaMet52Met6NumberOfCOX'] = _ViaXMet52Met6forVSS
            _ViaMet52Met6forVSS['_ViaMet52Met6NumberOfCOY'] = _ViaYMet52Met6forVSS
            self._DesignParameter['_ViaMet52Met6forVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6forVSSIn{}'.format(_Name)))[0]

            self._DesignParameter['_ViaMet52Met6forVSS']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaMet52Met6forVSS)

            self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing(Guardring_right + self._DesignParameter['_Met6VDDRouting']['_Width'] / 2 + _SLSlicerGuardringWidth / 2 + self._DesignParameter['_Met6VDDRouting']['_Width'] + _DRCObj._MetalxMinSpace11, MinSnapSpacing), self.CeilMinSnapSpacing(Guardring_top + _SLSlicerGuardringWidth / 2 + self._DesignParameter['_Met6VDDRouting']['_Width'] / 2, MinSnapSpacing)], \
                                                                           [self.CeilMinSnapSpacing(Guardring_right + self._DesignParameter['_Met6VDDRouting']['_Width'] / 2 + _SLSlicerGuardringWidth / 2 + self._DesignParameter['_Met6VDDRouting']['_Width'] + _DRCObj._MetalxMinSpace11, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] - GuardringHeight, MinSnapSpacing)]]]

            self._DesignParameter['_Met6VSSRouting']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing(Guardring_right + self._DesignParameter['_Met6VSSRouting']['_Width'] / 2 + _SLSlicerGuardringWidth / 2, MinSnapSpacing), self.CeilMinSnapSpacing(Guardring_top + _SLSlicerGuardringWidth / 2 + self._DesignParameter['_Met6VDDRouting']['_Width'] / 2, MinSnapSpacing)], \
                                                                           [self.CeilMinSnapSpacing(Guardring_right + self._DesignParameter['_Met6VSSRouting']['_Width'] / 2 + _SLSlicerGuardringWidth / 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] - GuardringHeight, MinSnapSpacing)]]]

            tmp = []
            tmpY = self.CeilMinSnapSpacing(min(self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_ViaMet42Met5forCLKInput']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth'] / 2 - self._DesignParameter['_Met5VSSRouting']['_Width'] / 2 - _DRCObj._MetalxMinSpace6,
                       self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][1]), MinSnapSpacing)

            for i in range(0, _NumberofSlicerWithSRLatch // 2 - 1):
                tmp.append([[self.CeilMinSnapSpacing(self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0] -
                             self._DesignParameter['_Met4VDDRouting']['_Width'] / 2, MinSnapSpacing),
                             self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i + 1][1] + tmpY, MinSnapSpacing)], \
                            [self.CeilMinSnapSpacing(self._DesignParameter['_Met6VSSRouting']['_XYCoordinates'][0][0][0] +
                             self._DesignParameter['_Met6VSSRouting']['_Width'] / 2, MinSnapSpacing),
                             self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i + 1][1] + tmpY, MinSnapSpacing)]])

            if _NumberofSlicerWithSRLatch % 2 == 1 and _NumberofSlicerWithSRLatch != 1:
                tmp.append([[self.CeilMinSnapSpacing(self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0] -
                             self._DesignParameter['_Met4VDDRouting']['_Width'] / 2, MinSnapSpacing),
                             self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-2][1] + tmpY, MinSnapSpacing)], [
                                self.CeilMinSnapSpacing(self._DesignParameter['_Met6VSSRouting']['_XYCoordinates'][0][0][0] +
                                self._DesignParameter['_Met6VSSRouting']['_Width'] / 2, MinSnapSpacing),
                                self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-2][1] + tmpY, MinSnapSpacing)]])

            tmp.append([[self.CeilMinSnapSpacing(self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0] -
                         self._DesignParameter['_Met4VDDRouting']['_Width'] / 2, MinSnapSpacing),
                         self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + tmpY, MinSnapSpacing)], [
                            self.CeilMinSnapSpacing(self._DesignParameter['_Met6VSSRouting']['_XYCoordinates'][0][0][0] +
                            self._DesignParameter['_Met6VSSRouting']['_Width'] / 2, MinSnapSpacing),
                            self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + tmpY, MinSnapSpacing)]])

            self._DesignParameter['_Met5VSSRouting']['_XYCoordinates'] = tmp

            del tmp


            _ViaXMet42Met5forVDD2 = int((self._DesignParameter['_Met4VDDRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaYMet42Met5forVDD2 = int((self._DesignParameter['_Met5VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaXMet42Met5forVDD2 <= 1:
                _ViaXMet42Met5forVDD2 = 1
                _ViaYMet42Met5forVDD2 = int((self._DesignParameter['_Met5VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaYMet42Met5forVDD2 <= 1:
                _ViaYMet42Met5forVDD2 = 1
                _ViaXMet42Met5forVDD2 = int((self._DesignParameter['_Met4VDDRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet42Met5forVDD2 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaMet42Met5forVDD2['_ViaMet42Met5NumberOfCOX'] = _ViaXMet42Met5forVDD2
            _ViaMet42Met5forVDD2['_ViaMet42Met5NumberOfCOY'] = _ViaYMet42Met5forVDD2
            self._DesignParameter['_ViaMet42Met5forVDD2'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5forVDD2In{}'.format(_Name)))[0]

            self._DesignParameter['_ViaMet42Met5forVDD2']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaMet42Met5forVDD2)

            tmp = []
            for i in range(0, len(self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'])):
                for j in range(0, len(self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'])):
                    tmp.append([self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][i][0][0], self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'][j][0][1]])

            self._DesignParameter['_ViaMet42Met5forVDD2']['_XYCoordinates'] = tmp

            del tmp

            _ViaXMet52Met6forVDD = int((self._DesignParameter['_Met6VDDRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaYMet52Met6forVDD = int((self._DesignParameter['_Met5VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaXMet52Met6forVDD <= 1:
                _ViaXMet52Met6forVDD = 1
                _ViaYMet52Met6forVDD = int((self._DesignParameter['_Met5VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaYMet52Met6forVDD <= 1:
                _ViaYMet52Met6forVDD = 1
                _ViaXMet52Met6forVDD = int((self._DesignParameter['_Met6VDDRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet52Met6forVDD = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaMet52Met6forVDD['_ViaMet52Met6NumberOfCOX'] = _ViaXMet52Met6forVDD
            _ViaMet52Met6forVDD['_ViaMet52Met6NumberOfCOY'] = _ViaYMet52Met6forVDD
            self._DesignParameter['_ViaMet52Met6forVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6forVDDIn{}'.format(_Name)))[0]

            self._DesignParameter['_ViaMet52Met6forVDD']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaMet52Met6forVDD)

            tmp = []

            for i in range(0, len(self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'])):
                for j in range(0, len(self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'])):
                    tmp.append([self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][i][0][0], self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'][j][0][1]])

            self._DesignParameter['_ViaMet52Met6forVDD']['_XYCoordinates'] = tmp

            del tmp

            _ViaXMet32Met4forVSS = int((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            _ViaYMet32Met4forVSS = int((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaXMet32Met4forVSS <= 1:
                _ViaXMet32Met4forVSS = 1
                _ViaYMet32Met4forVSS = int((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            if _ViaYMet32Met4forVSS <= 1:
                _ViaYMet32Met4forVSS = 1
                _ViaXMet32Met4forVSS = int((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][0] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Met4CLKinput']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet32Met4forVSS = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaMet32Met4forVSS['_ViaMet32Met4NumberOfCOX'] = _ViaXMet32Met4forVSS
            _ViaMet32Met4forVSS['_ViaMet32Met4NumberOfCOY'] = _ViaYMet32Met4forVSS
            self._DesignParameter['_ViaMet32Met4forVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4forVSSIn{}'.format(_Name)))[0]

            self._DesignParameter['_ViaMet32Met4forVSS']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet32Met4forVSS)

            tmp = []
            for i in range(0, _NumberofSlicerWithSRLatch // 2):
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i + 1][0], self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i + 1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SupplyLineMet3VSS']['_XYCoordinates'][0][1]])

            if _NumberofSlicerWithSRLatch % 2 == 1:
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0], self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_SupplyLineMet3VSS']['_XYCoordinates'][0][1]])
            self._DesignParameter['_ViaMet32Met4forVSS']['_XYCoordinates'] = tmp

            del tmp

            _ViaXMet42Met5forVSS = int((self._DesignParameter['_ViaMet32Met4forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaYMet42Met5forVSS = int((self._DesignParameter['_ViaMet32Met4forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaXMet42Met5forVSS <= 1:
                _ViaXMet42Met5forVSS = 1
                _ViaYMet42Met5forVSS = int((self._DesignParameter['_ViaMet32Met4forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaYMet42Met5forVSS <= 1:
                _ViaYMet42Met5forVSS = 1
                _ViaXMet42Met5forVSS = int((self._DesignParameter['_ViaMet32Met4forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet42Met5forVSS = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaMet42Met5forVSS['_ViaMet42Met5NumberOfCOX'] = _ViaXMet42Met5forVSS
            _ViaMet42Met5forVSS['_ViaMet42Met5NumberOfCOY'] = _ViaYMet42Met5forVSS
            self._DesignParameter['_ViaMet42Met5forVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5forVSSIn{}'.format(_Name)))[0]

            self._DesignParameter['_ViaMet42Met5forVSS']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaMet42Met5forVSS)

            tmp = []
            for i in range(0, _NumberofSlicerWithSRLatch // 2):
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i + 1][0], self._DesignParameter['_Met5VSSRouting']['_XYCoordinates'][i][0][1]])

            if _NumberofSlicerWithSRLatch % 2 == 1:
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][0], self._DesignParameter['_Met5VSSRouting']['_XYCoordinates'][-1][0][1]])

            self._DesignParameter['_ViaMet42Met5forVSS']['_XYCoordinates'] = tmp

            del tmp

            self._DesignParameter['_Met4VSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_Met4VSSRouting']['_Width'] = self.CeilMinSnapSpacing(max(self._DesignParameter['_ViaMet32Met4forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'], self._DesignParameter['_ViaMet42Met5forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']), 2 * MinSnapSpacing)

            tmp = []
            for i in range(0, (_NumberofSlicerWithSRLatch + 1) // 2):
                tmp.append([[self._DesignParameter['_ViaMet32Met4forVSS']['_XYCoordinates'][i][0], self.CeilMinSnapSpacing(max(self._DesignParameter['_ViaMet32Met4forVSS']['_XYCoordinates'][i][1] + self._DesignParameter['_ViaMet32Met4forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2, self._DesignParameter['_ViaMet42Met5forVSS']['_XYCoordinates'][i][1] + self._DesignParameter['_ViaMet42Met5forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2), MinSnapSpacing)], \
                            [self._DesignParameter['_ViaMet32Met4forVSS']['_XYCoordinates'][i][0], self.CeilMinSnapSpacing(min(self._DesignParameter['_ViaMet32Met4forVSS']['_XYCoordinates'][i][1] - self._DesignParameter['_ViaMet32Met4forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2, self._DesignParameter['_ViaMet42Met5forVSS']['_XYCoordinates'][i][1] - self._DesignParameter['_ViaMet42Met5forVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2), MinSnapSpacing)]])

            self._DesignParameter['_Met4VSSRouting']['_XYCoordinates'] = tmp

            del tmp

            tmp = []
            for i in range(0, len(self._DesignParameter['_Met6VSSRouting']['_XYCoordinates'])):
                for j in range(0, len(self._DesignParameter['_Met5VSSRouting']['_XYCoordinates'])):
                    tmp.append([self._DesignParameter['_Met6VSSRouting']['_XYCoordinates'][i][0][0], self._DesignParameter['_Met5VSSRouting']['_XYCoordinates'][j][0][1]])

            self._DesignParameter['_ViaMet52Met6forVSS']['_XYCoordinates'] = tmp

            del tmp



            _ViaXMet42Met5forVDDinSR = int((self._DesignParameter['_Met6VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaYMet42Met5forVDDinSR = int((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaXMet42Met5forVDDinSR <= 1:
                _ViaXMet42Met5forVDDinSR = 1
                _ViaYMet42Met5forVDDinSR = int((self._DesignParameter['_Met5VDDRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaYMet42Met5forVDDinSR <= 1:
                _ViaYMet42Met5forVDDinSR = 1
                _ViaXMet42Met5forVDDinSR = int((self._DesignParameter['_Met6VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet42Met5forVDDinSR = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaMet42Met5forVDDinSR['_ViaMet42Met5NumberOfCOX'] = _ViaXMet42Met5forVDDinSR
            _ViaMet42Met5forVDDinSR['_ViaMet42Met5NumberOfCOY'] = _ViaYMet42Met5forVDDinSR
            self._DesignParameter['_ViaMet42Met5forVDDinSR'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name='ViaMet42Met5forVDDinSRIn{}'.format(_Name)))[0]

            self._DesignParameter['_ViaMet42Met5forVDDinSR']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaMet42Met5forVDDinSR)

            tmp = []
            for i in range(0, _NumberofSlicerWithSRLatch):
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0][0],
                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]])
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0][0],
                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]])

            self._DesignParameter['_ViaMet42Met5forVDDinSR']['_XYCoordinates'] = tmp

            del tmp

            _ViaXMet52Met6forVDDinSR = int((self._DesignParameter['_Met6VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
            _ViaYMet52Met6forVDDinSR = int((self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

            if _ViaXMet52Met6forVDDinSR <= 1:
                _ViaXMet52Met6forVDDinSR = 1
                _ViaYMet52Met6forVDDinSR = int((self._DesignParameter['_Met5VDDRouting']['_Width'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
            if _ViaYMet52Met6forVDDinSR <= 1:
                _ViaYMet52Met6forVDDinSR = 1
                _ViaXMet52Met6forVDDinSR = int((self._DesignParameter['_Met6VDDRouting']['_Width'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

            _ViaMet52Met6forVDDinSR = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaMet52Met6forVDDinSR['_ViaMet52Met6NumberOfCOX'] = _ViaXMet52Met6forVDDinSR
            _ViaMet52Met6forVDDinSR['_ViaMet52Met6NumberOfCOY'] = _ViaYMet52Met6forVDDinSR
            self._DesignParameter['_ViaMet52Met6forVDDinSR'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name='ViaMet52Met6forVDDinSRIn{}'.format(_Name)))[0]

            self._DesignParameter['_ViaMet52Met6forVDDinSR']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**_ViaMet52Met6forVDDinSR)

            tmp = []
            for i in range(0, (_NumberofSlicerWithSRLatch + 1) // 2 - 1):
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0][0],
                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][2 * i + 2][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]])
            for i in range(0, _NumberofSlicerWithSRLatch):
                tmp.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][0] + self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0][0],
                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][i][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_SRLatch']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][1][1]])

            self._DesignParameter['_ViaMet52Met6forVDDinSR']['_XYCoordinates'] = tmp

            del tmp


            self._DesignParameter['_AdditionalMet2forVSSinSL'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_AdditionalMet2forVSSinSL']['_Width'] = self.CeilMinSnapSpacing(_SLSlicerGuardringWidth + 2 * _DRCObj._MetalxMinWidth, 2 * MinSnapSpacing)

            self._DesignParameter['_AdditionalMet2forVSSinSL']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing(Guardring_left + self._DesignParameter['_AdditionalMet2forVSSinSL']['_Width'] / 2 - _SLSlicerGuardringWidth / 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1], MinSnapSpacing)], \
                                                                                     [self.CeilMinSnapSpacing(Guardring_left + self._DesignParameter['_AdditionalMet2forVSSinSL']['_Width'] / 2 - _SLSlicerGuardringWidth / 2, MinSnapSpacing), self.CeilMinSnapSpacing(min(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]), MinSnapSpacing)]], \
                                                                                    [[self.CeilMinSnapSpacing(Guardring_right - self._DesignParameter['_AdditionalMet2forVSSinSL']['_Width'] / 2 + _SLSlicerGuardringWidth / 2, MinSnapSpacing),
                                                                                      self.CeilMinSnapSpacing(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1], MinSnapSpacing)], \
                                                                                     [self.CeilMinSnapSpacing(Guardring_right - self._DesignParameter['_AdditionalMet2forVSSinSL']['_Width'] / 2 + _SLSlicerGuardringWidth / 2, MinSnapSpacing),
                                                                                      self.CeilMinSnapSpacing(min(self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][-1][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]), MinSnapSpacing)]]]

            self._DesignParameter['_AdditionalLineVDDMet4'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_AdditionalLineVDDMet4']['_Width'] = self._DesignParameter['_Met4VDDRouting'][
                '_Width']
            self._DesignParameter['_AdditionalLineVDDMet4']['_XYCoordinates'] = [
                [self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0],
                 [self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][0][0][0],
                  self.CeilMinSnapSpacing(self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'][0][0][1] +
                  self._DesignParameter['_Met5VDDRouting']['_Width'] / 2, MinSnapSpacing)]],
                [self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][1][0],
                 [self._DesignParameter['_Met4VDDRouting']['_XYCoordinates'][1][0][0],
                  self.CeilMinSnapSpacing(self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'][0][0][1] +
                  self._DesignParameter['_Met5VDDRouting']['_Width'] / 2, MinSnapSpacing)]]]

            self._DesignParameter['_AdditionalLineVDDMet6'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL6'][0],
                _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _Width=400)
            self._DesignParameter['_AdditionalLineVDDMet6']['_Width'] = self._DesignParameter['_Met6VDDRouting'][
                '_Width']
            self._DesignParameter['_AdditionalLineVDDMet6']['_XYCoordinates'] = [
                [self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0],
                 [self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0][0],
                  self.CeilMinSnapSpacing(self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'][0][0][1] +
                  self._DesignParameter['_Met5VDDRouting']['_Width'] / 2, MinSnapSpacing)]],
                [self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0],
                 [self._DesignParameter['_Met6VDDRouting']['_XYCoordinates'][0][0][0],
                  self.CeilMinSnapSpacing(self._DesignParameter['_Met5VDDRouting']['_XYCoordinates'][0][0][1] +
                  self._DesignParameter['_Met5VDDRouting']['_Width'] / 2, MinSnapSpacing)]]]

        self._DesignParameter['_PinVDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_PinVSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
            _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VSS')


        tmp1 = []
        tmp2 = []
        for i in range(0, _NumberofSlicerWithSRLatch):
            self._DesignParameter['CK<{0}>pin'.format(i)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],\
                                                           _XYCoordinates=[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Inputpin']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Inverter']['_DesignObj']._DesignParameter['_Inputpin']['_XYCoordinates'][0][1]
                                                                            - i*GuardringHeight]],
                                                           _Mag=0.5, _Angle=0, _TEXT='CLK<{0}>'.format(i))

            self._DesignParameter['OUT<{0}>pin'.format(i)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],\
                                                              _XYCoordinates=[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_OUTpin']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_OUTpin']['_XYCoordinates'][0][1]
                                                                               - i*GuardringHeight]],
                                                              _Mag=0.5, _Angle=0, _TEXT='OUT<{0}>'.format(i))

            self._DesignParameter['OUTb<{0}>pin'.format(i)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],\
                                                              _XYCoordinates=[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_OUTbpin']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_OUTbpin']['_XYCoordinates'][0][1]
                                                                               - i*GuardringHeight]],
                                                              _Mag=0.5, _Angle=0, _TEXT='OUTb<{0}>'.format(i))

            self._DesignParameter['INp<{0}>pin'.format(i)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], \
                _XYCoordinates=[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinInputP']['_XYCoordinates'][0][0],
                                 self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinInputP']['_XYCoordinates'][0][1] - i * GuardringHeight]],
                _Mag=0.5, _Angle=0, _TEXT='INp<{0}>'.format(i))

            self._DesignParameter['INn<{0}>pin'.format(i)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], \
                _XYCoordinates=[[self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinInputN']['_XYCoordinates'][0][0],
                                    self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinInputN']['_XYCoordinates'][0][1] - i * GuardringHeight]],
                _Mag=0.5, _Angle=0, _TEXT='INn<{0}>'.format(i))

            tmp1.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinVDD']['_XYCoordinates'][0][0],\
                        self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinVDD']['_XYCoordinates'][0][1] - i * GuardringHeight])
            

            tmp2.append([self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][0] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinVSS']['_XYCoordinates'][0][0],\
                        self._DesignParameter['_SlicerWithSRLatchX4']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_XYCoordinates'][0][1] + self._DesignParameter['_SlicerWithSRLatchX4']['_DesignObj']._DesignParameter['_Slicer']['_DesignObj']._DesignParameter['_PinVSS']['_XYCoordinates'][0][1] - i * GuardringHeight])
            
            
        self._DesignParameter['_PinVDD']['_XYCoordinates'] = tmp1
        self._DesignParameter['_PinVSS']['_XYCoordinates'] = tmp2
        del tmp1, tmp2








if __name__ == '__main__':
    #####################SRLatch#######################
        for _tries in range(1, 2):
            _SRFinger1 = 5#random.randint(1, 16)
            _SRFinger2 = 1#random.randint(1, 16)
            _SRFinger3 = 2#random.randint(1, 16)
            _SRFinger4 = 2#random.randint(1, 16)
            _RandChannelWidth = 350#random.randrange(200, 400, 1)
            _SRNPRatio = 2
            _SRNMOSChannelWidth1 = _RandChannelWidth
            _SRPMOSChannelWidth1 = _SRNPRatio * _RandChannelWidth
            _SRNMOSChannelWidth2 = _RandChannelWidth
            _SRPMOSChannelWidth2 = _SRNPRatio * _RandChannelWidth
            _SRNMOSChannelWidth3 = _RandChannelWidth
            _SRPMOSChannelWidth3 = _SRNPRatio * _RandChannelWidth
            _SRNMOSChannelWidth4 = _RandChannelWidth
            _SRPMOSChannelWidth4 = _SRNPRatio * _RandChannelWidth
            _SRChannelLength = 30
            _SRVDD2VSSHeightAtOneSide = None
            _SRDummy = True
            _SRNumSupplyCoX = None
            _SRNumSupplyCoY = 2
            _SRSupplyMet1XWidth = None
            _SRSupplyMet1YWidth = None
            _SRNumViaPoly2Met1CoX = None
            _SRNumViaPoly2Met1CoY = None
            _SRNumViaPMOSMet12Met2CoX = None
            _SRNumViaPMOSMet12Met2CoY = None
            _SRNumViaNMOSMet12Met2CoX = None
            _SRNumViaNMOSMet12Met2CoY = None
            _SRNumViaPMOSMet22Met3CoX = None
            _SRNumViaPMOSMet22Met3CoY = None
            _SRNumViaNMOSMet22Met3CoX = None
            _SRNumViaNMOSMet22Met3CoY = None
            _SRXVT = 'LVT'
            _SRPowerLine = None
            #####################Slicer#######################
            _SLCLKinputPMOSFinger1 = 6#random.randint(1, 16)
            _SLCLKinputPMOSFinger2 = 3#random.randint(1, 16)
            _SLPMOSFinger = 2#random.randint(1, 16)
            _SLPMOSChannelWidth = 1000#random.randrange(200, 1050, 1)
            _SLDATAinputNMOSFinger = 12#random.randint(2, 16)
            _SLNMOSFinger = 2#random.randint(1, 16)
            _SLCLKinputNMOSFinger = 8#random.randint(1, 16)
            _SLNMOSChannelWidth = 1000#random.randrange(200, 1050, 1)
            _SLCLKinputNMOSChannelWidth = 1000#random.randrange(200, 1050, 1)
            _SLChannelLength = 30
            _SLDummy = True
            _SLXVT = 'LVT'
            _SLGuardringWidth = 200
            _SLGuardring = True
            _SLSlicerGuardringWidth = 200
            _SLSlicerGuardring = None
            _SLNumSupplyCOY = None
            _SLNumSupplyCOX = None
            _SLSupplyMet1XWidth = None
            _SLSupplyMet1YWidth = None
            _SLVDD2VSSHeight = None
            _SLNumVIAPoly2Met1COX = None
            _SLNumVIAPoly2Met1COY = None
            _SLNumVIAMet12COX = None
            _SLNumVIAMet12COY = None
            _SLPowerLine = None
            _NumberofSlicerWithSRLatch = 4#random.randint(1, 16)
            #####################Inverter#######################
            _InvFinger = 6#random.randint(5, 16)
            _InvChannelWidth = 350#random.randrange(200, 400, 1)
            _InvChannelLength = 30
            _InvNPRatio = 3
            _InvVDD2VSSHeight = None
            _InvDummy = True
            _InvNumSupplyCoX = None
            _InvNumSupplyCoY = None
            _InvSupplyMet1XWidth = None
            _InvSupplyMet1YWidth = None
            _InvNumViaPoly2Met1CoX = None
            _InvNumViaPoly2Met1CoY = None
            _InvNumViaPMOSMet12Met2CoX = None
            _InvNumViaPMOSMet12Met2CoY = None
            _InvNumViaNMOSMet12Met2CoX = None
            _InvNumViaNMOSMet12Met2CoY = None
            _InvXVT = 'LVT'
            _InvPowerLine = None
            #####################Power Line#######################
            _SLSRInvSupplyLine = None
            _SLSRInvSupplyLineX4 = False

            from Private import MyInfo
            import DRCchecker

            libname = 'SlicerWithSRLatchX4'
            cellname = 'SlicerWithSRLatchX4'
            _fileName = cellname + '.gds'

            InputParams = dict(
                _SRFinger1=_SRFinger1, _SRFinger2=_SRFinger2, _SRFinger3=_SRFinger3, _SRFinger4=_SRFinger4,
                _SRNMOSChannelWidth1=_SRNMOSChannelWidth1, _SRPMOSChannelWidth1=_SRPMOSChannelWidth1,
                _SRNMOSChannelWidth2=_SRNMOSChannelWidth2, _SRPMOSChannelWidth2=_SRPMOSChannelWidth2,
                _SRNMOSChannelWidth3=_SRNMOSChannelWidth3, _SRPMOSChannelWidth3=_SRPMOSChannelWidth3,
                _SRNMOSChannelWidth4=_SRNMOSChannelWidth4, _SRPMOSChannelWidth4=_SRPMOSChannelWidth4,
                _SRChannelLength=_SRChannelLength, _SRNPRatio=_SRNPRatio,
                _SRVDD2VSSHeightAtOneSide=_SRVDD2VSSHeightAtOneSide, _SRDummy=_SRDummy, _SRNumSupplyCoX=_SRNumSupplyCoX,
                _SRNumSupplyCoY=_SRNumSupplyCoY,
                _SRSupplyMet1XWidth=_SRSupplyMet1XWidth, _SRSupplyMet1YWidth=_SRSupplyMet1YWidth,
                _SRNumViaPoly2Met1CoX=_SRNumViaPoly2Met1CoX, \
                _SRNumViaPoly2Met1CoY=_SRNumViaPoly2Met1CoY, _SRNumViaPMOSMet12Met2CoX=_SRNumViaPMOSMet12Met2CoX,
                _SRNumViaPMOSMet12Met2CoY=_SRNumViaPMOSMet12Met2CoY,
                _SRNumViaNMOSMet12Met2CoX=_SRNumViaNMOSMet12Met2CoX, _SRNumViaNMOSMet12Met2CoY=_SRNumViaNMOSMet12Met2CoY,
                _SRNumViaPMOSMet22Met3CoX=_SRNumViaPMOSMet22Met3CoX, _SRNumViaPMOSMet22Met3CoY=_SRNumViaPMOSMet22Met3CoY,
                _SRNumViaNMOSMet22Met3CoX=_SRNumViaNMOSMet22Met3CoX, _SRNumViaNMOSMet22Met3CoY=_SRNumViaNMOSMet22Met3CoY,
                _SRXVT=_SRXVT, _SRPowerLine=_SRPowerLine,
                _SLCLKinputPMOSFinger1=_SLCLKinputPMOSFinger1, _SLCLKinputPMOSFinger2=_SLCLKinputPMOSFinger2,
                _SLPMOSFinger=_SLPMOSFinger, _SLPMOSChannelWidth=_SLPMOSChannelWidth,
                _SLDATAinputNMOSFinger=_SLDATAinputNMOSFinger, _SLNMOSFinger=_SLNMOSFinger,
                _SLCLKinputNMOSFinger=_SLCLKinputNMOSFinger, _SLNMOSChannelWidth=_SLNMOSChannelWidth,
                _SLCLKinputNMOSChannelWidth=_SLCLKinputNMOSChannelWidth,
                _SLChannelLength=_SLChannelLength, _SLDummy=_SLDummy, _SLXVT=_SLXVT, _SLGuardringWidth=_SLGuardringWidth,
                _SLGuardring=_SLGuardring,
                _SLSlicerGuardringWidth=_SLSlicerGuardringWidth, _SLSlicerGuardring=_SLSlicerGuardring,
                _SLNumSupplyCOY=_SLNumSupplyCOY, _SLNumSupplyCOX=_SLNumSupplyCOX, _SLSupplyMet1XWidth=_SLSupplyMet1XWidth,
                _SLSupplyMet1YWidth=_SLSupplyMet1YWidth, _SLVDD2VSSHeight=_SLVDD2VSSHeight,
                _SLNumVIAPoly2Met1COX=_SLNumVIAPoly2Met1COX, _SLNumVIAPoly2Met1COY=_SLNumVIAPoly2Met1COY,
                _SLNumVIAMet12COX=_SLNumVIAMet12COX, _SLNumVIAMet12COY=_SLNumVIAMet12COY, _SLPowerLine=_SLPowerLine, \
                _InvFinger=_InvFinger, _InvChannelWidth=_InvChannelWidth, _InvChannelLength=_InvChannelLength,
                _InvNPRatio=_InvNPRatio,
                _InvVDD2VSSHeight=_InvVDD2VSSHeight, _InvDummy=_InvDummy, _InvNumSupplyCoX=_InvNumSupplyCoX,
                _InvNumSupplyCoY=_InvNumSupplyCoY, _InvSupplyMet1XWidth=_InvSupplyMet1XWidth,
                _InvSupplyMet1YWidth=_InvSupplyMet1YWidth, _InvNumViaPoly2Met1CoX=_InvNumViaPoly2Met1CoX, \
                _InvNumViaPoly2Met1CoY=_InvNumViaPoly2Met1CoY, _InvNumViaPMOSMet12Met2CoX=_InvNumViaPMOSMet12Met2CoX,
                _InvNumViaPMOSMet12Met2CoY=_InvNumViaPMOSMet12Met2CoY,
                _InvNumViaNMOSMet12Met2CoX=_InvNumViaNMOSMet12Met2CoX, \
                _InvNumViaNMOSMet12Met2CoY=_InvNumViaNMOSMet12Met2CoY, _InvXVT=_InvXVT, _InvPowerLine=_InvPowerLine,
                _SLSRInvSupplyLineX4=_SLSRInvSupplyLineX4, _NumberofSlicerWithSRLatch=_NumberofSlicerWithSRLatch
            )
            LayoutObj = _SlicerWithSRLatchX4(_DesignParameter=None, _Name=cellname)
            LayoutObj._CalculateDesignParameter(**InputParams)
            LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
            testStreamFile = open('./{}'.format(_fileName), 'wb')
            tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
            tmp.write_binary_gds_stream(testStreamFile)
            testStreamFile.close()

            print('#############################      Sending to FTP Server...      #############################')
            My = MyInfo.USER(DesignParameters._Technology)
            Checker = DRCchecker.DRCchecker(
                username=My.ID,
                password=My.PW,
                WorkDir=My.Dir_Work,
                DRCrunDir=My.Dir_DRCrun,
                libname=libname,
                cellname=cellname,
                GDSDir=My.Dir_GDS
            )
            Checker.Upload2FTP()
            Checker.StreamIn(tech=DesignParameters._Technology)

        #     import ftplib
        #
        #     ftp = ftplib.FTP('141.223.29.62'
        #     ftp.login('jicho0927', 'cho89140616!!')
        #     ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
        #     myfile = open('SlicerWithSRLatchX4.gds', 'rb')
        #     ftp.storbinary('STOR SlicerWithSRLatchX4.gds', myfile)
        #     myfile.close()
        #
        #     import DRCchecker
        #
        #     a = DRCchecker.DRCchecker('jicho0927', 'cho89140616!!', '/mnt/sdc/jicho0927/OPUS/SAMSUNG28n', '/mnt/sdc/jicho0927/OPUS/SAMSUNG28n/DRC/run', 'SlicerWithSRLatchX4', 'SlicerWithSRLatchX4', None)
        #     a.DRCchecker()
        #
        # print("DRC Clean!!!")

        #     import ftplib
        #
        #     ftp = ftplib.FTP('141.223.29.62')
        #     ftp.login('jicho0927', 'cho89140616!!')
        #     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc65n')
        #     myfile = open('SlicerWithSRLatchX4.gds', 'rb')
        #     ftp.storbinary('STOR SlicerWithSRLatchX4.gds', myfile)
        #     myfile.close()
        #
        #     import DRCchecker
        #     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc65n','/mnt/sdc/jicho0927/OPUS/tsmc65n/DRC/run','SlicerWithSRLatchX4','SlicerWithSRLatchX4',None)
        #     a.DRCchecker()
        #
        # print ("DRC Clean!!!")

        #     import ftplib
        #
        #     ftp = ftplib.FTP('141.223.29.62')
        #     ftp.login('jicho0927', 'cho89140616!!')
        #     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc40n')
        #     myfile = open('SlicerWithSRLatchX4.gds', 'rb')
        #     ftp.storbinary('STOR SlicerWithSRLatchX4.gds', myfile)
        #     myfile.close()
        #
        #     import DRCchecker
        #
        #     a = DRCchecker.DRCchecker('jicho0927', 'cho89140616!!', '/mnt/sdc/jicho0927/OPUS/tsmc40n', '/mnt/sdc/jicho0927/OPUS/tsmc40n/DRC/run', 'SlicerWithSRLatchX4', 'SlicerWithSRLatchX4', None)
        #     a.DRCchecker()
        #
        # print("DRC Clean!!!")

        #     import ftplib
        #
        #     ftp = ftplib.FTP('141.223.29.62')
        #     ftp.login('jicho0927', 'cho89140616!!')
        #     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc90n')
        #     myfile = open('SlicerWithSRLatchX4.gds', 'rb')
        #     ftp.storbinary('STOR SlicerWithSRLatchX4.gds', myfile)
        #     myfile.close()
        #
        #     import DRCchecker
        #     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc90n','/mnt/sdc/jicho0927/OPUS/tsmc90n/DRC/run','SlicerWithSRLatchX4','SlicerWithSRLatchX4',None)
        #     a.DRCchecker()
        #
        #
        # print ("DRC Clean!!!")


