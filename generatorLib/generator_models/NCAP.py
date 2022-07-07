from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import PSubRing

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self, length=2500, width=1000, Xnum=1, Ynum=4, Guardring=True, guardring_height=None, guardring_width=None, guardring_right=2, guardring_left=2, guardring_top=2, guardring_bot=2):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		_OriginXY=[[0,0]]

		self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=Xnum, _NMOSChannelWidth=width, _NMOSChannellength=length, _NMOSDummy=False, _GateSpacing=drc._PolygateSpace_ncap, _SDWidth=drc._Metal1MinSpace21, _XVT='LVT', _PCCrit=False))
		#self._DesignParameter['nmos']['_XYCoordinates'] = _OriginXY

		########## To erase XVT Layer(LVT is set temporarily) ##########
		_XVTLayer='_LVTLayer'
		self._DesignParameter['nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']=0
		self._DesignParameter['nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']=0

		Ydistance_od=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']+drc._OdSpace_ncap
		tmp=[]
		for i in range(0, Ynum):
			tmp.append([_OriginXY[0][0], _OriginXY[0][1] - (Ynum-1)/2*Ydistance_od+i*Ydistance_od])

		self._DesignParameter['nmos']['_XYCoordinates'] = tmp
		del tmp

		CoX=int((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']-2*drc._Metal1MinEnclosureCO2)/(drc._CoMinSpace+drc._CoMinWidth))

		self._DesignParameter['via_poly_m1']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1In{}'.format(_Name)))[0]
		self._DesignParameter['via_poly_m1']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**dict(_ViaPoly2Met1NumberOfCOX=CoX, _ViaPoly2Met1NumberOfCOY=1))

		del CoX

		tmp=[]
		for j in range(0, Ynum+1):
			for i in range(0, Xnum):
				tmp.append([self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _OriginXY[0][1]-Ynum/2*Ydistance_od+Ydistance_od*j])

		self._DesignParameter['via_poly_m1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['poly']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'])

		tmp=[]
		for i in range(0, Xnum):
			tmp.append([[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['via_poly_m1']['_XYCoordinates'][0][1]-self._DesignParameter['via_poly_m1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2], \
						[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['via_poly_m1']['_XYCoordinates'][-1][1]+self._DesignParameter['via_poly_m1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2]])

		self._DesignParameter['poly']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['NWELL']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']+2*drc._PolygateMinEnclosureByNcap, _YWidth=self._DesignParameter['nmos']['_XYCoordinates'][-1][1]-self._DesignParameter['nmos']['_XYCoordinates'][0][1]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']+2*drc._PolygateMinEnclosureByNcap)
		self._DesignParameter['NWELL']['_XYCoordinates']=_OriginXY

		self._DesignParameter['NCAPLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NCAP'][0], _Datatype=DesignParameters._LayerMapping['NCAP'][1], _XWidth=self._DesignParameter['NWELL']['_XWidth'], _YWidth=self._DesignParameter['NWELL']['_YWidth'])
		self._DesignParameter['NCAPLayer']['_XYCoordinates']=_OriginXY

		if Guardring == True :
			self._DesignParameter['guardring']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='PSubRingIn{}'.format(_Name)))[0]
			self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=3000, contact_bottom=guardring_left, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))

			if guardring_width == None :
				guardring_Xwidth=self._DesignParameter['NWELL']['_XWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+2*drc._NwMinSpacetoRX

			elif guardring_width != None :
				guardring_Xwidth=guardring_width

			if guardring_height == None :
				guardring_Yheight=self._DesignParameter['NWELL']['_YWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+2*drc._NwMinSpacetoRX

			elif guardring_height != None :
				guardring_Yheight=guardring_height

			self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=guardring_Yheight, width=guardring_Xwidth, contact_bottom=guardring_left, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
			self._DesignParameter['guardring']['_XYCoordinates']=_OriginXY