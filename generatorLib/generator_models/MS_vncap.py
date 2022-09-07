from generatorLib import DRC
from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math

class VNCAP(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='MS_vncap'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self, width = None, height = None):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing=drc._MinSnapSpacing

        old_width = width
        unit = round((width - 386) / 280)
        width = unit * 280 + 320 - 66


        ##### METAL 1 Layers #####
        self._DesignParameter['met1_left'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['met1_right'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['met1_top'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['met1_bot'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['met1_base'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['met1_thick_array'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])
        self._DesignParameter['met1_thin_array'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])

        self._DesignParameter['met1_base']['_XYCoordinates'] = [[0, 330]]
        self._DesignParameter['met1_base']['_XWidth'] = width + 628 * 2
        self._DesignParameter['met1_base']['_YWidth'] = 660

        self._DesignParameter['met1_bot']['_XYCoordinates'] = [[0, 660 + 440 / 2]]
        self._DesignParameter['met1_bot']['_XWidth'] = width - 160 * 2
        self._DesignParameter['met1_bot']['_YWidth'] = 440

        top_edge = 1100 + height + 440
        met1_left_x = 0 - width / 2 - 628 / 2
        met1_left_y = self.FloorMinSnapSpacing((top_edge + (1100 + 220)) / 2, _MinSnapSpacing)
        met1_height = (1100 + height + 440) - (1100 + 220)
        self._DesignParameter['met1_left']['_XYCoordinates'] = [[met1_left_x, met1_left_y]]
        self._DesignParameter['met1_left']['_XWidth'] = 628
        self._DesignParameter['met1_left']['_YWidth'] = met1_height

        self._DesignParameter['met1_right']['_XYCoordinates'] = [[abs(met1_left_x), met1_left_y]]
        self._DesignParameter['met1_right']['_XWidth'] = 628
        self._DesignParameter['met1_right']['_YWidth'] = met1_height

        self._DesignParameter['met1_top']['_XYCoordinates'] = [[0, top_edge - 440 / 2]]
        self._DesignParameter['met1_top']['_XWidth'] = width + 628 * 2
        self._DesignParameter['met1_top']['_YWidth'] = 440

        self._DesignParameter['met1_thin_array']['_XWidth'] = 56
        self._DesignParameter['met1_thin_array']['_YWidth'] = height - 154

        self._DesignParameter['met1_thick_array']['_XWidth'] = 92
        self._DesignParameter['met1_thick_array']['_YWidth'] = height - 154

        met1_thin_y = self.CeilMinSnapSpacing(660 + 440 + (154 + height) / 2, _MinSnapSpacing)
        met1_thick_y = self.FloorMinSnapSpacing(660 + 440 + (height - 154) / 2, _MinSnapSpacing)

        thick_init_x = 0 - width / 2 + 160 + 92 / 2
        thin_init_y = 0 - width / 2 + 160 + 92 + 66 + 56 / 2

        thick_xy_value = []
        thin_xy_value = []
        for i in range(unit):
            thick_xy_value.append([thick_init_x + i * 280, met1_thick_y])
            thin_xy_value.append([thin_init_y + i * 280, met1_thin_y])
        self._DesignParameter['met1_thin_array']['_XYCoordinates'] = thin_xy_value
        self._DesignParameter['met1_thick_array']['_XYCoordinates'] = thick_xy_value


        ##### METAL 2 Layers #####
        self._DesignParameter['met2_left'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        self._DesignParameter['met2_right'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        self._DesignParameter['met2_top'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        self._DesignParameter['met2_bot'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        self._DesignParameter['met2_base'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        self._DesignParameter['met2_thick_array'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1])
        self._DesignParameter['met2_thin_array'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1])

        self._DesignParameter['met2_base']['_XYCoordinates'] = [[0, 384 / 2]]
        self._DesignParameter['met2_base']['_XWidth'] = width + 628 * 2
        self._DesignParameter['met2_base']['_YWidth'] = 384

        self._DesignParameter['met2_bot']['_XYCoordinates'] = [[0, 660 + 440 / 2]]
        self._DesignParameter['met2_bot']['_XWidth'] = width + 628 * 2
        self._DesignParameter['met2_bot']['_YWidth'] = 440

        met2_left_Y = (top_edge + 660) / 2
        self._DesignParameter['met2_left']['_XYCoordinates'] = [[met1_left_x, met2_left_Y]]
        self._DesignParameter['met2_left']['_XWidth'] = 628
        self._DesignParameter['met2_left']['_YWidth'] = top_edge - 660

        self._DesignParameter['met2_right']['_XYCoordinates'] = [[abs(met1_left_x), met2_left_Y]]
        self._DesignParameter['met2_right']['_XWidth'] = 628
        self._DesignParameter['met2_right']['_YWidth'] = top_edge - 660

        self._DesignParameter['met2_top']['_XYCoordinates'] = [[0, top_edge - 440 / 2]]
        self._DesignParameter['met2_top']['_XWidth'] = width + 628 * 2
        self._DesignParameter['met2_top']['_YWidth'] = 440

        self._DesignParameter['met2_thin_array']['_XWidth'] = 56
        self._DesignParameter['met2_thin_array']['_YWidth'] = height

        self._DesignParameter['met2_thick_array']['_XWidth'] = 92
        self._DesignParameter['met2_thick_array']['_YWidth'] = height - 154 * 2

        met2_array_y = self.CeilMinSnapSpacing(660 + 440 + height / 2, _MinSnapSpacing)


        thick_xy_value = []
        thin_xy_value = []
        for i in range(unit):
            thick_xy_value.append([thick_init_x + i * 280, met2_array_y])
            thin_xy_value.append([thin_init_y + i * 280, met2_array_y])

        self._DesignParameter['met2_thin_array']['_XYCoordinates'] = thin_xy_value
        self._DesignParameter['met2_thick_array']['_XYCoordinates'] = thick_xy_value

if __name__ == '__main__':
    Obj = VNCAP()
    Obj._CalculateDesignParameter(width = 3000, height = 5000
                                  )

    Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
    _fileName = 'MS_vncap.gds'
    testStreamFile = open('./MS_vncap.gds', 'wb')
    tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('kms95', 'dosel545')
    ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
    myfile = open('MS_vncap.gds', 'rb')
    ftp.storbinary('STOR MS_vncap.gds', myfile)
    myfile.close()
    ftp.close()



