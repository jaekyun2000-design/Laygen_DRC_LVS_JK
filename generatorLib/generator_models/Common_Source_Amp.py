# from generatorLib import StickDiagram
# from generatorLib import DesignParameters
# import copy
# import math
# from generatorLib import DRC
# from generatorLib.generator_models import NMOSWithDummy
# from generatorLib.generator_models import ViaPoly2Met1
# from generatorLib.generator_models import ViaMet12Met2
# from generatorLib.generator_models import ViaMet22Met3
# from generatorLib.generator_models import ViaMet32Met4
# from generatorLib.generator_models import PSubRing
#
#
# class _Common_Source_Amp(StickDiagram._StickDiagram):
# 	def __init__(self, _DesignParameter=None, _Name='Common_Source_Amp'):
# 		super().__init__()
# 		if _DesignParameter != None:
# 			self._DesignParameter = _DesignParameter
# 		else:
# 			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
# 		self._DesignParameter['_Name']['Name'] = _Name
#
# 	def _CalculateDesignParameter(self, nmos_param={'_NMOSNumberofGate':2, '_NMOSChannelWidth':2000, '_NMOSChannellength':30, '_NMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
# 										R_drain={'_ResWidth':None, '_ResLength':None, '_CONUMX':None, '_CONUMY':None}, \
# 										R_feedback={'_ResWidth':None, '_ResLength':None, '_CONUMX':None, '_CONUMY':None}) :
# 		drc = DRC.DRC()
# 		_Name = self._DesignParameter['_Name']['_Name']
# 		MinSnapSpacing=drc._MinSnapSpacing