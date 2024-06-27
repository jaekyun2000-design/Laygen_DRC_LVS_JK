from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

from generatorLib.generator_models.LDO_gen import PassTr_unit
from generatorLib.generator_models.LDO_gen import SubRing
from generatorLib.generator_models.LDO_gen import ViaMet12Met2
from generatorLib.generator_models.LDO_gen import ViaMet22Met3

class _PassTr(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='_PassTr'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameter(self,
                                  Finger=10,
                                  ChannelLength=30,
                                  ChannelWidth=1000,   # DRC: <1.211(when finger > 10) -> <=1190
                                  NumofMOS_row=4,
                                  NumofMOS_col=1,
                                  _XVT='RVT',
                                  UnitHeight=4068, # distance btw NbodyContact center
                                  PassTr_RingHeight=None,
                                  PassTr_RingWidth=None,
                                  _NbodyCOpitch=175,
                                  _NbodyThickness=348,
                                  _NbodyNWEnclosure=56
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        def roundReal(val, digits):
            return round(val+10**(-len(str(val))-1), digits)


        print('#########################################################################################################')
        print('                                       {}  Pass Tr Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        Parameters_unit = dict(
            Finger=Finger,
            ChannelLength=ChannelLength,
            ChannelWidth=ChannelWidth,
            GateSpacing=None,
            _SDWidth=None,
            NumofMOS_row=NumofMOS_row,
            _XVT=_XVT,

            _NbodyCOpitch=_NbodyCOpitch,
            _NbodyThickness=_NbodyThickness,
            _NbodyNWEnclosure=_NbodyNWEnclosure
        )

        print('******************************************* Locate instances *******************************************')
        # Pass Tr. parameter rules
        if NumofMOS_col < 1:
            raise Exception("PassTr_col should be at least 1")
        elif NumofMOS_col == 1:
            pass
        elif NumofMOS_col % 2 == 1:
            raise Exception("PassTr_col should be even number (except 1)")

        self._DesignParameter['PassTrUnit'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PassTr_unit._PassTrUnit(_Name='PassTrUnitIn{}'.format(_Name)), _XYCoordinates = [])[0]
        self._DesignParameter['PassTrUnit']['_DesignObj']._CalculateDesignParameter(**Parameters_unit)

        self._DesignParameter['PassTrUnit_init'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PassTr_unit._PassTrUnit(_Name='PassTrUnit_initIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['PassTrUnit_init']['_DesignObj']._CalculateDesignParameter(**Parameters_unit)

        self._DesignParameter['PassTrUnit_flipped'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=PassTr_unit._PassTrUnit(_Name='PassTrUnitFlipIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['PassTrUnit_flipped']['_DesignObj']._CalculateDesignParameter(**Parameters_unit)

        self._DesignParameter['PassTrUnit_flipped_init'] = self._SrefElementDeclaration(_Reflect=[1, 0, 0], _Angle=0, _DesignObj=PassTr_unit._PassTrUnit(_Name='PassTrUnitFlip_initIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['PassTrUnit_flipped_init']['_DesignObj']._CalculateDesignParameter(**Parameters_unit)

        if NumofMOS_col == 1:
            self._DesignParameter['PassTrUnit']['_XYCoordinates'] = [[0, 0]]

        else:
            if NumofMOS_col % 2 == 1:
                self._DesignParameter['PassTrUnit_init']['_XYCoordinates'] = [[0, 0]]

                if UnitHeight != None:
                    SpacebtwUnit = UnitHeight - abs(self.getXY('PassTrUnit_init', 'NbodyContact')[1][1]) * 2
                    NbodyOverlap = abs(self.getXY('PassTrUnit_init', 'NbodyContact')[1][1]) * 2
                else:
                    SpacebtwUnit = abs(self.getXY('PassTrUnit_init', 'NbodyContact')[0][1]) * 2
                    NbodyOverlap = abs(self.getXY('PassTrUnit_init', 'NbodyContact')[1][1]) * 2

                for i in range(1, NumofMOS_col // 2 + 1):
                    if len(self.getXY('PassTrUnit')) < 1:
                        self._DesignParameter['PassTrUnit_flipped']['_XYCoordinates'].append([0, self.getXY('PassTrUnit_init')[-1][1] + NbodyOverlap])
                    else:
                        self._DesignParameter['PassTrUnit_flipped']['_XYCoordinates'].append([0, self.getXY('PassTrUnit')[-1][1] + NbodyOverlap])
                    self._DesignParameter['PassTrUnit']['_XYCoordinates'].append([0, self.getXY('PassTrUnit_flipped')[-1][1] + SpacebtwUnit])

            else:
                self._DesignParameter['PassTrUnit_flipped_init']['_XYCoordinates'] = [[0, 0]]

                if UnitHeight != None:
                    SpacebtwUnit = UnitHeight - abs(self.getXY('PassTrUnit_flipped_init', 'NbodyContact')[1][1]) * 2
                    NbodyOverlap = abs(self.getXY('PassTrUnit_flipped_init', 'NbodyContact')[1][1]) * 2
                else:
                    SpacebtwUnit = abs(self.getXY('PassTrUnit_flipped_init', 'NbodyContact')[0][1]) * 2
                    NbodyOverlap = abs(self.getXY('PassTrUnit_flipped_init', 'NbodyContact')[1][1]) * 2

                self._DesignParameter['PassTrUnit_init']['_XYCoordinates'] = [[0, self.getXY('PassTrUnit_flipped_init')[-1][1] + SpacebtwUnit]]

                for i in range(2, NumofMOS_col // 2 + 1):
                    if len(self.getXY('PassTrUnit')) < 1:
                        self._DesignParameter['PassTrUnit_flipped']['_XYCoordinates'].append([0, self.getXY('PassTrUnit_init')[-1][1] + NbodyOverlap])
                    else:
                        self._DesignParameter['PassTrUnit_flipped']['_XYCoordinates'].append([0, self.getXY('PassTrUnit')[-1][1] + NbodyOverlap])
                    self._DesignParameter['PassTrUnit']['_XYCoordinates'].append([0, self.getXY('PassTrUnit_flipped')[-1][1] + SpacebtwUnit])



            print('******************************************* PolyGate Routing *******************************************')
            _RoutingXWidth = (self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['PolyGateRouting']['_XYCoordinates'][0][-1][0]
                              - self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['PolyGateRouting']['_XYCoordinates'][0][0][0])
            # for DRC, reset Pass Tr. Gate routing
            SpacebtwGateBody = self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['PolyGateRouting']['_XYCoordinates'][0][0][0] - self.getXYLeft('PassTrUnit_init', 'NbodyContact', '_Met1Layer')[0][0]
            if (SpacebtwGateBody < _DRCObj._MetalxMinSpace11) & (_RoutingXWidth > 1500):
                _RoutingXWidth -= (_DRCObj._MetalxMinSpace11 - SpacebtwGateBody) * 2

            if NumofMOS_col > 2:
                _RoutingYWidth = self.getXYTop('PassTrUnit', 'PMOSPolyGate', '_Met1Layer')[-1][1] - self.getXYBot('PassTrUnit_flipped', 'PMOSPolyGate', '_Met1Layer')[-1][1]
            else:
                _RoutingYWidth = self.getXYTop('PassTrUnit_init', 'PMOSPolyGate', '_Met1Layer')[-1][1] - self.getXYBot('PassTrUnit_flipped_init', 'PMOSPolyGate', '_Met1Layer')[-1][1]
            self._DesignParameter['PolyGateRouting'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=_RoutingXWidth,
                                                                                        _YWidth=_RoutingYWidth,
                                                                                        _XYCoordinates=[])

            if len(self.getXY('PassTrUnit_flipped_init')) >= 1 and len(self.getXY('PassTrUnit_init')) >= 1:
                self._DesignParameter['PolyGateRouting']['_XYCoordinates'].append([self.getXY('PassTrUnit_init', 'NbodyContact')[0][0], (self.getXY('PassTrUnit_init')[0][1] + self.getXY('PassTrUnit_flipped_init')[0][1]) / 2])
            for i in range(1, NumofMOS_col // 2):
                self._DesignParameter['PolyGateRouting']['_XYCoordinates'].append([self.getXY('PassTrUnit', 'NbodyContact')[0][0], (self.getXY('PassTrUnit')[i-1][1] + self.getXY('PassTrUnit_flipped')[i-1][1]) / 2])

            if NumofMOS_col % 2 == 0: del self._DesignParameter['PassTrUnit_init']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]
            del self._DesignParameter['PassTrUnit_flipped_init']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]
            del self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]
            del self._DesignParameter['PassTrUnit_flipped']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]



        print('******************************************* Subring Setting ********************************************')
        if NumofMOS_col == 1:
            PassTr_totalYWidth = (self.getXYTop('PassTrUnit', 'NbodyContact', '_Met1Layer')[-1][1] -
                                  self.getXYBot('PassTrUnit', 'NbodyContact', '_Met1Layer')[0][1])
            Nbody_YCoord = (self.getXYTop('PassTrUnit', 'NbodyContact', '_Met1Layer')[-1][1] +
                            self.getXYBot('PassTrUnit', 'NbodyContact', '_Met1Layer')[0][1]) / 2
        elif NumofMOS_col == 2:
            PassTr_totalYWidth = (self.getXYTop('PassTrUnit_init', 'NbodyContact', '_Met1Layer')[-1][1] -
                                  self.getXYBot('PassTrUnit_flipped_init', 'NbodyContact', '_Met1Layer')[0][1])
            Nbody_YCoord = (self.getXYTop('PassTrUnit_init', 'NbodyContact', '_Met1Layer')[-1][1] +
                            self.getXYBot('PassTrUnit_flipped_init', 'NbodyContact', '_Met1Layer')[0][1]) / 2
        elif NumofMOS_col % 2 == 1:
            PassTr_totalYWidth = (self.getXYTop('PassTrUnit', 'NbodyContact', '_Met1Layer')[-1][1] -
                                  self.getXYBot('PassTrUnit_init', 'NbodyContact', '_Met1Layer')[0][1])
            Nbody_YCoord = (self.getXYTop('PassTrUnit', 'NbodyContact', '_Met1Layer')[-1][1] +
                            self.getXYBot('PassTrUnit_init', 'NbodyContact', '_Met1Layer')[0][1]) / 2
        else:
            PassTr_totalYWidth = (self.getXYTop('PassTrUnit', 'NbodyContact', '_Met1Layer')[-1][1] -
                                  self.getXYBot('PassTrUnit_flipped_init', 'NbodyContact', '_Met1Layer')[0][1])
            Nbody_YCoord = (self.getXYTop('PassTrUnit', 'NbodyContact', '_Met1Layer')[-1][1] +
                            self.getXYBot('PassTrUnit_flipped_init', 'NbodyContact', '_Met1Layer')[0][1]) / 2

        # Add NSubRing
        if PassTr_RingHeight == None:
            NsubRingHeight = PassTr_totalYWidth - 2 * _NbodyThickness
        else:
            NsubRingHeight = PassTr_RingHeight
        if PassTr_RingWidth == None:
            NsubRingWidth = self.getXWidth('PassTrUnit', 'NbodyContact', '_Met1Layer') + _DRCObj._MetalxMinSpace41 * 2 + _NbodyNWEnclosure * 2
        else:
            NsubRingWidth = PassTr_RingWidth

        if NumofMOS_col == 1:
            NsubXYCoord = [[(self.getXY('PassTrUnit', 'PMOS')[-1][0] +
                             self.getXY('PassTrUnit', 'PMOS')[0][0]) / 2, Nbody_YCoord]]
        elif NumofMOS_col == 2:
            NsubXYCoord = [[(self.getXY('PassTrUnit_init', 'PMOS')[-1][0] +
                             self.getXY('PassTrUnit_init', 'PMOS')[0][0]) / 2, Nbody_YCoord]]
        else:
            NsubXYCoord = [[(self.getXY('PassTrUnit', 'PMOS')[-1][0] +
                             self.getXY('PassTrUnit', 'PMOS')[0][0]) / 2, Nbody_YCoord]]

        self._DesignParameter['NSubRing'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=SubRing._SubRing(_Name='NSubRingIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['NSubRing']['_DesignObj']._CalculateDesignParameter(_Psubtype=False,
                                                                                  _MetalOpen=None,
                                                                                  _Height=NsubRingHeight,
                                                                                  _Width=NsubRingWidth,
                                                                                  _Thickness=_NbodyThickness,
                                                                                  _COpitch=_NbodyCOpitch,
                                                                                  _Enclosure=_NbodyNWEnclosure)
        self._DesignParameter['NSubRing']['_XYCoordinates'] = NsubXYCoord

        # Set reference coordinate
        XCoord_diff = - self.getXYLeft('NSubRing', 'leftlower', '_Met1Layer')[0][0]
        YCoord_diff = - self.getXYBot('NSubRing', 'botleft', '_Met1Layer')[0][1]
        self._DesignParameter['NSubRing']['_XYCoordinates'][0][0] += XCoord_diff
        self._DesignParameter['NSubRing']['_XYCoordinates'][0][1] += YCoord_diff
        if len(self._DesignParameter['PassTrUnit']['_XYCoordinates']) >= 1:
            for i in range(0, len(self._DesignParameter['PassTrUnit']['_XYCoordinates'])):
                self._DesignParameter['PassTrUnit']['_XYCoordinates'][i][0] += XCoord_diff
                self._DesignParameter['PassTrUnit']['_XYCoordinates'][i][1] += YCoord_diff
        if len(self._DesignParameter['PassTrUnit_init']['_XYCoordinates']) >= 1:
            for i in range(0, len(self._DesignParameter['PassTrUnit_init']['_XYCoordinates'])):
                self._DesignParameter['PassTrUnit_init']['_XYCoordinates'][i][0] += XCoord_diff
                self._DesignParameter['PassTrUnit_init']['_XYCoordinates'][i][1] += YCoord_diff
        if len(self._DesignParameter['PassTrUnit_flipped']['_XYCoordinates']) >= 1:
            for i in range(0, len(self._DesignParameter['PassTrUnit_flipped']['_XYCoordinates'])):
                self._DesignParameter['PassTrUnit_flipped']['_XYCoordinates'][i][0] += XCoord_diff
                self._DesignParameter['PassTrUnit_flipped']['_XYCoordinates'][i][1] += YCoord_diff
        if len(self._DesignParameter['PassTrUnit_flipped_init']['_XYCoordinates']) >= 1:
            for i in range(0, len(self._DesignParameter['PassTrUnit_flipped_init']['_XYCoordinates'])):
                self._DesignParameter['PassTrUnit_flipped_init']['_XYCoordinates'][i][0] += XCoord_diff
                self._DesignParameter['PassTrUnit_flipped_init']['_XYCoordinates'][i][1] += YCoord_diff
        if NumofMOS_col > 1:
            if len(self._DesignParameter['PolyGateRouting']['_XYCoordinates']) >= 1:
                for i in range(0, len(self._DesignParameter['PolyGateRouting']['_XYCoordinates'])):
                    self._DesignParameter['PolyGateRouting']['_XYCoordinates'][i][0] += XCoord_diff
                    self._DesignParameter['PolyGateRouting']['_XYCoordinates'][i][1] += YCoord_diff

        if NumofMOS_col == 1:
            # ADD MET1 path & del bodycontact
            del self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]
            del self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][-1]
        else:
            self._DesignParameter['PassM1Routing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                      _XWidth=self.getXYRight('NSubRing', 'rightupper', '_Met1Layer')[0][0]
                                                                                              - self.getXYLeft('NSubRing', 'leftupper', '_Met1Layer')[0][0],
                                                                                      _YWidth=_NbodyThickness, _XYCoordinates=[])
            if NumofMOS_col > 2:
                self._DesignParameter['PassM1Routing']['_XYCoordinates'].append(self.getXY('PassTrUnit_flipped_init', 'NbodyContact', '_Met1Layer')[0])
                self._DesignParameter['PassM1Routing']['_XYCoordinates'].append(self.getXY('PassTrUnit_init', 'NbodyContact', '_Met1Layer')[0])
            for i in range(0, len(self.getXY('PassTrUnit'))):
                if NumofMOS_col > 2:
                    self._DesignParameter['PassM1Routing']['_XYCoordinates'].append(self.getXY('PassTrUnit', 'NbodyContact', '_Met1Layer')[i])
                    self._DesignParameter['PassM1Routing']['_XYCoordinates'].append(self.getXY('PassTrUnit_flipped', 'NbodyContact', '_Met1Layer')[i])
            del self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]
            del self._DesignParameter['PassTrUnit_flipped']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]
            del self._DesignParameter['PassTrUnit_flipped_init']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]
            del self._DesignParameter['PassTrUnit_init']['_DesignObj']._DesignParameter['NbodyContact']['_XYCoordinates'][0]



        print('******************************************** PassTr Routing ********************************************')
        # M2 Routing (amp out ~ pass gate, pass drain rail)
        if NumofMOS_col == 1:
            PassDM2YWidth = self.getYWidth('PassTrUnit', 'PMOS', '_Met1Layer')
        else:
            PassDM2YWidth = self.getYWidth('PassTrUnit', 'PMOS', '_Met1Layer')
        self._DesignParameter['PassDM2Routing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                   _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                   _XWidth=self.getXYRight('NSubRing', 'rightupper', '_Met1Layer')[0][0] -
                                                                                           self.getXYLeft('NSubRing', 'leftupper', '_Met1Layer')[0][0],
                                                                                   _YWidth=PassDM2YWidth,
                                                                                   _XYCoordinates=[])

        PassM2XCoord = self.getXY('NSubRing')[0][0]
        if NumofMOS_col == 1:
            self._DesignParameter['PassDM2Routing']['_XYCoordinates'].append([PassM2XCoord, self.getXY('PassTrUnit')[0][1]])
        else:
            self._DesignParameter['PassDM2Routing']['_XYCoordinates'].append([PassM2XCoord, self.getXY('PassTrUnit_init')[0][1]])
            self._DesignParameter['PassDM2Routing']['_XYCoordinates'].append([PassM2XCoord, self.getXY('PassTrUnit_flipped_init')[0][1]])
            for i in range(0, NumofMOS_col // 2 - 1):
                self._DesignParameter['PassDM2Routing']['_XYCoordinates'].append([PassM2XCoord, self.getXY('PassTrUnit_flipped')[i][1]])
                self._DesignParameter['PassDM2Routing']['_XYCoordinates'].append([PassM2XCoord, self.getXY('PassTrUnit')[i][1]])

            tmp = self.getXY('PassDM2Routing')
            tmp.sort(key=lambda x: (x[1], x[0]))

            self._DesignParameter['PassDM2TieRouting'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                          _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                          _XWidth=_NbodyThickness,
                                                                                          _YWidth=abs(tmp[-1][1] - tmp[0][1]) + self.getYWidth('PassDM2Routing'),
                                                                                          _XYCoordinates=[])
            self._DesignParameter['PassDM2TieRouting']['_XYCoordinates'] = [[self.getXY('NSubRing', 'rightupper', '_Met1Layer')[0][0],
                                                                             (tmp[0][1] + tmp[-1][1]) / 2],
                                                                            [self.getXY('NSubRing', 'leftupper', '_Met1Layer')[0][0],
                                                                             (tmp[0][1] + tmp[-1][1]) / 2]]
            del tmp

        if NumofMOS_col == 1:
            PassDM1M2Via_COXnum = int((self.getYWidth('PassDM2Routing') - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
        else:
            PassDM1M2Via_COXnum = int((self.getYWidth('PassDM2Routing') - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

        COXchangeFlag = 0
        if (self.getYWidth('PassDM2Routing') > 460) & (PassDM1M2Via_COXnum <= 3):
            PassDM1M2Via_COXnum = 4
            COXchangeFlag = 1
        tmp = []
        if NumofMOS_col == 1:
            tmp_Coord = self.getXY('PassTrUnit', 'PMOS', '_Met1Layer')
            tmp_Coord_sort = []
            for i in tmp_Coord:
                if i not in tmp_Coord_sort:
                    tmp_Coord_sort.append(i)
            tmp_Coord_sort.sort(key=lambda x: (x[1], x[0]))

            for k in range(0, len(self.getXY('PassDM2Routing'))):
                for i in range(0, NumofMOS_row):
                    for j in range(0, int(roundReal(Finger / 2, 0))):
                        tmp.append([tmp_Coord_sort[i * (Finger + 1) + 2 * j + 1][0], self.getXY('PassDM2Routing')[k][1]])
        else:
            if NumofMOS_col == 2:
                tmp_Coord1 = self.getXY('PassTrUnit_init', 'PMOS', '_Met1Layer')
                tmp_Coord2 = self.getXY('PassTrUnit_flipped_init', 'PMOS', '_Met1Layer')
                tmp_Coord_sort1 = []
                for i in tmp_Coord1:
                    if i not in tmp_Coord_sort1:
                        tmp_Coord_sort1.append(i)
                tmp_Coord_sort1.sort(key=lambda x: (x[1], x[0]))
                tmp_Coord_sort2 = []
                for i in tmp_Coord2:
                    if i not in tmp_Coord_sort2:
                        tmp_Coord_sort2.append(i)
                tmp_Coord_sort2.sort(key=lambda x: (x[1], x[0]))

                for k in range(0, len(self.getXY('PassDM2Routing'))):
                    for i in range(0, NumofMOS_row):
                        for j in range(0, int(roundReal(Finger / 2, 0))):
                            tmp.append([tmp_Coord_sort1[i * (Finger + 1) + 2 * j + 1][0], self.getXY('PassDM2Routing')[k][1]])
                            tmp.append([tmp_Coord_sort2[i * (Finger + 1) + 2 * j + 1][0], self.getXY('PassDM2Routing')[k][1]])
            else:
                tmp_Coord = self.getXY('PassTrUnit', 'PMOS', '_Met1Layer')
                tmp_Coord_sort = []
                for i in tmp_Coord:
                    if i not in tmp_Coord_sort:
                        tmp_Coord_sort.append(i)
                tmp_Coord_sort.sort(key=lambda x: (x[1], x[0]))

                for k in range(0, len(self.getXY('PassDM2Routing'))):
                    for i in range(0, NumofMOS_row):
                        for j in range(0, int(roundReal(Finger / 2, 0))):
                            tmp.append([tmp_Coord_sort[i * (Finger + 1) + 2 * j + 1][0], self.getXY('PassDM2Routing')[k][1]])

        self._DesignParameter['PassDM1M2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='PassDM1M2ViaIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['PassDM1M2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=PassDM1M2Via_COXnum, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['PassDM1M2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getXWidth('PassTrUnit', 'PMOS', '_Met1Layer')
        self._DesignParameter['PassDM1M2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getXWidth('PassTrUnit', 'PMOS', '_Met1Layer')
        if COXchangeFlag == 1:
            self._DesignParameter['PassDM1M2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getYWidth('PassTrUnit', 'PMOS', '_Met1Layer')
            self._DesignParameter['PassDM1M2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getYWidth('PassTrUnit', 'PMOS', '_Met1Layer')
        self._DesignParameter['PassDM1M2Via']['_XYCoordinates'] = tmp
        del tmp


        # M3 Routing
        if NumofMOS_col > 2:
            tmpPassM3XWidth1 = (self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]
                                - self._DesignParameter['PassTrUnit']['_DesignObj']._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) // 2
            tmpPassM3XWidth2 = self.getXWidth('PolyGateRouting')
            if (tmpPassM3XWidth1 * 3 < self.getXWidth('PolyGateRouting')) & (Finger <= 4):
                PassM3XWidth = tmpPassM3XWidth2
            else:
                PassM3XWidth = tmpPassM3XWidth1

            if PassM3XWidth >= _DRCObj._MetalxMaxWidth:
                PassM3XWidth = _DRCObj._MetalxMaxWidth

            self._DesignParameter['PassGM3Routing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                       _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                       _XWidth=PassM3XWidth,
                                                                                       _YWidth=self.getXYTop('NSubRing', 'topright', '_Met1Layer')[0][1] -
                                                                                               self.getXYBot('NSubRing', 'botright', '_Met1Layer')[0][1],
                                                                                       _XYCoordinates=[])
            if PassM3XWidth == tmpPassM3XWidth1:
                PassM3YCoord = self.getXY('NSubRing')[0][1]
                if NumofMOS_row == 1:
                    self._DesignParameter['PassGM3Routing']['_XYCoordinates'].append([self.getXY('PassTrUnit', 'PMOS')[0][0], PassM3YCoord])
                else:
                    for i in range(NumofMOS_row):
                        self._DesignParameter['PassGM3Routing']['_XYCoordinates'].append([self.getXY('PassTrUnit', 'PMOS')[i * (NumofMOS_col // 2 - 1)][0], PassM3YCoord])
            else:
                self._DesignParameter['PassGM3Routing']['_XYCoordinates'] = self.getXY('NSubRing')

            if PassM3XWidth == tmpPassM3XWidth1:
                PassGM1M3Via_COXnum = int((self.getXWidth('PassGM3Routing') - 2 * _DRCObj._MetalxMinEnclosureCO2 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
            else:
                PassGM1M3Via_COXnum = int((self.getXWidth('PassGM3Routing') - 2 * _DRCObj._MetalxMinEnclosureCO2 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
            tmpViaXWidth = min(self.getXYRight('PassGM3Routing')[0][0] - self.getXYLeft('PolyGateRouting')[0][0], self.getXWidth('PassGM3Routing'))
            PassGM1M3Via_end_COXnum = int((tmpViaXWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace)) - 1
            PassGM1M3Via_COYnum = int((self.getYWidth('PolyGateRouting') - 2 * _DRCObj._CoMinSpace
                                       - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAyMinWidth) // (_DRCObj._VIAyMinWidth + _DRCObj._VIAyMinSpace)) - 1

            # DRC Rule checking
            if PassGM1M3Via_COXnum == 0:
                PassGM1M3Via_COXnum = 1
            if PassGM1M3Via_COYnum == 0:
                PassGM1M3Via_COYnum = 1
            # if (self.getXWidth('PassGM3Routing') > 330) & (PassGM1M3Via_COXnum < 3):
            #     PassGM1M3Via_COXnum = 3
            # if (self.getXWidth('PassGM3Routing') > 460) & (PassGM1M3Via_COXnum < 4) & PassGM1M3Via_COYnum == 1:
            #     PassGM1M3Via_COXnum = 4
            if (self.getXWidth('PassGM3Routing') > 330) & (PassGM1M3Via_COXnum * PassGM1M3Via_COYnum < 3):
                if PassGM1M3Via_COXnum < PassGM1M3Via_COYnum:
                    PassGM1M3Via_COXnum += 1
                else:
                    PassGM1M3Via_COYnum += 1
            if (self.getXWidth('PassGM3Routing') > 440) & (PassGM1M3Via_COXnum * PassGM1M3Via_COYnum < 4):
                if PassGM1M3Via_COXnum < PassGM1M3Via_COYnum:
                    PassGM1M3Via_COXnum += 1
                else:
                    PassGM1M3Via_COYnum += 1

            if (self.getXWidth('PolyGateRouting') > 330) & (PassGM1M3Via_COXnum * PassGM1M3Via_COYnum < 3) & NumofMOS_row == 1:
                if PassGM1M3Via_COXnum < PassGM1M3Via_COYnum:
                    PassGM1M3Via_COXnum += 1
                else:
                    PassGM1M3Via_COYnum += 1
            if (self.getXWidth('PolyGateRouting') > 440) & (PassGM1M3Via_COXnum * PassGM1M3Via_COYnum < 4) & NumofMOS_row == 1:
                if PassGM1M3Via_COXnum < PassGM1M3Via_COYnum:
                    PassGM1M3Via_COXnum += 1
                else:
                    PassGM1M3Via_COYnum += 1


            if ((self.getXWidth('PassGM3Routing') > 330) & (PassGM1M3Via_end_COXnum < 3)) | ((self.getXWidth('PassGM3Routing') > 460) & (PassGM1M3Via_end_COXnum < 4)):
                PassGM1M3Via_end_COXnum = 0

            tmp = []
            tmp1 = []
            for j in range(0, len(self.getXY('PolyGateRouting'))):
                if len(self.getXY('PassGM3Routing')) == 1:
                    tmp.append([self.getXY('PassGM3Routing')[0][0], self.getXY('PolyGateRouting')[j][1]])
                else:
                    for i in range(1, len(self.getXY('PassGM3Routing')) - 1):
                        tmp.append([self.getXY('PassGM3Routing')[i][0], self.getXY('PolyGateRouting')[j][1]])
                    if tmpViaXWidth == self.getXWidth('PassGM3Routing'):
                        tmp1.append([self.getXY('PassGM3Routing')[0][0], self.getXY('PolyGateRouting')[j][1]])
                        tmp1.append([self.getXY('PassGM3Routing')[-1][0], self.getXY('PolyGateRouting')[j][1]])
                    else:
                        tmp1.append([(self.getXYRight('PassGM3Routing')[0][0] + self.getXYLeft('PolyGateRouting')[0][0]) / 2, self.getXY('PolyGateRouting')[j][1]])
                        tmp1.append([(self.getXYLeft('PassGM3Routing')[-1][0] + self.getXYRight('PolyGateRouting')[0][0]) / 2, self.getXY('PolyGateRouting')[j][1]])

            self._DesignParameter['PassGM1M2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='PassGM1M2ViaIn{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['PassGM1M2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=PassGM1M3Via_COXnum, _ViaMet12Met2NumberOfCOY=PassGM1M3Via_COYnum)
            self._DesignParameter['PassGM1M2Via']['_XYCoordinates'] = tmp

            self._DesignParameter['PassGM2M3Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0,_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='PassGM2M3ViaIn{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['PassGM2M3Via']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=PassGM1M3Via_COXnum, _ViaMet22Met3NumberOfCOY=PassGM1M3Via_COYnum)
            self._DesignParameter['PassGM2M3Via']['_XYCoordinates'] = self._DesignParameter['PassGM1M2Via']['_XYCoordinates']

            if PassGM1M3Via_end_COXnum > 0:
                self._DesignParameter['PassGM1M2Via_end'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='PassGM1M2Via_endIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['PassGM1M2Via_end']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=PassGM1M3Via_end_COXnum, _ViaMet12Met2NumberOfCOY=PassGM1M3Via_COYnum)
                self._DesignParameter['PassGM1M2Via_end']['_XYCoordinates'] = tmp1
                self._DesignParameter['PassGM2M3Via_end'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='PassGM2M3Via_endIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['PassGM2M3Via_end']['_DesignObj']._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=PassGM1M3Via_end_COXnum, _ViaMet22Met3NumberOfCOY=PassGM1M3Via_COYnum)
                self._DesignParameter['PassGM2M3Via_end']['_XYCoordinates'] = self._DesignParameter['PassGM1M2Via_end']['_XYCoordinates']
            del tmp, tmp1



        print('*************************************** Additional Layer Setting ***************************************')
        self._DesignParameter['NWLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                            _XWidth=self.getXYRight('NSubRing', 'corner', '_NWLayer')[1][0] -
                                                                                    self.getXYLeft('NSubRing', 'corner', '_NWLayer')[0][0],
                                                                            _YWidth=self.getXYTop('NSubRing', 'corner', '_NWLayer')[0][1] -
                                                                                    self.getXYBot('NSubRing', 'corner', '_NWLayer')[-1][1],
                                                                            _XYCoordinates=self._DesignParameter['NSubRing']['_XYCoordinates'])




# ################################# DRC Check #################################
import random
if __name__ == '__main__':
    # for i in range(0, 100):
    #     Finger = random.randint(2, 50)
    #     ChannelLength = 30
    #     ChannelWidth = random.randrange(300, 1100)
    #     NumofMOS_row = random.randint(2, 10)
    #     NumofMOS_col = random.randrange(2, 10, 2)
    #     _XVT = random.choice(['HVT','RVT','LVT','SLVT'])
    #     UnitHeight = None
    #     PassTr_RingHeight= None
    #     PassTr_RingWidth= None
    #     _NbodyCOpitch = random.randrange(150, 200, 2)
    #     _NbodyThickness = random.randrange(300, 500, 2)
    #     _NbodyNWEnclosure = random.randrange(56, 100, 2)
    #
    #     print(f"{i}nd loop")
    #     print("Finger=", Finger)
    #     print("ChannelLength=", ChannelLength)
    #     print("ChannelWidth=", ChannelWidth)
    #     print("NumofMOS_row=", NumofMOS_row)
    #     print("NumofMOS_col=", NumofMOS_col)
    #     print("_XVT=", _XVT)
    #     print("UnitHeight=", UnitHeight)
    #     print("PassTr_RingHeight=", PassTr_RingHeight)
    #     print("PassTr_RingWidth=", PassTr_RingWidth)
    #     print("_NbodyCOpitch=", _NbodyCOpitch)
    #     print("_NbodyThickness=", _NbodyThickness)
    #     print("_NbodyNWEnclosure=", _NbodyNWEnclosure)

        Finger = 34
        ChannelLength = 30
        ChannelWidth = 1000
        NumofMOS_row = 4
        NumofMOS_col = 4
        _XVT = 'RVT'
        UnitHeight = 4068
        PassTr_RingHeight = None
        PassTr_RingWidht = None
        _NbodyCOpitch = 142
        _NbodyThickness = 348
        _NbodyNWEnclosure = 56



        DesignParameters._Technology = 'SS28nm'
        TopObj = _PassTr(_DesignParameter=None, _Name='_PassTr')
        TopObj._CalculateDesignParameter(
            Finger=Finger,
            ChannelLength=ChannelLength,
            ChannelWidth=ChannelWidth,
            NumofMOS_row = NumofMOS_row,
            NumofMOS_col = NumofMOS_col,
            _XVT = _XVT,
            UnitHeight = UnitHeight,
            PassTr_RingHeight=None,
            PassTr_RingWidth=None,
            _NbodyCOpitch = _NbodyCOpitch,
            _NbodyThickness = _NbodyThickness,
            _NbodyNWEnclosure = _NbodyNWEnclosure
        )
        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./_PassTr.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('#############################      Sending to FTP Server...      ##############################')

        import ftplib

        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('smlim96', 'min753531')
        ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
        myfile = open('./_PassTr.gds', 'rb')
        ftp.storbinary('STOR _PassTr.gds', myfile)
        myfile.close()

        # import DRCchecker
        # a = DRCchecker.DRCchecker('smlim96','min753531','/mnt/sdc/smlim96/OPUS/ss28','/mnt/sdc/smlim96/OPUS/ss28/DRC/run','_PassTr','_PassTr',None)
        # a.DRCchecker()
        # print ("DRC Clean!!!")