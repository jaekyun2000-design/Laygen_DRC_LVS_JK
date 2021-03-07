import re
from gds_editor_ver3 import user_define_exceptions
import sys
import os
import user_setup
_Technology= user_setup._Technology
_CadenceServer = '141.223.86.110'
if _Technology =='065nm':
    _UploadDirectory = '/OPUS/tsmc65WorkingSpace/gdsFile'
elif _Technology =='180nm':
    _UploadDirectory = '/home/alecnew1/OPUS/DesignAutomationTSMC018'
elif _Technology =='130nm':
    _UploadDirectory = '/home/alecnew1/OPUS/DesignAutomationTSMC013/workspace'
elif _Technology =='090nm':
    _UploadDirectory = '/home/alecnew1/OPUS/DesignAutomationTSMC90'
elif _Technology =='045nm':
    _UploadDirectory = '/home/alecnew1/OPUS/DesignAutomationTSMC45'
_HomeDirectory = os.getcwd()
_DebugMode=1
_LayerMapping=dict()

if sys.platform == 'win32':
    _TmpFileForPowerRailArrayName = 'testMemmap'
    _TmpFileForPowerRailArrayNameForParallelMapping = 'ParallelMemmap'
    _TmpFileForPowerRailArrayPath = 'E:\\Temp\\'
    _TmpFileForPowerRailArray0='E:\\Temp\\Memmap0'
    _TmpFileForPowerRailArray1='E:\\Temp\\Memmap1'
    _TmpFileForPowerRailArrayBoundary='E:\\Temp\\Memmap2'

    # _TmpFileForPowerRailArray='c:\\Temp\\testMemmap'
    # _TmpFileForSupplyRailArray1='c:\\Temp\\testMemmap1'
    # _TmpFileForSupplyRailArray2='c:\\Temp\\testMemmap2'
    # _TmpFileForSupplyRailArray='c:\\Temp\\testMemmap'
elif sys.platform == 'linux2':
    #_HomeDirectory = os.getenv('HOME') + '/Workspace/BottomUpDesign/SSTDrv'
    _TmpFileForPowerRailArrayName = 'testMemmap'
    _TmpFileForPowerRailArrayNameForParallelMapping = '/mnt/SSD2TBVol0/ParallelMemmap'
    _TmpFileForPowerRailArrayPath = '/mnt/SSD2TBVol0/'
    _TmpFileForPowerRailArray0=os.getenv('HOME') + '/WorkSpace/SSTDrv/Memmap0'
    _TmpFileForPowerRailArray1=os.getenv('HOME') + '/WorkSpace/SSTDrv/Memmap1'
    _TmpFileForPowerRailArrayBoundary=os.getenv('HOME') + '/WorkSpace/SSTDrv/Memmap2'
#############################################
#_LayerMapping (layernumber, datatype)
#############################################

#############################################
#design parameter == (datatype, layer, value)
#0: text
#1: geometry coordinate
#5: geometry coordinates for boundarys or path elements

#2: geometry width or distance btw elements
#3: number
#4: gdsstructure
#############################################

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
                #print 'The line is comment. skip the current step:', tmp
            elif re.match('^\s+$',tmp):
            #elif (tmp in ['\n',  '\r\n']):
                pass
                #print 'The line is blink. skip the current step:', tmp
            else:
                tmp2=tmp.split()
                _newLayerMapDictionary[(tmp2[0],tmp2[1])]=(int(tmp2[2]), int(tmp2[3]))
        return _newLayerMapDictionary
    else :
        raise user_define_exceptions.IncorrectInputError('CadenceVersion has incorrect value')


#######################
# load layers
#
# '180nm':
#  '065nm':

if _Technology == '180nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC180nm/tsmc18rf.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
elif _Technology=='065nm':
    _LayerMapFile = open(_HomeDirectory + '/PyQTInterface/layermap/TSMC65nm/tsmcN65.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
elif _Technology=='045nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC45nm/tsmcN45.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
elif _Technology=='090nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC90nm/tsmcN90rf.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
elif _Technology=='130nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC130nm/tsmc13rf.layermap')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'VIRTUOSO')
    # _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'ICFB')
elif _Technology=='350nm':
    _LayerMapFile = open(_HomeDirectory + '/TSMCTechfile/TSMC350nm/techfile')
    _LayerMappingTmp = _ReadLayerMapFile(_LayerMapFile, 'ICFB')

#######################

#################    Conversion into Singlevariable   ##################################
 

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



# print 'WELLBODY boundary generation'
#         # _xycoordinatetmp = [[0, 0], [0, 100], [100, 100], [100, 0], [0, 0]]
#         if self._TechnologyNMOS == '180nm':
#             _Layernumber = layermapping[('WELLBODY', 'drawing')][0]
#             _DataType = layermapping[('WELLBODY', 'drawing')][1]
 

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
########################################################################################

#############################################
#design parameter == (datatype, layer, value)
#datatype
#0: text
#1: geometry coordinate
#2: geometry width or distance btw elements
#3: number
#4: gdsstructure
#5: designparameter

#layer
#'sref' or physical layer number
#############################################
