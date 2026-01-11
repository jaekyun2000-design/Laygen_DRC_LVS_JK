from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyCodes import QTInterfaceWithAST
import re
import copy

print("*********************Constraint Template file load Start")

class _TemplateManageWidget(QWidget):

    send_TemplateName_signal = pyqtSignal(str)

    def __init__(self, templateDict=None):
        super().__init__()
        self.templateDict = templateDict
        self.initUI()

    def initUI(self):
        selectButton = QPushButton("Select",self)

        selectButton.clicked.connect(self.on_selectBox_accepted)

        self.ListWidget = QListWidget()

        self.ListWidget.itemDoubleClicked.connect(self.on_selectBox_accepted)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(selectButton)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(setupBox)
        vbox.addWidget(self.ListWidget)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)


        self.Listshow()
        self.setLayout(vbox)

        self.setWindowTitle('Template')
        # self.setGeometry(300,300,500,500)
        self.show()

    def Listshow(self):
        for templateList in self.templateDict:
            self.ListWidget.addItem(QListWidgetItem(templateList))

    def on_selectBox_accepted(self):
        try:
            self.send_TemplateName_signal.emit(self.ListWidget.currentItem().text())        #Current Module Name emit!!
        except:
            print("no list is selected")
        self.destroy()

    def on_createBox_accepted(self):
        pass

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_selectBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()

class _VariableListWidget(QWidget):

    send_VariableName_signal = pyqtSignal(str)

    def __init__(self, variableList=None):
        super().__init__()
        self.variableList = variableList
        self.initUI()

    def initUI(self):
        selectButton = QPushButton("Select",self)

        selectButton.clicked.connect(self.on_selectBox_accepted)

        self.ListWidget = QListWidget()
        self.ListWidget.itemDoubleClicked.connect(self.on_selectBox_accepted)

        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(selectButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        # vbox.addLayout(setupBox)
        vbox.addWidget(self.ListWidget)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)


        self.Listshow()
        self.setLayout(vbox)

        self.setWindowTitle('VariableList to Variable Call')
        self.setGeometry(300,300,500,500)
        self.show()

    def Listshow(self):
        for variableName in self.variableList:
            try:
                self.ListWidget.addItem(QListWidgetItem(variableName))
            except:
                pass

    def on_selectBox_accepted(self):
        try:
            self.send_VariableName_signal.emit(self.ListWidget.currentItem().text())        #Current Module Name emit!!
        except:
            print("no list is selected")
        self.destroy()

    def on_createBox_accepted(self):
        pass

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.on_selectBox_accepted()
        elif QKeyEvent.key() == Qt.Key_Escape:
            self.destroy()

