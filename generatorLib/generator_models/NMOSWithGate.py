from generatorLib import DRC
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1

from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math

class _NMOS(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(
                                        finger = None, channel_width = None, channel_length = None,
                                        dummy = None, PCCrit = None, XVT=None,

                                        via_coy = None, space_bw_gate_nmos = None,
                                        gate_option = None)

    def __init__(self, _DesignParameter=None, _Name='nmos_with_gate'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self, finger=None, channel_width=None, channel_length=None,
                                 dummy=None, XVT=None, PCCrit=None,

                                  via_coy = None, space_bw_gate_nmos = None, gate_option = None):
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        if space_bw_gate_nmos == None:
            space_bw_gate_nmos = 0

        nmos_inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
        nmos_inputs['_NMOSNumberofGate'] = finger
        nmos_inputs['_NMOSChannelWidth'] = channel_width
        nmos_inputs['_NMOSChannellength'] = channel_length
        nmos_inputs['_NMOSDummy'] = dummy
        nmos_inputs['_PCCrit'] = PCCrit
        nmos_inputs['_XVT'] = XVT

        self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=
                                                                     NMOSWithDummy._NMOS(_DesignParameter= None,
                                                                    _Name= 'nmos_in_{}'.format(_Name)))[0]
        self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**nmos_inputs)
        self._DesignParameter['nmos']['_XYCoordinates'] = [[0,0]]

        """
        Input Gate Via Generation          
        """

        self._DesignParameter['nmos_gate_via'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(
            _DesignParameter=None, _Name='nmos_gate_via_in_{}'.format(_Name)))[0]

        nmos_via_inputs = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        if via_coy == None:
            via_coy = 1

        nmos_via_inputs['_ViaPoly2Met1NumberOfCOY'] = via_coy

        tmp_num_for_gate = 1  # Final COX Value
        width_coverage = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] + \
                         self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][
                             0] - \
                         self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][
                             0]

        while (1):
            nmos_via_inputs['_ViaPoly2Met1NumberOfCOX'] = tmp_num_for_gate
            self._DesignParameter['nmos_gate_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **nmos_via_inputs)
            if self._DesignParameter['nmos_gate_via']['_DesignObj']._DesignParameter['_POLayer'][
                '_XWidth'] < width_coverage:
                tmp_num_for_gate = tmp_num_for_gate + 1
            else:
                tmp_num_for_gate = tmp_num_for_gate - 1
                break
        if tmp_num_for_gate == 0 or tmp_num_for_gate == 1:
            tmp_num_for_gate = 2

        if gate_option == 'rotate':   # Y value Calibre
            nmos_via_inputs['_ViaPoly2Met1NumberOfCOX'] = via_coy
            nmos_via_inputs['_ViaPoly2Met1NumberOfCOY'] = tmp_num_for_gate
        else:
            nmos_via_inputs['_ViaPoly2Met1NumberOfCOX'] = tmp_num_for_gate

        self._DesignParameter['nmos_gate_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **nmos_via_inputs)
        self._DesignParameter['nmos_gate_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **nmos_via_inputs)

        nmos_input_via_y_value = \
            0 + self._DesignParameter['nmos']['_DesignObj']._DesignParameter\
            ['_Met1Layer']['_YWidth'] / 2 + self._DesignParameter['nmos_gate_via']['_DesignObj']\
                ._DesignParameter['_Met1Layer']['_YWidth'] / 2 + drc._Metal1MinSpace2 + space_bw_gate_nmos
        self._DesignParameter['nmos_gate_via']['_XYCoordinates'] = [[0, nmos_input_via_y_value]]

        """
        Routing
        """
        self._DesignParameter['additional_poly1'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _Width=None)
        nmos_offset = self._DesignParameter['nmos']['_XYCoordinates']
        nmos_poly_ref = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']
        nmos_y_value =  self._DesignParameter['nmos_gate_via']['_XYCoordinates'][0][1]

        leftmostedge = nmos_offset[0][0] + nmos_poly_ref['_XYCoordinates'][0][0] - nmos_poly_ref['_XWidth'] / 2
        rightmostedge = nmos_offset[0][0] + nmos_poly_ref['_XYCoordinates'][-1][0] + nmos_poly_ref['_XWidth'] / 2

        nmos_target = []
        nmos_target.append([[leftmostedge, nmos_y_value], [rightmostedge, nmos_y_value]])

        self._DesignParameter['additional_poly1']['_Width'] = self._DesignParameter['nmos_gate_via']\
            ['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['additional_poly1']['_XYCoordinates'] = nmos_target

        if nmos_offset[0][1] + nmos_poly_ref['_XYCoordinates'][0][1] + nmos_poly_ref['_YWidth'] / 2 < \
                nmos_y_value - self._DesignParameter['nmos_gate_via']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2:
            self._DesignParameter['additional_poly2'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _Width=nmos_poly_ref['_XWidth'])
            nmos_path = []
            poly_source = []
            poly_target = []
            for i in range(len(nmos_poly_ref['_XYCoordinates'])):
                poly_source.append([a + b for a, b in zip (nmos_poly_ref['_XYCoordinates'][i], nmos_offset[0])])
                poly_target.append([nmos_poly_ref['_XYCoordinates'][i][0] + nmos_offset[0][0], nmos_y_value])
                nmos_path.append([poly_source[i],poly_target[i]])
            self._DesignParameter['additional_poly2']['_XYCoordinates'] = nmos_path

            output_points =\
            self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']
            self._DesignParameter['_XYCoordinateOutputRouting'] = dict(_DesignParametertype= 7, _XYCoordinates = output_points)

            supply_points = \
            self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']
            self._DesignParameter['_XYCoordinateSupplyRouting'] = dict(_DesignParametertype= 7, _XYCoordinates = supply_points)
        self.offset_value = abs(nmos_y_value)

        if gate_option == 'left':    # X value Calibre (-)
            if tmp_num_for_gate != 2:
                raise Exception(f"{gate_option} option is not provided: gate number = {tmp_num_for_gate}")
            else:
                rightmostedge = 0 + channel_length/2
                calibre_x_value = rightmostedge - self.getXWidth('nmos_gate_via', '_POLayer') / 2
                if self.getXYTop('nmos','_PODummyLayer')[0][1] + drc._PolygateMinSpace > self.getXYBot('nmos_gate_via','_POLayer')[0][1]:
                    calibre_y_value = self.getXYTop('nmos','_PODummyLayer')[0][1] + drc._PolygateMinSpace - \
                                      self.getXYBot('nmos_gate_via', '_POLayer')[0][1]
                    self._DesignParameter['nmos_gate_via']['_XYCoordinates'][0][1] = nmos_input_via_y_value + calibre_y_value
                self._DesignParameter['nmos_gate_via']['_XYCoordinates'][0][0] = calibre_x_value
        elif gate_option == 'right':    # X value Calibre (+)
            if tmp_num_for_gate != 2:
                raise Exception(f"{gate_option} option is not provided: gate number = {tmp_num_for_gate}")
            else:
                leftmostedge = 0 - channel_length/2
                calibre_x_value = leftmostedge + self.getXWidth('nmos_gate_via', '_POLayer') / 2
                self._DesignParameter['nmos_gate_via']['_XYCoordinates'][0][0] = calibre_x_value
                if self.getXYTop('nmos',' _PODummyLayer')[0][1] + drc._PolygateMinSpace > self.getXYBot('nmos_gate_via','_POLayer')[0][1]:
                    calibre_y_value = self.getXYTop('nmos','_PODummyLayer')[0][1] + drc._PolygateMinSpace - \
                                      self.getXYBot('nmos_gate_via', '_POLayer')[0][1]
                    self._DesignParameter['nmos_gate_via']['_XYCoordinates'][0][1] = nmos_input_via_y_value + calibre_y_value
        elif gate_option == 'rotate':
            calibre_value = (self.getYWidth('nmos_gate_via', '_Met1Layer') - self.getXWidth('nmos_gate_via', '_Met1Layer')) / 2
            self.offset_value = self.offset_value - calibre_value




if __name__ == '__main__':
    Obj = _NMOS()
    Obj._CalculateDesignParameter(finger=1, channel_width=200, channel_length=30,
                                  dummy=True, XVT='SLVT',PCCrit=True, space_bw_gate_nmos= 500)

    Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
    _fileName = 'MS_nmos_with_gate.gds'
    testStreamFile = open('./MS_nmos_with_gate.gds', 'wb')
    tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('kms95', 'dosel545')
    ftp.cwd('/mnt/sdb/kms95/Desktop')
    myfile = open('MS_nmos_with_gate.gds', 'rb')
    ftp.storbinary('STOR MS_nmos_with_gate.gds', myfile)
    myfile.close()
    ftp.close()