import re #used to read drc_rule file
import math
from gds_editor_ver3 import user_define_exceptions
from generatorLib import DesignParameters
import user_setup
_Technology= user_setup._Technology


class DRCMultiplicantForMinEdgeWidth:  ####????????????????????????????????????????????????????????????????????????
    def __init__(self):
        if DesignParameters._Technology == 'SS28nm':
            self._MultiplicantForMinEdgeWidth = 1
        if DesignParameters._Technology == 'TSMC45nm':
            self._MultiplicantForMinEdgeWidth = 1
        if DesignParameters._Technology == 'TSMC65nm':
            self._MultiplicantForMinEdgeWidth = 1
        if DesignParameters._Technology == 'TSMC90nm':
            self._MultiplicantForMinEdgeWidth = 0
        if DesignParameters._Technology == 'TSMC130nm':
            self._MultiplicantForMinEdgeWidth = 0
        if DesignParameters._Technology == 'TSMC180nm':
            self._MultiplicantForMinEdgeWidth = 0

    def DRCMinEdgeWidth(self, _MinWidth=None):
        return self._MultiplicantForMinEdgeWidth * _MinWidth


class DRCMinSnapSpacing:  ####????????????????????????????????????????????????????????????????????????
    def __init__(self):
        if DesignParameters._Technology == 'SS28nm':
            self._MinSnapSpacing = 1
        if DesignParameters._Technology == 'TSMC45nm':
            self._MinSnapSpacing = 5
        if DesignParameters._Technology == 'TSMC65nm':
            self._MinSnapSpacing = 5
        if DesignParameters._Technology == 'TSMC90nm':
            self._MinSnapSpacing = 5
        if DesignParameters._Technology == 'TSMC130nm':
            self._MinSnapSpacing = 5
        if DesignParameters._Technology == 'TSMC180nm':
            self._MinSnapSpacing = 5


class DRCOD:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._OdMinWidth = 60
            self._OdMinSpace = 80
            self._OdMinSpace3 = 100
        if DesignParameters._Technology == 'SS28nm':
            self._OdMinWidth = 78
            self._OdMinSpace = 80
            self._OdMinSpace3 = 100
        if DesignParameters._Technology == 'TSMC65nm':
            self._OdMinWidth = 150
            self._OdMinSpace = 110
            self._OdMinSpace3 = 130
        if DesignParameters._Technology == 'TSMC90nm':
            self._OdMinWidth = 110
            self._OdMinSpace = 140
            self._OdMinSpace2 = 160
        if DesignParameters._Technology == 'TSMC130nm':
            self._OdMinWidth = 150
            self._OdMinSpace = 210
        if DesignParameters._Technology == 'TSMC180nm':
            self._OdMinWidth = 220
            self._OdMinSpace = 280

    def DRCODMinSpace(self, _Width=None, _ParallelLength=None, ):
        if DesignParameters._Technology == 'TSMC45nm':
            if _Width == None and _ParallelLength == None:
                return self._OdMinSpace
            elif (120 < _Width and 140 < _ParallelLength):
                return self._OdMinSpace3

            else:
                return self._OdMinSpace

        if DesignParameters._Technology == 'SS28nm':
            return self._OdMinSpace

        if DesignParameters._Technology == 'TSMC65nm':
            if _Width == None and _ParallelLength == None:
                return self._OdMinSpace
            elif (150 < _Width and 200 < _ParallelLength):
                return self._OdMinSpace3

            else:
                return self._OdMinSpace
        if DesignParameters._Technology == 'TSMC90nm':
            if _Width == None and _ParallelLength == None:
                return self._OdMinSpace
            elif (300 < _Width and 230 < _ParallelLength):
                return self._OdMinSpace2

            else:
                return self._OdMinSpace
        if DesignParameters._Technology == 'TSMC130nm':
            return self._OdMinSpace

        if DesignParameters._Technology == 'TSMC180nm':
            return self._OdMinSpace


class DRCPP:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._PpMinWidth = 180
            self._PpMinSpace = 180
            self._PpMinExtensiononPactive = 80
            self._PpMinEnclosureOfPo = 110
            self._PpMinEnclosureOfPtypePoRes = 140
        if DesignParameters._Technology == 'SS28nm':
            self._PpMinWidth = 170
            self._PpMinSpace = 170
            self._PpMinExtensiononPactive = 56
            self._PpMinExtensiononPactive2 = 21
            self._PpMinEnclosureOfPo = 0
            self._PpMinEnclosureOfPo2 = 0
            self._PpMinEnclosureOfPtypePoRes = 240
            self._PpMinExtensiononPactive3 = 20

            self._PpMinSpacetoPRES = 170  ##ADDED BY Junung
            self._RXMinSpacetoPRES = 230  ##Added By Junung
            self._RXMinSpacetoOP = 160  ## Added By Junung
            self._PpMinArea = 160000  ## Added By Junung

        if DesignParameters._Technology == 'TSMC65nm':
            self._PpMinWidth = 180
            self._PpMinSpace = 180
            self._PpMinExtensiononPactive = 130
            self._PpMinExtensiononPactive2 = 20  # PP.EX.2  Pactive2 -> for suppy rail (PW STRAP)
            self._PpMinEnclosureOfPo = 150
            self._PpMinEnclosureOfPtypePoRes = 200
        if DesignParameters._Technology == 'TSMC90nm':
            self._PpMinWidth = 240
            self._PpMinSpace = 240
            self._PpMinExtensiononPactive = 130
            self._PpMinEnclosureOfPo = 200
            self._PpMinEnclosureOfPtypePoRes = 200
        if DesignParameters._Technology == 'TSMC130nm':
            self._PpMinWidth = 310
            self._PpMinSpace = 310
            self._PpMinExtensiononPactive = 180
            self._PpMinEnclosureOfPo = 200
            self._PpMinEnclosureOfPtypePoRes = 200
        if DesignParameters._Technology == 'TSMC180nm':
            self._PpMinWidth = 440
            self._PpMinSpace = 440
            self._PpMinExtensiononPactive = 180
            self._PpMinEnclosureOfPo = 320
            self._PpMinEnclosureOfPtypePoRes = 180


class DRCNP:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._NpMinWidth = 180
            self._NpMinSpace = 180
            self._NpMinExtensiononNactive = 80
            self._NpMinEnclosureOfPo = 110
        if DesignParameters._Technology == 'SS28nm':  # There is no NP layer in 28nm, junung
            self._NpMinWidth = 180
            self._NpMinSpace = 180
            self._NpMinExtensiononNactive = 130
            self._NpMinEnclosureOfPo = 150
        if DesignParameters._Technology == 'TSMC65nm':
            self._NpMinWidth = 180
            self._NpMinSpace = 180
            self._NpMinExtensiononNactive = 130
            self._NpMinExtensiononNactive2 = 20  # Nactive2 -> for supply rail
            self._NpMinEnclosureOfPo = 150
        if DesignParameters._Technology == 'TSMC90nm':
            self._NpMinWidth = 240
            self._NpMinSpace = 240
            self._NpMinExtensiononNactive = 130
            self._NpMinEnclosureOfPo = 200
        if DesignParameters._Technology == 'TSMC130nm':
            self._NpMinWidth = 310
            self._NpMinSpace = 310
            self._NpMinExtensiononNactive = 180
            self._NpMinEnclosureOfPo = 200
        if DesignParameters._Technology == 'TSMC180nm':
            self._NpMinWidth = 440
            self._NpMinSpace = 440
            self._NpMinExtensiononNactive = 180
            self._NpMinEnclosureOfPo = 320


