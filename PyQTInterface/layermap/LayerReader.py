import re
import sys
import os
print("***Layer Map file load Start")

_Technology='065nm'
_CadenceServer = '141.223.86.110'
if _Technology =='065nm':
    _UploadDirectory = '/mnt/ramdisk0'
elif _Technology =='180nm':
    _UploadDirectory = '/home/alecnew1/OPUS/DesignAutomationTSMC018'
elif _Technology =='130nm':
    _UploadDirectory = '/home/alecnew1/OPUS/DesignAutomationTSMC013/workspace'
elif _Technology =='090nm':
    _UploadDirectory = '/OPUS/tsmc90WorkingSpace/gdsFile'
elif _Technology =='045nm':
    _UploadDirectory = '/OPUS/tsmc40WorkingSpace/gdsFile'
_HomeDirectory = os.getcwd()
_LayerMapping=dict()

def _ReadLayerMapFile(_LayerMapFile, CadenceVersion ):
    if CadenceVersion=='ICFB':
        _newLayerMapDictionary={}
        linenum=len(_LayerMapFile.readlines())
        _LayerMapFile.seek(0)
        _passFlag = 1
        for i in range(0, linenum):
            tmp=_LayerMapFile.readline()
            if re.match('^\s*streamLayers\s*[(]\s*$',tmp):
                while(1):
                    tmp = _LayerMapFile.readline()

                    if re.match('^\s*[)]\s*;\s*streamLayers\s+$',tmp):
                        break
                    elif re.match('^\s*[(]\s*[(]\s*"(.+)"\s*"(.+)"\s*[)]\s+(\d+)\s+(\d+)\s+(.+)\s+[)]\s*$',tmp):
                        test= re.match('^\s*[(]\s*[(]\s*"(.+)"\s*"(.+)"\s*[)]\s+(\d+)\s+(\d+)\s+(.+)\s+[)]\s*$',tmp)
                        _newLayerMapDictionary[(test.group(1),test.group(2))]=(test.group(3), test.group(4))
                        # print  '1: ', test.group(1)
                        # print  '2: ', test.group(2)
                        # print  '3: ', test.group(3)
                        # print  '4: ', test.group(4)
                        # print  '5: ', test.group(5)

                        #_newLayerMapDictionary[(test.group(1),test.group(2))]=(test.group(3), test.group(4))
                        #_newLayerMapDictionary[(test.group(1),test.group(2))]=(int(test.group(3)), int(test.group(4)))
                        #print  test.group(1), test.group(2), test.group(3), test.group(4), test.group(5)
                break
        return _newLayerMapDictionary

    elif CadenceVersion== 'VIRTUOSO':
        _newLayerMapDictionary={}
        linenum=len(_LayerMapFile.readlines())
        _LayerMapFile.seek(0)

        for i in range(0, linenum):
            tmp=_LayerMapFile.readline()
            if re.match('^\s*#.*$',tmp):
            #if (tmp[0] =='#'):
                pass
                # The line is comment. skip the current step:', tmp
            elif re.match('^\s+$',tmp):
            #elif (tmp in ['\n',  '\r\n']):
                pass
                # The line is blink. skip the current step:', tmp
            else:
                tmp2=tmp.split()
                _newLayerMapDictionary[(tmp2[0],tmp2[1])]=(int(tmp2[2]), int(tmp2[3]),tmp2[0])
        return _newLayerMapDictionary
    else :
        print('CadenceVersion has incorrect value')

def _LayerNumber2LayerName(_LayerMapping):

    _LayerNum2Name = dict()

    for _LayerCommonName in _LayerMapping:
        if _LayerMapping[_LayerCommonName][1] == 0:
            i = str(_LayerMapping[_LayerCommonName][0])
            layerName = _LayerMapping[_LayerCommonName][2]
            _LayerNum2Name[i] = layerName
    return _LayerNum2Name

