import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PyQTInterface import VisualizationItem
from PyCodes import EnvForClientSetUp
from PyCodes import userDefineExceptions
from PyCodes import ASTmodule
from PyQTInterface.layermap import LayerReader
from DesignManager.ElementManager import element_manager
import ast, astunparse
import pickle
import gzip
import json
import re
from gds_editor_ver3 import gds_stream


# import gds_editor_ver3.gds_structures
# import gds_editor_ver3.gds_tags
# import gds_editor_ver3.gds_record
# import gds_editor_ver3.gds_elements


class QtDesignParameter:
    def __init__(self, _id=None, _type=None, _ParentName=None, _ItemTraits=None,
                 _DesignParameterName=None):  # _ParentName: module name, _DesignParameterName: designParameter name
        self._id = _id
        self._type = _type  # boundary, path, sref, gdsObj
        self._ParentName = _ParentName
        if _DesignParameterName == None:
            self._DesignParameterName = _id
            print("There is no valid design parameter name")
        else:
            self._DesignParameterName = _DesignParameterName
        self._DesignParameter = None
        self._DesignHierarchy = None
        self._XYCoordinatesForDisplay = []
        self._NoShowFlag = None
        self._SimplifyFlag = None
        # self._XYCoordinateVariable = None
        # self._YWidthVariable = None
        # self._XWidthVariable = None
        # self._WidthVariable = None
        # self._DesignModuleLib = None
        ###self._VisualizationItemObj = VisualizationItem._VisualizationItem(_ItemTraits = _ItemTraits)

    def _createDesignParameter(self):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _createDesignConstrain Run.")
        _tmpDesignParameter = {"_id": self._id, "_DesignParametertype": self._type, }
        if self._type == 1:  # boundary
            _tmpDesignParameter["_Layer"] = None
            _tmpDesignParameter["_Datatype"] = None
            _tmpDesignParameter["_XYCoordinates"] = []
            _tmpDesignParameter["_XWidth"] = None
            _tmpDesignParameter["_YWidth"] = None
            _tmpDesignParameter["_Ignore"] = None
            _tmpDesignParameter["_ElementName"] = None
            _tmpDesignParameter["_DesignParametertype"] = 1
            _tmpDesignParameter["_DesignParameterName"] = self._DesignParameterName
        elif self._type == 2:  # path
            _tmpDesignParameter["_Layer"] = None
            _tmpDesignParameter["_Datatype"] = None
            _tmpDesignParameter["_XYCoordinates"] = []
            _tmpDesignParameter["_Width"] = None
            _tmpDesignParameter["_Ignore"] = None
            _tmpDesignParameter["_ElementName"] = None
            _tmpDesignParameter["_DesignParametertype"] = 2
            _tmpDesignParameter["_DesignParameterName"] = self._DesignParameterName
        elif self._type == 3:  # sref
            _tmpDesignParameter["_DesignObj"] = None  ####[libName, moduleName] ????
            _tmpDesignParameter["_DesignLibName"] = None  ####[libName, moduleName] ????
            _tmpDesignParameter[
                "_DesignModuleName"] = None  ###_ViaPoly2Met1OnPMOS = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnPMOSIn{}'.format(_Name)))[0],
            _tmpDesignParameter[
                "_XYCoordinates"] = []  ###$_DesignParameterName = self._SrefElementDeclaration(_DesignObj=$_DesignLibName.$_DesignModuleName(_DesignParameter=None, _Name=$_DesignObj))[0]
            _tmpDesignParameter["_Reflect"] = None
            _tmpDesignParameter["_Angle"] = None
            _tmpDesignParameter["_Ignore"] = None
            _tmpDesignParameter["_ElementName"] = None
            _tmpDesignParameter["_DesignParametertype"] = 3
            _tmpDesignParameter["_DesignParameterName"] = self._DesignParameterName
        elif self._type == 4:  # gds
            _tmpDesignParameter["_GDSFile"] = None
            _tmpDesignParameter["_DesignParametertype"] = 4
            _tmpDesignParameter["_DesignParameterName"] = self._DesignParameterName
        elif self._type == 5:  # gds
            _tmpDesignParameter["_Name"] = None
            _tmpDesignParameter["_DesignParametertype"] = 5
            _tmpDesignParameter["_DesignParameterName"] = self._DesignParameterName
        elif self._type == 8:  # text
            _tmpDesignParameter["_Layer"] = None
            # _tmpDesignParameter["_Datatype"] = None
            _tmpDesignParameter["_Presentation"] = None
            _tmpDesignParameter["_Reflect"] = None
            _tmpDesignParameter["_XYCoordinates"] = []
            _tmpDesignParameter["_Mag"] = None
            _tmpDesignParameter["_Angle"] = None
            _tmpDesignParameter["_TEXT"] = None
            _tmpDesignParameter["_Ignore"] = None
            _tmpDesignParameter["_ElementName"] = None
            _tmpDesignParameter["_DesignParametertype"] = 8
            _tmpDesignParameter["_DesignParameterName"] = self._DesignParameterName

            # def _TextElementDeclaration(self, _Layer=None, _Datatype=None, _Presentation=None, _Reflect=None,
            #                             _XYCoordinates=[], _Mag=None, _Angle=None, _TEXT=None, _ElementName=None, ):
            #     return dict(_DesignParametertype=8, _Layer=_Layer, _Datatype=_Datatype, _Presentation=_Presentation,
            #                 _Reflect=_Reflect, _XYCoordinates=_XYCoordinates, _Mag=_Mag, _Angle=_Angle, _TEXT=_TEXT,
            #                 _ElementName=_ElementName)
        # self._DesignParameter['_SEL1<{}>Pin'.format(i)] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0], \
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], \
        #     _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], \
        #     _Mag=0.1, _Angle=0, _TEXT='SEL1<{}>'.format(i), )
        self._DesignParameter = _tmpDesignParameter

    def _readDesignParameterValue(self, _index=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _setDesignParameterValue Run.")
        if self._DesignParameter == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                return self._DesignParameter[_index]
            except:
                return userDefineExceptions._UnkownError

    def _setDesignParameterValue(self, _index=None, _value=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _setDesignParameterValue Run.")
        if self._DesignParameter == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                self._DesignParameter[_index] = _value
            except:
                return userDefineExceptions._UnkownError

    ##################################################################################################
    # def _updateVisualItem(self):
    #     self._VisualizationItemObj.updateTraits(self._DesignParameter)
    def _setDesignParameterName(self, _DesignParameterName=None):
        self._DesignParameterName = _DesignParameterName

    # def _VisualItem(self):
    #     return self._VisualizationItemObj
    ######################################################################################################
    def __del__(self):
        pass


class QtDesinConstraint:
    def __init__(self, _id=None, _type=None, _ast=None):
        self._id = _id
        self._type = _type

        if _ast == None:
            self._ast = None
        else:
            self._ast = _ast
            self._ast._id = self._id
            self._ast._type = self._type

    def _createDesignConstraintSTMT(self, _stmt):
        # Type for Compound STMT
        if self._type == "Module":
            self._ast = ast.Module()
        elif self._type == "If":
            self._ast = ast.If()

        elif self._type == "While":
            self._ast = ast.While()

        elif self._type == "For":
            self._ast = ast.For()

        elif self._type == "Try":
            self._ast = ast.Try()

        elif self._type == "With":
            self._ast = ast.With()

        elif self._type == "FunctionDef":
            self._ast = ast.FunctionDef()

        elif self._type == "ClassDef":
            self._ast = ast.ClassDef()

        # Type for Simple STMT
        elif self._type == "Expression":
            self._ast = ast.Expression()
        elif self._type == "Assert":
            self._ast = ast.Assert()
        elif self._type == "Assign":
            self._ast = ast.Assign()
        elif self._type == "Pass":
            self._ast = ast.Pass()
        elif self._type == "Del":
            self._ast = ast.Del()
        elif self._type == "Return":
            self._ast = ast.Return()
        elif self._type == "Raise":
            self._ast = ast.Raise()
        elif self._type == "Break":
            self._ast = ast.Break()
        elif self._type == "Continue":
            self._ast = ast.Continue()
        elif self._type == "Import":
            self._ast = ast.Import()
        elif self._type == "ImportFrom":
            self._ast = ast.ImportFrom()
        elif self._type == "Name":
            self._ast = ast.Name()
        elif self._type == "Store":
            self._ast = ast.Store()
        elif self._type == "BinOp":
            self._ast = ast.BinOp()
        elif self._type == "Constant":
            self._ast = ast.Constant()
        elif self._type == "Sub":
            self._ast = ast.Sub()
        elif self._type == "Load":
            self._ast = ast.Load()
        elif self._type == "Num":
            self._ast = ast.Num()

        self._ast._id = self._id
        for field in self._ast._fields:
            if field in _stmt:
                if type(_stmt[field]) != list:
                    self._ast.__dict__[field] = _stmt[field]
            else:
                self._ast.__dict__[field] = None

    def _createDesignConstraint(self):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _createDesignConstrain Run.")

        # _tmpAST = {"_id": self._id, "_type": self._type, "_lineCodes": [], "_space": 0, "_tab": 0, }

        # Type for Compound STMT
        if self._type == "If":
            self._ast = ast.If()

        elif self._type == "While":
            self._ast = ast.While()

        elif self._type == "For":
            self._ast = ast.For()

        elif self._type == "Try":
            self._ast = ast.Try()

        elif self._type == "With":
            self._ast = ast.With()

        elif self._type == "FunctionDef":
            self._ast = ast.FunctionDef()

        elif self._type == "ClassDef":
            self._ast = ast.ClassDef()

        # Type for Simple STMT
        elif self._type == "Expression":
            self._ast = ast.Expression()
        elif self._type == "Assert":
            self._ast = ast.Assert()
        elif self._type == "Assign":
            self._ast = ast.Assign()
        elif self._type == "Pass":
            self._ast = ast.Pass()
        elif self._type == "Del":
            self._ast = ast.Del()
        elif self._type == "Return":
            self._ast = ast.Return()
        elif self._type == "Raise":
            self._ast = ast.Raise()
        elif self._type == "Break":
            self._ast = ast.Break()
        elif self._type == "Continue":
            self._ast = ast.Continue()
        elif self._type == "Import":
            self._ast = ast.Import()
        elif self._type == "ImportFrom":
            self._ast = ast.ImportFrom()

        self._ast._id = self._id

    def _readConstraintValueAsSTMT(self):
        _STMTlist = ASTmodule._convertPyCodeToSTMTlist(self._ast)
        return _STMTlist[0]

    def _readDesignConstraintValue(self, _index=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _setDesignConstraintValue Run.")
        if self._ParseTree == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                return self._ParseTree[_index]
            except:
                return userDefineExceptions._UnkownError

    # def _setDesignConstraintValueWithSTMT(self, _index = None, _value = None):
    #     if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
    #         print(self._id, " : _setDesignConstraintValue Run.")
    #     if self._ast == None:
    #         #raise userDefineExceptions.StatusError("_ParseTree has None value. use _createDesignConstrain to create _ParseTree.")
    #         return userDefineExceptions._InvalidInputError
    #     else:
    #         try:
    #             # self._ast[_index] = _value
    #             self._ast.__dict__[_index] = _value
    #         except:
    #             return userDefineExceptions._UnkownError
    def _setDesignConstraintValue(self, _index=None, _value=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _setDesignConstraintValue Run.")
        if self._ast == None:
            # raise userDefineExceptions.StatusError("_ParseTree has None value. use _createDesignConstrain to create _ParseTree.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                self._ast.__dict__[_index] = _value
            except:
                return userDefineExceptions._UnkownError

    # def _setDesignConstraintLink(self, _id=None, _type=None):
    #     pass
    # use _setDesignConstraintValue
    # variable Conversion is required
    # _findSubDesignConstraint
    def _appendDesignConstraintValue(self, _index=None, _value=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _setDesignConstraintValue Run.")
        if self._ast == None:
            # raise userDefineExceptions.StatusError("_ParseTree has None value. use _createDesignConstrain to create _ParseTree.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if _index in self._ast.__dict__:
                    if self._ast.__dict__[_index] == None:
                        self._ast.__dict__[_index] = [_value]
                    else:
                        if type(self._ast.__dict__[_index]) != list:
                            # if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
                            print(
                                'Warning. self._ast.{} = {} : which is not list format, but try to append deisgn constraint value'.format(
                                    _index, self._ast.__dict__[_index]))
                            self._ast.__dict__[_index] = [_value]
                        else:
                            self._ast.__dict__[_index].append(_value)
                else:
                    self._ast.__dict__[_index] = _value
            except:
                return userDefineExceptions._UnkownError

    # def _setDesignConstraintLink(self, _id=None, _type=None):
    #     pass
    # use _setDesignConstraintValue
    # variable Conversion is required
    # _findSubDesignConstraint

    def _findSubHierarchy(self, _MaxSearchDepth=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print(self._id, " : _findSubHierarchy Run.")

        if self._ParseTree == None:
            # raise userDefineExceptions.StatusError("_ParseTree has None value. use _createDesignConstrain to create _ParseTree.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpStack0 = [[self._ParseTree], ]
                _tmpStackPt0 = _tmpStack0[-1]
                _SearchDepthCounter = 0
                while True:
                    if (_MaxSearchDepth != None) and (_SearchDepthCounter >= _MaxSearchDepth):
                        break
                    _tmpStack1 = []
                    for element0 in _tmpStackPt0:
                        if type(element0) == type(dict()):
                            if "_id" in element0.keys():
                                for value in element0.values():
                                    if type(value) == type(list()):
                                        _tmpStack1 = _tmpStack1 + value
                    if not _tmpStack1:
                        break
                    else:
                        _tmpStack0.append(_tmpStack1)
                        _tmpStackPt0 = _tmpStack0[-1]
                        _SearchDepthCounter = _SearchDepthCounter + 1

                _tmpStack1 = []

                for element0 in _tmpStack0:
                    _tmpStack2 = []
                    for element1 in element0:
                        if (type(element1) == type(dict())):
                            if "_id" in element1:
                                _tmpStack2.append(element1["_id"])
                    _tmpStack1.append(_tmpStack2)

                return _tmpStack1
            except:
                return userDefineExceptions._UnkownError

    ###0
    ###1,2,3,4,5,
    ###        6
    ###        7a, 8b
    ###            9c
    ###            10,
    ###
    def __del__(self):
        pass


class QtProject:
    def __init__(self, _name="defaultProjectName", _LogMessageHandler=None):
        self._name = _name
        # self._idListForDesignParameter = dict() #### save assigned id
        # self._idListForDesignConstraint = dict()  #### save assigned id
        self._DesignParameter = dict()  ####module, runset, argument --> _DesignParameter
        self._DesignConstraint = dict()  ####module, runset, argument --> _DesignConstraint
        self._ParseTreeForDesignParameter = dict()
        self._ParseTreeForDesignConstrain = dict()  ####module, runset, argument --> _ParseTree
        self._LogMessageHandler = _LogMessageHandler
        self._ElementManager = element_manager.ElementManager()

        # designParameter Definition
        # self._DesignParameter["designParameterName"]  = dict(
        #     _ODLayer=dict(_id=0, _DesignParametertype=1, _Layer=None, _Datatype=1, _XYCoordinates=[], _XWidth=400,
        #                   _YWidth=400),
        #     # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
        #     _WELLBodyLayer=dict(_id=1, _DesignParametertype=1, _Layer=None, _Datatype=1, _XYCoordinates=[], _XWidth=400,
        #                         _YWidth=400),
        #     _Name=dict(_id=2, _DesignParametertype=5, _Name='NMOS'),
        #     _GDSFile=dict(_id=3, _DesignParametertype=4, _GDSFile=None),
        #     _Sref0=dict(_DesignParametertype=3, _DesignObj=None, _XYCoordinates=[], _Reflect=None, _Angle=None, _id=6,
        #                 _Ignore=None, _ElementName=dict(_id=7, _DesignParametertype=5, _Name='NMOS'), ),
        # )

    def _saveDesignConstraintAsPickle(self, _file=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_saveDesignConstraintAsPickle Run.")
        if _file == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                with gzip.open("{}.pickle".format(_file), 'wb') as f:
                    pickle.dump(self._DesignConstraint, f)
            except:
                return userDefineExceptions._UnkownError

    def _loadDesignConstraintAsPickle(self, _file=None, ):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_loadDesignConstraintAsPickle Run.")
        if _file == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                with gzip.open("{}".format(_file), 'rb') as f:
                    data = pickle.load(f)
                self._DesignConstraint = data
            except:
                return userDefineExceptions._UnkownError

    def _addDesignConstraintFromPickle(self, _file=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_addDesignConstraintFromPickle Run.")
        if _file == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                with gzip.open("{}".format(_file), 'rb') as f:
                    data = pickle.load(f)
                for element0 in data.keys():
                    if element0 in self._DesignConstraint.keys():
                        for element1 in data[element0]:
                            _tmpId = self._getDesignConstraintId(_ParentName=element0)
                            self._DesignConstraint[element0][element0 + str(_tmpId)] = data[element0][element1]
                    else:
                        self._DesignConstraint[element0] = data[element0]
                # self._DesignParameter = dict()  ####module, runset, argument --> _DesignParameter
                # self._DesignConstraint = dict()  ####module, runset, argument --> _DesignConstraint
                # self._ParseTreeForDesignParameter = dict()
                # self._ParseTreeForDesignConstrain = dict()  ####module, runset, argument --> _ParseTree

            except:
                return userDefineExceptions._UnkownError

    def _CopyDesignConstraint(self, _srcid=None, _srcParentName=None, _dstParentName=None, ):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_CopyDesignConstraint Run.")
        if _srcid == None or _srcParentName == None or _dstParentName == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if not _dstParentName in self._DesignConstraint.keys():
                    self._DesignConstraint[_dstParentName] = dict()
                _tmpId = self._getDesignConstraintId(_ParentName=_dstParentName)
                self._DesignConstraint[_dstParentName][_dstParentName + str(_tmpId)] = \
                self._DesignConstraint[_srcParentName][_srcid]

                # self._DesignParameter = dict()  ####module, runset, argument --> _DesignParameter
                # self._DesignConstraint = dict()  ####module, runset, argument --> _DesignConstraint
                # self._ParseTreeForDesignParameter = dict()
                # self._ParseTreeForDesignConstrain = dict()  ####module, runset, argument --> _ParseTree

            except:
                return userDefineExceptions._UnkownError

    def _setDesignConstraintValueWithSTMT(self, _module=None, _id=None, _STMT=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_setDesignConstraintValueWithSTMT Run.")
        if _module == None or _module == None or _STMT == None:
            # raise userDefineExceptions.StatusError("_ParseTree has None value. use _createDesignConstrain to create _ParseTree.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                del _STMT['_id']
                for key in _STMT:
                    _value = _STMT[key]
                    _updateList = []
                    # if type(_value) == list:            # this is option for add !!! Not for Set So caption!!
                    #     try:
                    #         _updateList = self._DesignConstraint[_module][_id][key]
                    #     except:
                    #         pass
                    #     for idVal in _value:
                    #         _updateList.append(idVal)
                    #     self._DesignConstraint[_module][_id]._setDesignConstraintValue(_index=key, _value=_updateList)
                    if type(_value) == list:
                        self._DesignConstraint[_module][_id]._setDesignConstraintValue(_index=key, _value=_value)
                    elif _value in self._DesignConstraint[_module][_id]:
                        _updateValue = self._DesignConstraint[_module][_id][_value]._ast
                        self._DesignConstraint[_module][_id]._setDesignConstraintValue(_index=key, _value=_updateValue)
                    else:
                        self._DesignConstraint[_module][_id]._setDesignConstraintValue(_index=key, _value=_value)
            except:
                return userDefineExceptions._UnkownError

    def _saveDesignParameterAsPickle(self, _file=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_saveDesignParameterAsPickle Run.")
        if _file == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                with gzip.open("{}.pickle".format(_file), 'wb') as f:
                    pickle.dump(self._DesignParameter, f)
            except:
                return userDefineExceptions._UnkownError

    def _loadDesignParameterAsPickle(self, _file=None, ):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_loadDesignConstraintAsPickle Run.")
        if _file == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                with gzip.open("{}".format(_file), 'rb') as f:
                    data = pickle.load(f)
                self._DesignParameter = data
            except:
                return userDefineExceptions._UnkownError

    def _addDesignParameterFromPickle(self, _file=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_addDesignConstraintFromPickle Run.")
        if _file == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                with gzip.open("{}".format(_file), 'rb') as f:
                    data = pickle.load(f)
                for element0 in data.keys():
                    if element0 in self._DesignParameter.keys():
                        for element1 in data[element0]:
                            _tmpId = self._getDesignParameterId(_ParentName=element0)
                            self._DesignParameter[element0][element0 + str(_tmpId)] = data[element0][element1]
                    else:
                        self._DesignParameter[element0] = data[element0]
                # self._DesignParameter = dict()  ####module, runset, argument --> _DesignParameter
                # self._DesignConstraint = dict()  ####module, runset, argument --> _DesignConstraint
                # self._ParseTreeForDesignParameter = dict()
                # self._ParseTreeForDesignConstrain = dict()  ####module, runset, argument --> _ParseTree

            except:
                return userDefineExceptions._UnkownError

    def _CopyDesignParameter(self, _srcid=None, _srcParentName=None, _dstParentName=None, ):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_CopyDesignConstraint Run.")
        if _srcid == None or _srcParentName == None or _dstParentName == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if not _dstParentName in self._DesignParameter.keys():
                    self._DesignParameter[_dstParentName] = dict()
                _tmpId = self._getDesignParameterId(_ParentName=_dstParentName)
                self._DesignParameter[_dstParentName][_dstParentName + str(_tmpId)] = \
                self._DesignParameter[_srcParentName][_srcid]

                # self._DesignParameter = dict()  ####module, runset, argument --> _DesignParameter
                # self._DesignConstraint = dict()  ####module, runset, argument --> _DesignConstraint
                # self._ParseTreeForDesignParameter = dict()
                # self._ParseTreeForDesignConstrain = dict()  ####module, runset, argument --> _ParseTree

            except:
                return userDefineExceptions._UnkownError

    def _XYCoordinate2MinMaxXY(self, _XYCoordinates=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_XYCoordinate2MinMaxXY Run.")
        if _XYCoordinates == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                x_list = []
                y_list = []
                for i in range(0, len(_XYCoordinates)):
                    x_list.append(_XYCoordinates[i][0])
                    y_list.append(_XYCoordinates[i][1])
                x_list = list(set(x_list))
                y_list = list(set(y_list))
                return x_list, y_list
            except:
                print(userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _MinMaxXY2XYCoordinate(self, _MinMaxXY=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_MinMaxXY2XYCoordinate Run.")
        if _MinMaxXY == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                x_list, y_list = _MinMaxXY
                # return [(min(x_list), min(y_list)), (max(x_list), min(y_list)), (max(x_list), max(y_list)), (min(x_list), max(y_list)), (min(x_list), min(y_list))]
                return [[min(x_list), min(y_list)], [max(x_list), min(y_list)], [max(x_list), max(y_list)],
                        [min(x_list), max(y_list)], [min(x_list), min(y_list)]]
            except:
                print(userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _XYCoordinate2CenterCoordinateAndWidth(self, _XYCoordinates=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_XYCoordinate2CenterCoordinateAndWidth Run.")
        if _XYCoordinates == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                x_list, y_list = self._XYCoordinate2MinMaxXY(_XYCoordinates)
                XYCenter = (float(min(x_list) + max(x_list)) / 2, float(min(y_list) + max(y_list)) / 2)
                WidthX = abs(min(x_list) - max(x_list))
                WidthY = abs(min(y_list) - max(y_list))
                # del x_list, y_list
                return XYCenter, WidthX, WidthY
            except:
                print(userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _CenterCoordinateAndWidth2XYCoordinate(self, _XYCenter=None, _WidthX=None, _WidthY=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_CenterCoordinateAndWidth2XYCoordinate Run.")
        if _XYCenter == None or _WidthX == None or _WidthY == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                x_list = [_XYCenter[0] - float(_WidthX) / 2, _XYCenter[0] + float(_WidthX) / 2]
                y_list = [_XYCenter[1] - float(_WidthY) / 2, _XYCenter[1] + float(_WidthY) / 2]
                return self._MinMaxXY2XYCoordinate([x_list, y_list])
            except:
                print(userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _loadDesignsFromGDS(self, _file=None, _topModuleName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_loadDesignsFromGDS Run.")
        if _file == None or _topModuleName == None:
            return userDefineExceptions._InvalidInputError
        else:
            dp_dict_list = []

            try:
                _GDSStreamObj = gds_stream.GDS_STREAM()
                with open("{}".format(_file), 'rb') as f:
                    _GDSStreamObj.read_binary_gds_stream(gds_file=f)
                for _tmpStructure in _GDSStreamObj._STRUCTURES:
                    # _tmpStructureName = _tmpStructure._STRNAME.strname.split('\x00', 1)[0]
                    _tmpStructureName = _tmpStructure._STRNAME.strname.decode()
                    if '\x00' in _tmpStructureName:
                        _tmpStructureName = _tmpStructureName.split('\x00', 1)[0]
                    # _tmpStructureName = _tmpStructure._STRNAME.strname
                    # print('monitor for decode in _loadDesignsFromGDS ', _tmpStructureName)
                    # print('monitor for dubug: ', _tmpStructureName)
                    layernum2name = LayerReader._LayerNumber2CommonLayerName(LayerReader._LayerMapping)

                    for _tmpElement in _tmpStructure._ELEMENTS:
                        _tmpId = self._getDesignParameterId(_ParentName=_tmpStructureName)
                        _tmpId = _tmpStructureName + str(_tmpId)
                        if "_BOUNDARY" in vars(_tmpElement._ELEMENTS):
                            dp_dict = dict(
                                _Layer=None,
                                _DesignParametertype=1,
                                _XYCoordinates=[],
                                _XWidth=None,
                                _YWidth=None,
                                _Ignore=None,
                                _DesignParameterName=None
                            )

                            _XYCenter, _XWidth, _YWidth = self._XYCoordinate2CenterCoordinateAndWidth(
                                _tmpElement._ELEMENTS._XY.xy)
                            tmp_layer_name = layernum2name[str(_tmpElement._ELEMENTS._LAYER.layer)]
                            dp_dict['_Layer'] = tmp_layer_name
                            dp_dict['_DesignParametertype'] = 1
                            dp_dict['_XYCoordinates'].append([_XYCenter[0], _XYCenter[1]])
                            dp_dict['_XWidth'] = _XWidth
                            dp_dict['_YWidth'] = _YWidth

                            dp_dict['_DesignParameterName'] = _tmpId

                            dp_dict_list.append(dp_dict)
                            print(dp_dict)
                            print(dp_dict_list)
                        #     self._createNewDesignParameter(_id=_tmpId, _type=1, _ParentName=_tmpStructureName)
                        #     self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                        #         "_Layer"] = _tmpElement._ELEMENTS._LAYER.layer
                        #     self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                        #         "_Datatype"] = _tmpElement._ELEMENTS._DATATYPE.datatype
                        #     self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_XYCoordinates"].append(
                        #         [_XYCenter[0], _XYCenter[1]])
                        #     self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_XWidth"] = _XWidth
                        #     self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_YWidth"] = _YWidth
                            # self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Ignore"]
                            # self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_ElementName"]
                        elif "_PATH" in vars(_tmpElement._ELEMENTS):
                            self._createNewDesignParameter(_id=_tmpId, _type=2, _ParentName=_tmpStructureName)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Layer"] = _tmpElement._ELEMENTS._LAYER.layer
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Datatype"] = _tmpElement._ELEMENTS._DATATYPE.datatype
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_XYCoordinates"].append(
                                _tmpElement._ELEMENTS._XY.xy)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Width"] = _tmpElement._ELEMENTS._WIDTH.width
                        elif "_SREF" in vars(_tmpElement._ELEMENTS):
                            self._createNewDesignParameter(_id=_tmpId, _type=3, _ParentName=_tmpStructureName)
                            # print('     monitor for debug: ', _tmpElement._ELEMENTS._SNAME.sname.decode())
                            # print('     monitor for debug: ', _tmpElement._ELEMENTS._XY)
                            _tmpSname = _tmpElement._ELEMENTS._SNAME.sname.decode()
                            if '\x00' in _tmpSname:
                                _tmpSname = _tmpSname.split('\x00', 1)[0]
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_DesignObj"] = _tmpSname
                            for _tmpXYCoordinate in _tmpElement._ELEMENTS._XY.xy:
                                self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                    "_XYCoordinates"].append(_tmpXYCoordinate)
                            if _tmpElement._ELEMENTS._STRANS != None:
                                if _tmpElement._ELEMENTS._STRANS._STRANS != None:
                                    self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Reflect"] = [
                                        _tmpElement._ELEMENTS._STRANS._STRANS.reflection,
                                        _tmpElement._ELEMENTS._STRANS._STRANS.abs_mag,
                                        _tmpElement._ELEMENTS._STRANS._STRANS.abs_angle]
                                if _tmpElement._ELEMENTS._STRANS._ANGLE != None:
                                    self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                        "_Angle"] = _tmpElement._ELEMENTS._STRANS._ANGLE.angle
                        elif "_TEXT" in vars(_tmpElement._ELEMENTS):
                            self._createNewDesignParameter(_id=_tmpId, _type=8, _ParentName=_tmpStructureName)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Layer"] = _tmpElement._ELEMENTS._LAYER.layer
                            for _tmpXYCoordinate in _tmpElement._ELEMENTS._TEXTBODY._XY.xy:
                                self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                    "_XYCoordinates"].append(_tmpXYCoordinate)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Presentation"] = [
                                _tmpElement._ELEMENTS._TEXTBODY._PRESENTATION.font,
                                _tmpElement._ELEMENTS._TEXTBODY._PRESENTATION.vertical_presentation,
                                _tmpElement._ELEMENTS._TEXTBODY._PRESENTATION.horizontal_presentation]
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Reflect"] = [
                                _tmpElement._ELEMENTS._TEXTBODY._STRANS._STRANS.reflection,
                                _tmpElement._ELEMENTS._TEXTBODY._STRANS._STRANS.abs_mag,
                                _tmpElement._ELEMENTS._TEXTBODY._STRANS._STRANS.abs_angle]
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Mag"] = _tmpElement._ELEMENTS._TEXTBODY._STRANS._MAG.mag
                            # self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Angle"] = _tmpElement._ELEMENTS._TEXTBODY._STRANS._ANGLE.angle
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_TEXT"] = _tmpElement._ELEMENTS._TEXTBODY._STRING.string_data

                            # print(vars(_tmpElement._ELEMENTS))
                # print(self._DesignParameter)
            except:
                print(userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

            return dp_dict_list

    def _loadDesignsFromGDSlegacy(self, _file=None, _topModuleName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_loadDesignsFromGDS Run.")
        if _file == None or _topModuleName == None:
            return userDefineExceptions._InvalidInputError
        else:

            try:
                _GDSStreamObj = gds_stream.GDS_STREAM()
                with open("{}".format(_file), 'rb') as f:
                    _GDSStreamObj.read_binary_gds_stream(gds_file=f)
                for _tmpStructure in _GDSStreamObj._STRUCTURES:
                    # _tmpStructureName = _tmpStructure._STRNAME.strname.split('\x00', 1)[0]
                    _tmpStructureName = _tmpStructure._STRNAME.strname.decode()
                    if '\x00' in _tmpStructureName:
                        _tmpStructureName = _tmpStructureName.split('\x00', 1)[0]
                    # _tmpStructureName = _tmpStructure._STRNAME.strname
                    # print('monitor for decode in _loadDesignsFromGDS ', _tmpStructureName)
                    # print('monitor for dubug: ', _tmpStructureName)

                    for _tmpElement in _tmpStructure._ELEMENTS:
                        _tmpId = self._getDesignParameterId(_ParentName=_tmpStructureName)
                        _tmpId = _tmpStructureName + str(_tmpId)
                        if "_BOUNDARY" in vars(_tmpElement._ELEMENTS):
                            self._createNewDesignParameter(_id=_tmpId, _type=1, _ParentName=_tmpStructureName)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Layer"] = _tmpElement._ELEMENTS._LAYER.layer
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Datatype"] = _tmpElement._ELEMENTS._DATATYPE.datatype
                            _XYCenter, _XWidth, _YWidth = self._XYCoordinate2CenterCoordinateAndWidth(
                                _tmpElement._ELEMENTS._XY.xy)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_XYCoordinates"].append(
                                [_XYCenter[0], _XYCenter[1]])
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_XWidth"] = _XWidth
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_YWidth"] = _YWidth
                            # self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Ignore"]
                            # self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_ElementName"]
                        elif "_PATH" in vars(_tmpElement._ELEMENTS):
                            self._createNewDesignParameter(_id=_tmpId, _type=2, _ParentName=_tmpStructureName)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Layer"] = _tmpElement._ELEMENTS._LAYER.layer
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Datatype"] = _tmpElement._ELEMENTS._DATATYPE.datatype
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_XYCoordinates"].append(
                                _tmpElement._ELEMENTS._XY.xy)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Width"] = _tmpElement._ELEMENTS._WIDTH.width
                        elif "_SREF" in vars(_tmpElement._ELEMENTS):
                            self._createNewDesignParameter(_id=_tmpId, _type=3, _ParentName=_tmpStructureName)
                            # print('     monitor for debug: ', _tmpElement._ELEMENTS._SNAME.sname.decode())
                            # print('     monitor for debug: ', _tmpElement._ELEMENTS._XY)
                            _tmpSname = _tmpElement._ELEMENTS._SNAME.sname.decode()
                            if '\x00' in _tmpSname:
                                _tmpSname = _tmpSname.split('\x00', 1)[0]
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_DesignObj"] = _tmpSname
                            for _tmpXYCoordinate in _tmpElement._ELEMENTS._XY.xy:
                                self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                    "_XYCoordinates"].append(_tmpXYCoordinate)
                            if _tmpElement._ELEMENTS._STRANS != None:
                                if _tmpElement._ELEMENTS._STRANS._STRANS != None:
                                    self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Reflect"] = [
                                        _tmpElement._ELEMENTS._STRANS._STRANS.reflection,
                                        _tmpElement._ELEMENTS._STRANS._STRANS.abs_mag,
                                        _tmpElement._ELEMENTS._STRANS._STRANS.abs_angle]
                                if _tmpElement._ELEMENTS._STRANS._ANGLE != None:
                                    self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                        "_Angle"] = _tmpElement._ELEMENTS._STRANS._ANGLE.angle
                        elif "_TEXT" in vars(_tmpElement._ELEMENTS):
                            self._createNewDesignParameter(_id=_tmpId, _type=8, _ParentName=_tmpStructureName)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Layer"] = _tmpElement._ELEMENTS._LAYER.layer
                            for _tmpXYCoordinate in _tmpElement._ELEMENTS._TEXTBODY._XY.xy:
                                self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                    "_XYCoordinates"].append(_tmpXYCoordinate)
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Presentation"] = [
                                _tmpElement._ELEMENTS._TEXTBODY._PRESENTATION.font,
                                _tmpElement._ELEMENTS._TEXTBODY._PRESENTATION.vertical_presentation,
                                _tmpElement._ELEMENTS._TEXTBODY._PRESENTATION.horizontal_presentation]
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Reflect"] = [
                                _tmpElement._ELEMENTS._TEXTBODY._STRANS._STRANS.reflection,
                                _tmpElement._ELEMENTS._TEXTBODY._STRANS._STRANS.abs_mag,
                                _tmpElement._ELEMENTS._TEXTBODY._STRANS._STRANS.abs_angle]
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_Mag"] = _tmpElement._ELEMENTS._TEXTBODY._STRANS._MAG.mag
                            # self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter["_Angle"] = _tmpElement._ELEMENTS._TEXTBODY._STRANS._ANGLE.angle
                            self._DesignParameter[_tmpStructureName][_tmpId]._DesignParameter[
                                "_TEXT"] = _tmpElement._ELEMENTS._TEXTBODY._STRING.string_data

                            # print(vars(_tmpElement._ELEMENTS))
                # print(self._DesignParameter)
            except:
                print(userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _loadConstraintsFromPySource(self, _file=None, _topModuleName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_loadDesignsFromGDS Run.")
        if _file == None or _topModuleName == None:
            return userDefineExceptions._InvalidInputError
        else:

            try:
                with open("{}".format(_file), 'r') as f:
                    # TopAST = ast.parse(f.read())
                    _STMTlist, _ids = self._createNewDesignConstraintAST(_ASTDtype='pyCode', _pyCode=f.read(),
                                                                         _ParentName=_topModuleName)
                return _STMTlist, _ids
            except:
                print(userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _resetXYCoordinatesForDisplay(self):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_UpdateXYCoordinateForDisplay Run.")
        try:
            for element0 in self._DesignParameter.keys():
                for element1 in self._DesignParameter[element0].keys():
                    self._DesignParameter[element0][element1]._XYCoordinatesForDisplay = []
        except:
            print(userDefineExceptions._UnkownError)
            return userDefineExceptions._UnkownError

    def _UpdateXYCoordinatesForDisplay(self, _ParentName=None, _Offset=[0, 0], _Transpose=[[1, 0], [0, 1]]):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_UpdateXYCoordinateForDisplay Run.")
        if _ParentName == None:
            return userDefineExceptions._InvalidInputError
        else:

            try:
                for _tmpId in self._DesignParameter[_ParentName]:
                    if self._DesignParameter[_ParentName][_tmpId]._type == 1:
                        # print('monitor for debug in _UpdateXYCoordinatesForDisplay 1')
                        _tmpResult0 = []
                        for _tmpXYCoordinate in self._DesignParameter[_ParentName][_tmpId]._DesignParameter[
                            "_XYCoordinates"]:
                            _tmpXYCoordinateConverted = self._CenterCoordinateAndWidth2XYCoordinate(
                                _XYCenter=_tmpXYCoordinate,
                                _WidthX=self._DesignParameter[_ParentName][_tmpId]._DesignParameter["_XWidth"],
                                _WidthY=self._DesignParameter[_ParentName][_tmpId]._DesignParameter["_YWidth"])
                            _tmpResult1 = []
                            for _tmpXYCoordinate0 in _tmpXYCoordinateConverted:
                                _tmpX0 = _tmpXYCoordinate0[0]
                                _tmpY0 = _tmpXYCoordinate0[1]
                                _tmpX1 = _Transpose[0][0] * _tmpX0 + _Transpose[0][1] * _tmpY0 + _Offset[0]
                                _tmpY1 = _Transpose[1][0] * _tmpX0 + _Transpose[1][1] * _tmpY0 + _Offset[1]
                                _tmpResult1.append([_tmpX1, _tmpY1])
                            _tmpResult0.append(_tmpResult1)
                        self._DesignParameter[_ParentName][_tmpId]._XYCoordinatesForDisplay = \
                        self._DesignParameter[_ParentName][_tmpId]._XYCoordinatesForDisplay + _tmpResult0
                        self._ConvertBoundaryXYExpression(_id=_tmpId, _ParentName=_ParentName)
                    elif self._DesignParameter[_ParentName][_tmpId]._type == 2:
                        # print('monitor for debug in _UpdateXYCoordinatesForDisplay 2')
                        _tmpResult0 = []
                        for _tmpXYCoordinate in self._DesignParameter[_ParentName][_tmpId]._DesignParameter[
                            "_XYCoordinates"]:
                            _tmpResult1 = []
                            for _tmpXYCoordinate0 in _tmpXYCoordinate:
                                _tmpX0 = _tmpXYCoordinate0[0]
                                _tmpY0 = _tmpXYCoordinate0[1]
                                _tmpX1 = _Transpose[0][0] * _tmpX0 + _Transpose[0][1] * _tmpY0 + _Offset[0]
                                _tmpY1 = _Transpose[1][0] * _tmpX0 + _Transpose[1][1] * _tmpY0 + _Offset[1]
                                _tmpResult1.append([_tmpX1, _tmpY1])
                            _tmpResult0.append(_tmpResult1)
                        self._DesignParameter[_ParentName][_tmpId]._XYCoordinatesForDisplay = \
                        self._DesignParameter[_ParentName][_tmpId]._XYCoordinatesForDisplay + _tmpResult0
                    elif self._DesignParameter[_ParentName][_tmpId]._type == 3:
                        # print('monitor for debug in _UpdateXYCoordinatesForDisplay 3')

                        for _tmpXYCoordinate in self._DesignParameter[_ParentName][_tmpId]._DesignParameter[
                            "_XYCoordinates"]:
                            _tmpX0 = _tmpXYCoordinate[0]
                            _tmpY0 = _tmpXYCoordinate[1]
                            _tmpX1 = _Transpose[0][0] * _tmpX0 + _Transpose[0][1] * _tmpY0
                            _tmpY1 = _Transpose[1][0] * _tmpX0 + _Transpose[1][1] * _tmpY0
                            _tmpX2 = _tmpX1 + _Offset[0]
                            _tmpY2 = _tmpY1 + _Offset[1]
                            _tmpNoReflect = [[1, 0], [0, 1]]
                            _tmpReflectOnX = [[1, 0], [0, -1]]
                            _tmpRotate0 = [[1, 0], [0, 1]]
                            _tmpRotate90 = [[0, -1], [1, 0]]
                            _tmpRotate180 = [[-1, 0], [0, -1]]
                            _tmpRotate270 = [[0, 1], [-1, 0]]
                            if self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Reflect'] == None or \
                                    self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Reflect'][0] == 0:
                                if self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == None or \
                                        self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 0:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate0[0][0] + _Transpose[0][1] * _tmpRotate0[1][
                                        0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate0[0][1] + _Transpose[0][1] * _tmpRotate0[1][
                                        1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate0[0][0] + _Transpose[1][1] * _tmpRotate0[1][
                                        0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate0[0][1] + _Transpose[1][1] * _tmpRotate0[1][
                                        1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpNoReflect[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpNoReflect[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpNoReflect[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpNoReflect[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 90:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate90[0][0] + _Transpose[0][1] * \
                                              _tmpRotate90[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate90[0][1] + _Transpose[0][1] * \
                                              _tmpRotate90[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate90[0][0] + _Transpose[1][1] * \
                                              _tmpRotate90[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate90[0][1] + _Transpose[1][1] * \
                                              _tmpRotate90[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpNoReflect[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpNoReflect[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpNoReflect[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpNoReflect[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 180:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate180[0][0] + _Transpose[0][1] * \
                                              _tmpRotate180[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate180[0][1] + _Transpose[0][1] * \
                                              _tmpRotate180[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate180[0][0] + _Transpose[1][1] * \
                                              _tmpRotate180[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate180[0][1] + _Transpose[1][1] * \
                                              _tmpRotate180[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpNoReflect[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpNoReflect[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpNoReflect[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpNoReflect[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 270:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate270[0][0] + _Transpose[0][1] * \
                                              _tmpRotate270[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate270[0][1] + _Transpose[0][1] * \
                                              _tmpRotate270[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate270[0][0] + _Transpose[1][1] * \
                                              _tmpRotate270[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate270[0][1] + _Transpose[1][1] * \
                                              _tmpRotate270[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpNoReflect[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpNoReflect[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpNoReflect[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpNoReflect[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                            elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Reflect'][0] == 1:
                                if self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == None or \
                                        self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 0:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate0[0][0] + _Transpose[0][1] * _tmpRotate0[1][
                                        0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate0[0][1] + _Transpose[0][1] * _tmpRotate0[1][
                                        1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate0[0][0] + _Transpose[1][1] * _tmpRotate0[1][
                                        0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate0[0][1] + _Transpose[1][1] * _tmpRotate0[1][
                                        1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 90:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate90[0][0] + _Transpose[0][1] * \
                                              _tmpRotate90[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate90[0][1] + _Transpose[0][1] * \
                                              _tmpRotate90[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate90[0][0] + _Transpose[1][1] * \
                                              _tmpRotate90[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate90[0][1] + _Transpose[1][1] * \
                                              _tmpRotate90[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 180:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate180[0][0] + _Transpose[0][1] * \
                                              _tmpRotate180[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate180[0][1] + _Transpose[0][1] * \
                                              _tmpRotate180[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate180[0][0] + _Transpose[1][1] * \
                                              _tmpRotate180[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate180[0][1] + _Transpose[1][1] * \
                                              _tmpRotate180[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 270:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate270[0][0] + _Transpose[0][1] * \
                                              _tmpRotate270[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate270[0][1] + _Transpose[0][1] * \
                                              _tmpRotate270[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate270[0][0] + _Transpose[1][1] * \
                                              _tmpRotate270[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate270[0][1] + _Transpose[1][1] * \
                                              _tmpRotate270[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                            self._UpdateXYCoordinatesForDisplay(
                                _ParentName=self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_DesignObj'],
                                _Offset=[_tmpX2, _tmpY2], _Transpose=_tmpTranspose1)
                    elif self._DesignParameter[_ParentName][_tmpId]._type == 8:
                        # print('monitor for debug in _UpdateXYCoordinatesForDisplay 8')
                        _tmpResult0 = []
                        for _tmpXYCoordinate in self._DesignParameter[_ParentName][_tmpId]._DesignParameter[
                            "_XYCoordinates"]:
                            _tmpX0 = _tmpXYCoordinate[0]
                            _tmpY0 = _tmpXYCoordinate[1]
                            _tmpNoReflect = [[1, 0], [0, 1]]
                            _tmpReflectOnX = [[1, 0], [0, -1]]
                            _tmpRotate0 = [[1, 0], [0, 1]]
                            _tmpRotate90 = [[0, -1], [1, 0]]
                            _tmpRotate180 = [[-1, 0], [0, -1]]
                            _tmpRotate270 = [[0, 1], [-1, 0]]
                            if self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Reflect'] == None or \
                                    self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Reflect'][0] == 0:
                                if self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == None or \
                                        self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 0:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate0[0][0] + _Transpose[0][1] * _tmpRotate0[1][
                                        0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate0[0][1] + _Transpose[0][1] * _tmpRotate0[1][
                                        1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate0[0][0] + _Transpose[1][1] * _tmpRotate0[1][
                                        0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate0[0][1] + _Transpose[1][1] * _tmpRotate0[1][
                                        1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpNoReflect[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpNoReflect[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpNoReflect[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpNoReflect[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 90:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate90[0][0] + _Transpose[0][1] * \
                                              _tmpRotate90[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate90[0][1] + _Transpose[0][1] * \
                                              _tmpRotate90[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate90[0][0] + _Transpose[1][1] * \
                                              _tmpRotate90[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate90[0][1] + _Transpose[1][1] * \
                                              _tmpRotate90[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpNoReflect[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpNoReflect[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpNoReflect[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpNoReflect[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 180:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate180[0][0] + _Transpose[0][1] * \
                                              _tmpRotate180[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate180[0][1] + _Transpose[0][1] * \
                                              _tmpRotate180[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate180[0][0] + _Transpose[1][1] * \
                                              _tmpRotate180[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate180[0][1] + _Transpose[1][1] * \
                                              _tmpRotate180[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpNoReflect[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpNoReflect[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpNoReflect[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpNoReflect[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 270:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate270[0][0] + _Transpose[0][1] * \
                                              _tmpRotate270[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate270[0][1] + _Transpose[0][1] * \
                                              _tmpRotate270[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate270[0][0] + _Transpose[1][1] * \
                                              _tmpRotate270[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate270[0][1] + _Transpose[1][1] * \
                                              _tmpRotate270[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpNoReflect[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpNoReflect[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpNoReflect[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpNoReflect[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                            elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Reflect'][0] == 1:
                                if self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == None or \
                                        self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 0:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate0[0][0] + _Transpose[0][1] * _tmpRotate0[1][
                                        0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate0[0][1] + _Transpose[0][1] * _tmpRotate0[1][
                                        1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate0[0][0] + _Transpose[1][1] * _tmpRotate0[1][
                                        0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate0[0][1] + _Transpose[1][1] * _tmpRotate0[1][
                                        1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 90:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate90[0][0] + _Transpose[0][1] * \
                                              _tmpRotate90[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate90[0][1] + _Transpose[0][1] * \
                                              _tmpRotate90[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate90[0][0] + _Transpose[1][1] * \
                                              _tmpRotate90[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate90[0][1] + _Transpose[1][1] * \
                                              _tmpRotate90[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 180:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate180[0][0] + _Transpose[0][1] * \
                                              _tmpRotate180[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate180[0][1] + _Transpose[0][1] * \
                                              _tmpRotate180[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate180[0][0] + _Transpose[1][1] * \
                                              _tmpRotate180[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate180[0][1] + _Transpose[1][1] * \
                                              _tmpRotate180[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                                elif self._DesignParameter[_ParentName][_tmpId]._DesignParameter['_Angle'] == 270:
                                    _tmp000 = _Transpose[0][0] * _tmpRotate270[0][0] + _Transpose[0][1] * \
                                              _tmpRotate270[1][0]
                                    _tmp001 = _Transpose[0][0] * _tmpRotate270[0][1] + _Transpose[0][1] * \
                                              _tmpRotate270[1][1]
                                    _tmp010 = _Transpose[1][0] * _tmpRotate270[0][0] + _Transpose[1][1] * \
                                              _tmpRotate270[1][0]
                                    _tmp011 = _Transpose[1][0] * _tmpRotate270[0][1] + _Transpose[1][1] * \
                                              _tmpRotate270[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmp100 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp101 = _tmpTranspose0[0][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[0][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmp110 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][0] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][0]
                                    _tmp111 = _tmpTranspose0[1][0] * _tmpReflectOnX[0][1] + _tmpTranspose0[1][1] * \
                                              _tmpReflectOnX[1][1]
                                    _tmpTranspose1 = [[_tmp100, _tmp101], [_tmp110, _tmp111]]
                            _tmpX1 = _tmpTranspose1[0][0] * _tmpX0 + _tmpTranspose1[0][1] * _tmpY0 + _Offset[0]
                            _tmpY1 = _tmpTranspose1[1][0] * _tmpX0 + _tmpTranspose1[1][1] * _tmpY0 + _Offset[1]
                            _tmpResult0.append([_tmpX1, _tmpY1])
                        self._DesignParameter[_ParentName][_tmpId]._XYCoordinatesForDisplay = \
                        self._DesignParameter[_ParentName][_tmpId]._XYCoordinatesForDisplay + _tmpResult0
            except:
                print(userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _UpdateXYCoordinateForDisplay(self, _id=None, _ParentName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_UpdateXYCoordinateForDisplay Run.")
        if _id == None or _ParentName == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpStackForHierarchy = self._HierarchyFromRootForDesignParameter(_id=_id, _ParentName=_ParentName)
                print('monitor for debug in _UpdateXYCoordinateForDisplay0 ', _tmpStackForHierarchy)
                # (XYCoordinate, ) _Reflect  _Angle
                ###############1. [ [[x0y0,T0]], [[x1y1,T1]], [[x2y2,T2]] ] [offset, transposeMatrix]
                ###############2. [ [x0y0 + T0[x1y1], T0T1], [[x2y2,T2]]]
                ###############3. [ [x0y0 + T0[x1y1] + T0T1[x2y2] , T0T1T2]]
                _tmpNoReflect = [[1, 0], [0, 1]]
                _tmpReflectOnX = [[1, 0], [0, -1]]
                _tmpRotate0 = [[1, 0], [0, 1]]
                _tmpRotate90 = [[0, -1], [1, 0]]
                _tmpRotate180 = [[-1, 0], [0, -1]]
                _tmpRotate270 = [[0, 1], [-1, 0]]

                _tmpStackForXYCoordinateForDisplay = []
                for element0 in _tmpStackForHierarchy:
                    _tmpStackForOffsetAndTransition = []
                    for element0Parent in element0.keys():  ###
                        for element0Id in element0[element0Parent]:
                            if self._DesignParameter[element0Parent][element0Id]._type == 1:
                                for _tmpXYCoordinate in \
                                self._DesignParameter[element0Parent][element0Id]._DesignParameter["_XYCoordinates"]:
                                    _tmp000 = _tmpRotate0[0][0] * _tmpNoReflect[0][0] + _tmpRotate0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp001 = _tmpRotate0[0][0] * _tmpNoReflect[0][1] + _tmpRotate0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp010 = _tmpRotate0[1][0] * _tmpNoReflect[0][0] + _tmpRotate0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp011 = _tmpRotate0[1][0] * _tmpNoReflect[0][1] + _tmpRotate0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmpXYCoordinateConverted = self._CenterCoordinateAndWidth2XYCoordinate(
                                        _XYCenter=_tmpXYCoordinate,
                                        _WidthX=self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            "_XWidth"],
                                        _WidthY=self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            "_YWidth"])
                                    _tmpStackForOffsetAndTransition.append([_tmpXYCoordinateConverted, _tmpTranspose0,
                                                                            self._DesignParameter[element0Parent][
                                                                                element0Id]._type])
                            elif self._DesignParameter[element0Parent][element0Id]._type == 2:
                                for _tmpXYCoordinates in \
                                self._DesignParameter[element0Parent][element0Id]._DesignParameter["_XYCoordinates"]:
                                    _tmp000 = _tmpRotate0[0][0] * _tmpNoReflect[0][0] + _tmpRotate0[0][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp001 = _tmpRotate0[0][0] * _tmpNoReflect[0][1] + _tmpRotate0[0][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmp010 = _tmpRotate0[1][0] * _tmpNoReflect[0][0] + _tmpRotate0[1][1] * \
                                              _tmpNoReflect[1][0]
                                    _tmp011 = _tmpRotate0[1][0] * _tmpNoReflect[0][1] + _tmpRotate0[1][1] * \
                                              _tmpNoReflect[1][1]
                                    _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmpStackForOffsetAndTransition.append([_tmpXYCoordinates, _tmpTranspose0,
                                                                            self._DesignParameter[element0Parent][
                                                                                element0Id]._type])
                            elif self._DesignParameter[element0Parent][element0Id]._type == 3:
                                for _tmpXYCoordinate in \
                                self._DesignParameter[element0Parent][element0Id]._DesignParameter["_XYCoordinates"]:
                                    if self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                        '_Reflect'] == None or \
                                            self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                                '_Reflect'][0] == 0:
                                        if self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == None or \
                                                self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                                    '_Angle'] == 0:
                                            _tmp000 = _tmpRotate0[0][0] * _tmpNoReflect[0][0] + _tmpRotate0[0][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp001 = _tmpRotate0[0][0] * _tmpNoReflect[0][1] + _tmpRotate0[0][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmp010 = _tmpRotate0[1][0] * _tmpNoReflect[0][0] + _tmpRotate0[1][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp011 = _tmpRotate0[1][0] * _tmpNoReflect[0][1] + _tmpRotate0[1][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 90:
                                            _tmp000 = _tmpRotate90[0][0] * _tmpNoReflect[0][0] + _tmpRotate90[0][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp001 = _tmpRotate90[0][0] * _tmpNoReflect[0][1] + _tmpRotate90[0][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmp010 = _tmpRotate90[1][0] * _tmpNoReflect[0][0] + _tmpRotate90[1][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp011 = _tmpRotate90[1][0] * _tmpNoReflect[0][1] + _tmpRotate90[1][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 180:
                                            _tmp000 = _tmpRotate180[0][0] * _tmpNoReflect[0][0] + _tmpRotate180[0][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp001 = _tmpRotate180[0][0] * _tmpNoReflect[0][1] + _tmpRotate180[0][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmp010 = _tmpRotate180[1][0] * _tmpNoReflect[0][0] + _tmpRotate180[1][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp011 = _tmpRotate180[1][0] * _tmpNoReflect[0][1] + _tmpRotate180[1][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 270:
                                            _tmp000 = _tmpRotate270[0][0] * _tmpNoReflect[0][0] + _tmpRotate270[0][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp001 = _tmpRotate270[0][0] * _tmpNoReflect[0][1] + _tmpRotate270[0][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmp010 = _tmpRotate270[1][0] * _tmpNoReflect[0][0] + _tmpRotate270[1][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp011 = _tmpRotate270[1][0] * _tmpNoReflect[0][1] + _tmpRotate270[1][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    elif self._DesignParameter[element0Parent][element0Id]._DesignParameter['_Reflect'][
                                        0] == 1:
                                        if self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == None or \
                                                self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                                    '_Angle'] == 0:
                                            _tmp000 = _tmpRotate0[0][0] * _tmpReflectOnX[0][0] + _tmpRotate0[0][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp001 = _tmpRotate0[0][0] * _tmpReflectOnX[0][1] + _tmpRotate0[0][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmp010 = _tmpRotate0[1][0] * _tmpReflectOnX[0][0] + _tmpRotate0[1][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp011 = _tmpRotate0[1][0] * _tmpReflectOnX[0][1] + _tmpRotate0[1][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 90:
                                            _tmp000 = _tmpRotate90[0][0] * _tmpReflectOnX[0][0] + _tmpRotate90[0][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp001 = _tmpRotate90[0][0] * _tmpReflectOnX[0][1] + _tmpRotate90[0][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmp010 = _tmpRotate90[1][0] * _tmpReflectOnX[0][0] + _tmpRotate90[1][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp011 = _tmpRotate90[1][0] * _tmpReflectOnX[0][1] + _tmpRotate90[1][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 180:
                                            _tmp000 = _tmpRotate180[0][0] * _tmpReflectOnX[0][0] + _tmpRotate180[0][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp001 = _tmpRotate180[0][0] * _tmpReflectOnX[0][1] + _tmpRotate180[0][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmp010 = _tmpRotate180[1][0] * _tmpReflectOnX[0][0] + _tmpRotate180[1][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp011 = _tmpRotate180[1][0] * _tmpReflectOnX[0][1] + _tmpRotate180[1][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 270:
                                            _tmp000 = _tmpRotate270[0][0] * _tmpReflectOnX[0][0] + _tmpRotate270[0][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp001 = _tmpRotate270[0][0] * _tmpReflectOnX[0][1] + _tmpRotate270[0][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmp010 = _tmpRotate270[1][0] * _tmpReflectOnX[0][0] + _tmpRotate270[1][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp011 = _tmpRotate270[1][0] * _tmpReflectOnX[0][1] + _tmpRotate270[1][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]

                                    _tmpStackForOffsetAndTransition.append([_tmpXYCoordinate, _tmpTranspose0,
                                                                            self._DesignParameter[element0Parent][
                                                                                element0Id]._type])
                            elif self._DesignParameter[element0Parent][element0Id]._type == 8:
                                for _tmpXYCoordinate in \
                                self._DesignParameter[element0Parent][element0Id]._DesignParameter["_XYCoordinates"]:
                                    if self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                        '_Reflect'] == None or \
                                            self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                                '_Reflect'][0] == 0:
                                        if self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == None or \
                                                self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                                    '_Angle'] == 0:
                                            _tmp000 = _tmpRotate0[0][0] * _tmpNoReflect[0][0] + _tmpRotate0[0][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp001 = _tmpRotate0[0][0] * _tmpNoReflect[0][1] + _tmpRotate0[0][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmp010 = _tmpRotate0[1][0] * _tmpNoReflect[0][0] + _tmpRotate0[1][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp011 = _tmpRotate0[1][0] * _tmpNoReflect[0][1] + _tmpRotate0[1][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 90:
                                            _tmp000 = _tmpRotate90[0][0] * _tmpNoReflect[0][0] + _tmpRotate90[0][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp001 = _tmpRotate90[0][0] * _tmpNoReflect[0][1] + _tmpRotate90[0][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmp010 = _tmpRotate90[1][0] * _tmpNoReflect[0][0] + _tmpRotate90[1][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp011 = _tmpRotate90[1][0] * _tmpNoReflect[0][1] + _tmpRotate90[1][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 180:
                                            _tmp000 = _tmpRotate180[0][0] * _tmpNoReflect[0][0] + _tmpRotate180[0][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp001 = _tmpRotate180[0][0] * _tmpNoReflect[0][1] + _tmpRotate180[0][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmp010 = _tmpRotate180[1][0] * _tmpNoReflect[0][0] + _tmpRotate180[1][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp011 = _tmpRotate180[1][0] * _tmpNoReflect[0][1] + _tmpRotate180[1][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 270:
                                            _tmp000 = _tmpRotate270[0][0] * _tmpNoReflect[0][0] + _tmpRotate270[0][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp001 = _tmpRotate270[0][0] * _tmpNoReflect[0][1] + _tmpRotate270[0][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmp010 = _tmpRotate270[1][0] * _tmpNoReflect[0][0] + _tmpRotate270[1][1] * \
                                                      _tmpNoReflect[1][0]
                                            _tmp011 = _tmpRotate270[1][0] * _tmpNoReflect[0][1] + _tmpRotate270[1][1] * \
                                                      _tmpNoReflect[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    elif self._DesignParameter[element0Parent][element0Id]._DesignParameter['_Reflect'][
                                        0] == 1:
                                        if self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == None or \
                                                self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                                    '_Angle'] == 0:
                                            _tmp000 = _tmpRotate0[0][0] * _tmpReflectOnX[0][0] + _tmpRotate0[0][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp001 = _tmpRotate0[0][0] * _tmpReflectOnX[0][1] + _tmpRotate0[0][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmp010 = _tmpRotate0[1][0] * _tmpReflectOnX[0][0] + _tmpRotate0[1][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp011 = _tmpRotate0[1][0] * _tmpReflectOnX[0][1] + _tmpRotate0[1][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 90:
                                            _tmp000 = _tmpRotate90[0][0] * _tmpReflectOnX[0][0] + _tmpRotate90[0][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp001 = _tmpRotate90[0][0] * _tmpReflectOnX[0][1] + _tmpRotate90[0][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmp010 = _tmpRotate90[1][0] * _tmpReflectOnX[0][0] + _tmpRotate90[1][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp011 = _tmpRotate90[1][0] * _tmpReflectOnX[0][1] + _tmpRotate90[1][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 180:
                                            _tmp000 = _tmpRotate180[0][0] * _tmpReflectOnX[0][0] + _tmpRotate180[0][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp001 = _tmpRotate180[0][0] * _tmpReflectOnX[0][1] + _tmpRotate180[0][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmp010 = _tmpRotate180[1][0] * _tmpReflectOnX[0][0] + _tmpRotate180[1][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp011 = _tmpRotate180[1][0] * _tmpReflectOnX[0][1] + _tmpRotate180[1][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                        elif self._DesignParameter[element0Parent][element0Id]._DesignParameter[
                                            '_Angle'] == 270:
                                            _tmp000 = _tmpRotate270[0][0] * _tmpReflectOnX[0][0] + _tmpRotate270[0][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp001 = _tmpRotate270[0][0] * _tmpReflectOnX[0][1] + _tmpRotate270[0][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmp010 = _tmpRotate270[1][0] * _tmpReflectOnX[0][0] + _tmpRotate270[1][1] * \
                                                      _tmpReflectOnX[1][0]
                                            _tmp011 = _tmpRotate270[1][0] * _tmpReflectOnX[0][1] + _tmpRotate270[1][1] * \
                                                      _tmpReflectOnX[1][1]
                                            _tmpTranspose0 = [[_tmp000, _tmp001], [_tmp010, _tmp011]]
                                    _tmpStackForOffsetAndTransition.append([_tmpXYCoordinate, _tmpTranspose0,
                                                                            self._DesignParameter[element0Parent][
                                                                                element0Id]._type])
                    _tmpStackForXYCoordinateForDisplay.append(_tmpStackForOffsetAndTransition)
                _tmpStackForFinalResult = []
                for index0 in range(0, len(_tmpStackForXYCoordinateForDisplay)):
                    if index0 == 0:
                        _tmpStackForFinalResult = _tmpStackForXYCoordinateForDisplay[index0]
                        # if (_tmpStackForXYCoordinateForDisplay[index0][2] == 1) or (_tmpStackForXYCoordinateForDisplay[index0][2] == 2):
                        #     _tmpStackForFinalResult = (_tmpStackForXYCoordinateForDisplay[index0])
                        # else:
                        #     _tmpStackForFinalResult = (_tmpStackForXYCoordinateForDisplay[index0])
                    else:
                        _tmp = []
                        for element0 in _tmpStackForFinalResult:
                            for element1 in _tmpStackForXYCoordinateForDisplay[index0]:
                                _tmp00 = element0[1][0][0] * element1[1][0][0] + element0[1][0][1] * element1[1][1][0]
                                _tmp01 = element0[1][0][0] * element1[1][0][1] + element0[1][0][1] * element1[1][1][1]
                                _tmp10 = element0[1][1][0] * element1[1][0][0] + element0[1][1][1] * element1[1][1][0]
                                _tmp11 = element0[1][1][0] * element1[1][0][1] + element0[1][1][1] * element1[1][1][1]
                                _tmpTranspose0 = [[_tmp00, _tmp01], [_tmp10, _tmp11]]
                                if (element1[2] == 1) or (element1[2] == 2):
                                    _tmpResult1 = []
                                    for _tmpXYCoordinateOfElement1 in element1[0]:
                                        _tmpResult1.append(
                                            [
                                                element0[0][0] + (element0[1][0][0] * _tmpXYCoordinateOfElement1[0] +
                                                                  element0[1][0][1] * _tmpXYCoordinateOfElement1[1]),
                                                element0[0][1] + (element0[1][1][0] * _tmpXYCoordinateOfElement1[0] +
                                                                  element0[1][1][1] * _tmpXYCoordinateOfElement1[1])
                                            ]
                                        )
                                    _tmpResult = [
                                        _tmpResult1,
                                        _tmpTranspose0,
                                        element1[2]
                                    ]
                                    _tmp.append(_tmpResult)
                                # elif(element1[2] == 8):
                                #     pass
                                else:
                                    _tmpResult = [[element0[0][0] + (
                                                element0[1][0][0] * element1[0][0] + element0[1][0][1] * element1[0][
                                            1]),
                                                   element0[0][1] + (
                                                               element0[1][1][0] * element1[0][0] + element0[1][1][1] *
                                                               element1[0][1])
                                                   ],
                                                  _tmpTranspose0,
                                                  element1[2]
                                                  ]
                                    _tmp.append(_tmpResult)
                        _tmpStackForFinalResult = _tmp
                # _tmpStackForFinalResult = list(set(_tmpStackForFinalResult))
                for element0 in _tmpStackForFinalResult:
                    self._DesignParameter[_ParentName][_id]._XYCoordinatesForDisplay.append(element0[0])

            except:
                print("_UpdateXYCoordinateForDisplay Error")
                return userDefineExceptions._UnkownError

    def _ConvertBoundaryXYExpression(self, _id=None, _ParentName=None):
        for i, five_point_xy in enumerate(self._DesignParameter[_ParentName][_id]._XYCoordinatesForDisplay):
            if type(five_point_xy) == list and len(five_point_xy) == 5:
                if type(five_point_xy[0]) == list:
                        self._DesignParameter[_ParentName][_id]._XYCoordinatesForDisplay[i] = five_point_xy[0]


    def _SaveDataAsJsonFormat(self, _data=None, _file=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_SaveDataAsJsonFormat Run.")
        if _data == None or _file == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                with open('{}.json'.format(_file), 'w', encoding="utf-8") as make_file:
                    json.dump(_data, make_file, ensure_ascii=False, indent="\t")
            except:
                return userDefineExceptions._UnkownError

    def _feed_design(self, design_type: str, module_name: str, _ast: ast.AST=None, dp_dict: dict=None, element_manager_update:bool =True) -> dict:
        if design_type == 'parameter':
            output = self._feed_design_dictionary(module_name=module_name,_dp_dict=dp_dict, element_manager_update=element_manager_update)
        elif design_type == 'constraint':
            output = self._feed_ast(module_name=module_name,_ast=_ast, element_manager_update= element_manager_update)

        return output

    def _update_design(self, design_type: str, module_name: str, id: str, _ast: ast.AST=None, dp_dict: dict=None) -> dict:
        if design_type == 'parameter':
            output = self._update_design_dictionary(module_name=module_name, id=id, _dp_dict=dp_dict)
        elif design_type == 'constraint':
            output = self._update_ast(module_name=module_name, id=id, _ast=_ast)

        return output

    def _createNewDesignParameter(self, _id=None, _type=None, _ParentName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_createNewDesignParameter Run.")
        if _ParentName == None or _id == None or _type == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if _ParentName not in self._DesignParameter.keys():
                    self._DesignParameter[_ParentName] = dict()
                self._DesignParameter[_ParentName][_id] = QtDesignParameter(_id=_id, _type=_type,
                                                                            _ParentName=_ParentName)
                self._DesignParameter[_ParentName][_id]._createDesignParameter()
            except:
                return userDefineExceptions._UnkownError

    def _feed_design_dictionary(self, module_name: str, _dp_dict: dict, element_manager_update: bool = True) -> dict:
        # _createNewDesignParameter_by_dict(self, module_name, _dp_dict, element_manager_update=True):
        """
        :param module_name:  current module name
        :param _dp_dict: dictionary file which contains design parameter values
        :param element_manager_update: This argument prevent recursive call btw createNewDesignParameter_by_dict and
        createNewDesignConstraint.
        :return:
        """
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_createNewDesignParameter Run.")
        if _dp_dict == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                # create new design parameter
                id_num = self._getDesignParameterId(module_name)
                designID = (module_name + str(id_num))
                self._createNewDesignParameter(_id=designID, _type=_dp_dict['_DesignParametertype'],
                                               _ParentName=module_name)
                for key in _dp_dict:
                    self._DesignParameter[module_name][designID]._setDesignParameterValue(_index=key,
                                                                                                      _value=_dp_dict[
                                                                                                          key])
                self._DesignParameter[module_name][designID]._setDesignParameterName(
                    _DesignParameterName=_dp_dict['_DesignParameterName'])
                self._UpdateXYCoordinateForDisplay(_id=designID, _ParentName=module_name)
                self._ConvertBoundaryXYExpression(_id=designID, _ParentName=module_name)
                # send design parameter info to element manager --> return: ast info or
                _designParameter = self._DesignParameter[module_name][designID]
                _designConstraint = None
                _designConstraint_id = None
                if element_manager_update == True:
                    try:
                        tmp_ast, _ = self._ElementManager.get_dpdict_return_ast(_dp_dict)
                        if tmp_ast:
                            tmp_dict = self._feed_ast(_ast=tmp_ast, module_name=module_name,element_manager_update=False)
                            _designConstraint = tmp_dict['constraint']
                            _designConstraint_id = tmp_dict['constraint_id']
                            self._ElementManager.load_dp_dc(_designParameter, _designConstraint)
                    except:
                        print('Constraint -> Parameter is not implemented')

                output = {'parameter': _designParameter, 'constraint': _designConstraint, 'parameter_id': designID, 'constraint_id': _designConstraint_id}
                return output
            except:
                return userDefineExceptions._UnkownError

    def _update_design_dictionary(self, module_name: str, id: str, _dp_dict: dict, element_manager_update: bool = True) -> dict:
        # _createNewDesignParameter_by_dict(self, module_name, _dp_dict, element_manager_update=True):
        """
        :param module_name:  current module name
        :param _dp_dict: dictionary file which contains design parameter values
        :param element_manager_update: This argument prevent recursive call btw createNewDesignParameter_by_dict and
        createNewDesignConstraint.
        :return:
        """
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_createNewDesignParameter Run.")
        if _dp_dict == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                for key in _dp_dict:
                    self._DesignParameter[module_name][id]._setDesignParameterValue(_index=key,_value=_dp_dict[key])
                self._DesignParameter[module_name][id]._setDesignParameterName(_DesignParameterName=_dp_dict['_DesignParameterName'])

                # send design parameter info to element manager --> return: ast info or
                _designParameter = self._DesignParameter[module_name][id]
                _designConstraint = None
                _designConstraint_id = None
                if element_manager_update == True:
                    try:
                        tmp_ast, designparameter_id = self._ElementManager.get_dpdict_return_ast(_dp_dict)
                        if tmp_ast:
                            tmp_dict = self._update_ast(_ast=tmp_ast, module_name=module_name, id=designparameter_id, element_manager_update=False)
                            _designConstraint = tmp_dict['constraint']
                            _designConstraint_id = tmp_dict['constraint_id']
                    except:
                        print('Constraint -> Parameter is not implemented')

                output = {'parameter': _designParameter, 'constraint': _designConstraint, 'parameter_id': id, 'constraint_id': _designConstraint_id}
                return output
            except:
                return userDefineExceptions._UnkownError

    def _deleteDesignParameter(self, _id=None, _ParentName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_deleteDesignParameter Run.")
        if _ParentName == None:
            # raise userDefineExceptions.IncorrectInputError("_id  or _ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if _id == None:
                    del self._DesignParameter[_ParentName]
                else:
                    del self._DesignParameter[_ParentName][_id]
                # del self._idListForDesignParameter[_ParentName][_id]
            except:
                return userDefineExceptions._UnkownError

    def _createNewDesignConstraint(self, _id=None, _type=None, _ParentName=None, _ast=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_createNewDesignConstraint Run.")
        if _ParentName == None or _id == None or _type == None or _ast == None:
            # raise userDefineExceptions.IncorrectInputError("_id or _type or _ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if _ParentName not in self._DesignConstraint.keys():
                    self._DesignConstraint[_ParentName] = dict()
                self._DesignConstraint[_ParentName][_id] = QtDesinConstraint(_id=_id, _type=_type, _ast=_ast)
                # self._DesignConstraint[_ParentName][_id]._createDesignConstrain()
            except:
                print("_createNewDesignConstraint Error")
                return userDefineExceptions._UnkownError

    def _createNewDesignConstraintAST(self, _id=None, _ASTDtype=None, _ParentName=None, _STMTList=None, _pyCode=None,
                                      _AST=None):
        if _ASTDtype == "pyCode":  # In case of pyCode input, there are at least one constraint.
            try:
                topAST = ast.parse(_pyCode)
                _astList = ASTmodule._searchAST(topAST)
                _ids = []
                for AST in _astList:
                    _idNum = self._getDesignConstraintId(_ParentName)
                    _id = _ParentName + str(_idNum)
                    self._DesignConstraint[_ParentName][_id] = QtDesinConstraint(_id=_id,
                                                                                 _type=ASTmodule._getASTtype(AST),
                                                                                 _ast=AST)
                    _ids.append(_id)
                    # if AST == topAST:
                    #     topId = _id
                # _STMTListOut = ASTmodule._convertPyCodeToSTMTlist(topAST)
                return None, _ids[0]
            except:
                raise userDefineExceptions.IncorrectInputError("constraint Parameter has invalid value")
        elif _ASTDtype == "ASTsingle":
            _idNum = self._getDesignConstraintId(_ParentName)
            _id = _ParentName + str(_idNum)
            self._DesignConstraint[_ParentName][_id] = QtDesinConstraint(_id=_id, _type=ASTmodule._getASTtype(_AST),
                                                                         _ast=_AST)
            # _STMTListOut = ASTmodule._convertPyCodeToSTMTlist(_AST)
            return None, [_id]


        elif _ASTDtype == "STMT":
            if type(_STMTList) != list:  # if stmt is single statement
                _STMTList = [_STMTList]
            for stmt in _STMTList:
                _idNum = self._getDesignConstraintId(_ParentName)
                _id = _ParentName + str(_idNum)

                self._DesignConstraint[_ParentName][_id] = QtDesinConstraint(_id=_id, _type=stmt['_type'])
                self._DesignConstraint[_ParentName][_id]._createDesignConstraintSTMT(stmt)

                # _ASTDictOut = ASTmodule._updateASTDictID(_id = _id, _ASTDict = _ASTDict)
                # _ASTDictOut = ASTmodule._ASTDictUpdateMissingPart(_ASTDictOut)
                # _module = _ParentName
                _ids = [_id]
                _STMTListOut = ASTmodule._convertPyCodeToSTMTlist(self._DesignConstraint[_ParentName][_id]._ast)

                return _STMTListOut, _ids
        elif _ASTDtype == "stmts":
            pass

    def _convertPyCodeToASTDict(self, _pyCode):
        _AST = ast.parse(_pyCode)
        _ASTDict = dict()
        for stmt in _AST.body:
            _key = self._getASTtype(stmt)
            _ASTDict[_key] = dict()

    def _feed_ast(self, module_name: str, _ast: ast.AST, element_manager_update: bool=True) -> list:
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_createNewDesignParameter Run.")
        if _ast == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                # create new design parameter
                id_num = self._getDesignConstraintId(module_name)
                constraintID = (module_name + str(id_num))
                self._createNewDesignConstraint(_id=constraintID, _type=ASTmodule._getASTtype(_ast),
                                                _ParentName=module_name, _ast=_ast)

                # send design parameter info to element manager --> return: ast info or
                _designConstraint = self._DesignConstraint[module_name][constraintID]
                _designParameter = None
                _designParameter_id = None
                if element_manager_update == True:
                    try:
                        tmp_dp_dict, _ = self._ElementManager.get_ast_return_dpdict(_ast)
                        if tmp_dp_dict:
                            tmp_dict = self._feed_design_dictionary(_dp_dict= tmp_dp_dict, module_name=module_name, element_manager_update=False)
                            _designParameter = tmp_dict['parameter']
                            _designParameter_id = tmp_dict['parameter_id']
                            self._ElementManager.load_dp_dc(_designParameter, _designConstraint)
                    except:
                        print("Constraint -> Parameter is not implemented.")


                output = {'parameter': _designParameter, 'constraint': _designConstraint, 'parameter_id': _designParameter_id, 'constraint_id': constraintID}
                return output
            except:
                return userDefineExceptions._UnkownError

    def _update_ast(self, module_name: str, id: str, _ast: ast.AST, element_manager_update: bool=True) -> list:
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_createNewDesignParameter Run.")
        if _ast == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                # send design parameter info to element manager --> return: ast info or
                self._DesignConstraint[module_name][id]._ast = _ast
                _designConstraint = self._DesignConstraint[module_name][id]
                _designParameter = None
                _designParameter_id = None
                if element_manager_update == True:
                    try:
                        tmp_dp_dict, contraint_id = self._ElementManager.get_ast_return_dpdict(_ast)
                        if tmp_dp_dict:
                            tmp_dict = self._update_design_dictionary(_dp_dict= tmp_dp_dict, module_name=module_name, id=contraint_id, element_manager_update=False)
                            _designParameter = tmp_dict['parameter']
                            _designParameter_id = tmp_dict['parameter_id']
                    except:
                        print("Constraint -> Parameter is not implemented.")


                output = {'parameter': _designParameter, 'constraint': _designConstraint, 'parameter_id': _designParameter_id, 'constraint_id': id}
                return output
            except:
                return userDefineExceptions._UnkownError

    def _getASTtype(self, _targetObject):
        _type = str(type(_targetObject))
        className = re.search('ast.[a-zA-Z]+', _type).group()
        className = className[4:]
        print(className)
        return className

    def _createDesignConstraintWithASTree(self, _ASTree=None, _ParentName=None):

        print(1)
        pass

    def _deleteDesignConstraint(self, _id=None, _ParentName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_deleteDesignConstraint Run.")
        if _ParentName == None:
            # raise userDefineExceptions.IncorrectInputError("_id or _ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if _id == None:
                    del self._DesignConstraint[_ParentName]
                else:
                    del self._DesignConstraint[_ParentName][_id]
                # del self._idListForDesignConstraint[_ParentName][_id]
            except:
                print("_deleteDesignConstraint Error")
                return userDefineExceptions._UnkownError

    def _setRootDesignConstraint(self, _id=None, _ParentName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_setRootDesignConstraint Run.")
        if _ParentName == None or _id == None:
            # raise userDefineExceptions.IncorrectInputError("_id or _ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                self._ParseTreeForDesignConstrain[_ParentName] = self._DesignConstraint[_ParentName][_id]
            except:
                return userDefineExceptions._UnkownError

    def _setRootDesignParameter(self, _id=None, _ParentName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_setRootDesignParameter Run.")
        if _ParentName == None or _id == None:
            # raise userDefineExceptions.IncorrectInputError("_id or _ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                self._ParseTreeForDesignParameter[_ParentName] = self._ParseTreeForDesignParameter[_ParentName]
            except:
                return userDefineExceptions._UnkownError

    def _getDesignParameterId(self, _ParentName=None, ):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_getDesignParameterId Run.")
        if _ParentName == None:
            # raise userDefineExceptions.IncorrectInputError("_ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if _ParentName not in self._DesignParameter.keys():
                    self._DesignParameter[_ParentName] = dict()
                _tmpIdGroup = list(range(0, len(self._DesignParameter[_ParentName].keys()) + 1))
                for _tmpId in self._DesignParameter[_ParentName].keys():
                    if int(_tmpId[len(_ParentName):]) in _tmpIdGroup:
                        _tmpIdGroup.remove(int(_tmpId[len(_ParentName):]))
                return min(_tmpIdGroup)
            except:
                return userDefineExceptions._UnkownError

    def _getDesignConstraintId(self, _ParentName=None, ):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_getDesignConstraintId Run.")
        if _ParentName == None:
            # raise userDefineExceptions.IncorrectInputError("_ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if _ParentName not in self._DesignConstraint.keys():
                    self._DesignConstraint[_ParentName] = dict()
                _tmpIdGroup = list(range(0, len(self._DesignConstraint[_ParentName].keys()) + 1))
                for _tmpId in self._DesignConstraint[_ParentName].keys():
                    if int(_tmpId[len(_ParentName):]) in _tmpIdGroup:
                        _tmpIdGroup.remove(int(_tmpId[len(_ParentName):]))
                return min(_tmpIdGroup)
            except:
                return userDefineExceptions._UnkownError

    def _GetHierarchicalVariableForXYCoordiantes(self, _id=None, _ParentName=None):
        # self._DesignParameter['_FFRetimingLeft']['_XYCoordinates'][0][0]  + self._DesignParameter['_FFRetimingLeft']['_DesignObj']._DesignParameter['_NMOSMaster']['_XYCoordinates'][0][0] + self._DesignParameter['_FFRetimingLeft']['_DesignObj']._DesignParameter['_NMOSMaster']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_GetHierarchicalVariableForXYCoordiantes Run.")
        if _ParentName == None or _id == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                pass
                # _tmpResult = self._HierarchyFromRootForDesignParameter(_ParentName = _ParentName,_id = _id )
                # if _tmpResult == userDefineExceptions._InvalidInputError:
                #     return userDefineExceptions._InvalidInputError
                # elif _tmpResult == userDefineExceptions._UnkownError:
                #     return userDefineExceptions._UnkownError
                # else:
                #     self._DesignParameter[_ParentName][_id]._DesignHierarchy = _tmpResult
                #     return True

            except:
                return userDefineExceptions._UnkownError

    def _GetHierarchicalVariableForXYWidth(self, _id=None, _ParentName=None):
        # float(self._DesignParameter['_FFRetimingRight']['_DesignObj']._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']) / 2
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_GetHierarchicalVariableForXYWidth Run.")
        if _ParentName == None or _id == None:
            return userDefineExceptions._InvalidInputError
        elif self._DesignParameter[_ParentName][_id]._DesignHierarchy == None:
            return userDefineExceptions._InvalidObjStateError
        else:
            try:
                pass
                # _tmpResult = ""
                # for element0 in self._DesignParameter[_ParentName][_id]._DesignHierarchy[1:]:
                #     pass
                # for index0 in range(0, len(self._DesignParameter[_ParentName][_id]._DesignHierarchy)):
                #     if index0 == 0:
                #         _tmpResult = _tmpResult + "self._DesignParameter[]"
                #     self._DesignParameter[_ParentName][_id]._DesignHierarchy[index0]
            except:
                return userDefineExceptions._UnkownError

    def _GetHierarchyFromRootForDesignParameter(self, _id=None, _ParentName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_VariableCompletionForDesignParameterWComplexHierarchy Run.")
        if _ParentName == None or _id == None:
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpResult = self._HierarchyFromRootForDesignParameter(_ParentName=_ParentName, _id=_id)
                if _tmpResult == userDefineExceptions._InvalidInputError:
                    return userDefineExceptions._InvalidInputError
                elif _tmpResult == userDefineExceptions._UnkownError:
                    return userDefineExceptions._UnkownError
                else:
                    self._DesignParameter[_ParentName][_id]._DesignHierarchy = _tmpResult
                    return True

            except:
                return userDefineExceptions._UnkownError

    def _ConstraintsForPyCodeDefineTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForPyCodeDefineTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForPyCodeDefineTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForPyCodeDefineTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForPyCodeDefineTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="pyCode",
                                                _ParentName=_ScriptName)
                # self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
                # self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._setDesignConstraintValue(_index="_name", _value=_ScriptName)
            except:
                print("_ConstraintsForPyCodeDefineTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForPyCodeDefineTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _ConstraintsForScriptDefineTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForScriptTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForScriptTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForScriptTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForScriptTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="scriptDefine",
                                                _ParentName=_ScriptName)
                # self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
                # self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._setDesignConstraintValue(_index="_name", _value=_ScriptName)
            except:
                print("_ConstraintsForScriptTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForScriptTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

            # _tmpParseTree = {"_id": self._id, "_type": self._type, "_lineCodes": [], "_space": 0, "_tab": 0, }
            # if self._type == "pyCode":
            #     # self._name = _name
            #     # self._file = None
            #     _tmpParseTree["_name"] = ""
            #     _tmpParseTree["_file"] = ""
            #
            # elif self._type == "scriptDefine":
            #     _tmpParseTree["_name"] = ""
            #     _tmpParseTree["_libImport"] = []
            #     _tmpParseTree["_variableDefine"] = []
            #     _tmpParseTree["_classDefine"] = []
            #     _tmpParseTree["_functionDefine"] = []
            #     _tmpParseTree["_statements"] = []
            #     _tmpParseTree["_pyCode"] = []

    def _ConstraintsForClassDefineTemplate(self, _ScriptName=None, ):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForClassTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForClassTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForClassTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForClassTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="classDefine",
                                                _ParentName=_ScriptName)
                # self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForClassTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForClassTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError
            # elif self._type == "classDefine":
            # _tmpParseTree["_name"] = ""
            # _tmpParseTree["_inheritance"] = []
            # _tmpParseTree["_statements"] = []
            # _tmpParseTree["_functionDefine"] = []
            # _tmpParseTree["_pyCode"] = []
            # # self._name = _name
            # # self._inheritance = []
            # # self._statements = []
            # # self._functionDefine = []
            # # self._pyCode = []

    def _ConstraintsForClassCallTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForClassTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForClassTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForClassTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForClassTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="classCall",
                                                _ParentName=_ScriptName)
                # self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForClassTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForClassTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _ConstraintsForFunctionDefineTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForClassTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForClassTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForClassTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForClassTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="functionDefine",
                                                _ParentName=_ScriptName)
                # self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForClassTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForClassTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _ConstraintsForFunctionCallTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForFunctionCallTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForFunctionCallTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForFunctionCallTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForFunctionCallTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="functionCall",
                                                _ParentName=_ScriptName)
                # self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForFunctionCallTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForFunctionCallTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    # _tmpParseTree["_name"] = ""
    # _tmpParseTree["_arguments"] = []
    # _tmpParseTree["_statements"] = []
    # _tmpParseTree["_pyCode"] = []
    def _ConstraintsForStatementTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForStatementTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForStatementTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForStatementTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForStatementTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="statement",
                                                _ParentName=_ScriptName)
                self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForStatementTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForStatementTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _ConstraintsForForLoopTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForForLoopTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForForLoopTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForForLoopTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForForLoopTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="forLoop",
                                                _ParentName=_ScriptName)
                self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForForLoopTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForForLoopTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    # self._type == "forLoop":
    # _tmpParseTree["_index"] = []
    # _tmpParseTree["_condition"] = []
    # _tmpParseTree["_statements"] = []
    def _ConstraintsForWhileLoopTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForWhileLoopTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForWhileLoopTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForWhileLoopTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForWhileLoopTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="whileLoop",
                                                _ParentName=_ScriptName)
                self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForWhileLoopTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForWhileLoopTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    # self._type == "whileLoop":
    # _tmpParseTree["_logic"] = []
    # _tmpParseTree["_statements"] = []
    def _ConstraintsForIfControlTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForIfControlTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForIfControlTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForIfControlTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForIfControlTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="ifControl",
                                                _ParentName=_ScriptName)
                self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForIfControlTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForIfControlTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    # self._type == "ifControl":
    # _tmpParseTree["_ifLogic"] = []
    # _tmpParseTree["_elifLogic"] = []
    # _tmpParseTree["_elseLogic"] = []
    def _ConstraintsForVariableDefineTemplate(self, _ScriptName=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_ConstraintsForVariableDefineTemplate Run.")
            if self._LogMessageHandler != None:
                self._LogMessageHandler._DebugMessage("_ConstraintsForVariableDefineTemplate Run.")
        if _ScriptName == None:
            print("_ConstraintsForVariableDefineTemplate: " + userDefineExceptions._InvalidInputError)
            if self._LogMessageHandler != None:
                self._LogMessageHandler._ErrorMessage(
                    "_ConstraintsForVariableDefineTemplate: " + userDefineExceptions._InvalidInputError)
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpId = self._getDesignConstraintId(_ParentName=_ScriptName)
                print("New DesignParameter id ", _tmpId)
                self._createNewDesignConstraint(_id=(_ScriptName + str(_tmpId)), _type="variableDefine",
                                                _ParentName=_ScriptName)
                self._DesignConstraint[_ScriptName][(_ScriptName + str(_tmpId))]._createDesignConstrain()
            except:
                print("_ConstraintsForVariableDefineTemplate: " + userDefineExceptions._UnkownError)
                if self._LogMessageHandler != None:
                    self._LogMessageHandler._ErrorMessage(
                        "_ConstraintsForVariableDefineTemplate: " + userDefineExceptions._UnkownError)
                return userDefineExceptions._UnkownError

    def _subHierarchyForDesignParameter(self, _ParentName=None, _id=None, _MaxSearchDepth=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_subHierarchyForDesignParameter Run.")
        if _ParentName == None:
            # raise userDefineExceptions.IncorrectInputError("_ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                if _id == None:
                    _tmpStack1 = []
                    for element1ForId in self._DesignParameter[_ParentName].keys():
                        _tmpStack1.append([_ParentName, element1ForId])
                else:
                    _tmpStack1 = [[_ParentName, _id]]
                _tmpStack0 = []
                _tmpStack0.append(_tmpStack1)
                _tmpStack0Pt = _tmpStack0[-1]
                _SearchDepthCounter = 0
                while True:
                    if (_MaxSearchDepth != None) and (_SearchDepthCounter >= _MaxSearchDepth):
                        break
                    _tmpStack1 = []
                    for [element0ForParent, element0ForId] in _tmpStack0Pt:
                        if self._DesignParameter[element0ForParent][element0ForId]._DesignParameter[
                            "_DesignParametertype"] == 3:
                            for element1ForId in self._DesignParameter[
                                self._DesignParameter[element0ForParent][element0ForId]._DesignParameter[
                                    "_DesignObj"]].keys():
                                _tmpStack1.append([self._DesignParameter[element0ForParent][
                                                       element0ForId]._DesignParameter["_DesignObj"], element1ForId])
                    if not _tmpStack1:
                        break
                    else:
                        _tmpStack0.append(_tmpStack1)
                        _tmpStack0Pt = _tmpStack0[-1]
                        _SearchDepthCounter = _SearchDepthCounter + 1
                return _tmpStack0
            except:
                return userDefineExceptions._UnkownError

    def _HierarchyFromRootForDesignParameter(self, _ParentName=None, _id=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_HierarchyFromRootForDesignParameter Run.")
        if _ParentName == None:
            # raise userDefineExceptions.IncorrectInputError("_ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _tmpStack0 = []
                _tmpStack0.insert(0, {_ParentName: [_id]})
                _tmpStack0Pt = _tmpStack0[0]
                while True:
                    _tmpStack1 = {}
                    for element0ForParent, element0ForIds in _tmpStack0Pt.items():
                        # for element0ForId in element0ForIds:
                        for element1ForParent in self._DesignParameter.keys():
                            for element1ForId in self._DesignParameter[element1ForParent].keys():
                                if self._DesignParameter[element1ForParent][element1ForId]._DesignParameter[
                                    "_DesignParametertype"] == 3:
                                    if self._DesignParameter[element1ForParent][element1ForId]._DesignParameter[
                                        "_DesignObj"] == element0ForParent:
                                        if element1ForParent in _tmpStack1.keys():
                                            _tmpStack1[element1ForParent].append(element1ForId)
                                        else:
                                            _tmpStack1[element1ForParent] = [element1ForId]
                    if not _tmpStack1:
                        break
                    else:
                        _tmpStack0.insert(0, _tmpStack1)
                        _tmpStack0Pt = _tmpStack0[0]
                return _tmpStack0  ####[[[_ParentName0, _id0], [_ParentName0, _id1], [_ParentName1, _id]1], [], [], []] --> [[[_ParentName0, _id0], [_ParentName0, _id1], [_ParentName1, _id]1], [], [], []]
            except:
                return userDefineExceptions._UnkownError

    def _subHierarchyForDesignConstraint(self, _ParentName=None, _id=None, _MaxSearchDepth=None):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("_subHierarchyForDesignConstraint Run.")
        if _ParentName == None or _id == None:
            # raise userDefineExceptions.IncorrectInputError("_id or _ParentName has None value.")
            return userDefineExceptions._InvalidInputError
        else:
            try:
                return self._DesignConstraint[_ParentName][_id]._findSubHierarchy()
            except:
                return userDefineExceptions._UnkownError


class QtInterFace:
    def __init__(self, ):
        self._qtProject = None

    def _saveProject(self, _name="defaultProjectName.bin"):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("###################### saveProject ##########################")
        if self._qtProject == None:
            return userDefineExceptions._InvalidObjStateError
        else:
            try:
                _PicklefileName = _name
                with gzip.open('{}'.format(_PicklefileName), 'wb') as testPickleFile:
                    pickle.dump(self._qtProject, testPickleFile)
                testPickleFile.close()
            except:
                return userDefineExceptions._UnkownError

    def _loadProject(self, _name="defaultProjectName.bin"):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("###################### loadProject ##########################")
        if not os.path.exists(_name):
            return userDefineExceptions._InvalidInputError
        else:
            try:
                _PicklefileName1 = _name
                with gzip.open('{}'.format(_PicklefileName1), 'rb') as QtProjectPickleFile:
                    _tmpQtProject = pickle.load(QtProjectPickleFile)
                QtProjectPickleFile.close()
                self._qtProject = _tmpQtProject
            except:
                return userDefineExceptions._UnkownError

    def _createProject(self, _name="defaultProjectName"):
        if (EnvForClientSetUp.DebuggingMode == 1) or (EnvForClientSetUp.DebuggingModeForQtInterface == 1):
            print("###################### saveProject ##########################")
        self._qtProject = QtProject(_name=_name)

    def _closeProject(self):
        del self._qtProject
        self._qtProject = None


def main():
    _tmpConstraints = {'_type': 'scriptDefine',
                       # 'pyCode', 'scriptDefine' 'libImport', 'classDefine', 'functionDefine','argument','statement','forLoop', 'condition', 'whileLoop', 'ifControl', 'ifLogic', 'logic',  'logicOp', 'expression',  'op', 'variableDefine', 'variable'
                       # self._tab = _tab        #'dictionary', 'dictionaryElement' 'list', 'number',
                       '_id': '0',
                       '_lineCodes': [],
                       '_space': 0,
                       '_tab': 0,
                       '_name': "testScript",
                       '_libImport': [
                           {'_type': 'libImport',
                            '_id': '1',
                            '_lineCodes': [],
                            '_space': 0,
                            '_tab': 0,
                            '_pyCode': [],
                            '_name': 'DesignParameters',
                            },
                           {'_type': 'libImport',
                            '_id': '2',
                            '_lineCodes': [],
                            '_space': 0,
                            '_tab': 0,
                            '_pyCode': [],
                            '_name': 'StickDiagram',
                            },
                           {'_type': 'libImport',
                            '_id': '3',
                            '_lineCodes': [],
                            '_space': 0,
                            '_tab': 0,
                            '_pyCode': [],
                            '_name': 'user_define_exceptions',
                            },
                           {'_type': 'libImport',
                            '_id': '4',
                            '_lineCodes': [],
                            '_space': 0,
                            '_tab': 0,
                            '_pyCode': [],
                            '_name': 'DRC',
                            },
                       ],
                       '_variableDefine': [],
                       '_classDefine': [
                           {'_type': 'classDefine',
                            '_id': '5',
                            '_lineCodes': [],
                            '_space': 0,
                            '_tab': 0,

                            '_name': 'DesignParameters',
                            '_inheritance': [],
                            '_statements': [],
                            '_functionDefine': [
                                {'_type': 'functionDefine',
                                 '_id': '6',
                                 '_lineCodes': [],
                                 '_space': 0,
                                 '_tab': 0,

                                 '_name': '__init__',
                                 '_arguments': [
                                     {'_type': 'argument',
                                      '_id': '7a',
                                      '_lineCodes': [],
                                      '_space': 0,
                                      '_tab': 0,

                                      '_name': 'self',
                                      '_value': [],
                                      },
                                 ],
                                 '_statements': [
                                     {'_type': 'statement',
                                      '_id': '8b',
                                      '_lineCodes': [],
                                      '_space': 0,
                                      '_tab': 0,

                                      '_pyCode': [],
                                      '_forLoop': [],
                                      '_ifControl': [],
                                      '_whileLoop': [],
                                      '_expression': [
                                          {'_type': 'expression',
                                           '_id': '9c',
                                           '_lineCodes': [],
                                           '_space': 0,
                                           '_tab': 1,
                                           '_leftBracket': [],
                                           '_rightBracket': [],
                                           '_expression': [],
                                           '_op': [],
                                           '_logic': [],
                                           '_classCall': [],
                                           '_functionCall': [],
                                           '_dictionaryCall': [],
                                           '_dictionaryDefine': [],
                                           '_listCall': [],
                                           '_listDefine': [],
                                           '_variableCall': [],
                                           '_number': [],
                                           '_string': [
                                               {'_type': 'string',
                                                '_id': '10',
                                                '_lineCodes': [],
                                                '_space': 0,
                                                '_tab': 0,

                                                '_string': ["pass"],
                                                },
                                           ],
                                           },
                                      ],
                                      '_dictionaryDefine': [],
                                      '_variableDefine': [],
                                      '_returnValueDefine': [],

                                      },

                                 ],
                                 '_pyCode': [],
                                 },
                            ],
                            '_pyCode': [],
                            },

                       ],
                       '_functionDefine': [],
                       '_statements': [],
                       '_pyCode': [],
                       }
    _tmpObj = QtDesinConstraint()
    _tmpObj._ParseTree = _tmpConstraints


def main1():
    designParameter = dict(
        _ODLayer=dict(_id=0, _DesignParametertype=1, _Layer=None, _Datatype=1, _XYCoordinates=[], _XWidth=400,
                      _YWidth=400),
        # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
        _WELLBodyLayer=dict(_id=1, _DesignParametertype=1, _Layer=None, _Datatype=1, _XYCoordinates=[], _XWidth=400,
                            _YWidth=400),
        _Name=dict(_id=2, _DesignParametertype=5, _Name='NMOS'),
        _GDSFile=dict(_id=3, _DesignParametertype=4, _GDSFile=None),
        _Sref0=dict(_DesignParametertype=3, _DesignObj=None, _XYCoordinates=[], _Reflect=None, _Angle=None, _id=6,
                    _Ignore=None, _ElementName=dict(_id=7, _DesignParametertype=5, _Name='NMOS'), ),
    )
    _tmpObj = QtDesignParameter()
    # _tmpObj._DesignParameter = designParameter["_Sref0"]
    # print(_tmpObj._findSubHierarchy())


def main2():
    _tmpObj = QtProject()
    _tmpObj._loadDesignsFromGDS(
        _file="C:/1/OneDrive - postech.ac.kr/workSpace/research/BottomUpDesignProject/Project20190524/PyQTInterface/inv_test_streamout.gds",
        _topModuleName="test")

    _tmpObj._UpdateXYCoordinateForDisplay(_id="inv_slvt_std0", _ParentName="inv_slvt_std")
    _tmpObj._UpdateXYCoordinateForDisplay(_id="M1V1M2_CDNS_4725498843400", _ParentName="M1V1M2_CDNS_472549884340")

    _tmpObj = QtProject()
    _tmpObj._loadDesignsFromGDS(
        _file="C:/1/OneDrive - postech.ac.kr/workSpace/research/BottomUpDesignProject/Project20190524/PyQTInterface/SSTSegX1.gds",
        _topModuleName="SSTSegX1")
    _tmpObj._UpdateXYCoordinateForDisplay(
        _id="SWLeftInMUXInDriverInvertedInSSTDrvWPreDrvInDriverInSSTDrvSegX1InSSTDrvTXP19",
        _ParentName="SWLeftInMUXInDriverInvertedInSSTDrvWPreDrvInDriverInSSTDrvSegX1InSSTDrvTXP")


def main3():
    _tmpObj = QtProject()
    _tmpObj._loadDesignsFromGDS(
        _file="./PyCodes/sref2.gds",
        _topModuleName="sref2")
    print('DesignParameter: ', _tmpObj._DesignParameter)
    print('_HierarchyFromRootForDesignParameter {} '.format('path'),
          _tmpObj._HierarchyFromRootForDesignParameter(_ParentName='path', _id='path0'))
    print('_XYCoordinatesForDisplay ', _tmpObj._DesignParameter['path']['path0']._XYCoordinatesForDisplay)
    _tmpObj._UpdateXYCoordinateForDisplay(_ParentName='path', _id='path0')
    print('_XYCoordinatesForDisplay ', _tmpObj._DesignParameter['path']['path0']._XYCoordinatesForDisplay)


def main4():
    _tmpObj = QtProject()
    _tmpObj._loadDesignsFromGDS(
        _file="./PyCodes/sref2.gds",
        _topModuleName="sref2")
    print('DesignParameter: ', _tmpObj._DesignParameter)
    _tmpObj._UpdateXYCoordinatesForDisplay(_ParentName='path')
    print('monitor for display ', _tmpObj._DesignParameter['path']['path0']._XYCoordinatesForDisplay)
    _tmpObj._resetXYCoordinatesForDisplay()
    print('monitor for display ', _tmpObj._DesignParameter['path']['path0']._XYCoordinatesForDisplay)
    _tmpObj._UpdateXYCoordinatesForDisplay(_ParentName='sref2')
    print('monitor for display ', _tmpObj._DesignParameter['sref1']['sref10']._XYCoordinatesForDisplay)
    print('monitor for display ', _tmpObj._DesignParameter['path']['path0']._XYCoordinatesForDisplay)
    _tmpObj._resetXYCoordinatesForDisplay()
    print('monitor for display ', _tmpObj._DesignParameter['sref1']['sref10']._XYCoordinatesForDisplay)
    print('monitor for display ', _tmpObj._DesignParameter['path']['path0']._XYCoordinatesForDisplay)


def main5():
    _tmpObj = QtProject()
    _tmpObj._loadDesignsFromGDS(
        _file="./PyCodes/SSTSegX1.gds",
        _topModuleName="SSTDrvWPreDrvInDriverInSSTDrvSegX1InSSTDrvTXP")
    # print('DesignParameter: ', _tmpObj._DesignParameter)
    _tmpObj._UpdateXYCoordinatesForDisplay(_ParentName='SSTDrvWPreDrvInDriverInSSTDrvSegX1InSSTDrvTXP')


if __name__ == "__main__":
    # execute only if run as a script
    # main()
    # main1()
    # main2()
    # main3()
    # main4()
    main5()