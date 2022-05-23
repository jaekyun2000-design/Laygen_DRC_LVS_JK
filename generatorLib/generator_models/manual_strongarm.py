from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models.rx_project import ViaPoly2Met1
from generatorLib.generator_models.rx_project import ViaMet12Met2
from generatorLib.generator_models.rx_project import ViaMet32Met4
from generatorLib.generator_models.rx_project import PSubRing
from generatorLib.generator_models.rx_project import NMOSWithDummy
from generatorLib.generator_models.rx_project import PMOSWithDummy
from generatorLib.generator_models.rx_project import NSubRing

class topcell(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='topcell'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,pmos_inner_gate=3):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=9, _PMOSChannelWidth=500, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[(- 1323.0), 624.0]]
		self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=3, _PMOSChannelWidth=500, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[(- 315.0), 624.0]]
		self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=3, _PMOSChannelWidth=500, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[315.0, 624.0]]
		self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=9, _PMOSChannelWidth=500, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[1323.0, 624.0]]
		self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=12, _NMOSChannelWidth=1000, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[(- 1386.0), (- 1172.0)]]
		self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=12, _NMOSChannelWidth=1000, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[1386.0, (- 1172.0)]]
		self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_botInSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=8, _NMOSChannelWidth=1000, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[0.0, (- 2495.0)]]
		self._DesignParameter['NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=2, _NMOSChannelWidth=500, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[(- 252.0), (- 1172.0)]]
		self._DesignParameter['NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=2, _NMOSChannelWidth=500, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[252.0, (- 1172.0)]]

		self._DesignParameter['GuardringInSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='GuardringInSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['GuardringInSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateDesignParameter(**dict(height=5330, width=5624, contact=2))
		self._DesignParameter['GuardringInSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[0.0, (- 1100.0)]]
		self._DesignParameter['GuardringInNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='GuardringInNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['GuardringInNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateDesignParameter(**dict(height=2838, width=4800, contact=2))
		self._DesignParameter['GuardringInNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[0.0, (- 1884.0)]]
		self._DesignParameter['GuardringInPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='GuardringInPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['GuardringInPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateDesignParameter(**dict(height=1068, width=4700, contact=2))
		self._DesignParameter['GuardringInPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[0.0, 571.0]]



		self._DesignParameter['PCCAM1_CDNS_6375475055680_1InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055680_1InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055680_1InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=11, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055680_1InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[(- 1323.0), 260.0]]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_15InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055654_15InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_15InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=3, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055654_15InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[(- 315.0), 260.0]]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_14InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055654_14InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_14InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=3, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055654_14InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[315.0, 260.0]]
		self._DesignParameter['PCCAM1_CDNS_6375475055680_0InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055680_0InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055680_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=11, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055680_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[1323.0, 260.0]]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_12InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055654_12InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_12InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055654_12InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[(- 252.0), (- 808.0)]]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_13InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055654_13InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_13InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055654_13InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[252.0, (- 808.0)]]

		self._DesignParameter['pccam_nmos_leftInSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pccam_nmos_leftInSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['pccam_nmos_leftInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=15, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['pccam_nmos_leftInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[(- 1386.0), (- 1836.0)]]
		self._DesignParameter['pccam_nmos_rightInSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pccam_nmos_rightInSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['pccam_nmos_rightInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=15, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['pccam_nmos_rightInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[1386.0, (- 1836.0)]]
		self._DesignParameter['nmos_bot_gate_poly_viaInSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='nmos_bot_gate_poly_viaInSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['nmos_bot_gate_poly_viaInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=10, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['nmos_bot_gate_poly_viaInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[0.0, (- 1881.0)]]
		self._DesignParameter['VSS_viastack_1to3InSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='VSS_viastack_1to3InSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['VSS_viastack_1to3InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=43, _ViaMet12Met2NumberOfCOY=5))
		self._DesignParameter['VSS_viastack_1to3InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[0.0, (- 3534.0)]]
		self._DesignParameter['VDD_viastackInSlicerInSlicerWithSRLatch_0_0'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='VDD_viastackInSlicerInSlicerWithSRLatch_0_0In{}'.format(_Name)))[0]
		self._DesignParameter['VDD_viastackInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=40, _ViaMet12Met2NumberOfCOY=2))
		self._DesignParameter['VDD_viastackInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'] = [[0.0, 1105.0]]
		self._DesignParameter['METAL2_path_29'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['METAL2_path_29']['_XYCoordinates'] = [[[(- 2167), (- 667)], [(- 252), (- 667)], [(- 252), (- 1140)]]]
		self._DesignParameter['METAL2_path_28'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['METAL2_path_28']['_XYCoordinates'] = [[[2167, (- 667)], [252, (- 667)], [252, (- 1140)]]]
		self._DesignParameter['METAL2_path_27'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['METAL2_path_27']['_XYCoordinates'] = [[[(- 2041), (- 1555)], [2041, (- 1555)]]]

		### Array 1 : Supply Routing From PMOS 1 ###
		self._DesignParameter['array1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['array1']['_Width'] = 50
		tmp = self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['VDD_viastackInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array1']['_XYCoordinates'] = path_list

		### Array 2 : Supply Routing From PMOS 2 ###
		self._DesignParameter['array2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['array2']['_Width'] = 50
		tmp = self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['VDD_viastackInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array2']['_XYCoordinates'] = path_list

		### Array 3 : Supply Routing From PMOS 2 ###
		self._DesignParameter['array3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['array3']['_Width'] = 50
		tmp = self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['VDD_viastackInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array3']['_XYCoordinates'] = path_list

		### Array 4 : Supply Routing From PMOS 4 ###
		self._DesignParameter['array4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['array4']['_Width'] = 50
		tmp = self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['VDD_viastackInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array4']['_XYCoordinates'] = path_list

		### Array 5 : Supply Routing From bot NMOS ###
		self._DesignParameter['array5'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['array5']['_Width'] = 50
		tmp = self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['VSS_viastack_1to3InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array5']['_XYCoordinates'] = path_list

		### Array 6 : Output Routing Via Generation in PMOS 1 ###
		self._DesignParameter['array6'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array6In{}'.format(_Name)))[0]
		self._DesignParameter['array6']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=4))

		tmp = self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']
		Output_points = []
		offset = self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Output_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])
		self._DesignParameter['array6']['_XYCoordinates'] = Output_points

		### Array 7 : Output Routing Via Generation in PMOS 2 ###
		self._DesignParameter['array7'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array7In{}'.format(_Name)))[0]
		self._DesignParameter['array7']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=4))

		tmp = self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']
		Output_points = []
		offset = self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Output_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])
		self._DesignParameter['array7']['_XYCoordinates'] = Output_points

		### Array 8 : Output Routing Via Generation in PMOS 3 ###
		self._DesignParameter['array8'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array8In{}'.format(_Name)))[0]
		self._DesignParameter['array8']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=4))

		tmp = self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']
		Output_points = []
		offset = self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Output_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])
		self._DesignParameter['array8']['_XYCoordinates'] = Output_points

		### Array 9 : Output Routing Via Generation in PMOS 4 ###
		self._DesignParameter['array9'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array9In{}'.format(_Name)))[0]
		self._DesignParameter['array9']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=4))

		tmp = self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']
		Output_points = []
		offset = self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Output_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])
		self._DesignParameter['array9']['_XYCoordinates'] = Output_points

		### Array 10 : Output Routing Via Generation in bot NMOS ###
		self._DesignParameter['array10'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array10In{}'.format(_Name)))[0]
		self._DesignParameter['array10']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=6))

		tmp = self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']
		Output_points = []
		offset = self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Output_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])
		self._DesignParameter['array10']['_XYCoordinates'] = Output_points

		### Array 11 : Additional Poly Path on PMOS 1 Gate ###
		self._DesignParameter['array11'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array11']['_Width'] = 30
		tmp = self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['PMOS1InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['PCCAM1_CDNS_6375475055680_1InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array11']['_XYCoordinates'] = path_list

		### Array 12 : Additional Poly Path on PMOS 2 Gate ###
		self._DesignParameter['array12'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array12']['_Width'] = 30
		tmp = self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['PMOS2InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['PCCAM1_CDNS_6375475055680_1InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array12']['_XYCoordinates'] = path_list

		### Array 13 : Additional Poly Path on PMOS 3 Gate ###
		self._DesignParameter['array13'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array13']['_Width'] = 30
		tmp = self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['PMOS3InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['PCCAM1_CDNS_6375475055680_1InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array13']['_XYCoordinates'] = path_list

		### Array 14 : Additional Poly Path on PMOS 4 Gate ###
		self._DesignParameter['array14'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array14']['_Width'] = 30
		tmp = self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['PMOS4InPMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['PCCAM1_CDNS_6375475055680_1InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array14']['_XYCoordinates'] = path_list

		### Array 15 : Additional Poly Path on bot NMOS Gate ###
		self._DesignParameter['array15'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array15']['_Width'] = 30
		tmp = self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['nmos_bot_gate_poly_viaInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array15']['_XYCoordinates'] = path_list

		### Array 16 : Additional Poly Path on NMOS 1 Gate ###
		self._DesignParameter['array16'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array16']['_Width'] = 30
		tmp = self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['pccam_nmos_leftInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array16']['_XYCoordinates'] = path_list

		### Array 17 : Additional Poly Path on NMOS 2 Gate ###
		self._DesignParameter['array17'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array17']['_Width'] = 30
		tmp = self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['pccam_nmos_rightInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array17']['_XYCoordinates'] = path_list

		### Array 18 : Additional Poly Path on NMOS 3 Gate ###
		self._DesignParameter['array18'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array18']['_Width'] = 30
		tmp = self._DesignParameter['NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['PCCAM1_CDNS_6375475055654_12InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array18']['_XYCoordinates'] = path_list

		### Array 19 : Additional Poly Path on NMOS 4 Gate ###
		self._DesignParameter['array19'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array19']['_Width'] = 30
		tmp = self._DesignParameter['NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		target_list = []
		path_list = []
		target_y = self._DesignParameter['PCCAM1_CDNS_6375475055654_12InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][1]
		for i in range(0,len(Routing_points)):
			target_list.append([Routing_points[i][0], target_y])
		for x,y in zip(target_list,Routing_points):
			path_list.append([x,y])
		self._DesignParameter['array19']['_XYCoordinates'] = path_list

		### Array 20 : Additional Dummy Poly Boundary on bot NMOS ###
		self._DesignParameter['array20'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1])
		self._DesignParameter['array20']['_XWidth'] = 30
		DRCObj = DRC.DRC()
		self._DesignParameter['array20']['_YWidth'] = round(DRCObj._PODummyMinArea // self._DesignParameter['array20']['_XWidth'])

		tmp = self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']
		points = []
		offset = self._DesignParameter['nmos_botInSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			if i == 0 or i == (len(tmp)-1):
				points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		self._DesignParameter['array20']['_XYCoordinates'] = points

		### Array 21, 22 : Output Routing Via Generation in NMOS 1 : Via_Up, Via_Down ###
		self._DesignParameter['array21'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array21In{}'.format(_Name)))[0]
		self._DesignParameter['array21']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=7))
		self._DesignParameter['array22'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array22In{}'.format(_Name)))[0]
		self._DesignParameter['array22']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=7))

		tmp = self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		tmplist1 = []
		tmplist2 = []
		for i in range(len(Routing_points)):
			if i % 2 == 1:		# Even numbers : Down
				Routing_points[i] = [Routing_points[i][0],Routing_points[i][1] - 32]
				tmplist1.append(Routing_points[i])
			elif i % 2 == 0: 	# Odd numbers : Up
				Routing_points[i] = [Routing_points[i][0], Routing_points[i][1] + 32]
				tmplist2.append(Routing_points[i])

		self._DesignParameter['array21']['_XYCoordinates'] = tmplist1
		self._DesignParameter['array22']['_XYCoordinates'] = tmplist2

		### Array 23, 24 : Output Routing Via Generation in NMOS 2 : Via_Up, Via_Down ###
		self._DesignParameter['array23'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array23In{}'.format(_Name)))[0]
		self._DesignParameter['array23']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=7))
		self._DesignParameter['array24'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='array24In{}'.format(_Name)))[0]
		self._DesignParameter['array24']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=7))

		tmp = self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		tmplist1 = []
		tmplist2 = []
		for i in range(len(Routing_points)):
			if i % 2 == 1:		# Even numbers : Down
				Routing_points[i] = [Routing_points[i][0],Routing_points[i][1] - 32]
				tmplist1.append(Routing_points[i])
			elif i % 2 == 0: 	# Odd numbers : Up
				Routing_points[i] = [Routing_points[i][0], Routing_points[i][1] + 32]
				tmplist2.append(Routing_points[i])

		self._DesignParameter['array23']['_XYCoordinates'] = tmplist1
		self._DesignParameter['array24']['_XYCoordinates'] = tmplist2

		### Array 25,26 : Additional Metal2 Routing On NMOS 1 ###
		self._DesignParameter['array25'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
		self._DesignParameter['array25']['_Width'] = 50
		self._DesignParameter['array26'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
		self._DesignParameter['array26']['_Width'] = 50

		tmp = self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		tmplist1 = [] # Down
		tmplist2 = [] # Up
		for i in range(len(Routing_points)):
			if i % 2 == 0:		# Even numbers : Down
				Routing_points[i] = [Routing_points[i][0],Routing_points[i][1] - 32]
				tmplist1.append(Routing_points[i])
			elif i % 2 == 1: 	# Odd numbers : Up
				Routing_points[i] = [Routing_points[i][0], Routing_points[i][1] + 32]
				tmplist2.append(Routing_points[i])

		target_y_for_downway = self._DesignParameter['METAL2_path_27']['_XYCoordinates'][0][0][1]
		target_y_for_upway = self._DesignParameter['METAL2_path_28']['_XYCoordinates'][0][1][1]

		path_for_upway = []
		path_for_downway = []
		for i in range(len(tmplist1)):
			path_for_downway.append([tmplist1[i],[tmplist1[i][0],target_y_for_downway]])
		for i in range(len(tmplist2)):
			path_for_upway.append([tmplist2[i],[tmplist2[i][0],target_y_for_upway]])
		self._DesignParameter['array25']['_XYCoordinates'] = path_for_upway
		self._DesignParameter['array26']['_XYCoordinates'] = path_for_downway

		### Array 27,28 : Additional Metal2 Routing On NMOS 2 ###
		self._DesignParameter['array27'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
		self._DesignParameter['array27']['_Width'] = 50
		self._DesignParameter['array28'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1])
		self._DesignParameter['array28']['_Width'] = 50

		tmp = self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']
		Routing_points = []
		offset = self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0]
		for i in range(len(tmp)):
			Routing_points.append([tmp[i][0]+offset[0],tmp[i][1]+offset[1]])

		tmplist1 = [] # Down
		tmplist2 = [] # Up
		for i in range(len(Routing_points)):
			if i % 2 == 0:		# Even numbers : Down
				Routing_points[i] = [Routing_points[i][0],Routing_points[i][1] - 32]
				tmplist1.append(Routing_points[i])
			elif i % 2 == 1: 	# Odd numbers : Up
				Routing_points[i] = [Routing_points[i][0], Routing_points[i][1] + 32]
				tmplist2.append(Routing_points[i])

		target_y_for_downway = self._DesignParameter['METAL2_path_27']['_XYCoordinates'][0][0][1]
		target_y_for_upway = self._DesignParameter['METAL2_path_28']['_XYCoordinates'][0][1][1]

		path_for_upway = []
		path_for_downway = []
		for i in range(len(tmplist1)):
			path_for_downway.append([tmplist1[i],[tmplist1[i][0],target_y_for_downway]])
		for i in range(len(tmplist2)):
			path_for_upway.append([tmplist2[i],[tmplist2[i][0],target_y_for_upway]])
		self._DesignParameter['array27']['_XYCoordinates'] = path_for_upway
		self._DesignParameter['array28']['_XYCoordinates'] = path_for_downway

		### Array 29 : Output Routing Via Generation in NMOS 1 : Metal 3 to Metal 4 ###
		self._DesignParameter['array29'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='array29In{}'.format(_Name)))[0]
		self._DesignParameter['array29']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))

		edge_of_y = self._DesignParameter['METAL2_path_28']['_XYCoordinates'][0][0][1]
		tmpViaObj = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='tmp'))[0]
		tmpViaObj['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		tmpViaObj['_XYCoordinates'] = [[0,0]]
		height = tmpViaObj['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']
		target_y = edge_of_y + round(height / 2)
		target_x = []

		offset = self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][0]

		target_x.append(self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0] + offset)
		target_x.append(self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][5][0] + offset)
		target_x.append(self._DesignParameter['NMOS1InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][7][0] + offset)

		target_coordinate_list = []
		for i in range(len(target_x)):
			target_coordinate_list.append([target_x[i],target_y])
		self._DesignParameter['array29']['_XYCoordinates'] = target_coordinate_list

		### Array 30 : Output Routing Via Generation in NMOS 2 : Metal 3 to Metal 4 ###
		self._DesignParameter['array30'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='array30In{}'.format(_Name)))[0]
		self._DesignParameter['array30']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		edge_of_y = self._DesignParameter['METAL2_path_28']['_XYCoordinates'][0][0][1]
		target_y = edge_of_y + round(height / 2)
		target_x = []

		offset = self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates'][0][0]

		target_x.append(self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][9][0] + offset)
		target_x.append(self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][5][0] + offset)
		target_x.append(self._DesignParameter['NMOS2InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][7][0] + offset)

		target_coordinate_list = []
		for i in range(len(target_x)):
			target_coordinate_list.append([target_x[i],target_y])
		self._DesignParameter['array30']['_XYCoordinates'] = target_coordinate_list

		### Array 31 : Additional Met4 Path For NMOS 1 ###
		self._DesignParameter['array31'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1])
		self._DesignParameter['array31']['_Width'] = 50

		target_coordinate_list = []
		target_y = self._DesignParameter['array6']['_XYCoordinates'][0][1]
		path_list = []

		for i in range(len(self._DesignParameter['array29']['_XYCoordinates'])):
			target_coordinate_list.append([self._DesignParameter['array29']['_XYCoordinates'][i][0],target_y])
		for i in range(len(target_coordinate_list)):
			path_list.append([self._DesignParameter['array29']['_XYCoordinates'][i],target_coordinate_list[i]])
		self._DesignParameter['array31']['_XYCoordinates'] = path_list

		### Array 32 : Additional Met4 Path For NMOS 2 ###
		self._DesignParameter['array32'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1])
		self._DesignParameter['array32']['_Width'] = 50

		target_coordinate_list = []
		target_y = self._DesignParameter['array7']['_XYCoordinates'][0][1]
		path_list = []

		for i in range(len(self._DesignParameter['array30']['_XYCoordinates'])):
			target_coordinate_list.append([self._DesignParameter['array30']['_XYCoordinates'][i][0],target_y])
		for i in range(len(target_coordinate_list)):
			path_list.append([self._DesignParameter['array30']['_XYCoordinates'][i],target_coordinate_list[i]])
		self._DesignParameter['array32']['_XYCoordinates'] = path_list

		### Array 33 : Additional Met1 Path For inner NMOS 1 ###
		self._DesignParameter['array33'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['array33']['_Width'] = 50

		tmp = self._DesignParameter['NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']
		offset = self._DesignParameter['NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates']
		tmplist = []
		for i in range(len(tmp)):
			if i % 2 == 0:
				tmplist.append(tmp[i][0] + offset[0][0])
		y_source = offset[0][1]
		y_target = offset[0][1] - self._DesignParameter['NMOS3InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - DRCObj._Metal1MinSpace
		path_list = []
		for i in range(len(tmplist)):
			path_list.append([[tmplist[i],y_source],[tmplist[i],y_target]])
		self._DesignParameter['array33']['_XYCoordinates'] = path_list

		### Array 34 : Additional Met1 Path For inner NMOS 2 ###
		self._DesignParameter['array34'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['array34']['_Width'] = 50

		tmp = self._DesignParameter['NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']
		offset = self._DesignParameter['NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_XYCoordinates']
		tmplist = []
		for i in range(len(tmp)):
			if i % 2 == 0:
				tmplist.append(tmp[i][0] + offset[0][0])
		y_source = offset[0][1]
		y_target = offset[0][1] - self._DesignParameter['NMOS4InNMOSSetofSlicer_0InSlicerInSlicerWithSRLatch_0_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2 - DRCObj._Metal1MinSpace
		path_list = []
		for i in range(len(tmplist)):
			path_list.append([[tmplist[i],y_source],[tmplist[i],y_target]])
		self._DesignParameter['array34']['_XYCoordinates'] = path_list


if __name__ == '__main__':
	Obj = topcell(_DesignParameter=None, _Name='StrongArmLatch')
	Obj._CalculateDesignParameter()
	# PbodyContactObj=_PbodyContact(_PbodyContactDesignParameter=DesignParameters.PbodyDesignParameter, _PbodyContactName='PbodyContact2')
	# PbodyContactObj=_PbodyContact(_Technology=DesignParameters._Technology, _XYCoordinatePbody=[0,0], _NumberOfPbodyCO=2, _WidthXPbodyOD=890, _WidthYPbodyOD=420, _WidthXPbodyNP=1250, _WidthYPbodyNP=780, _WidthPbodyCO=220, _LengthPbodyBtwCO=470, _WidthXPbodyMet1=810, _WidthYPbodyMet1=340, _PbodyName='PbodyContact')
	Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Obj._DesignParameter)
	_fileName = 'StrongArmLatch.gds'
	testStreamFile = open('./StrongArmLatch.gds', 'wb')

	tmp = Obj._CreateGDSStream(Obj._DesignParameter['_GDSFile']['_GDSFile'])

	tmp.write_binary_gds_stream(testStreamFile)

	testStreamFile.close()
