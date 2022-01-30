from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1

class TG_2X_CRIT_SLVT_v1(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='TG_2X_CRIT_SLVT_v1'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,nmos_gate=1,pmos_gate=1,nmos_width=200,pmos_width=400,length=30,XVT='SLVT',nmos_y=410,pmos_y=390,vss2vdd_height=1800,gate_spacing=100):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		None