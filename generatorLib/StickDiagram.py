import types

from gds_editor_ver3 import gds_stream
from gds_editor_ver3 import gds_structures
from gds_editor_ver3 import gds_tags
from gds_editor_ver3 import gds_record
from gds_editor_ver3 import gds_elements
from datetime import datetime, MINYEAR
from gds_editor_ver3 import user_define_exceptions
import gds_editor_ver3
#
# import gds_editor_ver3.gds_stream
# import gds_editor_ver3.gds_structures
# import gds_editor_ver3.gds_tags
# import gds_editor_ver3.gds_record
# import gds_editor_ver3.gds_elements
# from datetime import datetime, MINYEAR
# import gds_editor_ver3.user_define_exceptions

from generatorLib import DesignParameters
import copy









class _StickDiagram:
    def __init__(self):
        pass

    def exec_pass(self,code, library_manager):
        for name in library_manager.class_name_dict:
            locals()[name] = library_manager.libraries[name]
        exec(code)

        # exec(code)

    def RoundupMinSnapSpacing(self, _DesignParameter=None, _MinSnapSpacing=None):
        if _DesignParameter ==None or _MinSnapSpacing ==None:
            raise user_define_exceptions.IncorrectInputError('_DesignParameter or _MinSnapSpacing has incorrect valuse')
        return (int(_DesignParameter /_MinSnapSpacing ) + 1)*_MinSnapSpacing
    def RounddownMinSnapSpacing(self, _DesignParameter=None, _MinSnapSpacing=None):
        if _DesignParameter ==None or _MinSnapSpacing ==None:
            raise user_define_exceptions.IncorrectInputError('_DesignParameter or _MinSnapSpacing has incorrect valuse')
        return int(_DesignParameter /_MinSnapSpacing ) *_MinSnapSpacing

    def TopLeft(self,element_name,hierarchy_list=None):
        if '_DesignParameter' not in self.__dict__:
            raise Exception("There is no DesignParameter.")
        if element_name not in self._DesignParameter:
            raise Exception("Invalid element name.")
        if hierarchy_list == None:
            element = self._DesignParameter[element_name]
            if element['_DesignParametertype'] == 1 : #Boundary Case
                return (element['_XYCoordinates'][0][0],element['_XYCoordinates'][0][1]+element['_YWidth'])
        else:
            if hierarchy_list[0] not in self._DesignParameter:
                raise Exception("Invalid Hierachy element Name.")
            element = self._DesignParameter[hierarchy_list[0]]
            for hierarchy_element in hierarchy_list:
                if hierarchy_element not in element['_DeisgnObj']._DesignParameter:
                    raise Exception("Ivalid Hierarchy element Name.")
                element = element['_DesignObj']._DesignParameter[hierarchy_element]
            element = element['_DesignObj']._DesignParameter[element_name]
            return (element['_XYCoordinates'][0][0],element['_XYCoordinates'][0][1]+element['_YWidth'])

    def TopRight(self,element_name):
        if '_DesignParameter' not in self.__dict__:
            raise Exception("There is no DesignParameter.")
        if element_name not in self._DesignParameter:
            raise Exception("Invalid element name.")
        element = self._DesignParameter[element_name]
        if element['_DesignParametertype'] == 1 : #Boundary Case
            return (element['_XYCoordinates'][0][0]+element['_XWidth'],element['_XYCoordinates'][0][1]+element['_YWidth'])

    def BottomLeft(self,element_name):
        if '_DesignParameter' not in self.__dict__:
            raise Exception("There is no DesignParameter.")
        if element_name not in self._DesignParameter:
            raise Exception("Invalid element name.")
        element = self._DesignParameter[element_name]
        if element['_DesignParametertype'] == 1 : #Boundary Case
            return (element['_XYCoordinates'][0][0],element['_XYCoordinates'][0][1])

    def BottomRight(self,element_name):
        if '_DesignParameter' not in self.__dict__:
            raise Exception("There is no DesignParameter.")
        if element_name not in self._DesignParameter:
            raise Exception("Invalid element name.")
        element = self._DesignParameter[element_name]
        if element['_DesignParametertype'] == 1 : #Boundary Case
            return (element['_XYCoordinates'][0][0]+element['_XWidth'],element['_XYCoordinates'][0][1])

    def Center(self,element_name):
        if '_DesignParameter' not in self.__dict__:
            raise Exception("There is no DesignParameter.")
        if element_name not in self._DesignParameter:
            raise Exception("Invalid element name.")
        element = self._DesignParameter[element_name]
        if element['_DesignParametertype'] == 1 : #Boundary Case
            return (element['_XYCoordinates'][0][0]+element['_XWidth']/2,element['_XYCoordinates'][0][1]+element['_YWidth']/2)

    # def Distance(self,element_name1,element_name2):
    #     element1 = self._DesignParameter[element_name1]
    #     element2 = self._DesignParameter[element_name2]
    #     center1 = self.Center(element_name1)
    #     center2 = self.Center(element_name2)
    #
    #     if


    def XYCoordinate2MinMaxXY(self, _XYCoordinates):
        x_list = []
        y_list = []
        for i in range(0, len(_XYCoordinates)):
            x_list.append(_XYCoordinates[i][0])
            y_list.append(_XYCoordinates[i][1])

        x_list = list(set(x_list))
        y_list = list(set(y_list))

        return x_list, y_list

    def MinMaxXY2XYCoordinate(self, _MinMaxXY):
        x_list, y_list = _MinMaxXY
        # return [(min(x_list), min(y_list)), (max(x_list), min(y_list)), (max(x_list), max(y_list)), (min(x_list), max(y_list)), (min(x_list), min(y_list))]
        return [[min(x_list), min(y_list)], [max(x_list), min(y_list)], [max(x_list), max(y_list)],
                [min(x_list), max(y_list)], [min(x_list), min(y_list)]]

    def XYCoordinate2CenterCoordinateAndWidth(self, _XYCoordinates):
        x_list, y_list = self.XYCoordinate2MinMaxXY(_XYCoordinates)

        XYCenter = (float(min(x_list) + max(x_list)) / 2, float(min(y_list) + max(y_list)) / 2)
        WidthX = abs(min(x_list) - max(x_list))
        WidthY = abs(min(y_list) - max(y_list))
        # del x_list, y_list
        return XYCenter, WidthX, WidthY

    def CenterCoordinateAndWidth2XYCoordinate(self, _XYCenter, _WidthX, _WidthY):
        x_list = [_XYCenter[0] - float(_WidthX) / 2, _XYCenter[0] + float(_WidthX) / 2]
        y_list = [_XYCenter[1] - float(_WidthY) / 2, _XYCenter[1] + float(_WidthY) / 2]
        return self.MinMaxXY2XYCoordinate([x_list, y_list])

    def _CreateGDSStream(self, _GDSStructures=[]):

        _newGDSStream=gds_editor_ver3.gds_stream.GDS_STREAM()

        _newGDSStream._BGNLIB=gds_editor_ver3.gds_record.GDS_BGNLIB()
        _newGDSStream._BGNLIB.tag=gds_editor_ver3.gds_tags.DICT['BGNLIB']
        _newGDSStream._BGNLIB.time_access=datetime.now()
        _newGDSStream._BGNLIB.time_modi=datetime.now()

        _newGDSStream._LIBNAME=gds_editor_ver3.gds_record.GDS_LIBNAME()
        _newGDSStream._LIBNAME.tag=gds_editor_ver3.gds_tags.DICT['LIBNAME']
        _newGDSStream._LIBNAME.libname='testLib'
        _newGDSStream._UNITS=gds_editor_ver3.gds_record.GDS_UNITS()
        _newGDSStream._UNITS.tag=gds_editor_ver3.gds_tags.DICT['UNITS']
        _newGDSStream._UNITS.unit_meter=1e-009
        _newGDSStream._UNITS.unit_user=0.001

        _newGDSStream._STRUCTURES=_GDSStructures

        _newGDSStream._HEADER=gds_editor_ver3.gds_record.GDS_HEADER()
        _newGDSStream._HEADER.tag=gds_editor_ver3.gds_tags.DICT['HEADER']
        _newGDSStream._HEADER.gds_version=5
        _newGDSStream._ENDLIB=gds_editor_ver3.gds_record.GDS_ENDLIB()
        _newGDSStream._ENDLIB.tag=gds_editor_ver3.gds_tags.DICT['ENDLIB']

        return _newGDSStream

    def _CreateGDSStructure(self, _GDSStructureName=None):
        _newGDSStructure = gds_editor_ver3.gds_structures.GDS_STRUCTURE()

        _newGDSStructure._BGNSTR = gds_editor_ver3.gds_record.GDS_BGNSTR()
        _newGDSStructure._BGNSTR.tag = gds_editor_ver3.gds_tags.DICT['BGNSTR']
        _newGDSStructure._BGNSTR.time_creation = datetime.now()
        _newGDSStructure._BGNSTR.time_modi = datetime.now()

        _newGDSStructure._STRNAME = gds_editor_ver3.gds_record.GDS_STRNAME()
        _newGDSStructure._STRNAME.tag = gds_editor_ver3.gds_tags.DICT['STRNAME']
        if _GDSStructureName==None:
            raise user_define_exceptions.IncorrectInputError('_GDSStructureName should have correct datatype')
        _newGDSStructure._STRNAME.strname = _GDSStructureName

        _newGDSStructure._ENDSTR = gds_editor_ver3.gds_record.GDS_ENDLIB()
        _newGDSStructure._ENDSTR.tag = gds_editor_ver3.gds_tags.DICT['ENDSTR']

        return _newGDSStructure

    def _CreateGDSBoundaryElement(self,_Layer=None,_Datatype=None, _XYCoordinates=None, _ElementName=None):
        _newGDSBoundaryElement=gds_editor_ver3.gds_elements.GDS_ELEMENT()
        _newGDSBoundaryElement._ELEMENTS=gds_editor_ver3.gds_elements.GDS_BOUNDARY()
        _newGDSBoundaryElement._ELEMENTS._BOUNDARY=gds_editor_ver3.gds_record.GDS_BOUNDARY()
        _newGDSBoundaryElement._ELEMENTS._BOUNDARY.tag=gds_editor_ver3.gds_tags.DICT['BOUNDARY']

        _newGDSBoundaryElement._ELEMENTS._LAYER=gds_editor_ver3.gds_record.GDS_LAYER()
        if _Layer==None:
            raise user_define_exceptions.IncorrectInputError('_Layer should have correct data type')
        _newGDSBoundaryElement._ELEMENTS._LAYER.layer=_Layer
        _newGDSBoundaryElement._ELEMENTS._LAYER.tag=gds_editor_ver3.gds_tags.DICT['LAYER']

        _newGDSBoundaryElement._ELEMENTS._DATATYPE = gds_editor_ver3.gds_record.GDS_DATATYPE()
        if _Datatype==None:
            raise user_define_exceptions.IncorrectInputError('_Datatype should have correct data type')
        _newGDSBoundaryElement._ELEMENTS._DATATYPE.datatype= _Datatype
        _newGDSBoundaryElement._ELEMENTS._DATATYPE.tag = gds_editor_ver3.gds_tags.DICT['DATATYPE']

        _newGDSBoundaryElement._ELEMENTS._XY=gds_editor_ver3.gds_record.GDS_XY()
        if _XYCoordinates==None:
            raise user_define_exceptions.IncorrectInputError('_XYCoordinates should have correct data type')
        _newGDSBoundaryElement._ELEMENTS._XY.xy=_XYCoordinates
        _newGDSBoundaryElement._ELEMENTS._XY.tag=gds_editor_ver3.gds_tags.DICT['XY']


        _newGDSBoundaryElement._ENDEL=gds_editor_ver3.gds_record.GDS_ENDEL()
        _newGDSBoundaryElement._ENDEL.tag=gds_editor_ver3.gds_tags.DICT['ENDEL']

        _newGDSBoundaryElement._GDS_ELEMENT_NAME=_ElementName
        return _newGDSBoundaryElement

    def _CreateGDSPathElement(self,_Layer=None,_Datatype=None, _Width=None,_XYCoordinates=None, _ElementName=None):
        _newGDSPathElement=gds_editor_ver3.gds_elements.GDS_ELEMENT()
        _newGDSPathElement._ELEMENTS=gds_editor_ver3.gds_elements.GDS_PATH()
        _newGDSPathElement._ELEMENTS._PATH=gds_editor_ver3.gds_record.GDS_PATH()
        _newGDSPathElement._ELEMENTS._PATH.tag=gds_editor_ver3.gds_tags.DICT['PATH']

        _newGDSPathElement._ELEMENTS._LAYER=gds_editor_ver3.gds_record.GDS_LAYER()
        if _Layer == None:
            print('_ElementName: ', _ElementName)
            raise user_define_exceptions.IncorrectInputError('_Layer should have correct data type')
        _newGDSPathElement._ELEMENTS._LAYER.layer=_Layer
        _newGDSPathElement._ELEMENTS._LAYER.tag=gds_editor_ver3.gds_tags.DICT['LAYER']

        _newGDSPathElement._ELEMENTS._DATATYPE=gds_editor_ver3.gds_record.GDS_DATATYPE()
        if _Datatype == None:
            print('_ElementName: ', _ElementName)
            raise user_define_exceptions.IncorrectInputError('_Datatype should have correct data type')
        _newGDSPathElement._ELEMENTS._DATATYPE.datatype=_Datatype
        _newGDSPathElement._ELEMENTS._DATATYPE.tag=gds_editor_ver3.gds_tags.DICT['DATATYPE']

        _newGDSPathElement._ELEMENTS._WIDTH=gds_editor_ver3.gds_record.GDS_WIDTH()
        if _Width == None:
            print('_ElementName: ', _ElementName)
            raise user_define_exceptions.IncorrectInputError('_Width should have correct data type')
        _newGDSPathElement._ELEMENTS._WIDTH.width=_Width
        _newGDSPathElement._ELEMENTS._WIDTH.tag=gds_editor_ver3.gds_tags.DICT['WIDTH']

        _newGDSPathElement._ELEMENTS._XY=gds_editor_ver3.gds_record.GDS_XY()
        if _XYCoordinates == None:
            print('_ElementName: ', _ElementName)
            raise user_define_exceptions.IncorrectInputError('_XYCoordinates should have correct data type')
        _newGDSPathElement._ELEMENTS._XY.xy=_XYCoordinates
        _newGDSPathElement._ELEMENTS._XY.tag=gds_editor_ver3.gds_tags.DICT['XY']

        _newGDSPathElement._ELEMENTS._PATHTYPE=gds_editor_ver3.gds_record.GDS_PATHTYPE()
        _newGDSPathElement._ELEMENTS._PATHTYPE.pathtype=0
        _newGDSPathElement._ELEMENTS._PATHTYPE.tag=gds_editor_ver3.gds_tags.DICT['PATHTYPE']

        _newGDSPathElement._ENDEL = gds_editor_ver3.gds_record.GDS_ENDEL()
        _newGDSPathElement._ENDEL.tag = gds_editor_ver3.gds_tags.DICT['ENDEL']

        _newGDSPathElement._GDS_ELEMENT_NAME = _ElementName

        return _newGDSPathElement

    def _CreateGDSSrefElement(self, _SREFName=None, _XYCoordinates=None, _ElementName=None, _Reflect=None, _Angle=None, ):

        if _SREFName == None:
            raise user_define_exceptions.IncorrectInputError('_SREFName should have correct data type')
        if _XYCoordinates == None:
            raise user_define_exceptions.IncorrectInputError('_XYCoordinates should have correct data type')
        _newGDSSrefElement=gds_editor_ver3.gds_elements.GDS_ELEMENT()
        _newGDSSrefElement._ELEMENTS=gds_editor_ver3.gds_elements.GDS_SREF()
        _newGDSSrefElement._ELEMENTS._SREF=gds_editor_ver3.gds_record.GDS_SREF()
        _newGDSSrefElement._ELEMENTS._SREF.tag=gds_editor_ver3.gds_tags.DICT['SREF']
        _newGDSSrefElement._ELEMENTS._SNAME=gds_editor_ver3.gds_record.GDS_SNAME()
        _newGDSSrefElement._ELEMENTS._SNAME.sname=_SREFName
        _newGDSSrefElement._ELEMENTS._SNAME.tag=gds_editor_ver3.gds_tags.DICT['SNAME']
        if _Reflect or _Angle != None:
            _newGDSSrefElement._ELEMENTS._STRANS = gds_editor_ver3.gds_elements.GDS_STRANS()
            _newGDSSrefElement._ELEMENTS._STRANS._STRANS = gds_editor_ver3.gds_record.GDS_STRANS()
            _newGDSSrefElement._ELEMENTS._STRANS._STRANS.tag = gds_editor_ver3.gds_tags.DICT['STRANS']
            _newGDSSrefElement._ELEMENTS._STRANS._STRANS.reflection = _Reflect[0]
            _newGDSSrefElement._ELEMENTS._STRANS._STRANS.abs_mag = _Reflect[1]
            _newGDSSrefElement._ELEMENTS._STRANS._STRANS.abs_angle = _Reflect[2]
            _newGDSSrefElement._ELEMENTS._STRANS._ANGLE = gds_editor_ver3.gds_record.GDS_ANGLE()
            _newGDSSrefElement._ELEMENTS._STRANS._ANGLE.tag = gds_editor_ver3.gds_tags.DICT['ANGLE']
            _newGDSSrefElement._ELEMENTS._STRANS._ANGLE.angle = _Angle

        _newGDSSrefElement._ELEMENTS._XY=gds_editor_ver3.gds_record.GDS_XY()
        _newGDSSrefElement._ELEMENTS._XY.xy=_XYCoordinates
        _newGDSSrefElement._ELEMENTS._XY.tag=gds_editor_ver3.gds_tags.DICT['XY']

        _newGDSSrefElement._ENDEL=gds_editor_ver3.gds_record.GDS_ENDEL()
        _newGDSSrefElement._ENDEL.tag=gds_editor_ver3.gds_tags.DICT['ENDEL']

        _newGDSSrefElement._GDS_ELEMENT_NAME = _ElementName

        return _newGDSSrefElement

    def _CreateGDSTextElement(self,  _Layer=None,_Datatype=None, _Presentation = None, _Reflect=None, _XYCoordinates=None,  _Mag=None, _Angle=None,    _TEXT=None, _ElementName=None,):
        #### Type = 0 when used to represent pin layer
        if _TEXT == None:
            raise user_define_exceptions.IncorrectInputError('_TEXT should have string data to be written as text')
        if _XYCoordinates == None:
            raise user_define_exceptions.IncorrectInputError('_XYCoordinates should have correct data type')
        _newGDSTextElement=gds_editor_ver3.gds_elements.GDS_ELEMENT()
        _newGDSTextElement._ELEMENTS=gds_editor_ver3.gds_elements.GDS_TEXT()
        _newGDSTextElement._ELEMENTS._TEXT= gds_editor_ver3.gds_record.GDS_TEXT()
        _newGDSTextElement._ELEMENTS._TEXT.tag=gds_editor_ver3.gds_tags.DICT['TEXT']

        _newGDSTextElement._ELEMENTS._LAYER=gds_editor_ver3.gds_record.GDS_LAYER()
        if _Layer == None:
            raise user_define_exceptions.IncorrectInputError('_Layer should have correct data type')
        _newGDSTextElement._ELEMENTS._LAYER.layer=_Layer
        _newGDSTextElement._ELEMENTS._LAYER.tag=gds_editor_ver3.gds_tags.DICT['LAYER']


        _newGDSTextElement._ELEMENTS._TEXTBODY=gds_editor_ver3.gds_elements.GDS_TEXTBODY()
        _newGDSTextElement._ELEMENTS._TEXTBODY._TEXTTYPE = gds_editor_ver3.gds_record.GDS_TEXTTYPE()
        if _Datatype == None:
            raise user_define_exceptions.IncorrectInputError('_Datatype(_Texttype) should have correct data type')
        _newGDSTextElement._ELEMENTS._TEXTBODY._TEXTTYPE.texttype = _Datatype
        _newGDSTextElement._ELEMENTS._TEXTBODY._TEXTTYPE.tag = gds_editor_ver3.gds_tags.DICT['TEXTTYPE']
        _newGDSTextElement._ELEMENTS._TEXTBODY._PRESENTATION = gds_editor_ver3.gds_record.GDS_PRESENTATION()
        _newGDSTextElement._ELEMENTS._TEXTBODY._PRESENTATION.tag =  gds_editor_ver3.gds_tags.DICT['PRESENTATION']
        if _Presentation == None:
            raise user_define_exceptions.IncorrectInputError('_Presentation should have correct data type')
        _newGDSTextElement._ELEMENTS._TEXTBODY._PRESENTATION.font = _Presentation[0]
        _newGDSTextElement._ELEMENTS._TEXTBODY._PRESENTATION.vertical_presentation = _Presentation[1]
        _newGDSTextElement._ELEMENTS._TEXTBODY._PRESENTATION.horizontal_presentation = _Presentation[2]
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS = gds_editor_ver3.gds_elements.GDS_STRANS()
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._STRANS = gds_editor_ver3.gds_record.GDS_STRANS()
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._STRANS.tag = gds_editor_ver3.gds_tags.DICT['STRANS']
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._STRANS.reflection = _Reflect[0]
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._STRANS.abs_mag = _Reflect[1]
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._STRANS.abs_angle = _Reflect[2]
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._MAG = gds_editor_ver3.gds_record.GDS_MAG()
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._MAG.tag = gds_editor_ver3.gds_tags.DICT['MAG']
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._MAG.mag = _Mag
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._ANGLE = gds_editor_ver3.gds_record.GDS_ANGLE()
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._ANGLE.tag = gds_editor_ver3.gds_tags.DICT['ANGLE']
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRANS._ANGLE.angle = _Angle
        _newGDSTextElement._ELEMENTS._TEXTBODY._XY=gds_editor_ver3.gds_record.GDS_XY()
        if _XYCoordinates == None:
            raise user_define_exceptions.IncorrectInputError('_XYCoordinates should have correct data type')
        _newGDSTextElement._ELEMENTS._TEXTBODY._XY.xy=_XYCoordinates
        _newGDSTextElement._ELEMENTS._TEXTBODY._XY.tag=gds_editor_ver3.gds_tags.DICT['XY']
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRING=gds_editor_ver3.gds_record.GDS_STRING()
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRING.tag=gds_editor_ver3.gds_tags.DICT['STRING']
        if _TEXT == None:
            raise user_define_exceptions.IncorrectInputError('_TEXT should have correct data type')
        _newGDSTextElement._ELEMENTS._TEXTBODY._STRING.string_data = _TEXT
        _newGDSTextElement._ENDEL=gds_editor_ver3.gds_record.GDS_ENDEL()
        _newGDSTextElement._ENDEL.tag=gds_editor_ver3.gds_tags.DICT['ENDEL']

        _newGDSTextElement._GDS_ELEMENT_NAME = _ElementName
        return _newGDSTextElement

    def _ReadLayerMapFile(self,_LayerMapFile):
        _newLayerMapDictionary={}
        linenum=len(_LayerMapFile.readlines())
        _LayerMapFile.seek(0)

        for i in range(0, linenum):
            tmp=_LayerMapFile.readline()
            tmp2=tmp.split()
            #print  tmp2
            _newLayerMapDictionary[(tmp2[0],tmp2[1])]=(int(tmp2[2]), int(tmp2[3]))
        return _newLayerMapDictionary


    def _UpdateDesignParameter2GDSStructure(self, _DesignParameterInDictionary = None):
        print('#########################################################################################################')
        print('                                    {}  Update2GDS Start                                    '.format(_DesignParameterInDictionary['_Name']['_Name']))
        print('#########################################################################################################')

        _DesignParameterInDictionary['_GDSFile']['_GDSFile']=[ self._CreateGDSStructure(_GDSStructureName=_DesignParameterInDictionary['_Name']['_Name']) ]

        for _DesignParameter in _DesignParameterInDictionary:
            print('*********** ', _DesignParameter, ' is updating to GDS **********')
            if _DesignParameterInDictionary[_DesignParameter]['_DesignParametertype'] == 1 and _DesignParameterInDictionary[_DesignParameter]['_Ignore']==None:
                if DesignParameters._Technology!='180nm' and _DesignParameterInDictionary[_DesignParameter]['_Layer'] == DesignParameters._LayerMapping['WELLBODY'][0]:
                    pass
                elif DesignParameters._Technology!='065nm' and _DesignParameterInDictionary[_DesignParameter]['_Layer'] == DesignParameters._LayerMapping['PDK'][0] :
                    pass
                else :
                    for _XYCoordinate in _DesignParameterInDictionary[_DesignParameter]['_XYCoordinates']:

                        _DesignParameterInDictionary['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(
                                                                                            self._CreateGDSBoundaryElement(_Layer= _DesignParameterInDictionary[_DesignParameter]['_Layer'], _Datatype=_DesignParameterInDictionary[_DesignParameter]['_Datatype'],
                                                                                                                           _XYCoordinates=self.CenterCoordinateAndWidth2XYCoordinate( _XYCenter=_XYCoordinate,
                                                                                                                           _WidthX=_DesignParameterInDictionary[_DesignParameter]['_XWidth'],
                                                                                                                           _WidthY=_DesignParameterInDictionary[_DesignParameter]['_YWidth'],),
                                                                                                                           _ElementName = _DesignParameter)
                                                                                            )
            elif _DesignParameterInDictionary[_DesignParameter]['_DesignParametertype'] == 11 and _DesignParameterInDictionary[_DesignParameter]['_Ignore']==None:
                if DesignParameters._Technology!='180nm' and _DesignParameterInDictionary[_DesignParameter]['_Layer'] == DesignParameters._LayerMapping['WELLBODY'][0]:
                    pass
                elif DesignParameters._Technology!='065nm' and _DesignParameterInDictionary[_DesignParameter]['_Layer'] == DesignParameters._LayerMapping['PDK'][0] :
                    pass
                else :
                    for _XYCoordinate in _DesignParameterInDictionary[_DesignParameter]['_XYCoordinates']:

                        _DesignParameterInDictionary['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(
                                                                                            self._CreateGDSBoundaryElement(_Layer= _DesignParameterInDictionary[_DesignParameter]['_Layer'], _Datatype=_DesignParameterInDictionary[_DesignParameter]['_Datatype'],
                                                                                                                           _XYCoordinates=_DesignParameterInDictionary[_DesignParameter]['_XYCoordinates'],
                                                                                                                           _ElementName = _DesignParameter)
                                                                                            )
            elif _DesignParameterInDictionary[_DesignParameter]['_DesignParametertype'] == 2 and _DesignParameterInDictionary[_DesignParameter]['_Ignore']==None:
                for _XYCoordinates in _DesignParameterInDictionary[_DesignParameter]['_XYCoordinates']:
                    # print 'monitor for debug stickDiagram0: ', _DesignParameterInDictionary[_DesignParameter]['_XYCoordinates']
                    # print 'monitor for debug stickDiagram1: ', _XYCoordinates
                    # print 'monitor for debug stickDiagram1: numOfPoints=', len(_XYCoordinates)
                    _tmpXYCoordinates = copy.deepcopy(_XYCoordinates)
                    # print 'monitor for debug stickDiagram2: ', _tmpXYCoordinates
                    _tmpIndex = 0
                    while True:
                        # print 'monitor for debug _tmpIndex: ', _tmpIndex, len(_tmpXYCoordinates)
                        if _tmpIndex < (len(_tmpXYCoordinates) - 1):
                            if (_tmpXYCoordinates[_tmpIndex][0] == _tmpXYCoordinates[_tmpIndex + 1][0]) and (_tmpXYCoordinates[_tmpIndex][1] == _tmpXYCoordinates[_tmpIndex + 1][1]):
                                # print 'monitor for debug delete: ', _tmpXYCoordinates[_tmpIndex + 1]
                                del _tmpXYCoordinates[_tmpIndex + 1]
                            else:
                                _tmpIndex = _tmpIndex + 1
                        else :
                            break
                    # print 'monitor for debug stickDiagram2: ', _tmpXYCoordinates
                    # print 'monitor for debug stickDiagram2: numOfPoints=', len(_tmpXYCoordinates)
                    if len(_tmpXYCoordinates) >= 2:
                        _DesignParameterInDictionary['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(
                                                                                            self._CreateGDSPathElement(_Layer=_DesignParameterInDictionary[_DesignParameter]['_Layer'], _Datatype=_DesignParameterInDictionary[_DesignParameter]['_Datatype'],
                                                                                                                       _Width=_DesignParameterInDictionary[_DesignParameter]['_Width'],
                                                                                                               _XYCoordinates=_tmpXYCoordinates, _ElementName =_DesignParameter,)
                                                                                            )
                    del _tmpXYCoordinates
            elif _DesignParameterInDictionary[_DesignParameter]['_DesignParametertype'] == 3 and _DesignParameterInDictionary[_DesignParameter]['_DesignObj'] != None and _DesignParameterInDictionary[_DesignParameter]['_Ignore']==None:

                self._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=_DesignParameterInDictionary[_DesignParameter]['_DesignObj']._DesignParameter)
                #_DesignParameterInDictionary[_DesignParameter]['_DesignObj']._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=_DesignParameterInDictionary[_DesignParameter]['_DesignObj']._DesignParameter)

                _DesignParameterInDictionary['_GDSFile']['_GDSFile'] = _DesignParameterInDictionary['_GDSFile']['_GDSFile'] + _DesignParameterInDictionary[_DesignParameter]['_DesignObj']._DesignParameter['_GDSFile']['_GDSFile']

                for _XYCoordinate in _DesignParameterInDictionary[_DesignParameter]['_XYCoordinates']:
                    _DesignParameterInDictionary['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(
                                                                                            self._CreateGDSSrefElement(_SREFName=_DesignParameterInDictionary[_DesignParameter]['_DesignObj']._DesignParameter['_Name']['_Name'], _XYCoordinates=[_XYCoordinate], _Reflect=_DesignParameterInDictionary[_DesignParameter]['_Reflect'], _Angle=_DesignParameterInDictionary[_DesignParameter]['_Angle'])
                                                                                        )
            elif _DesignParameterInDictionary[_DesignParameter]['_DesignParametertype'] == 8:
                #print 'monitor for debug2: ', _DesignParameterInDictionary[_DesignParameter]['_XYCoordinates']
                for _XYCoordinate in _DesignParameterInDictionary[_DesignParameter]['_XYCoordinates']:
                    _DesignParameterInDictionary['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(
                                                                                                    self._CreateGDSTextElement(_Layer=_DesignParameterInDictionary[_DesignParameter]['_Layer'],
                                                                                                                               _Datatype=_DesignParameterInDictionary[_DesignParameter]['_Datatype'],
                                                                                                                               _Presentation = _DesignParameterInDictionary[_DesignParameter]['_Presentation'],
                                                                                                                               _Reflect=_DesignParameterInDictionary[_DesignParameter]['_Reflect'],
                                                                                                                               _XYCoordinates=[_XYCoordinate],
                                                                                                                               _Mag=_DesignParameterInDictionary[_DesignParameter]['_Mag'],
                                                                                                                               _Angle=_DesignParameterInDictionary[_DesignParameter]['_Angle'],
                                                                                                                               _TEXT=_DesignParameterInDictionary[_DesignParameter]['_TEXT'],
                                                                                                                               _ElementName=_DesignParameter
                                                                                                                               )
                                                                                                )
            elif _DesignParameterInDictionary[_DesignParameter]['_DesignParametertype'] == 6:
                for _tmpRail in _DesignParameterInDictionary[_DesignParameter]['_Rails']:
                    for _XYCoordinate in _tmpRail['_XYCoordinates']:
                        _DesignParameterInDictionary['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(
                                                                                            self._CreateGDSBoundaryElement(_Layer= _tmpRail['_Layer'], _Datatype=_tmpRail['_Datatype'],
                                                                                                                           _XYCoordinates=self.CenterCoordinateAndWidth2XYCoordinate( _XYCenter=_XYCoordinate,
                                                                                                                           _WidthX=_tmpRail['_XWidth'],
                                                                                                                           _WidthY=_tmpRail['_YWidth'],
                                                                                                                          _ElementName = _DesignParameter))
                                                                                            )
                for _tmpViaArray in _DesignParameterInDictionary[_DesignParameter]['_ViaArrays']:
                    _tmpViaArray['_DesignObj']._UpdateDesignParameter2GDSStructure()
                    #print 'testdisplay for debugging', _tmpViaArray, _tmpViaArray['_DesignObj']._DesignParameter['_GDSFile']['_GDSFile'], _tmpViaArray['_DesignObj']._DesignParameter['_Name']['_Name']

                    _DesignParameterInDictionary['_GDSFile']['_GDSFile'] = _DesignParameterInDictionary['_GDSFile']['_GDSFile'] + _tmpViaArray['_DesignObj']._DesignParameter['_GDSFile']['_GDSFile']

                    for _XYCoordinate in _tmpViaArray['_XYCoordinates']:
                        _DesignParameterInDictionary['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(
                                                                                                self._CreateGDSSrefElement(_SREFName=_tmpViaArray['_DesignObj']._DesignParameter['_Name']['_Name'], _XYCoordinates=[_XYCoordinate])
                                                                                            )

        print('#########################################################################################################')
        print('                                    {}  Update2GDS End                                    '.format(_DesignParameterInDictionary['_Name']['_Name']))
        print('#########################################################################################################')



    def _PathElementDeclaration(self,_Layer=None,_Datatype=None, _XYCoordinates=[],_Width=None , _ElementName=None,):
        #print 'display for debug: variable _XYCoordinates id ', id(_XYCoordinates)
        return dict(_DesignParametertype=2,_Layer=_Layer,_Datatype=_Datatype, _XYCoordinates=_XYCoordinates,_Width=_Width,  _Ignore=None, _ElementName = _ElementName)

    def _BoundaryElementDeclaration(self, _Layer=None,_Datatype=None, _XYCoordinates=[],_XWidth=None, _YWidth=None, _ElementName=None,):

        return dict(_DesignParametertype=1, _Layer=_Layer,_Datatype=_Datatype, _XYCoordinates=_XYCoordinates,_XWidth=_XWidth, _YWidth=_YWidth, _Ignore=None, _ElementName = _ElementName)

    def _PolygonElementDeclaration(self, _Layer=None,_Datatype=None, _XYCoordinates=[], _ElementName=None,):

        return dict(_DesignParametertype=11, _Layer=_Layer,_Datatype=_Datatype, _XYCoordinates=_XYCoordinates, _Ignore=None, _ElementName = _ElementName)

    def _SrefElementDeclaration(self, _DesignObj=None, _XYCoordinates=[], _Reflect=None, _Angle=None, _ElementName = None):

        return dict(_DesignParametertype=3,_DesignObj=_DesignObj, _XYCoordinates=_XYCoordinates, _Reflect=_Reflect, _Angle=_Angle, _Ignore=None, _ElementName = _ElementName),

    def _NameDeclaration(self,_Name= None ):

        return dict(_DesignParametertype=5,_Name=_Name)

    def _GDSObjDeclaration(self, _GDSFile = None):

        return dict(_DesignParametertype=4, _GDSFile=_GDSFile)
    def _TextElementDeclaration(self, _Layer=None,_Datatype=None, _Presentation = None, _Reflect=None, _XYCoordinates=[],  _Mag=None, _Angle=None,    _TEXT=None, _ElementName=None,):
        return  dict(_DesignParametertype=8, _Layer=_Layer,_Datatype=_Datatype, _Presentation = _Presentation, _Reflect=_Reflect, _XYCoordinates=_XYCoordinates,  _Mag=_Mag, _Angle=_Angle,   _TEXT=_TEXT, _ElementName=_ElementName)

    def _XYCoordinateInfoDeclaration(self,_XYCoordinateInfo=[] ):

        return dict(_DesignParametertype=7,_XYCoordinates=_XYCoordinateInfo)
    def _BitInfoDeclaraion(self, _BitNumber = None):
        return  dict(_DesignParametertype=7,_BitNumber = _BitNumber)

    def _SizeInfoDeclaraion(self, _DesignSizesInList = None):
        return  dict(_DesignParametertype=7,_DesignSizesInList = _DesignSizesInList)

    def _SupplyRailDeclaration(self, _HorizontalSupplyRailArea=[], _VerticalSupplyRailArea=[],  _ViaArrays = [], _Rails = [], _SupplyNodeName=None):
        return dict(_DesignParametertype=6, _HorizontalSupplyRailArea=_HorizontalSupplyRailArea, _VerticalSupplyRailArea=_VerticalSupplyRailArea,  _ViaArrays = _ViaArrays, _Rails =_Rails, _SupplyNodeName=_SupplyNodeName)