def _LayerNumber2CommonLayerName(_LayerMapping):

    _LayerNum2Name = dict()

    for _LayerCommonName in _LayerMapping:
        if _LayerMapping[_LayerCommonName][1] == 0:
            i = str(_LayerMapping[_LayerCommonName][0])
            layerName = _LayerMapping[_LayerCommonName][2]
            _LayerNum2Name[i] = _LayerCommonName
    return _LayerNum2Name
#######################
# load layers
#
# '180nm':
#  '065nm':

if _Technology == '180nm':
    _LayerMapFile = open(_HomeDirectory + '/PyQTInterface/layermap/TSMC180nm/tsmc18rf.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
    _LayerNameTmp = _LayerNumber2LayerName(_LayerMappingTmp)
elif _Technology=='065nm':
    # print(_HomeDirectory)
    _LayerMapFile = open(_HomeDirectory + '/PyQTInterface/layermap/TSMC65nm/tsmcN65.layermap')
    # print(_LayerMapFile)
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
    _LayerNameTmp = _LayerNumber2LayerName(_LayerMappingTmp)
elif _Technology=='045nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC45nm/tsmcN45.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
    _LayerNameTmp = _LayerNumber2LayerName(_LayerMappingTmp)
elif _Technology=='090nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC90nm/tsmcN90rf.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
    _LayerNameTmp = _LayerNumber2LayerName(_LayerMappingTmp)
elif _Technology=='130nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC130nm/tsmc13rf.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
    _LayerNameTmp = _LayerNumber2LayerName(_LayerMappingTmp)
    # _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'ICFB')
elif _Technology=='350nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC350nm/techfile')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'ICFB')

#################    Conversion into Singlevariable   ##################################
 ############################# PIMP Layer Mapping#########################################'

if _Technology == '180nm':
    _LayerMapping.update({'PIMP':_LayerMappingTmp[('PIMP', 'drawing')]})
    # _Layernumber = _LayerMappingTmp[('NIMP', 'drawing')][0]
    # _DataType = _LayerMappingTmp[('NIMP', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'PIMP':_LayerMappingTmp[('PP', 'drawing')]})
    # _Layernumber = _LayerMappingTmp[('NP', 'drawing')][0]
    # _DataType = _LayerMappingTmp[('NP', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'PIMP':_LayerMappingTmp[('PP', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'PIMP':_LayerMappingTmp[('PP', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'PIMP':_LayerMappingTmp[('PIMP', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'PIMP':_LayerMappingTmp[('PIMP', 'drawing')]})

 ############################# PDK Layer Mapping#########################################'
if _Technology == '180nm':
    _LayerMapping.update({'PDK':(None,None)})
elif _Technology == '065nm':
    _LayerMapping.update({'PDK':_LayerMappingTmp[('PDK', 'drawing')]})
            # _Layernumber = layermapping[('PDK', 'drawing')][0]
            # _DataType = layermapping[('PDK', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'PDK':_LayerMappingTmp[('PDK', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'PDK':_LayerMappingTmp[('PDKREC', 'wellbody')]})
elif _Technology == '130nm':
    _LayerMapping.update({'PDK':(None,None)})
elif _Technology == '350nm':
    _LayerMapping.update({'PDK':(None,None)})


 ############################# NIMP Layer Mapping#########################################'

if _Technology == '180nm':
    _LayerMapping.update({'NIMP':_LayerMappingTmp[('NIMP', 'drawing')]})
    # _Layernumber = _LayerMappingTmp[('NIMP', 'drawing')][0]
    # _DataType = _LayerMappingTmp[('NIMP', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'NIMP':_LayerMappingTmp[('NP', 'drawing')]})
    # _Layernumber = _LayerMappingTmp[('NP', 'drawing')][0]
    # _DataType = _LayerMappingTmp[('NP', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'NIMP':_LayerMappingTmp[('NP', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'NIMP':_LayerMappingTmp[('NP', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'NIMP':_LayerMappingTmp[('NIMP', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'NIMP':_LayerMappingTmp[('NIMP', 'drawing')]})

 ############################ DIFF Layer Mapping#########################################'

