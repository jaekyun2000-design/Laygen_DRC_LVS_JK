from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
import time
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1_resize
from generatorLib.generator_models import CascodePMOS
from generatorLib.generator_models import CascodeNMOS
from generatorLib.generator_models import Z_PWR_CNT


class TristateInverter(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='TristateInverter'):
        if _DesignParameter is not None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  NumFinger=4,
                                  PMOSWidth=400,
                                  NMOSWidth=200,

                                  CellHeight=1800,  # Option
                                  VDD2PMOS=None,  # Option (Not work when finger >= 3)
                                  VSS2NMOS=None,  # Option (Not work when finger >= 3)
                                  YCoordOfInputA=None,  # Optional
                                  YCoordOfInputEN=None,  # Optional
                                  YCoordOfInputENb=None,  # Optional

                                  ChannelLength=30,
                                  GateSpacing=100,
                                  XVT='SLVT',
                                  SupplyRailType=1          # (Not work when finger >= 3)
                                  ):
        """
        Top def for all kind of fingers

        """
        if NumFinger == 1:
            self._CalculateDesignParameterFinger1_v2(
                PMOSWidth=PMOSWidth,
                NMOSWidth=NMOSWidth,
                ChannelLength=ChannelLength,
                GateSpacing=GateSpacing,
                XVT=XVT,

                CellHeight=CellHeight,                  # Optional
                VDD2PMOS=VDD2PMOS,                      # Optional
                VSS2NMOS=VSS2NMOS,                      # Optional

                YCoordOfInputA=YCoordOfInputA,          # Optional
                YCoordOfInputEN=YCoordOfInputEN,        # Optional
                YCoordOfInputENb=YCoordOfInputENb,      # Optional
                SupplyRailType=SupplyRailType
            )
        elif NumFinger == 2:
            self._CalculateDesignParameterFinger2_v2(
                PMOSWidth=PMOSWidth,
                NMOSWidth=NMOSWidth,
                ChannelLength=ChannelLength,
                GateSpacing=GateSpacing,
                XVT=XVT,

                CellHeight=CellHeight,  # Optional
                VDD2PMOS=VDD2PMOS,  # Optional
                VSS2NMOS=VSS2NMOS,  # Optional

                YCoordOfInputA=YCoordOfInputA,  # Optional
                YCoordOfInputEN=YCoordOfInputEN,  # Optional
                YCoordOfInputENb=YCoordOfInputENb,  # Optional
                SupplyRailType=SupplyRailType
            )
        else:
            # there is no VDD2PMOS, VSS2NMOS
            self._CalculateDesignParameterF3(
                NumFinger_NM1=NumFinger,    # NM1 = NM2 (finger, nm width, pm width)
                NumFinger_NM2=NumFinger,
                Width_NM1=NMOSWidth,
                Width_NM2=NMOSWidth,
                Width_PM1=PMOSWidth,
                Width_PM2=PMOSWidth,

                ChannelLength=ChannelLength,
                GateSpacing=GateSpacing,
                XVT=XVT,

                CellHeight=CellHeight,              # Option
                YCoordOfInputA=YCoordOfInputA,      # Option
                YCoordOfInputEN=YCoordOfInputEN,    # Option
                YCoordOfInputENb=YCoordOfInputENb   # Option
            )


    def _CalculateDesignParameterF3(self,
                                    NumFinger_NM1=3,
                                    NumFinger_NM2=5,
                                    Width_NM1=200,
                                    Width_NM2=250,
                                    Width_PM1=400,
                                    Width_PM2=500,

                                    CellHeight=None,  # Option
                                    YCoordOfInputA=None,  # Option
                                    YCoordOfInputEN=None,  # Option
                                    YCoordOfInputENb=None,  # Option

                                    ChannelLength=30,
                                    GateSpacing=100,
                                    XVT='SLVT'
                                    ):
        """
            main def when finger >= 3,
            calculate when CellHeight == None

            it uses self._CalculateDesignParameterFinger3orMore_i() -> not support when CellHeight == None
        """
        drc = DRC.DRC()
        tmpLength = max(Width_NM1, Width_NM2) + max(Width_PM1, Width_PM2)
        self._CalculateDesignParameterFinger3orMore_i(
            NumFinger_NM1=NumFinger_NM1,
            NumFinger_NM2=NumFinger_NM2,
            Width_NM1=Width_NM1,
            Width_NM2=Width_NM2,
            Width_PM1=Width_PM1,
            Width_PM2=Width_PM2,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=tmpLength * 10,
            YCoordOfInputA=None,
            YCoordOfInputEN=None,
            YCoordOfInputENb=None
        )

        # # prev. calc.
        # GapBtwInputVia = drc._Metal1MinSpaceAtCorner
        # Met1GapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_Met1Layer')[0][1] - \
        #                           self.getXYTop('polyInputEN', '_Met1Layer')[0][1]
        # Margin_byMet1 = Met1GapBtw_ViaEN_ViaENb - 2 * drc._Metal1MinSpaceAtCorner - self.getYWidth('polyInputA', '_Met1Layer')
        # CellHeight_min = tmpLength * 10 - Margin_byMet1

        # new one
        tmpDRC_ODandPoly = 31
        # NM1 Side
        distanceNM1Met1topBoundary_2_NM1Center = max(self.getXYTop('NM1', '_Met1Layer')[0][1], self.getXYTop('via1nmos', '_Met1Layer')[0][1]) - self.getXY('NM1')[0][1]
        distanceBtwNM1_2_PolyInput_byMet1 = distanceNM1Met1topBoundary_2_NM1Center + drc._Metal1MinSpaceAtCorner + self.getYWidth('polyInputA', '_Met1Layer') / 2
        distanceBtwNM1_2_PolyInput_byODandPoly = \
            0.5 * self.getYWidth('NM1', '_ODLayer') \
            + 0.5 * (drc._CoMinWidth + 2 * drc._CoMinEnclosureByPOAtLeastTwoSide) + tmpDRC_ODandPoly
        distanceBtwNM1_2_PolyInput = max(distanceBtwNM1_2_PolyInput_byMet1, distanceBtwNM1_2_PolyInput_byODandPoly)

        distancePM1Met1botBoundary_2_PM1Center = self.getXY('PM1')[0][1] - min(self.getXYBot('PM1', '_Met1Layer')[0][1], self.getXYBot('via1ForPM1', '_Met1Layer')[0][1])
        distanceBtwPM1_2_PolyInput_byMet1 = distancePM1Met1botBoundary_2_PM1Center + drc._Metal1MinSpaceAtCorner + self.getYWidth('polyInputA', '_Met1Layer') / 2
        distanceBtwPM1_2_PolyInput_byODandPoly = \
            0.5 * self.getYWidth('PM1', '_ODLayer') \
            + 0.5 * (drc._CoMinWidth + 2 * drc._CoMinEnclosureByPOAtLeastTwoSide) + tmpDRC_ODandPoly
        distanceBtwPM1_2_PolyInput = max(distanceBtwPM1_2_PolyInput_byMet1, distanceBtwPM1_2_PolyInput_byODandPoly)

        Margin_byNM1PM1 = (self.getXY('PM1')[0][1] - self.getXY('NM1')[0][1]) - (distanceBtwNM1_2_PolyInput + distanceBtwPM1_2_PolyInput)

        # NM2 side
        Met1GapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_Met1Layer')[0][1] - self.getXYTop('polyInputEN', '_Met1Layer')[0][1]
        PolyGapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_POLayer')[0][1] - self.getXYTop('polyInputEN', '_POLayer')[0][1]
        Margin_byMet1NM2PM2 = Met1GapBtw_ViaEN_ViaENb - drc._Metal1MinSpaceAtCorner
        Margin_byPoly1NM2PM2 = PolyGapBtw_ViaEN_ViaENb - drc._PolygateMinSpace
        Margin_byNM2PM2 = min(Margin_byMet1NM2PM2, Margin_byPoly1NM2PM2)

        # Layer [NW - NPLUS(RX not BP)] , [BP - RX]
        margin_NW_NPLUS = self.getXYBot('nwlayer')[0][1] - max(self.getXYTop('NM1', '_ODLayer')[0][1], self.getXYTop('NM2', '_ODLayer')[0][1]) - drc._NwMinSpacetoNactive
        margin_PP_OD = min(self.getXYBot('PM1', '_PPLayer')[0][1], self.getXYBot('PM2', '_PPLayer')[0][1]) - max(self.getXYTop('NM1', '_ODLayer')[0][1], self.getXYTop('NM2', '_ODLayer')[0][1]) - drc._OdMinSpace2Pp

        CellHeight_min = tmpLength * 10 - min(Margin_byNM1PM1, Margin_byNM2PM2, margin_NW_NPLUS, margin_PP_OD)



        if CellHeight == None:
            _CellHeight = CellHeight_min
        elif CellHeight < CellHeight_min:
            raise NotImplementedError(f"Input CellHeight={CellHeight}, But CellHeight_min={CellHeight_min}")
        else:
            _CellHeight = CellHeight

        # initialize
        tmpName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_Name=tmpName)
        self._CalculateDesignParameterFinger3orMore_i(
            NumFinger_NM1=NumFinger_NM1,
            NumFinger_NM2=NumFinger_NM2,
            Width_NM1=Width_NM1,
            Width_NM2=Width_NM2,
            Width_PM1=Width_PM1,
            Width_PM2=Width_PM2,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=_CellHeight,
            YCoordOfInputA=YCoordOfInputA,
            YCoordOfInputEN=YCoordOfInputEN,
            YCoordOfInputENb=YCoordOfInputENb
        )


    def _CalcMinHeight(self,
                       NumFinger=1,
                       PMOSWidth=400,
                       NMOSWidth=200,

                       ChannelLength=30,
                       GateSpacing=100,
                       XVT='SLVT',
                       SupplyRailType=1
                       ):
        """



        """

        drc = DRC.DRC()
        tmpLength = NMOSWidth + PMOSWidth

        if NumFinger == 1:
            self._CalculateDesignParameterFinger1_i(
                NMOSWidth=NMOSWidth,
                PMOSWidth=PMOSWidth,
                ChannelLength=ChannelLength,
                GateSpacing=GateSpacing,
                XVT=XVT,
                CellHeight=tmpLength * 10,
                VDD2PMOS=None,
                VSS2NMOS=None,
                YCoordOfInputA=None,
                YCoordOfInputEN=None,
                YCoordOfInputENb=None,
                SupplyRailType=SupplyRailType
            )

            Met1GapBtw_ViaEN_ViaENb = self.getXYBot('InputVia_ENb', '_Met1Layer')[0][1] - \
                                      self.getXYTop('InputVia_EN', '_Met1Layer')[0][1]
            PolyGapBtw_ViaEN_ViaENb = self.getXYBot('InputVia_ENb', '_POLayer')[0][1] - \
                                      self.getXYTop('InputVia_EN', '_POLayer')[0][1]
            Margin_byMet1 = Met1GapBtw_ViaEN_ViaENb - drc._Metal1MinSpaceAtCorner
            Margin_byPoly = PolyGapBtw_ViaEN_ViaENb - drc._PolygateMinSpace  # need to check

            CellHeight_min = tmpLength * 10 - min(Margin_byMet1, Margin_byPoly)
        elif NumFinger == 2:
            self._CalculateDesignParameterFinger2_i(
                NMOSWidth=NMOSWidth,
                PMOSWidth=PMOSWidth,
                ChannelLength=ChannelLength,
                GateSpacing=GateSpacing,
                XVT=XVT,
                CellHeight=tmpLength * 10,
                VDD2PMOS=None,
                VSS2NMOS=None,
                YCoordOfInputA=None,
                YCoordOfInputEN=None,
                YCoordOfInputENb=None,
                SupplyRailType=SupplyRailType
            )
            # conservative condition.. (InputVia_EN  InputVia_ENb  -  InputVia_A  polygate3)
            # GapBtwPolygate3_EN = (self.getXYBot('polygate3')[0][1] - self.getXYTop('InputVia_EN', '_POLayer')[0][1])
            # GapBtwPolygate3_ENb = (self.getXYBot('InputVia_ENb', '_POLayer')[0][1] - self.getXYTop('polygate3')[0][1])
            # Margin_ENside = GapBtwPolygate3_EN - drc._PolygateMinSpace
            # Margin_ENbside = GapBtwPolygate3_ENb - drc._PolygateMinSpace
            # CellHeight_min = tmpLength * 10 - (Margin_ENside + Margin_ENbside)

            # gap between input vias (drc._Metal1MinSpaceAtCorner)
            GapBtw_EN_ENb = (self.getXYBot('InputVia_ENb', '_Met1Layer')[0][1] - self.getXYTop('InputVia_EN', '_Met1Layer')[0][1])
            Margin_byMet1 = GapBtw_EN_ENb - 2 * drc._Metal1MinSpaceAtCorner - self.getYWidth('InputVia_A', '_Met1Layer')
            CellHeight_min = tmpLength * 10 - Margin_byMet1


        else:
            self._CalculateDesignParameterFinger3orMore_i(
                NumFinger_NM1=NumFinger,
                NumFinger_NM2=NumFinger,
                Width_NM1=NMOSWidth,
                Width_NM2=NMOSWidth,
                Width_PM1=PMOSWidth,
                Width_PM2=PMOSWidth,
                ChannelLength=ChannelLength,
                GateSpacing=GateSpacing,
                XVT=XVT,
                CellHeight=tmpLength * 10,
                YCoordOfInputA=None,
                YCoordOfInputEN=None,
                YCoordOfInputENb=None
            )

            # # 1) conservative
            # Met1GapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_Met1Layer')[0][1] - \
            #                           self.getXYTop('polyInputEN', '_Met1Layer')[0][1]
            # PolyGapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_POLayer')[0][1] - \
            #                           self.getXYTop('polyInputEN', '_POLayer')[0][1]
            # Margin_byMet1 = Met1GapBtw_ViaEN_ViaENb - drc._Metal1MinSpaceAtCorner
            # Margin_byPoly = PolyGapBtw_ViaEN_ViaENb - drc._PolygateMinSpace  # need to check
            # CellHeight_min = tmpLength * 10 - min(Margin_byMet1, Margin_byPoly)

            # 2) spacing btw all input contact by drc._Metal1MinSpaceAtCorner
            GapBtwInputVia = drc._Metal1MinSpaceAtCorner
            Met1GapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_Met1Layer')[0][1] - \
                                      self.getXYTop('polyInputEN', '_Met1Layer')[0][1]
            Margin_byMet1 = Met1GapBtw_ViaEN_ViaENb - 2 * drc._Metal1MinSpaceAtCorner - self.getYWidth('polyInputA', '_Met1Layer') -10  # t
            CellHeight_min = tmpLength * 10 - Margin_byMet1
        # end of if-elif-else

        return CellHeight_min

    def _CalcMinHeightF3(self,
                       NumFinger_NM1=1,
                       NumFinger_NM2=1,
                       Width_PM1=400,
                       Width_PM2=400,
                       Width_NM1=200,
                       Width_NM2=200,

                       ChannelLength=30,
                       GateSpacing=100,
                       XVT='SLVT',
                       SupplyRailType=1
                       ):
        """


        """

        drc = DRC.DRC()
        tmpLength = max(Width_NM1, Width_NM2) + max(Width_PM1, Width_PM2)
        self._CalculateDesignParameterFinger3orMore_i(
            NumFinger_NM1=NumFinger_NM1,
            NumFinger_NM2=NumFinger_NM1,
            Width_NM1=Width_NM1,
            Width_NM2=Width_NM2,
            Width_PM1=Width_PM1,
            Width_PM2=Width_PM2,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=tmpLength * 10,
            YCoordOfInputA=None,
            YCoordOfInputEN=None,
            YCoordOfInputENb=None
        )

        # # 1) conservative
        # Met1GapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_Met1Layer')[0][1] - \
        #                           self.getXYTop('polyInputEN', '_Met1Layer')[0][1]
        # PolyGapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_POLayer')[0][1] - \
        #                           self.getXYTop('polyInputEN', '_POLayer')[0][1]
        # Margin_byMet1 = Met1GapBtw_ViaEN_ViaENb - drc._Metal1MinSpaceAtCorner
        # Margin_byPoly = PolyGapBtw_ViaEN_ViaENb - drc._PolygateMinSpace  # need to check
        # CellHeight_min = tmpLength * 10 - min(Margin_byMet1, Margin_byPoly)

        # 2) spacing btw all input contact by drc._Metal1MinSpaceAtCorner
        GapBtwInputVia = drc._Metal1MinSpaceAtCorner
        Met1GapBtw_ViaEN_ViaENb = self.getXYBot('polyInputENb', '_Met1Layer')[0][1] - \
                                  self.getXYTop('polyInputEN', '_Met1Layer')[0][1]
        Margin_byMet1 = Met1GapBtw_ViaEN_ViaENb - 2 * drc._Metal1MinSpaceAtCorner - self.getYWidth('polyInputA', '_Met1Layer')
        CellHeight_min = tmpLength * 10 - Margin_byMet1

        return CellHeight_min





    def _CalculateDesignParameterFinger1_v2(self,
                        NMOSWidth=200,
                        PMOSWidth=400,
                        ChannelLength=30,
                        GateSpacing=100,
                        XVT='SLVT',

                        CellHeight=None,        # Optional
                        VDD2PMOS=None,           # Optional
                        VSS2NMOS=None,           # Optional

                        YCoordOfInputA=None,    # Optional
                        YCoordOfInputEN=None,   # Optional
                        YCoordOfInputENb=None,  # Optional
                        SupplyRailType=1
                        ):
        """
        main def when finger == 1,
        calculate when CellHeight == None

        it uses self._CalculateDesignParameterFinger1_i() -> not support when CellHeight == None
        """

        drc = DRC.DRC()

        tmpLength = NMOSWidth + PMOSWidth
        self._CalculateDesignParameterFinger1_i(
            NMOSWidth=NMOSWidth,
            PMOSWidth=PMOSWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=tmpLength * 10,
            VDD2PMOS=None,
            VSS2NMOS=None,

            YCoordOfInputA=None,
            YCoordOfInputEN=None,
            YCoordOfInputENb=None,
            SupplyRailType=SupplyRailType
            )

        Met1GapBtw_ViaEN_ViaENb = self.getXYBot('InputVia_ENb', '_Met1Layer')[0][1] - self.getXYTop('InputVia_EN', '_Met1Layer')[0][1]
        PolyGapBtw_ViaEN_ViaENb = self.getXYBot('InputVia_ENb', '_POLayer')[0][1] - self.getXYTop('InputVia_EN', '_POLayer')[0][1]
        Margin_byMet1 = Met1GapBtw_ViaEN_ViaENb - drc._Metal1MinSpaceAtCorner
        Margin_byPoly = PolyGapBtw_ViaEN_ViaENb - drc._PolygateMinSpace       # need to check

        CellHeight_min = tmpLength * 10 - min(Margin_byMet1, Margin_byPoly)
        if CellHeight == None:
            _CellHeight = CellHeight_min
        elif CellHeight < CellHeight_min:
            raise NotImplementedError(f"Input CellHeight={CellHeight}, But CellHeight_min={CellHeight_min}")
        else:
            _CellHeight = CellHeight

        # initialize
        tmpName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_Name=tmpName)

        self._CalculateDesignParameterFinger1_i(
            NMOSWidth=NMOSWidth,
            PMOSWidth=PMOSWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=_CellHeight,
            VDD2PMOS=VDD2PMOS,
            VSS2NMOS=VSS2NMOS,

            YCoordOfInputA=YCoordOfInputA,
            YCoordOfInputEN=YCoordOfInputEN,
            YCoordOfInputENb=YCoordOfInputENb,
            SupplyRailType=SupplyRailType
        )

    def _CalculateDesignParameterFinger1_i(self,
                                         NMOSWidth=200,
                                         PMOSWidth=400,

                                         ChannelLength=30,
                                         GateSpacing=100,
                                         XVT='SLVT',

                                         CellHeight=1800,           # Required
                                         VDD2PMOS=400,              # Optional
                                         VSS2NMOS=275,              # Optional

                                         YCoordOfInputA=None,       # Optional
                                         YCoordOfInputEN=None,      # Optional
                                         YCoordOfInputENb=None,     # Optional
                                         SupplyRailType=1
                                         ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = drc._MinSnapSpacing

        if SupplyRailType == 1:
            bool_deleteViaAndMet1 = False
        elif SupplyRailType == 2:
            bool_deleteViaAndMet1 = True
        else:
            raise NotImplementedError

        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=3, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=True, deleteViaAndMet1=bool_deleteViaAndMet1))
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=3, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=False, deleteViaAndMet1=bool_deleteViaAndMet1))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]

        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=CascodeNMOS._CascodeNMOS(_Name='CascodeNMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateDesignParameter(**dict(_NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength, _NMOSDummy=True, _XVT=XVT, _GateSpacing=GateSpacing))

        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=CascodePMOS._CascodePMOS(_Name='CascodePMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculateDesignParameter(**dict(_PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength, _PMOSDummy=True, _XVT=XVT, _GateSpacing=GateSpacing))

        # dummy area
        if '_PODummyLayer' in self._DesignParameter['NMOS']['_DesignObj']._DesignParameter:
            Area_NmosDummy = self.getXWidth('NMOS', '_PODummyLayer') * self.getYWidth('NMOS', '_PODummyLayer')
            if Area_NmosDummy < drc._PODummyMinArea:
                YWidth_NmosDummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth('NMOS', '_PODummyLayer'), MinSnapSpacing * 2)
                self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_NmosDummy_Recalc
            else:
                pass
        else:
            pass
        if '_PODummyLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter:
            Area_PmosDummy = self.getXWidth('PMOS', '_PODummyLayer') * self.getYWidth('PMOS', '_PODummyLayer')
            if Area_PmosDummy < drc._PODummyMinArea:
                YWidth_PmosDummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth('PMOS', '_PODummyLayer'), MinSnapSpacing * 2)
                self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_PmosDummy_Recalc
            else:
                pass
        else:
            pass

        #
        DistanceBtwVSS2NMOS = list()
        DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('VSSRail', '_ODLayer') + self.getYWidth('NMOS', '_ODLayer')) + drc._OdMinSpace)
        DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('VSSRail', '_PPLayer') + self.getYWidth('NMOS', '_ODLayer')) + drc._OdMinSpace2Pp)
        DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('VSSRail', '_ODLayer') + self.getYWidth('NMOS', '_PODummyLayer')) + drc._PolygateMinSpace2OD if '_PODummyLayer' in self._DesignParameter['NMOS']['_DesignObj']._DesignParameter else 0)
        DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('VSSRail', '_Met1Layer') + self.getYWidth('NMOS', '_Met1Layer')) + drc._Metal1MinSpaceAtCorner if '_Met1Layer' in self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter else 0)
        VSS2NMOS_min = max(DistanceBtwVSS2NMOS)
        if VSS2NMOS == None:
            YCoordOfNMOS = VSS2NMOS_min
        elif VSS2NMOS < VSS2NMOS_min:
            raise NotImplementedError(f'VSS2NMOS={VSS2NMOS}, But VSS2NMOS_min={VSS2NMOS_min}')
        else:
            YCoordOfNMOS = VSS2NMOS

        #
        DistanceBtwVDD2PMOS = list()
        DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_ODLayer')) + drc._OdMinSpace)
        DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_PPLayer')) + drc._OdMinSpace2Pp)
        DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_PODummyLayer')) + drc._PolygateMinSpace2OD if '_PODummyLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter else 0)
        DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('VDDRail', '_Met1Layer') + self.getYWidth('PMOS', '_Met1Layer')) + drc._Metal1MinSpaceAtCorner if '_Met1Layer' in self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter else 0)
        VDD2PMOS_min = max(DistanceBtwVDD2PMOS)
        if VDD2PMOS == None:
            YCoordOfPMOS = CellHeight - VDD2PMOS_min
        elif VDD2PMOS < VDD2PMOS_min:
            raise NotImplementedError(f'VDD2PMOS={VDD2PMOS}, But VDD2PMOS_min={VDD2PMOS_min}')
        else:
            YCoordOfPMOS = CellHeight - VDD2PMOS

        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, YCoordOfNMOS]]
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, YCoordOfPMOS]]

        self._DesignParameter['VSSRouting'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])))
        self._DesignParameter['VSSRouting']['_XYCoordinates'] = [[
            (self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]),
            ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])) / 2)]]
        self._DesignParameter['VDDRouting'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VDDRouting']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), (((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]

        if SupplyRailType == 2:
            tmpXYs = []
            for XYs in self.getXY('VSSRouting'):
                tmpXYs.append([XYs[0], 0])
            self._DesignParameter['ViaForVSS'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVSS']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVSS']['_XYCoordinates'] = tmpXYs

            tmpXYs = []
            for XYs in self.getXY('VDDRouting'):
                tmpXYs.append([XYs[0], CellHeight])
            self._DesignParameter['ViaForVDD'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVDD']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVDD']['_XYCoordinates'] = tmpXYs
        else:
            pass

        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'],
            _YWidth=CellHeight,
            _XYCoordinates=[[0, (CellHeight / 2)]]
        )

        ''' Calculate InputVia(EN,ENb)'s YCoordinates '''
        self._DesignParameter['InputVia_EN'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_ENIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_EN']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_ENb'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_ENbIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_ENb']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_A'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_AIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_A']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))

        met1Width = self.getXWidth('NMOS', '_Met1Layer')
        xCoordOfInputViaENandENb = -met1Width / 2 - drc._Metal1MinSpaceAtCorner - self.getXWidth('InputVia_EN', '_Met1Layer') / 2

        # Xgap_InputContactPoly2DummyPoly = (-(GateSpacing + ChannelLength) - self.getXWidth('InputVia_EN', '_POLayer') / 2) - self.getXYRight('NMOS', '_PODummyLayer')[0][0]   # prev one
        Xgap_InputContactPoly2DummyPoly = (xCoordOfInputViaENandENb - self.getXWidth('InputVia_EN', '_POLayer') / 2) - self.getXYRight('NMOS', '_PODummyLayer')[0][0]
        Ygap_InputContactPoly2DummyPoly = math.ceil(math.sqrt(drc._PolygateMinSpaceAtCorner ** 2 - Xgap_InputContactPoly2DummyPoly ** 2))

        Ymin_Via_EN = math.ceil(self.getXYTop('NMOS', '_PODummyLayer')[0][1]
                                + Ygap_InputContactPoly2DummyPoly
                                + self.getYWidth('InputVia_EN', '_POLayer') / 2)
        if YCoordOfInputEN == None:
            YCoordOfInputVia_EN = Ymin_Via_EN
        elif YCoordOfInputEN < Ymin_Via_EN:
            raise NotImplementedError(f"Input YCoordOfInputEN={YCoordOfInputEN}, but minimum value is {Ymin_Via_EN}")
        else:
            YCoordOfInputVia_EN = YCoordOfInputEN

        Ymax_Via_ENb = math.floor(self.getXYBot('PMOS', '_PODummyLayer')[0][1]
                                  - Ygap_InputContactPoly2DummyPoly
                                  - self.getYWidth('InputVia_ENb', '_POLayer') / 2)
        if YCoordOfInputENb == None:
            YCoordOfInputVia_ENb = Ymax_Via_ENb
        elif YCoordOfInputENb > Ymax_Via_ENb:
            raise NotImplementedError(f"Input YCoordOfInputENb={YCoordOfInputENb}, but maximum value is {Ymax_Via_ENb}")
        else:
            YCoordOfInputVia_ENb = YCoordOfInputENb

        # need error raise
        if YCoordOfInputA == None:
            # YCoordOfInputVia_A = math.ceil((self.getXYTop('NMOS', '_Met1Layer')[0][1] + self.getXYBot('PMOS', '_Met1Layer')[0][1]) / 2)
            YCoordOfInputVia_A = (YCoordOfInputVia_EN + YCoordOfInputVia_ENb) / 2
        else:
            YCoordOfInputVia_A = YCoordOfInputA

        XCoordOfInputVia_A = self.getXWidth('NMOS', '_Met1Layer') / 2 + 60 + self.getXWidth('InputVia_A', '_Met1Layer') / 2

        self._DesignParameter['InputVia_EN']['_XYCoordinates'] = [[int(self.getXY('NMOS', '_Met1Layer')[0][0]), YCoordOfInputVia_EN]]
        self._DesignParameter['InputVia_ENb']['_XYCoordinates'] = [[int(self.getXY('NMOS', '_Met1Layer')[0][0]), YCoordOfInputVia_ENb]]

        self._DesignParameter['InputVia_EN']['_XYCoordinates'] = [[xCoordOfInputViaENandENb, YCoordOfInputVia_EN]]
        self._DesignParameter['InputVia_ENb']['_XYCoordinates'] = [[xCoordOfInputViaENandENb, YCoordOfInputVia_ENb]]


        self._DesignParameter['InputVia_A']['_XYCoordinates'] = [[XCoordOfInputVia_A, YCoordOfInputVia_A]]
        self._DesignParameter['POLY_boundary_30'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_30']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_29'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) - ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_29']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), (((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) + ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_24'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_24']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_23'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])))
        self._DesignParameter['POLY_boundary_23']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])) / 2)]]
        self._DesignParameter['nwlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=max((self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive2)), (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive))), _YWidth=((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + (2 * drc._NwMinEnclosurePactive)))
        self._DesignParameter['nwlayer']['_XYCoordinates'] = [[0, ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
        self._DesignParameter['OutputRouting']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), (((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), (((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))]]]
        self._DesignParameter['POLY_boundary_21'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_21']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_28'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_28']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_25'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])))
        self._DesignParameter['POLY_boundary_25']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])) / 2)]]
        self._DesignParameter['POLY_boundary_27'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) - ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_27']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), (((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) + ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]


        ''' Pin(Label) '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VSS',
            _XYCoordinates=[[0, 0]]
        )
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VDD',
            _XYCoordinates=[[0, CellHeight]]
        )
        self._DesignParameter['PIN_A'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='A',
            _XYCoordinates=[self.getXY('InputVia_A')[0]],
        )
        # print('XYs: ', self._DesignParameter['PIN_A']['_XYCoordinates'])
        # self._DesignParameter['PIN_EN'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='EN',
        #     _XYCoordinates=[self.getXY('InputVia_EN')[0]],
        # )
        self._DesignParameter['PIN_EN'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='EN',
            _XYCoordinates=[[int(self.getXY('NMOS', '_Met1Layer')[0][0]), YCoordOfInputVia_EN]],
        )
        print('XYs: ', self._DesignParameter['PIN_EN']['_XYCoordinates'])
        self._DesignParameter['PIN_ENb'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='ENb',
            _XYCoordinates=[self.getXY('InputVia_ENb')[0]],
        )
        # print('XYs: ', self._DesignParameter['PIN_ENb']['_XYCoordinates'])
        self._DesignParameter['PIN_Y'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='Y',
            _XYCoordinates=[[0, self.getXY('InputVia_A')[0][1]]]
        )
        # print('XYs: ', self._DesignParameter['PIN_Y']['_XYCoordinates'])

        # CellXWidth
        self.CellXWidth = self.getXY('NMOS', '_PODummyLayer')[-1][0] - self.getXY('NMOS', '_PODummyLayer')[0][0]

    def _CalculateDesignParameterFinger2_v2(self,
                                            NMOSWidth=200,
                                            PMOSWidth=400,

                                            ChannelLength=30,
                                            GateSpacing=100,
                                            XVT='SLVT',

                                            CellHeight=None,            # option
                                            VDD2PMOS=None,
                                            VSS2NMOS=None,
                                            YCoordOfInputA=None,
                                            YCoordOfInputEN=None,
                                            YCoordOfInputENb=None,
                                            SupplyRailType=1
                                            ):
        """
            main def when finger == 2,
            calculate when CellHeight == None

            it uses self._CalculateDesignParameterFinger2_i() -> not support when CellHeight == None
        """
        drc = DRC.DRC()
        tmpLength = NMOSWidth + PMOSWidth

        self._CalculateDesignParameterFinger2_i(
            NMOSWidth=NMOSWidth,
            PMOSWidth=PMOSWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=tmpLength * 10,
            VDD2PMOS=None,
            VSS2NMOS=None,
            YCoordOfInputA=None,
            YCoordOfInputEN=None,
            YCoordOfInputENb=None,
            SupplyRailType=SupplyRailType
        )
        #  InputVia_EN  InputVia_ENb  -  InputVia_A  polygate3
        GapBtw_EN_ENb = (self.getXYBot('InputVia_ENb', '_Met1Layer')[0][1] - self.getXYTop('InputVia_EN', '_Met1Layer')[0][1])
        Margin_byMet1 = GapBtw_EN_ENb - 2 * drc._Metal1MinSpaceAtCorner - self.getYWidth('InputVia_A', '_Met1Layer')
        CellHeight_min = tmpLength * 10 - Margin_byMet1


        if CellHeight == None:
            _CellHeight = CellHeight_min
            print(f"NoneNone CellHeight_min={CellHeight_min} ")
        elif CellHeight < CellHeight_min:
            raise NotImplementedError(f"Input CellHeight={CellHeight}, But CellHeight_min={CellHeight_min}")
        else:
            _CellHeight = CellHeight

        # initialize
        tmpName = self._DesignParameter['_Name']['_Name']
        del self._DesignParameter
        self.__init__(_Name=tmpName)
        self._CalculateDesignParameterFinger2_i(
            NMOSWidth=NMOSWidth,
            PMOSWidth=PMOSWidth,
            ChannelLength=ChannelLength,
            GateSpacing=GateSpacing,
            XVT=XVT,
            CellHeight=_CellHeight,
            VDD2PMOS=VDD2PMOS,
            VSS2NMOS=VSS2NMOS,
            YCoordOfInputA=YCoordOfInputA,
            YCoordOfInputEN=YCoordOfInputEN,
            YCoordOfInputENb=YCoordOfInputENb,
            SupplyRailType=SupplyRailType
        )


    def _CalculateDesignParameterFinger2_i(self,
                                         NMOSWidth=200,
                                         PMOSWidth=400,

                                         ChannelLength=30,
                                         GateSpacing=100,
                                         XVT='SLVT',

                                         CellHeight=1800,           # Required
                                         VDD2PMOS=410,              # Option
                                         VSS2NMOS=310,              # Option

                                         YCoordOfInputA=None,       # Optional
                                         YCoordOfInputEN=None,      # Optional
                                         YCoordOfInputENb=None,     # Optional
                                         SupplyRailType=1
                                         ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = drc._MinSnapSpacing

        if SupplyRailType == 1:
            bool_deleteViaAndMet1 = False
        elif SupplyRailType == 2:
            bool_deleteViaAndMet1 = True
        else:
            raise NotImplementedError

        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=5, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=True, deleteViaAndMet1=bool_deleteViaAndMet1))
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=5, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=False, deleteViaAndMet1=bool_deleteViaAndMet1))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]
        print(f"CellHeight={CellHeight}")

        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=4, _NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength, _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=None, _XVT=XVT))

        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=4, _PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength, _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=None, _XVT=XVT))

        # dummy area
        if '_PODummyLayer' in self._DesignParameter['NMOS']['_DesignObj']._DesignParameter:
            Area_NmosDummy = self.getXWidth('NMOS', '_PODummyLayer') * self.getYWidth('NMOS', '_PODummyLayer')
            if Area_NmosDummy < drc._PODummyMinArea:
                YWidth_NmosDummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth('NMOS', '_PODummyLayer'), MinSnapSpacing * 2)
                self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_NmosDummy_Recalc
            else:
                pass
        else:
            pass
        if '_PODummyLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter:
            Area_PmosDummy = self.getXWidth('PMOS', '_PODummyLayer') * self.getYWidth('PMOS', '_PODummyLayer')
            if Area_PmosDummy < drc._PODummyMinArea:
                YWidth_PmosDummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth('PMOS', '_PODummyLayer'), MinSnapSpacing * 2)
                self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_PmosDummy_Recalc
            else:
                pass
        else:
            pass

        #
        DistanceBtwVSS2NMOS = list()
        DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('VSSRail', '_ODLayer') + self.getYWidth('NMOS', '_ODLayer')) + drc._OdMinSpace)
        DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('VSSRail', '_PPLayer') + self.getYWidth('NMOS', '_ODLayer')) + drc._OdMinSpace2Pp)
        DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('VSSRail', '_ODLayer') + self.getYWidth('NMOS', '_PODummyLayer')) + drc._PolygateMinSpace2OD if '_PODummyLayer' in self._DesignParameter['NMOS']['_DesignObj']._DesignParameter else 0)
        DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('VSSRail', '_Met1Layer') + self.getYWidth('NMOS', '_Met1Layer')) + drc._Metal1MinSpaceAtCorner * 2 + drc._Metal1MinWidth if '_Met1Layer' in self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter else 0.5 * (self.getYWidth('NMOS', '_Met1Layer') + drc._Metal1MinSpaceAtCorner))
        VSS2NMOS_min = max(DistanceBtwVSS2NMOS)
        if VSS2NMOS == None:
            YCoordOfNMOS = VSS2NMOS_min
        elif VSS2NMOS < VSS2NMOS_min:
            raise NotImplementedError(f'VSS2NMOS={VSS2NMOS}, But VSS2NMOS_min={VSS2NMOS_min}')
        else:
            YCoordOfNMOS = VSS2NMOS

        #
        DistanceBtwVDD2PMOS = list()
        DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_ODLayer')) + drc._OdMinSpace)
        DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_PPLayer')) + drc._OdMinSpace2Pp)
        DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('VDDRail', '_ODLayer') + self.getYWidth('PMOS', '_PODummyLayer')) + drc._PolygateMinSpace2OD if '_PODummyLayer' in self._DesignParameter['PMOS']['_DesignObj']._DesignParameter else 0)
        DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('VDDRail', '_Met1Layer') + self.getYWidth('PMOS', '_Met1Layer')) + drc._Metal1MinSpaceAtCorner * 2 + drc._Metal1MinWidth if '_Met1Layer' in self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter else 0.5 * (self.getYWidth('PMOS', '_Met1Layer') + drc._Metal1MinSpaceAtCorner))
        VDD2PMOS_min = max(DistanceBtwVDD2PMOS)
        if VDD2PMOS == None:
            YCoordOfPMOS = CellHeight - VDD2PMOS_min
        elif VDD2PMOS < VDD2PMOS_min:
            raise NotImplementedError(f'VDD2PMOS={VDD2PMOS}, But VDD2PMOS_min={VDD2PMOS_min}')
        else:
            YCoordOfPMOS = CellHeight - VDD2PMOS

        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, YCoordOfNMOS]]
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, YCoordOfPMOS]]

        self._DesignParameter['VSSRouting1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])))
        self._DesignParameter['VSSRouting1']['_XYCoordinates'] = [
            [(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]),
             ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])) / 2)]]
        self._DesignParameter['VSSRouting2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],  _YWidth=self.getYWidth('VSSRouting1'))
        self._DesignParameter['VSSRouting2']['_XYCoordinates'] = [
            [(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]),
             ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])) / 2)]
        ]
        self._DesignParameter['VDDRouting1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VDDRouting1']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), (((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['VDDRouting2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self.getYWidth('VDDRouting1'))
        self._DesignParameter['VDDRouting2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), (((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]

        if SupplyRailType == 2:
            self._DesignParameter['ViaForVSS'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVSS']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVSS']['_XYCoordinates'] = [
                [self.getXY('PMOS', '_Met1Layer')[0][0],  0],
                [self.getXY('PMOS', '_Met1Layer')[-1][0], 0]
            ]
            self._DesignParameter['ViaForVDD'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVDD']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVDD']['_XYCoordinates'] = [
                [self.getXY('PMOS', '_Met1Layer')[0][0],  CellHeight],
                [self.getXY('PMOS', '_Met1Layer')[-1][0], CellHeight]
            ]
        else:
            pass



        self._DesignParameter['nwlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=max((self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive2)), (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive))), _YWidth=((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + (2 * drc._NwMinEnclosurePactive)))
        self._DesignParameter['nwlayer']['_XYCoordinates'] = [[0, ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_pmos_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
        self._DesignParameter['met1_pmos_1']['_XYCoordinates'] = [[0, ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpaceAtCorner) + (drc._Metal1MinWidth / 2))]]
        self._DesignParameter['met1_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['met1_pmos_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_pmos_1']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['met1_boundary_2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['met1_pmos_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_pmos_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_pmos_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['met1_pmos_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_pmos_1']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['met1_pmos_2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['met1_pmos_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_pmos_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_nmos_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
        self._DesignParameter['met1_nmos_1']['_XYCoordinates'] = [[0, ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpaceAtCorner) - (drc._Metal1MinWidth / 2))]]
        self._DesignParameter['met1_nmos_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['met1_nmos_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_nmos_1']['_YWidth'] / 2))))
        self._DesignParameter['met1_nmos_2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['met1_nmos_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_nmos_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_nmos3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['met1_nmos_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_nmos_1']['_YWidth'] / 2))))
        self._DesignParameter['met1_nmos3']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['met1_nmos_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_nmos_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_output_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
        self._DesignParameter['met1_output_1']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpaceAtCorner) + (drc._Metal1MinWidth / 2))]]
        self._DesignParameter['met1_output_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_1']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['met1_output_2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]), (((self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_1']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]

        self._DesignParameter['InputVia_EN'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='InputVia_ENIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_EN']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1))

        # YCoordOfInputEN
        YCoordOfInputEN_min = ((self.getXYTop('met1_output_1')[0][1] + drc._Metal1MinSpaceAtCorner) + ((drc._CoMinWidth / 2) + drc._Metal1MinEnclosureCO2))
        if YCoordOfInputEN == None:
            _YCoordOfInputEN = YCoordOfInputEN_min
        elif YCoordOfInputEN < YCoordOfInputEN_min:
            raise NotImplementedError(f"Input YCoordOfInputEN={YCoordOfInputEN}, but minimum value is {YCoordOfInputEN_min}")
        else:
            _YCoordOfInputEN = YCoordOfInputEN
        # self._DesignParameter['InputVia_EN']['_XYCoordinates'] = [[self._DesignParameter['NMOS']['_XYCoordinates'][0][0], (((self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_1']['_YWidth'] / 2)) + drc._Metal1MinSpaceAtCorner) + ((drc._CoMinWidth / 2) + drc._Metal1MinEnclosureCO2))]]
        self._DesignParameter['InputVia_EN']['_XYCoordinates'] = [[self.getXY('NMOS')[0][0], _YCoordOfInputEN]]

        self._DesignParameter['polygate_en_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate_en_1']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['polygate_en_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate_en_2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][2][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_output_3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
        self._DesignParameter['met1_output_3']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpaceAtCorner) - (drc._Metal1MinWidth / 2))]]
        self._DesignParameter['met1_output_4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_3']['_YWidth'] / 2))))
        self._DesignParameter['met1_output_4']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]), (((self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_3']['_YWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['InputVia_ENb'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='InputVia_ENbIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_ENb']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1))

        # YCoordOfInputEN
        YCoordOfInputENb_max = ((self.getXYBot('met1_output_3')[0][1] - drc._Metal1MinSpaceAtCorner) - ((drc._CoMinWidth / 2) + drc._Metal1MinEnclosureCO2))
        if YCoordOfInputENb == None:
            _YCoordOfInputENb = YCoordOfInputENb_max
        elif YCoordOfInputENb > YCoordOfInputENb_max:
            raise NotImplementedError(f"Input YCoordOfInputENb={YCoordOfInputENb}, but maximum value is {YCoordOfInputENb_max}")
        else:
            _YCoordOfInputENb = YCoordOfInputENb
        # self._DesignParameter['InputVia_ENb']['_XYCoordinates'] = [[self._DesignParameter['PMOS']['_XYCoordinates'][0][0], (((self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_3']['_YWidth'] / 2)) - drc._Metal1MinSpaceAtCorner) - ((drc._CoMinWidth / 2) + drc._Metal1MinEnclosureCO2))]]
        self._DesignParameter['InputVia_ENb']['_XYCoordinates'] = [[self.getXY('PMOS')[0][0], _YCoordOfInputENb]]

        self._DesignParameter['polygate_enb_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate_enb_1']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['polygate_enb_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate_enb_2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][2][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_output_5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_3']['_YWidth'] / 2)) - (self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_1']['_YWidth'] / 2))))
        self._DesignParameter['met1_output_5']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), (((self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_3']['_YWidth'] / 2)) + (self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'],
            _YWidth=CellHeight,
            _XYCoordinates=[[0, (CellHeight / 2)]]
        )


        self._DesignParameter['polygate1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        # self._DesignParameter['polygate1']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['polygate1']['_XYCoordinates'] = [[self.getXY('NMOS', '_POLayer')[0][0], (self.getXYBot('PMOS', '_POLayer')[0][1] + self.getXYTop('NMOS', '_POLayer')[0][1]) / 2]]
        self._DesignParameter['polygate2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['InputVia_A'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_AIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_A']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2, Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))

        # YCoordOfInputEN
        YCoordOfInputA_avg = (self.getXYBot('InputVia_ENb', '_Met1Layer')[0][1] + self.getXYTop('InputVia_EN', '_Met1Layer')[0][1]) / 2
        if YCoordOfInputA == None:
            _YCoordOfInputA = YCoordOfInputA_avg
        else:
            _YCoordOfInputA = YCoordOfInputA
        # self._DesignParameter['InputVia_A']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), self._DesignParameter['polygate1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['InputVia_A']['_XYCoordinates'] = [[self.getXY('NMOS', '_POLayer')[0][0], _YCoordOfInputA]]

        self._DesignParameter['polygate3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=((self._DesignParameter['polygate2']['_XYCoordinates'][0][0] - (self._DesignParameter['polygate2']['_XWidth'] / 2)) - (self._DesignParameter['polygate1']['_XYCoordinates'][0][0] + (self._DesignParameter['polygate1']['_XWidth'] / 2))), _YWidth=50.0)
        self._DesignParameter['polygate3']['_XYCoordinates'] = [[(((self._DesignParameter['polygate1']['_XYCoordinates'][0][0] + (self._DesignParameter['polygate1']['_XWidth'] / 2)) + (self._DesignParameter['polygate2']['_XYCoordinates'][0][0] - (self._DesignParameter['polygate2']['_XWidth'] / 2))) / 2), self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1]]]







        # error check InputVia A
        # InputVia_EN  InputVia_ENb  -  InputVia_A  polygate3

        ''' ---------------------------------------------- Pin(Label) ---------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VSS',
            _XYCoordinates=[[0, 0]]
        )
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VDD',
            _XYCoordinates=[[0, CellHeight]]
        )
        self._DesignParameter['PIN_A'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='A',
            _XYCoordinates=[self.getXY('InputVia_A')[0]],
        )
        self._DesignParameter['PIN_EN'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='EN',
            _XYCoordinates=[self.getXY('InputVia_EN')[0]],
        )
        self._DesignParameter['PIN_ENb'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='ENb',
            _XYCoordinates=[self.getXY('InputVia_ENb')[0]],
        )
        self._DesignParameter['PIN_Y'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='Y',
            _XYCoordinates=[[self.getXY('met1_output_5')[0][0], self.getXY('InputVia_A')[0][1]]]
        )

        # CellXWidth
        self.CellXWidth = self.getXY('NMOS', '_PODummyLayer')[-1][0] - self.getXY('NMOS', '_PODummyLayer')[0][0]



    def _CalculateDesignParameterFinger3orMore_i(self,
                                                  NumFinger_NM1=3,
                                                  NumFinger_NM2=5,
                                                  Width_NM1=200,
                                                  Width_NM2=250,
                                                  Width_PM1=400,
                                                  Width_PM2=500,

                                                  ChannelLength=30,
                                                  GateSpacing=100,
                                                  XVT='SLVT',

                                                  CellHeight=1800,         # Required
                                                  YCoordOfInputA=None,       # Option
                                                  YCoordOfInputEN=None,     # Option
                                                  YCoordOfInputENb=None     # Option
                                                  ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = drc._MinSnapSpacing

        NumFinger_PM1 = NumFinger_NM1
        NumFinger_PM2 = NumFinger_NM2


        NumPitch_NM = ((NumFinger_NM1 + NumFinger_NM2) + 2)
        NumPitch_PM = ((NumFinger_PM1 + NumFinger_PM2) + 2)


        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=max(NumPitch_NM, NumPitch_PM), UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80,
                   Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=max(NumPitch_NM, NumPitch_PM), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=False))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]



        self._DesignParameter['NM1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM1In{}'.format(_Name)))[0]
        self._DesignParameter['NM1']['_DesignObj']._CalculateNMOSDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM1, _NMOSChannelWidth=Width_NM1, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NM1']['_XYCoordinates'] = [[(((- (NumFinger_NM2 + 1)) * (GateSpacing + ChannelLength)) / 2), ((( (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._OdMinSpace2Pp)]]
        self._DesignParameter['NM2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM2In{}'.format(_Name)))[0]
        self._DesignParameter['NM2']['_DesignObj']._CalculateNMOSDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM2, _NMOSChannelWidth=Width_NM2, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NM2']['_XYCoordinates'] = [[(((NumFinger_NM1 + 1) * (GateSpacing + ChannelLength)) / 2), ((((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._OdMinSpace2Pp)]]
        self._DesignParameter['PM1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM1In{}'.format(_Name)))[0]
        self._DesignParameter['PM1']['_DesignObj']._CalculatePMOSDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM1, _PMOSChannelWidth=Width_PM1, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PM1']['_XYCoordinates'] = [[(((- (NumFinger_PM2 + 1)) * (GateSpacing + ChannelLength)) / 2), ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace2Pp) - (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]
        self._DesignParameter['PM2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM2In{}'.format(_Name)))[0]
        self._DesignParameter['PM2']['_DesignObj']._CalculatePMOSDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM2, _PMOSChannelWidth=Width_PM2, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PM2']['_XYCoordinates'] = [[(((NumFinger_PM1 + 1) * (GateSpacing + ChannelLength)) / 2), ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace2Pp) - (self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]


        # dummy area
        forlist = ['NM1', 'NM2', 'PM1', 'PM2']
        for Obj in forlist:
            if '_PODummyLayer' in self._DesignParameter[Obj]['_DesignObj']._DesignParameter:
                Area_NmosDummy = self.getXWidth(Obj, '_PODummyLayer') * self.getYWidth(Obj, '_PODummyLayer')
                if Area_NmosDummy < drc._PODummyMinArea:
                    YWidth_NmosDummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth(Obj, '_PODummyLayer'), MinSnapSpacing * 2)
                    self._DesignParameter[Obj]['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_NmosDummy_Recalc
                else:
                    pass
            else:
                pass


        path_list = []
        if (len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] ==self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] ==self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['VSSRail']['_XYCoordinates'][0][0] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['VSSRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=_width)
        self._DesignParameter['VSSRouting']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['VDDRail']['_XYCoordinates'][0][0] +
                              self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['VDDRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=_width)
        self._DesignParameter['VDDRouting']['_XYCoordinates'] = path_list


        path_list = []
        if (len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['PM1']['_XYCoordinates'][0][1] +
                              self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['PM1']['_XYCoordinates'][0][0] +
                              self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
            for i in range(
                    len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['tttt'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                     _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['tttt']['_XYCoordinates'] = path_list


        topBoundary = self.getXYTop('VDDRail', '_ODLayer')[0][1] + drc._NwMinEnclosurePactive
        botBoundary = min(self.getXYBot('PM1', '_ODLayer')[0][1], self.getXYBot('PM2', '_ODLayer')[0][1]) - drc._NwMinEnclosurePactive

        # self._DesignParameter['nwlayer'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
        #     _Width=((max(abs(((self._DesignParameter['PM2']['_XYCoordinates'][0][0] + self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))), abs(((self._DesignParameter['PM1']['_XYCoordinates'][0][0] + self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)))) + drc._NwMinEnclosurePactive2) * 2))
        # self._DesignParameter['nwlayer']['_XYCoordinates'] = [[[(self._DesignParameter['VDDRail']['_XYCoordinates'][0][0] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive)],
        #                                                        [(self._DesignParameter['VDDRail']['_XYCoordinates'][0][0] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]), (min(((self._DesignParameter['PM1']['_XYCoordinates'][0][1] + self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)), ((self._DesignParameter['PM2']['_XYCoordinates'][0][1] + self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) - drc._NwMinEnclosurePactive)]]]
        self._DesignParameter['nwlayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=((max(abs(((self._DesignParameter['PM2']['_XYCoordinates'][0][0] + self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))), abs(((self._DesignParameter['PM1']['_XYCoordinates'][0][0] + self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)))) + drc._NwMinEnclosurePactive2) * 2),
            _YWidth = topBoundary-botBoundary,
            _XYCoordinates=[[(self._DesignParameter['VDDRail']['_XYCoordinates'][0][0] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]), (topBoundary + botBoundary) / 2]]
        )

        XYList = []
        xy_offset = (0, ((((- (self._DesignParameter['NM1']['_XYCoordinates'][0][1] + self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])) + ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))) + 98) + drc._MetalxMinSpace21))
        for i in range(
                len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if (i % 2) == 1:
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['via1nmos'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1nmosIn{}'.format(_Name)))[0]
        self._DesignParameter['via1nmos']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1nmos']['_XYCoordinates'] = XYList
        XYList = []
        xy_offset = (0, ((((- self._DesignParameter['PM1']['_XYCoordinates'][0][1]) + ((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))) - drc._MetalxMinSpace21) - 98))
        for i in range(
                len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if (i % 2) == 1:
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['via1ForPM1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForPM1In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForPM1']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1ForPM1']['_XYCoordinates'] = XYList


        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'],
            _YWidth=CellHeight)
        self._DesignParameter['XVTLayer']['_XYCoordinates'] = [[0, (CellHeight / 2)]]

        ''' '''
        YWidth_Met1HorizontalRouting = 66
        self._DesignParameter['via1ForNM2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForNM2In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForNM2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1ForPM2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForPM2In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForPM2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))

        tmpXYs_NMintermediate = []
        tmpXYs_PMintermediate = []
        for i in range(len(self.getXY('NM2', '_Met1Layer'))):
            if i % 2 == 0:  # output node
                pass
            else:  # intermediate node
                tmpXYs_NMintermediate.append([
                    self.getXY('NM2', '_Met1Layer')[NumFinger_NM2 - i][0],
                    self.getXY('via1nmos')[0][1]
                ])
                tmpXYs_PMintermediate.append([
                    self.getXY('NM2', '_Met1Layer')[NumFinger_NM2 - i][0],
                    self.getXY('via1ForPM1')[0][1]
                ])
        self._DesignParameter['via1ForNM2']['_XYCoordinates'] = tmpXYs_NMintermediate
        self._DesignParameter['via1ForPM2']['_XYCoordinates'] = tmpXYs_PMintermediate


        YWidth_Met1RouteY_NMout = max(0, (self.getXY('via1ForNM2', '_Met1Layer')[0][1] + self.getYWidth('via1ForNM2', '_Met1Layer') / 2) - (self.getXY('NM2', '_Met1Layer')[0][1] + self.getYWidth('NM2', '_Met1Layer') / 2)) + drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting
        YWidth_Met1RouteY_PMout = max(0, -(self.getXY('via1ForPM2', '_Met1Layer')[0][1] - self.getYWidth('via1ForPM2', '_Met1Layer') / 2) + (self.getXY('PM2', '_Met1Layer')[0][1] - self.getYWidth('PM2', '_Met1Layer') / 2)) + drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting

        self._DesignParameter['Met1RouteY_NMout'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('NM2', '_Met1Layer'),
            _YWidth=YWidth_Met1RouteY_NMout)
        self._DesignParameter['Met1RouteY_PMout'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('PM2', '_Met1Layer'),
            _YWidth=YWidth_Met1RouteY_PMout)

        tmpXYs_NMout = []
        tmpXYs_PMout = []
        for i in range(len(self.getXY('NM2', '_Met1Layer'))):
            if i % 2 == 0:  # output node
                tmpXYs_NMout.append([
                    self.getXY('NM2', '_Met1Layer')[NumFinger_NM2 - i][0],
                    self.getXY('NM2', '_Met1Layer')[0][1] + self.getYWidth('NM2', '_Met1Layer') / 2 + self.getYWidth('Met1RouteY_NMout') / 2
                ])
                tmpXYs_PMout.append([
                    self.getXY('NM2', '_Met1Layer')[NumFinger_NM2 - i][0],
                    self.getXY('PM2', '_Met1Layer')[0][1] - self.getYWidth('PM2', '_Met1Layer') / 2 - self.getYWidth('Met1RouteY_PMout') / 2
                ])
            else:
                pass

        self._DesignParameter['Met1RouteY_NMout']['_XYCoordinates'] = tmpXYs_NMout
        self._DesignParameter['Met1RouteY_PMout']['_XYCoordinates'] = tmpXYs_PMout



        ''' '''
        RightBoundary_Met2RouteX = CoordCalc.getXYCoords_MaxX(self.getXY('via1ForPM1') + self.getXY('via1ForPM2'))[0][0]
        LeftBoundary_Met2RouteX = CoordCalc.getXYCoords_MinX(self.getXY('via1ForPM1') + self.getXY('via1ForPM2'))[0][0]

        self._DesignParameter['Met2RouteX_PM1PM2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=(RightBoundary_Met2RouteX - LeftBoundary_Met2RouteX),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met2RouteX_PM1PM2']['_XYCoordinates'] = [[
            (RightBoundary_Met2RouteX + LeftBoundary_Met2RouteX) / 2,
            self.getXY('via1ForPM2')[0][1]
        ]]

        self._DesignParameter['Met2RouteX_NM1NM2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=(RightBoundary_Met2RouteX - LeftBoundary_Met2RouteX),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met2RouteX_NM1NM2']['_XYCoordinates'] = [[
            (RightBoundary_Met2RouteX + LeftBoundary_Met2RouteX) / 2,
            self.getXY('via1ForNM2')[0][1]
        ]]

        RightBoundary_Met1XOut = CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_NMout') + self.getXY('Met1RouteY_NMout'))[0][0]
        LeftBoundary_Met1XOut = CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_NMout') + self.getXY('Met1RouteY_NMout'))[0][0]

        self._DesignParameter['Met1RouteX_NMOut'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=(RightBoundary_Met1XOut - LeftBoundary_Met1XOut) + self.getXWidth('Met1RouteY_NMout'),
            _YWidth=drc._Metal1MinWidth
        )
        self._DesignParameter['Met1RouteX_NMOut']['_XYCoordinates'] = [[
            (RightBoundary_Met1XOut + LeftBoundary_Met1XOut) / 2,
            self.getXY('Met1RouteY_NMout')[0][1] + self.getYWidth('Met1RouteY_NMout') / 2 - self.getYWidth('Met1RouteX_NMOut') / 2
        ]]

        self._DesignParameter['Met1RouteX_PMOut'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=(RightBoundary_Met1XOut - LeftBoundary_Met1XOut) + self.getXWidth('Met1RouteY_PMout'),
            _YWidth=drc._Metal1MinWidth
        )
        self._DesignParameter['Met1RouteX_PMOut']['_XYCoordinates'] = [[
            (RightBoundary_Met1XOut + LeftBoundary_Met1XOut) / 2,
            self.getXY('Met1RouteY_PMout')[0][1] - self.getYWidth('Met1RouteY_PMout') / 2 + self.getYWidth('Met1RouteX_PMOut') / 2
        ]]

        TopBoundary_Met1YOut = (self.getXY('Met1RouteX_PMOut')[0][1] - self.getYWidth('Met1RouteX_PMOut') / 2)
        BotBoundary_Met1YOut = (self.getXY('Met1RouteX_NMOut')[0][1] + self.getYWidth('Met1RouteX_NMOut') / 2)
        # XWidth_Met1YOut = self.getXWidth('Met1RouteY_PMout') * (len(self.getXY('Met1RouteY_PMout')) // 2)
        XWidth_Met1YOut = self.getXWidth('Met1RouteY_PMout')

        self._DesignParameter['Met1RouteY_Out'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=XWidth_Met1YOut,
            _YWidth=TopBoundary_Met1YOut - BotBoundary_Met1YOut
        )
        self._DesignParameter['Met1RouteY_Out']['_XYCoordinates'] = [[
            self.getXY('NM2', '_Met1Layer')[-1][0] + self.getXWidth('NM2', '_Met1Layer') / 2 - self.getXWidth('Met1RouteY_Out') / 2,
            (TopBoundary_Met1YOut + BotBoundary_Met1YOut) / 2
        ]]


        ''' Input Via A ''' ##
        # # prev. one
        # topBoundary = min(self.getXYBot('PM1', '_Met1Layer')[0][1], self.getXYBot('via1ForPM2', '_Met1Layer')[0][1])
        # botBoundary = max(self.getXYTop('NM1', '_Met1Layer')[0][1], self.getXYTop('via1ForNM2', '_Met1Layer')[0][1])
        # _YCoordOfInputA = (topBoundary + botBoundary) / 2 if YCoordOfInputA is None else YCoordOfInputA

        RightBoudary_InputViaA = self.getXY('NM1', '_POLayer')[-1][0] + self.getXWidth('NM1', '_POLayer') / 2 - drc._CoMinEnclosureByPOAtLeastTwoSide
        LeftBoudary_InputViaA = self.getXY('NM1', '_POLayer')[0][0] - self.getXWidth('NM1', '_POLayer') / 2 + drc._CoMinEnclosureByPOAtLeastTwoSide
        NumViaX_InputA = int((RightBoudary_InputViaA - LeftBoudary_InputViaA - drc._CoMinWidth) // (drc._CoMinWidth + drc._CoMinSpace) + 1)

        self._DesignParameter['polyInputA'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='polyInputAIn{}'.format(_Name)))[0]
        self._DesignParameter['polyInputA']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputA, _ViaPoly2Met1NumberOfCOY=1))
        self._DesignParameter['polyInputA']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = 66

        # boundary => polyInputA's center Ycoordinate
        topBoundary_byMet1 = min(self.getXYBot('PM1', '_Met1Layer')[0][1], self.getXYBot('via1ForPM2', '_Met1Layer')[0][1]) - drc._Metal1MinSpaceAtCorner - self.getYWidth('polyInputA', '_Met1Layer') / 2
        botBoundary_byMet1 = max(self.getXYTop('NM1', '_Met1Layer')[0][1], self.getXYTop('via1ForNM2', '_Met1Layer')[0][1]) + drc._Metal1MinSpaceAtCorner + self.getYWidth('polyInputA', '_Met1Layer') / 2
        topBoundary_byPolyAndOD = self.getXYBot('PM1', '_ODLayer')[0][1] - drc._PolygateMinSpace2OD2 - self.getYWidth('polyInputA', '_POLayer') / 2
        botBoundary_byPolyAndOD = self.getXYTop('NM1', '_ODLayer')[0][1] + drc._PolygateMinSpace2OD2 + self.getYWidth('polyInputA', '_POLayer') / 2
        topBoundary = min(topBoundary_byMet1, topBoundary_byPolyAndOD)
        botBoundary = max(botBoundary_byMet1, botBoundary_byPolyAndOD)
        if topBoundary < botBoundary:
            raise NotImplementedError

        _YCoordOfInputA = (topBoundary + botBoundary) / 2 if YCoordOfInputA is None else YCoordOfInputA


        self._DesignParameter['polyInputA']['_XYCoordinates'] = [
            [(RightBoudary_InputViaA + LeftBoudary_InputViaA) / 2, _YCoordOfInputA]
        ]
        self._DesignParameter['PolyboundaryInputA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXY('NM1', '_POLayer')[-1][0]-self.getXY('NM1', '_POLayer')[0][0]+self.getXWidth('NM1', '_POLayer'),
            _YWidth=self.getYWidth('polyInputA', '_POLayer'),
            _XYCoordinates=self.getXY('polyInputA')
        )


        ''' Input Via EN/ENb '''
        RightBoudary_InputViaEN = self.getXY('Met1RouteY_Out')[0][0] - self.getXWidth('Met1RouteY_Out') / 2 - drc._Metal1MinSpaceAtCorner - drc._Metal1MinEnclosureCO2
        LeftBoudary_InputViaEN = self.getXY('NM2', '_POLayer')[0][0] - self.getXWidth('NM2', '_POLayer') / 2 + drc._CoMinEnclosureByPOAtLeastTwoSide
        NumViaX_InputEN = int((RightBoudary_InputViaEN - LeftBoudary_InputViaEN - drc._CoMinWidth) // (drc._CoMinWidth + drc._CoMinSpace) + 1)

        self._DesignParameter['polyInputEN'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='polyInputENIn{}'.format(_Name)))[0]
        self._DesignParameter['polyInputEN']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputEN, _ViaPoly2Met1NumberOfCOY=1))
        self._DesignParameter['polyInputENb'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='polyInputENbIn{}'.format(_Name)))[0]
        self._DesignParameter['polyInputENb']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputEN, _ViaPoly2Met1NumberOfCOY=1))
        self._DesignParameter['polyInputEN']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = 66
        self._DesignParameter['polyInputENb']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = 66

        drcTmp58 = 58
        if YCoordOfInputEN is None:
            _YCoordOfInputEN = self.getXY('Met1RouteX_NMOut')[0][1] + self.getYWidth('Met1RouteX_NMOut') / 2 + drcTmp58 + self.getYWidth('polyInputEN', '_Met1Layer') / 2
        else:
            _YCoordOfInputEN = YCoordOfInputEN

        if YCoordOfInputENb is None:
            _YCoordOfInputENb = self.getXY('Met1RouteX_PMOut')[0][1] - self.getYWidth('Met1RouteX_PMOut') / 2 - drcTmp58 - self.getYWidth('polyInputENb', '_Met1Layer') / 2
        else:
            _YCoordOfInputENb = YCoordOfInputENb

        self._DesignParameter['polyInputEN']['_XYCoordinates'] = [
            [(RightBoudary_InputViaEN + LeftBoudary_InputViaEN) / 2, _YCoordOfInputEN]
        ]
        self._DesignParameter['polyInputENb']['_XYCoordinates'] = [
            [(RightBoudary_InputViaEN + LeftBoudary_InputViaEN) / 2, _YCoordOfInputENb]
        ]

        self._DesignParameter['PolyboundaryInputENENb'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXY('NM2', '_POLayer')[-1][0] - self.getXY('NM2', '_POLayer')[0][0] + self.getXWidth('NM2', '_POLayer'),
            _YWidth=self.getYWidth('polyInputEN', '_POLayer'),
            _XYCoordinates=[
                [self.getXY('NM2')[0][0], self.getXY('polyInputEN')[0][1]],
                [self.getXY('NM2')[0][0], self.getXY('polyInputENb')[0][1]],
            ]
        )

        '''  '''
        topBoundary_PolyRouteYNM2 = self.getXY('PolyboundaryInputENENb')[0][1] - self.getYWidth('PolyboundaryInputENENb') / 2
        botBoundary_PolyRouteYNM2 = self.getXY('NM2', '_POLayer')[0][1] + self.getYWidth('NM2', '_POLayer') / 2
        self._DesignParameter['PolyRouteYNM2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('NM2', '_POLayer'),
            _YWidth=topBoundary_PolyRouteYNM2-botBoundary_PolyRouteYNM2
        )
        tmpXYs = []
        for XYs in self.getXY('NM2', '_POLayer'):
            tmpXYs.append([XYs[0], (topBoundary_PolyRouteYNM2 + botBoundary_PolyRouteYNM2) / 2])
        self._DesignParameter['PolyRouteYNM2']['_XYCoordinates'] = tmpXYs

        botBoundary_PolyRouteYPM2 = self.getXY('PolyboundaryInputENENb')[1][1] + self.getYWidth('PolyboundaryInputENENb') / 2
        topBoundary_PolyRouteYPM2 = self.getXY('PM2', '_POLayer')[0][1] - self.getYWidth('PM2', '_POLayer') / 2
        self._DesignParameter['PolyRouteYPM2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('PM2', '_POLayer'),
            _YWidth=topBoundary_PolyRouteYPM2 - botBoundary_PolyRouteYPM2
        )
        tmpXYs = []
        for XYs in self.getXY('PM2', '_POLayer'):
            tmpXYs.append([XYs[0], (topBoundary_PolyRouteYPM2 + botBoundary_PolyRouteYPM2) / 2])
        self._DesignParameter['PolyRouteYPM2']['_XYCoordinates'] = tmpXYs


        ''' ---------------------------------------------- Pin(Label) ---------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VSS',
            _XYCoordinates=[[0, 0]]
        )
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VDD',
            _XYCoordinates=[[0, CellHeight]]
        )
        self._DesignParameter['PIN_A'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='A',
            _XYCoordinates=[self.getXY('polyInputA')[0]],
        )
        self._DesignParameter['PIN_EN'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='EN',
            _XYCoordinates=[self.getXY('polyInputEN')[0]],
        )
        self._DesignParameter['PIN_ENb'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='ENb',
            _XYCoordinates=[self.getXY('polyInputENb')[0]],
        )
        self._DesignParameter['PIN_Y'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='Y',
            _XYCoordinates=[[self.getXY('Met1RouteY_Out')[0][0], self.getXY('polyInputA')[0][1]]]
        )



        # CellXWidth
        self.CellXWidth = self.getXY('NM2', '_PODummyLayer')[-1][0] - self.getXY('NM1', '_PODummyLayer')[0][0]


if __name__ == '__main__':
    from Private import Myinfo
    import DRCchecker_test2 as DRCchecker
    from generatorLib.IksuPack import PlaygroundBot

    My = Myinfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)


    libname = 'TEST_TSINV'
    cellname = 'TristateInv'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''

    # InputParams = dict(
    #     NumFinger=1,
    #     PMOSWidth=500,
    #     NMOSWidth=250,
    #
    #     ChannelLength=30,
    #     GateSpacing=100,
    #     XVT='SLVT',
    #
    #     CellHeight=None,  # Option
    #     VDD2PMOS=None,  # Option (Not work when finger >= 3)
    #     VSS2NMOS=None,  # Option (Not work when finger >= 3)
    #
    #     YCoordOfInputA=None,  # Optional
    #     YCoordOfInputEN=None,  # Optional
    #     YCoordOfInputENb=None,  # Optional
    #     SupplyRailType=2  # (Not work when finger >= 3)
    # )
    InputParams = dict(
        NumFinger_NM1 = 3,
        NumFinger_NM2 = 5,
        Width_NM1 = 400,
        Width_NM2 = 250,
        Width_PM1 = 800,
        Width_PM2 = 500,

        CellHeight = 1900,  # Option
        YCoordOfInputA = None,  # Option
        YCoordOfInputEN = None,  # Option
        YCoordOfInputENb = None,  # Option

        ChannelLength = 30,
        GateSpacing = 100,
        XVT = 'SLVT'
    )


    Mode_DRCCheck = False  # True | False
    Num_DRCCheck = 50

    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        GDSDir=My.Dir_GDS,
        libname=libname,
        cellname=cellname,
    )

    if Mode_DRCCheck:
        ErrCount = 0            # DRC error
        knownErrorCount = 0     # failed to generate design. NotImplementedError

        start_time = time.time()
        for ii in range(0, Num_DRCCheck):
            if ii == 0:
                Bot.send2Bot(f'Start DRC checker...\nCellName: {cellname}\nTotal # of Run: {Num_DRCCheck}')

            forLoopCntMax = 10
            for iii in range(0, forLoopCntMax):
                try:
                    ''' ------------------------------- Random Parameters for Layout Object -------------------------------- '''
                    # InputParams['NumFinger'] = DRCchecker.RandomParam(start=1, stop=15, step=1)
                    # InputParams['PMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    # InputParams['NMOSWidth'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)

                    InputParams['NumFinger_NM1'] = DRCchecker.RandomParam(start=3, stop=10, step=1)
                    InputParams['NumFinger_NM2'] = DRCchecker.RandomParam(start=3, stop=10, step=1)
                    InputParams['Width_NM1'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Width_NM2'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Width_PM1'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Width_PM2'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)

                    print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                    tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
                    print(tmpStr)
                    print("".center(105, '='))

                    ''' ---------------------------------- Generate Layout Object -------------------------------------------'''
                    LayoutObj = TristateInverter(_Name=cellname)
                    # LayoutObj._CalculateDesignParameter(**InputParams)
                    LayoutObj._CalculateDesignParameterF3(**InputParams)
                    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
                    testStreamFile = open('./{}'.format(_fileName), 'wb')
                    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
                    tmp.write_binary_gds_stream(testStreamFile)
                    testStreamFile.close()
                except NotImplementedError:  # something known error !
                    print(f"forLoopCnt = {iii + 1}")
                    if iii + 1 == forLoopCntMax:
                        raise NotImplementedError
                else:
                    knownErrorCount = knownErrorCount + iii
                    # Bot.send2Bot(f"NotImplementedError...\nknownErrorCount = {knownErrorCount}")
                    break
            # end of for loop

            print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
            Checker.Upload2FTP()
            Checker.StreamIn(tech=DesignParameters._Technology)

            print(f'   DRC checking... {ii + 1}/{Num_DRCCheck}   '.center(105, '#'))
            try:
                Checker.DRCchecker()
            except Exception as e:      # something error
                ErrCount = ErrCount + 1
                print('Error Occurred: ', e)
                print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                print(tmpStr)
                print("".center(105, '='))
                m, s = divmod(time.time() - start_time, 60)
                h, m = divmod(m, 60)
                Bot.send2Bot(f'Error Occurred During Checking DRC({ii + 1}/{Num_DRCCheck})...\n'
                             f'CellName : {cellname}\n'
                             f'ErrMsg : {e}\n'
                             f'============================\n'
                             f'** InputParameters:\n'
                             f'{tmpStr}\n'
                             f'============================\n'
                             f'** Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')

            if (ii + 1) == Num_DRCCheck:
                elapsed_time = time.time() - start_time
                m, s = divmod(elapsed_time, 60)
                h, m = divmod(m, 60)
                Bot.send2Bot(f'DRC Checker Finished.\n'
                             f'CellName: {cellname}\n'
                             f'Total # of known Err: {knownErrorCount}\n'
                             f'Total # of DRC Err: {ErrCount}\n'
                             f'Total # of Run: {Num_DRCCheck}\n'
                             f'Elapsed Time: {int(h)}:{int(m):0>2}:{int(s):0>2}s')
    else:
        ''' ------------------------------------ Generate Layout Object ---------------------------------------------'''
        LayoutObj = TristateInverter(_Name=cellname)
        # LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._CalculateDesignParameterF3(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)

    print('      Finished       '.center(105, '#'))
