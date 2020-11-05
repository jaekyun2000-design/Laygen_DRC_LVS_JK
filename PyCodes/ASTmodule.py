import ast
import astunparse
import re
import copy
import inspect, sys

#stmtList = ["If","While","For","Try","With","FunctionDef","ClassDef","Expression","Assert","Assign","Pass","Del","Return","Raise","Break","Continue","Import","Name","Num"]


class _Custom_AST_API():
    def __init__(self):
        self.stmtList = []
        self.classList = []
        self._loadASTclassList()

    def _loadASTclassList(self):  # This function creates references when python version changes and ASTclass types are changed.
        for name, obj in inspect.getmembers(sys.modules['ast']):
            if inspect.isclass(obj):
                self.stmtList.append(name)
                self.classList.append(obj)

    def _createASTwithName(self,_name):
        _index = self.stmtList.index(_name)
        _tmp = self.classList[_index]
        return _tmp()


def _convertPyCodeToASTDict(_pyCode):
    _AST = ast.parse(_pyCode)

    _ASTDict = dict()
    for stmt in _AST.body:
        _key = _getASTtype(stmt)
        _ASTDict[_key] = dict()
        for field in stmt._fields:
            _ASTDict[_key][field] = None

        if 'body' in dir(stmt):
            for stmt2 in stmt.body:
                _convertPyCodeToASTDict()

# def _searchASTid(_targetASTList):



def _searchASTOG(_targetASTList):
    _ASTlist = list()    #Hierarchy search....?
    _IDlist = list()
    if type(_targetASTList) != list:
        _targetASTList = [_targetASTList]

    for stmt in _targetASTList:  # stmt is AST object (In this case Input is )
        _key = _getASTtype(stmt)
        _ASTlist.append(stmt)
        try:
            _IDlist.append(stmt._id)
        except:
            _IDlist.append("None")
        for field in stmt._fields:  # field is AST object's variable for storing values.
            _childASTList = list()
            _childIDlist = list()
            if field == "left":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.left)
            elif field == "right":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.right)
            elif field == "op":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.op)

            elif field == "ops":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.ops)

            elif field == "comparators":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.comparators)

            elif field == "body":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.body)

            elif field == "targets":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.targets)

            elif field == "test":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.test)

            elif field == "target":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.target)

            elif field == "iter":
                _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.iter)

            elif field == "value":
                try:
                    _childASTList, _childIDlist = _searchAST(_targetASTList=stmt.value)
                except:
                    pass

            _ASTlist = _ASTlist + _childASTList
            _IDlist = _IDlist + _childIDlist
    return  _ASTlist, _IDlist


def _searchAST_Legacy_20200410(_targetASTList):
    _ASTlist = list()    #Hierarchy search....?
    _IDlist = list()

    # _targetTMP = copy.deepcopy(_targetASTList)
    _targetTMP = _targetASTList

    if type(_targetTMP) != list:
        _targetTMP = [_targetTMP]

    for stmt in _targetTMP:  # stmt is AST object (In this case Input is )
        _ASTlist.append(stmt)
        try:
            _IDlist.append(stmt._id)
        except:
            _IDlist.append("None")

        tmpDict = vars(stmt)
        for field in tmpDict:
            _childASTList = list()
            _childIDlist = list()
            #if type(tmpDict[field]) == list:
            try:
                _childASTList, _childIDlist = _searchAST(_targetASTList=tmpDict[field])
            except:
                pass

            _ASTlist = _ASTlist + _childASTList
            _IDlist = _IDlist + _childIDlist
    return  _ASTlist, _IDlist
def _searchAST(_topAST):
    walker = ast.walk(_topAST)
    tmpList = []
    for node in walker:
        tmpList.append(node)
    return tmpList

def _searchSTMT(_targetSTMTList):
    _IDlist = list()
    if type(_targetSTMTList) != list:
        _targetSTMTList = [_targetSTMTList]

    for stmt in _targetSTMTList:
        _type = stmt['_type']
        _IDlist.append(stmt['_id'])
        for _key in stmt:
            if _key == "_type" or _key == '_id':
                continue
            try:
                _childIDlist = list()
                if type(stmt[_key]) == list:
                    _childIDlist = _searchSTMT(stmt[_key])
                else:
                    try:
                        _IDlist.append(stmt[_key]['_id'])
                    except:
                        pass
                _IDlist = _IDlist + _childIDlist
            except:
                pass
    return _IDlist



