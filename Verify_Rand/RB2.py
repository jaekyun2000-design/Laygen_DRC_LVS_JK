import StickDiagram
import DesignParameters
import copy
import DRC
import NMOS
import PMOS
import NbodyContact
import PbodyContact
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import ViaMet72Met8
import ftplib
import TG2
import opppcres_b
import psubring
import Rppolywo

class _ResistorBank(StickDiagram._StickDiagram) :
    _ParametersForDesignCalculation = dict(
                                           _TransmissionGateFinger = None, _TransmissionGateChannelWidth = None, _TransmissionGateChannelLength = None, _TransmissionGateNPRatio = None,
                                           _TransmissionGateVDD2VSSHeight = None,
                                           _PowerLine = False,
                                           _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None,_ResistorMetYCO=None,
                                           _PMOSSubringType=True, _PMOSSubringXWidth=None, _PMOSSubringYWidth=None,
                                           _PMOSSubringWidth=None,
                                           _NMOSSubringType=True, _NMOSSubringXWidth=None, _NMOSSubringYWidth=None,
                                           _NMOSSubringWidth=None,
                                           _TotalSubringType=True, _TotalSubringXWidth=None, _TotalSubringYWidth=None,
                                           _TotalSubringWidth=None)

    def __init__(self, _DesignParameter=None, _Name='ResistorBank'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),_GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name == None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateResistorBank(self,
                               # _InverterFinger=None, _InverterChannelWidth=None, _InverterChannelLength=None, _InverterNPRatio=None, _InverterDummy = False,
                               # _InverterVDD2VSSHeight=None, _InverterSLVT = False,
                               # _InverterNumSupplyCOX = None, _InverterNumSupplyCOY = None,
                               # _InverterSupplyMet1XWidth = None, _InverterSupplMet1YWidth = None, _InverterNumVIAPoly2Met1COX = None, _InverterNumVIAPoly2Met1COY = None,
                               # _InverterNumVIAMet12COX = None, _InverterNumVIAMet12COY = None,
                               _TransmissionGateFinger = None, _TransmissionGateChannelWidth = None, _TransmissionGateChannelLength = None, _TransmissionGateNPRatio = None,
                               _TransmissionGateDummy = False , _TransmissionGateVDD2VSSHeight = None, _TransmissionGateXVT = None,
                               _PowerLine = False,
                               # _TransmissionGateNumSupplyCOX = None, _TransmissionGateNumSupplyCOY = None, _TransmissionGateSupplyMet1XWidth = None, _TransmissionGateSupplyMet1YWidth = None,
                               # _TransmissionGateNumVIAPoly2Met1COX = None, _TransmissionGateNumVIAPoly2Met1COY = None, _TransmissionGateNumVIAMet12COX = None, _TransmissionGateNumVIAMet12COY = None,
                               _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None, _ResistorMetYCO=None,
                               _PMOSSubringType = True, _PMOSSubringXWidth = None, _PMOSSubringYWidth = None, _PMOSSubringWidth = None,
                               _NMOSSubringType = True, _NMOSSubringXWidth = None, _NMOSSubringYWidth = None, _NMOSSubringWidth = None,
                               _TotalSubringType = True, _TotalSubringXWidth = None, _TotalSubringYWidth = None, _TotalSubringWidth = None):

        print ('#########################################################################################################')
        print ('                                {}  ResistorBank Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = 'ResistorBank'
        _MinSnapSpacing = _DRCObj._MinSnapSpacing

        if DesignParameters._Technology == '028nm' :
            _viaspacing = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace
        else :
            _viaspacing = 0


        # print '###############################     Inverter Generation    ##############################################'
        # _Inverterinputs = copy.deepcopy(Inverter._Inverter._ParametersForDesignCalculation)
        # _Inverterinputs['_Finger'] = _InverterFinger
        # _Inverterinputs['_ChannelWidth'] = _InverterChannelWidth
        # _Inverterinputs['_ChannelLength'] = _InverterChannelLength
        # _Inverterinputs['_NPRatio'] = _InverterNPRatio
        # _Inverterinputs['_Dummy'] = _InverterDummy
        # _Inverterinputs['_VDD2VSSHeight'] = _InverterVDD2VSSHeight
        # _Inverterinputs['_SLVT'] = _InverterSLVT
        # _Inverterinputs['_SupplyMet1YWidth'] = _NMOSSubringWidth
        #
        # self._DesignParameter['_InverterRB'] = self._SrefElementDeclaration(_DesignObj=Inverter._Inverter(_DesignParameter=None, _Name='InverterIn{}'.format(_Name)))[0]
        # self._DesignParameter['_InverterRB']['_DesignObj']._CalculateInverter(**_Inverterinputs)

        if _TransmissionGateVDD2VSSHeight == None :
            det = 0
        else :
            det = 1

        while det != 2 :

            print ('##############################     TransmissionGate Generation    ########################################')
            _TransmissionGateinputs = copy.deepcopy(TG2._TransmissionGate._ParametersForDesignCalculation)
            _TransmissionGateinputs['_Finger'] = _TransmissionGateFinger
            _TransmissionGateinputs['_ChannelWidth'] = _TransmissionGateChannelWidth
            _TransmissionGateinputs['_ChannelLength'] = _TransmissionGateChannelLength
            _TransmissionGateinputs['_NPRatio'] = _TransmissionGateNPRatio
            _TransmissionGateinputs['_Dummy'] = _TransmissionGateDummy
            _TransmissionGateinputs['_VDD2VSSHeight'] = _TransmissionGateVDD2VSSHeight
            _TransmissionGateinputs['_XVT'] = _TransmissionGateXVT
            _TransmissionGateinputs['_SupplyMet1YWidth'] = _NMOSSubringWidth
            _TransmissionGateinputs['_Gatereverse'] = False
            _TransmissionGateinputs['_Bodycontact'] = False

            self._DesignParameter['_TransmissionGateRB'] = self._SrefElementDeclaration(_DesignObj=TG2._TransmissionGate(_DesignParameter=None, _Name = 'TransmissionGateIn{}'.format(_Name)))[0]
            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._CalculateTransmissionGate(**_TransmissionGateinputs)

            if _TransmissionGateVDD2VSSHeight == None :
                _TransmissionGateVDD2VSSHeight = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_VDD2VSSMinHeight']['_Ignore']
                print ('############################       Via for Digital input Generation       ################################')
                _ViaInputMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
                _ViaInputMet12Met2['_ViaMet12Met2NumberOfCOX'] = 2
                _ViaInputMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1

                self._DesignParameter['_ViaMet12Met2OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaInputMet12Met2)
                self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'] = []

                _ViaInputMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
                _ViaInputMet22Met3['_ViaMet22Met3NumberOfCOX'] = 2
                _ViaInputMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1

                self._DesignParameter['_ViaMet22Met3OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet22Met3OnInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaInputMet22Met3)
                self._DesignParameter['_ViaMet22Met3OnInput']['_XYCoordinates'] = []

                _ViaInputMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
                _ViaInputMet32Met4['_ViaMet32Met4NumberOfCOX'] = 2
                _ViaInputMet32Met4['_ViaMet32Met4NumberOfCOY'] = 1

                self._DesignParameter['_ViaMet32Met4OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met4OnInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet32Met4OnInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaInputMet32Met4)
                self._DesignParameter['_ViaMet32Met4OnInput']['_XYCoordinates'] = []

                _ViaInputMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
                _ViaInputMet42Met5['_ViaMet42Met5NumberOfCOX'] = 2
                _ViaInputMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1

                self._DesignParameter['_ViaMet42Met5OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnInputIn{}'.format(_Name)))[0]
                self._DesignParameter['_ViaMet42Met5OnInput']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaInputMet42Met5)
                self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'] = []

                if (DesignParameters._Technology == '028nm') :
                    print ('###############################       Opppcres_b Generation      #########################################')
                    _Opppcresinputs = copy.deepcopy(opppcres_b._Opppcres._ParametersForDesignCalculation)
                    _Opppcresinputs['_ResWidth'] = _ResistorWidth
                    _Opppcresinputs['_ResLength'] = _ResistorLength
                    _Opppcresinputs['_CONUMX'] = _ResistorMetXCO
                    _Opppcresinputs['_CONUMY'] = _ResistorMetYCO
                    self._DesignParameter['_OpppcresRB'] = self._SrefElementDeclaration(_DesignObj=opppcres_b._Opppcres(_DesignParameter=None, _Name = 'OpppcresIn{}'.format(_Name)))[0]
                    self._DesignParameter['_OpppcresRB']['_DesignObj']._CalculateOpppcresDesignParameter(**_Opppcresinputs)

                else :
                    print ('      Rppolywo Generation      '.center(105,'#'))
                    _Opppcresinputs = copy.deepcopy(Rppolywo._RPPOLYWOSegment._ParametersForDesignCalculation)
                    _Opppcresinputs['_ResXWidth'] = _ResistorWidth
                    _Opppcresinputs['_ResYWidth'] = _ResistorLength
                    _Opppcresinputs['_NumberOfCOY'] = _ResistorMetYCO
                    self._DesignParameter['_OpppcresRB'] = self._SrefElementDeclaration(_DesignObj=Rppolywo._RPPOLYWOSegment(_DesignParameter=None, _Name = 'RppolywoIn{}'.format(_Name)))[0]
                    self._DesignParameter['_OpppcresRB']['_DesignObj']._CalculateDesignParameter(**_Opppcresinputs)

                


                print ('#################################       PSubring Generation      #########################################')
                _PMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
                _PMOSSubringinputs['_PType'] = False
                _PMOSSubringinputs['_Width'] = _PMOSSubringWidth
                #if (_TransmissionGateFinger % 2 )
                if DesignParameters._Technology != '028nm' : ## for tsmc process
                    _PMOSSubringinputs['_XWidth'] = self.CeilMinSnapSpacing((max(((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                                (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                                - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] 
                                                + _DRCObj.DRCMETAL1MinSpace(self.getXWidth('_TransmissionGateRB','_PMOSTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_PMOSTG','_Met1Layer'), _PMOSSubringinputs['_Width']) * 2),
                                                self.getXWidth('_TransmissionGateRB','_PMOSTG','_PPLayer') + _DRCObj._NpMinExtensiononNactive2 * 2  + _DRCObj._PpMinEnclosureOfPo * 2) // 2 + \
                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                                self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                                                + _DRCObj.DRCMETAL1MinSpace(self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnPMOSControlTG','_Met1Layer'),self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnPMOSControlTG','_Met1Layer'),_PMOSSubringinputs['_Width']) + _DRCObj._MetalxMinSpace2), 2*_MinSnapSpacing)

                else :
                    _PMOSSubringinputs['_XWidth'] = ((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                                (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                                - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace3 * 2) // 2 + \
                                                (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                                self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace2 + _DRCObj._Metal1MinSpace3)

                #if DesignParameters._Technology == '028nm' :
                if (_TransmissionGateFinger == 1 and DesignParameters._Technology == '028nm') :
                    _PMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 + _DRCObj._MetalxMinSpace8 + _DRCObj._Metal1MinSpace3 +\
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                                    max((_viaspacing) // 2 + 
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])

                else :
                    _PMOSSubringinputs['_YWidth'] = (max(_DRCObj.DRCMETAL1MinSpace(_PMOSSubringinputs['_Width'] ,self.getXWidth('_TransmissionGateRB', '_ViaPoly2Met1OnPMOSControlTG','_Met1Layer'),self.getYWidth('_TransmissionGateRB', '_ViaPoly2Met1OnPMOSControlTG','_Met1Layer')),
                                                    _DRCObj._PpMinEnclosureOfPo + _DRCObj._NpMinExtensiononNactive2)+
                                                    _DRCObj.DRCMETAL1MinSpace(self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnPMOSControlTG','_Met1Layer'),self.getXWidth('_TransmissionGateRB', '_PMOSTG','_Met1Layer'),self.getXWidth('_TransmissionGateRB','_PMOSTG','_Met1Layer'))+
                                                    _DRCObj._Metal1MinSpacetoGate +
                                                    max(_DRCObj._Metal1DefaultSpace, 
                                                    _DRCObj.DRCMETALxMinSpace(self.getYWidth('_TransmissionGateRB', '_ViaMet22Met3OnPMOSOutputTG', '_Met3Layer'), _PMOSSubringinputs['_XWidth'],_PMOSSubringinputs['_Width'])) +
                                                    #self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +\
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                                    max((_viaspacing) // 2 + 
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))

                _TransmissionGateinputs['_MOStoSupply'] = max(_DRCObj.DRCMETALxMinSpace(self.getYWidth('_TransmissionGateRB', '_ViaMet22Met3OnPMOSOutputTG', '_Met3Layer'), _PMOSSubringinputs['_XWidth'],_PMOSSubringinputs['_Width']), _DRCObj._Metal1DefaultSpace)
                self._DesignParameter['_TransmissionGateRB'] = self._SrefElementDeclaration(_DesignObj=TG2._TransmissionGate(_DesignParameter=None, _Name = 'TransmissionGateIn{}'.format(_Name)))[0]
                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._CalculateTransmissionGate(**_TransmissionGateinputs)
                

                self._DesignParameter['_PMOSSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name = 'PMOSSubringIn{}'.format(_Name)))[0]
                self._DesignParameter['_PMOSSubringRB']['_DesignObj']._CalculatePSubring(**_PMOSSubringinputs)

                _NMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
                _NMOSSubringinputs['_PType'] = True
                _NMOSSubringinputs['_Width'] = _NMOSSubringWidth
                #if DesignParameters._Technology == '028nm' :
                # _NMOSSubringinputs['_XWidth'] = self.CeilMinSnapSpacing((max(((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                #                                  self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                #                                 (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0]
                #                                  - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                #                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] 
                #                                 + _DRCObj.DRCMETAL1MinSpace(self.getXWidth('_TransmissionGateRB','_NMOSTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_NMOSTG','_Met1Layer'), _NMOSSubringinputs['_Width']) * 2),
                #                                 self.getXWidth('_TransmissionGateRB','_NMOSTG','_NPLayer') + _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._NpMinEnclosureOfPo * 2)// 2 + \
                #                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                #                                 self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] 
                #                                 + _DRCObj._Metal1MinSpace2 * 2
                #                                 + _DRCObj.DRCMETAL1MinSpace(self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnNMOSControlTG','_Met1Layer'),self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnNMOSControlTG','_Met1Layer'),_NMOSSubringinputs['_Width']) * 2), 2*_MinSnapSpacing)
                
                _NMOSSubringinputs['_XWidth'] = _PMOSSubringinputs['_XWidth']

                # else :
                #     _NMOSSubringinputs['_XWidth'] = self.getXWidth('_TransmissionGateRB', '_NMOSTG', '_NPLayer') + 2 * _DRCObj._NpMinExtensiononNactive
                
                
                #if DesignParameters._Technology == '028nm' :
                if (_TransmissionGateFinger == 1 and DesignParameters._Technology == '028nm') :
                    _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 * 3 + \
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                                    max((_viaspacing) // 2 + 
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) 
                #     _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 * 3 +\
                #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
                #                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 +\
                #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
                else :
                    _NMOSSubringinputs['_YWidth'] = (_DRCObj._Metal1DefaultSpace +
                                                _DRCObj.DRCMETAL1MinSpace(self.getXWidth('_TransmissionGateRB','_NMOSTG','_Met1Layer'), self.getXWidth('_TransmissionGateRB','_NMOSTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnPMOSControlTG','_Met1Layer')) +\
                                                _DRCObj._Metal1MinSpacetoGate +
                                                max(_DRCObj.DRCMETAL1MinSpace(_NMOSSubringinputs['_Width'], self.getXWidth('_TransmissionGateRB','_ViaPoly2Met1OnNMOSControlTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnNMOSControlTG','_Met1Layer')),
                                                _DRCObj._NpMinEnclosureOfPo + _DRCObj._NpMinExtensiononNactive2)+
                                                #self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +\
                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                                max((_viaspacing) // 2 + 
                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))

                
                self._DesignParameter['_NMOSSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='NMOSSubringIn{}'.format(_Name)))[0]
                self._DesignParameter['_NMOSSubringRB']['_DesignObj']._CalculatePSubring(**_NMOSSubringinputs)

                _TotalSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
                _TotalSubringinputs['_PType'] = True
                _TotalSubringinputs['_Width'] = _TotalSubringWidth

                if DesignParameters._Technology == '028nm' :
                    _TotalSubringinputs['_XWidth'] =_NMOSSubringinputs['_XWidth'] + (_NMOSSubringinputs['_Width']+1) * 2 + _DRCObj._PpMinExtensiononPactive2 * 2+ \
                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + \
                                                    _DRCObj._RXMinSpacetoPRES * 2 + _DRCObj._PpMinSpace + 90

                    _TotalSubringinputs['_YWidth'] = max(_TransmissionGateVDD2VSSHeight + _NMOSSubringinputs['_Width'] +\
                                                        + _DRCObj._Metal1MinSpace3 + _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace,
                                                        self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] + _DRCObj._RXMinSpacetoPRES * 2)

                else :
                    _TotalSubringinputs['_XWidth'] =_NMOSSubringinputs['_XWidth'] + (_NMOSSubringinputs['_Width']) * 2 + _DRCObj._PpMinExtensiononPactive2 * 4 + _DRCObj._NwMinSpacetoPactive + _DRCObj._NwMinEnclosurePactive + \
                                                    max(_DRCObj._RPOMinSpace2OD * 2 , 
                                                    _DRCObj.DRCMETAL1MinSpace(_TransmissionGateChannelWidth * _TransmissionGateNPRatio, _TransmissionGateChannelWidth * _TransmissionGateNPRatio, _TotalSubringWidth) * 2 - _DRCObj._RPOMinExtensionOnPO * 2) \
                                                    + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_RPOLayer']['_XWidth']

                    _TotalSubringinputs['_YWidth'] = max(_TransmissionGateVDD2VSSHeight + _NMOSSubringinputs['_Width'] +\
                                                    +  max(_DRCObj._NwMinSpacetoPactive + _DRCObj._NwMinEnclosureNactive + _DRCObj._NpMinExtensiononNactive2 +  _DRCObj._PpMinExtensiononPactive2 , _DRCObj._PpMinSpace +  _DRCObj._PpMinExtensiononPactive2 +  _DRCObj._PpMinExtensiononPactive2) * 2,
                                                        self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + _DRCObj._PpMinSpace * 2 + _DRCObj._PpMinExtensiononPactive2 * 2,
                                                        self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] +
                                                        _DRCObj.DRCMETAL1MinSpace(_TotalSubringWidth, _ResistorWidth, self.getXWidth('_OpppcresRB','_Met1Layer') * 2 - _DRCObj._PpMinEnclosureOfPo * 2 + _DRCObj._Metal1MinEnclosureCO2 * 2))


                self._DesignParameter['_TotalSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='TotalSubringIn{}'.format(_Name)))[0]
                self._DesignParameter['_TotalSubringRB']['_DesignObj']._CalculatePSubring(**_TotalSubringinputs)


                print ('#################################       Coordinates Settings      ########################################')


                self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'] = [[0,0]]

                _VDD2VSSMinHeight = max(_NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_YWidth'] + max(_DRCObj.DRCMETAL1MinSpace(_NMOSSubringinputs['_Width'], _NMOSSubringinputs['_XWidth'] + _NMOSSubringinputs['_Width'] * 2 , _PMOSSubringinputs['_Width']) + _NMOSSubringinputs['_Width'],
                                        self.getWidth('_PMOSSubringRB','_NWLayer') * 0.5 + self.getWidth('_NMOSSubringRB','_PPLayer') * 0.5 + _DRCObj._NwMinSpacetoPactive)
                                        + _PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_YWidth'],
                                        abs(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] - self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]))

                if _VDD2VSSMinHeight % (2 * _MinSnapSpacing) != 0 :
                    _VDD2VSSMinHeight = self.CeilMinSnapSpacing(_VDD2VSSMinHeight, 2 * _MinSnapSpacing)

                print ('@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@# SET MINIMUM HEIGHT VALUE FOR RESISTOR BANK : ', _VDD2VSSMinHeight)

                if _TransmissionGateVDD2VSSHeight < _VDD2VSSMinHeight :
                    _TransmissionGateVDD2VSSHeight = _VDD2VSSMinHeight

                if _TransmissionGateVDD2VSSHeight == None :
                    _TransmissionGateVDD2VSSHeight = _VDD2VSSMinHeight
                det += 1

            else :
                det += 1


        print ('############################       Via for Digital input Generation       ################################')
        _ViaInputMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaInputMet12Met2['_ViaMet12Met2NumberOfCOX'] = 2
        _ViaInputMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet12Met2OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaInputMet12Met2)
        self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'] = []

        _ViaInputMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaInputMet22Met3['_ViaMet22Met3NumberOfCOX'] = 2
        _ViaInputMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet22Met3OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaInputMet22Met3)
        self._DesignParameter['_ViaMet22Met3OnInput']['_XYCoordinates'] = []

        _ViaInputMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaInputMet32Met4['_ViaMet32Met4NumberOfCOX'] = 2
        _ViaInputMet32Met4['_ViaMet32Met4NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet32Met4OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met4OnInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnInput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaInputMet32Met4)
        self._DesignParameter['_ViaMet32Met4OnInput']['_XYCoordinates'] = []

        _ViaInputMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaInputMet42Met5['_ViaMet42Met5NumberOfCOX'] = 2
        _ViaInputMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1

        self._DesignParameter['_ViaMet42Met5OnInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnInputIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnInput']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaInputMet42Met5)
        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'] = []

        if (DesignParameters._Technology == '028nm') :
            print ('###############################       Opppcres_b Generation      #########################################')
            _Opppcresinputs = copy.deepcopy(opppcres_b._Opppcres._ParametersForDesignCalculation)
            _Opppcresinputs['_ResWidth'] = _ResistorWidth
            _Opppcresinputs['_ResLength'] = _ResistorLength
            _Opppcresinputs['_CONUMX'] = _ResistorMetXCO
            _Opppcresinputs['_CONUMY'] = _ResistorMetYCO
            self._DesignParameter['_OpppcresRB'] = self._SrefElementDeclaration(_DesignObj=opppcres_b._Opppcres(_DesignParameter=None, _Name = 'OpppcresIn{}'.format(_Name)))[0]
            self._DesignParameter['_OpppcresRB']['_DesignObj']._CalculateOpppcresDesignParameter(**_Opppcresinputs)

        else :
            print ('      Rppolywo Generation      '.center(105,'#'))
            _Opppcresinputs = copy.deepcopy(Rppolywo._RPPOLYWOSegment._ParametersForDesignCalculation)
            _Opppcresinputs['_ResXWidth'] = _ResistorWidth
            _Opppcresinputs['_ResYWidth'] = _ResistorLength
            _Opppcresinputs['_NumberOfCOY'] = _ResistorMetYCO
            self._DesignParameter['_OpppcresRB'] = self._SrefElementDeclaration(_DesignObj=Rppolywo._RPPOLYWOSegment(_DesignParameter=None, _Name = 'RppolywoIn{}'.format(_Name)))[0]
            self._DesignParameter['_OpppcresRB']['_DesignObj']._CalculateDesignParameter(**_Opppcresinputs)

        


        print ('#################################       PSubring Generation      #########################################')
        _PMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _PMOSSubringinputs['_PType'] = False
        _PMOSSubringinputs['_Width'] = _PMOSSubringWidth
        #if (_TransmissionGateFinger % 2 )
        if DesignParameters._Technology != '028nm' : ## for tsmc process
            _PMOSSubringinputs['_XWidth'] = self.CeilMinSnapSpacing((max(((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] 
                                        + _DRCObj.DRCMETAL1MinSpace(self.getXWidth('_TransmissionGateRB','_PMOSTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_PMOSTG','_Met1Layer'), _PMOSSubringinputs['_Width']) * 2),
                                        self.getXWidth('_TransmissionGateRB','_PMOSTG','_PPLayer') + _DRCObj._NpMinExtensiononNactive2 * 2  + _DRCObj._PpMinEnclosureOfPo * 2) // 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
                                        + _DRCObj.DRCMETAL1MinSpace(self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnPMOSControlTG','_Met1Layer'),self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnPMOSControlTG','_Met1Layer'),_PMOSSubringinputs['_Width']) + _DRCObj._MetalxMinSpace2), 2*_MinSnapSpacing)

        else :
            _PMOSSubringinputs['_XWidth'] = ((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace3 * 2) // 2 + \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace2 + _DRCObj._Metal1MinSpace3)

        #if DesignParameters._Technology == '028nm' :
        if (_TransmissionGateFinger == 1 and DesignParameters._Technology == '028nm') :
            _PMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 + _DRCObj._MetalxMinSpace8 + _DRCObj._Metal1MinSpace3 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                            max((_viaspacing) // 2 + 
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])

        else :
            _PMOSSubringinputs['_YWidth'] = (max(_DRCObj.DRCMETAL1MinSpace(_PMOSSubringinputs['_Width'] ,self.getXWidth('_TransmissionGateRB', '_ViaPoly2Met1OnPMOSControlTG','_Met1Layer'),self.getYWidth('_TransmissionGateRB', '_ViaPoly2Met1OnPMOSControlTG','_Met1Layer')),
                                            _DRCObj._PpMinEnclosureOfPo + _DRCObj._NpMinExtensiononNactive2)+
                                             _DRCObj.DRCMETAL1MinSpace(self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnPMOSControlTG','_Met1Layer'),self.getXWidth('_TransmissionGateRB', '_PMOSTG','_Met1Layer'),self.getXWidth('_TransmissionGateRB','_PMOSTG','_Met1Layer'))+
                                             _DRCObj._Metal1MinSpacetoGate +
                                             max(_DRCObj._Metal1DefaultSpace, 
                                             _DRCObj.DRCMETALxMinSpace(self.getYWidth('_TransmissionGateRB', '_ViaMet22Met3OnPMOSOutputTG', '_Met3Layer'), _PMOSSubringinputs['_XWidth'],_PMOSSubringinputs['_Width'])) +
                                            #self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +\
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                            max((_viaspacing) // 2 + 
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))

        _TransmissionGateinputs['_MOStoSupply'] = max(_DRCObj.DRCMETALxMinSpace(self.getYWidth('_TransmissionGateRB', '_ViaMet22Met3OnPMOSOutputTG', '_Met3Layer'), _PMOSSubringinputs['_XWidth'],_PMOSSubringinputs['_Width']), _DRCObj._Metal1DefaultSpace)
        self._DesignParameter['_TransmissionGateRB'] = self._SrefElementDeclaration(_DesignObj=TG2._TransmissionGate(_DesignParameter=None, _Name = 'TransmissionGateIn{}'.format(_Name)))[0]
        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._CalculateTransmissionGate(**_TransmissionGateinputs)
        

        self._DesignParameter['_PMOSSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name = 'PMOSSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_PMOSSubringRB']['_DesignObj']._CalculatePSubring(**_PMOSSubringinputs)

        _NMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _NMOSSubringinputs['_PType'] = True
        _NMOSSubringinputs['_Width'] = _NMOSSubringWidth
        #if DesignParameters._Technology == '028nm' :
        # _NMOSSubringinputs['_XWidth'] = self.CeilMinSnapSpacing((max(((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
        #                                  self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
        #                                 (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0]
        #                                  - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
        #                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] 
        #                                 + _DRCObj.DRCMETAL1MinSpace(self.getXWidth('_TransmissionGateRB','_NMOSTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_NMOSTG','_Met1Layer'), _NMOSSubringinputs['_Width']) * 2),
        #                                 self.getXWidth('_TransmissionGateRB','_NMOSTG','_NPLayer') + _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._NpMinEnclosureOfPo * 2)// 2 + \
        #                                 self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
        #                                 self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] 
        #                                 + _DRCObj._Metal1MinSpace2 * 2
        #                                 + _DRCObj.DRCMETAL1MinSpace(self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnNMOSControlTG','_Met1Layer'),self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnNMOSControlTG','_Met1Layer'),_NMOSSubringinputs['_Width']) * 2), 2*_MinSnapSpacing)
        
        _NMOSSubringinputs['_XWidth'] = _PMOSSubringinputs['_XWidth']

        # else :
        #     _NMOSSubringinputs['_XWidth'] = self.getXWidth('_TransmissionGateRB', '_NMOSTG', '_NPLayer') + 2 * _DRCObj._NpMinExtensiononNactive
        
        
        #if DesignParameters._Technology == '028nm' :
        if (_TransmissionGateFinger == 1 and DesignParameters._Technology == '028nm') :
            _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 * 3 + \
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                            max((_viaspacing) // 2 + 
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) 
        #     _NMOSSubringinputs['_YWidth'] = _DRCObj._Metal1MinSpace3 * 3 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] +\
        #                                     (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) // 4 +\
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
        #                                     self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        else :
            _NMOSSubringinputs['_YWidth'] = (_DRCObj._Metal1DefaultSpace +
                                        _DRCObj.DRCMETAL1MinSpace(self.getXWidth('_TransmissionGateRB','_NMOSTG','_Met1Layer'), self.getXWidth('_TransmissionGateRB','_NMOSTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnPMOSControlTG','_Met1Layer')) +\
                                        _DRCObj._Metal1MinSpacetoGate +
                                        max(_DRCObj.DRCMETAL1MinSpace(_NMOSSubringinputs['_Width'], self.getXWidth('_TransmissionGateRB','_ViaPoly2Met1OnNMOSControlTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_ViaPoly2Met1OnNMOSControlTG','_Met1Layer')),
                                        _DRCObj._NpMinEnclosureOfPo + _DRCObj._NpMinExtensiononNactive2)+
                                        #self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 +\
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + \
                                        max((_viaspacing) // 2 + 
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))

        
        self._DesignParameter['_NMOSSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='NMOSSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_NMOSSubringRB']['_DesignObj']._CalculatePSubring(**_NMOSSubringinputs)

        _TotalSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
        _TotalSubringinputs['_PType'] = True
        _TotalSubringinputs['_Width'] = _TotalSubringWidth

        if DesignParameters._Technology == '028nm' :
            _TotalSubringinputs['_XWidth'] =_NMOSSubringinputs['_XWidth'] + (_NMOSSubringinputs['_Width']+1) * 2 + _DRCObj._PpMinExtensiononPactive2 * 2+ \
                                            self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + \
                                            _DRCObj._RXMinSpacetoPRES * 2 + _DRCObj._PpMinSpace + 90

            _TotalSubringinputs['_YWidth'] = max(_TransmissionGateVDD2VSSHeight + _NMOSSubringinputs['_Width'] +\
                                                + _DRCObj._Metal1MinSpace3 + _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace,
                                                self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] + _DRCObj._RXMinSpacetoPRES * 2)

        else :
            _TotalSubringinputs['_XWidth'] =_NMOSSubringinputs['_XWidth'] + (_NMOSSubringinputs['_Width']) * 2 + _DRCObj._PpMinExtensiononPactive2 * 4 + _DRCObj._NwMinSpacetoPactive + _DRCObj._NwMinEnclosurePactive + \
                                            max(_DRCObj._RPOMinSpace2OD * 2 , 
                                            _DRCObj.DRCMETAL1MinSpace(_TransmissionGateChannelWidth * _TransmissionGateNPRatio + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _TransmissionGateChannelWidth * _TransmissionGateNPRatio + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _TotalSubringWidth) * 2 - _DRCObj._RPOMinExtensionOnPO * 2) \
                                            + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_RPOLayer']['_XWidth']

            _TotalSubringinputs['_YWidth'] = max(_TransmissionGateVDD2VSSHeight + _NMOSSubringinputs['_Width'] +\
                                               +  max(_DRCObj._NwMinSpacetoPactive + _DRCObj._NwMinEnclosureNactive + _DRCObj._NpMinExtensiononNactive2 +  _DRCObj._PpMinExtensiononPactive2 , _DRCObj._PpMinSpace +  _DRCObj._PpMinExtensiononPactive2 +  _DRCObj._PpMinExtensiononPactive2) * 2,
                                                # _DRCObj._NwMinSpacetoPactive + _DRCObj._NwMinEnclosureNactive + _DRCObj._NpMinExtensiononNactive2 +  _DRCObj._PpMinExtensiononPactive2 + _DRCObj._PpMinSpace +  _DRCObj._PpMinExtensiononPactive2 +  _DRCObj._PpMinExtensiononPactive2,
                                                self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + _DRCObj._PpMinSpace * 2 + _DRCObj._PpMinExtensiononPactive2 * 2,
                                                self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] +
                                                _DRCObj.DRCMETAL1MinSpace(_ResistorWidth, _ResistorWidth, self.getXWidth('_OpppcresRB','_Met1Layer') * 2 - _DRCObj._PpMinEnclosureOfPo * 2 + _DRCObj._Metal1MinEnclosureCO2 * 2))


        self._DesignParameter['_TotalSubringRB'] = self._SrefElementDeclaration(_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='TotalSubringIn{}'.format(_Name)))[0]
        self._DesignParameter['_TotalSubringRB']['_DesignObj']._CalculatePSubring(**_TotalSubringinputs)


        print ('#################################       Coordinates Settings      ########################################')


        self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'] = [[0,0]]

        _VDD2VSSMinHeight = max(_NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_YWidth'] + max(_DRCObj.DRCMETAL1MinSpace(_NMOSSubringinputs['_Width'], _NMOSSubringinputs['_XWidth'] + _NMOSSubringinputs['_Width'] * 2 , _PMOSSubringinputs['_Width']) + _NMOSSubringinputs['_Width'],
                                self.getWidth('_PMOSSubringRB','_NWLayer') * 0.5 + self.getWidth('_NMOSSubringRB','_PPLayer') * 0.5 + _DRCObj._NwMinSpacetoPactive)
                                + _PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_YWidth'],
                                abs(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] - self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]))

        if _VDD2VSSMinHeight % (2 * _MinSnapSpacing) != 0 :
            _VDD2VSSMinHeight = self.CeilMinSnapSpacing(_VDD2VSSMinHeight, 2 * _MinSnapSpacing)

        print ('@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@# SET MINIMUM HEIGHT VALUE FOR RESISTOR BANK : ', _VDD2VSSMinHeight)

        if _TransmissionGateVDD2VSSHeight < _VDD2VSSMinHeight :
            _TransmissionGateVDD2VSSHeight = _VDD2VSSMinHeight

        if _TransmissionGateVDD2VSSHeight == None :
            _TransmissionGateVDD2VSSHeight = _VDD2VSSMinHeight

        self._DesignParameter['_VDD2VSSMinHeight'] = {'_Ignore' : _VDD2VSSMinHeight, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}

        if DesignParameters._Technology != '028nm' :
            _GapBtwRL = abs(self.CeilMinSnapSpacing(((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] 
                                        + _DRCObj.DRCMETAL1MinSpace(self.getXWidth('_TransmissionGateRB','_PMOSTG','_Met1Layer'), self.getYWidth('_TransmissionGateRB','_PMOSTG','_Met1Layer'), _PMOSSubringinputs['_Width']) * 2) // 2 - 
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] 
                                        + _DRCObj.DRCMETAL1MinSpace(self.getYWidth('_ViaMet12Met2OnInput','_Met1Layer'), self.getYWidth('_ViaMet12Met2OnInput','_Met1Layer'), _PMOSSubringinputs['_Width'])), 2 * _MinSnapSpacing))
        
        else :
            _GapBtwRL = abs(((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] -
                                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - \
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]
                                         - self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) * 2 + \
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace3 * 2) // 2 - 
                                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 +
                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + _DRCObj._Metal1MinSpace + _DRCObj._Metal1MinSpace3))

        self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] - _GapBtwRL // 2,
                                                                    self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight - int(round(_PMOSSubringinputs['_YWidth'] + 0.5))//2 - int(round((_PMOSSubringinputs['_Width'] + 0.5))) // 2]]


        #if (_TransmissionGateChannelWidth * _TransmissionGateNPRatio <= 700) :
        self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] - _GapBtwRL // 2,
                                                                    self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + int(round(_NMOSSubringinputs['_YWidth'] + 0.5)) // 2 + int(round(_NMOSSubringinputs['_Width'] +0.5))// 2]]

        # else :
        #     self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0],
        #                                                             self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + (_NMOSSubringinputs['_YWidth']) // 2 + _NMOSSubringinputs['_Width'] // 2 - (_DRCObj._MetalxMinSpace8 - _DRCObj._Metal1MinSpace3 - 1)//2 + 1]]

        ##Total Guardring Settings
        self._DesignParameter['_TotalSubringRB']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] + int(round(_TotalSubringinputs['_XWidth'] + 0.5))// 2 - int(round(_GapBtwRL + 0.5)) // 2 -
                                                                        int(round((_PMOSSubringinputs['_XWidth'] + 0.5))//2 +
                                                                        # + _TotalSubringinputs['_Width'] +
                                                                        max(_PMOSSubringinputs['_Width'] + _DRCObj._NwMinEnclosurePactive ,_NMOSSubringinputs['_Width'] + _DRCObj._PpMinExtensiononPactive2 
                                                                        + max(_DRCObj._PpMinSpace + _DRCObj._PpMinExtensiononPactive2, _DRCObj._NwMinEnclosureNactive + _DRCObj._NwMinSpacetoPactive + _DRCObj._PpMinExtensiononPactive2))),
                                                                        min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2,
                                                                        self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + int(round(_TotalSubringinputs['_YWidth'] + 0.5)) // 2 -
                                                                        int(round((_NMOSSubringinputs['_Width']+0.5))//2 + _DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace))
                                                                        # self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TotalSubringinputs['_YWidth'] // 2  - 
                                                                        # (_DRCObj._PpMinSpace +  _DRCObj._PpMinExtensiononPactive2 +  _DRCObj._PpMinExtensiononPactive2)
                                                                        ]]
        
        

        ## Resistor Settings
        if DesignParameters._Technology == '028nm' :
            self._DesignParameter['_OpppcresRB']['_XYCoordinates'] = [
                [self.CeilMinSnapSpacing(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                _NMOSSubringinputs['_Width'] + int(round(_NMOSSubringinputs['_XWidth'] + 0.5)) // 2 + _DRCObj._RXMinSpacetoPRES + 30 +
                int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + 0.5)) // 2, 2*_MinSnapSpacing),
                min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2, self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1])]]

        else :
            self._DesignParameter['_OpppcresRB']['_XYCoordinates'] = [
                [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                _NMOSSubringinputs['_Width'] + int(round(_NMOSSubringinputs['_XWidth'] + 0.5)) // 2 +
                max(_DRCObj._RPOMinSpace2OD + int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_RPOLayer']['_XWidth'] + 0.5)) // 2,
                _DRCObj._PpMinSpace + _DRCObj._PpMinExtensiononPactive2 + int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + 0.5)) // 2,
                _DRCObj.DRCMETAL1MinSpace(_TransmissionGateChannelWidth * _TransmissionGateNPRatio + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _TransmissionGateChannelWidth * _TransmissionGateNPRatio + self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], _TotalSubringWidth) + int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 0.5)) // 2),
                # _DRCObj._PpMinSpace, _DRCObj.DRCMETAL1MinSpace(_TransmissionGateChannelWidth * _TransmissionGateNPRatio, _TransmissionGateChannelWidth * _TransmissionGateNPRatio, _TotalSubringWidth) - _DRCObj._RPOMinExtensionOnPO) +
                # int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_RPOLayer']['_XWidth'] + 0.5)) // 2,
                min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2, self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1])]]
        
        # if _ResistorWidth % 2 == 0 and _ResistorLength % 2 == 1 :
        #     self._DesignParameter['_OpppcresRB']['_XYCoordinates'] = [
        #         [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
        #         _NMOSSubringinputs['_Width'] + int(round(_NMOSSubringinputs['_XWidth'] + 0.5)) // 2 + _DRCObj._RXMinSpacetoPRES +
        #         int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + 0.5)) // 2,
        #         min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2, self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1])]]

        # if _ResistorWidth % 2 == 1 and _ResistorLength % 2 == 0 :
        #     self._DesignParameter['_OpppcresRB']['_XYCoordinates'] = [
        #         [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
        #         _NMOSSubringinputs['_Width'] + int(round(_NMOSSubringinputs['_XWidth'] + 0.5)) // 2 + _DRCObj._RXMinSpacetoPRES +
        #         int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + 0.5)) // 2 - 1,
        #         min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2, self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1])]]

        # if _ResistorWidth % 2 == 1 and _ResistorLength % 2 == 1 :
        #     self._DesignParameter['_OpppcresRB']['_XYCoordinates'] = [
        #         [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
        #         _NMOSSubringinputs['_Width'] + int(round(_NMOSSubringinputs['_XWidth'] + 0.5)) // 2 + _DRCObj._RXMinSpacetoPRES +
        #         int(round(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] + 0.5)) // 2 - 1,
        #         min(self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + _TransmissionGateVDD2VSSHeight // 2, self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1])]]

        ##Input Via Settings
        # if DesignParameters._Technology == '028nm' :
        self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'] = [[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] + 
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] -
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 -
                                                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 - _DRCObj._Metal1MinSpace2,
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] + 
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0] -
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 -
                                                                        self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2 - _DRCObj._Metal1MinSpace2,
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]]]

      
        self._DesignParameter['_ViaMet22Met3OnInput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates']
        self._DesignParameter['_ViaMet32Met4OnInput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates']
        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates']

        #### Additional input metal for minimum metal design rules...
        if (self.getXWidth('_ViaMet12Met2OnInput','_Met2Layer') * self.getYWidth('_ViaMet12Met2OnInput','_Met2Layer') < _DRCObj._MetalxMinArea) :
            self._DesignParameter['_ViaAddMet2Layer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[],_Width=100)
            self._DesignParameter['_ViaAddMet2Layer']['_Width'] = self.getYWidth('_ViaMet12Met2OnInput','_Met2Layer')
            self._DesignParameter['_ViaAddMet2Layer']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][0] + self.getXWidth('_ViaMet12Met2OnInput','_Met2Layer') // 2, self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][0] + self.getXWidth('_ViaMet12Met2OnInput','_Met2Layer') // 2 -
                                                                        self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea / self.getYWidth('_ViaMet12Met2OnInput','_Met2Layer'), 2*_MinSnapSpacing),
                                                                        self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][1]]],
                                                                        [[self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][0] + self.getXWidth('_ViaMet12Met2OnInput','_Met2Layer') // 2, self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][1]],
                                                                        [self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][0] + self.getXWidth('_ViaMet12Met2OnInput','_Met2Layer') // 2 -
                                                                        self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea / self.getYWidth('_ViaMet12Met2OnInput','_Met2Layer'), 2*_MinSnapSpacing),
                                                                        self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][1]]]]

            self._DesignParameter['_ViaAddMet3Layer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[],_Width=100)
            self._DesignParameter['_ViaAddMet3Layer']['_Width'] = self.getYWidth('_ViaMet12Met2OnInput','_Met2Layer')
            self._DesignParameter['_ViaAddMet3Layer']['_XYCoordinates'] = self._DesignParameter['_ViaAddMet2Layer']['_XYCoordinates']

            self._DesignParameter['_ViaAddMet4Layer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[],_Width=100)
            self._DesignParameter['_ViaAddMet4Layer']['_Width'] = self.getYWidth('_ViaMet12Met2OnInput','_Met2Layer')
            self._DesignParameter['_ViaAddMet4Layer']['_XYCoordinates'] = self._DesignParameter['_ViaAddMet2Layer']['_XYCoordinates']

        if (self.getXWidth('_TransmissionGateRB', '_ViaMet12Met2OnNMOSOutputTG' , '_Met2Layer') * self.getYWidth('_TransmissionGateRB', '_ViaMet12Met2OnNMOSOutputTG' , '_Met2Layer') < _DRCObj._MetalxMinArea) :
            self._DesignParameter['_ViaAddMet2LayeronNMOS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[],_XWidth=400,_YWidth=400)
            self._DesignParameter['_ViaAddMet2LayeronNMOS']['_XWidth'] = self.getXWidth('_TransmissionGateRB', '_ViaMet12Met2OnNMOSOutputTG' , '_Met2Layer')
            self._DesignParameter['_ViaAddMet2LayeronNMOS']['_YWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea / self._DesignParameter['_ViaAddMet2LayeronNMOS']['_XWidth'], 2 * _MinSnapSpacing)
            self._DesignParameter['_ViaAddMet2LayeronNMOS']['_XYCoordinates'] = copy.deepcopy(self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'])
            for i in range (len(self._DesignParameter['_ViaAddMet2LayeronNMOS']['_XYCoordinates'])) :
                self._DesignParameter['_ViaAddMet2LayeronNMOS']['_XYCoordinates'][i][1] -= (self._DesignParameter['_ViaAddMet2LayeronNMOS']['_YWidth'] - self.getYWidth('_TransmissionGateRB', '_ViaMet12Met2OnNMOSOutputTG' , '_Met2Layer')) * 0.5



        self._DesignParameter['_Met5LayerInput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met5LayerInput']['_Width'] = self._DesignParameter['_ViaMet42Met5OnInput']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']
        self._DesignParameter['_Met5LayerInput']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] +
                                                                        abs(self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0]),
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][0][1]]],
                                                                        [[self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][1][0],
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][1][1]],
                                                                        [self._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] +
                                                                        abs(self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0]),
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][1][1]]]]



        print ('###############################       Additional Path Settings      ######################################')
        ##Additional NWell Generation
        self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_NWLayer']['_Width'] = _PMOSSubringinputs['_YWidth']
        self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] +
                                                                 self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] - _PMOSSubringinputs['_XWidth']//2,
                                                                 self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]],
                                                                [self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] + _PMOSSubringinputs['_XWidth']//2,
                                                                 self._DesignParameter['_TransmissionGateRB']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]]]]


        #Additional SLVT Generation
        #self._DesignParameter['_SLVTLayerPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XYCoordinates=[], _Width=100)
        if DesignParameters._Technology == '028nm' :
            _XVTLayer='_'+_TransmissionGateXVT+'Layer'
            if (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth'] *
                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']) < _DRCObj._SlvtMinArea2 :
                self._DesignParameter['_SLVTLayerNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_TransmissionGateXVT][0], _Datatype=DesignParameters._LayerMapping[_TransmissionGateXVT][1], _XYCoordinates=[], _Width=100)
                self._DesignParameter['_SLVTLayerNMOS']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']
                _LengthOfSLVT = _DRCObj._SlvtMinArea2 // self._DesignParameter['_SLVTLayerNMOS']['_Width'] + 2

                self._DesignParameter['_SLVTLayerNMOS']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] - _LengthOfSLVT // 2 - 1,
                                                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]],
                                                                                [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][0] + _LengthOfSLVT // 2 + 1,
                                                                                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_NMOSTG']['_XYCoordinates'][0][1]]]]

            if (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth'] *
                self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']) < _DRCObj._SlvtMinArea2 :
                self._DesignParameter['_SLVTLayerPMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[_TransmissionGateXVT][0], _Datatype=DesignParameters._LayerMapping[_TransmissionGateXVT][1], _XYCoordinates=[], _Width=100)
                self._DesignParameter['_SLVTLayerPMOS']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']
                _LengthOfSLVT = _DRCObj._SlvtMinArea2 // self._DesignParameter['_SLVTLayerPMOS']['_Width'] + 2
                self._DesignParameter['_SLVTLayerPMOS']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] - _LengthOfSLVT // 2 - 1,
                                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]],
                                                                            [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][0] + _LengthOfSLVT // 2 + 1,
                                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_PMOSTG']['_XYCoordinates'][0][1]]]]


        #Additional Metal & Via Generation for Resistor
        if DesignParameters._Technology == '028nm' :
            _LengthOfAddMet1Y = (self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] // 2 +
                             self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) * 2

        else :
            _LengthOfAddMet1Y = (self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_RPOLayer']['_YWidth'] // 2 +
                             self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) * 2

        _NumViaMet12Met2COX = (self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
        _NumViaMet12Met2COY = _LengthOfAddMet1Y // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)

        if DesignParameters._Technology=='028nm' :
            _CONUMXmax = int((self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
            _CONUMYmax = int((int((self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_OPLayer']['_YWidth'] - 2*_DRCObj._CoMinSpace2OP - 2*_DRCObj._CoMinEnclosureByPO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1) // 2)

            if _ResistorMetXCO == None :
                _ResistorMetXCO = _CONUMXmax
            if _ResistorMetYCO == None :
                _ResistorMetYCO = _CONUMYmax

        if DesignParameters._Technology!= '028nm' :
            self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] += 2 * _DRCObj._Metal1MinEnclosureCO2

        


        # _Resport1 = [[self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0][i] + 
        #             self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][i] for i in range (len(self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0]))]]
        _Resport1 = [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'][0][1]]]
        _Resport2 = [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                    self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'][0][1]]]


        _ViaResMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaResMet12Met2['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - _DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
        _ViaResMet12Met2['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

        if _ViaResMet12Met2['_ViaMet12Met2NumberOfCOX'] <= 1 :
            _ViaResMet12Met2['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaResMet12Met2['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
        if _ViaResMet12Met2['_ViaMet12Met2NumberOfCOY'] <= 1 :
            _ViaResMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1
            _ViaResMet12Met2['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - _DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

        #self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates']
        self._DesignParameter['_ViaMet12Met2OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaResMet12Met2)
        self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'] = _Resport2


        _ViaResMet12Met21 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
        _ViaResMet12Met21['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - _DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
        _ViaResMet12Met21['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

        if _ViaResMet12Met21['_ViaMet12Met2NumberOfCOX'] <= 1 :
            _ViaResMet12Met21['_ViaMet12Met2NumberOfCOX'] = 1
            _ViaResMet12Met21['_ViaMet12Met2NumberOfCOY'] = int((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
        if _ViaResMet12Met21['_ViaMet12Met2NumberOfCOY'] <= 1 :
            _ViaResMet12Met21['_ViaMet12Met2NumberOfCOY'] = 1
            _ViaResMet12Met21['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - _DRCObj._VIAxMinWidth - _DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))

        #self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates']
        self._DesignParameter['_ViaMet12Met2OnRes1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnResistor1In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet12Met2OnRes1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaResMet12Met21)
        self._DesignParameter['_ViaMet12Met2OnRes1']['_XYCoordinates'] = _Resport1
        
                                                                        # [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                        #   self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] - 
                                                                        #   _TotalSubringinputs['_YWidth']//2 + 
                                                                        #   self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 + _DRCObj._MetalxMinSpace9],
                                                                        #  [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                        #   self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] + 
                                                                        #   _TotalSubringinputs['_YWidth']//2 - 
                                                                        #   self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 - _DRCObj._MetalxMinSpace9]]
                                                                        ## [0] - Downward, [1] - Upward

        _ViaResMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaResMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaResMet12Met2['_ViaMet12Met2NumberOfCOX']
        _ViaResMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaResMet12Met2['_ViaMet12Met2NumberOfCOY']

        self._DesignParameter['_ViaMet22Met3OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnRes']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaResMet22Met3)
        self._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'] = _Resport2
        
        _ViaResMet22Met31 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaResMet22Met31['_ViaMet22Met3NumberOfCOX'] = _ViaResMet12Met21['_ViaMet12Met2NumberOfCOX']
        _ViaResMet22Met31['_ViaMet22Met3NumberOfCOY'] = _ViaResMet12Met21['_ViaMet12Met2NumberOfCOY']

        self._DesignParameter['_ViaMet22Met3OnRes1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnResistor1In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet22Met3OnRes1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaResMet22Met31)
        self._DesignParameter['_ViaMet22Met3OnRes1']['_XYCoordinates'] = _Resport1

        _ViaResMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaResMet32Met4['_ViaMet32Met4NumberOfCOX'] = _ViaResMet12Met21['_ViaMet12Met2NumberOfCOX']
        _ViaResMet32Met4['_ViaMet32Met4NumberOfCOY'] = _ViaResMet12Met21['_ViaMet12Met2NumberOfCOY']

        self._DesignParameter['_ViaMet32Met4OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaMet32Met4OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet32Met4OnRes']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaResMet32Met4)
        self._DesignParameter['_ViaMet32Met4OnRes']['_XYCoordinates'] = _Resport1
        
                                                                        # [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                        #   self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] - 
                                                                        #   _TotalSubringinputs['_YWidth']//2 + 
                                                                        #   self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 + _DRCObj._MetalxMinSpace9]]

        _ViaResMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
        _ViaResMet42Met5['_ViaMet42Met5NumberOfCOX'] = _ViaResMet12Met21['_ViaMet12Met2NumberOfCOX']
        _ViaResMet42Met5['_ViaMet42Met5NumberOfCOY'] = _ViaResMet12Met21['_ViaMet12Met2NumberOfCOY']

        self._DesignParameter['_ViaMet42Met5OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None,_Name='ViaMet42Met5OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet42Met5OnRes']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureY(**_ViaResMet42Met5)
        self._DesignParameter['_ViaMet42Met5OnRes']['_XYCoordinates'] = _Resport1

        _ViaResMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
        _ViaResMet52Met6['_ViaMet52Met6NumberOfCOX'] = _ViaResMet12Met21['_ViaMet12Met2NumberOfCOX']
        _ViaResMet52Met6['_ViaMet52Met6NumberOfCOY'] = _ViaResMet12Met21['_ViaMet12Met2NumberOfCOY']

        self._DesignParameter['_ViaMet52Met6OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None,_Name='ViaMet52Met6OnResistorIn{}'.format(_Name)))[0]
        self._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureY(**_ViaResMet52Met6)
        self._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'] = _Resport1

        # _ViaResMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
        # _ViaResMet62Met7['_ViaMet62Met7NumberOfCOX'] = _ResistorMetXCO
        # _ViaResMet62Met7['_ViaMet62Met7NumberOfCOY'] = _ResistorMetYCO

        # self._DesignParameter['_ViaMet62Met7OnRes'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None,_Name='ViaMet62Met7OnResistorIn{}'.format(_Name)))[0]
        # self._DesignParameter['_ViaMet62Met7OnRes']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(**_ViaResMet62Met7)
        # self._DesignParameter['_ViaMet62Met7OnRes']['_XYCoordinates'] = []


        ##Metal Generation for Input metal 1 
        self._DesignParameter['_Met1LayerInput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met1LayerInput']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_Met1LayerInput']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][0] - 
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][1]],
                                                                    [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][0][1]]],
                                                                    [[self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][0] - 
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][1]],
                                                                    [self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][0],
                                                                    self._DesignParameter['_ViaMet12Met2OnInput']['_XYCoordinates'][1][1]]]]


        ## Metal Generation for VCM
        self._DesignParameter['_Met2LayerVCM'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met2LayerVCM']['_XWidth'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
        self._DesignParameter['_Met2LayerVCM']['_YWidth'] = self.CeilMinSnapSpacing((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_XYCoordinates'][0][1] -
                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'][0][1]) + \
                                                            (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] +
                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) // 2, 2*_MinSnapSpacing)
        


        tmp1 = copy.deepcopy(self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'])
        tmp2 = copy.deepcopy(self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'])

        for i in tmp2 :
            if i in tmp1 : 
                tmp1.remove(i)
        
        for i in range(0, len(tmp1)) :
            tmp1[i][1] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_XYCoordinates'][0][1] - \
                         self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + \
                         self._DesignParameter['_Met2LayerVCM']['_YWidth'] // 2
        

        self._DesignParameter['_Met2LayerVCM']['_XYCoordinates'] = tmp1
        
        
        _ViaVCMMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaVCMMet22Met3['_ViaMet22Met3NumberOfCOX'] = 1
        _ViaVCMMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2)//(_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

        tmp = []

        self._DesignParameter['_ViaVCMMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaVCMMet22Met3In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaVCMMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_ViaVCMMet22Met3)
        
        for i in range (0, len(tmp1)) :
            tmp.append([tmp1[i][0],
                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]) // 2])

        self._DesignParameter['_ViaVCMMet22Met3']['_XYCoordinates'] = tmp

        del tmp

        _ViaVCMMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _ViaVCMMet32Met4['_ViaMet32Met4NumberOfCOX'] = 1
        _ViaVCMMet32Met4['_ViaMet32Met4NumberOfCOY'] = int((self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]- _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2)//(_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

        tmp = []

        self._DesignParameter['_ViaVCMMet32Met4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None,_Name='ViaVCMMet32Met4In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaVCMMet32Met4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaVCMMet32Met4)
        
        for i in range (0, len(tmp1)) :
            tmp.append([tmp1[i][0],
                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1] + 
                        (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] -
                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnNMOSControlTG']['_XYCoordinates'][0][1]) // 2])

        self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'] = tmp

        del tmp



        self._DesignParameter['_Met4LayerVCM'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met4LayerVCM']['_XWidth'] = self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][-1][0] - self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][0][0]
        self._DesignParameter['_Met4LayerVCM']['_YWidth'] = self._DesignParameter['_ViaVCMMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
        k = len(self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'])
        if k % 2 == 1 :
            self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'] = [[self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][k//2][0],
                                                                        self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][0][1]]]

        else :
            self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'] = [[self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][k//2 - 1][0] + 
                                                                        int(round((self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][k//2][0] -
                                                                        self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][k//2 - 1][0])+0.5)) // 2,
                                                                        self._DesignParameter['_ViaVCMMet32Met4']['_XYCoordinates'][0][1]]]

        del k
        

        ##Metal align for Resistor
        self._DesignParameter['_Met1LayerRes'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met1LayerRes']['_Width'] = max(self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], 
                                                            self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
        self._DesignParameter['_Met1LayerRes']['_XYCoordinates'] = [[[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                    min(self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][0][1] - 
                                                                    self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                                                                    self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0][1] -
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2)],
                                                                    [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                    max(self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2,
                                                                    self._DesignParameter['_ViaMet12Met2OnRes']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)]],
                                                                    [[self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                    max(self._DesignParameter['_ViaMet12Met2OnRes1']['_XYCoordinates'][0][1] + 
                                                                    self._DesignParameter['_ViaMet12Met2OnRes1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2,
                                                                    self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2)],
                                                                    [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0],
                                                                    min(self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][1] +
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'][0][1] -
                                                                    self._DesignParameter['_OpppcresRB']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2,
                                                                    self._DesignParameter['_ViaMet12Met2OnRes1']['_XYCoordinates'][0][1] - 
                                                                    self._DesignParameter['_ViaMet12Met2OnRes1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)]]]
                                                                    

        self._DesignParameter['_Met3LayerPMOSResAX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
        
        self._DesignParameter['_Met3LayerPMOSResAX']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_OpppcresRB']['_XYCoordinates'][0][0] +
                                                                       self._DesignParameter['_ViaMet12Met2OnRes']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // 2,
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnPMOSOutputTG']['_XYCoordinates'][0][1]]]]
    

        self._DesignParameter['_Met3LayerNMOSResAX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met3LayerNMOSResAX']['_Width'] = self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
        ##coordinates description goes below to via declaration

        _ViaTGPMOS2ResMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = int((_PMOSSubringinputs['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
        _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_Met3LayerPMOSResAX']['_Width']- _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
        if _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] <= 1 :
            _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_Met3LayerPMOSResAX']['_Width']- _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
        if _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] <= 1 :
            _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1
            _ViaTGPMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = int((_PMOSSubringinputs['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

        self._DesignParameter['_ViaTGPMOS2ResMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaTGPMOS2ResMet22Met3In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaTGPMOS2ResMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaTGPMOS2ResMet22Met3)
        self._DesignParameter['_ViaTGPMOS2ResMet22Met3']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - _GapBtwRL // 2,
                                                                            self._DesignParameter['_Met3LayerPMOSResAX']['_XYCoordinates'][0][0][1]]]

        _ViaTGNMOS2ResMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = int((_NMOSSubringinputs['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
        _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_Met3LayerNMOSResAX']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
        if _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] < 1 :
            _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = 1
            _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_Met3LayerNMOSResAX']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
        if _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] < 1 :
            _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1
            _ViaTGNMOS2ResMet22Met3['_ViaMet22Met3NumberOfCOX'] = int((_NMOSSubringinputs['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

        self._DesignParameter['_ViaTGNMOS2ResMet22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None,_Name='ViaTGNMOS2ResMet22Met3In{}'.format(_Name)))[0]
        self._DesignParameter['_ViaTGNMOS2ResMet22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaTGNMOS2ResMet22Met3)
        self._DesignParameter['_ViaTGNMOS2ResMet22Met3']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - _GapBtwRL // 2,
                                                                            self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'][0][1]]]

        self._DesignParameter['_Met3LayerNMOSResAX']['_XYCoordinates'] = [[[self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'][0][0],
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'][0][1]],
                                                                        [self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                       self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + 
                                                                       max(self.CeilMinSnapSpacing(self.getXWidth('_ViaTGNMOS2ResMet22Met3', '_Met3Layer')//2, 2*_MinSnapSpacing),
                                                                       self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2),
                                                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet22Met3OnNMOSOutputTG']['_XYCoordinates'][0][1]]]]



        self._DesignParameter['_Met2LayerResYX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=100)
        self._DesignParameter['_Met2LayerResYX']['_Width'] = max(_PMOSSubringinputs['_Width'], self.getXWidth('_ViaTGNMOS2ResMet22Met3','_Met2Layer'), self.getXWidth('_ViaTGPMOS2ResMet22Met3', '_Met2Layer'))
        self._DesignParameter['_Met2LayerResYX']['_XYCoordinates'] = [[[self._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - _GapBtwRL // 2,
                                                                    self._DesignParameter['_Met3LayerPMOSResAX']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3LayerPMOSResAX']['_Width'] // 2],
                                                                    [self._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - _GapBtwRL // 2,
                                                                    self._DesignParameter['_Met3LayerNMOSResAX']['_XYCoordinates'][0][0][1] - self._DesignParameter['_Met3LayerNMOSResAX']['_Width'] // 2]]]

        
        _LengthYbtwGuardring = abs((abs(self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1]) -
                                            abs(self._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) - \
                                            (abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1]) -
                                            abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]))) \
                                            + _NMOSSubringinputs['_Width'] // 2 + _TotalSubringinputs['_Width'] // 2

        _LengthOfPMOSRouting = (self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaPoly2Met1OnPMOSControlTG']['_XYCoordinates'][0][1] + 
                                        self._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2) - \
                                            (self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] - (_PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_YWidth'] // 2))
        
        self._DesignParameter['_Met1LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met1LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] * 2 + _NMOSSubringinputs['_XWidth']
        self._DesignParameter['_Met1LayerVSS']['_YWidth'] = _LengthYbtwGuardring
        self._DesignParameter['_Met1LayerVSS']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                                                                                abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                                    abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                                int(round(_LengthYbtwGuardring + 0.5)) // 2 + _NMOSSubringinputs['_Width'] // 2]]



        ##VDD and VSS VIA Generation.. (Make Metals first and then via)
        if _PowerLine == True :
            self._DesignParameter['_Met2LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #self._DesignParameter['_Met5LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #self._DesignParameter['_Met6LayerVDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met2LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met2LayerVSS1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)            
            self._DesignParameter['_Met3LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVSS1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #self._DesignParameter['_Met5LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            #self._DesignParameter['_Met6LayerVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met2LayerVSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met3LayerVSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_Met4LayerVSS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

            
            
            

            self._DesignParameter['_Met2LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
            # self._DesignParameter['_Met2LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_XWidth'] // 2
            self._DesignParameter['_Met2LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
            self._DesignParameter['_Met2LayerVDD']['_XYCoordinates'] = []
            
                                                                        # [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] -
                                                                        # (_PMOSSubringinputs['_Width'] + _PMOSSubringinputs['_XWidth'] // 2) + self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        # self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
                                                                        # _PMOSSubringinputs['_Width'] // 2 + _PMOSSubringinputs['_YWidth'] // 2]]
            self._DesignParameter['_Met3LayerVDD']['_XWidth'] = _PMOSSubringinputs['_Width'] * 2 + _PMOSSubringinputs['_XWidth']
            self._DesignParameter['_Met3LayerVDD']['_YWidth'] = _PMOSSubringinputs['_Width']
            self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = []
            
            

            self._DesignParameter['_Met2LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2
            self._DesignParameter['_Met2LayerVSS']['_YWidth'] = _LengthYbtwGuardring
            self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'] = []
            
                                                                        # [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                        # (_NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2) - self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        #     abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                        #         abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                        #     _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            self._DesignParameter['_Met3LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2
            self._DesignParameter['_Met3LayerVSS']['_YWidth'] = _LengthYbtwGuardring
            self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'] = []
            
                                                                        # [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                        # (_NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2) - self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        #     abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                        #         abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                        #     _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            self._DesignParameter['_Met4LayerVSS']['_XWidth'] = _NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2 
            self._DesignParameter['_Met4LayerVSS']['_YWidth'] = _LengthYbtwGuardring
            self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'] = []
            
                                                                        # [[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] +
                                                                        # (_NMOSSubringinputs['_Width'] + _NMOSSubringinputs['_XWidth'] // 2) - self._DesignParameter['_Met2LayerVDD']['_XWidth'] // 2,
                                                                        #     abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                        #         abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                        #     _LengthYbtwGuardring // 2 + _NMOSSubringinputs['_Width'] // 2]]

            
            

            #Via Generations
            _NumViaVDDCOX = int(self._DesignParameter['_Met2LayerVDD']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVDDCOX == 0 :
                _NumViaVDDCOX = 1
            _NumViaVDDCOY = int(self._DesignParameter['_Met2LayerVDD']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVDDCOY == 0 :
                _NumViaVDDCOY = 1
            _NumViaVSSCOX = int(self._DesignParameter['_Met2LayerVSS']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVSSCOX == 0 :
                _NumViaVSSCOX = 1
            _NumViaVSSCOY = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVSSCOY == 0 :
                _NumViaVSSCOY = 1

            _NumViaVSS2COX = int(self._DesignParameter['_Met2LayerVSS2']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVSS2COX == 0 :
                _NumViaVSS2COX = 1
            _NumViaVSS2COY = int(self._DesignParameter['_Met2LayerVSS2']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            if _NumViaVSS2COY == 0 :
                _NumViaVSS2COY = 1
            
            
            _ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _NumViaVDDCOY#int(self._DesignParameter['_Met2LayerVDD']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet12Met21 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSSMet12Met21['_ViaMet12Met2NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet12Met21['_ViaMet12Met2NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS1']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _NumViaVDDCOY#int(self._DesignParameter['_Met2LayerVDD']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet22Met31 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSSMet22Met31['_ViaMet22Met3NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet22Met31['_ViaMet22Met3NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS1']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = _NumViaVDDCOY
            _ViaVSSMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVSSMet32Met41 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSSMet32Met41['_ViaMet32Met4NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet32Met41['_ViaMet32Met4NumberOfCOY'] = int(self._DesignParameter['_Met2LayerVSS1']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
            _ViaVDDMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = _NumViaVDDCOY
            _ViaVSSMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
            _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = _NumViaVSSCOY
            _ViaVDDMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = _NumViaVDDCOX
            _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = _NumViaVDDCOY
            _ViaVSSMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
            _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = _NumViaVSSCOX
            _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = _NumViaVSSCOY

            _ViaVSS2Met12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
            _ViaVSS2Met12Met2['_ViaMet12Met2NumberOfCOX'] = _NumViaVSS2COX
            _ViaVSS2Met12Met2['_ViaMet12Met2NumberOfCOY'] = _NumViaVSS2COY
            _ViaVSS2Met22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
            _ViaVSS2Met22Met3['_ViaMet22Met3NumberOfCOX'] = _NumViaVSS2COX
            _ViaVSS2Met22Met3['_ViaMet22Met3NumberOfCOY'] = _NumViaVSS2COY
            _ViaVSS2Met32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
            _ViaVSS2Met32Met4['_ViaMet32Met4NumberOfCOX'] = _NumViaVSS2COX
            _ViaVSS2Met32Met4['_ViaMet32Met4NumberOfCOY'] = _NumViaVSS2COY
            

            self._DesignParameter['_ViaMet12Met2OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet12Met2OnVDD']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_ViaVDDMet12Met2)
            self._DesignParameter['_ViaMet12Met2OnVDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]
                                                                            + self._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1]]]

            self._DesignParameter['_ViaMet22Met3OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['_ViaMet22Met3OnVDD']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_ViaVDDMet22Met3)
            self._DesignParameter['_ViaMet22Met3OnVDD']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnVDD']['_XYCoordinates']
            
            self._DesignParameter['_ViaMet12Met2OnVDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = 0

        else:
            self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                _XYCoordinates=[[self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
                                                                            self._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1]
                                                                            + self._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1]]],
                _Mag=0.5, _Angle=0, _TEXT='VDD')

            self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                _XYCoordinates=[[self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0],
                                                                                abs(self._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] -
                                                                                    abs(self._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])) -
                                                                                int(round(_LengthYbtwGuardring + 0.5)) // 2 + _NMOSSubringinputs['_Width'] // 2]],
                _Mag=0.5, _Angle=0, _TEXT='VSS')

            self._DesignParameter['_Spin'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                _XYCoordinates=[[self._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] +
                                                                        abs(self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0]),
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][1][1]]],
                _Mag=0.5, _Angle=0, _TEXT='S')

            self._DesignParameter['_SBpin'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL5PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                _XYCoordinates=[[self._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] +
                                                                        abs(self._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0]),
                                                                        self._DesignParameter['_ViaMet42Met5OnInput']['_XYCoordinates'][0][1]]],
                _Mag=0.5, _Angle=0, _TEXT='SB')

            self._DesignParameter['_VRXpin'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL6PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                _XYCoordinates=_Resport1,
                _Mag=0.5, _Angle=0, _TEXT='VRX')

            self._DesignParameter['_VCMpin'] = self._TextElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL4PIN'][0],
                _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1],
                _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],
                _XYCoordinates=self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'],
                _Mag=0.5, _Angle=0, _TEXT='VCM')




if __name__ == '__main__' :


    # _InverterFinger = 2
    # _InverterChannelWidth = 200
    # _InverterChannelLength = 30
    # _InverterNPRatio = 2
    # _InverterDummy = True    #T/F?
    # _InverterVDD2VSSHeight = 2252 ## SHOULD BE FIXED OVER MIN VALUE
    # _InverterSLVT = True     #T/F?

    ## 65nm : 500nm min width (60), 28nm : 200nm min width (30), 40nm : 350nm min width(40),  90nm (100nm channel length) : 700nm min width
    ## 65nm : pmos maximum width 1.5um

    for _ in range (0,1) :
        _TransmissionGateFinger = 2
        _TransmissionGateChannelWidth = 500
        _TransmissionGateChannelLength = 60
        _TransmissionGateNPRatio = 2
        _TransmissionGateDummy = False    #T/F?
        _TransmissionGateVDD2VSSHeight = None ## FIXED
        _TransmissionGateXVT = 'LVT'     #T/F?

        _PowerLine = False

        _ResistorWidth = 1500
        _ResistorLength = 1800 ## length should be larger than width in 40nm tsmc process
        _ResistorMetXCO = None
        _ResistorMetYCO = 2

        _PMOSSubringType = False ## FIXED
        _PMOSSubringXWidth = None ## FIXED
        _PMOSSubringYWidth = None ## FIXED
        _PMOSSubringWidth = 170           ## 65 : 170, 45 : 170, 90 : 200, 28 : 170

        _NMOSSubringType = True ## FIXED
        _NMOSSubringXWidth = None ## FIXED
        _NMOSSubringYWidth = None ## FIXED
        _NMOSSubringWidth = _PMOSSubringWidth

        _TotalSubringType = True ## FIXED
        _TotalSubringXWidth = None ## FIXED
        _TotalSubringYWidth = None ## FIXED
        _TotalSubringWidth = _PMOSSubringWidth

        #DesignParameters._Technology = '028nm'

        ResistorBankObj = _ResistorBank(_DesignParameter=None, _Name='ResistorBank')
        #print ("A!!")
        ResistorBankObj._CalculateResistorBank(
                                #  _InverterFinger=_InverterFinger, _InverterChannelWidth=_InverterChannelWidth, _InverterChannelLength=_InverterChannelLength, _InverterNPRatio=_InverterNPRatio, _InverterDummy = _InverterDummy,
                                # _InverterVDD2VSSHeight=_InverterVDD2VSSHeight, _InverterSLVT = _InverterSLVT,
                                # _InverterNumSupplyCOX = None, _InverterNumSupplyCOY = None,
                                # _InverterSupplyMet1XWidth = None, _InverterSupplMet1YWidth = None, _InverterNumVIAPoly2Met1COX = None, _InverterNumVIAPoly2Met1COY = None,
                                # _InverterNumVIAMet12COX = None, _InverterNumVIAMet12COY = None,
                                _TransmissionGateFinger =_TransmissionGateFinger, _TransmissionGateChannelWidth = _TransmissionGateChannelWidth, _TransmissionGateChannelLength = _TransmissionGateChannelLength, _TransmissionGateNPRatio =_TransmissionGateNPRatio,
                                _TransmissionGateDummy = _TransmissionGateDummy , _TransmissionGateVDD2VSSHeight = _TransmissionGateVDD2VSSHeight, _TransmissionGateXVT = _TransmissionGateXVT,
                                _PowerLine = _PowerLine,
                                # _TransmissionGateNumSupplyCOX = None, _TransmissionGateNumSupplyCOY = None, _TransmissionGateSupplyMet1XWidth = None, _TransmissionGateSupplyMet1YWidth = None,
                                # _TransmissionGateNumVIAPoly2Met1COX = None, _TransmissionGateNumVIAPoly2Met1COY = None, _TransmissionGateNumVIAMet12COX = None, _TransmissionGateNumVIAMet12COY = None,
                                _ResistorWidth=_ResistorWidth, _ResistorLength=_ResistorLength, _ResistorMetXCO = _ResistorMetXCO, _ResistorMetYCO = _ResistorMetYCO,
                                    _PMOSSubringType=_PMOSSubringType, _PMOSSubringXWidth=_PMOSSubringXWidth, _PMOSSubringYWidth=_PMOSSubringYWidth,_PMOSSubringWidth=_PMOSSubringWidth,
                                    _NMOSSubringType=_NMOSSubringType, _NMOSSubringXWidth=_NMOSSubringXWidth, _NMOSSubringYWidth=_NMOSSubringYWidth,_NMOSSubringWidth=_NMOSSubringWidth,
                                    _TotalSubringType=_TotalSubringType, _TotalSubringXWidth=_TotalSubringXWidth, _TotalSubringYWidth=_TotalSubringYWidth,_TotalSubringWidth=_TotalSubringWidth)


        ResistorBankObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ResistorBankObj._DesignParameter)
        _fileName = 'ResistorBank.gds'
        testStreamFile = open('./{}'.format(_fileName), 'wb')

        tmp = ResistorBankObj._CreateGDSStream(ResistorBankObj._DesignParameter['_GDSFile']['_GDSFile'])

        tmp.write_binary_gds_stream(testStreamFile)

        testStreamFile.close()

        print ('###############      Sending to FTP Server...      ##################')


        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('junung', 'chlwnsdnd1!')
        #ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
        ftp.cwd('/mnt/sdc/junung/OPUS/TSMC65n')
        #ftp.cwd('/mnt/sdc/junung/OPUS/TSMC40n')
        #ftp.cwd('/mnt/sdc/junung/OPUS/TSMC90n')
        myfile = open('ResistorBank.gds', 'rb')
        ftp.storbinary('STOR ResistorBank.gds', myfile)
        myfile.close()
        ftp.close()

        # _Checker = DRCchecker.DRCchecker('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/TSMC40n','/mnt/sdc/junung/OPUS/TSMC40n/DRC/DRC_run','Rescell_tst','ResistorBank')
        # _Checker.DRCchecker()



