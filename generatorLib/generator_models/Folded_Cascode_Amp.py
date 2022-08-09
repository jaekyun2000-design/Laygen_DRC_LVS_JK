from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NSubRing
from generatorLib.generator_models import PSubRing
from generatorLib.generator_models import PbodyContact

class EasyDebugModule(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter_folded_cascode_amp(self, pset_param={'pmos_pdn_single_sw_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':2000, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                                        'pmos_pdn_pair_sw_param':{'_PMOSNumberofGate':32, '_PMOSChannelWidth':250, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                                        'pmos_current_pair1_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                                        'pmos_current_pair2_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
                                                        'pmos_current_single_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
                                                        'pmos_input_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                                        'pmos_guardring_co_left':1,'pmos_guardring_co_right':1, 'pmos_guardring_co_top':1, 'pmos_guardring_co_bot':2, 'pmos_guardring_height1':None, 'pmos_guardring_width1':None, 'pmos_guardring_width2':None, 'pmos_guardring_height2':None},\
                                                        nset_param={'nmos_pdn_sw_param':{'_NMOSNumberofGate':1, '_NMOSChannelWidth':2000, '_NMOSChannellength':30, '_NMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
                                                        'nmos_current_pair1_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
                                                        'nmos_current_pair2_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
                                                        'nmos_current_single_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
                                                        'nmos_input_param':{'_NMOSNumberofGate':8, '_NMOSChannelWidth':2500, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
                                                        'nmos_guardring_co_left':1,'nmos_guardring_co_right':1, 'nmos_guardring_co_top':1, 'nmos_guardring_co_bot':1, 'nmos_guardring_height1':None, 'nmos_guardring_width1':None, 'nmos_guardring_width2':None, 'nmos_guardring_height2':None}) :

            drc = DRC.DRC()
            _Name = self._DesignParameter['_Name']['_Name']
            MinSnapSpacing=drc._MinSnapSpacing
            _OriginXY=[[0,0]]


            #### Pset Generation ####
            self._DesignParameter['pmos_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_pdn_single_swIn{}'.format(_Name)))[0]
            self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_pdn_single_sw_param']))

            self._DesignParameter['pmos_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_pdn_pair_swIn{}'.format(_Name)))[0]
            self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_pdn_pair_sw_param']))

            self._DesignParameter['pmos_vb2']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vb2In{}'.format(_Name)))[0]
            self._DesignParameter['pmos_vb2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_current_single_param']))

            self._DesignParameter['pmos_vbp2']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vbp2In{}'.format(_Name)))[0]
            self._DesignParameter['pmos_vbp2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_current_pair2_param']))

            self._DesignParameter['pmos_vbp1']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vbp1In{}'.format(_Name)))[0]
            self._DesignParameter['pmos_vbp1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_current_pair1_param']))

            self._DesignParameter['pmos_input']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_inputIn{}'.format(_Name)))[0]
            self._DesignParameter['pmos_input']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_input_param']))

            _Lengthbtwmet1=self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]-self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]

            self._DesignParameter['pmos_vbp2']['_XYCoordinates']=[[_OriginXY[0][0]-_Lengthbtwmet1*(len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])-1)/2-drc._Metal1MinSpace*5.2, _OriginXY[0][1]],\
                                                                  [_OriginXY[0][0]+_Lengthbtwmet1*(len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])-1)/2+drc._Metal1MinSpace*5.2, _OriginXY[0][1]]]

            self._DesignParameter['gate_vbp2']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vbp2In{}'.format(_Name)))[0]
            self._DesignParameter['gate_vbp2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)
            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp2','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp2','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp2','_POLayer')/2])
            self._DesignParameter['gate_vbp2']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['poly_gate_vbp2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_gate_vbp2']['_Width']=self.getXWidth('pmos_vbp2','_POLayer')
            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp2','_POLayer')/2+self.getYWidth('gate_vbp2','_POLayer')/2], \
                            [self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_POLayer')/2-self.getYWidth('gate_vbp2','_POLayer')/2]])
                tmp.append([[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp2','_POLayer')/2+self.getYWidth('gate_vbp2','_POLayer')/2], \
                            [self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp2','_POLayer')/2-self.getYWidth('gate_vbp2','_POLayer')/2]])
            self._DesignParameter['poly_gate_vbp2']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['met1_gate_vbp2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['met1_gate_vbp2']['_Width']=self.getXWidth('gate_vbp2','_Met1Layer')
            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp2','_POLayer')/2+self.getYWidth('gate_vbp2','_Met1Layer')/2], \
                            [self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_POLayer')/2-self.getYWidth('gate_vbp2','_Met1Layer')/2]])
                tmp.append([[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp2','_POLayer')/2+self.getYWidth('gate_vbp2','_Met1Layer')/2], \
                            [self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp2','_POLayer')/2-self.getYWidth('gate_vbp2','_Met1Layer')/2]])
            self._DesignParameter['met1_gate_vbp2']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates']=[[self.getXY('pmos_vbp2')[0][0], self.getXY('gate_vbp2')[0][1]+self.getYWidth('gate_vbp2','_Met1Layer')+3*drc._Metal1MinSpace+2*drc._Metal1MinWidth+drc._Metal1MinSpace2+self.getYWidth('pmos_pdn_pair_sw','_Met1Layer')/2],\
                                                                         [self.getXY('pmos_vbp2')[1][0], self.getXY('gate_vbp2')[0][1]+self.getYWidth('gate_vbp2','_Met1Layer')+3*drc._Metal1MinSpace+2*drc._Metal1MinWidth+drc._Metal1MinSpace2+self.getYWidth('pmos_pdn_pair_sw','_Met1Layer')/2]]

            NumofVia=max(2,int(self.getYWidth('pmos_pdn_pair_sw','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
            self._DesignParameter['via12_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_pdn_pair_swIn{}'.format(_Name)))[0]
            self._DesignParameter['via12_pdn_pair_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=NumofVia)
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]])
            self._DesignParameter['via12_pdn_pair_sw']['_XYCoordinates']=tmp
            del tmp
            self._DesignParameter['via12_1_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_1_pdn_pair_swIn{}'.format(_Name)))[0]
            self._DesignParameter['via12_1_pdn_pair_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=NumofVia)
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
                tmp.append([-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]])
            self._DesignParameter['via12_1_pdn_pair_sw']['_XYCoordinates']=tmp
            del tmp
            del NumofVia

            self._DesignParameter['met1_pdn_pair_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['met1_pdn_pair_sw_x']['_Width']=2*drc._Metal1MinWidth
            self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates']=[[[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]-max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2-self.getWidth('met1_pdn_pair_sw_x')/2-drc._Metal1MinSpace2], \
                                                                            [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]-max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2-self.getWidth('met1_pdn_pair_sw_x')/2-drc._Metal1MinSpace2]], \
                                                                           [[-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][1]-max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2-self.getWidth('met1_pdn_pair_sw_x')/2-drc._Metal1MinSpace2], \
                                                                            [-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][1]-max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2-self.getWidth('met1_pdn_pair_sw_x')/2-drc._Metal1MinSpace2]]]

            self._DesignParameter['met1_pdn_pair_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['met1_pdn_pair_sw_y']['_Width']=self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]],\
                            [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]]])
                tmp.append([[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][1]],\
                            [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]]])
            self._DesignParameter['met1_pdn_pair_sw_y']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['gate_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_pdn_pair_swIn{}'.format(_Name)))[0]
            NumofCo=max(1,int((self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]+self.getXWidth('pmos_pdn_pair_sw','_POLayer'))/(drc._CoMinWidth + drc._CoMinSpace)))
            self._DesignParameter['gate_pdn_pair_sw']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=NumofCo, _ViaPoly2Met1NumberOfCOY=1)
            self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates']=[[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]+max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2+drc._Metal1MinSpace2],\
                                                                         [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]+max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2+drc._Metal1MinSpace2]]
            del NumofCo

            self._DesignParameter['poly_pdn_pair_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_pdn_pair_sw_x']['_Width']=self.getYWidth('gate_pdn_pair_sw','_POLayer')
            self._DesignParameter['poly_pdn_pair_sw_x']['_XYCoordinates']=[[[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_pair_sw','_POLayer')/2, self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]], \
                                                                            [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_POLayer')/2, self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]]],\
                                                                           [[-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_pair_sw','_POLayer')/2), self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]], \
                                                                            [-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_POLayer')/2), self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]]]]

            self._DesignParameter['poly_pdn_pair_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_pdn_pair_sw_y']['_Width']=self.getXWidth('pmos_pdn_pair_sw','_POLayer')
            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]], [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_POLayer')/2]])
                tmp.append([[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]], [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_POLayer')/2]])
            self._DesignParameter['poly_pdn_pair_sw_y']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['gate_vbp1']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vbp1In{}'.format(_Name)))[0]
            self._DesignParameter['gate_vbp1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)

            self._DesignParameter['pmos_vbp1']['_XYCoordinates']=[[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2+self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('gate_vbp1','_Met1Layer')/2+6*drc._Metal1MinSpace], \
                                                                  [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2+self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('gate_vbp1','_Met1Layer')/2+6*drc._Metal1MinSpace]]

            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp1','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp1','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp1','_POLayer')/2])
            self._DesignParameter['gate_vbp1']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['poly_gate_vbp1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_gate_vbp1']['_Width']=self.getXWidth('pmos_vbp1','_POLayer')
            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('gate_vbp1','_POLayer')/2], \
                            [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp1','_POLayer')/2-self.getYWidth('gate_vbp1','_POLayer')/2]])
                tmp.append([[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('gate_vbp1','_POLayer')/2], \
                            [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp1','_POLayer')/2-self.getYWidth('gate_vbp1','_POLayer')/2]])
            self._DesignParameter['poly_gate_vbp1']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['met1_gate_vbp1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['met1_gate_vbp1']['_Width']=self.getXWidth('gate_vbp1','_Met1Layer')
            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('gate_vbp1','_Met1Layer')/2], \
                            [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp1','_POLayer')/2-self.getYWidth('gate_vbp1','_Met1Layer')/2]])
                tmp.append([[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('gate_vbp1','_Met1Layer')/2], \
                            [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp1','_POLayer')/2-self.getYWidth('gate_vbp1','_Met1Layer')/2]])
            self._DesignParameter['met1_gate_vbp1']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['gate_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_pdn_single_swIn{}'.format(_Name)))[0]
            self._DesignParameter['gate_pdn_single_sw']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2)

            XCoordinate_single_sw=self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_vbp2','_PPLayer')/2-(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2)-drc._PpMinSpace
            YCoordinate_gate_sw=self._DesignParameter['gate_vbp2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vbp2','_POLayer')/2+self.getYWidth('gate_pdn_single_sw','_POLayer')/2

            self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates']=[[XCoordinate_single_sw, YCoordinate_gate_sw+self.getYWidth('gate_pdn_single_sw','_Met1Layer')/2+self.getYWidth('pmos_pdn_single_sw','_Met1Layer')/2+3*drc._Metal1MinSpace]]
            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], YCoordinate_gate_sw])
            self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['poly_pdn_single_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_pdn_single_sw_x']['_Width']=self.getYWidth('gate_pdn_single_sw','_POLayer')
            self._DesignParameter['poly_pdn_single_sw_x']['_XYCoordinates']=[[self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0], self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][-1]]]

            self._DesignParameter['poly_pdn_single_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_pdn_single_sw_y']['_Width']=self.getXWidth('pmos_pdn_single_sw','_POLayer')
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]], \
                            [self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0][1]]])
            self._DesignParameter['poly_pdn_single_sw_y']['_XYCoordinates']=tmp

            self._DesignParameter['pmos_vb2']['_XYCoordinates']=[[min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2-self.getXWidth('pmos_vb2','_PPLayer')/2-drc._PpMinSpace, self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_vbp1','_PPLayer')/2-self.getXWidth('pmos_input','_PPLayer')/2-drc._PpMinSpace), self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]]]
            self._DesignParameter['pmos_input']['_XYCoordinates']=[[self.getXY('pmos_vb2')[0][0], self.getXY('pmos_vbp1')[0][1]], [self.getXY('pmos_vb2')[0][0], self.getXY('pmos_vbp1')[0][1]+self.getYWidth('pmos_input','_Met1Layer')+19*drc._Metal1MinSpace]]

            self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'].append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]-self.getXWidth('pmos_vb2','_PPLayer')/2-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2-drc._PpMinSpace, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]])

            self._DesignParameter['gate_1_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_1_pdn_single_swIn{}'.format(_Name)))[0]
            self._DesignParameter['gate_1_pdn_single_sw']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2)
            tmp=[]
            for i in range(0, len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
                tmp.append([2*self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]-self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][i][0], self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0][1]])
            self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['poly_1_pdn_single_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_1_pdn_single_sw_x']['_Width']=self.getYWidth('gate_pdn_single_sw','_POLayer')
            self._DesignParameter['poly_1_pdn_single_sw_x']['_XYCoordinates']=[[self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates'][0], self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates'][-1]]]

            self._DesignParameter['poly_1_pdn_single_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_1_pdn_single_sw_y']['_Width']=self.getXWidth('pmos_pdn_single_sw','_POLayer')
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][1]], \
                            [self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates'][0][1]]])
            self._DesignParameter['poly_1_pdn_single_sw_y']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['gate_inputn']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputpIn{}'.format(_Name)))[0]
            self._DesignParameter['gate_inputn']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
                            self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]+self.getYWidth('pmos_input','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
                            self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]-self.getYWidth('pmos_input','_POLayer')/2])
            self._DesignParameter['gate_inputn']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['gate_inputp']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputnIn{}'.format(_Name)))[0]
            self._DesignParameter['gate_inputp']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
                            self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]+self.getYWidth('pmos_input','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
                            self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]-self.getYWidth('pmos_input','_POLayer')/2])
            self._DesignParameter['gate_inputp']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['gate_vb2']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vb2In{}'.format(_Name)))[0]
            self._DesignParameter['gate_vb2']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
                            self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vb2','_POLayer')/2])
                tmp.append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
                            self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vb2','_POLayer')/2])
            self._DesignParameter['gate_vb2']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['poly_gate_input']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_gate_input']['_Width']=self.getXWidth('pmos_input','_POLayer')
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]+self.getYWidth('pmos_input','_POLayer')/2+self.getYWidth('gate_inputp','_POLayer')/2],\
                            [self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]-self.getYWidth('pmos_input','_POLayer')/2-self.getYWidth('gate_inputp','_POLayer')/2]])
                tmp.append([[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]+self.getYWidth('pmos_input','_POLayer')/2+self.getYWidth('gate_inputn','_POLayer')/2],\
                            [self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]-self.getYWidth('pmos_input','_POLayer')/2-self.getYWidth('gate_inputn','_POLayer')/2]])
            self._DesignParameter['poly_gate_input']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['poly_vb2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['poly_vb2']['_Width']=self.getXWidth('pmos_vb2','_POLayer')
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vb2','_POLayer')/2+self.getYWidth('gate_vb2','_POLayer')/2],\
                            [self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vb2','_POLayer')/2-self.getYWidth('gate_vb2','_POLayer')/2]])
            self._DesignParameter['poly_vb2']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['met1_gate_input']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['met1_gate_input']['_Width']=self.getXWidth('gate_inputp','_Met1Layer')
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]+self.getYWidth('pmos_input','_POLayer')/2],\
                            [self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]-self.getYWidth('pmos_input','_POLayer')/2]])
                tmp.append([[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]+self.getYWidth('pmos_input','_POLayer')/2],\
                            [self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]-self.getYWidth('pmos_input','_POLayer')/2]])
            self._DesignParameter['met1_gate_input']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['met1_gate_vb2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['met1_gate_vb2']['_Width']=self.getXWidth('gate_vb2','_Met1Layer')
            tmp=[]
            for i in range(0,len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vb2','_POLayer')/2],\
                            [self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vb2','_POLayer')/2]])
            self._DesignParameter['met1_gate_vb2']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['pplayer_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['pplayer_y']['_Width']=min(self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self.getXWidth('pmos_vb2','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self.getXWidth('pmos_input','_PPLayer')/2)-min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_PPLayer')/2)
            self._DesignParameter['pplayer_y']['_XYCoordinates']=[[[(min(self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self.getXWidth('pmos_vb2','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self.getXWidth('pmos_input','_PPLayer')/2)+min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_PPLayer')/2))/2, self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]+self.getYWidth('pmos_input','_PPLayer')/2],\
                                                                  [(min(self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self.getXWidth('pmos_vb2','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self.getXWidth('pmos_input','_PPLayer')/2)+min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_PPLayer')/2))/2, self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vb2','_PPLayer')/2]]]

            self._DesignParameter['pplayer_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=None)
            self._DesignParameter['pplayer_x']['_Width']=self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_PPLayer')/2-min(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_PPLayer')/2, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('pmos_pdn_single_sw','_PPLayer')/2)
            self._DesignParameter['pplayer_x']['_XYCoordinates']=[[[min(self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_PPLayer')/2, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2), (self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_PPLayer')/2+min(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_PPLayer')/2, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('pmos_pdn_single_sw','_PPLayer')/2))/2],\
                                                                  [max(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self.getXWidth('pmos_vbp2','_PPLayer')/2, self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self.getXWidth('pmos_vbp1','_PPLayer')/2,self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self.getXWidth('pmos_pdn_pair_sw','_PPLayer')), (self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_PPLayer')/2+min(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_PPLayer')/2, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('pmos_pdn_single_sw','_PPLayer')/2))/2]]]

            self._DesignParameter['nguardring1']=self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='nguardring1In{}'.format(_Name)))[0]
            self._DesignParameter['nguardring1']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=pset_param['pmos_guardring_co_top'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_top'])
            if pset_param['pmos_guardring_height1'] != None :
                nguardring_yheight1=pset_param['pmos_guardring_height1']
            elif pset_param['pmos_guardring_height1'] == None :
                nguardring_yheight1=(self._DesignParameter['gate_inputp']['_XYCoordinates'][0][1]+self.getYWidth('gate_inputp','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)-(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)
            if pset_param['pmos_guardring_width1'] != None :
                nguardring_xwidth1=pset_param['pmos_guardring_width1']
            elif pset_param['pmos_guardring_width1'] == None :
                nguardring_xwidth1=max(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_input','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)\
                                   -min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getYWidth('nguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3)
            self._DesignParameter['nguardring1']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight1,width=nguardring_xwidth1,contact_bottom=pset_param['pmos_guardring_co_top'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_top'])

            self._DesignParameter['nguardring1']['_XYCoordinates']=[[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0], ((self._DesignParameter['gate_inputp']['_XYCoordinates'][0][1]+self.getYWidth('gate_inputp','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)+(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3))/2]]

            self._DesignParameter['nguardring2']=self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='nguardring2In{}'.format(_Name)))[0]
            self._DesignParameter['nguardring2']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=pset_param['pmos_guardring_co_bot'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_top'])
            if pset_param['pmos_guardring_height2'] != None :
                nguardring_yheight2=pset_param['pmos_guardring_height2']
            elif pset_param['pmos_guardring_height2'] == None :
                nguardring_yheight2=(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring2','top','_Met1Layer')/2+drc._Metal1MinSpace3)-min(self._DesignParameter['gate_vbp2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vbp2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('gate_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_vb2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vb2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3)
            if pset_param['pmos_guardring_width2'] != None :
                nguardring_xwidth2=pset_param['pmos_guardring_width2']
            elif pset_param['pmos_guardring_width2'] == None :
                nguardring_xwidth2=max(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp1','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp2','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
                                   -min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3)
            self._DesignParameter['nguardring2']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight2,width=nguardring_xwidth2,contact_bottom=pset_param['pmos_guardring_co_bot'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_right'])

            self._DesignParameter['nguardring2']['_XYCoordinates']=[[(max(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp1','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp2','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
                                                                     +min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3))/2, \
                                                                     ((self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring2','top','_Met1Layer')/2+drc._Metal1MinSpace3)+min(self._DesignParameter['gate_vbp2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vbp2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('gate_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_vb2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vb2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3))/2]]


            if self.getXWidth('pmos_pdn_pair_sw','_PODummyLayer')*self.getYWidth('pmos_pdn_pair_sw','_PODummyLayer'):
                self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea//self.getXWidth('pmos_pdn_pair_sw','_PODummyLayer'))+2*MinSnapSpacing


            #### Nset Generation ####
            self._DesignParameter['nmos_pdn_sw']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_pdn_pair_swIn{}'.format(_Name)))[0]
            self._DesignParameter['nmos_pdn_sw']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_pdn_sw_param']))

            self._DesignParameter['nmos_vb1']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_vb1In{}'.format(_Name)))[0]
            self._DesignParameter['nmos_vb1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_current_single_param']))

            self._DesignParameter['nmos_vbn1']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_vbn1In{}'.format(_Name)))[0]
            self._DesignParameter['nmos_vbn1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_current_pair1_param']))

            self._DesignParameter['nmos_input']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_inputIn{}'.format(_Name)))[0]
            self._DesignParameter['nmos_input']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_input_param']))

            self._DesignParameter['nmos_n0']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_n0In{}'.format(_Name)))[0]
            self._DesignParameter['nmos_n0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_current_pair2_param']))

            self._DesignParameter['gate_ninputn']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_ninputnIn{}'.format(_Name)))[0]
            self._DesignParameter['gate_ninputn']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)
            self._DesignParameter['gate_ninputp']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_ninputpIn{}'.format(_Name)))[0]
            self._DesignParameter['gate_ninputp']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)
            self._DesignParameter['gate_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vbn1In{}'.format(_Name)))[0]
            self._DesignParameter['gate_vbn1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)
            self._DesignParameter['gate_vb1']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vb1In{}'.format(_Name)))[0]
            self._DesignParameter['gate_vb1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)
            self._DesignParameter['gate_n0']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_n0In{}'.format(_Name)))[0]
            self._DesignParameter['gate_n0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1)

            self._DesignParameter['nmos_input']['_XYCoordinates']=[[self.getXY('pmos_input')[0][0], self.getXY('nguardring1','top')[0][1]+self.getYWidth('nguardring1','top','_Met1Layer')*3/2+drc._Metal1MinSpace3*2+self.getYWidth('nmos_input','_POLayer')/2+self.getYWidth('gate_ninputn','_Met1Layer')/2], [self.getXY('pmos_input')[0][0], self.getXY('nguardring1','top')[0][1]+self.getYWidth('nguardring1','top','_Met1Layer')*3/2+drc._Metal1MinSpace3*2+self.getYWidth('nmos_input','_POLayer')/2+self.getYWidth('gate_ninputn','_Met1Layer')/2+self.getYWidth('nmos_input','_Met1Layer')+19*drc._Metal1MinSpace]]
            self._DesignParameter['nmos_vb1']['_XYCoordinates']=[[self.getXY('nmos_input')[0][0], self.getXY('nmos_input')[1][1]+self.getYWidth('nmos_input','_Met1Layer')/2+self.getYWidth('nmos_vb1','_Met1Layer')/2+19*drc._Metal1MinSpace]]

            _Lengthbtwmet1=self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]-self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
            self._DesignParameter['nmos_vbn1']['_XYCoordinates']=[[_OriginXY[0][0]-_Lengthbtwmet1*(len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])-1)/2-drc._Metal1MinSpace*5.2, self.getXY('nguardring2','top')[0][1]+self.getYWidth('nguardring2','top','_ODLayer')*3/2+drc._Metal1MinSpace3*2+self.getYWidth('nmos_vbn1','_POLayer')/2+self.getYWidth('gate_vbn1','_Met1Layer')/2], [_OriginXY[0][0]+_Lengthbtwmet1*(len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])-1)/2+drc._Metal1MinSpace*5.2, self.getXY('nguardring2','top')[0][1]+self.getYWidth('nguardring2','top','_ODLayer')*3/2+drc._Metal1MinSpace3*2+self.getYWidth('nmos_vbn1','_POLayer')/2+self.getYWidth('gate_vbn1','_Met1Layer')/2]]
            self._DesignParameter['nmos_n0']['_XYCoordinates']=[[self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_Met1Layer')/2+self.getYWidth('nmos_n0','_Met1Layer')/2+19*drc._Metal1MinSpace], [self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_Met1Layer')/2+self.getYWidth('nmos_n0','_Met1Layer')/2+19*drc._Metal1MinSpace]]

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_POLayer')/2])
                tmp.append([self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]-self.getYWidth('nmos_vbn1','_POLayer')/2])
                tmp.append([self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]+self.getYWidth('nmos_vbn1','_POLayer')/2])
                tmp.append([self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]-self.getYWidth('nmos_vbn1','_POLayer')/2])
            self._DesignParameter['gate_vbn1']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]+self.getYWidth('nmos_vb1','_POLayer')/2])
                tmp.append([self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]-self.getYWidth('nmos_vb1','_POLayer')/2])
            self._DesignParameter['gate_vb1']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]+self.getYWidth('nmos_n0','_POLayer')/2])
                tmp.append([self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]-self.getYWidth('nmos_n0','_POLayer')/2])
                tmp.append([self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]+self.getYWidth('nmos_n0','_POLayer')/2])
                tmp.append([self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]-self.getYWidth('nmos_n0','_POLayer')/2])
            self._DesignParameter['gate_n0']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[0][1]+self.getYWidth('nmos_input','_POLayer')/2])
                tmp.append([self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[0][1]-self.getYWidth('nmos_input','_POLayer')/2])
            self._DesignParameter['gate_ninputp']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[1][1]+self.getYWidth('nmos_input','_POLayer')/2])
                tmp.append([self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[1][1]-self.getYWidth('nmos_input','_POLayer')/2])
            self._DesignParameter['gate_ninputn']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['m1_nvb1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=self.getXWidth('gate_vb1','_Met1Layer'))
            self._DesignParameter['m1_nn0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=self.getXWidth('gate_n0','_Met1Layer'))
            self._DesignParameter['m1_nvbn1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=self.getXWidth('gate_vbn1','_Met1Layer'))
            self._DesignParameter['m1_ninput']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=self.getXWidth('gate_ninputn','_Met1Layer'))

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]+self.getYWidth('nmos_vb1','_POLayer')/2],\
                            [self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]-self.getYWidth('nmos_vb1','_POLayer')/2]])
            self._DesignParameter['m1_nvb1']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_POLayer')/2],\
                            [self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]-self.getYWidth('nmos_vbn1','_POLayer')/2]])
                tmp.append([[self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]+self.getYWidth('nmos_vbn1','_POLayer')/2],\
                            [self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]-self.getYWidth('nmos_vbn1','_POLayer')/2]])
            self._DesignParameter['m1_nvbn1']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]+self.getYWidth('nmos_n0','_POLayer')/2],\
                            [self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]-self.getYWidth('nmos_n0','_POLayer')/2]])
                tmp.append([[self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]+self.getYWidth('nmos_n0','_POLayer')/2],\
                            [self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]-self.getYWidth('nmos_n0','_POLayer')/2]])
            self._DesignParameter['m1_nn0']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[0][1]+self.getYWidth('nmos_input','_POLayer')/2],\
                            [self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[0][1]-self.getYWidth('nmos_input','_POLayer')/2]])
                tmp.append([[self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[1][1]+self.getYWidth('nmos_input','_POLayer')/2],\
                            [self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[1][1]-self.getYWidth('nmos_input','_POLayer')/2]])
            self._DesignParameter['m1_ninput']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['poly_nvb1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=self.getXWidth('nmos_vb1','_POLayer'))
            self._DesignParameter['poly_nn0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=self.getXWidth('nmos_n0','_POLayer'))
            self._DesignParameter['poly_nvbn1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=self.getXWidth('nmos_vbn1','_POLayer'))
            self._DesignParameter['poly_ninput']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=self.getXWidth('nmos_input','_POLayer'))

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]+self.getYWidth('nmos_vb1','_POLayer')/2+self.getYWidth('gate_vb1','_POLayer')/2],\
                            [self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]-self.getYWidth('nmos_vb1','_POLayer')/2-self.getYWidth('gate_vb1','_POLayer')/2]])
            self._DesignParameter['poly_nvb1']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_POLayer')/2+self.getYWidth('gate_vbn1','_POLayer')/2],\
                            [self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]-self.getYWidth('nmos_vbn1','_POLayer')/2-self.getYWidth('gate_vbn1','_POLayer')/2]])
                tmp.append([[self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]+self.getYWidth('nmos_vbn1','_POLayer')/2+self.getYWidth('gate_vbn1','_POLayer')/2],\
                            [self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]-self.getYWidth('nmos_vbn1','_POLayer')/2-self.getYWidth('gate_vbn1','_POLayer')/2]])
            self._DesignParameter['poly_nvbn1']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]+self.getYWidth('nmos_n0','_POLayer')/2+self.getYWidth('gate_n0','_POLayer')/2],\
                            [self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]-self.getYWidth('nmos_n0','_POLayer')/2-self.getYWidth('gate_n0','_POLayer')/2]])
                tmp.append([[self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]+self.getYWidth('nmos_n0','_POLayer')/2+self.getYWidth('gate_n0','_POLayer')/2],\
                            [self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]-self.getYWidth('nmos_n0','_POLayer')/2-self.getYWidth('gate_n0','_POLayer')/2]])
            self._DesignParameter['poly_nn0']['_XYCoordinates']=tmp
            del tmp

            tmp=[]
            for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                tmp.append([[self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[0][1]+self.getYWidth('nmos_input','_POLayer')/2+self.getYWidth('gate_ninputn','_POLayer')/2],\
                            [self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[0][1]-self.getYWidth('nmos_input','_POLayer')/2-self.getYWidth('gate_ninputn','_POLayer')/2]])
                tmp.append([[self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[1][1]+self.getYWidth('nmos_input','_POLayer')/2+self.getYWidth('gate_ninputn','_POLayer')/2],\
                            [self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[1][1]-self.getYWidth('nmos_input','_POLayer')/2-self.getYWidth('gate_ninputn','_POLayer')/2]])
            self._DesignParameter['poly_ninput']['_XYCoordinates']=tmp
            del tmp

            self._DesignParameter['pguardring1']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='pguardring1In{}'.format(_Name)))[0]
            self._DesignParameter['pguardring1']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=nset_param['nmos_guardring_co_top'],contact_top=nset_param['nmos_guardring_co_top'],contact_left=nset_param['nmos_guardring_co_left'],contact_right=nset_param['nmos_guardring_co_top'])
            if nset_param['nmos_guardring_height1'] != None :
                pguardring_yheight1=nset_param['nmos_guardring_height1']
            elif nset_param['nmos_guardring_height1'] == None :
                pguardring_yheight1=(self._DesignParameter['gate_vb1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vb1','_Met1Layer')/2+self.getYWidth('pguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)-(self._DesignParameter['gate_ninputp']['_XYCoordinates'][-1][1]-self.getYWidth('gate_ninputp','_Met1Layer')/2-self.getYWidth('pguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3)
            if nset_param['nmos_guardring_width1'] != None :
                pguardring_xwidth1=nset_param['nmos_guardring_width1']
            elif nset_param['nmos_guardring_width1'] == None :
                pguardring_xwidth1=max(self._DesignParameter['nmos_n0']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos_n0','_Met1Layer')/2+self.getXWidth('pguardring1','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos_vbn1','_Met1Layer')/2+self.getXWidth('pguardring1','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
                                   -min(self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos_input','_Met1Layer')/2-self.getXWidth('pguardring1','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos_vb1','_Met1Layer')/2-self.getXWidth('pguardring1','left','_Met1Layer')/2-drc._Metal1MinSpace3)
            self._DesignParameter['pguardring1']['_DesignObj']._CalculateDesignParameter(height=pguardring_yheight1,width=pguardring_xwidth1,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_top'],contact_left=nset_param['nmos_guardring_co_left'],contact_right=nset_param['nmos_guardring_co_right'])
            # self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['bot']['_XYCoordinates']=[]
            # self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['od_bot']['_XYCoordinates']=[]
            # self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates']=[]
            # self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates']=[]
            self._DesignParameter['pguardring1']['_XYCoordinates']=[[(max(self._DesignParameter['nmos_n0']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos_n0','_Met1Layer')/2+self.getXWidth('pguardring1','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos_vbn1','_Met1Layer')/2+self.getXWidth('pguardring1','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
                                   +min(self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos_input','_Met1Layer')/2-self.getXWidth('pguardring1','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos_vb1','_Met1Layer')/2-self.getXWidth('pguardring1','left','_Met1Layer')/2-drc._Metal1MinSpace3))/2, ((self._DesignParameter['gate_vb1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vb1','_Met1Layer')/2+self.getYWidth('pguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)+(self._DesignParameter['gate_ninputp']['_XYCoordinates'][-1][1]-self.getYWidth('gate_ninputp','_Met1Layer')/2-self.getYWidth('pguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3))/2]]

            if self.getXY('nguardring2','left')[0][0] < self.getXY('pguardring1','left')[0][0]:
                left_x_guardring=self.getXY('nguardring2','left')[0][0]
            elif self.getXY('nguardring2','left')[0][0] >= self.getXY('pguardring1','left')[0][0]:
                left_x_guardring=self.getXY('pguardring1','left')[0][0]
            if self.getXY('nguardring2','right')[0][0] < self.getXY('pguardring1','right')[0][0]:
                right_x_guardring=self.getXY('pguardring1','right')[0][0]
            elif self.getXY('nguardring2','right')[0][0] >= self.getXY('pguardring1','right')[0][0]:
                right_x_guardring=self.getXY('nguardring2','right')[0][0]

            tmp_width_guardring=right_x_guardring-left_x_guardring
            tmp_x=(right_x_guardring+left_x_guardring)/2

            self._DesignParameter['pguardring1']['_DesignObj']._CalculateDesignParameter(height=pguardring_yheight1,width=tmp_width_guardring,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_top'],contact_left=nset_param['nmos_guardring_co_left'],contact_right=nset_param['nmos_guardring_co_right'])
            self._DesignParameter['pguardring1']['_XYCoordinates']=[[tmp_x, self._DesignParameter['pguardring1']['_XYCoordinates'][0][1]]]

            self._DesignParameter['nguardring2']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight2,width=tmp_width_guardring,contact_bottom=pset_param['pmos_guardring_co_bot'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_right'])
            self._DesignParameter['nguardring2']['_XYCoordinates']=[[tmp_x, self._DesignParameter['nguardring2']['_XYCoordinates'][0][1]]]

            self._DesignParameter['nguardring1']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight1,width=self.getXY('nguardring1','right')[0][0]-left_x_guardring,contact_bottom=pset_param['pmos_guardring_co_top'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_top'])
            self._DesignParameter['nguardring1']['_XYCoordinates']=[[(self.getXY('nguardring1','right')[0][0]+left_x_guardring)/2, self._DesignParameter['nguardring1']['_XYCoordinates'][0][1]]]

            self._DesignParameter['additional_od_left']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring2','od_left'))
            self._DesignParameter['additional_od_left']['_XYCoordinates']=[[self.getXY('nguardring2','left')[0], self.getXY('nguardring1','left')[0]]]
            self._DesignParameter['additional_met1_left']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring2','met_left'))
            self._DesignParameter['additional_met1_left']['_XYCoordinates']=[[self.getXY('nguardring2','left')[0], self.getXY('nguardring1','left')[0]]]
            self._DesignParameter['additional_nw_left']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring2','nw_left'))
            self._DesignParameter['additional_nw_left']['_XYCoordinates']=[[self.getXY('nguardring2','left')[0], self.getXY('nguardring1','left')[0]]]
            self._DesignParameter['additional_od_top']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring1','od_right'))
            self._DesignParameter['additional_od_top']['_XYCoordinates']=[[[self.getXY('nguardring1','right')[0][0]-self.getXWidth('nguardring1','od_right')/2, self.getXY('nguardring2','od_top')[0][1]], [self.getXY('nguardring2','right')[0][0]+self.getXWidth('nguardring2','od_right')/2, self.getXY('nguardring2','od_top')[0][1]]]]
            self._DesignParameter['additional_od_right']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring2','od_left'))
            self._DesignParameter['additional_od_right']['_XYCoordinates']=[[self.getXY('nguardring1','right')[0], [self.getXY('nguardring1','right')[0][0], self.getXY('nguardring2','top')[0][1]]]]

            self._DesignParameter['additional_nw1']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
            self._DesignParameter['additional_nw1']['_XWidth']=(self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','nw_right')/2)-(self.getXY('nguardring1','left')[0][0]-self.getXWidth('nguardring1','nw_left')/2)
            self._DesignParameter['additional_nw1']['_YWidth']=self.getXY('nguardring1','top')[0][1]-self.getXY('nguardring2','bot')[0][1]
            self._DesignParameter['additional_nw1']['_XYCoordinates']=[[((self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','nw_right')/2)+(self.getXY('nguardring1','left')[0][0]-self.getXWidth('nguardring1','nw_left')/2))/2, (self.getXY('nguardring1','top')[0][1]+self.getXY('nguardring2','bot')[0][1])/2]]

            self._DesignParameter['additional_nw2']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
            self._DesignParameter['additional_nw2']['_XWidth']=(self.getXY('nguardring2','right')[0][0]+self.getXWidth('nguardring2','nw_right')/2)-(self.getXY('nguardring2','left')[0][0]-self.getXWidth('nguardring2','nw_left')/2)
            self._DesignParameter['additional_nw2']['_YWidth']=self.getXY('additional_od_top')[0][0][1]-self.getXY('nguardring2','bot')[0][1]
            self._DesignParameter['additional_nw2']['_XYCoordinates']=[[((self.getXY('nguardring2','right')[0][0]+self.getXWidth('nguardring2','nw_right')/2)+(self.getXY('nguardring2','left')[0][0]-self.getXWidth('nguardring2','nw_left')/2))/2, (self.getXY('additional_od_top')[0][0][1]+self.getXY('nguardring2','bot')[0][1])/2]]

            self._DesignParameter['pguardring2']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='pguardring2In{}'.format(_Name)))[0]
            self._DesignParameter['pguardring2']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_bot'],contact_left=nset_param['nmos_guardring_co_bot'],contact_right=nset_param['nmos_guardring_co_right'])

            if nset_param['nmos_guardring_height2'] != None :
                pguardring_yheight2=nset_param['nmos_guardring_height2']
            elif nset_param['nmos_guardring_height2'] == None :
                pguardring_yheight2=self.getXY('pguardring1','bot')[0][1]-(self.getXY('nguardring2','top')[0][1]+self.getYWidth('nguardring2','top','_Met1Layer')/2+self.getYWidth('pguardring2','bot','_Met1Layer')/2+drc._Metal1MinSpace3)
            if nset_param['nmos_guardring_width2'] != None :
                pguardring_xwidth2=nset_param['nmos_guardring_width2']
            elif nset_param['nmos_guardring_width2'] == None :
                pguardring_xwidth2=self.getXY('pguardring1','right')[0][0]-(self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','right','_Met1Layer')/2+self.getXWidth('pguardring2','left','_Met1Layer')/2+drc._Metal1MinSpace3)

            self._DesignParameter['pguardring2']['_DesignObj']._CalculateDesignParameter(height=pguardring_yheight2,width=pguardring_xwidth2,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_bot'],contact_left=nset_param['nmos_guardring_co_bot'],contact_right=nset_param['nmos_guardring_co_right'])

            self._DesignParameter['pguardring2']['_XYCoordinates']=[[(self.getXY('pguardring1','right')[0][0]+(self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','right','_Met1Layer')/2+self.getXWidth('pguardring2','left','_Met1Layer')/2+drc._Metal1MinSpace3))/2, (self.getXY('pguardring1','bot')[0][1]+(self.getXY('nguardring2','top')[0][1]+self.getYWidth('nguardring2','top','_Met1Layer')/2+self.getYWidth('pguardring2','bot','_Met1Layer')/2+drc._Metal1MinSpace3))/2]]

            self._DesignParameter['pguardring3']=self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='pguardring3In{}'.format(_Name)))[0]
            _numofCoX=int((self.getXY('pguardring2','left')[0][0]+self.getXWidth('pguardring2','left','_Met1Layer')/2-self.getXY('pguardring1','left')[0][0]-self.getXWidth('pguardring1','left','_Met1Layer')/2)/(drc._CoMinSpace+drc._CoMinWidth))
            _numofCoY=nset_param['nmos_guardring_co_bot']
            self._DesignParameter['pguardring3']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=_numofCoX, _NumberOfPbodyCOY=_numofCoY, _Met1XWidth=None, _Met1YWidth=None))
            self._DesignParameter['pguardring3']['_XYCoordinates']=[[(self.getXY('pguardring1','left')[0][0]+self.getXY('pguardring2','left')[0][0])/2, self.getXY('pguardring2','top')[0][1]]]
            del _numofCoY
            del _numofCoX

            self._DesignParameter['AdditionalMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=self.getYWidth('pguardring1','bot','_Met1Layer'))
            self._DesignParameter['AdditionalMet1']['_XYCoordinates']=[[[self.getXY('pguardring1','left')[0][0], self.getXY('pguardring1','bot')[0][1]], [self.getXY('pguardring2','left')[0][0], self.getXY('pguardring1','bot')[0][1]]]]
            self._DesignParameter['AdditionalOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=self.getYWidth('pguardring1','bot','_ODLayer'))
            self._DesignParameter['AdditionalOD']['_XYCoordinates']=[[[self.getXY('pguardring1','left')[0][0], self.getXY('pguardring1','bot')[0][1]], [self.getXY('pguardring2','left')[0][0], self.getXY('pguardring1','bot')[0][1]]]]
            self._DesignParameter['AdditionalPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=self.getYWidth('pguardring1','bot','_PPLayer'))
            self._DesignParameter['AdditionalPP']['_XYCoordinates']=[[[self.getXY('pguardring1','left')[0][0], self.getXY('pguardring1','bot')[0][1]], [self.getXY('pguardring2','left')[0][0]  , self.getXY('pguardring1','bot')[0][1]]]]

            self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates']=[]
            self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['top']['_XYCoordinates']=[]
            self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates']=[]

            self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['bot']['_XYCoordinates']=[]
            self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['od_bot']['_XYCoordinates']=[]
            self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates']=[]
            self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates']=[]

            self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['od_bot']['_XYCoordinates']=[]
            self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['bot']['_XYCoordinates']=[]
            self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates']=[]
            self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates']=[]

            self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['top']['_XYCoordinates']=[]
            self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates']=[]
            self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates']=[]
            self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['pw_top']['_XYCoordinates']=[]

            self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['bot']['_XYCoordinates']=[]
            self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates']=[]


    # def _CalculateDesignParameter_common_source_amp(self):