def _convertPyCodeToSTMTlistOG(_targetASTList):
    _STMTList = list()

    if type(_targetASTList) != list:
        _targetASTList = [_targetASTList]

    for stmt in _targetASTList:  # stmt is AST object (In this case Input is )
        _STMTdict = dict()
        _key = _getASTtype(stmt)
        _STMTdict['_type'] = _key
        try:
            _STMTdict['_id'] = stmt._id
        except:
            _STMTdict['_id'] = 'UNVALID'
     #   _ASTList.append(_key)
        for field in stmt._fields:  # field is AST object's variable for storing values.            #Field 대신에 key를 이용해 접근해 보자. dir?? 을 해야하나
            _STMTdict[field] = None

            if field == "n":
                _STMTdict[field] = stmt.n
            elif field == "s":
                _STMTdict[field] = stmt.s
            elif field == "id":
                _STMTdict[field] = stmt.id

            # elif field == "value":
            #     valueClass = _getASTtype(stmt.value)
            #     if valueClass == "Constant":
            #         _STMTdict[field] = stmt.value.n


            elif field == "left":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.left)
                _STMTdict[field] = _childSTMTList[0]
            elif field == "right":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.right)
                _STMTdict[field] = _childSTMTList[0]
            elif field == "op":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.op)
                _STMTdict[field] = _childSTMTList[0]
            elif field == "ops":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.ops)
                _STMTdict[field] = _childSTMTList
            elif field == "comparators":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.comparators)
                _STMTdict[field] = _childSTMTList
            elif field == "body":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.body)
                _STMTdict[field] = _childSTMTList
            elif field == "targets":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.targets)
                _STMTdict[field] = _childSTMTList
            elif field == "test":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.test)
                _STMTdict[field] = _childSTMTList
            elif field == "target":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.target)
                _STMTdict[field] = _childSTMTList[0]
            elif field == "iter":
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.iter)
                _STMTdict[field] = _childSTMTList[0]

            elif field == 'value':
                try:
                    _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=stmt.value)
                    _STMTdict[field] = _childSTMTList[0]
                except:
                     _STMTdict[field] = stmt.value




        _STMTList.append(_STMTdict)
    return _STMTList

def _convertPyCodeToSTMTlist(_targetASTList):       #Crucial Problem!!!!!!!  It changes original AST value
    _STMTList = list()

    _targetTMP = copy.deepcopy(_targetASTList)


    if type(_targetTMP) != list:
        _targetTMP = [_targetTMP]

    for stmt in _targetTMP:  # stmt is AST object (In this case Input is )
        #_STMTdict = dict()

        _STMTdict = vars(stmt)
        _key = _getASTtype(stmt)
        _STMTdict['_type'] = _key
        try:
            _STMTdict['_id'] = stmt._id
        except:
            _STMTdict['_id'] = 'UNVALID'

        for field in _STMTdict:
            if type(_STMTdict[field]) == list:
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=_STMTdict[field])
                _STMTdict[field] = _childSTMTList
            elif _checkAST(_STMTdict[field]) == True:
                _childSTMTList = _convertPyCodeToSTMTlist(_targetASTList=_STMTdict[field])
                _STMTdict[field] = _childSTMTList[0]




        _STMTList.append(_STMTdict)
    del _targetTMP
    return _STMTList

