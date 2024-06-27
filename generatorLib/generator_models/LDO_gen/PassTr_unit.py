from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models.LDO_gen import NbodyContact
from generatorLib.generator_models import ViaPoly2Met1_resize


class _PassTrUnit(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='_PassTrUnit'):
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
                                  GateSpacing=None,
                                  _SDWidth=None,
                                  NumofMOS_row=4,
                                  _XVT='RVT',

                                  _NbodyCOpitch=142,
                                  _NbodyThickness=348,
                                  _NbodyNWEnclosure=56
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']


        print('#########################################################################################################')
        print('                                     {}  Pass Tr Unit Calculation Start                                  '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        if GateSpacing == None:
            UnitPitch = ChannelLength + _DRCObj._PolygateMinSpace
        else:
            UnitPitch = ChannelLength + GateSpacing

        if Finger <= 1:
            raise NotImplementedError("Number of Finger should be more than 1")

        print('******************************************* Locate instances *******************************************')
        # Pass Transistor (PMOS)
        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PMOSWithDummy._PMOS(_Name='PMOSIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculatePMOSDesignParameter(_PMOSNumberofGate=Finger, _PMOSChannelWidth=ChannelWidth, _PMOSChannellength=ChannelLength,
                                                                                  _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=_SDWidth, _XVT=_XVT)
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, 0]]

        # Poly Gate
        PolyGatePO_YWidth = _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
        PolyGateM1_YWidth = _DRCObj._CoMinWidth + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
        if Finger == 1:
            PolyGate_XWidth = _DRCObj._CoMinWidth + 2 * 4
            PolyGate_COXnum = 1
        elif Finger == 2:
            PolyGate_XWidth = abs(self.getXYLeft('PMOS', '_POLayer')[0][0]) + abs(self.getXYRight('PMOS', '_POLayer')[-1][0])
            PolyGate_COXnum = 2
        else:
            PolyGate_XWidth = abs(self.getXYLeft('PMOS', '_POLayer')[0][0]) + abs(self.getXYRight('PMOS', '_POLayer')[-1][0])
            PolyGate_COXnum = int((PolyGate_XWidth - 2 * _DRCObj._Metal1MinEnclosureCO2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + 1)
        PolyGate_XYCoordinates = [[self.getXY('PMOS')[0][0], self.getXYBot('PMOS', '_ODLayer')[0][1] - _DRCObj._XvtMinEnclosureOfODY - PolyGatePO_YWidth / 2]]
        self._DesignParameter['PMOSPolyGate'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PMOSPolyGateIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['PMOSPolyGate']['_DesignObj']._CalculateDesignParameter(_ViaPoly2Met1NumberOfCOX=PolyGate_COXnum, _ViaPoly2Met1NumberOfCOY=1,
                                                                                      Met1XWidth=None, Met1YWidth=PolyGateM1_YWidth, POXWidth=PolyGate_XWidth, POYWidth=PolyGatePO_YWidth)
        self._DesignParameter['PMOSPolyGate']['_XYCoordinates'] = PolyGate_XYCoordinates

        # NbodyContact
        _NbodyMet1XWidth = (abs(self.getXYLeft('PMOS', '_PODummyLayer')[0][0]) + abs(self.getXYRight('PMOS', '_PODummyLayer')[-1][0])) * NumofMOS_row - ChannelLength * (NumofMOS_row - 1) + _DRCObj._MetalxMinSpace41 * 2
        if _NbodyCOpitch == None:
            _XpitchBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None)
            _YpitchBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None)
        else:
            _XpitchBtwCO = _NbodyCOpitch
            _YpitchBtwCO = _NbodyCOpitch

        _NumofCOX = int((_NbodyMet1XWidth - 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide - _DRCObj._CoMinWidth) // _XpitchBtwCO + 1)
        _NumofCOY = int((_NbodyThickness - 2 * _DRCObj._CoMinEnclosureByOD - _DRCObj._CoMinWidth - _YpitchBtwCO / 2) // _YpitchBtwCO + 1)
        self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact._NbodyContact(_Name='NbodyContactIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(_InputModeArea=False, _NumberOfNbodyCOX=_NumofCOX, _NumberOfNbodyCOY=_NumofCOY,
                                                                                                  _Met1XWidth=_NbodyMet1XWidth, _Met1YWidth=_NbodyThickness,
                                                                                                  _COXpitch=_NbodyCOpitch, _COYpitch=_NbodyCOpitch, _NWEnclosure=_NbodyNWEnclosure)

        self._DesignParameter['PMOSDummy'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                            _XWidth= self.getXWidth('PMOS', '_PODummyLayer'),
                                                                            _YWidth=self.getYWidth('PMOS', '_POLayer'),
                                                                            _XYCoordinates=[])



        print('****************************************** Duplicate instances *****************************************')
        if NumofMOS_row > 1:
            for i in range(1, NumofMOS_row):
                self._DesignParameter['PMOS']['_XYCoordinates'].append([self.getXY('PMOS')[i-1][0] + (Finger / 2 + 0.5) * UnitPitch + (Finger / 2 + 0.5) * UnitPitch, self.getXY('PMOS')[i-1][1]])
                self._DesignParameter['PMOSPolyGate']['_XYCoordinates'].append([self.getXY('PMOS')[i][0], self.getXYBot('PMOS', '_ODLayer')[i-1][1] - _DRCObj._XvtMinEnclosureOfODY - PolyGatePO_YWidth / 2])
                NbodyContact_XCoord = (abs(self.getXY('PMOS')[0][0]) + abs(self.getXY('PMOS')[-1][0])) / 2

        else:
            NbodyContact_XCoord = self.getXY('PMOS')[0][0]
        self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[NbodyContact_XCoord, self.getXYBot('PMOSPolyGate', '_POLayer')[0][1] - 115 - _NbodyThickness / 2],
                                                                   [NbodyContact_XCoord, abs(self.getXYBot('PMOSPolyGate', '_POLayer')[0][1]) + _DRCObj._MetalxMinSpace41 + _NbodyThickness / 2]]

        self._DesignParameter['PMOSDummy']['_XYCoordinates'] = self.getXY('PMOS', '_PODummyLayer')



        print('********************************************** VDD Routing *********************************************')
        self._DesignParameter['VDDRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getXWidth('PMOS', '_Met1Layer'), _XYCoordinates=[])
        tmp_Coord = self.getXY('PMOS', '_Met1Layer')
        tmp_Coord.sort()

        tmp = []
        if NumofMOS_row == 1:
            for j in range(0, Finger // 2 + 1):
                tmp.append([[tmp_Coord[2 * j][0], tmp_Coord[2 * j][1]],
                            [tmp_Coord[2 * j][0], self.getXYTop('NbodyContact', '_Met1Layer')[-1][1]]])
        else:
            for i in range(0, NumofMOS_row):
                for j in range(0, Finger // 2 + 1):
                    tmp.append([[tmp_Coord[i * (Finger + 1) + 2 * j][0], tmp_Coord[i * (Finger + 1) + 2 * j][1]],
                                [tmp_Coord[i * (Finger + 1) + 2 * j][0], self.getXYTop('NbodyContact', '_Met1Layer')[-1][1]]])
        self._DesignParameter['VDDRouting']['_XYCoordinates'] = tmp
        del tmp



        print('******************************************* PolyGate Routing *******************************************')
        self._DesignParameter['PolyGateRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self.getYWidth('PMOSPolyGate', '_Met1Layer'), _XYCoordinates=[])
        self._DesignParameter['PolyGateRouting']['_XYCoordinates'] = [[[self.getXYLeft('PMOSPolyGate', '_Met1Layer')[0][0], self.getXY('PMOSPolyGate', '_Met1Layer')[0][1]],
                                                                       [self.getXYRight('PMOSPolyGate', '_Met1Layer')[-1][0],self.getXY('PMOSPolyGate', '_Met1Layer')[0][1]]]]



        print('*************************************** Additional Layer Setting ***************************************')
        # Add BP, XVT, NWELL Layer
        self._DesignParameter['PPLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                            _XWidth= self.getXYRight('PMOS', '_PPLayer')[-1][0] - self.getXYLeft('PMOS', '_PPLayer')[0][0],
                                                                            _YWidth=self.getYWidth('PMOS', '_PPLayer'),
                                                                            _XYCoordinates=[[(self.getXYRight('PMOS', '_PPLayer')[-1][0] + self.getXYLeft('PMOS', '_PPLayer')[0][0]) / 2, 0]])

        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping[_XVT][0], _Datatype=DesignParameters._LayerMapping[_XVT][1],
                                                                             _XWidth=self.getXYRight('PMOS', '_ODLayer')[-1][0] - self.getXYLeft('PMOS', '_ODLayer')[0][0] + 2 * _DRCObj._XvtMinEnclosureOfODX,
                                                                             _YWidth=self.getYWidth('PMOS', '_ODLayer') + 2 * _DRCObj._XvtMinEnclosureOfODY,
                                                                             _XYCoordinates=self.getXY('PPLayer'))

        self._DesignParameter['NWLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                            _XWidth=self.getXYRight('NbodyContact', '_NWLayer')[0][0] - self.getXYLeft('NbodyContact', '_NWLayer')[0][0],
                                                                            _YWidth=self.getXYTop('NbodyContact', '_NWLayer')[-1][1] - self.getXYBot('NbodyContact', '_NWLayer')[0][1],
                                                                            _XYCoordinates=[[self.getXY('PPLayer')[0][0], (self.getXYTop('NbodyContact', '_NWLayer')[-1][1] + self.getXYBot('NbodyContact', '_NWLayer')[0][1]) / 2]])


# ################################# DRC Check #################################
# import random
# if __name__ == '__main__':
#     # for i in range(0, 100):
#     #     Finger = random.randint(2, 100)
#     #     ChannelLength = 30
#     #     ChannelWidth = random.randrange(300, 1200)
#     #     GateSpacing = None
#     #     _SDWidth = None
#     #     NumofMOS_row = random.randint(1, 10)
#     #     _XVT = 'RVT'
#     #
#     #     _NbodyCOpitch = 142
#     #     _NbodyThickness = 348
#     #     _NbodyNWEnclosure = 56
#
#         Finger = 34
#         ChannelLength = 30
#         ChannelWidth = 1000
#         GateSpacing = None
#         _SDWidth = None
#         NumofMOS_row = 4
#         _XVT = 'RVT'
#
#         _NbodyCOpitch = 142
#         _NbodyThickness = 348
#         _NbodyNWEnclosure = 56
#
#         # print(f"{i}nd loop")
#         # print("Finger=", Finger)
#         # print("ChannelLength=", ChannelLength)
#         # print("ChannelWidth=", ChannelWidth)
#         # print("GateSpacing=", GateSpacing)
#         # print("_SDWidth=", _SDWidth)
#         # print("NumofMOS_row=", NumofMOS_row)
#         # print("_XVT=", _XVT)
#         # print("_NbodyCOpitch=", _NbodyCOpitch)
#         # print("_NbodyThickness=", _NbodyThickness)
#         # print("_NbodyNWEnclosure=", _NbodyNWEnclosure)
#
#
#
#         DesignParameters._Technology = 'SS28nm'
#         TopObj = _PassTrUnit(_DesignParameter=None, _Name='_PassTrUnit')
#         TopObj._CalculateDesignParameter(
#             Finger=Finger,
#             ChannelLength=ChannelLength,
#             ChannelWidth=ChannelWidth,
#             GateSpacing=GateSpacing,
#             _SDWidth=_SDWidth,
#             NumofMOS_row = NumofMOS_row,
#             _XVT = _XVT,
#
#             _NbodyCOpitch = _NbodyCOpitch,
#             _NbodyThickness = _NbodyThickness,
#             _NbodyNWEnclosure = _NbodyNWEnclosure
#         )
#         TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
#         testStreamFile = open('./_PassTrUnit.gds', 'wb')
#         tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
#         tmp.write_binary_gds_stream(testStreamFile)
#         testStreamFile.close()
#
#         print('#############################      Sending to FTP Server...      ##############################')
#
#         import ftplib
#
#         ftp = ftplib.FTP('141.223.24.53')
#         ftp.login('smlim96', 'min753531')
#         ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
#         myfile = open('./_PassTrUnit.gds', 'rb')
#         ftp.storbinary('STOR _PassTrUnit.gds', myfile)
#         myfile.close()
#
#     #     import DRCchecker
#     #     a = DRCchecker.DRCchecker('smlim96','min753531','/mnt/sdc/smlim96/OPUS/ss28','/mnt/sdc/smlim96/OPUS/ss28/DRC/run','_PassTrUnit','_PassTrUnit',None)
#     #     a.DRCchecker()
#     #
#     #
#     # print ("DRC Clean!!!")