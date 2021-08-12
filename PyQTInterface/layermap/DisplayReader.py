import mmap
import sys
import re
import os
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QBitmap
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt

import math
print("***************Display information file load Start")
import user_setup
_Technology= user_setup._Technology

STANDALONE = False

# _Technology= '065nm'
_HomeDirectory = os.getcwd()
_DisplayDict = dict()
_ColorDict = dict()
_PatternDict = dict()
_ColorPatternDict = dict()

if _Technology == '180nm':
    _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC180nm/display.drf'
elif _Technology=='028nm':
    _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/SS28nm/display.drf'
elif _Technology=='065nm':
    # print(_HomeDirectory)
    _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC65nm/display.drf'


class bitmap_converter:
    def __init__(self, name):
        self.name = name
        self.binary_list = []
        self.bytes_list = []
        self.qbit = None

    def calculate_qbit(self):
        self.convert_binary_list_to_bytes_list()
        size = self.get_bitmap_size()
        self.qbit = QBitmap(size,size)
        self.qbit.fromData(QSize(size, size),self.get_bitmap_hex())
        # else:
        #     return None
        # qbit = QBitmap(size,size)
        # return qbit.fromData(QSize=QSize(size, size), bytes=self.get_bitmap_hex())


    def add_binaries(self,binary_array):
        self.binary_list.extend(binary_array)

    def get_bitmap_hex(self):
        return bytes(self.bytes_list)

    def get_bitmap_size(self):
        return int(math.sqrt(len(self.binary_list)))

    def convert_binary_list_to_bytes_list(self):
        for i in range(int(len(self.binary_list)/4)):
            four_bits_binary = self.binary_list[i*4:(i+1)*4]
            byte_value = self.bin_to_int(four_bits_binary)
            self.bytes_list.append(byte_value)

    def bin_to_int(self, four_bits_binary:list):
        return 8*four_bits_binary[0] + 4*four_bits_binary[1] + 2* four_bits_binary[2] + four_bits_binary[3]


    def create_qbit(self,color):
        size = self.get_bitmap_size()
        point_list = []
        for x in range(size):
            for y in range(size):
                if self.binary_list[x+y*size] == 1:
                    point_list.append(QPoint(x,y))
        qbit = QPixmap(size,size)
        # qbit.fill(QColor(255,255,255))
        qbit.fill(Qt.GlobalColor.transparent)
        qbit_painter = QPainter(qbit)
        qbit_painter.setPen(color)
        # qbit_painter.drawPoints(point_list,len(point_list))
        for point in point_list:
            qbit_painter.drawPoint(point)
        return qbit


    # def bin_to_hex(self, four_bits_binary:str):
        # '''
        # four_bits_binary : '0b0101'
        # '''
        # int(four_bits_binary,2)
        # return format(int(four_bits_binary,2),'#04x')




with open(_DRFfile,'rb',0) as drf:
    lines = drf.readlines()
    stipple_flag = False
    bitmap = None
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

        if re.search('drDefineStipple', lineDecode):
            stipple_flag = True
        if stipple_flag:
            if line == b')\n' or line == b'\r\n':
                stipple_flag = False

            if b'display' in line:
                # if bitmap:
                #     bitmap.convert_binary_list_to_bytes_list()
                    # bitmap.calculate_qbit()
                lineDecode = lineDecode.split('display')[1]
                pattern_name = re.search(' [a-zA-Z0-9]+ ',lineDecode).group()[1:-1]
                bitmap = bitmap_converter(pattern_name)
                _PatternDict[pattern_name] = bitmap

            if bitmap:
                binary_list = list(map(int,re.findall(' [01]',lineDecode)))
                bitmap.add_binaries(binary_list)


        elif re.search('_drawing',lineDecode):
            # re.sub('\t',' ',lineDecode)
            # print('match')
            # lineDecode.split('')
            lineDecode = re.sub(' +',' ',lineDecode)
            lineDecode = lineDecode.replace('\t',' ')
            lineDecode = lineDecode.replace('_drawing',' ')
            split = lineDecode.split(' ')
            if _Technology == '028nm':
                split.pop(0)
            _DisplayDict[split[2]] = dict()
            _DisplayDict[split[2]]['drawingNum'] = split[3]
            _DisplayDict[split[2]]['Stipple'] = split[4]

            # if not STANDALONE:
            # _DisplayDict[split[2]]['Stipple_qbit'] = _PatternDict[split[4]].calculate_qbit()
            _DisplayDict[split[2]]['LineStyle'] = split[5]
            _DisplayDict[split[2]]['Fill'] = _ColorDict[split[6]]
            _DisplayDict[split[2]]['Fill'].name = split[6]
            _DisplayDict[split[2]]['Outline'] = _ColorDict[split[7]]
            # _DisplayDict[split[2]]['LayerOrginalName'] = split[6]
            # print(split)
            # print(lineDecode.group())
        # tmp2=line.split()
        # print(tmp2)

        # print(line)




print("******************Display information file load Complete")