def _convertSTMTlistToAST(_targetSTMTList):
    _topAST = None
    _astList = []

    if type(_targetSTMTList) != list:
        _targetSTMTList = [_targetSTMTList]

    for stmt in _targetSTMTList:
        _type = stmt['_type']

        if _type == "Module":
            _astList.append(ast.Module())
        elif _type == "If":
            _astList.append(ast.If())
        elif _type == "While":
            _astList.append(ast.While())
        elif _type == "For":
            _astList.append(ast.For())
        elif _type == "Try":
            _astList.append(ast.Try())
        elif _type == "With":
            _astList.append(ast.With())
        elif _type == "FunctionDef":
            _astList.append(ast.FunctionDef())
        elif _type == "ClassDef":
            _astList.append(ast.ClassDef())
        # Type for Simple STMT
        elif _type == "Expression":
            _astList.append(ast.Expression())
        elif _type == "Assert":
            _astList.append(ast.Assert())
        elif _type == "Assign":
            _astList.append(ast.Assign())
        elif _type == "Pass":
            _astList.append(ast.Pass())
        elif _type == "Del":
            _astList.append(ast.Del())
        elif _type == "Return":
            _astList.append(ast.Return())
        elif _type == "Raise":
            _astList.append(ast.Raise())
        elif _type == "Break":
            _astList.append(ast.Break())
        elif _type == "Continue":
            _astList.append(ast.Continue())
        elif _type == "Import":
            _astList.append(ast.Import())
        elif _type == "ImportFrom":
            _astList.append(ast.ImportFrom())
        elif _type == "Name":
            _astList.append(ast.Name())
        elif _type == "Store":
            _astList.append(ast.Store())
        elif _type == "BinOp":
            _astList.append(ast.BinOp())
        elif _type == "Constant":
            _astList.append(ast.Constant())
        elif _type == "Sub":
            _astList.append(ast.Sub())
        elif _type == "Load":
            _astList.append(ast.Load())
        else:
            print("Undefined AST:",_type)
            raise

        for field in _astList[-1]._fields:
            if field in stmt:
                if type(stmt[field]) == list:
                    _childAstList = _convertSTMTlistToAST(stmt[field])
                    _astList[-1].__dict__[field] = _childAstList
                elif (type(stmt[field]) == dict ) and ("_type" in stmt[field]) == True:
                    _childAST = _convertSTMTlistToAST(stmt[field])[0]
                    _astList[-1].__dict__[field] = _childAST
                else:
                    _astList[-1].__dict__[field] = stmt[field]
        _astList[-1] = ast.fix_missing_locations(_astList[-1])
    return _astList

def _returnChildIDandAST(_STMTList):
    _idToSTMTdict = dict()
    for _stmt in _STMTList:
        _idToSTMTdict[_stmt['_id']] = _stmt
        for key in _stmt:
            try:
                if type(_stmt[key]) != list and '_id' in _stmt[key]:
                    tmpID = _stmt[key]['_id']
                    _idToSTMTdict[tmpID] = _stmt[key]
                elif type(_stmt[key]) == list:
                    for _stmt2 in _stmt[key]:
                        tmpID = _stmt2['_id']
                        _idToSTMTdict[tmpID] = _stmt2
            except:
                print('debug:',key,_stmt)
    return _idToSTMTdict


def _searchSTMTlistWithIDList(_STMTList, _IDList):
    _idToSTMT = dict()
    for id in _IDList:
        _idToSTMT[id] = _searchSTMTlistWithID(_STMTList,id)
    return _idToSTMT

def _searchSTMTlistWithID(_STMTList, _ID):
    outputSTMT = None
    if type(_STMTList) != list:
        _STMTList = [_STMTList]
    for stmt in _STMTList:
        try:
            if _ID == stmt['_id']:
                return stmt
            else:
                for key in stmt:
                    #if type(stmt[key]) == list:
                    try:
                        outputSTMT = _searchSTMTlistWithID(stmt[key],_ID)
                    # else:
                    except:
                        try:
                            if stmt[key]['_id'] == _ID:
                                outputSTMT = stmt[key]
                        except:
                            pass
                    if outputSTMT != None:
                        return outputSTMT
        except:
            pass
#                        stmt[key][_ID] == ['_id']




def _convertPyCodeToASTDictUnit(_targetASTList):  #list like body[] , targets[], test[] ... etc
    _ASTDictList = list()
    _ASTList = []

    if type(_targetASTList) != list:
        _targetASTList = [_targetASTList]


    for stmt in _targetASTList:        #stmt is AST object (In this case Input is )
        _ASTDict = dict()
        _key = _getASTtype(stmt)
        _ASTDict[_key] = dict()
        _ASTList.append(_key)
        for field in stmt._fields:      #field is AST object's variable for storing values.
            _ASTDict[_key][field] = None
            if field == "n":
                _ASTDict[_key][field] = stmt.n
            elif field == "s":
                _ASTDict[_key][field] = stmt.s
            elif field == "id":
                _ASTDict[_key][field] = stmt.id
            elif field == "value":
                 # _childASTList, _childASTDictList = _convertPyCodeToASTDictUnit(_targetASTList=[stmt.value])
                 valueClass = _getASTtype(stmt.value)
                 if valueClass == "Constant":
                    _ASTDict[_key][field] = stmt.value.n

            #elif field == "test":
            #    _childASTList, _childASTDictList = _convertPyCodeToASTDictUnit(_targetASTList=[stmt.test])
            #    _fieldList = field + "List"
            #    _ASTDict[_key][field] = _childASTDictList[0]
            elif field == "left":
                _childASTList, _childASTDictList = _convertPyCodeToASTDictUnit(_targetASTList=[stmt.left])
                _fieldList = field + "List"
                _ASTDict[_key][field] = _childASTDictList[0]





            elif field == "ops":
                _childASTList, _childASTDictList = _convertPyCodeToASTDictUnit(_targetASTList=stmt.ops)
                _fieldList = field + "List"
                _ASTDict[_key][_fieldList] = _childASTList
                _ASTDict[_key][field] = _childASTDictList
            elif field == "comparators":
                _childASTList, _childASTDictList = _convertPyCodeToASTDictUnit(_targetASTList=stmt.comparators)
                _fieldList = field + "List"
                _ASTDict[_key][_fieldList] = _childASTList
                _ASTDict[_key][field] = _childASTDictList
            elif field == "body":
                _childASTList, _childASTDictList  = _convertPyCodeToASTDictUnit(_targetASTList=stmt.body)
                _fieldList = field + "List"
                _ASTDict[_key][_fieldList] = _childASTList
                _ASTDict[_key][field] = _childASTDictList


            elif field == "targets":
                _childASTList, _childASTDictList = _convertPyCodeToASTDictUnit(_targetASTList = stmt.targets)
                _fieldList = field + "List"
                _ASTDict[_key][_fieldList] = _childASTList
                _ASTDict[_key][field] = _childASTDictList

        _ASTDictList.append(_ASTDict)

    return _ASTList, _ASTDictList



