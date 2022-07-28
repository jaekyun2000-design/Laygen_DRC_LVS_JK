from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1

from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math

class _PMOS(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(
                                        finger = None, channel_width = None, channel_length = None,
                                        dummy = None, PCCrit = None, XVT=None,

                                        via_coy = None,space_bw_gate_pmos = None, gate_option = None)

    def __init__(self, _DesignParameter=None, _Name='pmos_with_gate'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self, finger=None, channel_width=None, channel_length=None,
                                 dummy=None, XVT=None, PCCrit=None, space_bw_gate_pmos = None,

                                  via_coy = None, gate_option = None):
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        if space_bw_gate_pmos == None:
            space_bw_gate_pmos = 0

        pmos_inputs = copy.deepcopy(PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        pmos_inputs['_PMOSNumberofGate'] = finger
        pmos_inputs['_PMOSChannelWidth'] = channel_width
        pmos_inputs['_PMOSChannellength'] = channel_length
        pmos_inputs['_PMOSDummy'] = dummy
        pmos_inputs['_PCCrit'] = PCCrit
        pmos_inputs['_XVT'] = XVT

        self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=
                                                                     PMOSWithDummy._PMOS(_DesignParameter= None,
                                                                    _Name= 'pmos_in_{}'.format(_Name)))[0]
        self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**pmos_inputs)
        self._DesignParameter['pmos']['_XYCoordinates'] = [[0,0]]

        """
        Input Gate Via Generation          
        """

        self._DesignParameter['pmos_gate_via'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(
            _DesignParameter=None, _Name='pmos_gate_via_in_{}'.format(_Name)))[0]

        pmos_via_inputs = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        if via_coy == None:
            via_coy = 1

        pmos_via_inputs['_ViaPoly2Met1NumberOfCOY'] = via_coy

        tmp_num_for_gate = 1  # Final COX Value
        width_coverage = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] + \
                         self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][
                             0] - \
                         self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][
                             0]

        while (1):
            pmos_via_inputs['_ViaPoly2Met1NumberOfCOX'] = tmp_num_for_gate
            self._DesignParameter['pmos_gate_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
                **pmos_via_inputs)
            if self._DesignParameter['pmos_gate_via']['_DesignObj']._DesignParameter['_POLayer'][
                '_XWidth'] < width_coverage:
                tmp_num_for_gate = tmp_num_for_gate + 1
            else:
                tmp_num_for_gate = tmp_num_for_gate - 1
                break
        if tmp_num_for_gate == 0 or tmp_num_for_gate == 1:
            tmp_num_for_gate = 2

        if gate_option == 'rotate':   # Y value Calibre
            pmos_via_inputs['_ViaPoly2Met1NumberOfCOX'] = via_coy
            pmos_via_inputs['_ViaPoly2Met1NumberOfCOY'] = tmp_num_for_gate
        else:
            pmos_via_inputs['_ViaPoly2Met1NumberOfCOX'] = tmp_num_for_gate


        self._DesignParameter['pmos_gate_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **pmos_via_inputs)
        self._DesignParameter['pmos_gate_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **pmos_via_inputs)

        pmos_input_via_y_value = \
            0 - self._DesignParameter['pmos']['_DesignObj']._DesignParameter\
            ['_Met1Layer']['_YWidth'] / 2 - self._DesignParameter['pmos_gate_via']\
            ['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - drc._Metal1MinSpace2 - space_bw_gate_pmos

        self._DesignParameter['pmos_gate_via']['_XYCoordinates'] = [[0, pmos_input_via_y_value]]

        """
        Routing
        """
        self._DesignParameter['additional_poly1'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _Width=None)
        pmos_offset = self._DesignParameter['pmos']['_XYCoordinates']
        pmos_poly_ref = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']
        pmos_y_value =  self._DesignParameter['pmos_gate_via']['_XYCoordinates'][0][1]

        leftmostedge = pmos_offset[0][0] + pmos_poly_ref['_XYCoordinates'][0][0] - pmos_poly_ref['_XWidth'] / 2
        rightmostedge = pmos_offset[0][0] + pmos_poly_ref['_XYCoordinates'][-1][0] + pmos_poly_ref['_XWidth'] / 2

        pmos_target = []
        pmos_target.append([[leftmostedge, pmos_y_value], [rightmostedge, pmos_y_value]])

        self._DesignParameter['additional_poly1']['_Width'] = self._DesignParameter['pmos_gate_via']\
            ['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
        self._DesignParameter['additional_poly1']['_XYCoordinates'] = pmos_target

        if pmos_offset[0][1] + pmos_poly_ref['_XYCoordinates'][0][1] - pmos_poly_ref['_YWidth'] / 2 > \
                pmos_y_value + self._DesignParameter['pmos_gate_via']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2:
            self._DesignParameter['additional_poly2'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _Width=pmos_poly_ref['_XWidth'])
            pmos_path = []
            poly_source = []
            poly_target = []
            for i in range(len(pmos_poly_ref['_XYCoordinates'])):
                poly_source.append([a + b for a, b in zip (pmos_poly_ref['_XYCoordinates'][i], pmos_offset[0])])
                poly_target.append([pmos_poly_ref['_XYCoordinates'][i][0] + pmos_offset[0][0], pmos_y_value])
                pmos_path.append([poly_source[i],poly_target[i]])
            self._DesignParameter['additional_poly2']['_XYCoordinates'] = pmos_path

        output_points = \
            self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting'][
                '_XYCoordinates']
        self._DesignParameter['_XYCoordinateNMOSOutputRouting'] = dict(_DesignParametertype=7, _XYCoordinates=output_points)

        supply_points = \
            self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting'][
                '_XYCoordinates']
        self._DesignParameter['_XYCoordinateNMOSSupplyRouting'] = dict(_DesignParametertype=7, _XYCoordinates=supply_points)
        self.offset_value = abs(self.getXY('pmos_gate_via','_Met1Layer')[0][1])

        if gate_option == 'left':  # X value Calibre (-)
            if tmp_num_for_gate != 2:
                raise Exception(f"{gate_option} option is not provided: gate number = {tmp_num_for_gate}")
            else:
                rightmostedge = 0 + channel_length / 2
                calibre_x_value = rightmostedge - self.getXWidth('pmos_gate_via', '_POLayer') / 2
                if self.getXYBot('pmos', '_PODummyLayer')[0][1] - drc._PolygateMinSpace < \
                        self.getXYTop('pmos_gate_via', '_POLayer')[0][1]:
                    calibre_y_value = abs(self.getXYBot('pmos', '_PODummyLayer')[0][1] - drc._PolygateMinSpace - \
                                      self.getXYTop('pmos_gate_via', '_POLayer')[0][1])
                    self._DesignParameter['pmos_gate_via']['_XYCoordinates'][0][1] = pmos_input_via_y_value - calibre_y_value
                self._DesignParameter['pmos_gate_via']['_XYCoordinates'][0][0] = calibre_x_value
                self.offset_value = abs(self.getXY('pmos_gate_via', '_Met1Layer')[0][1])
        elif gate_option == 'right':  # X value Calibre (+)
            if tmp_num_for_gate != 2:
                raise Exception(f"{gate_option} option is not provided: gate number = {tmp_num_for_gate}")
            else:
                leftmostedge = 0 - channel_length / 2
                calibre_x_value = leftmostedge + self.getXWidth('pmos_gate_via', '_POLayer') / 2
                self._DesignParameter['pmos_gate_via']['_XYCoordinates'][0][0] = calibre_x_value
                if self.getXYBot('pmos', ' _PODummyLayer')[0][1] - drc._PolygateMinSpace < \
                        self.getXYTop('pmos_gate_via', '_POLayer')[0][1]:
                    calibre_y_value = abs(self.getXYBot('pmos', '_PODummyLayer')[0][1] - drc._PolygateMinSpace - \
                                      self.getXYTop('pmos_gate_via', '_POLayer')[0][1])
                    self._DesignParameter['pmos_gate_via']['_XYCoordinates'][0][1] = pmos_input_via_y_value - calibre_y_value
                self.offset_value = abs(self.getXY('pmos_gate_via', '_Met1Layer')[0][1])
        elif gate_option == 'rotate':
            calibre_value = (self.getYWidth('pmos_gate_via', '_Met1Layer') - self.getXWidth('pmos_gate_via',
                                                                                            '_Met1Layer')) / 2
            self.offset_value = self.offset_value - calibre_value


if __name__ == '__main__':
    Obj = _PMOS()
    Obj._CalculateDesignParameter(finger=5, channel_width=200, channel_length=30,
                                  dummy=True, XVT='SLVT',PCCrit=True)

    Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
    _fileName = 'MS_pmos_with_gate.gds'
    testStreamFile = open('./MS_pmos_with_gate.gds', 'wb')
    tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()