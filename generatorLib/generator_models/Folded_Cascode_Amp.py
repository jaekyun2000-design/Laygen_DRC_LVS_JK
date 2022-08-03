from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NSubRing

class EasyDebugModule(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self, pmos_pdn_single_sw_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':2000, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                        pmos_pdn_pair_sw_param={'_PMOSNumberofGate':32, '_PMOSChannelWidth':250, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                        pmos_current_pair1_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                        pmos_current_pair2_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
                                        pmos_current_single_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
                                        pmos_input_param={'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
                                        pmos_guardring_co_left=1,pmos_guardring_co_right=1, pmos_guardring_co_top=1, pmos_guardring_co_bot=2, nguardring_height1=None, nguardring_width1=None, nguardring_width2=None, nguardring_height2=None) :

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
            self._DesignParameter['nguardring1']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=pmos_guardring_co_top,contact_top=pmos_guardring_co_top,contact_left=pmos_guardring_co_left,contact_right=pmos_guardring_co_top)
            if nguardring_height1 != None :
                nguardring_yheight1=nguardring_height1
            elif nguardring_height1 == None :
                nguardring_yheight1=(self._DesignParameter['gate_inputp']['_XYCoordinates'][0][1]+self.getYWidth('gate_inputp','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)-(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)
            if nguardring_width1 != None :
                nguardring_xwidth1=nguardring_width1
            elif nguardring_width1 == None :
                nguardring_xwidth1=max(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_input','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)\
                                   -min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getYWidth('nguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3)
            self._DesignParameter['nguardring1']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight1,width=nguardring_xwidth1,contact_bottom=pmos_guardring_co_top,contact_top=pmos_guardring_co_top,contact_left=pmos_guardring_co_left,contact_right=pmos_guardring_co_top)
            self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['bot']['_XYCoordinates']=[]
            self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['od_bot']['_XYCoordinates']=[]
            self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates']=[]
            self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates']=[]
            self._DesignParameter['nguardring1']['_XYCoordinates']=[[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0], ((self._DesignParameter['gate_inputp']['_XYCoordinates'][0][1]+self.getYWidth('gate_inputp','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)+(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3))/2]]

            self._DesignParameter['nguardring2']=self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='nguardring2In{}'.format(_Name)))[0]
            self._DesignParameter['nguardring2']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=pmos_guardring_co_bot,contact_top=pmos_guardring_co_top,contact_left=pmos_guardring_co_left,contact_right=pmos_guardring_co_top)
            if nguardring_height2 != None :
                nguardring_yheight2=nguardring_height2
            elif nguardring_height2 == None :
                nguardring_yheight2=(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring2','top','_Met1Layer')/2+drc._Metal1MinSpace3)-min(self._DesignParameter['gate_vbp2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vbp2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('gate_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_vb2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vb2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3)
            if nguardring_width2 != None :
                nguardring_xwidth2=nguardring_width2
            elif nguardring_width2 == None :
                nguardring_xwidth2=max(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp1','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp2','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
                                   -min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3)
            self._DesignParameter['nguardring2']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight2,width=nguardring_xwidth2,contact_bottom=pmos_guardring_co_bot,contact_top=pmos_guardring_co_top,contact_left=pmos_guardring_co_left,contact_right=pmos_guardring_co_right)
            self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates']=[]
            self._DesignParameter['nguardring2']['_XYCoordinates']=[[(max(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp1','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp2','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
                                                                     +min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3))/2, \
                                                                     ((self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring2','top','_Met1Layer')/2+drc._Metal1MinSpace3)+min(self._DesignParameter['gate_vbp2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vbp2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('gate_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_vb2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vb2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3))/2]]

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

            self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates']=[]
            self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['top']['_XYCoordinates']=[]

            self._DesignParameter['additional_nw1']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
            self._DesignParameter['additional_nw1']['_XWidth']=(self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','nw_right')/2)-(self.getXY('nguardring1','left')[0][0]-self.getXWidth('nguardring1','nw_left')/2)
            self._DesignParameter['additional_nw1']['_YWidth']=self.getXY('nguardring1','top')[0][1]-self.getXY('nguardring2','bot')[0][1]
            self._DesignParameter['additional_nw1']['_XYCoordinates']=[[((self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','nw_right')/2)+(self.getXY('nguardring1','left')[0][0]-self.getXWidth('nguardring1','nw_left')/2))/2, (self.getXY('nguardring1','top')[0][1]+self.getXY('nguardring2','bot')[0][1])/2]]

            self._DesignParameter['additional_nw2']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
            self._DesignParameter['additional_nw2']['_XWidth']=(self.getXY('nguardring2','right')[0][0]+self.getXWidth('nguardring2','nw_right')/2)-(self.getXY('nguardring2','left')[0][0]-self.getXWidth('nguardring2','nw_left')/2)
            self._DesignParameter['additional_nw2']['_YWidth']=self.getXY('additional_od_top')[0][0][1]-self.getXY('nguardring2','bot')[0][1]
            self._DesignParameter['additional_nw2']['_XYCoordinates']=[[((self.getXY('nguardring2','right')[0][0]+self.getXWidth('nguardring2','nw_right')/2)+(self.getXY('nguardring2','left')[0][0]-self.getXWidth('nguardring2','nw_left')/2))/2, (self.getXY('additional_od_top')[0][0][1]+self.getXY('nguardring2','bot')[0][1])/2]]

            if self.getXWidth('pmos_pdn_pair_sw','_PODummyLayer')*self.getYWidth('pmos_pdn_pair_sw','_PODummyLayer'):
                self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea//self.getXWidth('pmos_pdn_pair_sw','_PODummyLayer'))+2*MinSnapSpacing