if _Technology == '180nm':
    _LayerMapping.update({'DIFF':_LayerMappingTmp[('DIFF', 'drawing')]})
    # _Layernumber = layermapping[('DIFF', 'drawing')][0]
    # _DataType = layermapping[('DIFF', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'DIFF':_LayerMappingTmp[('OD', 'drawing')]})
            # _Layernumber = layermapping[('OD', 'drawing')][0]
            # _DataType = layermapping[('OD', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'DIFF':_LayerMappingTmp[('OD', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'DIFF':_LayerMappingTmp[('OD', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'DIFF':_LayerMappingTmp[('OD', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'DIFF':_LayerMappingTmp[('DIFF', 'drawing')]})
 ##########################    CONT Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'CONT':_LayerMappingTmp[('CONT', 'drawing')]})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'CONT':_LayerMappingTmp[('CO', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'CONT':_LayerMappingTmp[('CO', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'CONT':_LayerMappingTmp[('CO', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'CONT':_LayerMappingTmp[('CONT', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'CONT':_LayerMappingTmp[('CONT', 'drawing')]})

 #############################   METAL1 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL1':_LayerMappingTmp[('METAL1', 'drawing')]})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL1':_LayerMappingTmp[('M1', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL1':_LayerMappingTmp[('M1', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL1':_LayerMappingTmp[('M1', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL1':_LayerMappingTmp[('METAL1', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL1':_LayerMappingTmp[('METAL1', 'drawing')]})


 #############################   METAL1PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL1PIN':_LayerMappingTmp[('METAL1', 'pin')]})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL1PIN':_LayerMappingTmp[('M1', 'pin')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL1PIN':_LayerMappingTmp[('M1', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL1PIN':_LayerMappingTmp[('M1', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL1PIN':_LayerMappingTmp[('METAL1', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL1PIN':_LayerMappingTmp[('METAL1', 'pin')]})


 ##########################    VIA1 Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'VIA12':_LayerMappingTmp[('VIA12', 'drawing')]})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'VIA12':_LayerMappingTmp[('VIA1', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'VIA12':_LayerMappingTmp[('VIA1', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'VIA12':_LayerMappingTmp[('VIA1', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'VIA12':_LayerMappingTmp[('VIA12', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'VIA12':_LayerMappingTmp[('VIA12', 'drawing')]})


 ##########################    VIA2 Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'VIA23':_LayerMappingTmp[('VIA23', 'drawing')]})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'VIA23':_LayerMappingTmp[('VIA2', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'VIA23':_LayerMappingTmp[('VIA2', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'VIA23':_LayerMappingTmp[('VIA2', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'VIA23':_LayerMappingTmp[('VIA23', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'VIA23':_LayerMappingTmp[('VIA23', 'drawing')]})

 ##########################    VIA3 Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'VIA34':_LayerMappingTmp[('VIA34', 'drawing')]})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'VIA34':_LayerMappingTmp[('VIA3', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]

    # if self._TechnologyViaMet12Met2 == '180nm':
    #         _Layernumber = layermapping[('VIA12', 'drawing')][0]
    #         _DataType = layermapping[('VIA12', 'drawing')][1]
    #     elif self._TechnologyViaMet12Met2 == '065nm':
    #         _Layernumber = layermapping[('VIA1', 'drawing')][0]
    #         _DataType = layermapping[('VIA1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'VIA34':_LayerMappingTmp[('VIA3', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'VIA34':_LayerMappingTmp[('VIA3', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'VIA34':_LayerMappingTmp[('VIA34', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'VIA34':_LayerMappingTmp[('VIA34', 'drawing')]})

 ##########################    VIA4 Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'VIA45':_LayerMappingTmp[('VIA45', 'drawing')]})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'VIA45':_LayerMappingTmp[('VIA4', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]

    # if self._TechnologyViaMet12Met2 == '180nm':
    #         _Layernumber = layermapping[('VIA12', 'drawing')][0]
    #         _DataType = layermapping[('VIA12', 'drawing')][1]
    #     elif self._TechnologyViaMet12Met2 == '065nm':
    #         _Layernumber = layermapping[('VIA1', 'drawing')][0]
    #         _DataType = layermapping[('VIA1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'VIA45':_LayerMappingTmp[('VIA4', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'VIA45':_LayerMappingTmp[('VIA4', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'VIA45':_LayerMappingTmp[('VIA45', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'VIA45':None})

 ##########################    VIA5 Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'VIA56':_LayerMappingTmp[('VIA56', 'drawing')]})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'VIA56':_LayerMappingTmp[('VIA5', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]

    # if self._TechnologyViaMet12Met2 == '180nm':
    #         _Layernumber = layermapping[('VIA12', 'drawing')][0]
    #         _DataType = layermapping[('VIA12', 'drawing')][1]
    #     elif self._TechnologyViaMet12Met2 == '065nm':
    #         _Layernumber = layermapping[('VIA1', 'drawing')][0]
    #         _DataType = layermapping[('VIA1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'VIA56':_LayerMappingTmp[('VIA5', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'VIA56':_LayerMappingTmp[('VIA5', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'VIA56':_LayerMappingTmp[('VIA56', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'VIA56':None})

 ##########################    VIA6 Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'VIA67':_LayerMappingTmp[('VIA67', 'drawing')]})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'VIA67':_LayerMappingTmp[('VIA6', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]

    # if self._TechnologyViaMet12Met2 == '180nm':
    #         _Layernumber = layermapping[('VIA12', 'drawing')][0]
    #         _DataType = layermapping[('VIA12', 'drawing')][1]
    #     elif self._TechnologyViaMet12Met2 == '065nm':
    #         _Layernumber = layermapping[('VIA1', 'drawing')][0]
    #         _DataType = layermapping[('VIA1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'VIA67':_LayerMappingTmp[('VIA6', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'VIA67':_LayerMappingTmp[('VIA6', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'VIA67':_LayerMappingTmp[('VIA67', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'VIA67':None})

 ##########################    VIA7 Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'VIA78':None})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'VIA78':_LayerMappingTmp[('VIA7', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]

    # if self._TechnologyViaMet12Met2 == '180nm':
    #         _Layernumber = layermapping[('VIA12', 'drawing')][0]
    #         _DataType = layermapping[('VIA12', 'drawing')][1]
    #     elif self._TechnologyViaMet12Met2 == '065nm':
    #         _Layernumber = layermapping[('VIA1', 'drawing')][0]
    #         _DataType = layermapping[('VIA1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'VIA78':_LayerMappingTmp[('VIA7', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'VIA78':_LayerMappingTmp[('VIA7', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'VIA78':_LayerMappingTmp[('VIA78', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'VIA78':None})

 ##########################    VIA8 Layer Mapping#####################################'

