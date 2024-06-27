from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

from generatorLib.generator_models.LDO_gen import opppcres_b
from generatorLib.generator_models.LDO_gen import SubRing
from generatorLib.generator_models import ViaMet12Met2


class LDO_Fbres(StickDiagram._StickDiagram):

    def __init__(self, _DesignParameter=None, _Name='_Fbres'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameter(self,
                                  Fb_Res_Width=3000,
                                  Fb_Res_Length = 1000,
                                  Num_of_UpperRes = 2,
                                  Num_of_LowerRes = 3,
                                  SpacebtwRes_topbot = None,
                                  SpacebtwRes_rightleft = None,
                                  Fb_res_RingHeight = 8272,
                                  Fb_res_RingWidth = 14512,
                                  _GuardringCOpitch = 142,
                                  _GuardringThickness = 348,
                                  _GuardringEnclosure = 56
                                  ):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']


        print('#########################################################################################################')
        print('                                         {}  Fbres Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')


        Parameters_Res = dict(
            _ResWidth=Fb_Res_Width,
            _ResLength=Fb_Res_Length,
            _CONUMX=None,
            _CONUMY=1,
            _SeriesStripes=1,
            _ParallelStripes=1
        )
        def roundReal(val, digits):
            return round(val+10**(-len(str(val))-1), digits)

        PRESminspace = 400  # Not in DRC


        print('***************************************** feedback Res setting *****************************************')
        self._DesignParameter['Res'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=270, _DesignObj=opppcres_b._Opppcres(_Name='ResIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['Res']['_DesignObj']._CalculateOpppcresDesignParameter(**Parameters_Res)
        self._DesignParameter['Res']['_XYCoordinates'] = [[0, 0]]

        # Calculate # of Dummy Resistors
        if Num_of_LowerRes >= Num_of_UpperRes:
            Num_of_Dummy = Num_of_LowerRes - Num_of_UpperRes
        else:
            raise Exception("<Num_of_LowerRes> should be same or larger than <Num_of_UpperRes>")

        # Raise exception when generation is impossible
        if Num_of_UpperRes >= 10 or Num_of_LowerRes >= 10:
            raise Exception("Num of Resistors should be less than 10")

        if Num_of_UpperRes % 2 == 1 and Num_of_Dummy % 2 == 1:
            raise Exception("Doesn't meet symmetry condition \n"
                            "<Num_of_UpperRes> should be even number or subtraction of <Num_of_UpperRes> and <Num_of_LowerRes> should be even number")

        if SpacebtwRes_topbot == None and SpacebtwRes_rightleft == None:    # When FbresringWidth & FbresringHeight are input
            PRES_Xtotal = self.getYWidth('Res', '_PRESLayer') * (Num_of_UpperRes + Num_of_Dummy + 2) + (Num_of_UpperRes + Num_of_Dummy + 3) * PRESminspace
            PRES_Ytotal = self.getXWidth('Res', '_PRESLayer') * 2 + PRESminspace * 3
            if Fb_res_RingWidth == None or Fb_res_RingHeight == None:
                raise Exception("Parameter <FbresringWidth & Height> shoud be input")
            else:
                if Fb_res_RingWidth < PRES_Xtotal:
                    raise Exception("<FbresringWidth> should be larger")
                elif Fb_res_RingHeight < PRES_Ytotal:
                    raise Exception("<FbresringHeight> should be larger")
        else:   # When SpacebtwRes_topbot & SpacebtwRes_rightleft are input
            if SpacebtwRes_topbot == None or SpacebtwRes_rightleft == None:
                raise Exception("Parameter <SpacebtwRes_topbot & _rightleft> should be input (minimum space = 400)")
            else:
                if SpacebtwRes_topbot < PRESminspace:
                    raise Exception("<SpacebtwRes_topbot> should be larger")
                if SpacebtwRes_rightleft < PRESminspace:
                    raise Exception("<SpacebtwRes_rightleft> should be larger")

        # Resistor & Dummy Resistor Coordinate setting
        UpperRes_Coord = []
        LowerRes_Coord = []
        if SpacebtwRes_topbot == None and SpacebtwRes_rightleft == None:
            PRESspace_rightleft = (Fb_res_RingWidth - self.getYWidth('Res', '_PRESLayer') * (Num_of_UpperRes + Num_of_Dummy + 2)) / (Num_of_UpperRes + Num_of_Dummy + 3)
            PRESspace_topbot = (Fb_res_RingHeight - self.getXWidth('Res', '_PRESLayer') * 2) / 3
            for i in range(0, (Num_of_UpperRes + Num_of_Dummy + 2)):
                UpperRes_Coord.append([PRESspace_rightleft + self.getYWidth('Res', '_PRESLayer') / 2 + (self.getYWidth('Res', '_PRESLayer') + PRESspace_rightleft) * i,
                             PRESspace_topbot + self.getXWidth('Res', '_PRESLayer')])
                LowerRes_Coord.append([PRESspace_rightleft + self.getYWidth('Res', '_PRESLayer') / 2 + (self.getYWidth('Res', '_PRESLayer') + PRESspace_rightleft) * i, 0])
        else:
            for i in range(0, (Num_of_UpperRes + Num_of_Dummy + 2)):
                UpperRes_Coord.append([SpacebtwRes_rightleft + self.getYWidth('Res', '_PRESLayer') / 2 + (self.getYWidth('Res', '_PRESLayer') + SpacebtwRes_rightleft) * i,
                             SpacebtwRes_topbot + self.getXWidth('Res', '_PRESLayer')])
                LowerRes_Coord.append([SpacebtwRes_rightleft + self.getYWidth('Res', '_PRESLayer') / 2 + (self.getYWidth('Res', '_PRESLayer') + SpacebtwRes_rightleft) * i, 0])
        self._DesignParameter['Res']['_XYCoordinates'] = UpperRes_Coord + LowerRes_Coord



        print('*************************************** Guardring setting ****************************************')
        if SpacebtwRes_topbot == None and SpacebtwRes_rightleft == None:
            self._DesignParameter['PSubRing_Res'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=SubRing._SubRing(_Name='PSubRing_ResIn{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['PSubRing_Res']['_DesignObj']._CalculateDesignParameter(_Psubtype=True, _MetalOpen=None, _Height=Fb_res_RingHeight, _Width=Fb_res_RingWidth,
                                                                                          _Thickness=_GuardringThickness, _COpitch=_GuardringCOpitch, _Enclosure=_GuardringEnclosure)
            self._DesignParameter['PSubRing_Res']['_XYCoordinates'] = [[(UpperRes_Coord[0][0] + UpperRes_Coord[-1][0]) / 2, (UpperRes_Coord[0][1] + LowerRes_Coord[0][1]) / 2]]
        else:
            Ring_Width = (UpperRes_Coord[-1][0] - UpperRes_Coord[0][0] + self.getYWidth('Res', '_PRESLayer') + SpacebtwRes_rightleft * 2 + _GuardringEnclosure * 2)
            Ring_Height = (UpperRes_Coord[0][1] - LowerRes_Coord[0][1] + self.getXWidth('Res', '_PRESLayer') + SpacebtwRes_topbot * 2 + _GuardringEnclosure * 2)
            self._DesignParameter['PSubRing_Res'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=SubRing._SubRing(_Name='PSubRing_ResIn{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['PSubRing_Res']['_DesignObj']._CalculateDesignParameter(_Psubtype=True, _MetalOpen=None, _Height=Ring_Height, _Width=Ring_Width,
                                                                                          _Thickness=_GuardringThickness, _COpitch=_GuardringCOpitch, _Enclosure=_GuardringEnclosure)
            self._DesignParameter['PSubRing_Res']['_XYCoordinates'] = [[(UpperRes_Coord[0][0] + UpperRes_Coord[-1][0]) / 2, (UpperRes_Coord[0][1] + LowerRes_Coord[0][1]) / 2]]



        print('****************************************** Dummy VSS Routing *******************************************')
        # Find dummy Resistors
        Dummy_Coord = []
        Dummy_Coord_side = [UpperRes_Coord[0]] + [LowerRes_Coord[0]] + [UpperRes_Coord[-1]] + [LowerRes_Coord[-1]]
        if Num_of_UpperRes % 2 == 0:
            for i in range(0, Num_of_Dummy):
                Dummy_Coord.append(UpperRes_Coord[Num_of_UpperRes // 2 + i + 1])
        else:
            if Num_of_Dummy % 2 == 0:
                for i in range(0, Num_of_Dummy // 2):
                    Dummy_Coord.append(UpperRes_Coord[Num_of_UpperRes // 2 + i + 1])
                    Dummy_Coord.append(UpperRes_Coord[-(Num_of_UpperRes // 2 + i + 1) - 1])
            else:
                pass


        self._DesignParameter['_DummyVSSRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                 _Width=self.getYWidth('Res', '_Met1Layer'), _XYCoordinates=[])
        tmp = []
        for i in range(0, len(Dummy_Coord)):
            tmp.append([[Dummy_Coord[i][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], Dummy_Coord[i][1]],
                        [Dummy_Coord[i][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                         self.getXYTop('PSubRing_Res', 'topright', '_Met1Layer')[0][1]]])
            tmp.append([[Dummy_Coord[i][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], Dummy_Coord[i][1]],
                        [Dummy_Coord[i][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                         self.getXYTop('PSubRing_Res', 'topright', '_Met1Layer')[0][1]]])

        for i in range(0, len(Dummy_Coord_side) // 2):
            tmp.append([[Dummy_Coord_side[2*i][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], Dummy_Coord_side[2*i][1]],
                        [Dummy_Coord_side[2*i][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                         self.getXYTop('PSubRing_Res', 'topright', '_Met1Layer')[0][1]]])
            tmp.append([[Dummy_Coord_side[2*i][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], Dummy_Coord_side[2*i][1]],
                        [Dummy_Coord_side[2*i][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                         self.getXYTop('PSubRing_Res', 'topright', '_Met1Layer')[0][1]]])
            tmp.append([[Dummy_Coord_side[2*i+1][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], Dummy_Coord_side[2*i+1][1]],
                        [Dummy_Coord_side[2*i+1][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                         self.getXYBot('PSubRing_Res', 'botright', '_Met1Layer')[0][1]]])
            tmp.append([[Dummy_Coord_side[2*i+1][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], Dummy_Coord_side[2*i+1][1]],
                        [Dummy_Coord_side[2*i+1][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                         self.getXYBot('PSubRing_Res', 'botright', '_Met1Layer')[0][1]]])
        self._DesignParameter['_DummyVSSRouting']['_XYCoordinates'] = tmp
        del tmp



        print('***************************************** feedback Res Routing *****************************************')
        # Feedback Res Coord
        UpperFbRes_Coord = [x for x in UpperRes_Coord if x not in (Dummy_Coord + Dummy_Coord_side)]
        LowerFbRes_Coord = [x for x in LowerRes_Coord if x not in (Dummy_Coord + Dummy_Coord_side)]
        UpperFbRes_Coord.sort()
        LowerFbRes_Coord.sort()

        # Amp out - Upper Res - Lower Res Routing
        self._DesignParameter['_UpLowRouting'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                  _XWidth=self.getYWidth('Res', '_Met1Layer'),
                                                                                  _YWidth=UpperFbRes_Coord[0][1] - LowerFbRes_Coord[0][1],
                                                                                  _XYCoordinates=[])
        self._DesignParameter['_UpLowRouting']['_XYCoordinates'] = [[UpperFbRes_Coord[0][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                                                                     (UpperFbRes_Coord[0][1] + LowerFbRes_Coord[0][1]) / 2]]

        if self.getXWidth('Res', '_Met1Layer') // 2 >= _DRCObj._MetalxMaxWidth:
            RoutingWidth = _DRCObj._MetalxMaxWidth
        else:
            RoutingWidth = self.getXWidth('Res', '_Met1Layer') // 2


        # Lower Res Routing
        self._DesignParameter['_LowerResRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                 _Width=RoutingWidth, _XYCoordinates=[])
        tmp = []
        for i in range(0, len(LowerFbRes_Coord) - 1):
            tmp.append([[LowerFbRes_Coord[i][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], LowerFbRes_Coord[i][1]],
                        [LowerFbRes_Coord[i+1][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], LowerFbRes_Coord[i+1][1]]])
        self._DesignParameter['_LowerResRouting']['_XYCoordinates'] = tmp
        del tmp

        # Lower Res VSS
        self._DesignParameter['_LowerResVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                             _Width=self.getYWidth('Res', '_Met1Layer'), _XYCoordinates=[])
        self._DesignParameter['_LowerResVSS']['_XYCoordinates'] = [[[LowerFbRes_Coord[-1][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                                                                     LowerFbRes_Coord[-1][1]],
                                                                    [LowerFbRes_Coord[-1][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1],
                                                                     self.getXYBot('PSubRing_Res', 'botright', '_Met1Layer')[0][1]]]]

        # Upper Res Routing
        self._DesignParameter['_UpperResRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                 _Width=RoutingWidth, _XYCoordinates=[])
        tmp = []
        for i in range(0, len(UpperFbRes_Coord) - 1):
            tmp.append([[UpperFbRes_Coord[i][0] - self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], UpperFbRes_Coord[i][1]],
                        [UpperFbRes_Coord[i+1][0] + self._DesignParameter['Res']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1], UpperFbRes_Coord[i+1][1]]])
        self._DesignParameter['_UpperResRouting']['_XYCoordinates'] = tmp

        UpperVia_Xnum = int((self.getWidth('_UpperResRouting') - 2 * _DRCObj._Metal1MinEnclosureVia12 - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
        if self.getWidth('_UpperResRouting') > 460 and UpperVia_Xnum < 4:   # By DRC Rule GR612
            UpperVia_Xnum = 4
        self._DesignParameter['_UpperResMet12Met2Via'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=90, _DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='_UpperResMet12Met2ViaIn{}'.format(_Name)), _XYCoordinates=[])[0]
        self._DesignParameter['_UpperResMet12Met2Via']['_DesignObj']._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=UpperVia_Xnum, _ViaMet12Met2NumberOfCOY=1)
        self._DesignParameter['_UpperResMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('Res', '_Met1Layer')
        self._DesignParameter['_UpperResMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_UpperResMet12Met2Via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
        self._DesignParameter['_UpperResMet12Met2Via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.getWidth('_UpperResRouting')
        for i in range(len(tmp)):
            self._DesignParameter['_UpperResMet12Met2Via']['_XYCoordinates'].append(tmp[i][0])
            self._DesignParameter['_UpperResMet12Met2Via']['_XYCoordinates'].append(tmp[i][1])
        del tmp






################################# DRC Check #################################
import random
if __name__ == '__main__':
    for i in range(0,100):
        Fb_Res_Width = random.randrange(1000,5000,2)
        Fb_Res_Length = random.randrange(1000,5000,2)
        Num_of_UpperRes = random.randrange(2,8,2)
        Num_of_LowerRes = random.randint(Num_of_UpperRes,9)
        SpacebtwRes_topbot = random.randrange(400,1000,2)
        SpacebtwRes_rightleft = random.randrange(400,1000,2)
        Fb_res_RingHeight = None
        Fb_res_RingWidth = None
        _GuardringCOpitch = random.randrange(150, 200, 2)
        _GuardringThickness = random.randrange(300, 500, 2)
        _GuardringEnclosure = random.randrange(56, 100, 2)

        print(f"{i}nd loop")
        print("Fb_Res_Width =", Fb_Res_Width)
        print("Fb_Res_Length=", Fb_Res_Length)
        print("Num_of_UpperRes=", Num_of_UpperRes)
        print("Num_of_LowerRes=", Num_of_LowerRes)
        print("SpacebtwRes_topbot=", SpacebtwRes_topbot)
        print("SpacebtwRes_rightleft=", SpacebtwRes_rightleft)
        print("Fb_res_RingHeight=", Fb_res_RingHeight)
        print("Fb_res_RingWidth=", Fb_res_RingWidth)
        print("_GuardringCOpitch=", _GuardringCOpitch)
        print("_GuardringThickness=", _GuardringThickness)
        print("_GuardringEnclosure=", _GuardringEnclosure)

        # Fb_Res_Width = 3000
        # Fb_Res_Length = 1000
        # Num_of_UpperRes = 2
        # Num_of_LowerRes = 3
        # SpacebtwRes_topbot = None
        # SpacebtwRes_rightleft = None
        # Fb_res_RingHeight = 8272
        # Fb_res_RingWidth = 14512
        # _GuardringCOpitch = 142
        # _GuardringThickness = 348
        # _GuardringEnclosure = 56

        # Fb_Res_Width = 3000
        # Fb_Res_Length = 1000
        # Num_of_UpperRes = 3
        # Num_of_LowerRes = 7
        # SpacebtwRes_topbot = 600
        # SpacebtwRes_rightleft = 600
        # Fb_res_RingHeight = None
        # Fb_res_RingWidth = None
        # _GuardringCOpitch = 142
        # _GuardringThickness = 348
        # _GuardringEnclosure = 56



        DesignParameters._Technology = 'SS28nm'
        TopObj = LDO_Fbres(_DesignParameter=None, _Name='_LDO_Fbres')
        TopObj._CalculateDesignParameter(
            Fb_Res_Width=Fb_Res_Width,
            Fb_Res_Length=Fb_Res_Length,
            Num_of_UpperRes=Num_of_UpperRes,
            Num_of_LowerRes=Num_of_LowerRes,
            SpacebtwRes_topbot=SpacebtwRes_topbot,
            SpacebtwRes_rightleft=SpacebtwRes_rightleft,
            Fb_res_RingHeight=Fb_res_RingHeight,
            Fb_res_RingWidth=Fb_res_RingWidth,
            _GuardringCOpitch=_GuardringCOpitch,
            _GuardringThickness=_GuardringThickness,
            _GuardringEnclosure=_GuardringEnclosure
        )
        TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
        testStreamFile = open('./_LDO_Fbres.gds', 'wb')
        tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('#############################      Sending to FTP Server...      ##############################')

        import ftplib

        ftp = ftplib.FTP('141.223.24.53')
        ftp.login('smlim96', 'min753531')
        ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
        myfile = open('./_LDO_Fbres.gds', 'rb')
        ftp.storbinary('STOR _LDO_Fbres.gds', myfile)
        myfile.close()

        import DRCchecker
        a = DRCchecker.DRCchecker('smlim96','min753531','/mnt/sdc/smlim96/OPUS/ss28','/mnt/sdc/smlim96/OPUS/ss28/DRC/run','_LDO_Fbres','_LDO_Fbres',None)
        a.DRCchecker()

        print ("DRC Clean!!!")