from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2

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

            self._DesignParameter