if _Technology == '180nm':
    _LayerMapping.update({'VIA89':None})
            # _Layernumber = layermapping[('CONT', 'drawing')][0]
            # _DataType = layermapping[('CONT', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'VIA89':_LayerMappingTmp[('VIA8', 'drawing')]})
            # _Layernumber = layermapping[('CO', 'drawing')][0]
            # _DataType = layermapping[('CO', 'drawing')][1]

    # if self._TechnologyViaMet12Met2 == '180nm':
    #         _Layernumber = layermapping[('VIA12', 'drawing')][0]
    #         _DataType = layermapping[('VIA12', 'drawing')][1]
    #     elif self._TechnologyViaMet12Met2 == '065nm':
    #         _Layernumber = layermapping[('VIA1', 'drawing')][0]
    #         _DataType = layermapping[('VIA1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'VIA89':_LayerMappingTmp[('VIA8', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'VIA89':_LayerMappingTmp[('VIA8', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'VIA89':_LayerMappingTmp[('VIA89', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'VIA89':None})






 #############################   METAL2 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL2':_LayerMappingTmp[('METAL2', 'drawing')]})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL2':_LayerMappingTmp[('M2', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL2':_LayerMappingTmp[('M2', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL2':_LayerMappingTmp[('M2', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL2':_LayerMappingTmp[('METAL2', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL2':_LayerMappingTmp[('METAL2', 'drawing')]})

 #############################   METAL2PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL2PIN':_LayerMappingTmp[('METAL2', 'pin')]})
            # _Layernumber = layermapping[('METAL1', 'pin')][0]
            # _DataType = layermapping[('METAL1', 'pin')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL2PIN':_LayerMappingTmp[('M2', 'pin')]})
            # _Layernumber = layermapping[('M1', 'pin')][0]
            # _DataType = layermapping[('M1', 'pin')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL2PIN':_LayerMappingTmp[('M2', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL2PIN':_LayerMappingTmp[('M2', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL2PIN':_LayerMappingTmp[('METAL2', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL2PIN':_LayerMappingTmp[('METAL2', 'pin')]})

 #############################   METAL3 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL3':_LayerMappingTmp[('METAL3', 'drawing')]})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL3':_LayerMappingTmp[('M3', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL3':_LayerMappingTmp[('M3', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL3':_LayerMappingTmp[('M3', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL3':_LayerMappingTmp[('METAL3', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL3':_LayerMappingTmp[('METAL3', 'drawing')]})

 #############################   METAL3PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL3PIN':_LayerMappingTmp[('METAL3', 'pin')]})
            # _Layernumber = layermapping[('METAL1', 'pin')][0]
            # _DataType = layermapping[('METAL1', 'pin')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL3PIN':_LayerMappingTmp[('M3', 'pin')]})
            # _Layernumber = layermapping[('M1', 'pin')][0]
            # _DataType = layermapping[('M1', 'pin')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL3PIN':_LayerMappingTmp[('M3', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL3PIN':_LayerMappingTmp[('M3', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL3PIN':_LayerMappingTmp[('METAL3', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL3PIN':_LayerMappingTmp[('METAL3', 'pin')]})
 #############################   METAL4 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL4':_LayerMappingTmp[('METAL4', 'drawing')]})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL4':_LayerMappingTmp[('M4', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL4':_LayerMappingTmp[('M4', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL4':_LayerMappingTmp[('M4', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL4':_LayerMappingTmp[('METAL4', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL4':_LayerMappingTmp[('METAL4', 'drawing')]})

 #############################   METAL4PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL4PIN':_LayerMappingTmp[('METAL4', 'pin')]})
            # _Layernumber = layermapping[('METAL1', 'pin')][0]
            # _DataType = layermapping[('METAL1', 'pin')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL4PIN':_LayerMappingTmp[('M4', 'pin')]})
            # _Layernumber = layermapping[('M1', 'pin')][0]
            # _DataType = layermapping[('M1', 'pin')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL4PIN':_LayerMappingTmp[('M4', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL4PIN':_LayerMappingTmp[('M4', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL4PIN':_LayerMappingTmp[('METAL4', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL4PIN':_LayerMappingTmp[('METAL4', 'pin')]})

 #############################   METAL5 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL5':_LayerMappingTmp[('METAL5', 'drawing')]})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL5':_LayerMappingTmp[('M5', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL5':_LayerMappingTmp[('M5', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL5':_LayerMappingTmp[('M5', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL5':_LayerMappingTmp[('METAL5', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL5':None})

 #############################   METAL5PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL5PIN':_LayerMappingTmp[('METAL5', 'pin')]})
            # _Layernumber = layermapping[('METAL1', 'pin')][0]
            # _DataType = layermapping[('METAL1', 'pin')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL5PIN':_LayerMappingTmp[('M5', 'pin')]})
            # _Layernumber = layermapping[('M1', 'pin')][0]
            # _DataType = layermapping[('M1', 'pin')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL5PIN':_LayerMappingTmp[('M5', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL5PIN':_LayerMappingTmp[('M5', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL5PIN':_LayerMappingTmp[('METAL5', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL5PIN':None})

 #############################   METAL6 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL6':_LayerMappingTmp[('METAL6', 'drawing')]})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL6':_LayerMappingTmp[('M6', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL6':_LayerMappingTmp[('M6', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL6':_LayerMappingTmp[('M6', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL6':_LayerMappingTmp[('METAL6', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL6':None})

 #############################   METAL6PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL6PIN':_LayerMappingTmp[('METAL6', 'pin')]})
            # _Layernumber = layermapping[('METAL1', 'pin')][0]
            # _DataType = layermapping[('METAL1', 'pin')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL6PIN':_LayerMappingTmp[('M6', 'pin')]})
            # _Layernumber = layermapping[('M1', 'pin')][0]
            # _DataType = layermapping[('M1', 'pin')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL6PIN':_LayerMappingTmp[('M6', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL6PIN':_LayerMappingTmp[('M6', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL6PIN':_LayerMappingTmp[('METAL6', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL6PIN':None})


 #############################   METAL7 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL7':_LayerMappingTmp[('METAL7', 'drawing')]})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL7':_LayerMappingTmp[('M7', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL7':_LayerMappingTmp[('M7', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL7':_LayerMappingTmp[('M7', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL7':_LayerMappingTmp[('METAL7', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL7':None})

 #############################   METAL7PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL7PIN':_LayerMappingTmp[('METAL7', 'pin')]})
            # _Layernumber = layermapping[('METAL1', 'pin')][0]
            # _DataType = layermapping[('METAL1', 'pin')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL7PIN':_LayerMappingTmp[('M7', 'pin')]})
            # _Layernumber = layermapping[('M1', 'pin')][0]
            # _DataType = layermapping[('M1', 'pin')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL7PIN':_LayerMappingTmp[('M7', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL7PIN':_LayerMappingTmp[('M7', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL7PIN':_LayerMappingTmp[('METAL7', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL7PIN':None})


 #############################   METAL8 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL8':None})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL8':_LayerMappingTmp[('M8', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL8':_LayerMappingTmp[('M8', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL8':_LayerMappingTmp[('M8', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL8':_LayerMappingTmp[('METAL8', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL8':None})

 #############################   METAL8PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL8PIN':None})
            # _Layernumber = layermapping[('METAL1', 'pin')][0]
            # _DataType = layermapping[('METAL1', 'pin')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL8PIN':_LayerMappingTmp[('M8', 'pin')]})
            # _Layernumber = layermapping[('M1', 'pin')][0]
            # _DataType = layermapping[('M1', 'pin')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL8PIN':_LayerMappingTmp[('M8', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL8PIN':_LayerMappingTmp[('M8', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL8PIN':_LayerMappingTmp[('METAL8', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL8PIN':None})

 #############################   METAL9 Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL9':None})
            # _Layernumber = layermapping[('METAL1', 'drawing')][0]
            # _DataType = layermapping[('METAL1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL9':_LayerMappingTmp[('M9', 'drawing')]})
            # _Layernumber = layermapping[('M1', 'drawing')][0]
            # _DataType = layermapping[('M1', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL9':_LayerMappingTmp[('M9', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL9':_LayerMappingTmp[('M9', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL9':_LayerMappingTmp[('METAL9', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL9':None})

 #############################   METAL9PIN Layer Mapping#################################'
