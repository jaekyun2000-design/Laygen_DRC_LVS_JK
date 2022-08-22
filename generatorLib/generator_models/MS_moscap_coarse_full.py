from generatorLib import DRC


from generatorLib.generator_models import MS_moscap_array
from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings

class MOSCAP_COARSE_FULL(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                           finger_sel_p=None, finger_sel_n=None,
                                           finger_on = None,
                                           finger_moscap_p = None, finger_moscap_n = None,

                                           channel_width_sel_p = None, channel_width_sel_n = None,
                                           channel_width_on_p = None, channel_width_on_n = None,
                                           channel_width_moscap_p = None, channel_width_moscap_n = None,


                                           supply_num_coy=None, supply_num_cox=None,
                                           distance_to_vdd=None, distance_to_vss=None,
                                           space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                           gap_bw_mos_gates=None, array_dimension=None
                                           )
    def __init__(self, _DesignParameter=None, _Name=f'MS_moscap_coarse_full'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,
                                  channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                  finger_sel_p=None, finger_sel_n=None,
                                  finger_on=None,
                                  finger_moscap_p=None, finger_moscap_n=None,

                                  channel_width_sel_p=None, channel_width_sel_n=None,
                                  channel_width_on_p=None, channel_width_on_n=None,
                                  channel_width_moscap_p=None, channel_width_moscap_n=None,

                                  supply_num_coy=None, supply_num_cox=None,
                                  distance_to_vdd=None, distance_to_vss=None,
                                  space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                  gap_bw_mos_gates=None, array_dimension=None
                                  ):
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _MinSnapSpacing = drc._MinSnapSpacing

        moscap_array_input = dict(
            channel_length=channel_length, dummy=dummy, PCCrit=PCCrit, XVT=XVT,
            finger_sel_p=finger_sel_p, finger_sel_n=finger_sel_n,
            finger_on=finger_on,
            finger_moscap_p=finger_moscap_p, finger_moscap_n=finger_moscap_n,

            channel_width_sel_p=channel_width_sel_p, channel_width_sel_n=channel_width_sel_n,
            channel_width_on_p=channel_width_on_p, channel_width_on_n=channel_width_on_n,
            channel_width_moscap_p=channel_width_moscap_p, channel_width_moscap_n=channel_width_moscap_n,

            supply_num_coy=supply_num_coy, supply_num_cox=supply_num_cox,
            distance_to_vdd=distance_to_vdd, distance_to_vss=distance_to_vss,
            space_bw_gate_nmos=space_bw_gate_nmos, space_bw_gate_pmos=space_bw_gate_pmos,
            gap_bw_mos_gates=gap_bw_mos_gates, array_dimension = array_dimension
            )

        self._DesignParameter[f'moscap_coarse_full1'] = \
        self._SrefElementDeclaration(_DesignObj=MS_moscap_array.MOSCAP_ARRAY(_DesignParameter=None,
                                                                    _Name=f'moscap_coarse_full1_in_{_Name}'),
                                     _Reflect=[1, 0, 0], _Angle= 0)[0]
        self._DesignParameter[f'moscap_coarse_full2'] = \
        self._SrefElementDeclaration(_DesignObj=MS_moscap_array.MOSCAP_ARRAY(_DesignParameter=None,
                                                                    _Name=f'moscap_coarse_full2_in_{_Name}'),
                                     _Reflect=[0, 0, 0], _Angle= 0)[0]
        self._DesignParameter[f'moscap_coarse_full3'] = \
        self._SrefElementDeclaration(_DesignObj=MS_moscap_array.MOSCAP_ARRAY(_DesignParameter=None,
                                                                    _Name=f'moscap_coarse_full3_in_{_Name}'),
                                     _Reflect=[1, 0, 0], _Angle= 180)[0]
        self._DesignParameter[f'moscap_coarse_full4'] = \
        self._SrefElementDeclaration(_DesignObj=MS_moscap_array.MOSCAP_ARRAY(_DesignParameter=None,
                                                                    _Name=f'moscap_coarse_full4_in_{_Name}'),
                                     _Reflect=[0, 0, 0], _Angle= 180)[0]

        self._DesignParameter[f'moscap_coarse_full1']['_DesignObj']._CalculateDesignParameter(**moscap_array_input)
        self._DesignParameter[f'moscap_coarse_full2']['_DesignObj']._CalculateDesignParameter(**moscap_array_input)
        self._DesignParameter[f'moscap_coarse_full3']['_DesignObj']._CalculateDesignParameter(**moscap_array_input)
        self._DesignParameter[f'moscap_coarse_full4']['_DesignObj']._CalculateDesignParameter(**moscap_array_input)

        """
        sref 1: bottom right
        sref 2: top right   -> no inversion, no rotation
        sref 3: top left
        sref 4: bottom left
        
        """

        cell_x_offset = self.CeilMinSnapSpacing(abs(
            self._DesignParameter[f'moscap_coarse_full1']['_DesignObj'].leftmost_poly_edge) +
                                                 drc._PolygateMinSpace2 / 2, _MinSnapSpacing)
        cell_y_offset = self._DesignParameter['moscap_coarse_full1']['_DesignObj'].distance_to_vss
        self._DesignParameter[f'moscap_coarse_full1']['_XYCoordinates'] = [[cell_x_offset, -cell_y_offset]]
        self._DesignParameter[f'moscap_coarse_full2']['_XYCoordinates'] = [[cell_x_offset, cell_y_offset]]
        self._DesignParameter[f'moscap_coarse_full3']['_XYCoordinates'] = [[-cell_x_offset, cell_y_offset]]
        self._DesignParameter[f'moscap_coarse_full4']['_XYCoordinates'] = [[-cell_x_offset, -cell_y_offset]]

        via_offset_x1 = self.getXY('moscap_coarse_full1', 'via_for_input', '_Met3Layer')[0][0]
        via_offset_y1 = self.getXY('moscap_coarse_full1', 'via_for_input', '_Met3Layer')[0][1]

        via_offset_x2 = self.getXY('moscap_coarse_full1', 'via_for_input', '_Met3Layer')[-1][0]
        via_offset_y2 = self.getXY('moscap_coarse_full1', 'via_for_input', '_Met3Layer')[-1][1]

        if via_offset_y1 != via_offset_y2:
            raise NotImplementedError

        self._DesignParameter['input_routing'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=drc._MetalxMinWidth)
        self._DesignParameter['input_routing']['_XYCoordinates'] =[
                                    [[via_offset_x1, via_offset_y1],[via_offset_x1, -via_offset_y1]],
                                    [[via_offset_x2, via_offset_y1],[via_offset_x2, -via_offset_y1]],
                                    [[-via_offset_x1, via_offset_y1],[-via_offset_x1, -via_offset_y1]],
                                    [[-via_offset_x2, via_offset_y1],[-via_offset_x2, -via_offset_y1]]
        ]
        self.met3_routing_y_value = via_offset_y1

        """
        Additional Layers : Met1 & RX for Rails, SLVT Layer, BP Layer,
        
        """
        self._DesignParameter['additional_nxvt_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
            _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])
        self._DesignParameter['additional_pxvt_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[f'{XVT}'][0],
            _Datatype=DesignParameters._LayerMapping[f'{XVT}'][1])

        xvt_top_p = max(self.getXYTop('moscap_coarse_full2','moscap_1', 'inverter_sel', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
                        self.getXYTop('moscap_coarse_full2','moscap_1', 'moscap_on', 'pmos1', 'pmos', f'_{XVT}Layer')[0][1],
                        self.getXYTop('moscap_coarse_full2','moscap_1', 'moscap_on', 'pmos2', 'pmos', f'_{XVT}Layer')[0][1])
        xvt_bot_p = min(self.getXYBot('moscap_coarse_full2','moscap_1', 'inverter_sel', 'pmos', 'pmos', f'_{XVT}Layer')[0][1],
                        self.getXYBot('moscap_coarse_full2','moscap_1', 'moscap_on', 'pmos1', 'pmos', f'_{XVT}Layer')[0][1],
                        self.getXYBot('moscap_coarse_full2','moscap_1', 'moscap_on', 'pmos2', 'pmos', f'_{XVT}Layer')[0][1])

        xvt_top_n = max(self.getXYTop('moscap_coarse_full2','moscap_1', 'inverter_sel', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
                        self.getXYTop('moscap_coarse_full2','moscap_1', 'moscap_on', 'nmos1', 'nmos', f'_{XVT}Layer')[0][1],
                        self.getXYTop('moscap_coarse_full2','moscap_1', 'moscap_on', 'nmos2', 'nmos', f'_{XVT}Layer')[0][1])
        xvt_bot_n = min(self.getXYBot('moscap_coarse_full2','moscap_1', 'inverter_sel', 'nmos', 'nmos', f'_{XVT}Layer')[0][1],
                        self.getXYBot('moscap_coarse_full2','moscap_1', 'moscap_on', 'nmos1', 'nmos', f'_{XVT}Layer')[0][1],
                        self.getXYBot('moscap_coarse_full2','moscap_1', 'moscap_on', 'nmos2', 'nmos', f'_{XVT}Layer')[0][1])
        xvt_hor_edge = max(
            self.getXYRight('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'pmos2', 'pmos',
                            f'_{XVT}Layer')[0][0],
            self.getXYRight('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'nmos2', 'nmos',
                            f'_{XVT}Layer')[0][0]
        )
        pxvt_y_center = self.CeilMinSnapSpacing((xvt_bot_p + xvt_top_p) / 2, _MinSnapSpacing)
        nxvt_y_center = self.CeilMinSnapSpacing((xvt_bot_n + xvt_top_n) / 2, _MinSnapSpacing)

        self._DesignParameter['additional_pxvt_layer']['_XYCoordinates'] = [[0, pxvt_y_center], [0, - pxvt_y_center]]
        self._DesignParameter['additional_pxvt_layer']['_XWidth'] = 2 * xvt_hor_edge
        self._DesignParameter['additional_pxvt_layer']['_YWidth'] = (xvt_top_p - xvt_bot_p)

        self._DesignParameter['additional_nxvt_layer']['_XYCoordinates'] = [[0, nxvt_y_center], [0, - nxvt_y_center]]
        self._DesignParameter['additional_nxvt_layer']['_XWidth'] = 2 * xvt_hor_edge
        self._DesignParameter['additional_nxvt_layer']['_YWidth'] = (xvt_top_n - xvt_bot_n)




        self._DesignParameter['additional_bp_layer_pmos'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1])

        bp_top = max(self.getXYTop('moscap_coarse_full2','moscap_1', 'inverter_sel', 'pmos', 'pmos', f'_PPLayer')[0][1],
                        self.getXYTop('moscap_coarse_full2','moscap_1', 'moscap_on', 'pmos1', 'pmos', f'_PPLayer')[0][1],
                        self.getXYTop('moscap_coarse_full2','moscap_1', 'moscap_on', 'pmos2', 'pmos', f'_PPLayer')[0][1])
        bp_bot = min(self.getXYBot('moscap_coarse_full2','moscap_1', 'inverter_sel', 'pmos', 'pmos', f'_PPLayer')[0][1],
                        self.getXYBot('moscap_coarse_full2','moscap_1', 'moscap_on', 'pmos1', 'pmos', f'_PPLayer')[0][1],
                        self.getXYBot('moscap_coarse_full2','moscap_1', 'moscap_on', 'pmos2', 'pmos', f'_PPLayer')[0][1])
        bp_hor_edge = self.getXYRight('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'pmos2', 'pmos',
                            f'_PPLayer')[0][0]
        bp_y_center = self.CeilMinSnapSpacing((bp_top + bp_bot) / 2, _MinSnapSpacing)
        self._DesignParameter['additional_bp_layer_pmos']['_XYCoordinates'] = [[0, bp_y_center], [0, - bp_y_center]]
        self._DesignParameter['additional_bp_layer_pmos']['_XWidth'] = 2 * bp_hor_edge
        self._DesignParameter['additional_bp_layer_pmos']['_YWidth'] = (bp_top - bp_bot)



        self._DesignParameter['additional_bp_layer_rail'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1])
        distance_to_vdd = self.getXY('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'vdd',
                            f'_Met1Layer')[0][1]

        bp_hor_edge = self.getXYRight('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                            f'_PPLayer')[0][0]
        bp_height = self.getYWidth('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                            f'_PPLayer')
        self._DesignParameter['additional_bp_layer_rail']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['additional_bp_layer_rail']['_XWidth'] = 2 * bp_hor_edge
        self._DesignParameter['additional_bp_layer_rail']['_YWidth'] = bp_height

        self._DesignParameter['additional_rx_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1])

        rx_rightmostedge = self.getXYRight('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                            f'_ODLayer')[0][0]
        rx_height = self.getYWidth('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'vdd',
                            f'_ODLayer')
        self._DesignParameter['additional_rx_layer']['_XWidth'] = 2 * rx_rightmostedge
        self._DesignParameter['additional_rx_layer']['_YWidth'] = rx_height
        self._DesignParameter['additional_rx_layer']['_XYCoordinates'] = [[0, distance_to_vdd], [0, 0], [0, -distance_to_vdd]]



        self._DesignParameter['additional_met1_layer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1])

        met1_rightmostedge = self.getXYRight('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'vss',
                            f'_Met1Layer')[0][0]
        # met1_y_center_vdd = self.getXY('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'vdd',
        #                     f'_Met1Layer')[0][1]
        met1_height = self.getYWidth('moscap_coarse_full2', f'moscap_{array_dimension}', 'moscap_on', 'vdd',
                                   f'_Met1Layer')

        self._DesignParameter['additional_met1_layer']['_XWidth'] = 2 * met1_rightmostedge
        self._DesignParameter['additional_met1_layer']['_YWidth'] = met1_height
        self._DesignParameter['additional_met1_layer']['_XYCoordinates'] = [[0, distance_to_vdd], [0, 0], [0, -distance_to_vdd]]
        print("test")



if __name__ == '__main__':
    Obj = MOSCAP_COARSE_FULL()
    import random
    for i in range(0,3):

        # Obj._CalculateDesignParameter(channel_length=30, dummy=True, PCCrit=None, XVT='SLVT',
        #                               finger_sel_p=5, finger_sel_n=2,
        #                               finger_on=4,
        #                               finger_moscap_p=1, finger_moscap_n=3,
        #
        #                               channel_width_sel_p=700, channel_width_sel_n=200,
        #                               channel_width_on_p=500, channel_width_on_n=800,
        #                               channel_width_moscap_p=600, channel_width_moscap_n=750,
        #
        #                               supply_num_coy=None, supply_num_cox=None,
        #                               distance_to_vdd=None, distance_to_vss=None,
        #                               space_bw_gate_nmos=None, space_bw_gate_pmos=None,
        #                               gap_bw_mos_gates=None, array_dimension=4
        #                               )

        channel_length = random.randrange(30,100, 10)
        finger_sel_p = random.randrange(1, 9, 1)
        finger_sel_n= random.randrange(1, 9, 1)
        finger_on= random.randrange(1, 9, 1)
        finger_moscap_p= random.randrange(1, 9, 1)
        finger_moscap_n= random.randrange(1, 9, 1)
        channel_width_sel_p= random.randrange(400,1350,50)
        channel_width_sel_n= random.randrange(200,650,50)
        channel_width_on_p= random.randrange(400,1350,50)
        channel_width_on_n= random.randrange(200,650,50)
        channel_width_moscap_p= random.randrange(400,1350,50)
        channel_width_moscap_n= random.randrange(200,650,50)

        supply_num_coy= random.randrange(1,5,1)



        gap_bw_mos_gates= random.randrange(400,1800,50)
        array_dimension = random.randrange(2, 8, 1)
        Obj._CalculateDesignParameter(
            # channel_length=30, dummy=True, PCCrit=None, XVT='SLVT',
            #                           finger_sel_p=5, finger_sel_n=2,
            #                           finger_on=4,
            #                           finger_moscap_p=1, finger_moscap_n=3,
            #
            #                           channel_width_sel_p=700, channel_width_sel_n=200,
            #                           channel_width_on_p=500, channel_width_on_n=800,
            #                           channel_width_moscap_p=600, channel_width_moscap_n=750,
            #
            #                           supply_num_coy=None, supply_num_cox=None,
            #                           distance_to_vdd=None, distance_to_vss=None,
            #                           space_bw_gate_nmos=None, space_bw_gate_pmos=None,
            #                           gap_bw_mos_gates=None, array_dimension=4,

                    channel_length = channel_length, dummy = True, PCCrit = True, XVT = 'SLVT',
                    finger_sel_p = finger_sel_p, finger_sel_n = finger_sel_n,
                    finger_on = finger_on, finger_moscap_p = finger_moscap_p, finger_moscap_n = finger_moscap_n,

                    channel_width_sel_p = channel_width_sel_p, channel_width_sel_n = channel_width_sel_n,
                    channel_width_on_p = channel_width_on_p, channel_width_on_n = channel_width_on_n,
                    channel_width_moscap_p = channel_width_moscap_p, channel_width_moscap_n = channel_width_moscap_n,

                    supply_num_coy = supply_num_coy,
                    gap_bw_mos_gates = gap_bw_mos_gates, array_dimension = array_dimension
        )

        Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
        _fileName = 'MS_moscap_coarse_full.gds'
        testStreamFile = open('./MS_moscap_coarse_full.gds', 'wb')
        tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        import ftplib

        ftp = ftplib.FTP('141.223.29.62')
        ftp.login('kms95', 'dosel545')
        ftp.cwd('/mnt/sdb/kms95/OPUS/ss28')
        myfile = open('MS_moscap_coarse_full.gds', 'rb')
        ftp.storbinary('STOR MS_moscap_coarse_full.gds', myfile)
        myfile.close()
        ftp.close()

        import DRCchecker

        _DRC = DRCchecker.DRCchecker('kms95','dosel545','/mnt/sdb/kms95/OPUS/ss28','/mnt/sdb/kms95/OPUS/ss28/DRC/run',
                                     'MS_moscap_coarse_full','MS_moscap_coarse_full')
        _DRC.DRCchecker()