class _Template():
    def __init__(self):
        pass
    def createConstraintFromTemplate(self,_templateDict,_QTObj,_ModuleName,_parent=None,_parentKey=None):       #Read Dictionary and Create Constraint based on dictionary
        for key in _templateDict:
            tmpkey = re.sub(r'\d','',key)
            _designConstraintID = _QTObj._qtProject._getDesignConstraintId(_ModuleName)
            _newConstraintID = (_ModuleName + str(_designConstraintID))
            _QTObj._qtProject._createNewDesignConstraint(_id = _newConstraintID, _type= tmpkey, _ParentName= _ModuleName)

            self.set_type_initial_value(key,_QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID])
            for key2 in _templateDict[key]:
                if type(_templateDict[key][key2]) == list or type(_templateDict[key][key2])== str or type(_templateDict[key][key2])== int or type(_templateDict[key][key2])== float:
                    _QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID]._setDesignConstraintValue(key2,_templateDict[key][key2])
                    # if _parent != None:
                    #     _QTObj._qtProject._DesignConstraint[_ModuleName][_parent]._setDesignConstraintValue(key,_QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID])
                else:
                    self.createConstraintFromTemplate(_templateDict=_templateDict[key][key2],_QTObj=_QTObj,_ModuleName=_ModuleName,_parent=_newConstraintID,_parentKey=key2)
                    # if _parent != None:
                    #     _QTObj._qtProject._DesignConstraint[_ModuleName][_parent]._setDesignConstraintValue(key,_QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID])

            if _parent != None:
                        # if key2 == '_name':
                        #     constraintValue = _QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID]._ParseTree[key2]
                        # else:

                        # if _parentKey == "_statements" or _parentKey == "_arguments" or _parentKey == "_libImport" or _parentKey == "_dictionaryElements" or _parentKey == "_functionDefine":
                try:
                    constraintValue = _QTObj._qtProject._DesignConstraint[_ModuleName][_parent]._readDesignConstraintValue(_index=_parentKey)
                    constraintValue.append(_QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID]._ParseTree)
                except:
                    constraintValue = [_QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID]._ParseTree]
                    _QTObj._qtProject._DesignConstraint[_ModuleName][_parent]._setDesignConstraintValue(key,constraintValue)

            else:
                return _QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID]
                    # else:
                    #     constraintValue = [_QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID]._ParseTree]
                    #     _QTObj._qtProject._DesignConstraint[_ModuleName][_parent]._setDesignConstraintValue(key,constraintValue)

                    # _QTObj._qtProject._DesignConstraint[_ModuleName][_parent]._setDesignConstraintValue(key,_QTObj._qtProject._DesignConstraint[_ModuleName][_newConstraintID])

                # constraintValue= parentConstraint._readDesignConstraintValue(_index=constraintType)
                # constraintValue.append(DesignConstraint._ParseTree)
                # parentConstraint._setDesignConstraintValue(_index=constraintType,_value=constraintValue)

    def set_type_initial_value(self,type,constraint):
        if type == "pyCode":
            _ParseTree = ["_name","_file"]
        elif type == "scriptDefine":
            _ParseTree = ["_name","_libImport","_variableDefine","_classDefine","_functionDefine","_statements","_pyCode"]
        elif type == "libImport":
            _ParseTree = ["_name","_pyCode"]
        elif type == "classDefine":
            _ParseTree = ["_name","_inheritance","_statements","_functionDefine","_pyCode"]
        elif type == "classCall":
            _ParseTree = ["_name","_arguments"]
        elif type == "functionDefine":
            _ParseTree = ["_name","_arguments","_statements","_pyCode"]
        elif type == "functionCall":
            _ParseTree = ["_name","_arguments"]
        elif type == "argument":
            _ParseTree = ["_name","_value"]
        elif type == "statement":
            _ParseTree = ["_pyCode","_forLoop","_ifControl","_whileLoop","_expression","_dictionaryDefine","_variableDefine","_returnValueDefine"]
        elif type == "forLoop":
            _ParseTree = ["_index","_condition","_statements"]
        elif type == "condition":
            _ParseTree = ["_list"]
        elif type == "whileLoop":
            _ParseTree = ["_logic","_statements"]
        elif type == "ifControl":
            _ParseTree = ["_ifLogic","_elifLogic","_elseLogic"]
        elif type == "ifLogic":
            _ParseTree = ["_ifLogic","_elifLogic","_statements"]
        elif type == "logic":
            _ParseTree = ["_leftBracket","_rightBracket","_logic","_logicOp"]
        elif type == "logicOp":
            _ParseTree = ["_logicOp"]
        elif type == "expression":
            _ParseTree = ["_leftBracket","_rightBracket","_expression","_op","_logic","_classCall","_functionCall","_dictionaryCall","_dictionaryDefine","_listCall","_listDefine","_variableCall","_number","_string"]
        elif type == "op":
            _ParseTree = ["_op"]
        elif type == "variableDefine":
            _ParseTree = ["_variable","_expression"]
        elif type == "variableCall":
            _ParseTree = ["_variable"]
        elif type == "variable":
            _ParseTree = ["_name"]
        elif type == "dictionaryUpdate":
            _ParseTree = ["_variable","_dictionaryElements"]
        elif type == "dictionaryDefine":
            _ParseTree = ["_dictionaryElements"]
        elif type == "dictionaryCall":
            _ParseTree = ["_variable","_key"]
        elif type == "dictionaryElement":
            _ParseTree = ["_dictionaryElement"]
        elif type == "listDefine":
            _ParseTree = ["_var","_rangeFunction","_forLoopInList"]
        elif type == "listCall":
            _ParseTree = ["_variable","_index"]
        elif type == "number":
            _ParseTree = ["_value"]
        elif type == "string":
            _ParseTree = ["_string"]
        else:
            return

        for _constraintType in _ParseTree:
            constraint._setDesignConstraintValue(_constraintType,[])

    def digging(self,):
        pass

    def receiveDesignParameters(self,designParameterList,_QTObj,_ModuleName,type):
        if type == None:
            return None
        elif type == 0:     #dictionaryElement define macro
            constraintList = []
            for designParameter in designParameterList:
                tmpTemplateDict = dict(
                    dictionaryElement = dict(
                        _dictionaryElement = []
                    )
                )
                tmpTemplateDict['dictionaryElement']['_dictionaryElement'].append(designParameter['_DesignParameterName'])
                tmpTemplateDict['dictionaryElement']['_dictionaryElement'].append(self.designParameter2defineString(designParameter))
                constraint = self.createConstraintFromTemplate(tmpTemplateDict,_QTObj,_ModuleName)
                constraintList.append(constraint)
            return constraintList
        elif type == 1 :    #variable call macro
            constraintList = []
            for designParameter in designParameterList:
                # name = designParameter['_id']+"(DP)"
                name = 'self._DesignParameter[\'' + designParameter['_DesignParameterName'] + '\']'
                # name = designParameter['_DesignParameterName']
                tmpTemplateDict = dict(
                    variableCall = dict(
                        _variable = dict(
                            variable = dict(
                                _name = name
                            )
                        )
                    )
                )
                constraint = self.createConstraintFromTemplate(tmpTemplateDict,_QTObj,_ModuleName)
                constraintList.append(constraint)
            return constraintList
        elif type == 2 or type == 3:
            constraintList = []
            for designParameter in designParameterList:
                if designParameter['_DesignParametertype'] !=1 : #Only Boundary Element Support
                    continue
                else:
                    name = 'self._DesignParameter[\'' + designParameter['_DesignParameterName'] + '\']'
                    if type == 2:
                        name += "['_XWidth']"
                    else:
                        name += "['_YWidth']"
                    tmpTemplateDict = dict(
                        variableCall = dict(
                            _variable = dict(
                                variable = dict(
                                    _name = name
                                )
                            )
                        )
                    )
                    constraint = self.createConstraintFromTemplate(tmpTemplateDict,_QTObj,_ModuleName)
                    constraintList.append(constraint)
            return constraintList
        elif type == 4:
            constraintList = []
            for designParameter in designParameterList:
                # name = designParameter['_id']+"(DP)"
                name = 'self._DesignParameter[\'' + designParameter['_DesignParameterName'] + '\']'+"['_XYCoordinates']"
                # name = designParameter['_DesignParameterName']
                tmpTemplateDict = dict(
                    variableCall = dict(
                        _variable = dict(
                            variable = dict(
                                _name = name
                            )
                        )
                    )
                )
                constraint = self.createConstraintFromTemplate(tmpTemplateDict,_QTObj,_ModuleName)
                constraintList.append(constraint)
            return constraintList

    def receiveVariableName(self,variableName,_QTObj,_ModuleName):
        tmpTemplateDict = dict(
            variableCall = dict(
                _variable = dict(
                    variable = dict(
                        _name = variableName
                    )
                )
            )
        )
        constraint = self.createConstraintFromTemplate(tmpTemplateDict,_QTObj,_ModuleName)
        return constraint

    def receiveDesignConstraints(self,designConstraintList,_QTObj,_ModuleName):

        constraintList = []
        # for designConstraint in designConstraintList:
        tmpTemplateDict = dict()
        tmpTemplateDict = self.constraintToTemplate(designConstraintList._ParseTree)
        constraint = self.createConstraintFromTemplate(tmpTemplateDict,_QTObj,_ModuleName)
        return constraint
        # print(1)
        #
        # for key in designConstraintList._ParseTree:
        #     if key == "_type":
        #         type = designConstraintList._ParseTree[key]
        #         tmpTemplateDict[type] = dict()
        #     print(key)
            # tmpTemplateDict = dict()

    def constraintToTemplate(self,parseTree,number=None):
        if number == None:
            number = ""
        _type = parseTree["_type"] + str(number)
        tmpDictionary = dict()
        tmpDictionary[_type] = dict()
        for key in parseTree:
            if key == '_functionDefine':
                print(1)
            # if key == "_type":
            #     _type = parseTree[key]
            #     parentDictionary[_type] = dict()
        # else:
            _value = parseTree[key]
            if key == "_type" or key == "_id" or _value == None:
                continue
            if type(_value) == list:

                if len(_value) == 0:
                    continue
                if type(_value[0]) == dict:
                    tmpDictionary[_type][key]= dict()
                    for i in range(0,len(_value)):
                        tmpD = self.constraintToTemplate(_value[i],i)
                        for name in tmpD:
                            tmpDictionary[_type][key][name] = tmpD[name]
                else:
                    tmpDictionary[_type][key] = _value

            elif type(_value) == str or type(_value) == int or type(_value) == float:
                tmpDictionary[_type][key] = _value
        return tmpDictionary




    def designParameter2defineString(self,designParameter):
        dataType = designParameter['_DesignParametertype'] #number
        layer = designParameter['_Layer']              #string

        if dataType == 1:
            s_type = "_BoundaryElement"
        elif dataType == 2:
            s_type = "_PathElement"
        elif dataType == 3:
            s_type = "_BoundaryElement"
        else:
            print("Undefined Type Error")
            return

        DeclarationString = "self."+s_type+"Declaration"
        if dataType == 1 or dataType == 2:
            DeclarationString += "(_Layer=DesignParameters._LayerMapping['"+layer+"'][0],_Datatype=DesignParameters._LayerMapping['"+layer+"'][1],_XYCoordinates=[],"
            if dataType == 1:
                Xwidth = str(int(designParameter['_XWidth']))
                Ywidth = str(int(designParameter['_YWidth']))
                DeclarationString += "_XWidth="+Xwidth+",_YWidth="+Ywidth+")"
            else:
                width = str(int(designParameter['_Width']))
                DeclarationString += "_Width="+width+")"

        # print(DeclarationString)
        return DeclarationString