if _Technology == '180nm':
    _LayerMapping.update({'METAL9PIN':None})
            # _Layernumber = layermapping[('METAL1', 'pin')][0]
            # _DataType = layermapping[('METAL1', 'pin')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'METAL9PIN':_LayerMappingTmp[('M9', 'pin')]})
            # _Layernumber = layermapping[('M1', 'pin')][0]
            # _DataType = layermapping[('M1', 'pin')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'METAL9PIN':_LayerMappingTmp[('M9', 'pin')]})
elif _Technology == '090nm':
    _LayerMapping.update({'METAL9PIN':_LayerMappingTmp[('M9', 'pin')]})
elif _Technology == '130nm':
    _LayerMapping.update({'METAL9PIN':_LayerMappingTmp[('METAL9', 'pin')]})
elif _Technology == '350nm':
    _LayerMapping.update({'METAL9PIN':None})


 #########################   WELLBODY Layer Mapping #################################'
if _Technology == '180nm':
    _LayerMapping.update({'WELLBODY':_LayerMappingTmp[('WELLBODY', 'drawing')]})
if _Technology == '065nm':
    _LayerMapping.update({'WELLBODY':(None,None)})
elif _Technology == '045nm':
    _LayerMapping.update({'WELLBODY':(None,None)})
elif _Technology == '090nm':
    _LayerMapping.update({'WELLBODY':(None,None)})