class DRCPOLYGATE:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._PolygateMinWidth = 40
            self._PolygateMinSpace = 100
            self._PolygateMinSpace2 = 160
            self._PolygateMinSpace2Co = 40
            self._PolygateMinSpace2OD = 30
            self._PolygateMinSpace2PolygateInSameRPO = 180
            # self._PolygateMinEnclosureByNW=1000
            self._PolygateMinExtensionOnOD = 90
            self._PolygateOnODMinWidth1 = 140
            self._PolygateOnODMinWidth2 = 160
            self._PolygateOnODMinWidth3 = 200
            self._PolygateMinSpaceAtCorner = 110

        if DesignParameters._Technology == 'SS28nm':
            self._PolygateMinWidth = 30
            self._PolygateMinSpace = 96
            self._PolygateMinSpace2 = 114
            self._PolygateMinSpace2Co = 28
            self._PolygateMinSpace2OD = 20
            self._PolygateMinSpace2PolygateInSameRPO = 96
            self._PolygateMinExtensionOnOD = 57  # ##?? -> Check GRSLVT9b
            self._PolygateMinExtensionOnOD2 = 70
            self._PolygateMinExtensionOnOD3 = 105
            self._PolygateMinSpaceAtCorner = 96
            self._PMOS2GuardringMinSpace = 90
            self._NMOS2GuardringMinSpace = 90
            self._PolygateWithPCCRIT = 71

            self._OPlayeroverPoly = 200  ### Created by junung for OP layer rules
            self._PolyoverOPlayer = 400  ### Created by junung for OP layer rules
            self._PRESlayeroverPoly = 240  ### Created by junung for OP layer rules

            self._PCCRITExtension = 5  ### ADDED(by JiCho)!
            self._PCCRITMinLengthofPOLayer = 35  #### ADDED(by JiCho) !
            self._PODummyMinArea = 11000  ### ADDED(by JiCho)!
            self._PoDummyLengthToMove = 50  ### ADDED(by JiCho)!
            # self._PODummyMinSpace1 = 96
            # self._PODummyMinSpace2 = 222

        if DesignParameters._Technology == 'TSMC65nm':
            self._PolygateMinWidth = 60  # A
            self._PolygateMinSpace = 120  # F
            self._PolygateMinSpace2 = 180  # L PO.S.7
            self._PolygateMinSpace2Co = 55  # ???????????????
            self._PolygateMinSpace2OD = 50  # ???????????????
            self._PolygateMinSpace2PolygateInSameRPO = 250  # N
            # self._PolygateMinEnclosureByNW=1000
            self._PolygateMinExtensionOnOD = 140  # O
            self._PolygateMinExtensionOnODX = 115  # PO.EX.2
            self._PolygateMinSpaceAtCorner = 140  # S1/S2
            self._PODummyMinArea = 51000
        if DesignParameters._Technology == 'TSMC90nm':
            self._PolygateMinWidth = 100
            self._PolygateMinSpace = 140
            self._PolygateMinSpace2 = 180
            self._PolygateMinSpace2Co = 70
            self._PolygateMinSpace2OD = 50
            self._PolygateMinSpace2PolygateInSameRPO = 250
            # self._PolygateMinEnclosureByNW=430
            self._PolygateMinExtensionOnOD = 160
            self._PolygateMinSpaceAtCorner = 140
        if DesignParameters._Technology == 'TSMC130nm':
            self._PolygateMinWidth = 130
            self._PolygateMinSpace = 180
            self._PolygateMinSpace2Co = 110
            self._PolygateMinSpace2OD = 70
            self._PolygateMinSpace2PolygateInSameRPO = 180
            # self._PolygateMinEnclosureByNW=430
            self._PolygateMinExtensionOnOD = 180
            self._PolygateMinSpaceAtCorner = 180
        if DesignParameters._Technology == 'TSMC180nm':
            self._PolygateMinWidth = 180
            self._PolygateMinSpace = 375
            self._PolygateMinSpace2Co = 220
            self._PolygateMinSpace2OD = 100
            self._PolygateMinSpace2PolygateInSameRPO = 250
            # self._PolygateMinEnclosureByNW=430
            self._PolygateMinExtensionOnOD = 220
            self._PolygateMinSpaceAtCorner = 375

    def DRCPolygateMinExtensionOnOD(self, _ChannelLength = None):
        if _ChannelLength == None:
            raise NotImplementedError
        if DesignParameters._Technology == 'SS28nm':
            if _ChannelLength < 70:
                return self._PolygateMinExtensionOnOD
            elif 70 <= _ChannelLength < 90:
                return self._PolygateMinExtensionOnOD2
            elif _ChannelLength >= 90:
                return self._PolygateMinExtensionOnOD3
        if DesignParameters._Technology == 'TSMC65nm':
            return self._PolygateMinExtensionOnOD

    def DRCPolygateMinSpace(self, _TmpLengthBtwPolyEdge=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if _TmpLengthBtwPolyEdge <= self._PolygateOnODMinWidth1:
                return self._PolygateOnODMinWidth1
            elif _TmpLengthBtwPolyEdge <= self._PolygateOnODMinWidth2:
                return self._PolygateOnODMinWidth2
            elif _TmpLengthBtwPolyEdge <= self._PolygateOnODMinWidth3:
                return self._PolygateOnODMinWidth3

        if DesignParameters._Technology == 'SS28nm':
            return _TmpLengthBtwPolyEdge
        if DesignParameters._Technology == 'TSMC65nm':
            return _TmpLengthBtwPolyEdge
        if DesignParameters._Technology == 'TSMC90nm':
            return _TmpLengthBtwPolyEdge
        if DesignParameters._Technology == 'TSMC130nm':
            return _TmpLengthBtwPolyEdge
        if DesignParameters._Technology == 'TSMC180nm':
            return _TmpLengthBtwPolyEdge

    # def DRCPolyDummyMinSpace(self, _Width=None, _ParallelLength=None):
    #     if DesignParameters._Technology=='SS28nm':
    #         if _Width==None  and _ParallelLength < 48:
    #             return self._PolygateMinSpace1
    #         else:
    #             return self._PolygateMinSpace2

    def DRCPolyMinSpace(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if _Width == None and _ParallelLength == None:
                return self._PolygateMinSpace
            elif 120 < _Width and 140 < _ParallelLength:
                return self._PolygateMinSpace2
            else:
                return self._PolygateMinSpace

        if DesignParameters._Technology == 'SS28nm':
            if _ParallelLength < 48:
                return self._PolygateMinSpace
            else:
                return self._PolygateMinSpace2

        if DesignParameters._Technology == 'TSMC65nm':
            if _Width == None and _ParallelLength == None:
                return self._PolygateMinSpace
            elif 130 < _Width and 180 < _ParallelLength:
                return self._PolygateMinSpace2
            else:
                return self._PolygateMinSpace

        if DesignParameters._Technology == 'TSMC90nm':
            if _Width == None and _ParallelLength == None:
                return self._PolygateMinSpace
            elif 230 < _Width and 300 < _ParallelLength:
                return self._PolygateMinSpace2
            else:
                return self._PolygateMinSpace

        if DesignParameters._Technology == 'TSMC130nm':
            if _Width == None and _ParallelLength == None:
                return self._PolygateMinSpace
            else:
                return self._PolygateMinSpace

        if DesignParameters._Technology == 'TSMC180nm':
            if _Width == None and _ParallelLength == None:
                return self._PolygateMinSpace
            else:
                return self._PolygateMinSpace


class DRCCO:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._CoMinWidth = 60
            self._CoMinSpace = 80
            self._CoMinSpace2 = 100
            self._CoMinSpaceDifferentNet = 110
            self._CoMinSpaceFor3neighboring = 110
            self._CoMinEnclosureByOD = 10
            self._CoMinEnclosureByODAtLeastTwoSide = 30
            self._CoMinEnclosureByPO = 10
            self._CoMinEnclosureByPOAtLeastTwoSide = 20

        if DesignParameters._Technology == 'SS28nm':
            self._CoMinWidth = 40
            self._CoMinSpace = 60
            self._CoMinSpace2 = 60
            self._CoMinSpaceDifferentNet = 78
            self._CoMinSpaceFor3neighboring = 92
            self._CoMinEnclosureByOD = 8
            self._CoMinEnclosureByODAtLeastTwoSide = 30
            self._CoMinEnclosureByPO = 30
            self._CoMinEnclosureByPOAtLeastTwoSide = 10

            ##Created By junung for OPLayer rules
            self._CoMinSpace2OP = 200
            self._CoMinEnclosureByPO2 = 12  ##only in poly for resistor? Created by junung
            self._CoArrayMaxWidth = 1211  ## Added by jicho

        if DesignParameters._Technology == 'TSMC65nm':
            self._CoMinWidth = 90
            self._CoMinSpace = 110
            self._CoMinSpace2 = 140
            self._CoMinSpaceDifferentNet = 140
            self._CoMinSpaceFor3neighboring = 150
            self._CoMinEnclosureByOD = 30
            self._CoMinEnclosureByODAtLeastTwoSide = 30
            self._CoMinEnclosureByPO = 40
            self._CoMinEnclosureByPOAtLeastTwoSide = 40

        if DesignParameters._Technology == 'TSMC90nm':
            self._CoMinWidth = 120
            self._CoMinSpace = 140
            self._CoMinSpace2 = 160
            self._CoMinSpaceDifferentNet = 160
            self._CoMinSpaceFor3neighboring = 180
            self._CoMinEnclosureByOD = 40
            self._CoMinEnclosureByODAtLeastTwoSide = 40
            self._CoMinEnclosureByPO = 20
            self._CoMinEnclosureByPOAtLeastTwoSide = 50

        if DesignParameters._Technology == 'TSMC130nm':
            self._CoMinWidth = 160
            self._CoMinSpace = 180
            self._CoMinSpace2 = 200
            self._CoMinSpaceDifferentNet = 210
            self._CoMinSpaceFor3neighboring = 210
            self._CoMinEnclosureByOD = 90
            self._CoMinEnclosureByODAtLeastTwoSide = 90
            self._CoMinEnclosureByPO = 70
            self._CoMinEnclosureByPOAtLeastTwoSide = 120

        if DesignParameters._Technology == 'TSMC180nm':
            self._CoMinWidth = 220
            self._CoMinSpace = 250
            self._CoMinSpace2 = 280
            self._CoMinSpaceDifferentNet = 280
            self._CoMinSpaceFor3neighboring = 300
            self._CoMinEnclosureByOD = 120
            self._CoMinEnclosureByODAtLeastTwoSide = 120
            self._CoMinEnclosureByPO = 100
            self._CoMinEnclosureByPOAtLeastTwoSide = 100

    def DRCCOMinSpace(self, NumOfCOX=None, NumOfCOY=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if NumOfCOX == None and NumOfCOY == None:
                return self._CoMinSpace
            elif (2 < NumOfCOY and 2 <= NumOfCOX) or (2 <= NumOfCOY and 2 < NumOfCOX):
                return self._CoMinSpace2
            else:
                return self._CoMinSpace

        if DesignParameters._Technology == 'SS28nm':
            if NumOfCOX == None and NumOfCOY == None:
                return self._CoMinSpace
            elif (2 < NumOfCOY and 2 <= NumOfCOX) or (2 <= NumOfCOY and 2 < NumOfCOX):
                return self._CoMinSpace2
            else:
                return self._CoMinSpace

        if DesignParameters._Technology == 'TSMC65nm':
            if NumOfCOX == None and NumOfCOY == None:
                return self._CoMinSpace
            elif (2 < NumOfCOY and 2 <= NumOfCOX) or (2 <= NumOfCOY and 2 < NumOfCOX):
                return self._CoMinSpace2
            else:
                return self._CoMinSpace

        if DesignParameters._Technology == 'TSMC90nm':
            if NumOfCOX == None and NumOfCOY == None:
                return self._CoMinSpace
            elif (2 < NumOfCOY and 2 <= NumOfCOX) or (2 <= NumOfCOY and 2 < NumOfCOX):
                return self._CoMinSpace2
            else:
                return self._CoMinSpace

        if DesignParameters._Technology == 'TSMC130nm':
            if NumOfCOX == None and NumOfCOY == None:
                return self._CoMinSpace
            elif (4 <= NumOfCOY and 4 <= NumOfCOX):
                # elif (3<= NumOfCOY and 3<=NumOfCOX):
                return self._CoMinSpace2
            else:
                return self._CoMinSpace
        if DesignParameters._Technology == 'TSMC180nm':
            if NumOfCOX == None and NumOfCOY == None:
                return self._CoMinSpace
            elif (4 <= NumOfCOY and 4 <= NumOfCOX):
                # elif (3<= NumOfCOY and 3<=NumOfCOX):
                return self._CoMinSpace2
            else:
                return self._CoMinSpace

    def DRCCOFillAtOD2Met1(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        if DesignParameters._Technology == 'TSMC45nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'SS28nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'TSMC65nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC90nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC130nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (4 <= _NumberOfCOX and 4 <= _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC180nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (4 <= _NumberOfCOX and 4 <= _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByODAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

    def DRCCOFillAtPoly2Met1(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        if DesignParameters._Technology == 'TSMC45nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'SS28nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                   self.DRCCOMinSpace(NumOfCOX=None,
                                                      NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                   self.DRCCOMinSpace(NumOfCOX=None,
                                                      NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'TSMC65nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC90nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC130nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (4 <= _NumberOfCOX and 4 <= _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC180nm':
            _NumberOfCOX = int(XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=None,
                                                                                                        NumOfCOY=None)) / (
                                       self.DRCCOMinSpace(NumOfCOX=None,
                                                          NumOfCOY=None) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            if (4 <= _NumberOfCOX and 4 <= _NumberOfCOY):
                _NumberOfCOX = int(
                    XWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                           self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(
                    YWidth - 2 * self._CoMinEnclosureByPOAtLeastTwoSide + self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                                                             NumOfCOY=YWidth)) / (
                                       self.DRCCOMinSpace(NumOfCOX=XWidth,
                                                              NumOfCOY=YWidth) + self._CoMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)


class DRCMETAL1:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._Metal1MinWidth = 70
            self._Metal1MinSpace = 70
            self._Metal1MinSpace2 = 80
            self._Metal1MinSpace21 = 120
            self._Metal1MinSpace22 = 140
            self._Metal1MinSpace23 = 210
            self._Metal1MinSpace3 = 500
            self._Metal1MinSpaceAtCorner = 80
            # TSMC45nm DRC rule metal1minEnclosureCO & metal1minEnclosureCO2 are valid in both below cases.
            # self._Metal1MinEnclosureCO=0
            # self._Metal1MinEnclosureCO2=30
            self._Metal1MinEnclosureCO = 5
            self._Metal1MinEnclosureCO2 = 30
            self._Metal1MinEnclosureVia1 = 0
            self._Metal1MinEnclosureVia12 = 30
            self._Metal1MinArea = 21500

        if DesignParameters._Technology == 'SS28nm':
            self._Metal1MinWidth = 50  # A
            self._Metal1MinSpace = 50  # D
            self._Metal1MinSpacetoGate = 20
            self._Metal1MinSpace2 = 66  # E (by JiCho)
            self._Metal1MinSpace21 = 82  # E1k
            self._Metal1MinSpace22 = 74  # G
            self._Metal1MinSpace3 = 140  # F

            self._Metal1MinSpaceAtCorner = 60  # S1/S2

            self._Metal1MinEnclosureCO = 5  # I
            self._Metal1MinEnclosureCO2 = 21  # J
            self._Metal1MinEnclosureCO3 = 12  ##FOR PRES, By junung
            self._Metal1MinEnclosureVia1 = 0
            self._Metal1MinEnclosureVia12 = 32
            self._Metal1MinArea = 10000
            self._Metal1MinEnclosureArea = 48000  # ADDED!(by JiCho)

        if DesignParameters._Technology == 'TSMC65nm':
            self._Metal1MinWidth = 90
            self._Metal1MinSpace = 90
            self._Metal1MinSpace2 = 110
            self._Metal1MinSpace21 = 160
            self._Metal1MinSpace3 = 500
            self._Metal1MinSpace4 = 1500

            self._Metal1MinSpaceAtCorner = 110

            self._Metal1MinEnclosureCO = 0
            self._Metal1MinEnclosureCO2 = 40
            self._Metal1MinEnclosureVia1 = 0
            self._Metal1MinEnclosureVia12 = 40
            self._Metal1MinArea = 42000

        if DesignParameters._Technology == 'TSMC90nm':
            self._Metal1MinWidth = 120
            self._Metal1MinSpace = 120

            self._Metal1MinSpace2 = 170
            self._Metal1MinSpace3 = 500
            self._Metal1MinSpace4 = 1500

            self._Metal1MinSpaceAtCorner = None

            self._Metal1MinEnclosureCO = 0
            self._Metal1MinEnclosureCO2 = 50
            self._Metal1MinEnclosureVia1 = 5
            self._Metal1MinEnclosureVia12 = 50
            self._Metal1MinArea = 58000
        if DesignParameters._Technology == 'TSMC130nm':
            self._Metal1MinWidth = 160
            self._Metal1MinSpace = 180
            self._Metal1MinSpace2 = 220
            self._Metal1MinSpace3 = 600

            self._Metal1MinSpaceAtCorner = None

            self._Metal1MinEnclosureCO = 0
            self._Metal1MinEnclosureCO2 = 50
            self._Metal1MinEnclosureVia1 = 10
            self._Metal1MinEnclosureVia12 = 50
            self._Metal1MinArea = 122000
        if DesignParameters._Technology == 'TSMC180nm':
            self._Metal1MinWidth = 230
            self._Metal1MinSpace = 230
            self._Metal1MinSpace2 = 600

            self._Metal1MinSpaceAtCorner = None

            self._Metal1MinEnclosureCO = 5
            self._Metal1MinEnclosureCO2 = 60
            self._Metal1MinEnclosureVia1 = 5
            self._Metal1MinEnclosureVia12 = 60

            self._Metal1MinArea = 202000

    def DRCMETAL1MinSpace(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if _Width == None and _ParallelLength == None:
                return self._Metal1MinSpace
            elif 170 < _Width and 270 < _ParallelLength:
                if 240 < _Width and 270 < _ParallelLength:
                    if 310 < _Width and 400 < _ParallelLength:
                        if 620 < _Width and 620 < _ParallelLength:
                            if 1500 < _Width and 1500 < _ParallelLength:
                                return self._Metal1MinSpace3
                            else:
                                return self._Metal1MinSpace23
                        else:
                            return self._Metal1MinSpace22
                    else:
                        return self._Metal1MinSpace21
                else:
                    return self._Metal1MinSpace2
            else:
                return self._Metal1MinSpace

        if DesignParameters._Technology == 'SS28nm':
            if _Width == None and _ParallelLength == None:
                return self._Metal1MinSpace
            elif 72 < _Width and 104 < _ParallelLength:  # a
                if 156 < _Width and 104 < _ParallelLength:  # b
                    if 208 < _Width and 104 < _ParallelLength:  # c
                        if 208 < _Width and 300 < _ParallelLength:
                            return self._Metal1MinSpace3  # 140
                        else:
                            return self._Metal1MinSpace22  # c 74
                    else:
                        return self._Metal1MinSpace21  # b 82
                else:
                    return self._Metal1MinSpace2  # a 65
            else:
                return self._Metal1MinSpace  # 50

        if DesignParameters._Technology == 'TSMC65nm':
            if _Width == None and _ParallelLength == None:
                return self._Metal1MinSpace
            elif 200 < _Width and 380 < _ParallelLength:
                if 420 < _Width and 420 < _ParallelLength:
                    if 1500 < _Width and 1500 < _ParallelLength:
                        if 4500 < _Width and 4500 < _ParallelLength:
                            return self._Metal1MinSpace4
                        else:
                            return self._Metal1MinSpace3
                    else:
                        return self._Metal1MinSpace21
                else:
                    return self._Metal1MinSpace2
            else:
                return self._Metal1MinSpace

        if DesignParameters._Technology == 'TSMC90nm':
            if _Width == None and _ParallelLength == None:
                return self._Metal1MinSpace
            elif 300 < _Width and 520 < _ParallelLength:
                if 1500 < _Width and 1500 < _ParallelLength:
                    if 4500 < _Width and 4500 < _ParallelLength:
                        return self._Metal1MinSpace4
                    else:
                        return self._Metal1MinSpace3
                else:
                    return self._Metal1MinSpace2
            else:
                return self._Metal1MinSpace

        if DesignParameters._Technology == 'TSMC130nm':
            if _Width == None and _ParallelLength == None:
                return self._Metal1MinSpace
            elif 300 < _Width and 1000 < _ParallelLength:
                if _Width > 10000 and _ParallelLength > 10000:
                    return self._Metal1MinSpace3
                else:
                    return self._Metal1MinSpace2
            else:
                return self._Metal1MinSpace
        if DesignParameters._Technology == 'TSMC180nm':
            if _Width > 10000 and _ParallelLength > 10000:
                return self._Metal1MinSpace2
            else:
                return self._Metal1MinSpace

    def DRCMETAL1MinSpaceAtCorner(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'TSMC45nm':
            return self._Metal1MinSpaceAtCorner
        if DesignParameters._Technology == 'SS28nm':
            return self._Metal1MinSpaceAtCorner
        if DesignParameters._Technology == 'TSMC65nm':
            return self._Metal1MinSpaceAtCorner
        if DesignParameters._Technology == 'TSMC90nm':
            return self.DRCMETAL1MinSpace(_Width=_Width, _ParallelLength=_ParallelLength)
        if DesignParameters._Technology == 'TSMC130nm':
            return self.DRCMETAL1MinSpace(_Width=_Width, _ParallelLength=_ParallelLength)
        if DesignParameters._Technology == 'TSMC180nm':
            return self.DRCMETAL1MinSpace(_Width=_Width, _ParallelLength=_ParallelLength)


class DRCNW:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._NwMinWidth = 340
            self._NwMinSpace = 340
            self._NwMinEnclosurePactive = 80
            self._NwMinEnclosurePactive2 = 80
            self._NwMinSpacetoNactive = 80

        if DesignParameters._Technology == 'SS28nm':
            self._NwMinWidth = 260  # A
            self._NwMinSpace = 260  # C
            self._NwMinEnclosurePactive = 56  # H
            self._NwMinEnclosurePactive2 = 112  # GR260a
            self._NwMinSpacetoNactive = 56  #
            self._NwMinSpacetoRX = 60
            self._NwMinSpacetoSLVT = 170  # ADDED! (by JiCho)
            self._NwMinArea = 500000

        if DesignParameters._Technology == 'TSMC65nm':
            self._NwMinWidth = 470
            self._NwMinSpace = 470
            self._NwMinEnclosurePactive = 160
            self._NwMinEnclosurePactive2 = 160
            self._NwMinSpacetoNactive = 160
            self._NwMinArea = 640000

        if DesignParameters._Technology == 'TSMC90nm':
            self._NwMinWidth = 620
            self._NwMinSpace = 620
            self._NwMinEnclosurePactive = 220
            self._NwMinEnclosurePactive2 = 220
            self._NwMinSpacetoNactive = 220
        if DesignParameters._Technology == 'TSMC130nm':
            self._NwMinWidth = 620
            self._NwMinSpace = 620
            self._NwMinEnclosurePactive = 310
            self._NwMinEnclosurePactive2 = 310
            self._NwMinSpacetoNactive = 310
        if DesignParameters._Technology == 'TSMC180nm':
            self._NwMinWidth = 860
            self._NwMinSpace = 1400
            self._NwMinEnclosurePactive = 430
            self._NwMinEnclosurePactive2 = 430
            self._NwMinSpacetoNactive = 430


class DRCVIAx:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._VIAxMinWidth = 70
            self._VIAxMinSpace = 70
            self._VIAxMinSpace2 = 90
            self._VIAxMinSpaceDifferentNet = 110
            self._VIAxMinSpaceFor3neighboring = 98
            self._VIAxMinEnclosureByMetx = 0
            self._VIAxMinEnclosureByMetxTwoOppositeSide = 30

        if DesignParameters._Technology == 'SS28nm':
            self._VIAxMinWidth = 50  # A
            self._VIAxMinSpace = 80  # B
            self._VIAxMinSpace2 = 92  # C
            self._VIAxMinSpaceDifferentNet = 80  # B1
            self._VIAxMinSpaceFor3neighboring = 92  # C
            self._VIAxMinEnclosureByMetx = 0  # D
            self._VIAxMinEnclosureByMetxTwoOppositeSide = 32  # E

        if DesignParameters._Technology == 'TSMC65nm':
            self._VIAxMinWidth = 100
            self._VIAxMinSpace = 100
            self._VIAxMinSpace2 = 130
            self._VIAxMinSpaceDifferentNet = 130
            self._VIAxMinSpaceFor3neighboring = 140
            self._VIAxMinEnclosureByMetx = 0
            self._VIAxMinEnclosureByMetxTwoOppositeSide = 40

        if DesignParameters._Technology == 'TSMC90nm':
            self._VIAxMinWidth = 130
            self._VIAxMinSpace = 150
            self._VIAxMinSpace2 = 170
            self._VIAxMinSpaceDifferentNet = 170
            self._VIAxMinSpaceFor3neighboring = 190
            self._VIAxMinEnclosureByMetx = 5
            self._VIAxMinEnclosureByMetxTwoOppositeSide = 50
        if DesignParameters._Technology == 'TSMC130nm':
            self._VIAxMinWidth = 190
            self._VIAxMinSpace = 220
            self._VIAxMinSpace2 = 290
            self._VIAxMinSpaceDifferentNet = 290
            self._VIAxMinSpaceFor3neighboring = 310
            self._VIAxMinEnclosureByMetx = 5
            self._VIAxMinEnclosureByMetxTwoOppositeSide = 50
        if DesignParameters._Technology == 'TSMC180nm':
            self._VIAxMinWidth = 260
            self._VIAxMinSpace = 260
            self._VIAxMinSpaceDifferentNet = 260
            self._VIAxMinSpaceFor3neighboring = 260
            self._VIAxMinEnclosureByMetx = 10
            self._VIAxMinEnclosureByMetxTwoOppositeSide = 60

    def DRCVIAxMinSpace(self, NumOfVIAxX=None, NumOfVIAxY=None):
        if DesignParameters._Technology == 'TSMC45nm':

            if NumOfVIAxX == None and NumOfVIAxY == None:
                return self._VIAxMinSpace
            elif (2 < NumOfVIAxY and 2 <= NumOfVIAxX) or (2 <= NumOfVIAxY and 2 < NumOfVIAxX):
                return self._VIAxMinSpace2
            else:
                return self._VIAxMinSpace

        if DesignParameters._Technology == 'SS28nm':

            if NumOfVIAxX == None and NumOfVIAxY == None:
                return self._VIAxMinSpace
            elif (2 < NumOfVIAxY and 2 <= NumOfVIAxX) or (2 <= NumOfVIAxY and 2 < NumOfVIAxX):
                return self._VIAxMinSpace2
            else:
                return self._VIAxMinSpace

        if DesignParameters._Technology == 'TSMC65nm':

            if NumOfVIAxX == None and NumOfVIAxY == None:
                return self._VIAxMinSpace
            elif (2 < NumOfVIAxY and 2 <= NumOfVIAxX) or (2 <= NumOfVIAxY and 2 < NumOfVIAxX):
                return self._VIAxMinSpace2
            else:
                return self._VIAxMinSpace
        if DesignParameters._Technology == 'TSMC90nm':

            if NumOfVIAxX == None and NumOfVIAxY == None:
                return self._VIAxMinSpace
            elif (2 < NumOfVIAxY and 2 <= NumOfVIAxX) or (2 <= NumOfVIAxY and 2 < NumOfVIAxX):
                return self._VIAxMinSpace2
            else:
                return self._VIAxMinSpace
        if DesignParameters._Technology == 'TSMC130nm':

            if NumOfVIAxX == None and NumOfVIAxY == None:
                return self._VIAxMinSpace
            elif (3 <= NumOfVIAxY and 3 <= NumOfVIAxX):
                return self._VIAxMinSpace2
            else:
                return self._VIAxMinSpace
        if DesignParameters._Technology == 'TSMC180nm':
            return self._VIAxMinSpace

    def DRCVIAxFill(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        _tmpDRCMETAL1 = DRCMETAL1()
        _tmpDRCMETALx = DRCMETALx()
        if DesignParameters._Technology == 'TSMC45nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'SS28nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'TSMC65nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC90nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC130nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            if (3 <= _NumberOfCOX and 3 <= _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETAL1._Metal1MinEnclosureVia12,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                    NumOfVIAxX=XWidth, NumOfVIAxY=YWidth)) / (self.DRCVIAxMinSpace(NumOfVIAxX=XWidth,
                                                                                   NumOfVIAxY=YWidth) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC180nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETAL1._Metal1MinEnclosureVia12, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAxMinSpace(
                NumOfVIAxX=None, NumOfVIAxY=None)) / (self.DRCVIAxMinSpace(NumOfVIAxX=None,
                                                                           NumOfVIAxY=None) + self._VIAxMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        del _tmpDRCMETAL1
        del _tmpDRCMETALx


class DRCVIAy:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._VIAyMinWidth = 140
            self._VIAyMinSpace = 140
            self._VIAyMinSpace2 = 160
            self._VIAyMinSpaceDifferentNet = 160
            self._VIAyMinSpaceFor3neighboring = 175
            self._VIAyMinEnclosureByMetxOrMety = 0
            self._VIAyMinEnclosureByMetxOrMetyTwoOppositeSide = 45

        if DesignParameters._Technology == 'SS28nm':
            self._VIAyMinWidth = 50  # A
            self._VIAyMinSpace = 80  # B
            self._VIAyMinSpace2 = 80  # C
            self._VIAyMinSpaceDifferentNet = 80  # C
            self._VIAyMinSpaceFor3neighboring = 92
            self._VIAyMinEnclosureByMetxOrMety = 0
            self._VIAyMinEnclosureByMetxOrMetyTwoOppositeSide = 32  # D

        if DesignParameters._Technology == 'TSMC65nm':
            self._VIAyMinWidth = 200
            self._VIAyMinSpace = 200
            self._VIAyMinSpace2 = 250
            self._VIAyMinSpaceDifferentNet = 250
            self._VIAyMinSpaceFor3neighboring = 280
            self._VIAyMinEnclosureByMetxOrMety = 0
            self._VIAyMinEnclosureByMetxOrMetyTwoOppositeSide = 50

        if DesignParameters._Technology == 'TSMC90nm':
            self._VIAyMinWidth = 260
            self._VIAyMinSpace = 300
            self._VIAyMinSpace2 = 370
            self._VIAyMinSpaceDifferentNet = 370
            self._VIAyMinSpaceFor3neighboring = 390
            self._VIAyMinEnclosureByMetxOrMety = 10
            self._VIAyMinEnclosureByMetxOrMetyTwoOppositeSide = 50
        if DesignParameters._Technology == 'TSMC130nm':
            self._VIAyMinWidth = None
            self._VIAyMinSpace = None
            self._VIAyMinSpace2 = None
            self._VIAyMinSpaceDifferentNet = None
            self._VIAyMinSpaceFor3neighboring = None
            self._VIAyMinEnclosureByMetx = None
            self._VIAyMinEnclosureByMetxTwoOppositeSide = None
        if DesignParameters._Technology == 'TSMC180nm':
            self._VIAyMinWidth = None
            self._VIAyMinSpace = None
            self._VIAyMinSpaceDifferentNet = None
            self._VIAyMinSpaceFor3neighboring = None
            self._VIAyMinEnclosureByMetx = None
            self._VIAyMinEnclosureByMetxTwoOppositeSide = None

    def DRCVIAyMinSpace(self, NumOfVIAyX=None, NumOfVIAyY=None):
        if DesignParameters._Technology == 'TSMC45nm':

            if NumOfVIAyX == None and NumOfVIAyY == None:
                return self._VIAyMinSpace
            elif (2 < NumOfVIAyY and 2 <= NumOfVIAyX) or (2 <= NumOfVIAyY and 2 < NumOfVIAyX):
                return self._VIAyMinSpace2
            else:
                return self._VIAyMinSpace

        if DesignParameters._Technology == 'SS28nm':

            if NumOfVIAyX == None and NumOfVIAyY == None:
                return self._VIAyMinSpace
            elif (2 < NumOfVIAyY and 2 <= NumOfVIAyX) or (2 <= NumOfVIAyY and 2 < NumOfVIAyX):
                return self._VIAyMinSpace2
            else:
                return self._VIAyMinSpace

        if DesignParameters._Technology == 'TSMC65nm':

            if NumOfVIAyX == None and NumOfVIAyY == None:
                return self._VIAyMinSpace
            elif (2 < NumOfVIAyY and 2 <= NumOfVIAyX) or (2 <= NumOfVIAyY and 2 < NumOfVIAyX):
                return self._VIAyMinSpace2
            else:
                return self._VIAyMinSpace
        if DesignParameters._Technology == 'TSMC90nm':

            if NumOfVIAyX == None and NumOfVIAyY == None:
                return self._VIAyMinSpace
            elif (2 < NumOfVIAyY and 2 <= NumOfVIAyX) or (2 <= NumOfVIAyY and 2 < NumOfVIAyX):
                return self._VIAyMinSpace2
            else:
                return self._VIAyMinSpace
        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None

    def DRCVIAyFill(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        _tmpDRCMETALy = DRCMETALy()
        _tmpDRCMETALx = DRCMETALx()
        if DesignParameters._Technology == 'TSMC45nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                NumOfVIAyX=None, NumOfVIAyY=None)) / (self.DRCVIAyMinSpace(NumOfVIAyX=None,
                                                                           NumOfVIAyY=None) + self._VIAyMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                NumOfVIAyX=None, NumOfVIAyY=None)) / (self.DRCVIAyMinSpace(NumOfVIAyX=None,
                                                                           NumOfVIAyY=None) + self._VIAyMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETALy._MetalyMinEnclosureCO2,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                    NumOfVIAyX=XWidth, NumOfVIAyY=YWidth)) / (self.DRCVIAyMinSpace(NumOfVIAyX=XWidth,
                                                                                   NumOfVIAyY=YWidth) + self._VIAyMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETALy._MetalyMinEnclosureCO2,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                    NumOfVIAyX=XWidth, NumOfVIAyY=YWidth)) / (self.DRCVIAyMinSpace(NumOfVIAyX=XWidth,
                                                                                   NumOfVIAyY=YWidth) + self._VIAyMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'SS28nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                NumOfVIAyX=None, NumOfVIAyY=None)) / (self.DRCVIAyMinSpace(NumOfVIAyX=None,
                                                                           NumOfVIAyY=None) + self._VIAyMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                NumOfVIAyX=None, NumOfVIAyY=None)) / (self.DRCVIAyMinSpace(NumOfVIAyX=None,
                                                                           NumOfVIAyY=None) + self._VIAyMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETALy._MetalyMinEnclosureCO2,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                    NumOfVIAyX=XWidth, NumOfVIAyY=YWidth)) / (self.DRCVIAyMinSpace(NumOfVIAyX=XWidth,
                                                                                   NumOfVIAyY=YWidth) + self._VIAyMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETALy._MetalyMinEnclosureCO2,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                    NumOfVIAyX=XWidth, NumOfVIAyY=YWidth)) / (self.DRCVIAyMinSpace(NumOfVIAyX=XWidth,
                                                                                   NumOfVIAyY=YWidth) + self._VIAyMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'TSMC65nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                NumOfVIAyX=None, NumOfVIAyY=None)) / (self.DRCVIAyMinSpace(NumOfVIAyX=None,
                                                                           NumOfVIAyY=None) + self._VIAyMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                NumOfVIAyX=None, NumOfVIAyY=None)) / (self.DRCVIAyMinSpace(NumOfVIAyX=None,
                                                                           NumOfVIAyY=None) + self._VIAyMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETALy._MetalyMinEnclosureCO2,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                    NumOfVIAyX=XWidth, NumOfVIAyY=YWidth)) / (self.DRCVIAyMinSpace(NumOfVIAyX=XWidth,
                                                                                   NumOfVIAyY=YWidth) + self._VIAyMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETALy._MetalyMinEnclosureCO2,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                    NumOfVIAyX=XWidth, NumOfVIAyY=YWidth)) / (self.DRCVIAyMinSpace(NumOfVIAyX=XWidth,
                                                                                   NumOfVIAyY=YWidth) + self._VIAyMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC90nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                NumOfVIAyX=None, NumOfVIAyY=None)) / (self.DRCVIAyMinSpace(NumOfVIAyX=None,
                                                                           NumOfVIAyY=None) + self._VIAyMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                NumOfVIAyX=None, NumOfVIAyY=None)) / (self.DRCVIAyMinSpace(NumOfVIAyX=None,
                                                                           NumOfVIAyY=None) + self._VIAyMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max([_tmpDRCMETALy._MetalyMinEnclosureCO2,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                    NumOfVIAyX=XWidth, NumOfVIAyY=YWidth)) / (self.DRCVIAyMinSpace(NumOfVIAyX=XWidth,
                                                                                   NumOfVIAyY=YWidth) + self._VIAyMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max([_tmpDRCMETALy._MetalyMinEnclosureCO2,
                                                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAyMinSpace(
                    NumOfVIAyX=XWidth, NumOfVIAyY=YWidth)) / (self.DRCVIAyMinSpace(NumOfVIAyX=XWidth,
                                                                                   NumOfVIAyY=YWidth) + self._VIAyMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None
        del _tmpDRCMETALy
        del _tmpDRCMETALx


class DRCVIAz:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._VIAzMinWidth = 360
            self._VIAzMinSpace = 340
            self._VIAzMinSpace2 = 540
            self._VIAzMinSpaceFor3neighboring = 560
            self._VIAzMinEnclosureByMetxOrMety = 20
            self._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide = 80

        if DesignParameters._Technology == 'SS28nm':
            self._VIAzMinWidth = 360
            self._VIAzMinSpace = 440
            self._VIAzMinSpace2 = 440
            self._VIAzMinSpaceFor3neighboring = 440
            self._VIAzMinEnclosureByMetxOrMety = 20
            self._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide = 80

        if DesignParameters._Technology == 'TSMC65nm':
            self._VIAzMinWidth = 360
            self._VIAzMinSpace = 340
            self._VIAzMinSpace2 = 540
            self._VIAzMinSpaceFor3neighboring = 560
            self._VIAzMinEnclosureByMetxOrMety = 20
            self._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide = 80
        if DesignParameters._Technology == 'TSMC90nm':
            self._VIAzMinWidth = None
            self._VIAzMinSpace = None
            self._VIAzMinSpace2 = None
            self._VIAzMinSpaceFor3neighboring = None
            self._VIAzMinEnclosureByMetxOrMety = None
            self._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide = None
        if DesignParameters._Technology == 'TSMC130nm':
            self._VIAzMinWidth = None
            self._VIAzMinSpace = None
            self._VIAzMinSpace2 = None
            self._VIAzMinSpaceFor3neighboring = None
            self._VIAzMinEnclosureByMetx = None
            self._VIAzMinEnclosureByMetxTwoOppositeSide = None
        if DesignParameters._Technology == 'TSMC180nm':
            self._VIAzMinWidth = None
            self._VIAzMinSpace = None
            self._VIAzMinSpace2 = None
            self._VIAzMinSpaceFor3neighboring = None
            self._VIAzMinEnclosureByMetx = None
            self._VIAzMinEnclosureByMetxTwoOppositeSide = None

    def DRCVIAzMinSpace(self, NumOfVIAzX=None, NumOfVIAzY=None):
        if DesignParameters._Technology == 'TSMC45nm':

            if NumOfVIAzX == None and NumOfVIAzY == None:
                return self._VIAzMinSpace
            elif (2 <= NumOfVIAzY and 2 <= NumOfVIAzX):
                return self._VIAzMinSpace2
            else:
                return self._VIAzMinSpace

        if DesignParameters._Technology == 'SS28nm':

            if NumOfVIAzX == None and NumOfVIAzY == None:
                return self._VIAzMinSpace
            elif (2 <= NumOfVIAzY and 2 <= NumOfVIAzX):
                return self._VIAzMinSpace2
            else:
                return self._VIAzMinSpace

        if DesignParameters._Technology == 'TSMC65nm':

            if NumOfVIAzX == None and NumOfVIAzY == None:
                return self._VIAzMinSpace
            elif (2 <= NumOfVIAzY and 2 <= NumOfVIAzX):
                return self._VIAzMinSpace2
            else:
                return self._VIAzMinSpace
        if DesignParameters._Technology == 'TSMC90nm':
            return None
        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None

    def DRCVIAzFill(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        _tmpDRCMETALz = DRCMETALz()
        _tmpDRCMETALy = DRCMETALy()
        _tmpDRCMETALx = DRCMETALx()
        if DesignParameters._Technology == 'TSMC45nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None)) / (
                                       self.DRCVIAzMinSpace(NumOfVIAzX=None,
                                                            NumOfVIAzY=None) + self._VIAzMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None)) / (
                                       self.DRCVIAzMinSpace(NumOfVIAzX=None,
                                                            NumOfVIAzY=None) + self._VIAzMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                                   NumOfVIAzY=YWidth)) / (
                                           self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                NumOfVIAzY=YWidth) + self._VIAzMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                                   NumOfVIAzY=YWidth)) / (
                                           self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                NumOfVIAzY=YWidth) + self._VIAzMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == '028m':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None)) / (
                                       self.DRCVIAzMinSpace(NumOfVIAzX=None,
                                                            NumOfVIAzY=None) + self._VIAzMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None)) / (
                                       self.DRCVIAzMinSpace(NumOfVIAzX=None,
                                                            NumOfVIAzY=None) + self._VIAzMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                                   NumOfVIAzY=YWidth)) / (
                                           self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                NumOfVIAzY=YWidth) + self._VIAzMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                                   NumOfVIAzY=YWidth)) / (
                                           self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                NumOfVIAzY=YWidth) + self._VIAzMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'TSMC65nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None)) / (
                                       self.DRCVIAzMinSpace(NumOfVIAzX=None,
                                                            NumOfVIAzY=None) + self._VIAzMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None)) / (
                                       self.DRCVIAzMinSpace(NumOfVIAzX=None,
                                                            NumOfVIAzY=None) + self._VIAzMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                                   NumOfVIAzY=YWidth)) / (
                                           self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                NumOfVIAzY=YWidth) + self._VIAzMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                                   NumOfVIAzY=YWidth)) / (
                                           self.DRCVIAzMinSpace(NumOfVIAzX=XWidth,
                                                                NumOfVIAzY=YWidth) + self._VIAzMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC90nm':
            return None
        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None
        del _tmpDRCMETALz
        del _tmpDRCMETALy
        del _tmpDRCMETALx


class DRCVIAr:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._VIArMinWidth = 460
            self._VIArMinSpace = 440
            self._VIArMinSpace20 = 660
            self._VIArMinSpace21 = 540
            self._VIArMinSpaceFor3neighboring = 660
            self._VIArMinEnclosureByMetxOrMety = 20
            self._VIArMinEnclosureByMetxOrMetyTwoOppositeSide = 80

        if DesignParameters._Technology == 'SS28nm':
            self._VIArMinWidth = 3000
            self._VIArMinSpace = 2000
            self._VIArMinSpace20 = 2000
            self._VIArMinSpace21 = 2000
            self._VIArMinSpaceFor3neighboring = 2000
            self._VIArMinEnclosureByMetxOrMety = 1000
            self._VIArMinEnclosureByMetxOrMetyTwoOppositeSide = 1000

        if DesignParameters._Technology == 'TSMC65nm':
            self._VIArMinWidth = 460
            self._VIArMinSpace = 440
            self._VIArMinSpace20 = 660
            self._VIArMinSpace21 = 540
            self._VIArMinSpaceFor3neighboring = 660
            self._VIArMinEnclosureByMetxOrMety = 20
            self._VIArMinEnclosureByMetxOrMetyTwoOppositeSide = 80
        if DesignParameters._Technology == 'TSMC90nm':
            self._VIArMinWidth = None
            self._VIArMinSpace = None
            self._VIArMinSpace2 = None
            self._VIArMinEnclosureByMetxOrMety = None
            self._VIArMinEnclosureByMetxOrMetyTwoOppositeSide = None
        if DesignParameters._Technology == 'TSMC130nm':
            self._VIArMinWidth = None
            self._VIArMinSpace = None
            self._VIArMinSpace2 = None
            self._VIArMinEnclosureByMetx = None
            self._VIArMinEnclosureByMetxTwoOppositeSide = None
        if DesignParameters._Technology == 'TSMC180nm':
            self._VIArMinWidth = None
            self._VIArMinSpace = None
            self._VIArMinEnclosureByMetx = None
            self._VIArMinEnclosureByMetxTwoOppositeSide = None

    def DRCVIArMinSpace(self, NumOfVIArX=None, NumOfVIArY=None):
        if DesignParameters._Technology == 'TSMC45nm':

            if NumOfVIArX == None and NumOfVIArY == None:
                return self._VIArMinSpace
            elif (2 <= NumOfVIArY and 2 <= NumOfVIArX):
                return max([self._VIArMinSpace20, self._VIArMinSpace21])
            else:
                return self._VIArMinSpace

        if DesignParameters._Technology == 'SS28nm':

            if NumOfVIArX == None and NumOfVIArY == None:
                return self._VIArMinSpace
            elif (2 <= NumOfVIArY and 2 <= NumOfVIArX):
                return max([self._VIArMinSpace20, self._VIArMinSpace21])
            else:
                return self._VIArMinSpace

        if DesignParameters._Technology == 'TSMC65nm':

            if NumOfVIArX == None and NumOfVIArY == None:
                return self._VIArMinSpace
            elif (2 <= NumOfVIArY and 2 <= NumOfVIArX):
                return max([self._VIArMinSpace20, self._VIArMinSpace21])
            else:
                return self._VIArMinSpace
        if DesignParameters._Technology == 'TSMC90nm':
            return None
        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None

    def DRCVIArFill(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        _tmpDRCMETALr = DRCMETALr()
        _tmpDRCMETALz = DRCMETALz()
        _tmpDRCMETALy = DRCMETALy()
        _tmpDRCMETALx = DRCMETALx()
        if DesignParameters._Technology == 'TSMC45nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALr._MetalrMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(
                NumOfVIArX=None, NumOfVIArY=None)) / (self.DRCVIArMinSpace(NumOfVIArX=None,
                                                                           NumOfVIArY=None) + self._VIArMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALr._MetalrMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(
                NumOfVIArX=None, NumOfVIArY=None)) / (self.DRCVIArMinSpace(NumOfVIArX=None,
                                                                           NumOfVIArY=None) + self._VIArMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALr._MetalrMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                                   NumOfVIArY=YWidth)) / (
                                           self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                NumOfVIArY=YWidth) + self._VIArMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALr._MetalrMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                                   NumOfVIArY=YWidth)) / (
                                           self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                NumOfVIArY=YWidth) + self._VIArMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'SS28nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALr._MetalrMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(
                NumOfVIArX=None, NumOfVIArY=None)) / (self.DRCVIArMinSpace(NumOfVIArX=None,
                                                                           NumOfVIArY=None) + self._VIArMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALr._MetalrMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(
                NumOfVIArX=None, NumOfVIArY=None)) / (self.DRCVIArMinSpace(NumOfVIArX=None,
                                                                           NumOfVIArY=None) + self._VIArMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALr._MetalrMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                                   NumOfVIArY=YWidth)) / (
                                           self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                NumOfVIArY=YWidth) + self._VIArMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALr._MetalrMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                                   NumOfVIArY=YWidth)) / (
                                           self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                NumOfVIArY=YWidth) + self._VIArMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)

        if DesignParameters._Technology == 'TSMC65nm':
            _NumberOfCOX = int(XWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALr._MetalrMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(
                NumOfVIArX=None, NumOfVIArY=None)) / (self.DRCVIArMinSpace(NumOfVIArX=None,
                                                                           NumOfVIArY=None) + self._VIArMinWidth) if NumOfCOX == None else NumOfCOX
            _NumberOfCOY = int(YWidth - 2 * max(
                [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                 _tmpDRCMETALr._MetalrMinEnclosureCO2, _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(
                NumOfVIArX=None, NumOfVIArY=None)) / (self.DRCVIArMinSpace(NumOfVIArX=None,
                                                                           NumOfVIArY=None) + self._VIArMinWidth) if NumOfCOY == None else NumOfCOY
            if (2 < _NumberOfCOX and 2 <= _NumberOfCOY) or (2 <= _NumberOfCOX and 2 < _NumberOfCOY):
                _NumberOfCOX = int(XWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALr._MetalrMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                                   NumOfVIArY=YWidth)) / (
                                           self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                NumOfVIArY=YWidth) + self._VIArMinWidth) if NumOfCOX == None else NumOfCOX
                _NumberOfCOY = int(YWidth - 2 * max(
                    [_tmpDRCMETALy._MetalyMinEnclosureCO2, _tmpDRCMETALz._MetalzMinEnclosureCO2,
                     _tmpDRCMETALr._MetalrMinEnclosureCO2,
                     _tmpDRCMETALx._MetalxMinEnclosureCO2]) + self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                                   NumOfVIArY=YWidth)) / (
                                           self.DRCVIArMinSpace(NumOfVIArX=XWidth,
                                                                NumOfVIArY=YWidth) + self._VIArMinWidth) if NumOfCOY == None else NumOfCOY
            return (_NumberOfCOX, _NumberOfCOY)
        if DesignParameters._Technology == 'TSMC90nm':
            return None
        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None
        del _tmpDRCMETALr
        del _tmpDRCMETALz
        del _tmpDRCMETALy
        del _tmpDRCMETALx


