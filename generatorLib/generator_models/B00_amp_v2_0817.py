from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import opppcres_b_v2
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NSubRing
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PSubRing
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1_resize
from generatorLib.generator_models import NCAP
from generatorLib.generator_models import PbodyContact

class B00_amp_v2(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='B00_amp_v2'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,finger_N1=4,W_N=2400,Dummy=True,XVT='RVT',finger_N2=8,finger_N3=8,W_P=2400,finger_P1=4,finger_P2=4,finger_P5=5,finger_N5=2,finger_N4=2,finger_P3=1,finger_P4=1,Guad_via=2,res_compensation_W=1000,res_compensation_L=3500,res_compensation_series=2,NumofGate_res_com=5,NumofRX_res_com=2,L_cap=2600,W_cap=2600,L=450):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		L_N = L_P = L
		if (L >= 50):
		    dist = 114
		else:
		    dist = 96
		fingerA = ((((finger_P2 + finger_P5) - finger_N3) - finger_N5) + 1)
		fingerB = ((finger_N4 - finger_N5) + 1)
		fingerC = (((((finger_P1 + finger_P3) + finger_P4) + 2) - finger_N3) - finger_N5)
		finger_N_Dummy2 = max(2, fingerA, fingerB, fingerC)
		Guad_W = (((drc._CoMinWidth * Guad_via) + (drc._CoMinSpace * (Guad_via - 1))) + (drc._CoMinEnclosureByODAtLeastTwoSide * 2))
		self._DesignParameter['N1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='N1In{}'.format(_Name)))[0]
		self._DesignParameter['N1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=finger_N1, _NMOSChannelWidth=W_N, _NMOSChannellength=L_N, _NMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['N1']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['N2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='N2In{}'.format(_Name)))[0]
		self._DesignParameter['N2']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=finger_N2, _NMOSChannelWidth=W_N, _NMOSChannellength=L_N, _NMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['N2']['_XYCoordinates'] = [[(self._DesignParameter['N1']['_XYCoordinates'][0][0] - ((dist + L_N) * (1 + ((finger_N1 + finger_N2) / 2)))), self._DesignParameter['N1']['_XYCoordinates'][0][1]]]
		self._DesignParameter['N3'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='N3In{}'.format(_Name)))[0]
		self._DesignParameter['N3']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=finger_N3, _NMOSChannelWidth=W_N, _NMOSChannellength=L_N, _NMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['N3']['_XYCoordinates'] = [[(self._DesignParameter['N1']['_XYCoordinates'][0][0] + ((dist + L_N) * (1 + ((finger_N1 + finger_N3) / 2)))), self._DesignParameter['N1']['_XYCoordinates'][0][1]]]
		self._DesignParameter['P_Dummy0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='P_Dummy0In{}'.format(_Name)))[0]
		self._DesignParameter['P_Dummy0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger_N1, _PMOSChannelWidth=W_P, _PMOSChannellength=L_P, _PMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['P_Dummy0']['_XYCoordinates'] = [[self._DesignParameter['N1']['_XYCoordinates'][0][0], ((self._DesignParameter['N1']['_XYCoordinates'][0][1] + ((W_N + W_P) / 2)) + (((Guad_W + 310) + 100) * 2))]]
		self._DesignParameter['P1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='P1In{}'.format(_Name)))[0]
		self._DesignParameter['P1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger_P1, _PMOSChannelWidth=W_P, _PMOSChannellength=L_P, _PMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['P1']['_XYCoordinates'] = [[(self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] - ((dist + L_P) * (1 + ((finger_N1 + finger_P1) / 2)))), self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['P2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='P2In{}'.format(_Name)))[0]
		self._DesignParameter['P2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger_P2, _PMOSChannelWidth=W_P, _PMOSChannellength=L_P, _PMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['P2']['_XYCoordinates'] = [[(self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + ((dist + L_P) * (1 + ((finger_N1 + finger_P2) / 2)))), self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['N_Dummy2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='N_Dummy2In{}'.format(_Name)))[0]
		self._DesignParameter['N_Dummy2']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=finger_N_Dummy2, _NMOSChannelWidth=W_N, _NMOSChannellength=L_N, _NMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['N_Dummy2']['_XYCoordinates'] = [[(self._DesignParameter['N3']['_XYCoordinates'][0][0] + ((dist + L_N) * (1 + ((finger_N3 + finger_N_Dummy2) / 2)))), self._DesignParameter['N1']['_XYCoordinates'][0][1]]]
		self._DesignParameter['N5'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='N5In{}'.format(_Name)))[0]
		self._DesignParameter['N5']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=finger_N5, _NMOSChannelWidth=W_N, _NMOSChannellength=L_N, _NMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['N5']['_XYCoordinates'] = [[(self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + ((dist + L_N) * (1 + ((finger_N5 + finger_N_Dummy2) / 2)))), self._DesignParameter['N1']['_XYCoordinates'][0][1]]]
		finger_P_Dummy1 = ((((finger_N3 + finger_N5) - finger_P2) - finger_P5) + finger_N_Dummy2)
		self._DesignParameter['P_Dummy1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='P_Dummy1In{}'.format(_Name)))[0]
		self._DesignParameter['P_Dummy1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger_P_Dummy1, _PMOSChannelWidth=W_P, _PMOSChannellength=L_P, _PMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['P_Dummy1']['_XYCoordinates'] = [[(self._DesignParameter['P2']['_XYCoordinates'][0][0] + ((dist + L_P) * (1 + ((finger_P2 + finger_P_Dummy1) / 2)))), self._DesignParameter['P2']['_XYCoordinates'][0][1]]]
		self._DesignParameter['P5'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='P5In{}'.format(_Name)))[0]
		self._DesignParameter['P5']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger_P5, _PMOSChannelWidth=W_P, _PMOSChannellength=L_P, _PMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['P5']['_XYCoordinates'] = [[(self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + ((dist + L_P) * (1 + ((finger_P_Dummy1 + finger_P5) / 2)))), self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1]]]
		finger_N_Dummy1 = ((finger_N_Dummy2 + finger_N5) - finger_N4)
		self._DesignParameter['N_Dummy1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='N_Dummy1In{}'.format(_Name)))[0]
		self._DesignParameter['N_Dummy1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=finger_N_Dummy1, _NMOSChannelWidth=W_N, _NMOSChannellength=L_N, _NMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['N_Dummy1']['_XYCoordinates'] = [[(self._DesignParameter['N2']['_XYCoordinates'][0][0] - ((dist + L_N) * (1 + ((finger_N_Dummy1 + finger_N2) / 2)))), self._DesignParameter['N2']['_XYCoordinates'][0][1]]]
		self._DesignParameter['N4'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='N4In{}'.format(_Name)))[0]
		self._DesignParameter['N4']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=finger_N4, _NMOSChannelWidth=W_N, _NMOSChannellength=L_N, _NMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['N4']['_XYCoordinates'] = [[(self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] - ((dist + L_N) * (1 + ((finger_N_Dummy1 + finger_N4) / 2)))), self._DesignParameter['N1']['_XYCoordinates'][0][1]]]
		finger_P_Dummy2 = ((((((finger_N3 + finger_N5) + finger_N_Dummy2) - finger_P1) - finger_P3) - finger_P4) - 1)
		self._DesignParameter['P_Dummy2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='P_Dummy2In{}'.format(_Name)))[0]
		self._DesignParameter['P_Dummy2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger_P_Dummy2, _PMOSChannelWidth=W_P, _PMOSChannellength=L_P, _PMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['P_Dummy2']['_XYCoordinates'] = [[(self._DesignParameter['P1']['_XYCoordinates'][0][0] - ((dist + L_P) * (1 + ((finger_P1 + finger_P_Dummy2) / 2)))), self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['P3'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='P3In{}'.format(_Name)))[0]
		self._DesignParameter['P3']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger_P3, _PMOSChannelWidth=W_P, _PMOSChannellength=L_P, _PMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['P3']['_XYCoordinates'] = [[(self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] - ((dist + L_P) * (1 + ((finger_P_Dummy2 + finger_P3) / 2)))), self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['P4'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='P4In{}'.format(_Name)))[0]
		self._DesignParameter['P4']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger_P4, _PMOSChannelWidth=W_P, _PMOSChannellength=L_P, _PMOSDummy=Dummy, _GateSpacing=None, _SDWidth=None, _XVT=XVT, _PCCrit=None))
		self._DesignParameter['P4']['_XYCoordinates'] = [[(self._DesignParameter['P3']['_XYCoordinates'][0][0] - ((dist + L_P) * (1 + ((finger_P3 + finger_P4) / 2)))), self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1]]]
		Dummy_M1_H = ((Guad_W / 2) + 314)
		self._DesignParameter['Dummy_M1_4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) - 6), _YWidth=Dummy_M1_H)
		self._DesignParameter['Dummy_M1_4']['_XYCoordinates'] = [[self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0], (((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (Dummy_M1_H / 2))]]
		self._DesignParameter['Dummy_M1_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) - 6), _YWidth=Dummy_M1_H)
		self._DesignParameter['Dummy_M1_1']['_XYCoordinates'] = [[self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0], (((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][1] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (Dummy_M1_H / 2))]]
		self._DesignParameter['Dummy_M1_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) - 6), _YWidth=Dummy_M1_H)
		self._DesignParameter['Dummy_M1_2']['_XYCoordinates'] = [[self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0], (((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][1] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (Dummy_M1_H / 2))]]
		self._DesignParameter['Dummy_M1_3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) - 6), _YWidth=Dummy_M1_H)
		self._DesignParameter['Dummy_M1_3']['_XYCoordinates'] = [[self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0], (((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][1] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (Dummy_M1_H / 2))]]
		self._DesignParameter['Dummy_M1_5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) - 6), _YWidth=Dummy_M1_H)
		self._DesignParameter['Dummy_M1_5']['_XYCoordinates'] = [[self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0], (((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][1] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (Dummy_M1_H / 2))]]
		self._DesignParameter['PCCAM1_P_Dummy0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_P_Dummy0In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_P_Dummy0']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N1 - 1)][0]) + (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N1 - 1)][0]) + (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N1 - 1)][0]) + (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_P_Dummy0']['_XYCoordinates'] = [[self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0], (((self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['PCCAM1_P_Dummy_1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_P_Dummy_1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_P_Dummy_1']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P_Dummy1 - 1)][0]) + (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P_Dummy1 - 1)][0]) + (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P_Dummy1 - 1)][0]) + (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_P_Dummy_1']['_XYCoordinates'] = [[self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][0], (((self._DesignParameter['P_Dummy1']['_XYCoordinates'][0][1] + self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['P_Dummy1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['PCCAM1_P_Dummy2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_P_Dummy2In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_P_Dummy2']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P_Dummy2 - 1)][0]) + (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P_Dummy2 - 1)][0]) + (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P_Dummy2 - 1)][0]) + (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_P_Dummy2']['_XYCoordinates'] = [[self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][0], (((self._DesignParameter['P_Dummy2']['_XYCoordinates'][0][1] + self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['P_Dummy2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['PCCAM1_N_Dummy2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_N_Dummy2In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_N_Dummy2']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N_Dummy2 - 1)][0]) + (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N_Dummy2 - 1)][0]) + (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N_Dummy2 - 1)][0]) + (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_N_Dummy2']['_XYCoordinates'] = [[self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][0], (((self._DesignParameter['N_Dummy2']['_XYCoordinates'][0][1] + self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['N_Dummy2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['PCCAM1_N_Dummy1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_N_Dummy1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_N_Dummy1']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N_Dummy1 - 1)][0]) + (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N_Dummy1 - 1)][0]) + (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N_Dummy1 - 1)][0]) + (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_N_Dummy1']['_XYCoordinates'] = [[self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][0], (((self._DesignParameter['N_Dummy1']['_XYCoordinates'][0][1] + self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['N_Dummy1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['PCCAM1_VINn'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_VINnIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_VINn']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N2']['_XYCoordinates'][0][0] + self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N2 - 1)][0]) + (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N2']['_XYCoordinates'][0][0] + self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['N2']['_XYCoordinates'][0][0] + self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N2 - 1)][0]) + (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N2']['_XYCoordinates'][0][0] + self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['N2']['_XYCoordinates'][0][0] + self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N2 - 1)][0]) + (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N2']['_XYCoordinates'][0][0] + self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_VINn']['_XYCoordinates'] = [[self._DesignParameter['N2']['_XYCoordinates'][0][0], (((self._DesignParameter['N2']['_XYCoordinates'][0][1] + self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['PCCAM1_VINp'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_VINpIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_VINp']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N3']['_XYCoordinates'][0][0] + self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N3 - 1)][0]) + (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N3']['_XYCoordinates'][0][0] + self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['N3']['_XYCoordinates'][0][0] + self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N3 - 1)][0]) + (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N3']['_XYCoordinates'][0][0] + self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['N3']['_XYCoordinates'][0][0] + self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N3 - 1)][0]) + (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N3']['_XYCoordinates'][0][0] + self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_VINp']['_XYCoordinates'] = [[self._DesignParameter['N3']['_XYCoordinates'][0][0], (((self._DesignParameter['N3']['_XYCoordinates'][0][1] + self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['PCCAM1_N1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_N1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_N1']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N1']['_XYCoordinates'][0][0] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N1 - 1)][0]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N1']['_XYCoordinates'][0][0] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['N1']['_XYCoordinates'][0][0] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N1 - 1)][0]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N1']['_XYCoordinates'][0][0] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['N1']['_XYCoordinates'][0][0] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N1 - 1)][0]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N1']['_XYCoordinates'][0][0] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_N1']['_XYCoordinates'] = [[self._DesignParameter['N1']['_XYCoordinates'][0][0], (((self._DesignParameter['N1']['_XYCoordinates'][0][1] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['M1V1M2_N1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N1In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_N1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N1']['_XYCoordinates'][0][0] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N1 - 1)][0]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N1']['_XYCoordinates'][0][0] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_N1']['_XYCoordinates'] = [[self._DesignParameter['N1']['_XYCoordinates'][0][0], (((self._DesignParameter['N1']['_XYCoordinates'][0][1] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['PCCAM1_N5'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_N5In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_N5']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N5 - 1)][0]) + (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N5 - 1)][0]) + (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N5 - 1)][0]) + (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_N5']['_XYCoordinates'] = [[self._DesignParameter['N5']['_XYCoordinates'][0][0], (((self._DesignParameter['N5']['_XYCoordinates'][0][1] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['M1V1M2_N5'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N5In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_N5']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N5 - 1)][0]) + (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_N5']['_XYCoordinates'] = [[self._DesignParameter['N5']['_XYCoordinates'][0][0], (((self._DesignParameter['N5']['_XYCoordinates'][0][1] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['PCCAM1_P1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_P1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_P1']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P1']['_XYCoordinates'][0][0] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P1 - 1)][0]) + (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P1']['_XYCoordinates'][0][0] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['P1']['_XYCoordinates'][0][0] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P1 - 1)][0]) + (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P1']['_XYCoordinates'][0][0] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['P1']['_XYCoordinates'][0][0] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P1 - 1)][0]) + (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P1']['_XYCoordinates'][0][0] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_P1']['_XYCoordinates'] = [[self._DesignParameter['P1']['_XYCoordinates'][0][0], (((self._DesignParameter['P1']['_XYCoordinates'][0][1] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['PCCAM1_P2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_P2In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_P2']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P2']['_XYCoordinates'][0][0] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P2 - 1)][0]) + (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P2']['_XYCoordinates'][0][0] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['P2']['_XYCoordinates'][0][0] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P2 - 1)][0]) + (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P2']['_XYCoordinates'][0][0] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['P2']['_XYCoordinates'][0][0] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P2 - 1)][0]) + (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P2']['_XYCoordinates'][0][0] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_P2']['_XYCoordinates'] = [[self._DesignParameter['P2']['_XYCoordinates'][0][0], (((self._DesignParameter['P2']['_XYCoordinates'][0][1] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['PCCAM1_N4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_N4In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_N4']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N4 - 1)][0]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N4 - 1)][0]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N4 - 1)][0]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_N4']['_XYCoordinates'] = [[self._DesignParameter['N4']['_XYCoordinates'][0][0], (((self._DesignParameter['N4']['_XYCoordinates'][0][1] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['M1V1M2_N4'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N4In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_N4']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_N4 - 1)][0]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_N4']['_XYCoordinates'] = [[self._DesignParameter['N4']['_XYCoordinates'][0][0], (((self._DesignParameter['N4']['_XYCoordinates'][0][1] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]
		self._DesignParameter['METAL1_boundary_N4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'] = [[[(((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - 85), (((self._DesignParameter['N4']['_XYCoordinates'][0][1] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)], [(((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + 85), (((self._DesignParameter['N4']['_XYCoordinates'][0][1] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]]
		self._DesignParameter['P1_P2_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['P1_P2_gate']['_XYCoordinates'] = [[[(((self._DesignParameter['P1']['_XYCoordinates'][0][0] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + 3), (((self._DesignParameter['P1']['_XYCoordinates'][0][1] + self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)], [(((self._DesignParameter['P2']['_XYCoordinates'][0][0] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - 85), (((self._DesignParameter['P2']['_XYCoordinates'][0][1] + self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]]
		self._DesignParameter['PCCAM1_P5'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_P5In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_P5']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P5']['_XYCoordinates'][0][0] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P5 - 1)][0]) + (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P5']['_XYCoordinates'][0][0] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['P5']['_XYCoordinates'][0][0] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P5 - 1)][0]) + (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P5']['_XYCoordinates'][0][0] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['P5']['_XYCoordinates'][0][0] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P5 - 1)][0]) + (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P5']['_XYCoordinates'][0][0] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_P5']['_XYCoordinates'] = [[self._DesignParameter['P5']['_XYCoordinates'][0][0], (((self._DesignParameter['P5']['_XYCoordinates'][0][1] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['M1V1M2_P5'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P5In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_P5']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(2, max(1, (1 + int((((L_P - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_P5']['_XYCoordinates'] = [[self._DesignParameter['P5']['_XYCoordinates'][0][0], (((self._DesignParameter['P5']['_XYCoordinates'][0][1] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['M2V2M3_P5'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_P5In{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_P5']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(2, max(1, (1 + int((((L_P - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_P5']['_XYCoordinates'] = [[self._DesignParameter['P5']['_XYCoordinates'][0][0], (((self._DesignParameter['P5']['_XYCoordinates'][0][1] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['PCCAM1_P3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_P3In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_P3']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P3 - 1)][0]) + (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P3 - 1)][0]) + (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P3 - 1)][0]) + (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_P3']['_XYCoordinates'] = [[self._DesignParameter['P3']['_XYCoordinates'][0][0], (((self._DesignParameter['P3']['_XYCoordinates'][0][1] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['P3_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['P3_gate']['_XYCoordinates'] = [[[(((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + 3), (((self._DesignParameter['P3']['_XYCoordinates'][0][1] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)], [(((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - 85), (((self._DesignParameter['P3']['_XYCoordinates'][0][1] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]]
		self._DesignParameter['PCCAM1_P4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='PCCAM1_P4In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_P4']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P4 - 1)][0]) + (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1, Met1XWidth=(((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P4 - 1)][0]) + (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), Met1YWidth=50, POXWidth=(((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P4 - 1)][0]) + (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), POYWidth=50))
		self._DesignParameter['PCCAM1_P4']['_XYCoordinates'] = [[self._DesignParameter['P4']['_XYCoordinates'][0][0], (((self._DesignParameter['P4']['_XYCoordinates'][0][1] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['M1V1M2_P4'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P4In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_P4']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(finger_P4 - 1)][0]) + (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_P4']['_XYCoordinates'] = [[self._DesignParameter['P4']['_XYCoordinates'][0][0], (((self._DesignParameter['P4']['_XYCoordinates'][0][1] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]
		self._DesignParameter['METAL1_P4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['METAL1_P4']['_XYCoordinates'] = [[[(((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - 85), (((self._DesignParameter['P4']['_XYCoordinates'][0][1] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)], [(((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + 3), (((self._DesignParameter['P4']['_XYCoordinates'][0][1] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]]
		if (((((finger_P1 + finger_P_Dummy2) + finger_P3) % 2) == 0) and ((finger_P4 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P4_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P4_drain_path']['_XYCoordinates'] = path_list
		if (((((finger_P1 + finger_P_Dummy2) + finger_P3) % 2) == 0) and ((finger_P4 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P4_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P4_drain_path']['_XYCoordinates'] = path_list
		if (((((finger_P1 + finger_P_Dummy2) + finger_P3) % 2) == 1) and ((finger_P4 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P4_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P4_drain_path']['_XYCoordinates'] = path_list
		if (((((finger_P1 + finger_P_Dummy2) + finger_P3) % 2) == 1) and ((finger_P4 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_P4']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P4_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P4_drain_path']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL1_P4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['METAL1_P4']['_XYCoordinates'] = [[[min((self._DesignParameter['P4_drain_path']['_XYCoordinates'][0][0][0] - 25), (((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + 85)), (((self._DesignParameter['P4']['_XYCoordinates'][0][1] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)], [max((self._DesignParameter['P4_drain_path']['_XYCoordinates'][(- 1)][0][0] + 25), (((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - 85)), (((self._DesignParameter['P4']['_XYCoordinates'][0][1] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]]
		self._DesignParameter['N4_P4_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=max(L_N, L_P))
		self._DesignParameter['N4_P4_path']['_XYCoordinates'] = [[[(self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), (self._DesignParameter['PCCAM1_P4']['_XYCoordinates'][0][1] + 25)], [(self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), (self._DesignParameter['PCCAM1_N4']['_XYCoordinates'][0][1] - 25)]]]
		self._DesignParameter['N5_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=200)
		self._DesignParameter['N5_path']['_XYCoordinates'] = [[[self._DesignParameter['N5']['_XYCoordinates'][0][0], (((self._DesignParameter['N1']['_XYCoordinates'][0][1] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 69)], [self._DesignParameter['N5']['_XYCoordinates'][0][0], (((((self._DesignParameter['N1']['_XYCoordinates'][0][1] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 314) + Guad_W) - 25)]]]
		self._DesignParameter['N1_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=200)
		self._DesignParameter['N1_path']['_XYCoordinates'] = [[[self._DesignParameter['N1']['_XYCoordinates'][0][0], (((((self._DesignParameter['N1']['_XYCoordinates'][0][1] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 314) + Guad_W) - 25)], [self._DesignParameter['N1']['_XYCoordinates'][0][0], (((self._DesignParameter['N1']['_XYCoordinates'][0][1] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 69)]]]
		self._DesignParameter['N1_N4_N5_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(Guad_W - 50))
		self._DesignParameter['N1_N4_N5_path']['_XYCoordinates'] = [[[self._DesignParameter['N4_P4_path']['_XYCoordinates'][0][0][0], ((((self._DesignParameter['N1']['_XYCoordinates'][0][1] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 314) + (Guad_W / 2))], [self._DesignParameter['N5']['_XYCoordinates'][0][0], ((((self._DesignParameter['N1']['_XYCoordinates'][0][1] + self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 314) + (Guad_W / 2))]]]
		self._DesignParameter['P_guad'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='P_guadIn{}'.format(_Name)))[0]
		self._DesignParameter['P_guad']['_DesignObj']._CalculateDesignParameter(**dict(height=((self._DesignParameter['P5']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] + 400) + Guad_W), width=(((((self._DesignParameter['P5']['_XYCoordinates'][0][0] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + 400) + Guad_W), contact_bottom=Guad_via, contact_top=Guad_via, contact_left=Guad_via, contact_right=Guad_via))
		self._DesignParameter['P_guad']['_XYCoordinates'] = [[(+ self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1])]]
		self._DesignParameter['N_guad'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='N_guadIn{}'.format(_Name)))[0]
		self._DesignParameter['N_guad']['_DesignObj']._CalculateDesignParameter(**dict(height=((self._DesignParameter['N5']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] + 400) + Guad_W), width=(((((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + 400) + Guad_W), contact_bottom=Guad_via, contact_top=Guad_via, contact_left=Guad_via, contact_right=Guad_via))
		self._DesignParameter['N_guad']['_XYCoordinates'] = [[(+ self._DesignParameter['N1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['N1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M1V1M2_N1_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N1_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_N1_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		self._DesignParameter['M1V1M2_N1_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (((- W_N) / 2) + 131))
		for i in range(len(self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['M1V1M2_N1_drain']['_XYCoordinates'] = XYList
		path_list = []
		xy_offset = (0, ((W_N / 2) - 9))
		if (len(self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = 50
		elif (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = 50
		elif (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = 50
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N1']['_XYCoordinates'][0][1])], self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N1']['_XYCoordinates'][0][1])], self._DesignParameter['N1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['N1_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['N1_source_path']['_XYCoordinates'] = path_list
		if ((finger_N1 % 2) == 0):
		    self._DesignParameter['M1V1M2_N3_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N3_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N3_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N3_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_N) / 2) + 131))
		    for i in range(len(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N3_source']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 1):
		    self._DesignParameter['M1V1M2_N3_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N3_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N3_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N3_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_N) / 2) + 131))
		    for i in range(len(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N3_source']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 0):
		    self._DesignParameter['M2V2M3_N3_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_N3_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M2V2M3_N3_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		    self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_N / 2) - 131))
		    for i in range(len(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 1):
		    self._DesignParameter['M2V2M3_N3_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_N3_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M2V2M3_N3_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		    self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_N / 2) - 131))
		    for i in range(len(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 0):
		    self._DesignParameter['M1V1M2_N3_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N3_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N3_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N3_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_N / 2) - 131))
		    for i in range(len(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N3_drain']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 1):
		    self._DesignParameter['M1V1M2_N3_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N3_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N3_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N3_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_N / 2) - 131))
		    for i in range(len(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N3_drain']['_XYCoordinates'] = XYList
		if ((finger_N2 % 2) == 0):
		    self._DesignParameter['M1V1M2_N2_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N2_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N2_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N2_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_N) / 2) + 131))
		    for i in range(len(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N2_source']['_XYCoordinates'] = XYList
		if ((finger_N2 % 2) == 1):
		    self._DesignParameter['M1V1M2_N2_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N2_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N2_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N2_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_N) / 2) + 131))
		    for i in range(len(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N2_source']['_XYCoordinates'] = XYList
		self._DesignParameter['N1_N2_N3_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['N1_N2_N3_path']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_N2_source']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_N2_source']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M1V1M2_N3_source']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['M1V1M2_N3_source']['_XYCoordinates'][(- 1)][1])]]]
		if ((finger_N2 % 2) == 0):
		    self._DesignParameter['M1V1M2_N2_darin'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N2_darinIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N2_darin']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N2_darin']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_N / 2) - 131))
		    for i in range(len(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N2_darin']['_XYCoordinates'] = XYList
		if ((finger_N2 % 2) == 1):
		    self._DesignParameter['M1V1M2_N2_darin'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N2_darinIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N2_darin']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N2_darin']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_N / 2) - 131))
		    for i in range(len(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N2_darin']['_XYCoordinates'] = XYList
		if ((finger_N2 % 2) == 0):
		    self._DesignParameter['M2V2M3_N2_darin'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_N2_darinIn{}'.format(_Name)))[0]
		    self._DesignParameter['M2V2M3_N2_darin']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		    self._DesignParameter['M2V2M3_N2_darin']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_N / 2) - 131))
		    for i in range(len(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M2V2M3_N2_darin']['_XYCoordinates'] = XYList
		if ((finger_N2 % 2) == 1):
		    self._DesignParameter['M2V2M3_N2_darin'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_N2_darinIn{}'.format(_Name)))[0]
		    self._DesignParameter['M2V2M3_N2_darin']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		    self._DesignParameter['M2V2M3_N2_darin']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_N / 2) - 131))
		    for i in range(len(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M2V2M3_N2_darin']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 0):
		    self._DesignParameter['M1V1M2_P2_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P2_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P2_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P2_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_P) / 2) + 131))
		    for i in range(len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P2_source']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 1):
		    self._DesignParameter['M1V1M2_P2_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P2_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P2_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P2_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_P) / 2) + 131))
		    for i in range(len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P2_source']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 0):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P2']['_XYCoordinates'][0][1])], self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P2']['_XYCoordinates'][0][1])], self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P2_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P2_source_path']['_XYCoordinates'] = path_list
		if ((finger_N1 % 2) == 1):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P2']['_XYCoordinates'][0][1])], self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P2']['_XYCoordinates'][0][1])], self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P2_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P2_source_path']['_XYCoordinates'] = path_list
		if ((finger_N1 % 2) == 0):
		    self._DesignParameter['M2V2M3_P2_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_P2_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M2V2M3_P2_source']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		    self._DesignParameter['M2V2M3_P2_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_P) / 2) + 131))
		    for i in range(len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M2V2M3_P2_source']['_XYCoordinates'] = XYList
		if ((finger_N1 % 2) == 1):
		    self._DesignParameter['M2V2M3_P2_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_P2_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M2V2M3_P2_source']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		    self._DesignParameter['M2V2M3_P2_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_P) / 2) + 131))
		    for i in range(len(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M2V2M3_P2_source']['_XYCoordinates'] = XYList
		self._DesignParameter['P2_N3_P5'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=50)
		self._DesignParameter['P2_N3_P5']['_XYCoordinates'] = [[[(+ self._DesignParameter['M2V2M3_P2_source']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['M2V2M3_P2_source']['_XYCoordinates'][(- 1)][1])], [(self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]), self._DesignParameter['M2V2M3_P2_source']['_XYCoordinates'][0][1]], [(self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]), self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'][0][1]], [self._DesignParameter['M2V2M3_P5']['_XYCoordinates'][0][0], self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'][0][1]], [(+ self._DesignParameter['M2V2M3_P5']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_P5']['_XYCoordinates'][0][1])]]]
		if ((finger_P1 % 2) == 0):
		    self._DesignParameter['M1V1M2_P1_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P1_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P1_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P1_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_P) / 2) + 131))
		    for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P1_drain']['_XYCoordinates'] = XYList
		if ((finger_P1 % 2) == 1):
		    self._DesignParameter['M1V1M2_P1_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P1_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P1_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P1_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_P) / 2) + 131))
		    for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P1_drain']['_XYCoordinates'] = XYList
		if ((finger_P1 % 2) == 0):
		    self._DesignParameter['M2V2M3_P1_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_P1_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M2V2M3_P1_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		    self._DesignParameter['M2V2M3_P1_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_P) / 2) + 131))
		    for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M2V2M3_P1_drain']['_XYCoordinates'] = XYList
		if ((finger_P1 % 2) == 1):
		    self._DesignParameter['M2V2M3_P1_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_P1_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M2V2M3_P1_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		    self._DesignParameter['M2V2M3_P1_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_P) / 2) + 131))
		    for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M2V2M3_P1_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['P1_N2_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=50)
		self._DesignParameter['P1_N2_path']['_XYCoordinates'] = [[[(+ self._DesignParameter['M2V2M3_P1_drain']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_P1_drain']['_XYCoordinates'][0][1])], [(self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]), self._DesignParameter['M2V2M3_P1_drain']['_XYCoordinates'][0][1]], [(self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0] + self._DesignParameter['P_Dummy0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]), self._DesignParameter['M2V2M3_N2_darin']['_XYCoordinates'][0][1]], [(+ self._DesignParameter['M2V2M3_N2_darin']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_N2_darin']['_XYCoordinates'][0][1])]]]
		if ((finger_P1 % 2) == 0):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P1_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P1_source_path']['_XYCoordinates'] = path_list
		if ((finger_P1 % 2) == 1):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P1_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P1_source_path']['_XYCoordinates'] = path_list
		if ((finger_P1 % 2) == 0):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['P1_P2_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P1_P2_gate']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['P1_P2_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P1_P2_gate']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P1_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P1_drain_path']['_XYCoordinates'] = path_list
		if ((finger_P1 % 2) == 1):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['P1_P2_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P1_P2_gate']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['P1_P2_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P1_P2_gate']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P1']['_XYCoordinates'][0][1])], self._DesignParameter['P1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P1_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P1_drain_path']['_XYCoordinates'] = path_list
		if ((((finger_N1 + finger_P2) + finger_P_Dummy1) % 2) == 1):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P5']['_XYCoordinates'][0][1])], self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P5']['_XYCoordinates'][0][1])], self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P5_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P5_source_path']['_XYCoordinates'] = path_list
		if ((((finger_N1 + finger_P2) + finger_P_Dummy1) % 2) == 0):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P5']['_XYCoordinates'][0][1])], self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P5']['_XYCoordinates'][0][1])], self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P5_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P5_source_path']['_XYCoordinates'] = path_list
		if ((((finger_N1 + finger_P2) + finger_P_Dummy1) % 2) == 1):
		    self._DesignParameter['M1V1M2_P5_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P5_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P5_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P5']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'] = XYList
		if ((((finger_N1 + finger_P2) + finger_P_Dummy1) % 2) == 0):
		    self._DesignParameter['M1V1M2_P5_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P5_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P5_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P5']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['P5_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['P5_drain_path']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['P5_M2V2M3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='P5_M2V2M3In{}'.format(_Name)))[0]
		self._DesignParameter['P5_M2V2M3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['P5_M2V2M3']['_XYCoordinates'] = [[(+ self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['M1V1M2_P5_drain']['_XYCoordinates'][(- 1)][1])]]
		if ((((finger_N2 + finger_N_Dummy1) % 2) == 0) and ((finger_N4 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, ((W_N / 2) - 9))
		    if (len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N4_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N4_source_path']['_XYCoordinates'] = path_list
		if ((((finger_N2 + finger_N_Dummy1) % 2) == 0) and ((finger_N4 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, ((W_N / 2) - 9))
		    if (len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N4_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N4_source_path']['_XYCoordinates'] = path_list
		if ((((finger_N2 + finger_N_Dummy1) % 2) == 1) and ((finger_N4 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, ((W_N / 2) - 9))
		    if (len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N4_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N4_source_path']['_XYCoordinates'] = path_list
		if ((((finger_N2 + finger_N_Dummy1) % 2) == 1) and ((finger_N4 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, ((W_N / 2) - 9))
		    if (len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N4_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N4_source_path']['_XYCoordinates'] = path_list
		if ((((finger_N2 + finger_N_Dummy1) % 2) == 0) and ((finger_N4 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, (((- W_N) / 2) + 9))
		    if (len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_N4']['_YWidth'] / 2)))]][0][1]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_N4']['_YWidth'] / 2)))]][0][0]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N4_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N4_drain_path']['_XYCoordinates'] = path_list
		if ((((finger_N2 + finger_N_Dummy1) % 2) == 0) and ((finger_N4 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, (((- W_N) / 2) + 9))
		    if (len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_N4']['_YWidth'] / 2)))]][0][1]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_N4']['_YWidth'] / 2)))]][0][0]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N4_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N4_drain_path']['_XYCoordinates'] = path_list
		if ((((finger_N2 + finger_N_Dummy1) % 2) == 1) and ((finger_N4 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, (((- W_N) / 2) + 9))
		    if (len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_N4']['_YWidth'] / 2)))]][0][1]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_N4']['_YWidth'] / 2)))]][0][0]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N4_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N4_drain_path']['_XYCoordinates'] = path_list
		if ((((finger_N2 + finger_N_Dummy1) % 2) == 1) and ((finger_N4 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, (((- W_N) / 2) + 9))
		    if (len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_N4']['_YWidth'] / 2)))]][0][1]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_N4']['_YWidth'] / 2)))]][0][0]
		        for i in range(len(self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N4']['_XYCoordinates'][0][1])], self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N4_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N4_drain_path']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL1_boundary_N4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['METAL1_boundary_N4']['_XYCoordinates'] = [[[min((self._DesignParameter['N4_drain_path']['_XYCoordinates'][0][0][0] - 25), (((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + 85)), (((self._DesignParameter['N4']['_XYCoordinates'][0][1] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)], [max((self._DesignParameter['N4_drain_path']['_XYCoordinates'][(- 1)][0][0] + 25), (((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - 85)), (((self._DesignParameter['N4']['_XYCoordinates'][0][1] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + 94)]]]
		if ((((finger_N1 + finger_N2) + finger_N_Dummy2) % 2) == 0):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N5']['_XYCoordinates'][0][1])], self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N5']['_XYCoordinates'][0][1])], self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N5_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N5_source_path']['_XYCoordinates'] = path_list
		if ((((finger_N1 + finger_N2) + finger_N_Dummy2) % 2) == 1):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N5']['_XYCoordinates'][0][1])], self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['N5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N5']['_XYCoordinates'][0][1])], self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['N5_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['N5_source_path']['_XYCoordinates'] = path_list
		if ((((finger_N1 + finger_N2) + finger_N_Dummy2) % 2) == 0):
		    self._DesignParameter['M1V1M2_N5_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N5_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N5_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_N) / 2) + 131))
		    for i in range(len(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N5']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'] = XYList
		if ((((finger_N1 + finger_N2) + finger_N_Dummy2) % 2) == 1):
		    self._DesignParameter['M1V1M2_N5_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_N5_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_N5_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, (((- W_N) / 2) + 131))
		    for i in range(len(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['N5']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['N5']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['N5']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['N5_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['N5_drain_path']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['N5_M2V2M3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='N5_M2V2M3In{}'.format(_Name)))[0]
		self._DesignParameter['N5_M2V2M3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['N5_M2V2M3']['_XYCoordinates'] = [[(+ self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['M1V1M2_N5_drain']['_XYCoordinates'][(- 1)][1])]]
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 1) and ((finger_P3 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P3_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P3_source_path']['_XYCoordinates'] = path_list
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 1) and ((finger_P3 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P3_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P3_source_path']['_XYCoordinates'] = path_list
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 0) and ((finger_P3 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P3_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P3_source_path']['_XYCoordinates'] = path_list
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 0) and ((finger_P3 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, (((- W_P) / 2) + 9))
		    if (len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P3_source_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P3_source_path']['_XYCoordinates'] = path_list
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 1) and ((finger_P3 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P3_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P3_drain_path']['_XYCoordinates'] = path_list
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 1) and ((finger_P3 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P3_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P3_drain_path']['_XYCoordinates'] = path_list
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 0) and ((finger_P3 % 2) == 1)):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P3_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P3_drain_path']['_XYCoordinates'] = path_list
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 0) and ((finger_P3 % 2) == 0)):
		    path_list = []
		    xy_offset = (0, ((W_P / 2) - 9))
		    if (len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = 50
		    elif (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = 50
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['P3_gate']['_XYCoordinates'][0][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['P3_drain_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['P3_drain_path']['_XYCoordinates'] = path_list
		self._DesignParameter['P3_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['P3_gate']['_XYCoordinates'] = [[[min((self._DesignParameter['P3_drain_path']['_XYCoordinates'][0][0][0] - 25), (((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + 85)), (((self._DesignParameter['P3']['_XYCoordinates'][0][1] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)], [max((self._DesignParameter['P3_drain_path']['_XYCoordinates'][(- 1)][0][0] + 25), (((self._DesignParameter['P3']['_XYCoordinates'][0][0] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - 85)), (((self._DesignParameter['P3']['_XYCoordinates'][0][1] + self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - 94)]]]
		if (((((finger_P1 + finger_P_Dummy2) + finger_P3) % 2) == 0) and ((finger_P4 % 2) == 1)):
		    self._DesignParameter['M1V1M2_P4_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P4_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P4_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'] = XYList
		if (((((finger_P1 + finger_P_Dummy2) + finger_P3) % 2) == 0) and ((finger_P4 % 2) == 0)):
		    self._DesignParameter['M1V1M2_P4_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P4_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P4_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'] = XYList
		if (((((finger_P1 + finger_P_Dummy2) + finger_P3) % 2) == 1) and ((finger_P4 % 2) == 1)):
		    self._DesignParameter['M1V1M2_P4_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P4_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P4_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'] = XYList
		if (((((finger_P1 + finger_P_Dummy2) + finger_P3) % 2) == 1) and ((finger_P4 % 2) == 0)):
		    self._DesignParameter['M1V1M2_P4_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P4_sourceIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P4_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P4']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'] = XYList
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 1) and ((finger_P3 % 2) == 1)):
		    self._DesignParameter['M1V1M2_P3_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P3_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P3_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'] = XYList
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 1) and ((finger_P3 % 2) == 0)):
		    self._DesignParameter['M1V1M2_P3_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P3_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P3_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'] = XYList
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 0) and ((finger_P3 % 2) == 1)):
		    self._DesignParameter['M1V1M2_P3_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P3_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P3_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'] = XYList
		if ((((finger_P1 + finger_P_Dummy2) % 2) == 0) and ((finger_P3 % 2) == 0)):
		    self._DesignParameter['M1V1M2_P3_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_P3_drainIn{}'.format(_Name)))[0]
		    self._DesignParameter['M1V1M2_P3_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		    self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((W_P / 2) - 131))
		    for i in range(len(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['P3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['P3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['P3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['P3_P4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['P3_P4']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_P4_source']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['M1V1M2_P3_drain']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['N5_P5_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=50)
		self._DesignParameter['N5_P5_path']['_XYCoordinates'] = [[[(+ self._DesignParameter['P5_M2V2M3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['P5_M2V2M3']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['N5_M2V2M3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['N5_M2V2M3']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['VINn'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['PCCAM1_VINn']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_VINn']['_XYCoordinates'][0][1])]], _Mag=0.3, _Angle=0, _TEXT='VINn')
		self._DesignParameter['VINp'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['PCCAM1_VINp']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_VINp']['_XYCoordinates'][0][1])]], _Mag=0.3, _Angle=0, _TEXT='VINp')
		self._DesignParameter['VOUT'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['N5_P5_path']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['N5_P5_path']['_XYCoordinates'][0][0][1])]], _Mag=0.3, _Angle=0, _TEXT='VOUT')
		self._DesignParameter['VDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][0] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_left']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['P_guad']['_XYCoordinates'][0][1] + self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['od_left']['_XYCoordinates'][0][1]))]], _Mag=0.3, _Angle=0, _TEXT='VDD')
		self._DesignParameter['VSS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['od_left']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['od_left']['_XYCoordinates'][0][1]))]], _Mag=0.3, _Angle=0, _TEXT='VSS')
		self._DesignParameter['res_compensation'] = self._SrefElementDeclaration(_DesignObj=opppcres_b_v2._Opppcres(_Name='res_compensationIn{}'.format(_Name)))[0]
		self._DesignParameter['res_compensation']['_DesignObj']._CalculateOpppcresDesignParameter(**dict(_ResWidth=res_compensation_W, _ResLength=res_compensation_L, _CONUMX=None, _CONUMY=1, _SeriesStripes=res_compensation_series, _ParallelStripes=1))
		self._DesignParameter['res_compensation']['_XYCoordinates'] = [[(((((self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]) - (self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth'] / 2)) - (Guad_W / 2)) - 250) + ((res_compensation_series - 1) * ((res_compensation_W / 2) + 57))), (self._DesignParameter['N1']['_XYCoordinates'][0][1] - ((((Guad_W + 200) + 250) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] / 2)))]]
		self._DesignParameter['ncap'] = self._SrefElementDeclaration(_DesignObj=NCAP._NCap(_Name='ncapIn{}'.format(_Name)))[0]
		self._DesignParameter['ncap']['_DesignObj']._CalculateNCapDesignParameter(**dict(_XWidth=L_cap, _YWidth=W_cap, _NumofGates=NumofGate_res_com, NumOfCOX=None, NumOfCOY=None, Guardring=False, guardring_height=None, guardring_width=None, guardring_right=2, guardring_left=2, guardring_top=2, guardring_bot=2, _NumofOD=NumofRX_res_com, _ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['ncap']['_XYCoordinates'] = [[(((((self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_left']['_XYCoordinates'][0][0]) + (self._DesignParameter['N_guad']['_XYCoordinates'][0][0] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_right']['_XYCoordinates'][0][0])) - self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth']) - 500) / 2), (- ((((Guad_W + 200) + 250) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['ncap']['_DesignObj']._DesignParameter['NCAPLayer']['_YWidth'] / 2)))]]
		self._DesignParameter['Psubring_bottom'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='Psubring_bottomIn{}'.format(_Name)))[0]
		self._DesignParameter['Psubring_bottom']['_DesignObj']._CalculateDesignParameter(**dict(height=(((self._DesignParameter['N_guad']['_XYCoordinates'][0][1] + self._DesignParameter['N_guad']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]) + max(((((Guad_W + 200) + 250) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['ncap']['_DesignObj']._DesignParameter['NCAPLayer']['_YWidth'] / 2)), ((((Guad_W + 200) + 250) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] / 2)))) * 2), width=(((((self._DesignParameter['N5']['_XYCoordinates'][0][0] + self._DesignParameter['N5']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + (self._DesignParameter['N5']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['N4']['_XYCoordinates'][0][0] + self._DesignParameter['N4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['N4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + 400) + Guad_W), contact_bottom=Guad_via, contact_top=Guad_via, contact_left=Guad_via, contact_right=Guad_via))
		self._DesignParameter['Psubring_bottom']['_XYCoordinates'] = [[self._DesignParameter['N1']['_XYCoordinates'][0][0], min((self._DesignParameter['N1']['_XYCoordinates'][0][1] - ((((Guad_W + 200) + 250) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['ncap']['_DesignObj']._DesignParameter['NCAPLayer']['_YWidth'] / 2))), ((self._DesignParameter['N1']['_XYCoordinates'][0][1] - self._DesignParameter['N1']['_XYCoordinates'][0][1]) - ((((Guad_W + 200) + 250) + (self._DesignParameter['N1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] / 2))))]]
		self._DesignParameter['res_compensation']['_Reflect'] = [1, 0, 0]
		self._DesignParameter['res_compensation']['_Angle'] = 180
		self._DesignParameter['N5_P5_res'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=200)
		self._DesignParameter['N5_P5_res']['_XYCoordinates'] = [[[(+ self._DesignParameter['P5_M2V2M3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['P5_M2V2M3']['_XYCoordinates'][0][1])], [self._DesignParameter['P5_M2V2M3']['_XYCoordinates'][0][0], ((self._DesignParameter['res_compensation']['_XYCoordinates'][0][1] + self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]) - 25)]]]
		self._DesignParameter['M1V1M2res_com_in'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2res_com_inIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2res_com_in']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((res_compensation_W - 36) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2res_com_in']['_XYCoordinates'] = [[(+ (self._DesignParameter['res_compensation']['_XYCoordinates'][0][0] + self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0])), (+ (self._DesignParameter['res_compensation']['_XYCoordinates'][0][1] + self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]))]]
		self._DesignParameter['M2V2M3res_com_in'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3res_com_inIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3res_com_in']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int(((((res_compensation_W - 36) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3res_com_in']['_XYCoordinates'] = [[(+ (self._DesignParameter['res_compensation']['_XYCoordinates'][0][0] + self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0])), (+ (self._DesignParameter['res_compensation']['_XYCoordinates'][0][1] + self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]))]]
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'])):
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['ncap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['ncap']['_XYCoordinates'][0][1])], self._DesignParameter['ncap']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['cap_horizonta'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=(242 + L_cap), _YWidth=(W_cap / 2))
		self._DesignParameter['cap_horizonta']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'])):
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['ncap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['ncap']['_XYCoordinates'][0][1])], self._DesignParameter['ncap']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['cap_M1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(L_cap / 2), _YWidth=(220 + W_cap))
		self._DesignParameter['cap_M1']['_XYCoordinates'] = XYList
		self._DesignParameter['M1V1M2_cap_side'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_cap_sideIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_cap_side']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOY=max(1, (1 + int(((((W_cap / 2) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOX=1))
		self._DesignParameter['M1V1M2_cap_side']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1V']['_XYCoordinates'])):
		    xy = (self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1V']['_XYCoordinates'][i][0] if (type(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1V']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1V']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['ncap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['ncap']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['M1V1M2_cap_side']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'])):
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['ncap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['ncap']['_XYCoordinates'][0][1])], self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['cap_M1_UD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(242 + L_cap), _YWidth=50)
		self._DesignParameter['cap_M1_UD']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1V']['_XYCoordinates'])):
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['ncap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['ncap']['_XYCoordinates'][0][1])], self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1V']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['cap_M2_side'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=82, _YWidth=(220 + W_cap))
		self._DesignParameter['cap_M2_side']['_XYCoordinates'] = XYList
		self._DesignParameter['N3_cap_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=200)
		self._DesignParameter['N3_cap_path']['_XYCoordinates'] = [[[(self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'][0][0] + 75), (self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'][0][1] + 25)], [(self._DesignParameter['M2V2M3_N3_drain']['_XYCoordinates'][0][0] + 75), ((((self._DesignParameter['ncap']['_XYCoordinates'][0][1] + self._DesignParameter['ncap']['_DesignObj']._DesignParameter['NWELL']['_XYCoordinates'][0][1]) + (self._DesignParameter['ncap']['_DesignObj']._DesignParameter['NWELL']['_YWidth'] / 2)) - 390) - 25)]]]
		self._DesignParameter['M1V1M2_cap_N3'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_cap_N3In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_cap_N3']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int((((self._DesignParameter['cap_M1']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_cap_N3']['_XYCoordinates'] = [[(+ (self._DesignParameter['ncap']['_XYCoordinates'][0][0] + self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][(((2 * NumofGate_res_com) * NumofRX_res_com) - 1)][0])), (+ (self._DesignParameter['ncap']['_XYCoordinates'][0][1] + self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][(((2 * NumofGate_res_com) * NumofRX_res_com) - 1)][1]))]]
		self._DesignParameter['M2V2M3_cap_N3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_cap_N3In{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_cap_N3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int((((self._DesignParameter['cap_M1']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_cap_N3']['_XYCoordinates'] = [[(+ (self._DesignParameter['ncap']['_XYCoordinates'][0][0] + self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][(((2 * NumofGate_res_com) * NumofRX_res_com) - 1)][0])), (+ (self._DesignParameter['ncap']['_XYCoordinates'][0][1] + self._DesignParameter['ncap']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][(((2 * NumofGate_res_com) * NumofRX_res_com) - 1)][1]))]]
		self._DesignParameter['N2_cap_path2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=50)
		self._DesignParameter['N2_cap_path2']['_XYCoordinates'] = [[[(+ self._DesignParameter['M2V2M3_cap_N3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_cap_N3']['_XYCoordinates'][0][1])], [(self._DesignParameter['N3_cap_path']['_XYCoordinates'][0][0][0] - 100), self._DesignParameter['M2V2M3_cap_N3']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['M1V1M2_cap_res'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_cap_resIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_cap_res']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((res_compensation_W - 36) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_cap_res']['_XYCoordinates'] = [[((self._DesignParameter['res_compensation']['_XYCoordinates'][0][0] + self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][((2 * res_compensation_series) - 1)][0]) - ((2 * (res_compensation_series - 1)) * (114 + res_compensation_W))), (self._DesignParameter['res_compensation']['_XYCoordinates'][0][1] + self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][((2 * res_compensation_series) - (1 + (res_compensation_series % 2)))][1])]]
		self._DesignParameter['res_cap_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['res_cap_path']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_cap_res']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_cap_res']['_XYCoordinates'][0][1])], [(((self._DesignParameter['ncap']['_XYCoordinates'][0][0] + self._DesignParameter['ncap']['_DesignObj']._DesignParameter['NWELL']['_XYCoordinates'][0][0]) + (self._DesignParameter['ncap']['_DesignObj']._DesignParameter['NWELL']['_XWidth'] / 2)) - 461), self._DesignParameter['M1V1M2_cap_res']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['res_cap_path2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=82)
		self._DesignParameter['res_cap_path2']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_cap_side']['_XYCoordinates'][(((2 * NumofGate_res_com) * NumofRX_res_com) - 1)][0]), (+ self._DesignParameter['M1V1M2_cap_side']['_XYCoordinates'][(((2 * NumofGate_res_com) * NumofRX_res_com) - 1)][1])], [self._DesignParameter['M1V1M2_cap_side']['_XYCoordinates'][(((2 * NumofGate_res_com) * NumofRX_res_com) - 1)][0], (self._DesignParameter['res_cap_path']['_XYCoordinates'][0][0][1] + 25)]]]
		self._DesignParameter['N_guad_res_compensation'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='N_guad_res_compensationIn{}'.format(_Name)))[0]
		self._DesignParameter['N_guad_res_compensation']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=Guad_via, _NumberOfPbodyCOY=max(1, (1 + int((((self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _Met1XWidth=None, _Met1YWidth=((self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_top']['_XYCoordinates'][0][1]) - (self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1]))))
		self._DesignParameter['N_guad_res_compensation']['_XYCoordinates'] = [[((((self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][0] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_right']['_XYCoordinates'][0][0]) - self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth']) - 500) - Guad_W), (self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_right']['_XYCoordinates'][0][1])]]
		self._DesignParameter['N_guad_res_compensation_BP'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(Guad_W + 42), _YWidth=((self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_top']['_XYCoordinates'][0][1]) - (self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1])))
		self._DesignParameter['N_guad_res_compensation_BP']['_XYCoordinates'] = [[((((self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][0] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_right']['_XYCoordinates'][0][0]) - self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth']) - 500) - Guad_W), (self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_right']['_XYCoordinates'][0][1])]]
		self._DesignParameter['N_guad_res_compensation_RX'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=Guad_W, _YWidth=((self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_top']['_XYCoordinates'][0][1]) - (self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates'][0][1])))
		self._DesignParameter['N_guad_res_compensation_RX']['_XYCoordinates'] = [[((((self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][0] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_right']['_XYCoordinates'][0][0]) - self._DesignParameter['res_compensation']['_DesignObj']._DesignParameter['_PRESLayer']['_XWidth']) - 500) - Guad_W), (self._DesignParameter['Psubring_bottom']['_XYCoordinates'][0][1] + self._DesignParameter['Psubring_bottom']['_DesignObj']._DesignParameter['pw_right']['_XYCoordinates'][0][1])]]
		self._DesignParameter['NW_amp'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['nw_bot']['_XWidth'], _YWidth=self._DesignParameter['P_guad']['_DesignObj']._DesignParameter['nw_left']['_YWidth'])
		self._DesignParameter['NW_amp']['_XYCoordinates'] = [[(+ self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1])]]
		self._DesignParameter['BP_amp'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(((self._DesignParameter['P5']['_XYCoordinates'][0][0] + self._DesignParameter['P5']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['P5']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - ((self._DesignParameter['P4']['_XYCoordinates'][0][0] + self._DesignParameter['P4']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['P4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['P4']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'])
		self._DesignParameter['BP_amp']['_XYCoordinates'] = [[(+ self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['P_Dummy0']['_XYCoordinates'][0][1])]]
		self._DesignParameter['res_path2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=50)
		self._DesignParameter['res_path2']['_XYCoordinates'] = [[[(+ self._DesignParameter['M2V2M3res_com_in']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3res_com_in']['_XYCoordinates'][0][1])], [self._DesignParameter['N5_P5_res']['_XYCoordinates'][0][0][0], self._DesignParameter['M2V2M3res_com_in']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['N4_path2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['N4_path2']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_N4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_N4']['_XYCoordinates'][0][1])], [self._DesignParameter['N4_P4_path']['_XYCoordinates'][0][0][0], self._DesignParameter['M1V1M2_N4']['_XYCoordinates'][0][1]]]]
		