elif _Technology == '130nm':
    _LayerMapping.update({'WELLBODY':(None,None)})
elif _Technology == '350nm':
    _LayerMapping.update({'WELLBODY':_LayerMappingTmp[('WELLBODY', 'drawing')]})



#  WELLBODY boundary generation'
#         # _xycoordinatetmp = [[0, 0], [0, 100], [100, 100], [100, 0], [0, 0]]
#         if self._TechnologyNMOS == '180nm':
#             _Layernumber = layermapping[('WELLBODY', 'drawing')][0]
#             _DataType = layermapping[('WELLBODY', 'drawing')][1]
 ##########################   POLY Layer Mapping    #################################'

if _Technology == '180nm':
    _LayerMapping.update({'POLY':_LayerMappingTmp[('POLY1', 'drawing')]})
            # _Layernumber = layermapping[('POLY1', 'drawing')][0]
            # _DataType = layermapping[('POLY1', 'drawing')][1]
elif _Technology == '065nm':
    _LayerMapping.update({'POLY':_LayerMappingTmp[('PO', 'drawing')]})
            # _Layernumber = layermapping[('PO', 'drawing')][0]
            # _DataType = layermapping[('PO', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'POLY':_LayerMappingTmp[('PO', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'POLY':_LayerMappingTmp[('PO', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'POLY':_LayerMappingTmp[('POLYG', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'POLY':_LayerMappingTmp[('POLY1', 'drawing')]})
 #########################   NWELL Layer Mapping    #################################'