class DRCMETALx:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._MetalxMinWidth = 70
            self._MetalxMinSpace = 70
            self._MetalxMinSpace2 = 100
            self._MetalxMinSpace21 = 120
            self._MetalxMinSpace22 = 150
            self._MetalxMinSpace23 = 210
            self._MetalxMinSpace3 = 500

            self._MetalxMinSpaceAtCorner = 100

            self._MetalxMinEnclosureCO = 0
            self._MetalxMinEnclosureCO2 = 30
            self._MetalxMinArea = 27000

        if DesignParameters._Technology == 'SS28nm':
            self._MetalxMinWidth = 50  # A
            self._MetalxMinSpace = 50  # D
            self._MetalxMinSpace2 = 65  # E  (M1 with span > 0.072) minimum space for run length > 0.104, >= 0.065
            self._MetalxMinSpace21 = 66  ## M3 minimum space to (M3 with width > 0.156) for run length >0 , > = 0.066, junung
            self._MetalxMinSpace3 = 82  # E1
            self._MetalxMinSpace4 = 74  # F
            self._MetalxMinSpace41 = 95  ## Mx minimum space to (Mx with width > 0.208), for run length > 0.3, >= 0.095, junung
            self._MetalxMinSpace5 = 140  # G	1	1					Update

            self._MetalxMinSpace6 = 165  # M4 minimum space to (M4 with width > 0.700), for run length > 0.700, >= 0.165  , junung
            self._MetalxMinSpace7 = 173  # (M4 with width > 0.700) minimum space to (M4 with width > 0.072), for run length > 0.700, >= 0.173 , junung
            self._MetalxMinSpace8 = 181  # (M4 with width > 0.700) minimum space to (M4 with width > 0.156), for run length > 0.700, >= 0.181 , junung
            self._MetalxMinSpace9 = 210  # (M5 with width > 0.208) minimum space to (M5 with width > 0.700), for run length > 0.700, >= 0.21 , junung
            self._MetalxMinSpace10 = 280  # (M6 with width > 0.700) minimum space to (M6 with width > 0.700), >= 0.28, junung
            self._MetalxMinSpace11 = 500  # (M6 with width > 1.500) minimum space to (M6 with width > 0.700), >= 0.5, junung

            self._MetalxMinSpaceAtCorner = 60  # S1/S2

            self._MetalxMinEnclosureCO = 0  # I
            self._MetalxMinEnclosureCO2 = 32  # J
            self._MetalxMinArea = 11000  # K

            self._MetalxMaxWidth = 4500  # M7 not over MOB maximum width <= 4.5 , junung

        if DesignParameters._Technology == 'TSMC65nm':
            self._MetalxMinWidth = 100
            self._MetalxMinSpace = 100
            self._MetalxMinSpace2 = 120
            self._MetalxMinSpace21 = 160
            self._MetalxMinSpace3 = 500
            self._MetalxMinSpace4 = 1500

            self._MetalxMinSpaceAtCorner = 110

            self._MetalxMinEnclosureCO = 0
            self._MetalxMinEnclosureCO2 = 40
            self._MetalxMinArea = 52000
        if DesignParameters._Technology == 'TSMC90nm':
            self._MetalxMinWidth = 140
            self._MetalxMinSpace = 140
            self._MetalxMinSpace2 = 190
            self._MetalxMinSpace3 = 500
            self._MetalxMinSpace4 = 1500

            self._MetalxMinSpaceAtCorner = None

            self._MetalxMinEnclosureCO = 5
            self._MetalxMinEnclosureCO2 = 50
            self._MetalxMinArea = 70000
        if DesignParameters._Technology == 'TSMC130nm':
            self._MetalxMinWidth = 200
            self._MetalxMinSpace = 210
            self._MetalxMinSpace2 = 240
            self._MetalxMinSpace3 = 600

            self._MetalxMinSpaceAtCorner = None

            self._MetalxMinEnclosureCO = 5
            self._MetalxMinEnclosureCO2 = 50
            self._MetalxMinArea = 144000

        if DesignParameters._Technology == 'TSMC180nm':
            self._MetalxMinWidth = 280
            self._MetalxMinSpace = 280
            self._MetalxMinSpace2 = 600
            self._MetalxMinSpaceWhenRunWidth200Length380 = 120
            self._MetalxMinSpaceWhenRunWidth1500Length1500 = 500
            self._MetalxMinSpaceWhenRunWidth4500Length4500 = 1500

            self._MetalxMinSpaceAtCorner = None

            self._MetalxMinEnclosureCO = 10
            self._MetalxMinEnclosureCO2 = 60
            self._MetalxMinArea = 202000

    def DRCMETALxMinSpace(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalxMinSpace
            elif 170 < _Width and 270 < _ParallelLength:
                if 240 < _Width and 270 < _ParallelLength:
                    if 310 < _Width and 400 < _ParallelLength:
                        if 620 < _Width and 620 < _ParallelLength:
                            if 1500 < _Width and 1500 < _ParallelLength:
                                return self._MetalxMinSpace3
                            else:
                                return self._MetalxMinSpace23
                        else:
                            return self._MetalxMinSpace22
                    else:
                        return self._MetalxMinSpace21
                else:
                    return self._MetalxMinSpace2
            else:
                return self._MetalxMinSpace

        if DesignParameters._Technology == 'SS28nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalxMinSpace
            elif 72 < _Width and 104 < _ParallelLength:
                if 156 < _Width and 104 < _ParallelLength:
                    if 208 < _Width and 104 < _ParallelLength:
                        if 208 < _Width and 300 < _ParallelLength:
                            return self._MetalxMinSpace5
                        else:
                            return self._MetalxMinSpace4
                    else:
                        return self._MetalxMinSpace3
                else:
                    return self._MetalxMinSpace2
            else:
                return self._MetalxMinSpace

        if DesignParameters._Technology == 'TSMC65nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalxMinSpace
            elif 200 < _Width and 380 < _ParallelLength:
                if 420 < _Width and 420 < _ParallelLength:
                    if 1500 < _Width and 1500 < _ParallelLength:
                        if 4500 < _Width and 4500 < _ParallelLength:
                            return self._MetalxMinSpace4
                        else:
                            return self._MetalxMinSpace3
                    else:
                        return self._MetalxMinSpace21
                else:
                    return self._MetalxMinSpace2
            else:
                return self._MetalxMinSpace
        if DesignParameters._Technology == 'TSMC90nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalxMinSpace
            elif 210 < _Width and 520 < _ParallelLength:
                if 1500 < _Width and 1500 < _ParallelLength:
                    if 4500 < _Width and 4500 < _ParallelLength:
                        return self._MetalxMinSpace4
                    else:
                        return self._MetalxMinSpace3
                else:
                    return self._MetalxMinSpace2
            else:
                return self._MetalxMinSpace

        if DesignParameters._Technology == 'TSMC130nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalxMinSpace
            elif 390 < _Width and 1000 < _ParallelLength:
                if 10000 < _Width and 10000 < _ParallelLength:
                    return self._MetalxMinSpace3
                else:
                    return self._MetalxMinSpace2
            else:
                return self._MetalxMinSpace
        if DesignParameters._Technology == 'TSMC180nm':
            if _Width > 10000 and _ParallelLength > 10000:
                return self._MetalxMinSpace2
            else:
                return self._MetalxMinSpace

    def DRCMETALxMinSpaceAtCorner(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'TSMC45nm':
            return self._MetalxMinSpaceAtCorner
        if DesignParameters._Technology == 'SS28nm':
            return self._MetalxMinSpaceAtCorner
        if DesignParameters._Technology == 'TSMC65nm':
            return self._MetalxMinSpaceAtCorner
        if DesignParameters._Technology == 'TSMC90nm':
            return self.DRCMETALxMinSpace(_Width=_Width, _ParallelLength=_ParallelLength)
        if DesignParameters._Technology == 'TSMC130nm':
            return self.DRCMETALxMinSpace(_Width=_Width, _ParallelLength=_ParallelLength)
        if DesignParameters._Technology == 'TSMC180nm':
            return self.DRCMETALxMinSpace(_Width=_Width, _ParallelLength=_ParallelLength)


class DRCMETALy:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._MetalyMinWidth = 140
            self._MetalyMaxWidth = 12000
            self._MetalyMinSpace = 140
            self._MetalyMinSpace2 = 190
            self._MetalyMinSpace3 = 500
            self._MetalyMinSpace4 = 1500

            self._MetalyMinEnclosureCO = 0
            self._MetalyMinEnclosureCO2 = 45
            self._MetalyMinArea = 70000

        if DesignParameters._Technology == 'SS28nm':
            self._MetalyMinWidth = 50
            self._MetalyMaxWidth = 10000
            self._MetalyMinSpace = 50
            self._MetalyMinSpace2 = 65
            self._MetalyMinSpace3 = 82
            self._MetalyMinSpace4 = 74
            self._MetalyMinSpace5 = 140

            self._MetalyMinEnclosureCO = 0
            self._MetalyMinEnclosureCO2 = 32
            self._MetalyMinArea = 11

        if DesignParameters._Technology == 'TSMC65nm':
            self._MetalyMinWidth = 200
            self._MetalyMaxWidth = 12000
            self._MetalyMinSpace = 200
            self._MetalyMinSpace2 = 240
            self._MetalyMinSpace3 = 500
            self._MetalyMinSpace4 = 1500

            self._MetalyMinEnclosureCO = 0
            self._MetalyMinEnclosureCO2 = 50
            self._MetalyMinArea = 144000
        if DesignParameters._Technology == 'TSMC90nm':
            self._MetalyMinWidth = 280
            self._MetalyMaxWidth = 12000
            self._MetalyMinSpace = 280
            self._MetalyMinSpace2 = 500
            self._MetalyMinSpace3 = 1500

            self._MetalyMinEnclosureCO = 10
            self._MetalyMinEnclosureCO2 = 50
            self._MetalyMinArea = 140000
        if DesignParameters._Technology == 'TSMC130nm':
            self._MetalyMinWidth = None
            self._MetalyMaxWidth = None
            self._MetalyMinSpace = None
            self._MetalyMinSpace2 = None
            self._MetalyMinSpace3 = None

            self._MetalyMinEnclosureCO = None
            self._MetalyMinEnclosureCO2 = None
            self._MetalyMinArea = None

        if DesignParameters._Technology == 'TSMC180nm':
            self._MetalyMinWidth = None
            self._MetalyMaxWidth = None
            self._MetalyMinSpace = None
            self._MetalyMinSpace2 = None
            self._MetalyMinSpace3 = None

            self._MetalyMinEnclosureCO = None
            self._MetalyMinEnclosureCO2 = None
            self._MetalyMinArea = None

    def DRCMetalyMinSpace(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalyMinSpace
            elif 210 < _Width and 520 < _ParallelLength:
                if 1500 < _Width and 1500 < _ParallelLength:
                    if 4500 < _Width and 4500 < _ParallelLength:
                        return self._MetalyMinSpace4
                    else:
                        return self._MetalyMinSpace3
                else:
                    return self._MetalyMinSpace2
            else:
                return self._MetalyMinSpace

        if DesignParameters._Technology == 'SS28nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalyMinSpace
            elif 72 < _Width and 104 < _ParallelLength:
                if 156 < _Width and 104 < _ParallelLength:
                    if 208 < _Width and 104 < _ParallelLength:
                        if 208 < _Width and 300 < _ParallelLength:
                            return self._MetalyMinSpace5
                        else:
                            return self._MetalyMinSpace4
                    else:
                        return self._MetalyMinSpace3
                else:
                    return self._MetalyMinSpace2
            else:
                return self._MetalyMinSpace

        if DesignParameters._Technology == 'TSMC65nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalyMinSpace
            elif 390 < _Width and 1000 < _ParallelLength:
                if 1500 < _Width and 1500 < _ParallelLength:
                    if 4500 < _Width and 4500 < _ParallelLength:
                        return self._MetalyMinSpace4
                    else:
                        return self._MetalyMinSpace3
                else:
                    return self._MetalyMinSpace2
            else:
                return self._MetalyMinSpace
        if DesignParameters._Technology == 'TSMC90nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalyMinSpace
            elif 1500 < _Width and 1500 < _ParallelLength:
                if 4500 < _Width and 4500 < _ParallelLength:
                    return self._MetalyMinSpace3
                else:
                    return self._MetalyMinSpace2
            else:
                return self._MetalyMinSpace

        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None


class DRCMETALz:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._MetalzMinWidth = 400
            self._MetalzMaxWidth = 12000
            self._MetalzMinSpace = 400
            self._MetalzMinSpace2 = 500
            self._MetalzMinSpace3 = 1500

            self._MetalzMinEnclosureCO = 20
            self._MetalzMinEnclosureCO2 = 80
            self._MetalzMinArea = 565000

        if DesignParameters._Technology == 'SS28nm':
            self._MetalzMinWidth = 400
            self._MetalzMaxWidth = 12000
            self._MetalzMinSpace = 400
            self._MetalzMinSpace2 = 800
            self._MetalzMinSpace3 = 1600

            self._MetalzMinEnclosureCO = 20
            self._MetalzMinEnclosureCO2 = 80
            self._MetalzMinArea = 480

        if DesignParameters._Technology == 'TSMC65nm':
            self._MetalzMinWidth = 400
            self._MetalzMaxWidth = 12000
            self._MetalzMinSpace = 400
            self._MetalzMinSpace2 = 500
            self._MetalzMinSpace3 = 1500

            self._MetalzMinEnclosureCO = 20
            self._MetalzMinEnclosureCO2 = 80
            self._MetalzMinArea = 565000
        if DesignParameters._Technology == 'TSMC90nm':
            self._MetalzMinWidth = None
            self._MetalzMaxWidth = None
            self._MetalzMinSpace = None
            self._MetalzMinSpace2 = None
            self._MetalzMinSpace3 = None

            self._MetalzMinEnclosureCO = None
            self._MetalzMinEnclosureCO2 = None
            self._MetalzMinArea = None
        if DesignParameters._Technology == 'TSMC130nm':
            self._MetalzMinWidth = None
            self._MetalzMaxWidth = None
            self._MetalzMinSpace = None
            self._MetalzMinSpace2 = None
            self._MetalzMinSpace3 = None

            self._MetalzMinEnclosureCO = None
            self._MetalzMinEnclosureCO2 = None
            self._MetalzMinArea = None

        if DesignParameters._Technology == 'TSMC180nm':
            self._MetalzMinWidth = None
            self._MetalzMaxWidth = None
            self._MetalzMinSpace = None
            self._MetalzMinSpace2 = None
            self._MetalzMinSpace3 = None

            self._MetalzMinEnclosureCO = None
            self._MetalzMinEnclosureCO2 = None
            self._MetalzMinArea = None

    def DRCMetalzMinSpace(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalzMinSpace
            elif 1500 < _Width and 1500 < _ParallelLength:
                if 4500 < _Width and 4500 < _ParallelLength:
                    return self._MetalzMinSpace3
                else:
                    return self._MetalzMinSpace2
            else:
                return self._MetalzMinSpace

        if DesignParameters._Technology == 'SS28nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalzMinSpace
            elif 2000 < _Width and 2000 < _ParallelLength:
                if 4000 < _Width and 4000 < _ParallelLength:
                    return self._MetalzMinSpace3
                else:
                    return self._MetalzMinSpace2
            else:
                return self._MetalzMinSpace

        if DesignParameters._Technology == 'TSMC65nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalzMinSpace
            elif 1500 < _Width and 1500 < _ParallelLength:
                if 4500 < _Width and 4500 < _ParallelLength:
                    return self._MetalzMinSpace3
                else:
                    return self._MetalzMinSpace2
            else:
                return self._MetalzMinSpace
        if DesignParameters._Technology == 'TSMC90nm':
            return None

        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None


class DRCMETALr:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._MetalrMinWidth = 500
            self._MetalrMaxWidth = 12000
            self._MetalrMinSpace = 500
            self._MetalrMinSpace2 = 650
            self._MetalrMinSpace3 = 1500

            self._MetalrMinEnclosureCO = 20
            self._MetalrMinEnclosureCO2 = 80
            self._MetalrMinArea = 1000000

        if DesignParameters._Technology == 'SS28nm':
            self._MetalrMinWidth = 4000  # A
            self._MetalrMaxWidth = 12000  # B
            self._MetalrMinSpace = 2000  # C

            self._MetalrMinEnclosureCO = 1000  # F
            self._MetalrMinEnclosureCO2 = 1000  # G
            self._MetalrMinArea = 16000  # H

        if DesignParameters._Technology == 'TSMC65nm':
            self._MetalrMinWidth = 500
            self._MetalrMaxWidth = 12000
            self._MetalrMinSpace = 500
            self._MetalrMinSpace2 = 650
            self._MetalrMinSpace3 = 1500

            self._MetalrMinEnclosureCO = 20
            self._MetalrMinEnclosureCO2 = 80
            self._MetalrMinArea = 1000000
        if DesignParameters._Technology == 'TSMC90nm':
            self._MetalrMinWidth = None
            self._MetalrMaxWidth = None
            self._MetalrMinSpace = None
            self._MetalrMinSpace2 = None
            self._MetalrMinSpace3 = None

            self._MetalrMinEnclosureCO = None
            self._MetalrMinEnclosureCO2 = None
            self._MetalrMinArea = None
        if DesignParameters._Technology == 'TSMC130nm':
            self._MetalrMinWidth = None
            self._MetalrMaxWidth = None
            self._MetalrMinSpace = None
            self._MetalrMinSpace2 = None
            self._MetalrMinSpace3 = None

            self._MetalrMinEnclosureCO = None
            self._MetalrMinEnclosureCO2 = None
            self._MetalrMinArea = None

        if DesignParameters._Technology == 'TSMC180nm':
            self._MetalrMinWidth = None
            self._MetalrMaxWidth = None
            self._MetalrMinSpace = None
            self._MetalrMinSpace2 = None
            self._MetalrMinSpace3 = None

            self._MetalrMinEnclosureCO = None
            self._MetalrMinEnclosureCO2 = None
            self._MetalrMinArea = None

    def DRCMetalrMinSpace(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalrMinSpace
            elif 1500 < _Width and 1500 < _ParallelLength:
                if 4500 < _Width and 4500 < _ParallelLength:
                    return self._MetalrMinSpace3
                else:
                    return self._MetalrMinSpace2
            else:
                return self._MetalrMinSpace

        if DesignParameters._Technology == 'SS28nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalrMinSpace
            else:
                return self._MetalrMinSpace

        if DesignParameters._Technology == 'TSMC65nm':
            if _Width == None and _ParallelLength == None:
                return self._MetalrMinSpace
            elif 1500 < _Width and 1500 < _ParallelLength:
                if 4500 < _Width and 4500 < _ParallelLength:
                    return self._MetalrMinSpace3
                else:
                    return self._MetalrMinSpace2
            else:
                return self._MetalrMinSpace
        if DesignParameters._Technology == 'TSMC90nm':
            return None

        if DesignParameters._Technology == 'TSMC130nm':
            return None
        if DesignParameters._Technology == 'TSMC180nm':
            return None


class DRCRPO:
    def __init__(self):
        if DesignParameters._Technology == 'TSMC45nm':
            self._RPOMinWidth = 400
            self._RPOMinSpace = 400

            self._RPOMinSpace2OD = 220
            self._RPOMinSpace2CO = 220

            self._RPOMinSpace2UnrelatedPO = 180
            self._RPOMinExtensionOnPO = 220
            self._RPOMinExtensionOnPOLargerThan10um = 300
            self._RPOMinExtensionOnPOSmallerThan430nm = 300
        if DesignParameters._Technology == 'TSMC65nm':
            self._RPOMinWidth = 430
            self._RPOMinSpace = 430

            self._RPOMinSpace2OD = 220
            self._RPOMinSpace2CO = 220

            self._RPOMinSpace2UnrelatedPO = 250
            self._RPOMinExtensionOnPO = 220
            self._RPOMinExtensionOnPOLargerThan10um = 300
        if DesignParameters._Technology == 'TSMC90nm':
            self._RPOMinWidth = 430
            self._RPOMinSpace = 430
            self._RPOMinSpace2OD = 220
            self._RPOMinSpace2CO = 220

            self._RPOMinSpace2UnrelatedPO = 250
            self._RPOMinExtensionOnPO = 220
            self._RPOMinExtensionOnPOLargerThan10um = 300

        if DesignParameters._Technology == 'TSMC130nm':
            self._RPOMinWidth = 430
            self._RPOMinSpace = 430
            self._RPOMinSpace2OD = 220
            self._RPOMinSpace2CO = 220

            self._RPOMinSpace2UnrelatedPO = 180
            self._RPOMinExtensionOnPO = 220
            self._RPOMinExtensionOnPOLargerThan10um = 300

        if DesignParameters._Technology == 'TSMC180nm':
            self._RPOMinWidth = 430
            self._RPOMinSpace = 430
            self._RPOMinSpace2OD = 220
            self._RPOMinSpace2CO = 220

            self._RPOMinSpace2UnrelatedPO = 250
            self._RPOMinExtensionOnPO = 220

    def DRCRPOMinExtensionOnPO(self, _Width=None):
        if DesignParameters._Technology == 'TSMC45nm':
            if _Width > 100000:
                return self._RPOMinExtensionOnPOLargerThan10um
            elif _Width > 430:
                return self._RPOMinExtensionOnPOSmallerThan430nm
            else:
                return self._RPOMinExtensionOnPO
        if DesignParameters._Technology == 'TSMC65nm':
            if _Width > 100000:
                return self._RPOMinExtensionOnPOLargerThan10um
            else:
                return self._RPOMinExtensionOnPO
        if DesignParameters._Technology == 'TSMC90nm':
            if _Width > 100000:
                return self._RPOMinExtensionOnPOLargerThan10um
            else:
                return self._RPOMinExtensionOnPO
        if DesignParameters._Technology == 'TSMC130nm':
            return self._RPOMinExtensionOnPO
        if DesignParameters._Technology == 'TSMC180nm':
            return self._RPOMinExtensionOnPO


class DRCSLVT:
    def __init__(self):
        if DesignParameters._Technology == 'SS28nm':
            self._SlvtMinWidth = 170
            self._SlvtMinSpace = 170
            self._SlvtMinExtensionOnOD = 56
            self._SlvtMinArea = 95000
            self._SlvtMinArea2 = 160000  ## SLVT (BH) Minimum Area 0.16um^2, junung

    def DRCSLVTMinSpace(self, _Width=None, _ParallelLength=None):
        if DesignParameters._Technology == 'SS28nm':
            if _Width == None and _ParallelLength == None:
                return self._SlvtMinSpace
            else:
                return self._SlvtMinSpace


class DRCXVT:
    # XVT means {SLVT, LVT, HVT}. So far, all XVT's DRC rules are all the same. If different rules are found, it should be changed.
    def __init__(self):
        if DesignParameters._Technology == 'SS28nm':
            self._XvtMinWidth = 170
            self._XvtMinSpace = 170
            self._XvtMinExtensionOnOD = 56  # GRSLVT9b
            self._XvtMinEnclosureOfODX = 35  # This value is calculated by GRSLVT9a(horizontal direction)
            self._XvtMinEnclosureOfODY = 56  # GRSLVT9b (vertical direction,  same with _XvtMinExtensionOnOD)
            self._XvtMinArea = 95000
            self._XvtMinArea2 = 160000

        elif DesignParameters._Technology == 'TSMC65nm':
            self._XvtMinWidth = 180  # VTL_N_W_1
            self._XvtMinSpace = 180  # VTL_N_S_1 (there are other space rules)
            self._XvtMinEnclosureOfODX = 10  # This value is calculated by VTL_N_EN1(horizontal direction)
            self._XvtMinEnclosureOfODY = 160  # VTL_N_EN2 (vertical direction)
            self._XvtMinArea = 270000  # VTL_N_A_1 = VTL_N_A_2
            # self._XvtMinArea2 = 160000


class DRC(DRCMultiplicantForMinEdgeWidth, DRCOD, DRCPOLYGATE, DRCPP, DRCNP, DRCCO, DRCMETAL1, DRCMETALy, DRCVIAy,
          DRCMETALz, DRCVIAz, DRCMETALr, DRCVIAr, DRCNW, DRCVIAx, DRCMETALx, DRCMinSnapSpacing, DRCRPO, DRCSLVT,
          DRCXVT):
    def __init__(self):
        DRCNW.__init__(self)
        DRCOD.__init__(self)
        DRCPOLYGATE.__init__(self)
        DRCPP.__init__(self)
        DRCNP.__init__(self)
        DRCCO.__init__(self)
        DRCMETAL1.__init__(self)
        DRCVIAx.__init__(self)
        DRCMETALx.__init__(self)
        DRCVIAy.__init__(self)
        DRCMETALy.__init__(self)
        DRCVIAz.__init__(self)
        DRCMETALz.__init__(self)
        DRCVIAr.__init__(self)
        DRCMETALr.__init__(self)
        DRCMinSnapSpacing.__init__(self)
        DRCRPO.__init__(self)
        DRCSLVT.__init__(self)
        DRCXVT.__init__(self)
    # def CalculateMinimumDistanceBtwElements(self, _Element1 = None, _Element2 = None):
    #     if _Element1 == None or _Element2 == None:
    #         raise user_define_exceptions.IncorrectInputError('_Element1 & Element2 should not be None')
    #     _DesignParameterTypeOfElement1= _Element1['_DesignParametertype']
    #     _DesignParameterTypeOfElement2= _Element2['_DesignParametertype']



