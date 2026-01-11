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

# _Technology= 'TSMC65nm'
_HomeDirectory = os.getcwd()
_DisplayDict = dict()
_ColorDict = dict()
_PatternDict = dict()
_ColorPatternDict = dict()
_LinePatternDict = dict()

def run_for_process_update():
    global _DisplayDict
    global _ColorDict
    global _PatternDict
    global _ColorPatternDict
    global _LinePatternDict
    global _DRFfile
    global _Technology
    _Technology = user_setup._Technology
    _DisplayDict = dict()
    _ColorDict = dict()
    _PatternDict = dict()
    _ColorPatternDict = dict()
    _LinePatternDict = dict()

    if _Technology == 'TSMC180nm':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC180nm/display.drf'
    elif _Technology == 'SS28nm':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/SS28nm/display.drf'
    elif _Technology == 'TSMC28nm':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC28nm/display.drf'
    elif _Technology == 'SS65nm':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/SS65nm/display.drf'
    elif _Technology == 'TSMC45nm':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC45nm/display.drf'
    elif _Technology == 'TSMC65nm':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC65nm/display.drf'
    elif _Technology == 'TSMC90nm':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC90nm/display.drf'
    elif _Technology == 'TSMC130nm':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC130nm/display.drf'
    elif _Technology == 'TSMC350m':
        _DRFfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC350nm/display.drf'

    with open(_DRFfile, 'rb', 0) as drf:
        lines = drf.readlines()
        stipple_flag = False
        packet_flag = False
        bitmap = None
        line_style_flag = False
        for line in lines:
            # print(line)
            lineDecode = line.decode('ISO-8859-1')
            # parse = re.compile('_drawing$',lineDecode)
            # print(lineDecode)

            if re.search('display\s+.*\s*\d{1,3}\s*\d{1,3}\s*\d{1,3}', lineDecode):
                try:
                    split = lineDecode.split()
                    R = int(split[3])
                    G = int(split[4])
                    B = int(split[5])
                    _ColorDict[split[2]] = QColor(R, G, B)
                except:
                    pass

            if re.search('drDefineStipple', lineDecode):
                stipple_flag = True
            if stipple_flag:
                # if line == b')\n' or line == b'\r\n':
                #     stipple_flag = False
                if lineDecode[0] == ')':
                    stipple_flag =False

                if b'display' in line:
                    # if bitmap:
                    #     bitmap.convert_binary_list_to_bytes_list()
                    # bitmap.calculate_qbit()
                    lineDecode = lineDecode.split('display')[1]
                    pattern_name = re.search(' [a-zA-Z0-9]+ ', lineDecode).group()[1:-1]
                    bitmap = bitmap_converter(pattern_name)
                    _PatternDict[pattern_name] = bitmap

                if bitmap:
                    binary_list = list(map(int, re.findall(' [01]', lineDecode)))
                    bitmap.add_binaries(binary_list)

            if re.search('drDefineLineStyle', lineDecode):
                line_style_flag = True
            if line_style_flag:
                if lineDecode[0] == ')' or lineDecode[1] == ')':
                    line_style_flag = False
                if 'display' in lineDecode:
                    split = re.split('[ \t]+', lineDecode)
                    if split[0] == '':
                        split.pop(0)
                    pattern = ",".join(split[4:-1])
                    _LinePatternDict[split[2]] = dict(
                        size = int(split[3]),
                        pattern = eval(pattern)
                    )

            if re.search('drDefinePacket', lineDecode):
                packet_flag = True
            if packet_flag:
                # if line == b')\n' or line == b'\r\n':
                #     stipple_flag = False
                if lineDecode[0] == ')':
                    packet_flag = False

                # if '_drawing' in lineDecode or '_pin' in lineDecode or '_cirt' in lineDecode:
                try:
                    split = re.split('[ \t]+', lineDecode)

                    if split[0] == '':
                        split.pop(0)
                    _DisplayDict[split[2]] = dict()
                    # _DisplayDict[split[2]]['drawingNum'] = split[2].split('_drawing')[0]
                    _DisplayDict[split[2]]['drawingNum'] = split[2]
                    _DisplayDict[split[2]]['Stipple'] = split[3]
                    _DisplayDict[split[2]]['LineStyle'] = _LinePatternDict[split[4]]
                    if len(_DisplayDict[split[2]]['LineStyle']['pattern'])%2 == 1:
                        _DisplayDict[split[2]]['LineStyle']['pattern'] = _DisplayDict[split[2]]['LineStyle']['pattern']*2
                    _DisplayDict[split[2]]['Fill'] = _ColorDict[split[5]]
                    _DisplayDict[split[2]]['Fill'].name = split[5]
                    _DisplayDict[split[2]]['Outline'] = _ColorDict[split[6]]
                except:
                    pass

def readtechfile():
    global _DisplayDict
    global _Technology
    _Technology = user_setup._Technology

    if _Technology == 'TSMC180nm':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC180nm/techfile'
    elif _Technology == 'SS28nm':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/SS28nm/techfile'
    elif _Technology == 'TSMC28nm':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC28nm/techfile'
    elif _Technology == 'SS65nm':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/SS65nm/techfile'       # there is no techfile
    elif _Technology == 'TSMC45nm':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC45nm/techfile'
    elif _Technology == 'TSMC65nm':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC65nm/techfile'
    elif _Technology == 'TSMC90nm':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC90nm/techfile'
    elif _Technology == 'TSMC130nm':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC130nm/techfile'
    elif _Technology == 'TSMC350m':
        techfile = _HomeDirectory + '/PyQTInterface/layermap/TSMC350nm/techfile'
    if not os.path.isfile(techfile):
        return
    with open(techfile, 'rb', 0) as tech:
        lines = tech.readlines()
        techDisplays = False
        for line in lines:
            lineDecode = line.decode('ISO-8859-1')
            if re.search('techDisplays', lineDecode):
                techDisplays = True
            if techDisplays:
                if line == b')\n' or line == b'\r\n':
                    techDisplays = False

                try:
                    split = re.split('[ \t]+', lineDecode)

                    if split[0] == '':
                        split.pop(0)
                    lay_dat_name = split[1] + '_' + split[2]
                    packet_name = split[3]
                    _DisplayDict[lay_dat_name] = dict()
                    _DisplayDict[lay_dat_name]['Fill'] = _DisplayDict[packet_name]['Fill']
                    _DisplayDict[lay_dat_name]['Outline'] = _DisplayDict[packet_name]['Outline']
                    _DisplayDict[lay_dat_name]['Stipple'] = _DisplayDict[packet_name]['Stipple']

                except:
                    pass

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






run_for_process_update()
print("******************Display information file load Complete")