if _Technology == '180nm':
    _LayerMapping.update({'NWELL':_LayerMappingTmp[('NWELL', 'drawing')]})
elif _Technology == '065nm':
    _LayerMapping.update({'NWELL':_LayerMappingTmp[('NW', 'drawing')]})
    # if self._TechnologyINV == '180nm':
    #         _Layernumber = layermapping[('NWELL', 'drawing')][0]
    #         _DataType = layermapping[('NWELL', 'drawing')][1]
    #     elif self._TechnologyINV == '065nm':
    #         _Layernumber = layermapping[('NW', 'drawing')][0]
    #         _DataType = layermapping[('NW', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'NWELL':_LayerMappingTmp[('NW', 'drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'NWELL':_LayerMappingTmp[('NW', 'drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'NWELL':_LayerMappingTmp[('NWELL', 'drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'NWELL':_LayerMappingTmp[('NWELL', 'drawing')]})

 #########################   N3V Layer Mapping    #################################'

if _Technology == '180nm':
    _LayerMapping.update({'N3V':(None,None)})
elif _Technology == '065nm':
    _LayerMapping.update({'N3V':(None,None)})
    # if self._TechnologyINV == '180nm':
    #         _Layernumber = layermapping[('NWELL', 'drawing')][0]
    #         _DataType = layermapping[('NWELL', 'drawing')][1]
    #     elif self._TechnologyINV == '065nm':
    #         _Layernumber = layermapping[('NW', 'drawing')][0]
    #         _DataType = layermapping[('NW', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'N3V':(None,None)})