def _concatenateChildASTDict(_parentAST,_childAST):
    for key in _childAST.keys():
        if key in _parentAST.keys():
            regEx = key + '\d+'
            keyName = re.search()
            key = key
def _updateSTMTListID(_id,_STMT):
    if _id != None:
        _STMT['_id'] = _id

def _updateASTDictID(_id,_ASTDict):
    if _id != None:
        _type = list(_ASTDict[1].keys())
        _ASTDict[1][_type[0]]["_id"] = _id
    return _ASTDict

def _ASTDictUpdateMissingPart(_ASTDict):
    for i in range(1, len(_ASTDict)):
        _type = list(_ASTDict[i].keys())
        _type = _type[0]
        if _type == "If":
            tmpAST = ast.If()
        elif _type == "While":
            tmpAST = ast.While()
        elif _type == "For":
            tmpAST = ast.For()
        elif _type == "Try":
            tmpAST = ast.Try()
        elif _type == "With":
            tmpAST = ast.With()
        elif _type == "FunctionDef":
            tmpAST = ast.FunctionDef()
        elif _type == "ClassDef":
            tmpAST = ast.ClassDef()
        elif _type == "Expression":
            tmpAST = ast.Expression()
        elif _type == "Assert":
            tmpAST = ast.Assert()
        elif _type == "Assign":
            tmpAST = ast.Assign()
        elif _type == "Pass":
            tmpAST = ast.Pass()
        elif _type == "Del":
            tmpAST = ast.Del()
        elif _type == "Return":
            tmpAST = ast.Return()
        elif _type == "Raise":
            tmpAST = ast.Raise()
        elif _type == "Break":
            tmpAST = ast.Break()
        elif _type == "Continue":
            tmpAST = ast.Continue()
        elif _type == "Import":
            tmpAST = ast.Import()
        elif _type == "Name":
            tmpAST = ast.Name()



        for field in tmpAST._fields:
            _ASTDict[i][_type][field] = None

    return _ASTDict




def _getASTtype(_targetAST):            #Input is specific AST object (ex: AST.If, AST.Express ....) , Output is object's ClassName
    _type = str(type(_targetAST))
    className = re.search('ast.[a-zA-Z]+', _type).group()
    className = className[4:]
    return className

def _checkAST(_target):
    try:
        _getASTtype(_target)
        return True
    except:
        return False

def _STMTListMask(_STMTList):
    for stmt in _STMTList:
        if stmt['_key'] == 'ctx':
            stmt['_hide'] = True
        else:
            stmt['_hide'] = True

        # if stmt['_key'] == "If":





#stmtList = _loadASTclassList()
#def _STMTtoAST(_targetSTMT):




if __name__ == "__main__":
    customAST = _Custom_AST_API()
    a = [ast.parse("if a ==10 : \n \t print('heelo')"), ast.parse("a=10*3")]
    code = "a= 1 \n" \
           "b = 2.0 \n" \
            "c = 'hello'\n"\
    #
    # a = ast.parse(code)
    # b= _convertPyCodeToSTMTlist(a)
    # c = _convertSTMTlistToAST(b)
    # print(astunparse.dump(a))
    #c,d = _searchAST(a)