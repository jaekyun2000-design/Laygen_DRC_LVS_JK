from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy


class EasyDebugModule(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self, pmos_pdn_single_sw_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':2000, '_PMOSChannellength':30, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                        pmos_pdn_pair_sw_param={'_PMOSNumberofGate':32, '_PMOSChannelWidth':250, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                        pmos_current_pair1_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                        pmos_current_pair2_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
                                        pmos_current_single_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
                                        pmos_input_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}) :

            drc = DRC.DRC()
            _Name = self._DesignParameter['_Name']['_Name']
            MinSnapSpacing=drc._MinSnapSpacing
            _OriginXY=[[0,0]]

            self._DesignParameter['pmos_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_pdn_single_swIn{}'.format(_Name)))[0]
            self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_pdn_single_sw_param))

            self._DesignParameter['pmos_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_pdn_pair_swIn{}'.format(_Name)))[0]
            self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_pdn_pair_sw_param))

            self._DesignParameter['pmos_vb2']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vb2In{}'.format(_Name)))[0]
            self._DesignParameter['pmos_vb2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_current_single_param))

            self._DesignParameter['pmos_vbp2']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vbp2In{}'.format(_Name)))[0]
            self._DesignParameter['pmos_vbp2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_current_pair2_param))

            self._DesignParameter['pmos_vbp1']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vbp1In{}'.format(_Name)))[0]
            self._DesignParameter['pmos_vbp1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_current_pair1_param))

            self._DesignParameter['pmos_input']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_inputIn{}'.format(_Name)))[0]
            self._DesignParameter['pmos_input']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_input_param))

            _Lengthbtwmet1=self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]-self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]

            self._DesignParameter['pmos_vbp2']['_XYCoordinates']=[[_OriginXY[0][0]-_Lengthbtwmet1*len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])/2, _OriginXY[0][1]],\
                                                                  [_OriginXY[0][0]+_Lengthbtwmet1*len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])/2, _OriginXY[0][1]]]



