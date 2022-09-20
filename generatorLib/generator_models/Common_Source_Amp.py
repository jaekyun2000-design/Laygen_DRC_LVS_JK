from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import opppcres_b
from generatorLib.generator_models import NCAP
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import PSubRing


class _Common_Source_Amp(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Common_Source_Amp'):
		super().__init__()
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self, nmos_param={'_NMOSNumberofGate':3, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
										psubring_param={'height':None, 'width':None, 'contact_bottom':2, 'contact_top':2, 'contact_left':2, 'contact_right':2}, \
										R_drain={'_ResWidth':800, '_ResLength':4628, '_CONUMX':None, '_CONUMY':1}, \
										R_feedback={'_ResWidth':800, '_ResLength':1068, '_CONUMX':None, '_CONUMY':1}, \
										cap1_param={'_XWidth':2763, '_YWidth':3000, '_NumofGates':10, 'NumOfCOX':None, 'NumOfCOY':None, 'Guardring':False, 'guardring_height':None, 'guardring_width':None, 'guardring_right':None, 'guardring_left':None, 'guardring_top':None, 'guardring_bot':None}, \
										cap2_param={'_XWidth':3459, '_YWidth':2997, '_NumofGates':12, 'NumOfCOX':None, 'NumOfCOY':None, 'Guardring':False, 'guardring_height':None, 'guardring_width':None, 'guardring_right':None, 'guardring_left':None, 'guardring_top':None, 'guardring_bot':None}, \
										) :
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing=drc._MinSnapSpacing
		_OriginXY=[[0,0]]

		self._DesignParameter['nmos']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**nmos_param)
		self._DesignParameter['R_drain']=self._SrefElementDeclaration(_DesignObj=opppcres_b._Opppcres(_Name='R_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['R_drain']['_DesignObj']._CalculateOpppcresDesignParameter(**R_drain)
		self._DesignParameter['R_feedback']=self._SrefElementDeclaration(_DesignObj=opppcres_b._Opppcres(_Name='R_feedbackIn{}'.format(_Name)))[0]
		self._DesignParameter['R_feedback']['_DesignObj']._CalculateOpppcresDesignParameter(**R_feedback)
		self._DesignParameter['cap1']=self._SrefElementDeclaration(_DesignObj=NCAP._NCap(_Name='cap1In{}'.format(_Name)))[0]
		self._DesignParameter['cap1']['_DesignObj']._CalculateNCapDesignParameter(**cap1_param)
		self._DesignParameter['cap2']=self._SrefElementDeclaration(_DesignObj=NCAP._NCap(_Name='cap2In{}'.format(_Name)))[0]
		self._DesignParameter['cap2']['_DesignObj']._CalculateNCapDesignParameter(**cap2_param)
		self._DesignParameter['guardring']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='guardringIn{}'.format(_Name)))[0]
		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=psubring_param['contact_bottom'],contact_top=psubring_param['contact_top'],contact_left=psubring_param['contact_left'],contact_right=psubring_param['contact_right'])

		self._DesignParameter['nmos']['_XYCoordinates']=_OriginXY

		CoNumX=max(1,int(self.getXWidth('nmos','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gateIn{}'.format(_Name)))[0]
		self._DesignParameter['gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['nmos']['_XYCoordinates'][0][1]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][1]+self.getYWidth('nmos','_POLayer')/2])
			tmp.append([self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['nmos']['_XYCoordinates'][0][1]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][1]-self.getYWidth('nmos','_POLayer')/2])
		self._DesignParameter['gate']['_XYCoordinates']=tmp
		del tmp
		del CoNumX

		self._DesignParameter['poly_gate']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_gate']['_Width']=self.getXWidth('nmos','_POLayer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate']['_XYCoordinates'][0][1]+self.getYWidth('gate','_POLayer')/2], \
						[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate']['_XYCoordinates'][1][1]-self.getYWidth('gate','_POLayer')/2]])
		self._DesignParameter['poly_gate']['_XYCoordinates']=tmp
		del tmp

		if psubring_param['height']!=None:
			yheight=psubring_param['height']
		elif psubring_param['height']==None:
			yheight=(self._DesignParameter['gate']['_XYCoordinates'][0][1]+self.getYWidth('gate','_Met1Layer')/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3)-(self._DesignParameter['gate']['_XYCoordinates'][1][1]-self.getYWidth('gate','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3)
		if psubring_param['width']!=None:
			xwidth=psubring_param['width']
		elif psubring_param['width']==None:
			xwidth=self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos','_Met1Layer')/2+self.getXWidth('guardring','right','_Met1Layer')/2+drc._Metal1MinSpace3-(self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos','_Met1Layer')/2-self.getXWidth('guardring','left','_Met1Layer')/2-drc._Metal1MinSpace3)

		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(height=yheight,width=xwidth,contact_bottom=psubring_param['contact_bottom'],contact_top=psubring_param['contact_top'],contact_left=psubring_param['contact_left'],contact_right=psubring_param['contact_right'])
		self._DesignParameter['guardring']['_XYCoordinates']=self.getXY('nmos')

		self._DesignParameter['m1_source']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_source']['_Width']=self.getXWidth('nmos','_Met1Layer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self.getXY('guardring','bot')[0][1]], \
						[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self.getXY('guardring','top')[0][1]]])
		self._DesignParameter['m1_source']['_XYCoordinates']=tmp
		del tmp

		ViaNumY=max(1,int(self.getYWidth('nmos','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_drain']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=ViaNumY)
		tmp=[]
		for i in range(0,len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos']['_XYCoordinates'][0][1]])
		self._DesignParameter['via12_drain']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via23_drain']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=ViaNumY)
		self._DesignParameter['via23_drain']['_XYCoordinates']=self._DesignParameter['via12_drain']['_XYCoordinates']

		self._DesignParameter['via34_drain']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via34_drain']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=ViaNumY)
		self._DesignParameter['via34_drain']['_XYCoordinates']=self._DesignParameter['via12_drain']['_XYCoordinates']
		del ViaNumY

		ViaNumX=max(1,int(self.getXWidth('gate','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		self._DesignParameter['via12_gate']['_XYCoordinates']=self.getXY('gate')
		del ViaNumX

		self._DesignParameter['m2_gate']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate']['_Width']=self.getYWidth('via12_gate','_Met2Layer')
		self._DesignParameter['m2_gate']['_XYCoordinates']=[[[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0], self.getXY('via12_gate')[0][1]], [self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0], self.getXY('via12_gate')[0][1]]], \
															[[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0], self.getXY('via12_gate')[-1][1]], [self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0], self.getXY('via12_gate')[-1][1]]]]

		self._DesignParameter['R_feedback']['_XYCoordinates']=[[max(self.getXY('guardring','right')[0][0]+self.getXWidth('guardring','right','_PPLayer')/2+self.getXWidth('R_feedback','_PRESLayer')/2+drc._PpMinSpacetoPRES, self.getXY('guardring','right')[0][0]+self.getXWidth('guardring','right','_ODLayer')/2+self.getXWidth('R_feedback','_PRESLayer')/2+drc._RXMinSpacetoPRES), \
																min(self.getXY('guardring','top')[0][1]-self.getYWidth('guardring','top','_PPLayer')/2-self.getYWidth('R_feedback','_PRESLayer')/2-drc._PpMinSpacetoPRES, self.getXY('guardring','top')[0][1]-self.getYWidth('guardring','top','_ODLayer')/2-self.getYWidth('R_feedback','_PRESLayer')/2-drc._RXMinSpacetoPRES)]]

		self._DesignParameter['R_drain']['_XYCoordinates']=[[self.getXY('R_feedback','_OPLayer')[0][0]+self.getXWidth('R_feedback','_OPLayer')/2+self.getXWidth('R_drain','_OPLayer')/2+drc._OPMinspace, min(self.getXY('guardring','top')[0][1]-self.getYWidth('guardring','top','_PPLayer')/2-self.getYWidth('R_drain','_PRESLayer')/2-drc._PpMinSpacetoPRES, self.getXY('guardring','top')[0][1]-self.getYWidth('guardring','top','_ODLayer')/2-self.getYWidth('R_drain','_PRESLayer')/2-drc._RXMinSpacetoPRES)]]

		ViaNumX=max(1,int(self.getXWidth('R_drain','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_R_drain']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_R_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_R_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		self._DesignParameter['via12_R_drain']['_XYCoordinates']=[[self.getXY('R_drain','_Met1Layer')[1][0], self.getXY('R_drain','_Met1Layer')[1][1]]]

		self._DesignParameter['via23_R_drain']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_R_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_R_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=ViaNumX, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_R_drain']['_XYCoordinates']=self._DesignParameter['via12_R_drain']['_XYCoordinates']

		self._DesignParameter['via34_R_drain']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_R_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via34_R_drain']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=ViaNumX, _ViaMet32Met4NumberOfCOY=1)
		self._DesignParameter['via34_R_drain']['_XYCoordinates']=self._DesignParameter['via12_R_drain']['_XYCoordinates']
		del ViaNumX

		ViaNumX=max(1,int(self.getXWidth('R_feedback','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_R_feedback']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_R_feedbackIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_R_feedback']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		self._DesignParameter['via12_R_feedback']['_XYCoordinates']=[[self.getXY('R_feedback','_Met1Layer')[1][0], self.getXY('R_feedback','_Met1Layer')[1][1]]]

		self._DesignParameter['via23_R_feedback']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_R_feedbackIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_R_feedback']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=ViaNumX, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_R_feedback']['_XYCoordinates']=self._DesignParameter['via12_R_feedback']['_XYCoordinates']

		# self._DesignParameter['via34_R_feedback']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_R_feedbackIn{}'.format(_Name)))[0]
		# self._DesignParameter['via34_R_feedback']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=ViaNumX, _ViaMet32Met4NumberOfCOY=1)
		# self._DesignParameter['via34_R_feedback']['_XYCoordinates']=[self._DesignParameter['via12_R_feedback']['_XYCoordinates'][0]]
		del ViaNumX

		self._DesignParameter['cap1']=self._SrefElementDeclaration(_DesignObj=NCAP._NCap(_Name='cap1In{}'.format(_Name)))[0]
		self._DesignParameter['cap1']['_DesignObj']._CalculateNCapDesignParameter(**cap1_param)
		self._DesignParameter['cap2']=self._SrefElementDeclaration(_DesignObj=NCAP._NCap(_Name='cap2In{}'.format(_Name)))[0]
		self._DesignParameter['cap2']['_DesignObj']._CalculateNCapDesignParameter(**cap2_param)

		self._DesignParameter['cap1']['_XYCoordinates']=[[self.getXY('nmos')[0][0], self.getXY('guardring','top','_PPLayer')[0][1]+self.getYWidth('guardring','top','_PPLayer')/2+self.getYWidth('cap1','NWELL')/2+drc._NwMinEnclosurePactive2]]
		self._DesignParameter['cap2']['_XYCoordinates']=[[self.getXY('nmos')[0][0], self.getXY('cap1')[0][1]+self.getYWidth('cap1','NWELL')/2+self.getYWidth('cap2','NWELL')/2+2*drc._NwMinSpace]]

		self._DesignParameter['pres']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0],_Datatype=DesignParameters._LayerMapping['PRES'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['pres']['_Width']=self.getXY('R_drain')[0][0]+self.getXWidth('R_drain','_PRESLayer')/2-(self.getXY('R_feedback')[0][0]-self.getXWidth('R_feedback','_PRESLayer')/2)
		self._DesignParameter['pres']['_XYCoordinates']=[[[(self.getXY('R_drain')[0][0]+self.getXWidth('R_drain','_PRESLayer')/2+(self.getXY('R_feedback')[0][0]-self.getXWidth('R_feedback','_PRESLayer')/2))/2, self.getXY('R_drain')[0][1]+self.getYWidth('R_drain','_PRESLayer')/2], \
														  [(self.getXY('R_drain')[0][0]+self.getXWidth('R_drain','_PRESLayer')/2+(self.getXY('R_feedback')[0][0]-self.getXWidth('R_feedback','_PRESLayer')/2))/2, max(self.getXY('R_drain')[0][1]-self.getYWidth('R_drain','_PRESLayer')/2, self.getXY('R_feedback')[0][1]-self.getYWidth('R_feedback','_PRESLayer')/2)]]]

		self._DesignParameter['pplayer']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['pplayer']['_Width']=self.getXY('R_drain')[0][0]+self.getXWidth('R_drain','_PPLayer')/2-(self.getXY('R_feedback')[0][0]-self.getXWidth('R_feedback','_PPLayer')/2)
		self._DesignParameter['pplayer']['_XYCoordinates']=[[[(self.getXY('R_drain')[0][0]+self.getXWidth('R_drain','_PPLayer')/2+(self.getXY('R_feedback')[0][0]-self.getXWidth('R_feedback','_PPLayer')/2))/2, self.getXY('R_drain')[0][1]+self.getYWidth('R_drain','_PPLayer')/2], \
														  [(self.getXY('R_drain')[0][0]+self.getXWidth('R_drain','_PPLayer')/2+(self.getXY('R_feedback')[0][0]-self.getXWidth('R_feedback','_PPLayer')/2))/2, max(self.getXY('R_drain')[0][1]-self.getYWidth('R_drain','_PPLayer')/2, self.getXY('R_feedback')[0][1]-self.getYWidth('R_feedback','_PPLayer')/2)]]]

		self._DesignParameter['m1_cap1_po']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_cap1_po']['_Width']=self.getYWidth('cap1','_Met1Layer1')
		self._DesignParameter['m1_cap1_po']['_XYCoordinates']=[[self.getXY('cap1','_XYCoordinateM1inPO')[0], self.getXY('cap1','_XYCoordinateM1inPO')[-2]], [self.getXY('cap1','_XYCoordinateM1inPO')[1], self.getXY('cap1','_XYCoordinateM1inPO')[-1]]]

		self._DesignParameter['m1_cap2_po']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_cap2_po']['_Width']=self.getYWidth('cap2','_Met1Layer1')
		self._DesignParameter['m1_cap2_po']['_XYCoordinates']=[[self.getXY('cap2','_XYCoordinateM1inPO')[0], self.getXY('cap2','_XYCoordinateM1inPO')[-2]], [self.getXY('cap2','_XYCoordinateM1inPO')[1], self.getXY('cap2','_XYCoordinateM1inPO')[-1]]]

		self._DesignParameter['m1_cap1_od']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_cap1_od']['_Width']=10*drc._Metal1MinWidth
		self._DesignParameter['m1_cap1_od']['_XYCoordinates']=[[self.getXY('cap1','_Met1Layer2')[0], self.getXY('cap1','_Met1Layer2')[-1]]]

		self._DesignParameter['m1_cap2_od']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_cap2_od']['_Width']=10*drc._Metal1MinWidth
		self._DesignParameter['m1_cap2_od']['_XYCoordinates']=[[self.getXY('cap2','_Met1Layer2')[0], self.getXY('cap2','_Met1Layer2')[-1]]]

		self._DesignParameter['m4_mos_R_drain']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m4_mos_R_drain']['_Width']=self.getYWidth('via34_R_drain','_Met4Layer')
		self._DesignParameter['m4_mos_R_drain']['_XYCoordinates']=[[self.getXY('via34_R_drain')[0], [self.getXY('via34_drain')[0][0], self.getXY('via34_R_drain')[0][1]]]]

		self._DesignParameter['via34_mos_cap']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via34_mos_capIn{}'.format(_Name)))[0]
		self._DesignParameter['via34_mos_cap']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via34_mos_cap']['_XYCoordinates']=[[self.getXY('nmos')[0][0], self.getXY('via34_R_drain')[0][1]]]

		self._DesignParameter['via12_mos_R_feedback']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_mos_R_feedbackIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_mos_R_feedback']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
		self._DesignParameter['via12_mos_R_feedback']['_XYCoordinates']=[[self.getXY('R_feedback')[0][0], self._DesignParameter['via12_gate']['_XYCoordinates'][-1][1]]]

		self._DesignParameter['m2_mos_R_feedback']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_mos_R_feedback']['_Width']=self.getYWidth('via12_gate','_Met2Layer')
		self._DesignParameter['m2_mos_R_feedback']['_XYCoordinates']=[[[self.getXY('nmos')[0][0], self._DesignParameter['via12_gate']['_XYCoordinates'][-1][1]], self.getXY('via12_mos_R_feedback')[0]]]

		self._DesignParameter['m1_mos_R_feedback']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_mos_R_feedback']['_Width']=self.getXWidth('via12_mos_R_feedback','_Met1Layer')
		self._DesignParameter['m1_mos_R_feedback']['_XYCoordinates']=[[self.getXY('via12_mos_R_feedback')[0], self.getXY('R_feedback','_Met1Layer')[0]]]

		self._DesignParameter['via23_mos_cap1_po']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_mos_cap1_poIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_mos_cap1_po']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_mos_cap1_po']['_XYCoordinates']=[[self.getXY('via34_mos_cap')[0][0], self._DesignParameter['m1_cap1_po']['_XYCoordinates'][0][0][1]], [self.getXY('via34_mos_cap')[0][0], self._DesignParameter['m1_cap1_po']['_XYCoordinates'][1][0][1]]]

		self._DesignParameter['via12_mos_cap1_po']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_mos_cap1_poIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_mos_cap1_po']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
		self._DesignParameter['via12_mos_cap1_po']['_XYCoordinates']=[[self.getXY('via34_mos_cap')[0][0], self._DesignParameter['m1_cap1_po']['_XYCoordinates'][0][0][1]], [self.getXY('via34_mos_cap')[0][0], self._DesignParameter['m1_cap1_po']['_XYCoordinates'][1][0][1]]]

		self._DesignParameter['via23_mos_cap2_od']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_mos_cap2_odIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_mos_cap2_od']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_mos_cap2_od']['_XYCoordinates']=[[self.getXY('via34_mos_cap')[0][0], self._DesignParameter['m1_cap2_od']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['via12_mos_cap2_od']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_mos_cap2_odIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_mos_cap2_od']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=2)
		self._DesignParameter['via12_mos_cap2_od']['_XYCoordinates']=[[self.getXY('via34_mos_cap')[0][0], self._DesignParameter['m1_cap2_od']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['m3_mos_cap1_cap2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_mos_cap1_cap2']['_Width']=self.getXWidth('via34_mos_cap','_Met3Layer')
		self._DesignParameter['m3_mos_cap1_cap2']['_XYCoordinates']=[[self.getXY('via34_mos_cap')[0], self.getXY('via23_mos_cap2_od')[0]]]

		self._DesignParameter['via23_mos_cap2_po']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_mos_cap2_poIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_mos_cap2_po']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_mos_cap2_po']['_XYCoordinates']=[[self.getXY('via23_R_feedback')[0][0], self._DesignParameter['m1_cap2_po']['_XYCoordinates'][0][0][1]], [self.getXY('via23_R_feedback')[0][0], self._DesignParameter['m1_cap2_po']['_XYCoordinates'][1][0][1]]]

		self._DesignParameter['via12_mos_cap2_po']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_mos_cap2_poIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_mos_cap2_po']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
		self._DesignParameter['via12_mos_cap2_po']['_XYCoordinates']=[[self.getXY('via23_R_feedback')[0][0], self._DesignParameter['m1_cap2_po']['_XYCoordinates'][0][0][1]], [self.getXY('via23_R_feedback')[0][0], self._DesignParameter['m1_cap2_po']['_XYCoordinates'][1][0][1]]]

		self._DesignParameter['via23_mos_cap1_od']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_mos_cap1_odIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_mos_cap1_od']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_mos_cap1_od']['_XYCoordinates']=[[self.getXY('via23_R_feedback')[0][0], self._DesignParameter['m1_cap1_od']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['via12_mos_cap1_od']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_mos_cap1_odIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_mos_cap1_od']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=2)
		self._DesignParameter['via12_mos_cap1_od']['_XYCoordinates']=[[self.getXY('via23_R_feedback')[0][0], self._DesignParameter['m1_cap1_od']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['m3_cap2_cap1_mos']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_cap2_cap1_mos']['_Width']=self.getXWidth('via23_mos_cap1_od','_Met3Layer')
		self._DesignParameter['m3_cap2_cap1_mos']['_XYCoordinates']=[[self.getXY('via23_mos_cap2_po')[1], self.getXY('via23_R_feedback')[0]]]

		self._DesignParameter['VDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VDD')
		self._DesignParameter['VSS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VSS')
		self._DesignParameter['VOUT'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VOUT')
		self._DesignParameter['VIN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VIN')

		self._DesignParameter['VDD']['_XYCoordinates']=[self.getXY('R_drain','_Met1Layer')[0]]
		self._DesignParameter['VSS']['_XYCoordinates']=[self.getXY('guardring','bot')[0]]
		self._DesignParameter['VOUT']['_XYCoordinates']=[self.getXY('via23_R_feedback')[0]]
		self._DesignParameter['VIN']['_XYCoordinates']=[[self.getXY('nmos')[0][0], self.getXY('via12_gate')[-1][1]]]