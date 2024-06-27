from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC
from generatorLib.generator_models import NbodyContact_sm
from generatorLib.generator_models import PbodyContact_sm


class _SubRing(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='_SubRing'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameter(self, _Psubtype=True, _MetalOpen=None, _Height=5000, _Width=3000, _Thickness=348, _COpitch=175, _Enclosure=None):

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        if _COpitch == None:
            _XpitchBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None)
            _YpitchBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None)
        else:
            _XpitchBtwCO = _COpitch
            _YpitchBtwCO = _COpitch

        _NumofCOX = int((_Thickness - 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide - _DRCObj._CoMinWidth) // _XpitchBtwCO + 1)
        _NumofCOY_topbot = int((_Width / 2 - 2 * _DRCObj._CoMinEnclosureByOD - _DRCObj._CoMinWidth - _YpitchBtwCO / 2) // _YpitchBtwCO + 1)
        _NumofCOY_rightleft = int((_Height / 2 - 2 * _DRCObj._CoMinEnclosureByOD - _DRCObj._CoMinWidth - _YpitchBtwCO / 2) // _YpitchBtwCO + 1)

        if _Width / 2 % 2 == 0:
            _XCoord = 0
            _OverLapX = 0
        elif _Width / 2 % 2 == 1:
            _XCoord = 0
            _OverLapX = 1 + MinSnapSpacing / 2.0
        else:
            _XCoord = MinSnapSpacing / 2.0
            _OverLapX = 1 + MinSnapSpacing / 2.0

        if _Height / 2 % 2 == 0:
            _YCoord = 0
            _OverLapY = 0
        elif _Height / 2 % 2 == 1:
            _YCoord = 0
            _OverLapY = 1 + MinSnapSpacing / 2.0
        else:
            _YCoord = MinSnapSpacing / 2.0
            _OverLapY = 1 + MinSnapSpacing / 2.0

        Parameters_TopRight_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOY_topbot,
            _NumberOfNbodyCOY=_NumofCOX,
            _Met1XWidth=_Width / 2 + _OverLapX,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_TopRight_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOY_topbot,
            _NumberOfPbodyCOY=_NumofCOX,
            _Met1XWidth=_Width / 2 + _OverLapX,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        Parameters_TopLeft_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOY_topbot,
            _NumberOfNbodyCOY=_NumofCOX,
            _Met1XWidth=_Width / 2 + _OverLapX,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_TopLeft_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOY_topbot,
            _NumberOfPbodyCOY=_NumofCOX,
            _Met1XWidth=_Width / 2 + _OverLapX,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        Parameters_BotRight_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOY_topbot,
            _NumberOfNbodyCOY=_NumofCOX,
            _Met1XWidth=_Width / 2 + _OverLapX,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_BotRight_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOY_topbot,
            _NumberOfPbodyCOY=_NumofCOX,
            _Met1XWidth=_Width / 2 + _OverLapX,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        Parameters_BotLeft_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOY_topbot,
            _NumberOfNbodyCOY=_NumofCOX,
            _Met1XWidth=_Width / 2 + _OverLapX,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_BotLeft_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOY_topbot,
            _NumberOfPbodyCOY=_NumofCOX,
            _Met1XWidth=_Width / 2 + _OverLapX,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        Parameters_RightUpper_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOX,
            _NumberOfNbodyCOY=_NumofCOY_rightleft,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Height / 2 + _OverLapY,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_RightUpper_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOX,
            _NumberOfPbodyCOY=_NumofCOY_rightleft,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Height / 2 + _OverLapY,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        Parameters_RightLower_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOX,
            _NumberOfNbodyCOY=_NumofCOY_rightleft,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Height / 2 + _OverLapY,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_RightLower_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOX,
            _NumberOfPbodyCOY=_NumofCOY_rightleft,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Height / 2 + _OverLapY,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        Parameters_LeftUpper_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOX,
            _NumberOfNbodyCOY=_NumofCOY_rightleft,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Height / 2 + _OverLapY,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_LeftUpper_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOX,
            _NumberOfPbodyCOY=_NumofCOY_rightleft,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Height / 2 + _OverLapY,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        Parameters_LeftLower_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOX,
            _NumberOfNbodyCOY=_NumofCOY_rightleft,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Height / 2 + _OverLapY,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_LeftLower_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOX,
            _NumberOfPbodyCOY=_NumofCOY_rightleft,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Height / 2 + _OverLapY,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        Parameters_Corner_N = dict(
            _InputModeArea=False,
            _NumberOfNbodyCOX=_NumofCOX,
            _NumberOfNbodyCOY=_NumofCOX,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _NWEnclosure=_Enclosure
        )
        Parameters_Corner_P = dict(
            _InputModeArea=False,
            _NumberOfPbodyCOX=_NumofCOX,
            _NumberOfPbodyCOY=_NumofCOX,
            _Met1XWidth=_Thickness,
            _Met1YWidth=_Thickness,
            _COXpitch=_COpitch,
            _COYpitch=_COpitch,
            _PPEnclosure=_Enclosure
        )

        if _Psubtype == True:
            if _MetalOpen != 'top':
                self._DesignParameter['topright'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='toprightIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['topright']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_TopRight_P)
                self._DesignParameter['topright']['_XYCoordinates'] = [[_XCoord + _Width / 4, _YCoord + (_Height + _Thickness) / 2]]
                self._DesignParameter['topleft'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='topleftIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['topleft']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_TopLeft_P)
                self._DesignParameter['topleft']['_XYCoordinates'] = [[_XCoord - _Width / 4, _YCoord + (_Height + _Thickness) / 2]]

            if _MetalOpen != 'bot':
                self._DesignParameter['botright'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='botrightIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['botright']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_BotRight_P)
                self._DesignParameter['botright']['_XYCoordinates'] = [[_XCoord + _Width / 4, _YCoord - (_Height + _Thickness) / 2]]
                self._DesignParameter['botleft'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='botleftIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['botleft']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_BotLeft_P)
                self._DesignParameter['botleft']['_XYCoordinates'] = [[_XCoord - _Width / 4, _YCoord - (_Height + _Thickness) / 2]]

            if _MetalOpen != 'right':
                self._DesignParameter['rightupper'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='rightupperIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['rightupper']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_RightUpper_P)
                self._DesignParameter['rightupper']['_XYCoordinates'] = [[_XCoord + (_Width + _Thickness) / 2, _YCoord + _Height / 4]]
                self._DesignParameter['rightlower'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='rightlowerIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['rightlower']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_RightLower_P)
                self._DesignParameter['rightlower']['_XYCoordinates'] = [[_XCoord + (_Width + _Thickness) / 2, _YCoord - _Height / 4]]

            if _MetalOpen != 'left':
                self._DesignParameter['leftupper'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='leftupperIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['leftupper']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_LeftUpper_P)
                self._DesignParameter['leftupper']['_XYCoordinates'] = [[_XCoord - (_Width + _Thickness) / 2, _YCoord + _Height / 4]]
                self._DesignParameter['leftlower'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='leftlowerIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['leftlower']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_LeftLower_P)
                self._DesignParameter['leftlower']['_XYCoordinates'] = [[_XCoord - (_Width + _Thickness) / 2, _YCoord - _Height / 4]]

            self._DesignParameter['corner'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=PbodyContact_sm._PbodyContact(_Name='cornerIn{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['corner']['_DesignObj']._CalculatePbodyContactDesignParameter(**Parameters_Corner_P)
            self._DesignParameter['corner']['_XYCoordinates'] = [[_XCoord - (_Width + _Thickness) / 2, _YCoord + (_Height + _Thickness) / 2], [_XCoord + (_Width + _Thickness) / 2, _YCoord + (_Height + _Thickness) / 2],
                                                                 [_XCoord - (_Width + _Thickness) / 2, _YCoord - (_Height + _Thickness) / 2], [_XCoord + (_Width + _Thickness) / 2, _YCoord - (_Height + _Thickness) / 2]]

        else:
            if _MetalOpen != 'top':
                self._DesignParameter['topright'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='toprightIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['topright']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_TopRight_N)
                self._DesignParameter['topright']['_XYCoordinates'] = [[_XCoord + _Width / 4, _YCoord + (_Height + _Thickness) / 2]]
                self._DesignParameter['topleft'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='topleftIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['topleft']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_TopLeft_N)
                self._DesignParameter['topleft']['_XYCoordinates'] = [[_XCoord -_Width / 4, _YCoord + (_Height + _Thickness) / 2]]

            if _MetalOpen != 'bot':
                self._DesignParameter['botright'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='botrightIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['botright']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_BotRight_N)
                self._DesignParameter['botright']['_XYCoordinates'] = [[_XCoord + _Width / 4, _YCoord - (_Height + _Thickness) / 2]]
                self._DesignParameter['botleft'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='botleftIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['botleft']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_BotLeft_N)
                self._DesignParameter['botleft']['_XYCoordinates'] = [[_XCoord - _Width / 4, _YCoord - (_Height + _Thickness) / 2]]

            if _MetalOpen != 'right':
                self._DesignParameter['rightupper'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='rightupperIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['rightupper']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_RightUpper_N)
                self._DesignParameter['rightupper']['_XYCoordinates'] = [[_XCoord + (_Width + _Thickness) / 2, _YCoord + _Height / 4]]
                self._DesignParameter['rightlower'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='rightlowerIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['rightlower']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_RightLower_N)
                self._DesignParameter['rightlower']['_XYCoordinates'] = [[_XCoord + (_Width + _Thickness) / 2, _YCoord - _Height / 4]]

            if _MetalOpen != 'left':
                self._DesignParameter['leftupper'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='leftupperIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['leftupper']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_LeftUpper_N)
                self._DesignParameter['leftupper']['_XYCoordinates'] = [[_XCoord - (_Width + _Thickness) / 2, _YCoord + _Height / 4]]
                self._DesignParameter['leftlower'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='leftlowerIn{}'.format(_Name)), _XYCoordinates=[])[0]
                self._DesignParameter['leftlower']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_LeftLower_N)
                self._DesignParameter['leftlower']['_XYCoordinates'] = [[_XCoord - (_Width + _Thickness) / 2, _YCoord - _Height / 4]]

            self._DesignParameter['corner'] = self._SrefElementDeclaration(_Reflect=[0, 0, 0], _Angle=0, _DesignObj=NbodyContact_sm._NbodyContact(_Name='cornerIn{}'.format(_Name)), _XYCoordinates=[])[0]
            self._DesignParameter['corner']['_DesignObj']._CalculateNbodyContactDesignParameter(**Parameters_Corner_N)
            self._DesignParameter['corner']['_XYCoordinates'] = [[_XCoord - (_Width + _Thickness) / 2, _YCoord + (_Height + _Thickness) / 2], [_XCoord + (_Width + _Thickness) / 2, _YCoord + (_Height + _Thickness) / 2],
                                                                 [_XCoord - (_Width + _Thickness) / 2, _YCoord - (_Height + _Thickness) / 2], [_XCoord + (_Width + _Thickness) / 2, _YCoord - (_Height + _Thickness) / 2]]

if __name__ == '__main__':
    _Psubtype = False
    _MetalOpen = None
    _Height = 1502
    _Width = 1502
    _Thickness = 348
    _COpitch = 175
    _Enclosure = 56


    DesignParameters._Technology = 'SS28nm'
    TopObj = _SubRing(_DesignParameter=None, _Name='_SubRing')
    TopObj._CalculateDesignParameter(
        _Psubtype=_Psubtype,
        _MetalOpen=_MetalOpen,
        _Height=_Height,
        _Width=_Width,
        _Thickness=_Thickness,
        _COpitch=_COpitch,
        _Enclosure=_Enclosure
    )
    TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
    testStreamFile = open('./_SubRing.gds', 'wb')
    tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      ##############################')

    import ftplib

    ftp = ftplib.FTP('141.223.24.53')
    ftp.login('smlim96', 'min753531')
    ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
    myfile = open('_SubRing.gds', 'rb')
    ftp.storbinary('STOR _SubRing.gds', myfile)
    myfile.close()