elif _Technology == '090nm':
    _LayerMapping.update({'N3V':(None,None)})
elif _Technology == '130nm':
    _LayerMapping.update({'N3V':(None,None)})
elif _Technology == '350nm':
    _LayerMapping.update({'N3V':_LayerMappingTmp[('N3V', 'drawing')]})

 #########################   RPDMY Layer Mapping    #################################'

if _Technology == '180nm':
    _LayerMapping.update({'RPDMY':_LayerMappingTmp[('RPDUMMY','drawing')]})
elif _Technology == '065nm':
    _LayerMapping.update({'RPDMY':_LayerMappingTmp[('RPDMY','drawing')]})
    # if self._TechnologyINV == '180nm':
    #         _Layernumber = layermapping[('NWELL', 'drawing')][0]
    #         _DataType = layermapping[('NWELL', 'drawing')][1]
    #     elif self._TechnologyINV == '065nm':
    #         _Layernumber = layermapping[('NW', 'drawing')][0]
    #         _DataType = layermapping[('NW', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'RPDMY':_LayerMappingTmp[('RPDMY','drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'RPDMY':_LayerMappingTmp[('RPDMY','drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'RPDMY':_LayerMappingTmp[('RPDMY','drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'RPDMY':_LayerMappingTmp[('RPDUMMY','drawing')]})
 #########################   RPO Layer Mapping    #################################'

if _Technology == '180nm':
    _LayerMapping.update({'RPO':_LayerMappingTmp[('RPO','drawing')]})
elif _Technology == '065nm':
    _LayerMapping.update({'RPO':_LayerMappingTmp[('RPO','drawing')]})
    # if self._TechnologyINV == '180nm':
    #         _Layernumber = layermapping[('NWELL', 'drawing')][0]
    #         _DataType = layermapping[('NWELL', 'drawing')][1]
    #     elif self._TechnologyINV == '065nm':
    #         _Layernumber = layermapping[('NW', 'drawing')][0]
    #         _DataType = layermapping[('NW', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'RPO':_LayerMappingTmp[('RPO','drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'RPO':_LayerMappingTmp[('RPO','drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'RPO':_LayerMappingTmp[('RPO','drawing')]})
elif _Technology == '350nm':
    _LayerMapping.update({'RPO':_LayerMappingTmp[('RPO','drawing')]})

 #########################   RH Layer Mapping    #################################'

if _Technology == '180nm':
    _LayerMapping.update({'RH':(None,None)})
elif _Technology == '065nm':
    _LayerMapping.update({'RH':_LayerMappingTmp[('RH','drawing')]})
    # if self._TechnologyINV == '180nm':
    #         _Layernumber = layermapping[('NWELL', 'drawing')][0]
    #         _DataType = layermapping[('NWELL', 'drawing')][1]
    #     elif self._TechnologyINV == '065nm':
    #         _Layernumber = layermapping[('NW', 'drawing')][0]
    #         _DataType = layermapping[('NW', 'drawing')][1]
elif _Technology == '045nm':
    _LayerMapping.update({'RH':_LayerMappingTmp[('RH','drawing')]})
elif _Technology == '090nm':
    _LayerMapping.update({'RH':_LayerMappingTmp[('RH','drawing')]})
elif _Technology == '130nm':
    _LayerMapping.update({'RH':(None,None)})
elif _Technology == '350nm':
    _LayerMapping.update({'RH':(None,None)})

_LayerMapFile.close()


print("******Layer Map file load Complete")