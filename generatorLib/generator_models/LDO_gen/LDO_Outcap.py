from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

from generatorLib.generator_models.LDO_gen import NCAP
from generatorLib.generator_models.LDO_gen import SubRing
from generatorLib.generator_models import ViaMet12Met2


class _OutCap(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='_LDO'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameter(self,
                                  OutCap=True,
                                  OutCap_XWidth=3000,
                                  OutCap_YWidth=2078,
                                  OutCap_NumofGates=5,
                                  OutCap_NumofOD=4,
                                  OutCap_RingWidth=None,
                                  OutCap_RingHeight=None,
                                  _GuardringCOpitch=175,
                                  _GuardringThickness=348,
                                  _GuardringEnclosure=56
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']


        print('#########################################################################################################')
        print('                                  {}  Output Cap Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        Parameters_OutCap = dict(
            _XWidth=OutCap_XWidth,
            _YWidth=OutCap_YWidth,
            _NumofGates=OutCap_NumofGates,
            _NumofOD=OutCap_NumofOD,
            NumOfCOX=None,
            NumOfCOY=None,
            Guardring=False
        )


        # Output Cap.
        self._DesignParameter['OutCap'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NCAP._NCap(_Name='OutCapIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['OutCap']['_DesignObj']._CalculateNCapDesignParameter(**Parameters_OutCap)


        print('****************************************** Output Cap Setting ******************************************')
        # Output Cap Setting
        self._DesignParameter['OutCap']['_XYCoordinates'] = [[0, 0]]

        # for DRC rule (GR504e2)
        if OutCap_YWidth >= 3000:
            proper_ringwidth = (self.getXYRight('OutCap', 'Viapoly2Met1V', '_Met1Layer')[-1][0] - self.getXYLeft('OutCap', 'Viapoly2Met1V', '_Met1Layer')[0][0]
                                 + _DRCObj._MetalxMinSpace11 * 2)
        else:
            proper_ringwidth = self.getXWidth('OutCap', 'NWELL') + 2 * _DRCObj._NwMinSpacetoRX + _GuardringEnclosure * 2

        if OutCap_RingHeight == None:
            PsubringHeight = self.getYWidth('OutCap', 'NWELL') + 2 * _DRCObj._NwMinSpacetoRX + _GuardringEnclosure * 2
        else:
            PsubringHeight = OutCap_RingHeight
            if OutCap_RingHeight <= self.getYWidth('OutCap', 'NWELL') + 2 * _DRCObj._NwMinSpacetoRX + _GuardringEnclosure * 2:
                raise Exception("<OutCap_RingHeight> should be larger")

        if OutCap_RingWidth == None:
            # PsubringWidth = self.getXWidth('OutCap', 'NWELL') + 2 * _DRCObj._NwMinSpacetoRX + _GuardringEnclosure * 2
            PsubringWidth = proper_ringwidth
        else:
            PsubringWidth = OutCap_RingWidth
            # if OutCap_RingHeight <= self.getXWidth('OutCap', 'NWELL') + 2 * _DRCObj._NwMinSpacetoRX + _GuardringEnclosure * 2:
            if OutCap_RingHeight <= proper_ringwidth:
                raise Exception("<OutCap_RingWidth> should be larger")

        self._DesignParameter['PSubRing'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=SubRing._SubRing(_Name='PSubRingIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['PSubRing']['_DesignObj']._CalculateDesignParameter(_Psubtype=True, _MetalOpen=None,
                                                                                  _Height=PsubringHeight,
                                                                                  _Width=PsubringWidth,
                                                                                  _Thickness=_GuardringThickness,
                                                                                  _COpitch=_GuardringCOpitch,
                                                                                  _Enclosure=_GuardringEnclosure)
        self._DesignParameter['PSubRing']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['OutCap']['_XYCoordinates'] = self.getXY('PSubRing')


        print('****************************************** Output Cap Routing ******************************************')
        # RX Metal1 Routing
        self._DesignParameter['OutCapMet1RXRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _Width=OutCap_YWidth / 2, _XYCoordinates=[])
        tmp = []
        if OutCap == True:
            for i in range(0, OutCap_NumofOD):
                tmp.append([[self.getXYLeft('PSubRing', 'leftupper', '_Met1Layer')[0][0],
                              self.getXY('OutCap', 'Viapoly2Met1V')[i][1]],
                             [self.getXYRight('PSubRing', 'rightupper', '_Met1Layer')[0][0],
                              self.getXY('OutCap', 'Viapoly2Met1V')[OutCap_NumofOD * OutCap_NumofGates + i][1]]])
        else:
            for i in range(0, OutCap_NumofOD):
                tmp.append([[self.getXY('OutCap', 'Viapoly2Met1V')[i][0],
                             self.getXY('OutCap', 'Viapoly2Met1V')[i][1]],
                            [self.getXY('OutCap', 'Viapoly2Met1V')[OutCap_NumofOD * OutCap_NumofGates + i][0],
                             self.getXY('OutCap', 'Viapoly2Met1V')[OutCap_NumofOD * OutCap_NumofGates + i][1]]])
        self._DesignParameter['OutCapMet1RXRouting']['_XYCoordinates'] = tmp
        del tmp

        # Poly gate Metal1 Routing
        if OutCap_NumofGates >= 2:
            self._DesignParameter['OutCapMet1PolyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                          _Width=self.getYWidth('OutCap', 'Viapoly2Met1H', '_Met1Layer'), _XYCoordinates=[])
            tmp = []
            aaaa = self.getXY('OutCap', 'Viapoly2Met1H')
            for i in range(0, OutCap_NumofOD + 1):
                tmp.append([[self.getXY('OutCap', 'Viapoly2Met1H')[i][0],
                             self.getXY('OutCap', 'Viapoly2Met1H')[i][1]],
                            [self.getXY('OutCap', 'Viapoly2Met1H')[(OutCap_NumofOD + 1) * (OutCap_NumofGates - 1) + i][0],
                             self.getXY('OutCap', 'Viapoly2Met1H')[(OutCap_NumofOD + 1) * (OutCap_NumofGates - 1) + i][1]]])
            self._DesignParameter['OutCapMet1PolyRouting']['_XYCoordinates'] = tmp
            del tmp

        # RX Metal1 to Metal2 via gen.
        NCAPViaRX_XWidth = self._DesignParameter['OutCapMet1RXRouting']['_Width']
        NCAPViaRX_COYnum = int((NCAPViaRX_XWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (
                    _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1)
        if NCAPViaRX_COYnum <= 3:
            NCAPViaRX_COYnum = 4  # by DRC rule
        tmp = []
        for i in range(0, len(self._DesignParameter['OutCap']['_DesignObj']._DesignParameter['Viapoly2Met1V']['_XYCoordinates'])):
            tmp.append([self.getXY('OutCap', 'Viapoly2Met1V')[i][0],
                        self.getXY('OutCap', 'Viapoly2Met1V')[i][1]])
        self._DesignParameter['OutCapViaRX'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='NCAPViaRXIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['OutCapViaRX']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=NCAPViaRX_COYnum)
        self._DesignParameter['OutCapViaRX']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('OutCap', 'Viapoly2Met1V', '_Met1Layer')
        self._DesignParameter['OutCapViaRX']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getXWidth('OutCap', 'Viapoly2Met1V', '_Met1Layer')
        self._DesignParameter['OutCapViaRX']['_XYCoordinates'] = tmp
        del tmp

        # RX Metal2 Routing
        self._DesignParameter['OutCapMet2RXRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                    _Width=self.getXWidth('OutCapViaRX', '_Met2Layer'), _XYCoordinates=[])
        tmp = []
        for i in range(0, OutCap_NumofGates + 1):
            tmp.append([[self.getXYBot('OutCapViaRX', '_Met2Layer')[OutCap_NumofOD * i][0],
                         self.getXY('OutCapViaRX', '_Met2Layer')[OutCap_NumofOD * i][1]],
                        [self.getXYTop('OutCapViaRX', '_Met2Layer')[OutCap_NumofOD * (i + 1) - 1][0],
                         self.getXY('OutCapViaRX', '_Met2Layer')[OutCap_NumofOD * (i + 1) - 1][1]]])
        self._DesignParameter['OutCapMet2RXRouting']['_XYCoordinates'] = tmp
        del tmp

        # Poly gate Metal1 to Metal2 via gen.
        NCAPViaPoly_YWidth = OutCap_XWidth / 2
        NCAPViaPoly_COXnum = int((NCAPViaPoly_YWidth - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) + 1)
        tmp = []
        for i in range(0, len(self._DesignParameter['OutCap']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'])):
            tmp.append([self.getXY('OutCap', 'Viapoly2Met1H')[i][0],
                        self.getXY('OutCap', 'Viapoly2Met1H')[i][1]])
        self._DesignParameter['OutCapViaPoly'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='NCAPViaPolyIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['OutCapViaPoly']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=NCAPViaPoly_COXnum, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['OutCapViaPoly']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('OutCap', 'Viapoly2Met1H', '_Met1Layer')
        self._DesignParameter['OutCapViaPoly']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self.getYWidth('OutCap', 'Viapoly2Met1H', '_Met1Layer')
        self._DesignParameter['OutCapViaPoly']['_XYCoordinates'] = tmp
        del tmp

        # Poly gate Metal2 Routing
        self._DesignParameter['OutCapMet2PolyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                      _Width=self.getXWidth('OutCapViaPoly', '_Met2Layer'), _XYCoordinates=[])
        tmp = []
        for i in range(0, OutCap_NumofGates):
            tmp.append([[self.getXYBot('OutCapViaPoly', '_Met2Layer')[(OutCap_NumofOD + 1) * i][0],
                         self.getXY('OutCapViaPoly', '_Met2Layer')[(OutCap_NumofOD + 1) * i][1]],
                        [self.getXYTop('OutCapViaPoly', '_Met2Layer')[(OutCap_NumofOD + 1) * (i + 1) - 1][0],
                         self.getXY('OutCapViaPoly', '_Met2Layer')[(OutCap_NumofOD + 1) * (i + 1) - 1][1]]])
        self._DesignParameter['OutCapMet2PolyRouting']['_XYCoordinates'] = tmp
        del tmp



################################# DRC Check #################################
import random
if __name__ == '__main__':
    for i in range(0,100):
        OutCap = True
        OutCap_XWidth = random.randrange(1000, 5000, 2)
        OutCap_YWidth = random.randrange(1000, 5000, 2)
        OutCap_NumofGates = random.randint(1, 5)
        OutCap_NumofOD = random.randint(1, 5)
        OutCap_RingWidth = None
        OutCap_RingHeight = None
        _GuardringCOpitch = random.randrange(150, 200, 2)
        _GuardringThickness = random.randrange(300, 500, 2)
        _GuardringEnclosure = random.randrange(56, 100, 2)

        print(f"{i}nd loop")
        print("OutCap_XWidth =", OutCap_XWidth)
        print("OutCap_YWidth=", OutCap_YWidth)
        print("OutCap_NumofGates=", OutCap_NumofGates)
        print("OutCap_NumofOD=", OutCap_NumofOD)
        print("OutCap_RingHeight=", OutCap_RingHeight)
        print("OutCap_RingWidth=", OutCap_RingWidth)
        print("_GuardringCOpitch=", _GuardringCOpitch)
        print("_GuardringThickness=", _GuardringThickness)
        print("_GuardringEnclosure=", _GuardringEnclosure)

        # OutCap_XWidth = 3000
        # OutCap_YWidth = 2100
        # OutCap_NumofGates = 4
        # OutCap_NumofOD = 4
        # OutCap_RingHeight = None
        # OutCap_RingWidth = None
        # _GuardringCOpitch = 142
        # _GuardringThickness = 348
        # _GuardringEnclosure = 56



        DesignParameters._Technology = 'SS28nm'
        TopObj = _OutCap(_DesignParameter=None, _Name='_OutCap')
        TopObj._CalculateDesignParameter(
            OutCap=OutCap,
            OutCap_XWidth=OutCap_XWidth,
            OutCap_YWidth=OutCap_YWidth,
            OutCap_NumofGates=OutCap_NumofGates,
            OutCap_NumofOD=OutCap_NumofOD,
            OutCap_RingWidth=OutCap_RingWidth,
            OutCap_RingHeight=OutCap_RingHeight,
            _GuardringCOpitch=_GuardringCOpitch,
            _GuardringThickness=_GuardringThickness,
            _GuardringEnclosure=_GuardringEnclosure
        )
        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./_OutCap.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('#############################      Sending to FTP Server...      ##############################')

        import ftplib

        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('smlim96', 'min753531')
        ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
        myfile = open('./_OutCap.gds', 'rb')
        ftp.storbinary('STOR _OutCap.gds', myfile)
        myfile.close()

        import DRCchecker
        a = DRCchecker.DRCchecker('smlim96','min753531','/mnt/sdc/smlim96/OPUS/ss28','/mnt/sdc/smlim96/OPUS/ss28/DRC/run','_OutCap','_OutCap',None)
        a.DRCchecker()

        print ("DRC Clean!!!")