import time

from generatorLib import DRC
from generatorLib import DesignParameters
from generatorLib import StickDiagram
from generatorLib.generator_models.LDO_gen import LDO_Fbres
from generatorLib.generator_models.LDO_gen import LDO_Outcap
from generatorLib.generator_models.LDO_gen import LDO_PassTr
from generatorLib.generator_models.LDO_gen import LDO_OPAmp
from generatorLib.generator_models.LDO_gen import SubRing
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models.LDO_gen import opppcres_b

class _LDO(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='_LDO'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameter(self,
                                  Compact_Mode=True,
                                  # OPAmp
                                  Amp_P0_Finger=10,
                                  Amp_P1_Finger=10,
                                  Amp_P2_Finger=18,
                                  Amp_P3_Finger=4,

                                  Amp_N0_Finger=10,
                                  Amp_N1_Finger=10,
                                  Amp_N2_Finger=4,
                                  Amp_N3_Finger=4,
                                  Amp_N4_Finger=8,

                                  Amp_MOS_Length=50,
                                  Amp_MOS_Width=1000,  # DRC: <1.211(when finger > 10) -> <=1190
                                  _XVT='RVT',

                                  Amp_NCAP_XWidth=3500,  # Length
                                  Amp_NCAP_YWidth=2550,  # Width
                                  Amp_NCAP_NumofGate=2,
                                  Amp_NCAP_NumofRX=3,  # 270deg rotate

                                  Amp_Res_Width=1650,
                                  Amp_Res_Length=1500,
                                  Amp_Res_SeriesStripes=2,
                                  Amp_Res_ParallelStripes=1,

                                  _GuardringCOpitch=175,
                                  _GuardringThickness=348,
                                  _GuardringEnclosure=56,

                                  # Pass Tr
                                  PassTr_Finger=34,
                                  PassTr_Length=30,
                                  PassTr_Width=1000,   # DRC: <1.211(when finger > 10) -> <=1190
                                  PassTr_row=4,
                                  PassTr_col=1,
                                  UnitHeight=4068,  # distance btw NbodyContact center
                                  Pass_XVT='RVT',

                                  # Feedback Resistor
                                  InsertFbRes=False,
                                  Fb_Res_Width=3000,
                                  Fb_Res_Length=1000,
                                  Num_of_UpperRes=2,
                                  Num_of_LowerRes=3,
                                  SpacebtwRes_topbot=None,
                                  SpacebtwRes_rightleft=None,
                                  Fb_res_RingHeight=8272,
                                  Fb_res_RingWidth=14512,

                                  # Output Cap
                                  InsertOutCap = True,
                                  OutCap_XWidth=3000,
                                  OutCap_YWidth=2078,
                                  OutCap_NumofGates=5,
                                  OutCap_NumofOD=4,
                                  OutCap_RingWidth=None,
                                  OutCap_RingHeight=None
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']


        print('#########################################################################################################')
        print('                                         {}  LDO Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        Parameters_Amp = dict(
            Insert_comp=Compact_Mode,
            P0_Finger=Amp_P0_Finger,
            P1_Finger=Amp_P1_Finger,
            P2_Finger=Amp_P2_Finger,
            P3_Finger=Amp_P3_Finger,

            N0_Finger=Amp_N0_Finger,
            N1_Finger=Amp_N1_Finger,
            N2_Finger=Amp_N2_Finger,
            N3_Finger=Amp_N3_Finger,
            N4_Finger=Amp_N4_Finger,

            ChannelLength=Amp_MOS_Length,
            MOS_Width=Amp_MOS_Width,
            GateSpacing=None,
            SDWidth=None,
            XVT=_XVT,

            NCAP_XWidth=Amp_NCAP_XWidth,
            NCAP_YWidth=Amp_NCAP_YWidth,
            NCAP_NumofGate=Amp_NCAP_NumofGate,
            NCAP_NumofRX=Amp_NCAP_NumofRX,

            ResWidth=Amp_Res_Width,
            ResLength=Amp_Res_Length,
            ResCONUMX=None,
            ResCONUMY=1,
            _SeriesStripes=Amp_Res_SeriesStripes,
            _ParallelStripes=Amp_Res_ParallelStripes,

            _GuardringCOpitch=_GuardringCOpitch,
            _GuardringThickness=_GuardringThickness,
            _GuardringPPEnclosure=_GuardringEnclosure
        )

        def roundReal(val, digits):
            return round(val+10**(-len(str(val))-1), digits)

        PRESminspace = 400 # Not in DRC Rule

        print('************************************* Initial Positioning instances ************************************')
        # Amp compensation rules
        if Amp_NCAP_XWidth * Amp_NCAP_NumofGate * Amp_NCAP_YWidth * Amp_NCAP_NumofRX >= 25000 * 25000 * 0.7 and Compact_Mode == True:
            raise Exception("NCAP is too big. Set <Compact_Mode> to False")

        # OP Amp.
        self._DesignParameter['OPAmp'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0,
                                                                      _DesignObj=LDO_OPAmp._SingleEndedOPAmp(_Name='SingleEndedOPampIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['OPAmp']['_DesignObj']._CalculateDesignParameter(**Parameters_Amp)
        self._DesignParameter['OPAmp']['_XYCoordinates'] = [[0, 0]]


        if UnitHeight != None:
            Passring_Height = max(UnitHeight, self.getXY('OPAmp', 'NSubRing', 'topright')[0][1] - self.getXY('OPAmp', 'PSubRing', 'botright')[0][1])
        else:
            Passring_Height = UnitHeight

        if PassTr_col % 2 == 1:
            PassTr_YCoord = self.getXY('OPAmp', 'P0')[0][1]
        else:
            PassTr_YCoord = self.getXY('OPAmp', 'N0')[0][1]

        # Pass Tr.
        self._DesignParameter['PassTr'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=LDO_PassTr._PassTr(_Name='PassTrIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['PassTr']['_DesignObj']._CalculateDesignParameter(Finger=PassTr_Finger,
                                                                                ChannelLength=PassTr_Length,
                                                                                ChannelWidth=PassTr_Width,
                                                                                NumofMOS_row=PassTr_row,
                                                                                NumofMOS_col=PassTr_col,
                                                                                _XVT=Pass_XVT,
                                                                                UnitHeight=Passring_Height,
                                                                                PassTr_RingHeight=None,
                                                                                PassTr_RingWidth=None,
                                                                                _NbodyCOpitch=_GuardringCOpitch,
                                                                                _NbodyThickness=_GuardringThickness,
                                                                                _NbodyNWEnclosure=_GuardringEnclosure)
        self._DesignParameter['PassTr']['_XYCoordinates'] = [[0, PassTr_YCoord]]

        if PassTr_col == 1:
            PassTr_YWidth = abs(self.getXYTop('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1] -
                                  self.getXYBot('PassTr', 'NSubRing', 'botright', '_Met1Layer')[0][1])
        elif PassTr_col == 2:
            PassTr_YWidth = abs(self.getXYTop('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1] -
                                  self.getXYBot('PassTr', 'NSubRing', 'botright', '_Met1Layer')[0][1])
        elif PassTr_col % 2 == 0:
            PassTr_YWidth = abs(self.getXYTop('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1] -
                                  self.getXYBot('PassTr', 'NSubRing', 'botright', '_Met1Layer')[0][1])
        else:
            PassTr_YWidth = abs(self.getXYTop('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1] -
                                  self.getXYBot('PassTr', 'NSubRing', 'botright', '_Met1Layer')[0][1])



        if Compact_Mode == True:
            print('**************************************** Pass Tr. Coord setting ****************************************')
            Nbody_XCoord1 = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_Met1Layer')[0][0]) + _DRCObj._Metal1MinSpace3
            SpacebtwGRMOS = abs(self.getXYBot('OPAmp', 'NSubRing', 'botright', '_Met1Layer')[0][1]) - abs(self.getXYTop('OPAmp', 'PSubRing', 'topright', '_Met1Layer')[0][1])
            PassTr_XCoord = Nbody_XCoord1 + max(SpacebtwGRMOS, _DRCObj._PpMinSpace)
            self._DesignParameter['PassTr']['_XYCoordinates'][0][0] = PassTr_XCoord

            # Adjusting subring's top
            amp_subring_height = self.getXY('OPAmp', 'NSubRing', 'topright', '_Met1Layer')[0][1] - self.getXY('OPAmp', 'PSubRing_CapRes', 'botright', '_Met1Layer')[0][1]
            pass_subring_height = self.getXY('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1] - self.getXY('PassTr', 'NSubRing', 'botright', '_Met1Layer')[0][1]
            tmpampYCenter = (self.getXY('OPAmp', 'NSubRing', 'topright', '_Met1Layer')[0][1] + self.getXY('OPAmp', 'PSubRing_CapRes', 'botright', '_Met1Layer')[0][1]) / 2
            tmppassYCenter = (self.getXY('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1] + self.getXY('PassTr', 'NSubRing', 'botright', '_Met1Layer')[0][1]) / 2

            SpacebtwAmpPassM1 = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_Met1Layer')[0][0] - self.getXYLeft('PassTr', 'NSubRing', 'leftupper', '_Met1Layer')[0][0])
            if pass_subring_height <= amp_subring_height:
                amp_pass_diff = self.getXYTop('OPAmp', 'NSubRing', 'topright', '_Met1Layer')[0][1] - self.getXYTop('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1]
                self._DesignParameter['PassTr']['_XYCoordinates'][0][1] += amp_pass_diff
            else:
                self._DesignParameter['PassTr']['_XYCoordinates'][0][1] = tmpampYCenter - tmppassYCenter

            # for DRC rule (GR504)
            if (OutCap_YWidth / 2 >= 1500) & (SpacebtwAmpPassM1 < _DRCObj._MetalxMinSpace11):
                self._DesignParameter['PassTr']['_XYCoordinates'][0][0] += _DRCObj._MetalxMinSpace11 - SpacebtwAmpPassM1


            if InsertFbRes == True:
                print('***************************************** Feedback Res setting *****************************************')
                if SpacebtwRes_topbot == None and SpacebtwRes_rightleft == None and Fb_res_RingHeight == None and Fb_res_RingWidth == None:
                    # Feedback Resistor
                    self._DesignParameter['FbRes'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=LDO_Fbres.LDO_Fbres(_Name='FbResIn{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['FbRes']['_DesignObj']._CalculateDesignParameter(Fb_Res_Width=Fb_Res_Width,
                                                                                           Fb_Res_Length=Fb_Res_Length,
                                                                                           Num_of_UpperRes=Num_of_UpperRes,
                                                                                           Num_of_LowerRes=Num_of_LowerRes,
                                                                                           SpacebtwRes_topbot=PRESminspace,
                                                                                           SpacebtwRes_rightleft=PRESminspace,
                                                                                           Fb_res_RingHeight=Fb_res_RingHeight,
                                                                                           Fb_res_RingWidth=Fb_res_RingWidth,
                                                                                           _GuardringCOpitch=_GuardringCOpitch,
                                                                                           _GuardringThickness=_GuardringThickness,
                                                                                           _GuardringEnclosure=_GuardringEnclosure)
                    self._DesignParameter['FbRes']['_XYCoordinates'] = [[0, 0]]

                    # re-set FbRes ring width & height
                    Pass_subXWidth = self.getXYLeft('PassTr', 'NSubRing', 'rightupper', '_Met1Layer')[0][0] - self.getXYRight('PassTr', 'NSubRing', 'leftupper', '_Met1Layer')[0][0]
                    Res_subXWidth = self.getXYLeft('FbRes', 'PSubRing_Res', 'rightupper', '_Met1Layer')[0][0] - self.getXYRight('FbRes', 'PSubRing_Res', 'leftupper', '_Met1Layer')[0][0]
                    Pass_subYWidth = self.getXYBot('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1] - self.getXYTop('PassTr', 'NSubRing', 'botright', '_Met1Layer')[0][1]
                    Res_subYWidth = self.getXYBot('FbRes', 'PSubRing_Res', 'topright', '_Met1Layer')[0][1] - self.getXYTop('FbRes', 'PSubRing_Res', 'botright', '_Met1Layer')[0][1]
                    SpacebtwAmpPass = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_NWLayer')[0][0] - self.getXYLeft('PassTr', 'NSubRing', 'leftupper', '_NWLayer')[0][0])
                    # set FbRes ring width to Pass Tr ring width
                    if Res_subXWidth < Pass_subXWidth:
                        Res_sub_width = Pass_subXWidth
                    else:
                        Res_sub_width = Res_subXWidth

                    # set FbRes ring width to Pass Tr ring width
                    if amp_subring_height + _GuardringThickness + _GuardringEnclosure * 2 > pass_subring_height + _GuardringThickness + _GuardringEnclosure * 2 + SpacebtwAmpPass + Res_subYWidth + (_GuardringThickness + _GuardringEnclosure) * 2:
                        Res_sub_height = amp_subring_height + _GuardringThickness + _GuardringEnclosure * 2 - (pass_subring_height + _GuardringThickness + _GuardringEnclosure * 2 + SpacebtwAmpPass + (_GuardringThickness + _GuardringEnclosure) * 2)
                    else:
                        Res_sub_height = Res_subYWidth

                    del self._DesignParameter['FbRes']['_XYCoordinates']
                    self._DesignParameter['FbRes'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=LDO_Fbres.LDO_Fbres(_Name='FbResIn{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['FbRes']['_DesignObj']._CalculateDesignParameter(Fb_Res_Width=Fb_Res_Width,
                                                                                           Fb_Res_Length=Fb_Res_Length,
                                                                                           Num_of_UpperRes=Num_of_UpperRes,
                                                                                           Num_of_LowerRes=Num_of_LowerRes,
                                                                                           SpacebtwRes_topbot=None,
                                                                                           SpacebtwRes_rightleft=None,
                                                                                           Fb_res_RingHeight=Res_sub_height,
                                                                                           Fb_res_RingWidth=Res_sub_width,
                                                                                           _GuardringCOpitch=_GuardringCOpitch,
                                                                                           _GuardringThickness=_GuardringThickness,
                                                                                           _GuardringEnclosure=_GuardringEnclosure)
                    self._DesignParameter['FbRes']['_XYCoordinates'] = [[0, 0]]

                else:
                    # Feedback Resistor
                    self._DesignParameter['FbRes'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=LDO_Fbres.LDO_Fbres(_Name='FbResIn{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['FbRes']['_DesignObj']._CalculateDesignParameter(Fb_Res_Width=Fb_Res_Width,
                                                                                           Fb_Res_Length=Fb_Res_Length,
                                                                                           Num_of_UpperRes=Num_of_UpperRes,
                                                                                           Num_of_LowerRes=Num_of_LowerRes,
                                                                                           SpacebtwRes_topbot=SpacebtwRes_topbot,
                                                                                           SpacebtwRes_rightleft=SpacebtwRes_rightleft,
                                                                                           Fb_res_RingHeight=Fb_res_RingHeight,
                                                                                           Fb_res_RingWidth=Fb_res_RingWidth,
                                                                                           _GuardringCOpitch=_GuardringCOpitch,
                                                                                           _GuardringThickness=_GuardringThickness,
                                                                                           _GuardringEnclosure=_GuardringEnclosure)
                    self._DesignParameter['FbRes']['_XYCoordinates'] = [[0, 0]]

                # FbRes Coord resetting
                Res_reXCoord = self.getXY('FbRes')[0][0] - self.getXYLeft('FbRes', 'PSubRing_Res', 'leftlower', '_Met1Layer')[0][0]
                Res_reYCoord = self.getXY('FbRes')[0][1] - self.getXYBot('FbRes', 'PSubRing_Res', 'botleft', '_Met1Layer')[0][1]
                self._DesignParameter['FbRes']['_XYCoordinates'] = [[Res_reXCoord, Res_reYCoord]]

                # SpacebtwAmpPass = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_NWLayer')[0][0] - self.getXYLeft('PassTr', 'NSubRing', 'leftupper', '_NWLayer')[0][0])
                Res_subXWidth = self.getXYRight('FbRes', 'PSubRing_Res', 'rightupper', '_Met1Layer')[0][0] - self.getXYLeft('FbRes', 'PSubRing_Res', 'leftupper', '_Met1Layer')[0][0]
                Res_subYWidth = self.getXYTop('FbRes', 'PSubRing_Res', 'topright', '_Met1Layer')[0][1] - self.getXYBot('FbRes', 'PSubRing_Res', 'botright', '_Met1Layer')[0][1]

                FbRes_XCoord = self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_NWLayer')[0][0] + SpacebtwAmpPass + _GuardringEnclosure
                FbRes_Ycoord = self.getXYBot('PassTr', 'NSubRing', 'botright', '_NWLayer')[0][1] - SpacebtwAmpPass - Res_subYWidth - _GuardringEnclosure

                self._DesignParameter['FbRes']['_XYCoordinates'][0][0] += FbRes_XCoord
                self._DesignParameter['FbRes']['_XYCoordinates'][0][1] += FbRes_Ycoord

                # Adjusting subring's bot
                amp_bot = self.getXYBot('OPAmp', 'PSubRing_CapRes', 'botright', '_Met1Layer')[0][1]
                Fb_bot = self.getXYBot('FbRes', 'PSubRing_Res', 'botright', '_Met1Layer')[0][1]
                amp_Fb_diff = amp_bot - Fb_bot

                self._DesignParameter['PassTr']['_XYCoordinates'][0][1] += amp_Fb_diff
                self._DesignParameter['FbRes']['_XYCoordinates'][0][1] += amp_Fb_diff


                print('****************************************** Amp - FbRes Routing *****************************************')
                # Amp INP ~ Fb res (M4)
                self._DesignParameter['Amp2ResM4Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                         _Width=self.getWidth('OPAmp', '_OUT1NCAPMet3Routing'), _XYCoordinates=[])
                self._DesignParameter['Amp2ResM4Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'N1PolyGate')[0][0],
                                                                                 self.getXY('OPAmp', 'N1PolyGate')[0][1] + self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer') / 2],
                                                                                [self.getXY('OPAmp', 'N1PolyGate')[0][0],
                                                                                 self.getXY('FbRes', '_UpLowRouting')[0][1] - self.getWidth('OPAmp', '_OUT1NCAPMet3Routing') / 2]],
                                                                               [[self.getXY('OPAmp', 'N1PolyGate')[0][0] - self.getWidth('OPAmp', '_OUT1NCAPMet3Routing') / 2,
                                                                                 self.getXY('FbRes', '_UpLowRouting')[0][1]],
                                                                                [self.getXY('FbRes', '_UpLowRouting')[0][0] + self.getXWidth('FbRes', '_UpLowRouting') / 2,
                                                                                 self.getXY('FbRes', '_UpLowRouting')[0][1]]]]

                # Amp INP
                self._DesignParameter['Amp2ResViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2ResViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2ResViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
                self._DesignParameter['Amp2ResViaM12M2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                self._DesignParameter['Amp2ResViaM12M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                self._DesignParameter['Amp2ResViaM12M2']['_XYCoordinates'] = [[self._DesignParameter['Amp2ResM4Routing']['_XYCoordinates'][0][0][0],
                                                                               self._DesignParameter['Amp2ResM4Routing']['_XYCoordinates'][0][0][1] - self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer') / 2]]

                self._DesignParameter['Amp2ResViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2ResViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2ResViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
                self._DesignParameter['Amp2ResViaM22M3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                self._DesignParameter['Amp2ResViaM22M3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                self._DesignParameter['Amp2ResViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2ResViaM12M2']['_XYCoordinates']

                self._DesignParameter['Amp2ResViaM32M4'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Amp2ResViaM32M4In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2ResViaM32M4']['_DesignObj']._CalculateViaMet32Met4DesignParameter(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2)
                self._DesignParameter['Amp2ResViaM32M4']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                self._DesignParameter['Amp2ResViaM32M4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                self._DesignParameter['Amp2ResViaM32M4']['_XYCoordinates'] = self._DesignParameter['Amp2ResViaM12M2']['_XYCoordinates']

                # Fb Res
                self._DesignParameter['Amp2ResViaM12M21'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2ResViaM12M21In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2ResViaM12M21']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
                self._DesignParameter['Amp2ResViaM12M21']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('FbRes', '_UpLowRouting')
                self._DesignParameter['Amp2ResViaM12M21']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getXWidth('FbRes', '_UpLowRouting')
                self._DesignParameter['Amp2ResViaM12M21']['_XYCoordinates'] = [[self._DesignParameter['Amp2ResM4Routing']['_XYCoordinates'][-1][-1][0] - self.getXWidth('FbRes', '_UpLowRouting') / 2,
                                                                               self._DesignParameter['Amp2ResM4Routing']['_XYCoordinates'][-1][-1][1]]]

                self._DesignParameter['Amp2ResViaM22M31'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2ResViaM22M31In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2ResViaM22M31']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
                self._DesignParameter['Amp2ResViaM22M31']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getXWidth('FbRes', '_UpLowRouting')
                self._DesignParameter['Amp2ResViaM22M31']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getXWidth('FbRes', '_UpLowRouting')
                self._DesignParameter['Amp2ResViaM22M31']['_XYCoordinates'] = self._DesignParameter['Amp2ResViaM12M21']['_XYCoordinates']

                self._DesignParameter['Amp2ResViaM32M41'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Amp2ResViaM32M41In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2ResViaM32M41']['_DesignObj']._CalculateViaMet32Met4DesignParameter(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2)
                self._DesignParameter['Amp2ResViaM32M41']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getXWidth('FbRes', '_UpLowRouting')
                self._DesignParameter['Amp2ResViaM32M41']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = self.getXWidth('FbRes', '_UpLowRouting')
                self._DesignParameter['Amp2ResViaM32M41']['_XYCoordinates'] = self._DesignParameter['Amp2ResViaM12M21']['_XYCoordinates']


                print('**************************************** FbRes - Pass Tr Routing ***************************************')
                # Fb res (upper) ~ Pass Tr Drain (M2)
                tmp = self._DesignParameter['FbRes']['_DesignObj']._DesignParameter['Res']['_XYCoordinates']
                tmp.sort(key=lambda x: (x[1], x[0]))
                self._DesignParameter['Pass2ResM2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                          _Width=self.getWidth('FbRes', '_UpperResRouting'), _XYCoordinates=[])
                self._DesignParameter['Pass2ResM2Routing']['_XYCoordinates'] = [[[self.getXY('FbRes')[0][0] + tmp[-2][0]
                                                                                  - self._DesignParameter['FbRes']['_DesignObj']._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                                                                                  self.getXY('FbRes')[0][1] + tmp[-2][1]],
                                                                                 [self.getXYRight('FbRes', 'PSubRing_Res', 'rightupper', '_Met1Layer')[0][0],
                                                                                  self.getXY('FbRes')[0][1] + tmp[-2][1]]]]

                addVia_Xnum = int((self.getWidth('FbRes', '_UpperResRouting') - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
                if self.getWidth('FbRes', '_UpperResRouting') > 460 and addVia_Xnum < 4:  # By DRC Rule GR612
                    addVia_Xnum = 4
                self._DesignParameter['Pass2ResViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Pass2ResViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Pass2ResViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=addVia_Xnum, _ViaMet12Met2NumberOfCOY=1)
                self._DesignParameter['Pass2ResViaM12M2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('FbRes', 'Res', '_Met1Layer')
                self._DesignParameter['Pass2ResViaM12M2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getYWidth('FbRes', 'Res', '_Met1Layer')
                self._DesignParameter['Pass2ResViaM12M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getWidth('FbRes', '_UpperResRouting')
                self._DesignParameter['Pass2ResViaM12M2']['_XYCoordinates'] = [[self._DesignParameter['Pass2ResM2Routing']['_XYCoordinates'][0][0][0],
                                                                                self._DesignParameter['Pass2ResM2Routing']['_XYCoordinates'][0][0][1]]]

                # Additional M2 (Pass Tr - Fb Res)
                if Pass_subXWidth < Res_sub_width:
                    # for DRC (M2-M2 min sapce)
                    if abs(self.getXYRight('PassTr', 'NSubRing', 'rightupper', '_Met1Layer')[0][0] - self.getXYLeft('FbRes', 'PSubRing_Res', 'rightupper', '_Met1Layer')[0][0]) <= _DRCObj._MetalxMinSpace11:
                        self._DesignParameter['Pass2ResM2Routing_add2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                       _Width=self.getXWidth('PassTr', 'PassDM2TieRouting'), _XYCoordinates=[])
                        self._DesignParameter['Pass2ResM2Routing_add2']['_XYCoordinates'] = [[[self.getXY('PassTr', 'PassDM2TieRouting')[0][0],
                                                                                               self.getXY('PassTr', 'PassDM2TieRouting')[0][1]],
                                                                                              [self.getXY('PassTr', 'PassDM2TieRouting')[0][0],
                                                                                               self.getXY('Pass2ResM2Routing')[0][-1][1]]]]
                        self._DesignParameter['Pass2ResM2Routing']['_XYCoordinates'][-1][-1] = [self._DesignParameter['Pass2ResM2Routing_add2']['_XYCoordinates'][-1][-1][0] + self.getWidth('Pass2ResM2Routing_add2') / 2,
                                                                                                self.getXY('FbRes')[0][1] + tmp[-2][1]]
                    else:
                        self._DesignParameter['Pass2ResM2Routing_add1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                       _Width=self.getYWidth('PassTr', 'PassDM2Routing'), _XYCoordinates=[])
                        self._DesignParameter['Pass2ResM2Routing_add1']['_XYCoordinates'] = [[[self.getXY('PassTr', 'PassDM2TieRouting')[0][0],
                                                                                               self.getXY('PassTr', 'PassDM2TieRouting')[0][1]],
                                                                                              [self.getXY('Pass2ResM2Routing')[0][-1][0],
                                                                                               self.getXY('PassTr', 'PassDM2TieRouting')[0][1]]]]
                        self._DesignParameter['Pass2ResM2Routing_add2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                       _Width=self.getXWidth('PassTr', 'PassDM2TieRouting'), _XYCoordinates=[])
                        self._DesignParameter['Pass2ResM2Routing_add2']['_XYCoordinates'] = [[[self.getXY('Pass2ResM2Routing')[0][-1][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                                               self.getXY('PassTr', 'PassDM2TieRouting')[0][1]],
                                                                                              [self.getXY('Pass2ResM2Routing')[0][-1][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                                               self.getXY('Pass2ResM2Routing')[0][-1][1]]]]
                else:
                    self._DesignParameter['Pass2ResM2Routing_add2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                   _Width=self.getXWidth('PassTr', 'PassDM2TieRouting'), _XYCoordinates=[])
                    self._DesignParameter['Pass2ResM2Routing_add2']['_XYCoordinates'] = [[[self.getXY('Pass2ResM2Routing')[0][-1][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                                           self.getXY('PassTr', 'PassDM2TieRouting')[0][1]],
                                                                                          [self.getXY('Pass2ResM2Routing')[0][-1][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                                           self.getXY('Pass2ResM2Routing')[0][-1][1]]]]
                del tmp



                if InsertOutCap == True:
                    print('***************************************** OutCap Coord setting *****************************************')
                    self._DesignParameter['OutCap'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=LDO_Outcap._OutCap(_Name='OutCapIn{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['OutCap']['_DesignObj']._CalculateDesignParameter(OutCap=True,
                                                                                            OutCap_XWidth=OutCap_XWidth,
                                                                                            OutCap_YWidth=OutCap_YWidth,
                                                                                            OutCap_NumofGates=OutCap_NumofGates,
                                                                                            OutCap_NumofOD=OutCap_NumofOD,
                                                                                            OutCap_RingWidth=OutCap_RingWidth,
                                                                                            OutCap_RingHeight=OutCap_RingHeight,
                                                                                            _GuardringCOpitch=_GuardringCOpitch,
                                                                                            _GuardringThickness=_GuardringThickness,
                                                                                            _GuardringEnclosure=_GuardringEnclosure)
                    self._DesignParameter['OutCap']['_XYCoordinates'] = [[0, 0]]

                    SpacebtwAmpPass = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_NWLayer')[0][0] - self.getXYLeft('PassTr', 'NSubRing', 'leftupper', '_NWLayer')[0][0])
                    Cap_subXWidth = self.getXYRight('OutCap', 'PSubRing', 'rightupper', '_Met1Layer')[0][0] - self.getXYLeft('OutCap', 'PSubRing', 'leftupper', '_Met1Layer')[0][0]
                    Cap_subYWidth = self.getXYTop('OutCap', 'PSubRing', 'topright', '_Met1Layer')[0][1] - self.getXYBot('OutCap', 'PSubRing', 'botright', '_Met1Layer')[0][1]
                    Cap_XCoord = max(self.getXYRight('PassTr', 'NSubRing', 'rightupper', '_NWLayer')[0][0],
                                     self.getXYRight('FbRes', 'PSubRing_Res', 'rightupper', '_PPLayer')[0][0]) + SpacebtwAmpPass + Cap_subXWidth / 2 + _GuardringEnclosure
                    Cap_Ycoord = tmpampYCenter

                    self._DesignParameter['OutCap']['_XYCoordinates'][0][0] = Cap_XCoord
                    self._DesignParameter['OutCap']['_XYCoordinates'][0][1] = Cap_Ycoord


                    print('***************************************** Amp - Pass Tr Routing ****************************************')
                    # Amp OUT ~ Pass Tr. Gate (M3)
                    self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                              _Width=self.getYWidth('PassTr', 'PolyGateRouting'), _XYCoordinates=[])
                    if PassTr_col == 1:
                        pass
                    elif PassTr_col == 2:
                        self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                         [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                        # for DRC rule (overlap with routing & amp D-OUT via)
                        if (self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2) >= self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]:
                            M3diff = abs((self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2
                                          - self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]))
                            del self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates']
                            self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                      _Width=self.getYWidth('PassTr', 'PolyGateRouting') - M3diff * 3, _XYCoordinates=[])
                            self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                             [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                        Amp2PassVia_XWidth = self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] - self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]
                        Amp2PassVia_XCoord = (self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] + self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]) / 2
                        # # for DRC rule
                        # if self.getWidth('OutCap', 'OutCapMet2PolyRouting') >= 1500:
                        #     Amp2PassVia_XWidth = self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] - self.getXYRight('OutCap', 'OutCapViaPoly', '_Met2Layer')[0][0] - _DRCObj._MetalxMinSpace11
                        #     Amp2PassVia_XCoord = (self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] + self.getXYRight('OutCap', 'OutCapViaPoly', '_Met2Layer')[0][0]) / 2
                        Amp2PassVia_YWidth = self.getWidth('Amp2PassM3Routing')
                        Amp2PassVia_COXnum = int((Amp2PassVia_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) - 1
                        Amp2PassVia_COYnum = int((Amp2PassVia_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1
                        if (Amp2PassVia_XWidth > 330) & (Amp2PassVia_COXnum < 3):
                            Amp2PassVia_COXnum = 3
                        if (Amp2PassVia_XWidth > 460) & (Amp2PassVia_COXnum <= 3):
                            Amp2PassVia_COXnum = 4
                        self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum)
                        self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                        self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum)
                        self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                        # for DRC rule (GR604)
                        if Amp2PassVia_XWidth > 700 and (self.getXYBot('Amp2PassViaM12M2', '_Met2Layer')[0][1] - self.getXYTop('PassTr', 'PassDM2Routing')[-1][1]) <= _DRCObj._MetalxMinSpace10:
                            del self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']
                            del self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates']
                            self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                            self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum - 2)
                            self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                            self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                            self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum - 2)
                            self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                    else:
                        self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('OPAmp', 'PIN_OUT')[0][1]],
                                                                                         [self.getXY('PassTr', 'PassGM3Routing')[-1][0] +
                                                                                          self.getXWidth('PassTr', 'PassGM3Routing') / 2, self.getXY('OPAmp', 'PIN_OUT')[0][1]]]]


                    print('***************************************** Pass Tr - Cap Routing ****************************************')
                    # Pass Tr. Drain ~ Output Cap (M3)
                    self._DesignParameter['Pass2CapM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                              _Width=self.getYWidth('PassTr', 'PassDM2Routing'), _XYCoordinates=[])
                    self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'] = [[[self.getXY('PassTr', 'PassDM2TieRouting')[0][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                                      self.getXY('OutCap')[0][1]],
                                                                                     [self.getXY('OutCap', 'OutCapViaPoly')[-1][0] + self.getWidth('OutCap', 'OutCapMet2PolyRouting') / 2,
                                                                                      self.getXY('OutCap')[0][1]]]]

                    Pass2CapVia_XWidth = self.getWidth('OutCap', 'OutCapMet2PolyRouting')
                    Pass2CapVia_YWidth = self.getWidth('Pass2CapM3Routing')
                    Pass2CapVia_COXnum = int((Pass2CapVia_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) - 1
                    Pass2CapVia_COYnum = int((Pass2CapVia_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1

                    # for DRC rule
                    if (Pass2CapVia_XWidth > 330) & (Pass2CapVia_COXnum < 3):
                        Pass2CapVia_COXnum = 3
                    if (Pass2CapVia_YWidth > 330) & (Pass2CapVia_COYnum < 3):
                        Pass2CapVia_COYnum = 3
                    if (Pass2CapVia_XWidth > 460) & (Pass2CapVia_COXnum * Pass2CapVia_COYnum <= 3):
                        Pass2CapVia_COXnum = 4
                    if (Pass2CapVia_YWidth > 460) & (Pass2CapVia_COXnum * Pass2CapVia_COYnum <= 3):
                        Pass2CapVia_COYnum = 4

                    tmp = []
                    for i in range(0, OutCap_NumofGates):
                        tmp.append([self.getXY('OutCap', 'OutCapViaPoly')[(OutCap_NumofOD + 1) * i][0], self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'][0][0][1]])
                    self._DesignParameter['Pass2CapVia'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Pass2CapViaIn{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Pass2CapVia']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Pass2CapVia_COXnum, _ViaMet22Met3NumberOfCOY=Pass2CapVia_COYnum)
                    self._DesignParameter['Pass2CapVia']['_XYCoordinates'] = tmp
                    del tmp

                    self._DesignParameter['Pass2CapVia2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Pass2CapVia2In{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Pass2CapVia2']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=Pass2CapVia_COYnum)
                    self._DesignParameter['Pass2CapVia2']['_XYCoordinates'] = [[self.getXY('PassTr', 'PassDM2TieRouting')[0][0],
                                                                                self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'][0][0][1]]]

                    # Coord re-setting when Pass ring width < Res ring width
                    if Pass_subXWidth < Res_sub_width:
                        # self._DesignParameter['Pass2ResM2Routing_add1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                        #                                                                                _Width=self.getWidth('Pass2CapM3Routing'), _XYCoordinates=[])
                        # self._DesignParameter['Pass2ResM2Routing_add1']['_XYCoordinates'] = [[[self.getXY('PassTr', 'PassDM2TieRouting')[0][0],
                        #                                                                        self.getXY('PassTr', 'PassDM2TieRouting')[0][1]],
                        #                                                                       [self.getXY('Pass2ResM2Routing')[0][-1][0],
                        #                                                                        self.getXY('PassTr', 'PassDM2TieRouting')[0][1]]]]
                        # self._DesignParameter['Pass2ResM2Routing_add2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                        #                                                                                _Width=self.getXWidth('PassTr', 'PassDM2TieRouting'), _XYCoordinates=[])
                        # self._DesignParameter['Pass2ResM2Routing_add2']['_XYCoordinates'] = [[[self.getXY('Pass2ResM2Routing')[0][-1][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                        #                                                                        self.getXY('PassTr', 'PassDM2TieRouting')[0][1]],
                        #                                                                       [self.getXY('Pass2ResM2Routing')[0][-1][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                        #                                                                        self.getXY('Pass2ResM2Routing')[0][-1][1]]]]

                        self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'] = [[[self.getXY('Pass2ResM2Routing_add2')[-1][0][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                                          self.getXY('OutCap')[0][1]],
                                                                                         [self.getXY('OutCap', 'OutCapViaPoly')[-1][0] + self.getWidth('OutCap', 'OutCapMet2PolyRouting') / 2,
                                                                                          self.getXY('OutCap')[0][1]]]]
                        self._DesignParameter['Pass2CapVia2']['_XYCoordinates'] = [[self.getXY('Pass2ResM2Routing_add2')[-1][0][0],
                                                                                    self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'][0][0][1]]]

                    if self.getXYBot('PassTr', 'PassDM2TieRouting')[0][1] > self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'][0][0][1] - self.getWidth('Pass2CapM3Routing') / 2:
                        self._DesignParameter['Pass2CapM2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                  _Width=self.getXWidth('PassTr', 'PassDM2TieRouting'), _XYCoordinates=[])
                        if Pass_subXWidth < Res_sub_width:
                            self._DesignParameter['Pass2CapM2Routing']['_XYCoordinates'] = [[[self.getXY('Pass2ResM2Routing_add2')[-1][-1][0], self.getXY('PassTr', 'PassDM2TieRouting')[0][1]],
                                                                                             [self.getXY('Pass2ResM2Routing_add2')[-1][-1][0],
                                                                                              self.getXY('OutCap')[0][1] - self.getWidth('Pass2CapM3Routing') / 2]]]
                        else:
                            self._DesignParameter['Pass2CapM2Routing']['_XYCoordinates'] = [[[self.getXY('PassTr', 'PassDM2TieRouting')[0][0], self.getXY('PassTr', 'PassDM2TieRouting')[0][1]],
                                                                                             [self.getXY('PassTr', 'PassDM2TieRouting')[0][0],
                                                                                              self.getXY('OutCap')[0][1] - self.getWidth('Pass2CapM3Routing') / 2]]]


                else:
                    print('***************************************** Amp - Pass Tr Routing ****************************************')
                    # Amp OUT ~ Pass Tr. Gate (M3)
                    self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                              _Width=self.getYWidth('PassTr', 'PolyGateRouting'), _XYCoordinates=[])
                    if PassTr_col == 1:
                        pass
                    elif PassTr_col == 2:
                        self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                         [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                        # for DRC rule (overlap with routing & amp D-OUT via)
                        if (self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2) >= self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]:
                            M3diff = abs((self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2
                                          - self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]))
                            del self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates']
                            self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                      _Width=self.getYWidth('PassTr', 'PolyGateRouting') - M3diff * 3, _XYCoordinates=[])
                            self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                             [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                        Amp2PassVia_XWidth = self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] - self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]
                        Amp2PassVia_XCoord = (self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] + self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]) / 2
                        Amp2PassVia_YWidth = self.getWidth('Amp2PassM3Routing')
                        Amp2PassVia_COXnum = int((Amp2PassVia_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) - 1
                        Amp2PassVia_COYnum = int((Amp2PassVia_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1
                        if (Amp2PassVia_XWidth > 330) & (Amp2PassVia_COXnum < 3):
                            Amp2PassVia_COXnum = 3
                        if (Amp2PassVia_XWidth > 460) & (Amp2PassVia_COXnum <= 3):
                            Amp2PassVia_COXnum = 4
                        self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum)
                        self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                        self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum)
                        self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                        # for DRC rule (GR604)
                        if Amp2PassVia_XWidth > 700 and (self.getXYBot('Amp2PassViaM12M2', '_Met2Layer')[0][1] - self.getXYTop('PassTr', 'PassDM2Routing')[-1][1]) <= _DRCObj._MetalxMinSpace10:
                            del self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']
                            del self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates']
                            self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                            self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum - 2)
                            self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                            self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                            self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum - 2)
                            self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                    else:
                        self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('OPAmp', 'PIN_OUT')[0][1]],
                                                                                         [self.getXY('PassTr', 'PassGM3Routing')[-1][0] + self.getXWidth('PassTr', 'PassGM3Routing') / 2,
                                                                                          self.getXY('OPAmp', 'PIN_OUT')[0][1]]]]




            else:
                if InsertOutCap == True:
                    print('***************************************** OutCap Coord setting *****************************************')
                    self._DesignParameter['OutCap'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=LDO_Outcap._OutCap(_Name='OutCapIn{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['OutCap']['_DesignObj']._CalculateDesignParameter(OutCap=True,
                                                                                            OutCap_XWidth=OutCap_XWidth,
                                                                                            OutCap_YWidth=OutCap_YWidth,
                                                                                            OutCap_NumofGates=OutCap_NumofGates,
                                                                                            OutCap_NumofOD=OutCap_NumofOD,
                                                                                            OutCap_RingWidth=OutCap_RingWidth,
                                                                                            OutCap_RingHeight=OutCap_RingHeight,
                                                                                            _GuardringCOpitch=_GuardringCOpitch,
                                                                                            _GuardringThickness=_GuardringThickness,
                                                                                            _GuardringEnclosure=_GuardringEnclosure)
                    self._DesignParameter['OutCap']['_XYCoordinates'] = [[0, 0]]

                    SpacebtwAmpPass = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_NWLayer')[0][0] - self.getXYLeft('PassTr', 'NSubRing', 'leftupper', '_NWLayer')[0][0])
                    Cap_subXWidth = self.getXYRight('OutCap', 'PSubRing', 'rightupper', '_Met1Layer')[0][0] - self.getXYLeft('OutCap', 'PSubRing', 'leftupper', '_Met1Layer')[0][0]
                    Cap_subYWidth = self.getXYTop('OutCap', 'PSubRing', 'topright', '_Met1Layer')[0][1] - self.getXYBot('OutCap', 'PSubRing', 'botright', '_Met1Layer')[0][1]

                    if pass_subring_height <= amp_subring_height:
                        Cap_XCoord = self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_NWLayer')[0][0] + SpacebtwAmpPass + Cap_subXWidth / 2 + _GuardringEnclosure
                        Cap_Ycoord = self.getXYBot('PassTr' , 'NSubRing', 'botright', '_NWLayer')[0][1] - SpacebtwAmpPass - Cap_subYWidth / 2 - _GuardringEnclosure
                    else:
                        Cap_XCoord = self.getXYRight('PassTr', 'NSubRing', 'rightupper', '_NWLayer')[0][0] + SpacebtwAmpPass + Cap_subXWidth / 2 + _GuardringEnclosure
                        Cap_Ycoord = tmpampYCenter

                    self._DesignParameter['OutCap']['_XYCoordinates'][0][0] = Cap_XCoord
                    self._DesignParameter['OutCap']['_XYCoordinates'][0][1] = Cap_Ycoord


                    print('***************************************** Amp - Pass Tr Routing ****************************************')
                    # Amp OUT ~ Pass Tr. Gate (M3)
                    self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                              _Width=self.getYWidth('PassTr', 'PolyGateRouting'), _XYCoordinates=[])
                    if PassTr_col == 1:
                        pass
                    elif PassTr_col == 2:
                        self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                         [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                        # for DRC rule (overlap with routing & amp D-OUT via)
                        if (self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2) >= self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]:
                            M3diff = abs((self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2
                                          - self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]))
                            del self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates']
                            self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                      _Width=self.getYWidth('PassTr', 'PolyGateRouting') - M3diff * 3, _XYCoordinates=[])
                            self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                             [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                        Amp2PassVia_XWidth = self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] - self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]
                        Amp2PassVia_XCoord = (self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] + self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]) / 2
                        # # for DRC rule
                        # if self.getWidth('OutCap', 'OutCapMet2PolyRouting') >= 1500:
                        #     Amp2PassVia_XWidth = self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] - self.getXYRight('OutCap', 'OutCapViaPoly', '_Met2Layer')[0][0] - _DRCObj._MetalxMinSpace11
                        #     Amp2PassVia_XCoord = (self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] + self.getXYRight('OutCap', 'OutCapViaPoly', '_Met2Layer')[0][0]) / 2
                        Amp2PassVia_YWidth = self.getWidth('Amp2PassM3Routing')
                        Amp2PassVia_COXnum = int((Amp2PassVia_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) - 1
                        Amp2PassVia_COYnum = int((Amp2PassVia_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1
                        if (Amp2PassVia_XWidth > 330) & (Amp2PassVia_COXnum < 3):
                            Amp2PassVia_COXnum = 3
                        if (Amp2PassVia_XWidth > 460) & (Amp2PassVia_COXnum <= 3):
                            Amp2PassVia_COXnum = 4
                        self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum)
                        self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                        self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum)
                        self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                        # for DRC rule (GR604)
                        if Amp2PassVia_XWidth > 700 and (self.getXYBot('Amp2PassViaM12M2', '_Met2Layer')[0][1] - self.getXYTop('PassTr', 'PassDM2Routing')[-1][1]) <= _DRCObj._MetalxMinSpace10:
                            del self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']
                            del self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates']
                            self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                            self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum - 2)
                            self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                            self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                            self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum - 2)
                            self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                    else:
                        self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('OPAmp', 'PIN_OUT')[0][1]],
                                                                                         [self.getXY('PassTr', 'PassGM3Routing')[-1][0] +
                                                                                          self.getXWidth('PassTr', 'PassGM3Routing') / 2, self.getXY('OPAmp', 'PIN_OUT')[0][1]]]]


                    # Amp INP - Pass Drain (M3 - M2)
                    self._DesignParameter['Amp2PassDM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                               _Width=self.getWidth('OPAmp', '_VBMet2Routing'), _XYCoordinates=[])
                    # for DRC(GR604) -> Bottom of <Amp2PassDM3Routing> - Top of Amp N1 Drain M3Via should be >= 0.066
                    dist_btw_amppassM3 = (self.getXY('OPAmp', 'N1PolyGate')[0][1] - self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer') / 2
                                          - (self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][0][1] + self.getXWidth('OPAmp', '_N1Met22Met3Via', '_Met3Layer') / 2))
                    if dist_btw_amppassM3 <= _DRCObj._MetalxMinSpace21:
                        diff_btw_amppassM3 = _DRCObj._MetalxMinSpace21 - dist_btw_amppassM3
                    else:
                        diff_btw_amppassM3 = 0
                    self._DesignParameter['Amp2PassDM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'N1PolyGate')[0][0],
                                                                                       self.getXY('OPAmp', 'N1PolyGate')[0][1] - self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer') / 2 + diff_btw_amppassM3],
                                                                                      [self.getXY('OPAmp', 'N1PolyGate')[0][0],
                                                                                       self.getXY('OPAmp', 'NSubRing', 'botright', '_Met1Layer')[0][1] + self.getWidth('OPAmp', '_VBMet2Routing') / 2]]]

                    self._DesignParameter['Amp2PassDM2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                               _Width=self.getWidth('OPAmp', '_VBMet2Routing'), _XYCoordinates=[])
                    self._DesignParameter['Amp2PassDM2Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'N1PolyGate')[0][0] - self.getWidth('OPAmp', '_VBMet2Routing') / 2,
                                                                                       self.getXY('OPAmp', 'NSubRing', 'botright', '_Met1Layer')[0][1]],
                                                                                      [self.getXY('PassTr', 'PassDM2TieRouting')[-1][0] + self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                                       self.getXY('OPAmp', 'NSubRing', 'botright', '_Met1Layer')[0][1]]]]

                    # Amp INP
                    self._DesignParameter['Amp2PassDViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassDViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Amp2PassDViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
                    self._DesignParameter['Amp2PassDViaM12M2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                    self._DesignParameter['Amp2PassDViaM12M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                    self._DesignParameter['Amp2PassDViaM12M2']['_XYCoordinates'] = [[self._DesignParameter['Amp2PassDM3Routing']['_XYCoordinates'][0][0][0],
                                                                                     self._DesignParameter['Amp2PassDM3Routing']['_XYCoordinates'][0][0][1] + self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer') / 2]]

                    self._DesignParameter['Amp2PassDViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassDViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Amp2PassDViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
                    self._DesignParameter['Amp2PassDViaM22M3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                    self._DesignParameter['Amp2PassDViaM22M3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
                    self._DesignParameter['Amp2PassDViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassDViaM12M2']['_XYCoordinates']

                    # M3 -> M2 @ PMOS subring
                    self._DesignParameter['Amp2PassDViaM22M32'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassDViaM22M32In{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Amp2PassDViaM22M32']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
                    self._DesignParameter['Amp2PassDViaM22M32']['_XYCoordinates'] = [[self._DesignParameter['Amp2PassDM3Routing']['_XYCoordinates'][0][0][0],
                                                                                      self._DesignParameter['Amp2PassDM2Routing']['_XYCoordinates'][0][0][1]]]



                    print('***************************************** Pass Tr - Cap Routing ****************************************')
                    if pass_subring_height <= amp_subring_height:
                        if PassTr_col == 1:
                            pass
                        else:
                            # for DRC rule
                            Pass2M2Routing_Width = self.getWidth('OutCap', 'OutCapMet2PolyRouting')
                            if self.getWidth('OutCap', 'OutCapMet2PolyRouting') > 1500:
                                Pass2M2Routing_Width = 1500
                            # Pass Tr. Drain ~ Output Cap (M3)
                            self._DesignParameter['Pass2CapM2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                      _Width=Pass2M2Routing_Width, _XYCoordinates=[])
                            self._DesignParameter['Pass2CapM2Routing']['_XYCoordinates'] = [[[self.getXY('OutCap', 'OutCapViaPoly')[0][0], self.getXY('OutCap', 'OutCapViaPoly')[-1][1]],
                                                                                             [self.getXY('OutCap', 'OutCapViaPoly')[0][0],
                                                                                              self.getXYBot('PassTr', 'PassDM2TieRouting')[0][1] + self.getYWidth('PassTr', 'PassDM2Routing')]]]
                    else:
                        # Pass Tr. Drain ~ Output Cap (M3)
                        self._DesignParameter['Pass2CapM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                  _Width=self.getYWidth('PassTr', 'PassDM2Routing'), _XYCoordinates=[])
                        self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'] = [[[self.getXY('PassTr', 'PassDM2TieRouting')[0][0] - self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                                          self.getXY('OutCap')[0][1]],
                                                                                         [self.getXY('OutCap', 'OutCapViaPoly')[-1][0] + self.getWidth('OutCap', 'OutCapMet2PolyRouting') / 2,
                                                                                          self.getXY('OutCap')[0][1]]]]

                        Pass2CapVia_XWidth = self.getWidth('OutCap', 'OutCapMet2PolyRouting')
                        Pass2CapVia_YWidth = self.getWidth('Pass2CapM3Routing')
                        Pass2CapVia_COXnum = int((Pass2CapVia_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) - 1
                        Pass2CapVia_COYnum = int((Pass2CapVia_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1

                        # for DRC rule
                        if (Pass2CapVia_XWidth > 330) & (Pass2CapVia_COXnum < 3):
                            Pass2CapVia_COXnum = 3
                        if (Pass2CapVia_YWidth > 330) & (Pass2CapVia_COYnum < 3):
                            Pass2CapVia_COYnum = 3
                        if (Pass2CapVia_XWidth > 460) & (Pass2CapVia_COXnum * Pass2CapVia_COYnum <= 3):
                            Pass2CapVia_COXnum = 4
                        if (Pass2CapVia_YWidth > 460) & (Pass2CapVia_COXnum * Pass2CapVia_COYnum <= 3):
                            Pass2CapVia_COYnum = 4

                        tmp = []
                        for i in range(0, OutCap_NumofGates):
                            tmp.append([self.getXY('OutCap', 'OutCapViaPoly')[(OutCap_NumofOD + 1) * i][0], self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'][0][0][1]])
                        self._DesignParameter['Pass2CapVia'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Pass2CapViaIn{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Pass2CapVia']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Pass2CapVia_COXnum, _ViaMet22Met3NumberOfCOY=Pass2CapVia_COYnum)
                        self._DesignParameter['Pass2CapVia']['_XYCoordinates'] = tmp
                        del tmp

                        self._DesignParameter['Pass2CapVia2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Pass2CapVia2In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Pass2CapVia2']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=Pass2CapVia_COYnum)
                        self._DesignParameter['Pass2CapVia2']['_XYCoordinates'] = [[self.getXY('PassTr', 'PassDM2TieRouting')[0][0],
                                                                                    self._DesignParameter['Pass2CapM3Routing']['_XYCoordinates'][0][0][1]]]

                else:
                    print('***************************************** Amp - Pass Tr Routing ****************************************')
                    # Amp OUT ~ Pass Tr. Gate (M3)
                    self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                              _Width=self.getYWidth('PassTr', 'PolyGateRouting'), _XYCoordinates=[])
                    if PassTr_col == 1:
                        pass
                    elif PassTr_col == 2:
                        self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                         [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                        # for DRC rule (overlap with routing & amp D-OUT via)
                        if (self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2) >= self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]:
                            M3diff = abs((self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2
                                          - self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]))
                            del self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates']
                            self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                      _Width=self.getYWidth('PassTr', 'PolyGateRouting') - M3diff * 3, _XYCoordinates=[])
                            self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                             [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                        Amp2PassVia_XWidth = self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] - self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]
                        Amp2PassVia_XCoord = (self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] + self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]) / 2
                        Amp2PassVia_YWidth = self.getWidth('Amp2PassM3Routing')
                        Amp2PassVia_COXnum = int((Amp2PassVia_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) - 1
                        Amp2PassVia_COYnum = int((Amp2PassVia_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1
                        if (Amp2PassVia_XWidth > 330) & (Amp2PassVia_COXnum < 3):
                            Amp2PassVia_COXnum = 3
                        if (Amp2PassVia_XWidth > 460) & (Amp2PassVia_COXnum <= 3):
                            Amp2PassVia_COXnum = 4
                        self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum)
                        self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                        self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                        self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum)
                        self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                        # for DRC rule (GR604)
                        if Amp2PassVia_XWidth > 700 and (self.getXYBot('Amp2PassViaM12M2', '_Met2Layer')[0][1] - self.getXYTop('PassTr', 'PassDM2Routing')[-1][1]) <= _DRCObj._MetalxMinSpace10:
                            del self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']
                            del self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates']
                            self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                            self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum - 2)
                            self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                            self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                            self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum - 2)
                            self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                    else:
                        self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('OPAmp', 'PIN_OUT')[0][1]],
                                                                                         [self.getXY('PassTr', 'PassGM3Routing')[-1][0] +
                                                                                          self.getXWidth('PassTr', 'PassGM3Routing') / 2, self.getXY('OPAmp', 'PIN_OUT')[0][1]]]]

        else: # Compact_Mode == False
            print('**************************************** Pass Tr. Coord setting ****************************************')
            Nbody_XCoord1 = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_Met1Layer')[0][0]) + _DRCObj._Metal1MinSpace3
            SpacebtwGRMOS = abs(self.getXYBot('OPAmp', 'NSubRing', 'botright', '_Met1Layer')[0][1]) - abs(self.getXYTop('OPAmp', 'PSubRing', 'topright', '_Met1Layer')[0][1])
            PassTr_XCoord = Nbody_XCoord1 + max(SpacebtwGRMOS, _DRCObj._PpMinSpace)
            self._DesignParameter['PassTr']['_XYCoordinates'][0][0] = PassTr_XCoord

            # Adjusting subring's top
            tmpampYCenter = (self.getXY('OPAmp', 'NSubRing', 'topright', '_Met1Layer')[0][1] + self.getXY('OPAmp', 'PSubRing', 'botright', '_Met1Layer')[0][1]) / 2
            tmppassYCenter = (self.getXY('PassTr', 'NSubRing', 'topright', '_Met1Layer')[0][1] + self.getXY('PassTr', 'NSubRing', 'botright', '_Met1Layer')[0][1]) / 2

            SpacebtwAmpPassM1 = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_Met1Layer')[0][0] - self.getXYLeft('PassTr', 'NSubRing', 'leftupper', '_Met1Layer')[0][0])
            self._DesignParameter['PassTr']['_XYCoordinates'][0][1] = tmpampYCenter - tmppassYCenter

            # for DRC rule (GR504)
            if (OutCap_YWidth / 2 >= 1500) & (SpacebtwAmpPassM1 < _DRCObj._MetalxMinSpace11):
                self._DesignParameter['PassTr']['_XYCoordinates'][0][0] += _DRCObj._MetalxMinSpace11 - SpacebtwAmpPassM1


            print('***************************************** Amp - Pass Tr Routing ****************************************')
            # Amp OUT ~ Pass Tr. Gate (M3)
            self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                      _Width=self.getYWidth('PassTr', 'PolyGateRouting'), _XYCoordinates=[])
            if PassTr_col == 1:
                pass
            elif PassTr_col == 2:
                self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                 [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                # for DRC rule (overlap with routing & amp D-OUT via)
                if (self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2) >= self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]:
                    M3diff = abs((self.getXY('PassTr', 'PolyGateRouting')[0][1] + self.getYWidth('PassTr', 'PolyGateRouting') / 2
                                  - self.getXYBot('OPAmp', '_OUTMet22Met3Via', '_Met3Layer')[0][1]))
                    del self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates']
                    self._DesignParameter['Amp2PassM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                              _Width=self.getYWidth('PassTr', 'PolyGateRouting') - M3diff * 3, _XYCoordinates=[])
                    self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]],
                                                                                     [self.getXY('PassTr', 'PolyGateRouting')[0][0], self.getXY('PassTr', 'PolyGateRouting')[0][1]]]]

                Amp2PassVia_XWidth = self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] - self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]
                Amp2PassVia_XCoord = (self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][-1][0] + self.getXYLeft('PassTr', 'PolyGateRouting')[0][0]) / 2
                Amp2PassVia_YWidth = self.getWidth('Amp2PassM3Routing')
                Amp2PassVia_COXnum = int((Amp2PassVia_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) - 1
                Amp2PassVia_COYnum = int((Amp2PassVia_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1
                if (Amp2PassVia_XWidth > 330) & (Amp2PassVia_COXnum < 3):
                    Amp2PassVia_COXnum = 3
                if (Amp2PassVia_XWidth > 460) & (Amp2PassVia_COXnum <= 3):
                    Amp2PassVia_COXnum = 4
                self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum)
                self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum)
                self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

                # for DRC rule (GR604)
                if Amp2PassVia_XWidth > 700 and (self.getXYBot('Amp2PassViaM12M2', '_Met2Layer')[0][1] - self.getXYTop('PassTr', 'PassDM2Routing')[-1][1]) <= _DRCObj._MetalxMinSpace10:
                    del self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']
                    del self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates']
                    self._DesignParameter['Amp2PassViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Amp2PassViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=Amp2PassVia_COXnum, _ViaMet12Met2NumberOfCOY=Amp2PassVia_COYnum - 2)
                    self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates'] = [[Amp2PassVia_XCoord, self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'][0][0][1]]]
                    self._DesignParameter['Amp2PassViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Amp2PassViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=Amp2PassVia_COXnum, _ViaMet22Met3NumberOfCOY=Amp2PassVia_COYnum - 2)
                    self._DesignParameter['Amp2PassViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassViaM12M2']['_XYCoordinates']

            else:
                self._DesignParameter['Amp2PassM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'PIN_OUT')[0][0], self.getXY('OPAmp', 'PIN_OUT')[0][1]],
                                                                                 [self.getXY('PassTr', 'PassGM3Routing')[-1][0] +
                                                                                  self.getXWidth('PassTr', 'PassGM3Routing') / 2, self.getXY('OPAmp', 'PIN_OUT')[0][1]]]]


            # Amp INP - Pass Drain (M3 - M2)
            self._DesignParameter['Amp2PassDM3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                       _Width=self.getWidth('OPAmp', '_VBMet2Routing'), _XYCoordinates=[])
            # for DRC(GR604) -> Bottom of <Amp2PassDM3Routing> - Top of Amp N1 Drain M3Via should be >= 0.066
            dist_btw_amppassM3 = (self.getXY('OPAmp', 'N1PolyGate')[0][1] - self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer') / 2
                                  - (self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][0][1] + self.getXWidth('OPAmp', '_N1Met22Met3Via', '_Met3Layer') / 2))
            if dist_btw_amppassM3 <= _DRCObj._MetalxMinSpace21:
                diff_btw_amppassM3 = _DRCObj._MetalxMinSpace21 - dist_btw_amppassM3
            else:
                diff_btw_amppassM3 = 0
            self._DesignParameter['Amp2PassDM3Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'N1PolyGate')[0][0],
                                                                               self.getXY('OPAmp', 'N1PolyGate')[0][1] - self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer') / 2 + diff_btw_amppassM3],
                                                                              [self.getXY('OPAmp', 'N1PolyGate')[0][0],
                                                                               self.getXY('OPAmp', 'NSubRing', 'botright', '_Met1Layer')[0][1] + self.getWidth('OPAmp', '_VBMet2Routing') / 2]]]

            self._DesignParameter['Amp2PassDM2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                       _Width=self.getWidth('OPAmp', '_VBMet2Routing'), _XYCoordinates=[])
            self._DesignParameter['Amp2PassDM2Routing']['_XYCoordinates'] = [[[self.getXY('OPAmp', 'N1PolyGate')[0][0] - self.getWidth('OPAmp', '_VBMet2Routing') / 2,
                                                                               self.getXY('OPAmp', 'NSubRing', 'botright', '_Met1Layer')[0][1]],
                                                                              [self.getXY('PassTr', 'PassDM2TieRouting')[-1][0] + self.getXWidth('PassTr', 'PassDM2TieRouting') / 2,
                                                                               self.getXY('OPAmp', 'NSubRing', 'botright', '_Met1Layer')[0][1]]]]

            # Amp INP
            self._DesignParameter['Amp2PassDViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2PassDViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['Amp2PassDViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
            self._DesignParameter['Amp2PassDViaM12M2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
            self._DesignParameter['Amp2PassDViaM12M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
            self._DesignParameter['Amp2PassDViaM12M2']['_XYCoordinates'] = [[self._DesignParameter['Amp2PassDM3Routing']['_XYCoordinates'][0][0][0],
                                                                             self._DesignParameter['Amp2PassDM3Routing']['_XYCoordinates'][0][0][1] + self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer') / 2]]

            self._DesignParameter['Amp2PassDViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassDViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['Amp2PassDViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
            self._DesignParameter['Amp2PassDViaM22M3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
            self._DesignParameter['Amp2PassDViaM22M3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getYWidth('OPAmp', 'N1PolyGate', '_Met1Layer')
            self._DesignParameter['Amp2PassDViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2PassDViaM12M2']['_XYCoordinates']

            # M3 -> M2 @ PMOS subring
            self._DesignParameter['Amp2PassDViaM22M32'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2PassDViaM22M32In{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['Amp2PassDViaM22M32']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
            self._DesignParameter['Amp2PassDViaM22M32']['_XYCoordinates'] = [[self._DesignParameter['Amp2PassDM3Routing']['_XYCoordinates'][0][0][0],
                                                                              self._DesignParameter['Amp2PassDM2Routing']['_XYCoordinates'][0][0][1]]]


            if InsertFbRes == True:
                if InsertOutCap == True: # InsertFbRes == True
                    pass
                else: # InsertFbRes == True & InsertOutCap == False
                    pass
            else: # InsertFbRes == False
                print('************************************* Compensation Cap Res setting *************************************')
                # initial coord setting
                self._DesignParameter['LHP_Res_lower'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=270, _DesignObj=opppcres_b._Opppcres(_Name='LHP_Res_lowerIn{}'.format(_Name)),_XYCoordinates=[])[0]
                self._DesignParameter['LHP_Res_lower']['_DesignObj']._CalculateOpppcresDesignParameter(_ResWidth=Amp_Res_Width,
                                                                                                       _ResLength=Amp_Res_Length,
                                                                                                       _CONUMX=None,
                                                                                                       _CONUMY=1,
                                                                                                       _SeriesStripes=Amp_Res_SeriesStripes,
                                                                                                       _ParallelStripes=Amp_Res_ParallelStripes)
                self._DesignParameter['LHP_Res_lower']['_XYCoordinates'] = [[0, 0]]

                self._DesignParameter['LHP_Res_upper'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=90, _DesignObj=opppcres_b._Opppcres(_Name='LHP_Res_upperIn{}'.format(_Name)),_XYCoordinates=[])[0]
                self._DesignParameter['LHP_Res_upper']['_DesignObj']._CalculateOpppcresDesignParameter(_ResWidth=Amp_Res_Width,
                                                                                                       _ResLength=Amp_Res_Length,
                                                                                                       _CONUMX=None,
                                                                                                       _CONUMY=1,
                                                                                                       _SeriesStripes=Amp_Res_SeriesStripes,
                                                                                                       _ParallelStripes=Amp_Res_ParallelStripes)
                self._DesignParameter['LHP_Res_upper']['_XYCoordinates'] = [[0, 0]]

                LHP_RingHeight = self.getXWidth('LHP_Res_lower', '_PRESLayer') + _DRCObj._RXMinSpacetoPRES * 2 + _GuardringEnclosure * 2
                LHP_RingWidth = self.getYWidth('LHP_Res_lower', '_PRESLayer') + _DRCObj._RXMinSpacetoPRES * 2 + _GuardringEnclosure * 2
                self._DesignParameter['LHP_ResRing'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=SubRing._SubRing(_Name='LHP_ResRingIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['LHP_ResRing']['_DesignObj']._CalculateDesignParameter(_Psubtype=True,
                                                                                             _MetalOpen=None,
                                                                                             _Height=LHP_RingHeight,
                                                                                             _Width=LHP_RingWidth,
                                                                                             _Thickness=_GuardringThickness,
                                                                                             _COpitch=_GuardringCOpitch,
                                                                                             _Enclosure=_GuardringEnclosure)
                self._DesignParameter['LHP_ResRing']['_XYCoordinates'] = [[0, 0], [0, 0]]

                self._DesignParameter['Comp_Cap_lower'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=LDO_Outcap._OutCap(_Name='Comp_Cap_lowerIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Comp_Cap_lower']['_DesignObj']._CalculateDesignParameter(OutCap=False,
                                                                                                OutCap_XWidth=Amp_NCAP_XWidth,
                                                                                                OutCap_YWidth=Amp_NCAP_YWidth,
                                                                                                OutCap_NumofGates=Amp_NCAP_NumofGate,
                                                                                                OutCap_NumofOD=Amp_NCAP_NumofRX,
                                                                                                OutCap_RingWidth=None,
                                                                                                OutCap_RingHeight=None,
                                                                                                _GuardringCOpitch=_GuardringCOpitch,
                                                                                                _GuardringThickness=_GuardringThickness,
                                                                                                _GuardringEnclosure=_GuardringEnclosure)
                self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'] = [[0, 0]]

                self._DesignParameter['Comp_Cap_upper'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=90, _DesignObj=LDO_Outcap._OutCap(_Name='Comp_Cap_upperIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Comp_Cap_upper']['_DesignObj']._CalculateDesignParameter(OutCap=False,
                                                                                                OutCap_XWidth=Amp_NCAP_XWidth,
                                                                                                OutCap_YWidth=Amp_NCAP_YWidth,
                                                                                                OutCap_NumofGates=Amp_NCAP_NumofGate,
                                                                                                OutCap_NumofOD=Amp_NCAP_NumofRX,
                                                                                                OutCap_RingWidth=None,
                                                                                                OutCap_RingHeight=None,
                                                                                                _GuardringCOpitch=_GuardringCOpitch,
                                                                                                _GuardringThickness=_GuardringThickness,
                                                                                                _GuardringEnclosure=_GuardringEnclosure)
                self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'] = [[0, 0]]

                # resetting the coord
                SpacebtwAmpPass = abs(self.getXYRight('OPAmp', 'NSubRing', 'rightupper', '_NWLayer')[0][0] - self.getXYLeft('PassTr', 'NSubRing', 'leftupper', '_NWLayer')[0][0])
                LHP_RingXCoord = (self.getXYLeft('PassTr', 'NSubRing', 'leftupper', '_NWLayer')[0][0]
                                  - SpacebtwAmpPass - LHP_RingWidth / 2 - _GuardringThickness - _GuardringEnclosure)
                LHP_RingYCoord1 = (self.getXYBot('OPAmp', 'PSubRing', 'botright', '_PPLayer')[0][1]
                                   - 2000 - LHP_RingHeight / 2 - _GuardringThickness - _GuardringEnclosure) # lower
                LHP_RingYCoord2 = (self.getXYTop('OPAmp', 'NSubRing', 'topright', '_NWLayer')[0][1]
                                   + 2000 + LHP_RingHeight / 2 + _GuardringThickness + _GuardringEnclosure) # upper
                self._DesignParameter['LHP_ResRing']['_XYCoordinates'] = [[LHP_RingXCoord, LHP_RingYCoord1], [LHP_RingXCoord, LHP_RingYCoord2]]

                Res_Ycenter = self.getXWidth('LHP_Res_lower', '_PRESLayer') / 2 - (_DRCObj._PRESlayeroverPoly + Amp_Res_Width / 2)
                LHP_ResYCoord1 = LHP_RingYCoord1 + Res_Ycenter
                LHP_ResYCoord2 = LHP_RingYCoord2 - Res_Ycenter
                self._DesignParameter['LHP_Res_lower']['_XYCoordinates'] = [[LHP_RingXCoord, LHP_ResYCoord1]]
                self._DesignParameter['LHP_Res_upper']['_XYCoordinates'] = [[LHP_RingXCoord, LHP_ResYCoord2]]

                CompCap_RingXWidth = self.getYWidth('Comp_Cap_lower', 'OutCap', 'NWELL') + 2 * _DRCObj._NwMinSpacetoRX + _GuardringEnclosure * 2
                CompCap_RingYWidth = self.getXWidth('Comp_Cap_lower', 'OutCap', 'NWELL') + 2 * _DRCObj._NwMinSpacetoRX + _GuardringEnclosure * 2
                CompCap_RingXCoord = (self.getXYLeft('LHP_ResRing', 'leftupper', '_PPLayer')[0][0]
                                      - SpacebtwAmpPass - CompCap_RingXWidth / 2 - _GuardringThickness - _GuardringEnclosure)
                CompCap_RingYCoord1 = (self.getXYBot('OPAmp', 'PSubRing', 'botright', '_PPLayer')[0][1]
                                       - 2000 - CompCap_RingYWidth / 2 - _GuardringThickness - _GuardringEnclosure)  # lower
                CompCap_RingYCoord2 = (self.getXYTop('OPAmp', 'NSubRing', 'topright', '_NWLayer')[0][1]
                                       + 2000 + CompCap_RingYWidth / 2 + _GuardringThickness + _GuardringEnclosure)  # upper
                self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'] = [[CompCap_RingXCoord, CompCap_RingYCoord1]]
                self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'] = [[CompCap_RingXCoord, CompCap_RingYCoord2]]


                print('************************************* Compensation Cap Res routing *************************************')
                # Amp OUT - Comp Res (M3)
                self._DesignParameter['Amp2CompRM3Routing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                               _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                               _XWidth=self.getWidth('OPAmp', '_OUTMet3Routing'),
                                                                                               _YWidth=self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][1] - self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][1]
                                                                                                       + self.getXWidth('LHP_Res_upper', '_Met1Layer'),
                                                                                               _XYCoordinates=[[self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][0][0],
                                                                                                                (self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][0][1]
                                                                                                                 + self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][-1][1]) / 2]])

                # for DRC (Amp OUT - Comp Res via (TBD) & Guardring M1 spacing) -> Change M1 to M3 & reset via coord (GR504)
                if abs(self.getXYRight('Amp2CompRM3Routing')[0][0] - self.getXYLeft('LHP_ResRing', 'rightupper', '_Met1Layer')[0][0]) <= _DRCObj._Metal1MinSpace3:
                    # Amp OUT - Comp Res (M3)
                    self._DesignParameter['Amp2CompRM3Routing_add'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                   _Width=self.getXWidth('LHP_Res_upper', '_Met1Layer'), _XYCoordinates=[])
                    tmp = self._DesignParameter['LHP_Res_upper']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']
                    tmp.sort(key=lambda x: (x[1], x[0]))
                    self._DesignParameter['Amp2CompRM3Routing_add']['_XYCoordinates'] = [[[self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][0] + tmp[-1][1],
                                                                                           self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][1] + tmp[0][0]],
                                                                                          [self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][0][0]
                                                                                           + self.getWidth('OPAmp', '_OUTMet3Routing') / 2,
                                                                                           self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][1] + tmp[0][0]]],
                                                                                         [[self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][0] + tmp[-1][1],
                                                                                           self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][1] + tmp[0][0]],
                                                                                          [self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][0][0]
                                                                                           + self.getWidth('OPAmp', '_OUTMet3Routing') / 2,
                                                                                           self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][1] + tmp[0][0]]]]
                else:
                    # Amp OUT - Comp Res (M1)
                    self._DesignParameter['Amp2CompRM1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                               _Width=self.getXWidth('LHP_Res_upper', '_Met1Layer'), _XYCoordinates=[])
                    tmp = self._DesignParameter['LHP_Res_upper']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']
                    tmp.sort(key=lambda x: (x[1], x[0]))
                    self._DesignParameter['Amp2CompRM1Routing']['_XYCoordinates'] = [[[self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][0] + tmp[-1][1],
                                                                                       self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][1] + tmp[0][0]],
                                                                                      [self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][0][0]
                                                                                       + self.getWidth('OPAmp', '_OUTMet3Routing') / 2,
                                                                                       self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][1] + tmp[0][0]]],
                                                                                     [[self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][0] + tmp[-1][1],
                                                                                       self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][1] + tmp[0][0]],
                                                                                      [self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_OUTMet3Routing']['_XYCoordinates'][0][0][0]
                                                                                       + self.getWidth('OPAmp', '_OUTMet3Routing') / 2,
                                                                                       self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][1] + tmp[0][0]]]]


                Amp2CompRVia_COYnum = int((self.getXWidth('LHP_Res_upper', '_Met1Layer') - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1
                if (self.getXWidth('LHP_Res_upper', '_Met1Layer') > 330) & (Amp2CompRVia_COYnum < 3):
                    Amp2CompRVia_COYnum = 3
                if (self.getXWidth('LHP_Res_upper', '_Met1Layer') > 460) & (Amp2CompRVia_COYnum <= 3):
                    Amp2CompRVia_COYnum = 4
                self._DesignParameter['Amp2CompRViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Amp2CompRViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2CompRViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=Amp2CompRVia_COYnum)
                self._DesignParameter['Amp2CompRViaM12M2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                self._DesignParameter['Amp2CompRViaM12M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                self._DesignParameter['Amp2CompRViaM12M2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('LHP_Res_upper', '_Met1Layer')
                self._DesignParameter['Amp2CompRViaM12M2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getXWidth('LHP_Res_upper', '_Met1Layer')

                self._DesignParameter['Amp2CompRViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2CompRViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2CompRViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=Amp2CompRVia_COYnum)
                self._DesignParameter['Amp2CompRViaM22M3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                self._DesignParameter['Amp2CompRViaM22M3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                self._DesignParameter['Amp2CompRViaM22M3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getXWidth('LHP_Res_upper', '_Met1Layer')
                self._DesignParameter['Amp2CompRViaM22M3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self.getXWidth('LHP_Res_upper', '_Met1Layer')

                if abs(self.getXYRight('Amp2CompRM3Routing')[0][0] - self.getXYLeft('LHP_ResRing', 'rightupper', '_Met1Layer')[0][0]) <= _DRCObj._Metal1MinSpace3:
                    self._DesignParameter['Amp2CompRViaM12M2']['_XYCoordinates'] = [[self._DesignParameter['Amp2CompRM3Routing_add']['_XYCoordinates'][0][0][0],
                                                                                     self._DesignParameter['Amp2CompRM3Routing_add']['_XYCoordinates'][0][0][1]],
                                                                                    [self._DesignParameter['Amp2CompRM3Routing_add']['_XYCoordinates'][0][0][0],
                                                                                     self._DesignParameter['Amp2CompRM3Routing_add']['_XYCoordinates'][-1][-1][1]]]
                else:
                    self._DesignParameter['Amp2CompRViaM12M2']['_XYCoordinates'] = [[self.getXY('Amp2CompRM3Routing')[0][0],
                                                                                     self._DesignParameter['Amp2CompRM1Routing']['_XYCoordinates'][0][0][1]],
                                                                                    [self.getXY('Amp2CompRM3Routing')[0][0],
                                                                                     self._DesignParameter['Amp2CompRM1Routing']['_XYCoordinates'][-1][-1][1]]]
                self._DesignParameter['Amp2CompRViaM22M3']['_XYCoordinates'] = self._DesignParameter['Amp2CompRViaM12M2']['_XYCoordinates']


                # Comp Cap - Comp Res (M2)
                tmp2 = self._DesignParameter['Comp_Cap_lower']['_DesignObj']._DesignParameter['OutCapMet2RXRouting']['_XYCoordinates']
                tmp2.sort()
                self._DesignParameter['CompM2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                      _Width=self.getWidth('Comp_Cap_lower', 'OutCapMet2RXRouting'), _XYCoordinates=[])
                if Amp_Res_SeriesStripes % 2 == 0:
                    self._DesignParameter['CompM2Routing']['_XYCoordinates'] = [[[self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][0] + tmp[-1][1],
                                                                                  self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][1] + tmp[-1][0]],
                                                                                 [self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][0] + tmp[-1][1],
                                                                                  self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] + tmp2[-1][-1][0]],
                                                                                 [self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][0] + tmp2[-1][-1][1],
                                                                                  self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] + tmp2[-1][-1][0]]],
                                                                                [[self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][0] + tmp[-1][1],
                                                                                  self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][1] - tmp[-1][0]],
                                                                                 [self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][0] + tmp[-1][1],
                                                                                  self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1] - tmp2[-1][-1][0]],
                                                                                 [self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][0] + tmp2[-1][-1][1],
                                                                                  self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1] - tmp2[-1][-1][0]]]]
                else:
                    self._DesignParameter['CompM2Routing']['_XYCoordinates'] = [[[self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][0] + tmp[0][1],
                                                                                  self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][1] + tmp[-1][0]],
                                                                                 [self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][0] + tmp[0][1],
                                                                                  self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] + tmp2[-1][-1][0]],
                                                                                 [self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][0] + tmp2[-1][-1][1],
                                                                                  self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] + tmp2[-1][-1][0]]],
                                                                                [[self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][0] + tmp[0][1],
                                                                                  self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][1] - tmp[-1][0]],
                                                                                 [self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][0] + tmp[0][1],
                                                                                  self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1] - tmp2[-1][-1][0]],
                                                                                 [self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][0] + tmp2[-1][-1][1],
                                                                                  self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1] - tmp2[-1][-1][0]]]]

                CompVia_COYnum = int((self.getXWidth('LHP_Res_upper', '_Met1Layer') - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1
                if (self.getXWidth('LHP_Res_upper', '_Met1Layer') > 330) & (CompVia_COYnum < 3):
                    CompVia_COYnum = 3
                if (self.getXWidth('LHP_Res_upper', '_Met1Layer') > 460) & (CompVia_COYnum <= 3):
                    CompVia_COYnum = 4
                self._DesignParameter['CompViaM12M2'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='CompViaM12M2In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['CompViaM12M2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=CompVia_COYnum)
                self._DesignParameter['CompViaM12M2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getWidth('CompM2Routing')
                self._DesignParameter['CompViaM12M2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('LHP_Res_upper', '_Met1Layer')
                self._DesignParameter['CompViaM12M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getWidth('CompM2Routing')
                self._DesignParameter['CompViaM12M2']['_XYCoordinates'] = [[self.getXY('CompM2Routing')[0][0][0],
                                                                            self._DesignParameter['LHP_Res_upper']['_XYCoordinates'][0][1] + tmp[-1][0]],
                                                                           [self.getXY('CompM2Routing')[0][0][0],
                                                                            self._DesignParameter['LHP_Res_lower']['_XYCoordinates'][0][1] - tmp[-1][0]]]
                                                                            # self.getXY('CompM2Routing')[1][0][1] - self.getXWidth('LHP_Res_upper', '_Met1Layer') / 2]]
                del tmp, tmp2


                # Amp 1-stage output - Comp Cap (M3)
                tmp = self._DesignParameter['Comp_Cap_lower']['_DesignObj']._DesignParameter['OutCapMet2PolyRouting']['_XYCoordinates']
                tmp.sort()
                # for DRC
                Amp2CompC_XCoord = self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_P2Met3Routing']['_XYCoordinates'][0][0][0]
                # amp-cap & amp-res M3 spacing
                if abs(Amp2CompC_XCoord + self.getWidth('OPAmp', '_OUTMet3Routing') / 2 - self.getXYLeft('Amp2CompRM3Routing')[0][0]) <= _DRCObj._MetalxMinSpace5:
                    Amp2CompC_XCoord = (self.getXY('Amp2CompRM3Routing')[0][0] + self.getXY('Amp2PassDM3Routing')[0][0][0]) / 2
                # amp-cap & Cap Poly routing M2 spacing
                elif self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][0] + tmp[-1][-1][1] + _DRCObj._MetalxMinWidth / 2 - (Amp2CompC_XCoord + self.getWidth('OPAmp', '_OUTMet3Routing') / 2) <= _DRCObj._MetalxMinSpace:
                    Amp2CompC_XCoord = (self.getXY('Amp2CompRM3Routing')[0][0] + self.getXY('Amp2PassDM3Routing')[0][0][0]) / 2

                self._DesignParameter['Amp2CompCM3Routing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                               _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                               _XWidth=self.getWidth('OPAmp', '_OUTMet3Routing'),
                                                                                               _YWidth=self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] + tmp[-1][-1][0]
                                                                                                       - self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1] + tmp[-1][-1][0]
                                                                                                       + self.getWidth('Comp_Cap_lower', 'OutCapMet2PolyRouting'),
                                                                                               _XYCoordinates=[[Amp2CompC_XCoord,
                                                                                                                (self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] +
                                                                                                                 self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1]) / 2]])


                Amp2CompCVia_COYnum = int((self.getWidth('Comp_Cap_lower', 'OutCapMet2PolyRouting') - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace2)) - 1
                if (self.getWidth('Comp_Cap_lower', 'OutCapMet2PolyRouting') > 330) & (Amp2CompRVia_COYnum < 3):
                    Amp2CompCVia_COYnum = 3
                if (self.getWidth('Comp_Cap_lower', 'OutCapMet2PolyRouting') > 460) & (Amp2CompRVia_COYnum <= 3):
                    Amp2CompCVia_COYnum = 4
                self._DesignParameter['Amp2CompCViaM22M3'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Amp2CompCViaM22M3In{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['Amp2CompCViaM22M3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=Amp2CompCVia_COYnum)
                self._DesignParameter['Amp2CompCViaM22M3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                self._DesignParameter['Amp2CompCViaM22M3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                for i in range(0, Amp_NCAP_NumofGate):
                    self._DesignParameter['Amp2CompCViaM22M3']['_XYCoordinates'].append([self.getXY('Amp2CompCM3Routing')[0][0], self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] + tmp[i][0][0]])
                    self._DesignParameter['Amp2CompCViaM22M3']['_XYCoordinates'].append([self.getXY('Amp2CompCM3Routing')[0][0], self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1] - tmp[i][0][0]])

                # Additional M2 for Amp Out - Comp Cap
                if self.getXYRight('Amp2CompCViaM22M3', '_Met2Layer')[0][0] > self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][0] + tmp[-1][-1][1]:
                    self._DesignParameter['Amp2CompCM2Routing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                   _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                   _XWidth=self.getXYRight('Amp2CompCViaM22M3', '_Met2Layer')[0][0]
                                                                                                           - (self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][0] + tmp[-1][-1][1]),
                                                                                                   _YWidth=self.getWidth('Comp_Cap_lower', 'OutCapMet2PolyRouting'),
                                                                                                   _XYCoordinates=[])
                    for i in range(len(self._DesignParameter['Amp2CompCViaM22M3']['_XYCoordinates'])):
                        self._DesignParameter['Amp2CompCM2Routing']['_XYCoordinates'].append([(self.getXYRight('Amp2CompCViaM22M3', '_Met2Layer')[0][0]
                                                                                               + (self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][0] + tmp[-1][-1][1])) / 2,
                                                                                              self.getXY('Amp2CompCViaM22M3')[i][1]])

                # for DRC (routing - N1 drain(M3) spacing) -> change to M4 routing (GR604)
                if self.getXYLeft('Amp2CompCM3Routing')[0][0] - self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][-1][0] - self.getYWidth('OPAmp', '_N1Met22Met3Via', '_Met3Layer') / 2 <= _DRCObj._MetalxMinSpace21:
                    del self._DesignParameter['Amp2CompCM3Routing']['_XYCoordinates'][0]
                    self._DesignParameter['Amp2CompCM4Routing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                                                   _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                                   _XWidth=self.getWidth('OPAmp', '_OUTMet3Routing'),
                                                                                                   _YWidth=self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] + tmp[-1][-1][0]
                                                                                                           - self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1] + tmp[-1][-1][0]
                                                                                                           + self.getWidth('Comp_Cap_lower', 'OutCapMet2PolyRouting'),
                                                                                                   _XYCoordinates=[[Amp2CompC_XCoord,
                                                                                                                    (self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][1] +
                                                                                                                     self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][1]) / 2]])
                    self._DesignParameter['Amp2CompCViaM32M4'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Amp2CompCViaM32M4In{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Amp2CompCViaM32M4']['_DesignObj']._CalculateViaMet32Met4DesignParameter(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=Amp2CompCVia_COYnum)
                    self._DesignParameter['Amp2CompCViaM32M4']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                    self._DesignParameter['Amp2CompCViaM32M4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                    self._DesignParameter['Amp2CompCViaM32M4']['_XYCoordinates'] = self._DesignParameter['Amp2CompCViaM22M3']['_XYCoordinates']

                    self._DesignParameter['Amp2CompCViaM32M4_add'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Amp2CompCViaM32M4_addIn{}'.format(_Name)), _XYCoordinates=[])[0]
                    self._DesignParameter['Amp2CompCViaM32M4_add']['_DesignObj']._CalculateViaMet32Met4DesignParameter(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=1)
                    self._DesignParameter['Amp2CompCViaM32M4_add']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                    self._DesignParameter['Amp2CompCViaM32M4_add']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] = self.getXWidth('Amp2CompRM3Routing')
                    self._DesignParameter['Amp2CompCViaM32M4_add']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self.getYWidth('OPAmp', '_N1Met22Met3Via', '_Met3Layer')
                    self._DesignParameter['Amp2CompCViaM32M4_add']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] = self.getYWidth('OPAmp', '_N1Met22Met3Via', '_Met3Layer')
                    self._DesignParameter['Amp2CompCViaM32M4_add']['_XYCoordinates'] = [[self.getXY('Amp2CompCM4Routing')[0][0], self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['_N1Met22Met3Via']['_XYCoordinates'][-1][1]],
                                                                                        [self.getXY('Amp2CompCM4Routing')[0][0], self._DesignParameter['OPAmp']['_DesignObj']._DesignParameter['P2PolyGate']['_XYCoordinates'][0][1]]]

                del tmp


                if InsertOutCap == True: # InsertFbRes == False
                    pass
                else: # InsertFbRes == False & InsertOutCap == False
                    pass


        # Additional NWell Layer
        self._DesignParameter['NWLayer1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                             _XWidth=self.getXYRight('PassTr', 'NSubRing', 'rightupper', '_NWLayer')[0][0]
                                                                                     - self.getXYLeft('OPAmp', 'NWLayer')[0][0],
                                                                             _YWidth=self.getYWidth('OPAmp', 'NWLayer'),
                                                                             _XYCoordinates=[[(self.getXYRight('PassTr', 'NSubRing', 'rightupper', '_NWLayer')[0][0]
                                                                                               + self.getXYLeft('OPAmp', 'NWLayer')[0][0]) / 2,
                                                                                              self.getXY('OPAmp', 'NWLayer')[0][1]]])



        print('******************************************** PIN Generation ********************************************')
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VSS')

        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VDD')

        self._DesignParameter['PIN_VREF'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VREF')

        self._DesignParameter['PIN_VOUT'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='VOUT')

        self._DesignParameter['PIN_VSS']['_XYCoordinates'] = [self.getXY('OPAmp', 'PSubRing', 'corner')[0]]
        self._DesignParameter['PIN_VDD']['_XYCoordinates'] = [self.getXY('OPAmp', 'NSubRing', 'corner')[0], self.getXY('PassTr', 'NSubRing', 'corner')[0]]
        self._DesignParameter['PIN_VREF']['_XYCoordinates'] = self.getXY('OPAmp', 'N0PolyGate')
        self._DesignParameter['PIN_VOUT']['_XYCoordinates'] = [self.getXY('PassTr', 'PassDM2TieRouting')[0]]

        if InsertFbRes == True:
            self._DesignParameter['PIN_VSS']['_XYCoordinates'].append(self.getXY('FbRes', 'PSubRing_Res', 'corner')[0])
        if InsertOutCap == True:
            self._DesignParameter['PIN_VSS']['_XYCoordinates'].append(self.getXY('OutCap', 'PSubRing', 'corner')[0])
        if Compact_Mode == False:
            self._DesignParameter['PIN_VSS']['_XYCoordinates'].append(self.getXY('LHP_ResRing', 'corner')[0])
            self._DesignParameter['PIN_VSS']['_XYCoordinates'].append([self._DesignParameter['Comp_Cap_lower']['_XYCoordinates'][0][0],
                                                                       self.getXY('LHP_ResRing', 'corner')[0][1]])
            self._DesignParameter['PIN_VSS']['_XYCoordinates'].append([self._DesignParameter['Comp_Cap_upper']['_XYCoordinates'][0][0],
                                                                       self.getXY('LHP_ResRing', 'corner')[1][1]])