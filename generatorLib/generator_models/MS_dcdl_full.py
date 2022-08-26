from generatorLib import DRC


from generatorLib.generator_models import MS_inverters_with_moscap_fine
from generatorLib.generator_models import MS_moscap_coarse_full

from generatorLib import StickDiagram
from generatorLib import DesignParameters

import copy, math, warnings

class DCDL_FULL(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(
                                            #########            UNIVERSAL INPUTS             ##########
                                            channel_length=None, dummy=None, PCCrit=None, XVT=None,
                                            supply_num_coy=None, supply_num_cox=None,
                                            distance_to_vdd=None, distance_to_vss=None,
                                            space_bw_gate_nmos=None, space_bw_gate_pmos=None,
                                            gap_bw_mos_gates=None,

                                            ######### INVERTERS WITH MOSCAP FINE ARRAY INPUTS ##########
                                            # INVERTER WITH INPUT COARSE

                                            finger1_n=None, finger1_p=None,
                                            channel_width_finger1_n=None, channel_width_finger1_p=None,

                                            # INVERTER WITH INPUT FINE

                                            finger2_n=None, finger2_p=None,
                                            channel_width_finger2_n=None, channel_width_finger2_p=None,

                                            # INVERTER IN LATCH

                                            finger3_n=None, finger3_p=None,
                                            channel_width_finger3_n=None, channel_width_finger3_p=None,

                                            # MOSCAP FINE INPUTS
                                            finger_sel_p_fine=None, finger_sel_n_fine=None,
                                            finger_on_fine=None,
                                            finger_moscap_p_fine=None, finger_moscap_n_fine=None,

                                            channel_width_sel_p_fine=None, channel_width_sel_n_fine=None,
                                            channel_width_on_p_fine=None, channel_width_on_n_fine=None,
                                            channel_width_moscap_p_fine=None, channel_width_moscap_n_fine=None,

                                            array_dimension_for_moscap_fine = None,

                                            #########        MOSCAP COARSE ARRAY INPUTS        ##########
                                            finger_sel_p_coarse = None, finger_sel_n_coarse = None,
                                            finger_on_coarse = None,
                                            finger_moscap_p_coarse = None, finger_moscap_n_coarse = None,
                                            channel_width_sel_p_coarse=None, channel_width_sel_n_coarse=None,
                                            channel_width_on_p_coarse=None, channel_width_on_n_coarse=None,
                                            channel_width_moscap_p_coarse=None, channel_width_moscap_n_coarse=None,

                                            array_dimension_for_moscap_coarse=None

                                           )

    def __init__(self, _DesignParameter=None, _Name=f'MS_DCDL_full'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
                                         _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        self._DesignParameter['_Name']['Name'] = _Name