templateDict = dict()

templateDict['MakeClassFromStickDiagram']=dict(
    classDefine = dict(
        _inheritance = dict(
            classCall = dict(
                _name = "StickDiagram._StickDiagram"
            )
        ),
        _statements = dict(
            statement = dict(
                _variableDefine = dict(
                    variableDefine = dict(
                        _variable = dict(
                            variable = dict(
                                _name = "_ParametersForDesignCalculation"
                            )
                        ),
                        _expression = dict(
                            expression =dict(
                                _dictionaryDefine = dict(
                                    dictionaryDefine = dict( )
                                )
                            )
                        )
                    )
                )
            )
        ),

        _functionDefine = dict(
            functionDefine = dict(
                _name = "__init__",
                _arguments = dict(
                    argument = dict(
                        _name = "self"
                    ),
                    argument2 = dict(
                        _name = "_DesignParameter",
                        _value = ["None"]
                    ),
                    argument3 = dict(
                        _name = "_Name",
                        _value = ["None"]
                    )
                ),
                _statements = dict(
                    statement = dict(
                        _ifControl = dict(
                            ifControl = dict(
                                _ifLogic = dict(
                                    ifLogic = dict(
                                        _ifLogic = dict(
                                            logic = dict(
                                                _logic = dict(
                                                    variableCall = dict(
                                                        _variable = dict(
                                                            variable = dict(
                                                                _name = "_DesignParameter"
                                                            )
                                                        )
                                                    ),
                                                    statement = dict(
                                                        _expression = dict(
                                                            expression = dict(
                                                                _string = dict(
                                                                    string = dict(
                                                                        _string = ["None"]
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                ),
                                                _logicOp = dict(
                                                    logicOp = dict(
                                                        _logicOp = ["!="]
                                                    )
                                                )
                                            )
                                        ),
                                        _statements = dict(
                                            statement = dict(
                                                _variableDefine = dict(
                                                    variableDefine = dict(
                                                        _variable = dict(
                                                            variable = dict(
                                                                _name = "self._DesignParameter"
                                                            )
                                                        ),
                                                        _expression = dict(
                                                            expression = dict(
                                                                _variableCall = dict(
                                                                    variableCall = dict(
                                                                        _variable = dict(
                                                                            variable = dict(
                                                                                _name = "_DesignParameter"
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                _elseLogic = dict(
                                    ifLogic = dict(
                                        _statements = dict(
                                            statement = dict(
                                                _variableDefine = dict(
                                                    variableDefine = dict(
                                                        _variable = dict(
                                                            variable = dict(
                                                                _name = "self._DesignParameter"
                                                            )
                                                        ),
                                                        _expression = dict(
                                                            expression =dict(
                                                                _dictionaryDefine = dict(
                                                                    dictionaryDefine = dict( )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    statement2 = dict(
                        _ifControl = dict(
                            ifControl = dict(
                                _ifLogic = dict(
                                    ifLogic = dict(
                                        _ifLogic = dict(
                                            logic = dict(
                                                _logic = dict(
                                                    variableCall = dict(
                                                        _variable = dict(
                                                            variable = dict(
                                                                _name = "_Name"
                                                            )
                                                        )
                                                    ),
                                                    expression = dict(
                                                        _string = dict(
                                                            string = dict(
                                                                _string = ["None"]
                                                            )
                                                        )
                                                    )
                                                ),
                                                _logicOp = dict(
                                                    logicOp = dict(
                                                        _logicOp = ["!="]
                                                    )
                                                )
                                            ),
                                        ),
                                        _statements = dict(
                                            statement = dict(
                                                _expression = dict(
                                                    expression = dict(
                                                        _dictionaryCall = dict(
                                                            dictionaryCall = dict(
                                                                _variable = dict(
                                                                    variable = dict(
                                                                        _name = "self._DesignParameter['_Name']"
                                                                    )
                                                                    # variable = dict(
                                                                    #     _name = "Test"
                                                                    # )
                                                                ),
                                                                _key = ["'_Name'"]
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )

)

templateDict['scriptDefine']=dict(
    scriptDefine = dict(
        _libImport = dict(
            libImport1 = dict(
                _name = "StickDiagram"
            ),
            libImport2 = dict(
                _name = "DesignParameters"
            ),
            libImport3 = dict(
                _name = "user_define_exceptions"
            ),
            libImport4 = dict(
                _name = "DRC"
            ),
            libImport5 = dict(
                _name = "ftplib"
            ),
            libImport6 = dict(
                _name = "base64"
            ),
            libImport7 = dict(
                _name = "sys"
            ),

        )
    )
)


templateDict['IfLogic']=dict(
    statement = dict(
        _ifControl = dict(
            ifControl = dict(
                _ifLogic = dict(
                    ifLogic = dict(
                        _ifLogic = dict(
                            logic = dict(
                                _logicOp = dict(
                                    logicOp = dict()
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

templateDict['functionDefine']=dict(
    functionDefine = dict(
        _arguments = dict(
            argument = dict(
                _name = "self"
            )
        ),
        _statements = dict(
            statement = dict()
        )
    )
)

templateDict['functionCall']=dict(
    statement = dict(
        _expression = dict(
            expression = dict(
                _functionCall = dict(
                    functionCall = dict(
                        _arguments = dict(
                            argument = dict(
                                _name = "\\None"
                            )
                        )
                    )
                )
            )
        )
    )
)

templateDict['variableDefine']=dict(
    statement = dict(
        _variableDefine = dict(
            variableDefine = dict(
                _variable = dict(
                    variable = dict()
                ),
                # _expression = dict(
                #     expression = dict()
                # )
            )
        )
    )
)

templateDict['variableDefine=1']=dict(
    statement = dict(
        _variableDefine = dict(
            variableDefine = dict(
                _variable = dict(
                    variable = dict()
                ),
                _expression = dict(
                    expression = dict(
                        _number = dict(
                            number = dict(
                                _value = 1
                            )
                        )
                    )
                )
            )
        )
    )
)

templateDict['variableDefine=2']=dict(
    statement = dict(
        _variableDefine = dict(
            variableDefine = dict(
                _variable = dict(
                    variable = dict()
                ),
                _expression = dict(
                    expression = dict(
                        _number = dict(
                            number = dict(
                                _value = 2
                            )
                        )
                    )
                )
            )
        )
    )
)

templateDict['variableDefine=None']=dict(
    statement = dict(
        _variableDefine = dict(
            variableDefine = dict(
                _variable = dict(
                    variable = dict()
                ),
                _expression = dict(
                    expression = dict(
                        _string = dict(
                            string = dict(
                                _string = ['None']
                            )
                        )
                    )
                )
            )
        )
    )
)

templateDict['variableDefine=str']=dict(
    statement = dict(
        _variableDefine = dict(
            variableDefine = dict(
                _variable = dict(
                    variable = dict()
                ),
                _expression = dict(
                    expression = dict(
                        _string = dict(
                            string = dict(

                            )
                        )
                    )
                )
            )
        )
    )
)



templateDict['variableCall']=dict(
    variableCall = dict(
        _variable = dict(
            variable = dict()
        )
    )
)

templateDict['dictionaryElementWithKeyAndStatement'] = dict(
    dictionaryElement = dict(
        _dictionaryElement = dict(
            statement1 = dict(
                _expression = dict(
                    expression = dict(
                        _string = dict(
                            string = dict(
                                _string = "EnterKeyValueHere"
                            )
                        )
                    )
                )
            ),
            statement2 = dict(
                _expression = dict(
                    expression = dict(
                        _string = dict(
                            string = dict(
                                _string = "testString"
                            )
                        )
                    )
                )
            )
        )
    )
)

templateDict['string'] = dict(
    expression = dict(
        _string = dict(
            string = dict()
        )
    )
)
templateDict['number'] = dict(
    expression = dict(
        _number = dict(
            number = dict()
        )
    )
)

templateDict['forControlRange'] = dict(
    statement = dict(
        _forLoop = dict(
            forLoop = dict(
                _index = dict(
                    variable = dict()
                ),
                _condition = dict(
                    condition = dict(
                        _list = dict(
                            listDefine = dict(
                                _rangeFunction = dict(
                                    functionCall = dict(
                                        _name = "range",
                                        _arguments = dict(
                                            argument1 = dict(),
                                            argument2 = dict()
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)
templateDict['forControlinList'] = dict(
    statement = dict(
        _forLoop = dict(
            forLoop = dict(
                _index = dict(
                    variable = dict()
                ),
                _condition = dict(
                    variableCall = dict(
                        _variable = dict(
                            variable = dict()
                        )
                    )
                )
            )
        )
    )

)

templateDict['logicValueDefine'] = dict(
    expression = dict(
        _logic = dict(
            logic = dict(
                _logicOp = dict(
                    logicOp = dict(
                        _logicOp = ["="]
                    )
                )
            )
        )
    )
)

templateDict['logic =='] = dict(
    expression = dict(
        _logic = dict(
            logic = dict(
                _logicOp = dict(
                    logicOp = dict(
                        _logicOp = ["=="]
                    )
                )
            )
        )
    )
)

templateDict['[]'] = dict(
    expression = dict(
        _string = dict(
            string = dict(
                _string = ["[]"]
            )
        )
    )
)

templateDict['tmp']=dict(
    variableCall = dict(
        _variable = dict(
            variable = dict(
                _name = "tmp"
            )
        )
    )
)


templateDict['tmp=[]'] = dict(
    statement = dict(
        _expression = dict(
            expression = dict(
                _logic = dict(
                    logic = dict(
                        _logicOp = dict(
                            logicOp = dict(
                                _logicOp = ["="]
                            )
                        ),
                        _logic = dict(
                            variableCall = dict(
                                _variable = dict(
                                    variable = dict(
                                        _name = "tmp"
                                    )
                                )
                            ),
                            expression = dict(
                                _string = dict(
                                    string = dict(
                                        _string = ["[]"]
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

templateDict['0'] = dict(
    expression = dict(
        _number = dict(
            number = dict(
                _value = ['0']
            )
        )
    )
)
templateDict['None'] = dict(
    variableCall = dict(
        _variable = dict(
            variable = dict(
                _name = "None"
            )
        )
    )
)
templateDict['printFunction'] = dict(
    statement = dict(
        _expression = dict(
            functionCall = dict(
                _name = "print",
                _arguments = dict(
                    argument = dict(
                        _name = '\\None'
                    )
                )
            )
        )
    )
)

templateDict['_DRCObj'] = dict(
    statement = dict(
        _variableDefine = dict(
            variableDefine = dict(
                _variable = dict(
                    variable = dict(
                        _name = "_DRCObj"
                    )
                ),
                _expression = dict(
                    functionCall = dict(
                        _name = "DRC.DRC"
                    )
                )
            )
        )
    )
)

templateDict['WhileTrue'] = dict(
    statement = dict(
        _whileLoop = dict(
            whileLoop = dict(
                _logic = dict(
                    logic =dict(
                        _logic =dict(
                            expression = dict(
                                _string = dict(
                                    string = dict(
                                        _string =["True"]
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)
# templateDict['logicForAnythin']
# templateDict['functionCall']=dict(
#     functionCall = dict(
#         _function = function
#     )
# )
print("************************Constraint Template file load Complete")











if __name__ == '__main__':
    _QTObj = QTInterface.QtInterFace()
    _QTObj._createProject("ProjectForEasyDebug")
    template = _Template()

    template.createConstraintFromTemplate(_templateDict=templateDict['MakeClassFromStickDiagram'],_QTObj=_QTObj,_ModuleName="testModule")
