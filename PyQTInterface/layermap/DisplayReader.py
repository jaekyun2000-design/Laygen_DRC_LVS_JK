import mmap
import sys
import re
import os
from PyQt5.QtGui import QColor

print("*********Display information file load Start")
_Technology='065nm'
_HomeDirectory = os.getcwd()
_DisplayDict = dict()
_ColorDict = dict()


if _Technology == '180nm':
    _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC180nm/display.drf'
elif _Technology=='065nm':
    # print(_HomeDirectory)
    _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC65nm/display.drf'

with open(_DRFfile,'rb',0) as drf:
    lines = drf.readlines()
    for line in lines:
        # print(line)
        lineDecode = line.decode('ISO-8859-1')
        # parse = re.compile('_drawing$',lineDecode)
        # print(lineDecode)

        if re.search('display\s+.*\s*\d{1,3}\s*\d{1,3}\s*\d{1,3}',lineDecode):
            try:
                split = lineDecode.split()
                R = int(split[3])
                G = int(split[4])
                B = int(split[5])
                _ColorDict[split[2]] = QColor(R,G,B)
            except:
                pass


        elif re.search('_drawing',lineDecode):
            # re.sub('\t',' ',lineDecode)
            # print('match')
            # lineDecode.split('')
            lineDecode = lineDecode.replace('\t',' ')
            lineDecode = lineDecode.replace('_drawing',' ')
            split = lineDecode.split(' ')
            _DisplayDict[split[2]] = dict()
            _DisplayDict[split[2]]['drawingNum'] = split[3]
            _DisplayDict[split[2]]['Stipple'] = split[4]
            _DisplayDict[split[2]]['LineStyle'] = split[5]
            _DisplayDict[split[2]]['Fill'] = _ColorDict[split[6]]
            _DisplayDict[split[2]]['Outline'] = _ColorDict[split[7]]
            # _DisplayDict[split[2]]['LayerOrginalName'] = split[6]
            # print(split)
            # print(lineDecode.group())
        # tmp2=line.split()
        # print(tmp2)

        # print(line)


print("************Display information file load Complete")