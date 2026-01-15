from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import user_define_exceptions


from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

import ftplib

class _PSubring(StickDiagram._StickDiagram):
	_ParametersForDesignCalculation= dict(_PType = True, _XWidth = None, _YWidth = None, _Width = None)
	def __init__(self, _DesignParameter=None, _Name=None):

		if _DesignParameter!=None:
			self._DesignParameter=_DesignParameter
		else :
			self._DesignParameter = dict(
				_ODLayerx=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
				_ODLayery=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1],_XYCoordinates=[], _XWidth=400, _YWidth=400),
				_Met1Layerx=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
				_Met1Layery=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1],_XYCoordinates=[], _XWidth=400, _YWidth=400),
				_PPLayer = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[],_Width=100),
				_NPLayer = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1],_XYCoordinates=[],_Width=100),
				_COLayer = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
				_NWLayer = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=400),
				_Name = self._NameDeclaration(_Name=_Name), _GDSFile = self._GDSObjDeclaration(_GDSFile=None),
				_XYcoordAsCent=dict(_XYcoordAsCent=1),
			)



		if _Name != None:
			self._DesignParameter['_Name']['_Name']=_Name

	def _CalculatePSubring(self, _PType = True, _XWidth = None, _YWidth = None, _Width = None):
		print ('#########################################################################################################')
		print ('                                    {}  PSubring Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
		print ('#########################################################################################################')
		_DRCObj = DRC.DRC()
		_XYCoordinateOfPSubring = [[0, 0]]
		_MinSnapSpacing = _DRCObj._MinSnapSpacing

		#if DesignParameters._Technology != '028nm' :
		if _XWidth % (2 * _MinSnapSpacing) != 0 or _YWidth % (2 * _MinSnapSpacing) != 0 or _Width % (2 * _MinSnapSpacing) != 0 :
			_XWidth = self.CeilMinSnapSpacing(_XWidth, 2 * _MinSnapSpacing)
			_YWidth = self.CeilMinSnapSpacing(_YWidth, 2 * _MinSnapSpacing)
			_Width = self.CeilMinSnapSpacing(_Width, 2 * _MinSnapSpacing)

		if _XWidth == None or _YWidth == None or _Width < _DRCObj._MetalxMinWidth :
			raise NotImplementedError

		print ('#############################     METAL1 Layer Calcuation    ############################################')
		if _XWidth % 2 == 0 and _YWidth % 2 == 0 and _Width % 2 == 0:
			self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
			self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
			self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + _YWidth / 2 + _Width / 2],
																	   [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - _YWidth / 2 - _Width / 2 ]]
			self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
			self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
			self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - _XWidth / 2 - _Width / 2,
																		   _XYCoordinateOfPSubring[0][1]],
																		  [_XYCoordinateOfPSubring[0][0] + _XWidth / 2  + _Width / 2 ,
																		   _XYCoordinateOfPSubring[0][1]]]
		if _XWidth % 2 == 0 and _YWidth % 2 == 0 and _Width % 2 == 1:
			self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * (_Width + 1)
			self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width + 1
			self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + _YWidth / 2 + _Width / 2],
																	   [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - _YWidth / 2 - _Width / 2 ]]
			self._DesignParameter['_Met1Layery']['_XWidth'] = _Width + 1
			self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * (_Width + 1)
			self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - _XWidth / 2 - _Width / 2,
																		   _XYCoordinateOfPSubring[0][1]],
																		  [_XYCoordinateOfPSubring[0][0] + _XWidth / 2  + _Width / 2 ,
																		   _XYCoordinateOfPSubring[0][1]]]
		if _XWidth % 2 == 0 and _YWidth % 2 == 1 and _Width % 2 == 0:
			self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * (_Width)
			self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
			self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + (_YWidth + 1) / 2 + _Width / 2],
																	   [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - (_YWidth + 1) / 2 - _Width / 2 ]]
			self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
			self._DesignParameter['_Met1Layery']['_YWidth'] = (_YWidth + 1) + 2 * (_Width)
			self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - _XWidth / 2 - _Width / 2,
																		   _XYCoordinateOfPSubring[0][1]],
																		  [_XYCoordinateOfPSubring[0][0] + _XWidth / 2  + _Width / 2 ,
																		   _XYCoordinateOfPSubring[0][1]]]
		if _XWidth % 2 == 0 and _YWidth % 2 == 1 and _Width % 2 == 1:
			self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * (_Width + 1)
			self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width + 1
			self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + (_YWidth + 1) / 2 + (_Width + 1) / 2],
																	   [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - (_YWidth + 1) / 2 - (_Width + 1) / 2 ]]
			self._DesignParameter['_Met1Layery']['_XWidth'] = _Width + 1
			self._DesignParameter['_Met1Layery']['_YWidth'] = (_YWidth + 1) + 2 * (_Width + 1)
			self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - _XWidth / 2 - (_Width + 1) / 2,
																		   _XYCoordinateOfPSubring[0][1]],
																		  [_XYCoordinateOfPSubring[0][0] + _XWidth / 2  + (_Width + 1) / 2 ,
																		   _XYCoordinateOfPSubring[0][1]]]
		if _XWidth % 2 == 1 and _YWidth % 2 == 0 and _Width % 2 == 0:
			self._DesignParameter['_Met1Layerx']['_XWidth'] = (_XWidth+1) + 2 * _Width
			self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
			self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + _YWidth // 2 + _Width // 2],
																	   [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - _YWidth // 2 - _Width // 2 ]]
			self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
			self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
			self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - (_XWidth+1) // 2 - _Width // 2,
																		   _XYCoordinateOfPSubring[0][1]],
																		  [_XYCoordinateOfPSubring[0][0] + (_XWidth+1) // 2  + _Width // 2 ,
																		   _XYCoordinateOfPSubring[0][1]]]

		if _XWidth % 2 == 1 and _YWidth % 2 == 0 and _Width % 2 == 1:
			self._DesignParameter['_Met1Layerx']['_XWidth'] = (_XWidth+1) + 2 * (_Width + 1)
			self._DesignParameter['_Met1Layerx']['_YWidth'] = (_Width + 1)
			self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + _YWidth // 2 + (_Width + 1) // 2],
																	   [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - _YWidth // 2 - (_Width + 1) // 2 ]]
			self._DesignParameter['_Met1Layery']['_XWidth'] = (_Width + 1)
			self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * (_Width + 1)
			self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - (_XWidth+1) // 2 - (_Width + 1) // 2,
																		   _XYCoordinateOfPSubring[0][1]],
																		  [_XYCoordinateOfPSubring[0][0] + (_XWidth+1) // 2  + (_Width + 1) // 2 ,
																		   _XYCoordinateOfPSubring[0][1]]]

		if _XWidth % 2 == 1 and _YWidth % 2 == 1 and _Width % 2 == 0:
			self._DesignParameter['_Met1Layerx']['_XWidth'] = (_XWidth+1) + 2 * _Width
			self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
			self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + (_YWidth + 1) // 2 + _Width // 2],
																	   [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - (_YWidth + 1) // 2 - _Width // 2 ]]
			self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
			self._DesignParameter['_Met1Layery']['_YWidth'] = (_YWidth + 1) + 2 * _Width
			self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - (_XWidth+1) // 2 - _Width // 2,
																		   _XYCoordinateOfPSubring[0][1]],
																		  [_XYCoordinateOfPSubring[0][0] + (_XWidth+1) // 2  + _Width // 2 ,
																		   _XYCoordinateOfPSubring[0][1]]]

		if _XWidth % 2 == 1 and _YWidth % 2 == 1 and _Width % 2 == 1:
			self._DesignParameter['_Met1Layerx']['_XWidth'] = (_XWidth+1) + 2 * (_Width + 1)
			self._DesignParameter['_Met1Layerx']['_YWidth'] = (_Width + 1)
			self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + (_YWidth + 1) // 2 + (_Width + 1) // 2],
																	   [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - (_YWidth + 1) // 2 - (_Width + 1) // 2 ]]
			self._DesignParameter['_Met1Layery']['_XWidth'] = (_Width + 1)
			self._DesignParameter['_Met1Layery']['_YWidth'] = (_YWidth + 1) + 2 * (_Width + 1)
			self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - (_XWidth+1) // 2 - (_Width + 1) // 2,
																		   _XYCoordinateOfPSubring[0][1]],
																		  [_XYCoordinateOfPSubring[0][0] + (_XWidth+1) // 2  + (_Width + 1) // 2 ,
																		   _XYCoordinateOfPSubring[0][1]]]

		# if _XWidth % 2 == 0 and _YWidth % 2 == 0 and _Width % 2 == 0 :
		#     self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(_YWidth / 2 + 0.5) + int(_Width / 2 + 0.5)],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(_YWidth / 2 + 0.5) - int(_Width / 2 + 0.5)]]
		#     self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5),
		#                                                                _XYCoordinateOfPSubring[0][1]],
		#                                                               [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5),
		#                                                                _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 0 and _YWidth % 2 == 0 and _Width % 2 == 1 :
		#     self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(_YWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(_YWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1]]
		#     self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1,
		#                                                                _XYCoordinateOfPSubring[0][1]],
		#                                                               [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#                                                                _XYCoordinateOfPSubring[0][1]]]
		#
		#
		# if _XWidth % 2 == 0 and _YWidth % 2 == 1 and _Width % 2 == 0 :
		#     self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int((_YWidth) / 2 + 0.5) + int(_Width / 2 + 0.5)],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int((_YWidth) / 2 + 0.5) - int(_Width / 2 + 0.5)]]
		#     self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5),
		#                                                                _XYCoordinateOfPSubring[0][1]],
		#                                                                 [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5),
		#                                                                 _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 0 and _YWidth % 2 == 1 and _Width % 2 == 1:
		#     self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 2]]
		#     self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1,
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 1 and _YWidth % 2 == 0 and _Width % 2 == 0:
		#     self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5)],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5)]]
		#     self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5),
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 1 and _YWidth % 2 == 0 and _Width % 2 == 1:
		#     self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5) + 1],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 1]]
		#     self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1,
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 2,
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 1 and _YWidth % 2 == 1 and _Width % 2 == 0:
		#     self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5)],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 1]]
		#     self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5),
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1]]]
		#     self._DesignParameter['_Met1Layery2']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery2']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layery2']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1] - int(_YWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1]]
		#
		# if _XWidth % 2 == 1 and _YWidth % 2 == 1 and _Width % 2 == 1:
		#     self._DesignParameter['_Met1Layerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layerx']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5) + 1],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 2]]
		#     self._DesignParameter['_Met1Layery']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_Met1Layery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1,
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 2,
		#          _XYCoordinateOfPSubring[0][1]]]
		#     self._DesignParameter['_Met1Layery2']['_XWidth'] = _Width
		#     self._DesignParameter['_Met1Layery2']['_YWidth'] = _Width
		#     self._DesignParameter['_Met1Layery2']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 2,
		#                                                                 _XYCoordinateOfPSubring[0][1] - int(_YWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 2]]

		print ('###############################     DIFF Layer Calcuation     ############################################')

		if _XWidth % 2 == 0 and _YWidth % 2 == 0 and _Width % 2 == 0:
			self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
			self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
			self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][
																		   1] + _YWidth // 2 + _Width // 2],
																	  [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][
																		   1] - _YWidth // 2 - _Width // 2]]
			self._DesignParameter['_ODLayery']['_XWidth'] = _Width
			self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
			self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
				[_XYCoordinateOfPSubring[0][0] - _XWidth // 2 - _Width // 2,
				 _XYCoordinateOfPSubring[0][1]],
				[_XYCoordinateOfPSubring[0][0] + _XWidth // 2 + _Width // 2,
				 _XYCoordinateOfPSubring[0][1]]]
		if _XWidth % 2 == 0 and _YWidth % 2 == 0 and _Width % 2 == 1:
			self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * (_Width + 1)
			self._DesignParameter['_ODLayerx']['_YWidth'] = _Width + 1
			self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][
																		   1] + _YWidth // 2 + _Width // 2],
																	  [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][
																		   1] - _YWidth // 2 - _Width // 2]]
			self._DesignParameter['_ODLayery']['_XWidth'] = _Width + 1
			self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * (_Width + 1)
			self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
				[_XYCoordinateOfPSubring[0][0] - _XWidth // 2 - _Width // 2,
				 _XYCoordinateOfPSubring[0][1]],
				[_XYCoordinateOfPSubring[0][0] + _XWidth // 2 + _Width // 2,
				 _XYCoordinateOfPSubring[0][1]]]
		if _XWidth % 2 == 0 and _YWidth % 2 == 1 and _Width % 2 == 0:
			self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * (_Width)
			self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
			self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + (
																				   _YWidth + 1) // 2 + _Width // 2],
																	  [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - (
																				   _YWidth + 1) // 2 - _Width // 2]]
			self._DesignParameter['_ODLayery']['_XWidth'] = _Width
			self._DesignParameter['_ODLayery']['_YWidth'] = (_YWidth + 1) + 2 * (_Width)
			self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
				[_XYCoordinateOfPSubring[0][0] - _XWidth // 2 - _Width // 2,
				 _XYCoordinateOfPSubring[0][1]],
				[_XYCoordinateOfPSubring[0][0] + _XWidth // 2 + _Width // 2,
				 _XYCoordinateOfPSubring[0][1]]]
		if _XWidth % 2 == 0 and _YWidth % 2 == 1 and _Width % 2 == 1:
			self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * (_Width + 1)
			self._DesignParameter['_ODLayerx']['_YWidth'] = _Width + 1
			self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + (
																				   _YWidth + 1) // 2 + (
																				   _Width + 1) // 2],
																	  [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - (
																				   _YWidth + 1) // 2 - (
																				   _Width + 1) // 2]]
			self._DesignParameter['_ODLayery']['_XWidth'] = _Width + 1
			self._DesignParameter['_ODLayery']['_YWidth'] = (_YWidth + 1) + 2 * (_Width + 1)
			self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
				[_XYCoordinateOfPSubring[0][0] - _XWidth // 2 - (_Width + 1) // 2,
				 _XYCoordinateOfPSubring[0][1]],
				[_XYCoordinateOfPSubring[0][0] + _XWidth // 2 + (_Width + 1) // 2,
				 _XYCoordinateOfPSubring[0][1]]]
		if _XWidth % 2 == 1 and _YWidth % 2 == 0 and _Width % 2 == 0:
			self._DesignParameter['_ODLayerx']['_XWidth'] = (_XWidth + 1) + 2 * _Width
			self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
			self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][
																		   1] + _YWidth // 2 + _Width // 2],
																	  [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][
																		   1] - _YWidth // 2 - _Width // 2]]
			self._DesignParameter['_ODLayery']['_XWidth'] = _Width
			self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
			self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
				[_XYCoordinateOfPSubring[0][0] - (_XWidth + 1) // 2 - _Width // 2,
				 _XYCoordinateOfPSubring[0][1]],
				[_XYCoordinateOfPSubring[0][0] + (_XWidth + 1) // 2 + _Width // 2,
				 _XYCoordinateOfPSubring[0][1]]]

		if _XWidth % 2 == 1 and _YWidth % 2 == 0 and _Width % 2 == 1:
			self._DesignParameter['_ODLayerx']['_XWidth'] = (_XWidth + 1) + 2 * (_Width + 1)
			self._DesignParameter['_ODLayerx']['_YWidth'] = (_Width + 1)
			self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + _YWidth // 2 + (
																				   _Width + 1) // 2],
																	  [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - _YWidth // 2 - (
																				   _Width + 1) // 2]]
			self._DesignParameter['_ODLayery']['_XWidth'] = (_Width + 1)
			self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * (_Width + 1)
			self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
				[_XYCoordinateOfPSubring[0][0] - (_XWidth + 1) // 2 - (_Width + 1) // 2,
				 _XYCoordinateOfPSubring[0][1]],
				[_XYCoordinateOfPSubring[0][0] + (_XWidth + 1) // 2 + (_Width + 1) // 2,
				 _XYCoordinateOfPSubring[0][1]]]

		if _XWidth % 2 == 1 and _YWidth % 2 == 1 and _Width % 2 == 0:
			self._DesignParameter['_ODLayerx']['_XWidth'] = (_XWidth + 1) + 2 * _Width
			self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
			self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + (
																				   _YWidth + 1) // 2 + _Width // 2],
																	  [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - (
																				   _YWidth + 1) // 2 - _Width // 2]]
			self._DesignParameter['_ODLayery']['_XWidth'] = _Width
			self._DesignParameter['_ODLayery']['_YWidth'] = (_YWidth + 1) + 2 * _Width
			self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
				[_XYCoordinateOfPSubring[0][0] - (_XWidth + 1) // 2 - _Width // 2,
				 _XYCoordinateOfPSubring[0][1]],
				[_XYCoordinateOfPSubring[0][0] + (_XWidth + 1) // 2 + _Width // 2,
				 _XYCoordinateOfPSubring[0][1]]]

		if _XWidth % 2 == 1 and _YWidth % 2 == 1 and _Width % 2 == 1:
			self._DesignParameter['_ODLayerx']['_XWidth'] = (_XWidth + 1) + 2 * (_Width + 1)
			self._DesignParameter['_ODLayerx']['_YWidth'] = (_Width + 1)
			self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] + (
																				   _YWidth + 1) // 2 + (
																				   _Width + 1) // 2],
																	  [_XYCoordinateOfPSubring[0][0],
																	   _XYCoordinateOfPSubring[0][1] - (
																				   _YWidth + 1) // 2 - (
																				   _Width + 1) // 2]]
			self._DesignParameter['_ODLayery']['_XWidth'] = (_Width + 1)
			self._DesignParameter['_ODLayery']['_YWidth'] = (_YWidth + 1) + 2 * (_Width + 1)
			self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
				[_XYCoordinateOfPSubring[0][0] - (_XWidth + 1) // 2 - (_Width + 1) // 2,
				 _XYCoordinateOfPSubring[0][1]],
				[_XYCoordinateOfPSubring[0][0] + (_XWidth + 1) // 2 + (_Width + 1) // 2,
				 _XYCoordinateOfPSubring[0][1]]]
		# if _XWidth % 2 == 0 and _YWidth % 2 == 0 and _Width % 2 == 0:
		#     self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(_Width / 2 + 0.5)],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(_Width / 2 + 0.5)]]
		#     self._DesignParameter['_ODLayery']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5),
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5),
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 0 and _YWidth % 2 == 0 and _Width % 2 == 1:
		#     self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5) + 1],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 1]]
		#     self._DesignParameter['_ODLayery']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1,
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 0 and _YWidth % 2 == 1 and _Width % 2 == 0:
		#     self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(_Width / 2 + 0.5)],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5)]]
		#     self._DesignParameter['_ODLayery']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5),
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5),
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 0 and _YWidth % 2 == 1 and _Width % 2 == 1:
		#     self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5) + 1],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 2]]
		#     self._DesignParameter['_ODLayery']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1,
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 1 and _YWidth % 2 == 0 and _Width % 2 == 0:
		#     self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5)],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5)]]
		#     self._DesignParameter['_ODLayery']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5),
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 1 and _YWidth % 2 == 0 and _Width % 2 == 1:
		#     self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5) + 1],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 1]]
		#     self._DesignParameter['_ODLayery']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1,
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 2,
		#          _XYCoordinateOfPSubring[0][1]]]
		#
		# if _XWidth % 2 == 1 and _YWidth % 2 == 1 and _Width % 2 == 0:
		#     self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5)],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 1]]
		#     self._DesignParameter['_ODLayery']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5),
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1]]]
		#     self._DesignParameter['_ODLayery2']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery2']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayery2']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 1,
		#          _XYCoordinateOfPSubring[0][1] - int(_YWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1]]
		#
		# if _XWidth % 2 == 1 and _YWidth % 2 == 1 and _Width % 2 == 1:
		#     self._DesignParameter['_ODLayerx']['_XWidth'] = _XWidth + 2 * _Width
		#     self._DesignParameter['_ODLayerx']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayerx']['_XYCoordinates'] = [[_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] + int(
		#                                                                    _YWidth / 2 + 0.5) + int(
		#                                                                    _Width / 2 + 0.5) + 1],
		#                                                               [_XYCoordinateOfPSubring[0][0],
		#                                                                _XYCoordinateOfPSubring[0][1] - int(
		#                                                                    _YWidth / 2 + 0.5) - int(
		#                                                                    _Width / 2 + 0.5) - 2]]
		#     self._DesignParameter['_ODLayery']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery']['_YWidth'] = _YWidth + 2 * _Width
		#     self._DesignParameter['_ODLayery']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] - int(_XWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 1,
		#          _XYCoordinateOfPSubring[0][1]],
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 2,
		#          _XYCoordinateOfPSubring[0][1]]]
		#     self._DesignParameter['_ODLayery2']['_XWidth'] = _Width
		#     self._DesignParameter['_ODLayery2']['_YWidth'] = _Width
		#     self._DesignParameter['_ODLayery2']['_XYCoordinates'] = [
		#         [_XYCoordinateOfPSubring[0][0] + int(_XWidth / 2 + 0.5) + int(_Width / 2 + 0.5) + 2,
		#          _XYCoordinateOfPSubring[0][1] - int(_YWidth / 2 + 0.5) - int(_Width / 2 + 0.5) - 2]]


		print ('##############################     CONT Layer Calcuation    ##############################################')
		self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
		self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
		_COXNumMin1 = int((self._DesignParameter['_Met1Layerx']['_XWidth'] - _DRCObj._CoMinWidth -_DRCObj._Metal1MinEnclosureCO2 * 2 - 2 * self._DesignParameter['_Met1Layery']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
		if _COXNumMin1 == 0 :
			_COXNumMin1 = 1
		_COYNumMin1 = int((self._DesignParameter['_Met1Layerx']['_YWidth'] - _DRCObj._CoMinWidth -_DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
		if _COYNumMin1 == 0 :
			_COYNumMin1 = 1
		_COXNumMin2 = int((self._DesignParameter['_Met1Layery']['_XWidth'] - _DRCObj._CoMinWidth -_DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
		if _COXNumMin2 == 0 :
			_COXNumMin2 = 1
		_COYNumMin2 = int((self._DesignParameter['_Met1Layery']['_YWidth'] - _DRCObj._CoMinWidth - 2 * self._DesignParameter['_Met1Layerx']['_YWidth'] - _DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
		if _COYNumMin2 == 0 :
			_COYNumMin2 = 1
		tmp = []

		for i in range (0, _COXNumMin1) :
			for j in range (0,_COYNumMin1) :
				if _COXNumMin1 % 2 == 0 and _COYNumMin1 % 2 == 0 :
					tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin1 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin1 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin1 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin1 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
				elif _COXNumMin1 % 2 == 0 and _COYNumMin1 % 2 == 1 :
					tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin1 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin1 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin1 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin1 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
				elif _COXNumMin1 % 2 == 1 and _COYNumMin1 % 2 == 0 :
					tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin1 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin1 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin1 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin1 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
				else :
					tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin1 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin1 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin1 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin1 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

		for i in range (0, _COXNumMin2) :
			for j in range (0, _COYNumMin2) :
				if _COXNumMin2 % 2 == 0 and _COYNumMin2 % 2 == 0 :
					tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin2 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin2 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin2 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin2 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
				elif _COXNumMin2 % 2 == 0 and _COYNumMin2 % 2 == 1 :
					tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin2 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin2 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin2 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin2 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
				elif _COXNumMin2 % 2 == 1 and _COYNumMin2 % 2 == 0 :
					tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin2 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin2 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin2 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin2 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
				else :
					tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin2 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin2 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin2 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
								self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin2 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

		if DesignParameters._Technology != '028nm' :
			COXdistance = abs(tmp[_COXNumMin1 * 2 + 1][0] - tmp[_COXNumMin1 * 2 - 1][0] - _DRCObj._CoMinWidth)
			COYdistance = abs(tmp[_COXNumMin1 * 2 + 1][1] - tmp[_COXNumMin1 * 2 - 1][1] - _DRCObj._CoMinWidth)
			if COXdistance ** 2 + COYdistance ** 2 < _DRCObj._CoMinSpace2 ** 2 :
				_COXNumMin1 = int((self._DesignParameter['_Met1Layerx']['_XWidth'] - _DRCObj._CoMinWidth -_DRCObj._Metal1MinEnclosureCO2 * 2 - 2 * self._DesignParameter['_Met1Layery']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
				if _COXNumMin1 == 0 :
					_COXNumMin1 = 1
				_COYNumMin1 = int((self._DesignParameter['_Met1Layerx']['_YWidth'] - _DRCObj._CoMinWidth -_DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
				if _COYNumMin1 == 0 :
					_COYNumMin1 = 1
				_COXNumMin2 = int((self._DesignParameter['_Met1Layery']['_XWidth'] - _DRCObj._CoMinWidth -_DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
				if _COXNumMin2 == 0 :
					_COXNumMin2 = 1
				_COYNumMin2 = int((self._DesignParameter['_Met1Layery']['_YWidth'] - _DRCObj._CoMinWidth - 2 * self._DesignParameter['_Met1Layerx']['_YWidth'] - _DRCObj._Metal1MinEnclosureCO2 * 2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))
				if _COYNumMin2 == 0 :
					_COYNumMin2 = 1
				tmp = []

				for i in range (0, _COXNumMin1) :
					for j in range (0,_COYNumMin1) :
						if _COXNumMin1 % 2 == 0 and _COYNumMin1 % 2 == 0 :
							tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin1 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin1 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
							tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin1 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin1 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
						elif _COXNumMin1 % 2 == 0 and _COYNumMin1 % 2 == 1 :
							tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin1 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin1 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
							tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin1 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin1 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
						elif _COXNumMin1 % 2 == 1 and _COYNumMin1 % 2 == 0 :
							tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin1 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin1 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
							tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin1 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin1 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
						else :
							tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin1 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin1 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
							tmp.append([self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin1 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin1 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

				for i in range (0, _COXNumMin2) :
					for j in range (0, _COYNumMin2) :
						if _COXNumMin2 % 2 == 0 and _COYNumMin2 % 2 == 0 :
							tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin2 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin2 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
							tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin2 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin2 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
						elif _COXNumMin2 % 2 == 0 and _COYNumMin2 % 2 == 1 :
							tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin2 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin2 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
							tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COXNumMin2 // 2 - 0.5) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin2 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
						elif _COXNumMin2 % 2 == 1 and _COYNumMin2 % 2 == 0 :
							tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin2 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin2 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
							tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin2 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * (_COYNumMin2 // 2 - 0.5) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
						else :
							tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin2 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin2 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
							tmp.append([self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COXNumMin2 - 1) // 2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
										self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) * ((_COYNumMin2 - 1) // 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

		self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

		del tmp


		if _PType == True :
			print ('##############################     PIMP Layer Calcuation     ##############################################')
			if _Width % 2 == 1 :
				if DesignParameters._Technology == '028nm' :
					self._DesignParameter['_PPLayer']['_Width'] = _Width + 2 * _DRCObj._PpMinExtensiononPactive2 + 1
				else :
					self._DesignParameter['_PPLayer']['_Width'] = _Width + 2 * _DRCObj._PpMinExtensiononPactive2 + 1
			else :
				if DesignParameters._Technology == '028nm' :
					self._DesignParameter['_PPLayer']['_Width'] = _Width + 2 * _DRCObj._PpMinExtensiononPactive2
				else :
					self._DesignParameter['_PPLayer']['_Width'] = _Width + 2 * _DRCObj._PpMinExtensiononPactive2
			if _YWidth % 2 == 1 :
				_tmpY = _YWidth + 1
			else :
				_tmpY = _YWidth

			if _Width % 2 == 1 :
				_tmpW = _Width + 1
			else :
				_tmpW = _Width

			if DesignParameters._Technology == '028nm' :
				self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + _tmpY // 2 + _tmpW + _DRCObj._PpMinExtensiononPactive2],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_tmpY // 2 + _tmpW // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_tmpY // 2 + _tmpW // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] + (_tmpY // 2 + _tmpW // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + _tmpW // 2 + _DRCObj._PpMinExtensiononPactive2,
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + (_tmpY // 2 + _tmpW // 2)]
																	]]

			else :
				self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + _tmpY // 2 + _tmpW + _DRCObj._PpMinExtensiononPactive2],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_tmpY // 2 + _tmpW // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_tmpY // 2 + _tmpW // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] + (_tmpY // 2 + _tmpW // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + _tmpW // 2 + _DRCObj._PpMinExtensiononPactive2,
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + (_tmpY // 2 + _tmpW // 2)]
																	]]


		if _PType == False :
			if DesignParameters._Technology != '028nm' :
				print ('     NIMP Layer Calculation      '.center(105,'#'))
				self._DesignParameter['_NPLayer']['_Width'] = _Width + 2 * _DRCObj._NpMinExtensiononNactive2

				self._DesignParameter['_NPLayer']['_XYCoordinates'] = [[[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + _YWidth // 2 + _Width + _DRCObj._NpMinExtensiononNactive2],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_YWidth // 2 + _Width // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_YWidth // 2 + _Width // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] + (_YWidth // 2 + _Width // 2)],
																	[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + _Width // 2 + _DRCObj._NpMinExtensiononNactive2,
																	 self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + (_YWidth // 2 + _Width // 2)]]]
			print ('##############################     NWELL Layer Calcuation    ##############################################')
			if _YWidth % 2 == 1 :
					_tmpY = _YWidth + 1
			else :
					_tmpY = _YWidth

			if _Width % 2 == 1 :
					_tmpW = _Width + 1
			else :
					_tmpW = _Width

			if DesignParameters._Technology == '028nm' :
				if _Width % 2 == 1 :
					self._DesignParameter['_NWLayer']['_Width'] = _Width + 2 * _DRCObj._NwMinEnclosurePactive + 1
				else :
					self._DesignParameter['_NWLayer']['_Width'] = _Width + 2 * _DRCObj._NwMinEnclosurePactive


				self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + _tmpY // 2 + _tmpW + _DRCObj._NwMinEnclosurePactive],
																		[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_tmpY // 2 + _tmpW // 2)],
																		[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_tmpY // 2 + _tmpW // 2)],
																		[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] + (_tmpY // 2 + _tmpW // 2)],
																		[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + _tmpW // 2 + _DRCObj._NwMinEnclosurePactive,
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + (_tmpY // 2 + _tmpW // 2)]
																		]]

			else :
				self._DesignParameter['_NWLayer']['_Width'] = self._DesignParameter['_NPLayer']['_Width'] + 2 * _DRCObj._NwMinEnclosurePactive
				self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + _tmpY // 2 + _tmpW + _DRCObj._NpMinExtensiononNactive2 + _DRCObj._NwMinEnclosurePactive],
																		[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0],
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] - (_tmpY // 2 + _tmpW // 2)],
																		[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] - (_tmpY // 2 + _tmpW // 2)],
																		[self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][0],
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][0][1] + (_tmpY // 2 + _tmpW // 2)],
																		[self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][0] + _tmpW // 2 + _DRCObj._NpMinExtensiononNactive2 + _DRCObj._NwMinEnclosurePactive,
																		self._DesignParameter['_Met1Layery']['_XYCoordinates'][1][1] + (_tmpY // 2 + _tmpW // 2)]
																		]]


if __name__ == '__main__' :

	ans = [False, 2000.0, 2000.0, 170]
	_PType = ans[0]
	_XWidth = ans[1]
	_YWidth = ans[2]
	_Width = ans[3]

	#DesignParameters._Technology = '028nm'

	PSubringObj = _PSubring(_DesignParameter=None, _Name='PSubring')
	#print ("A!!")
	PSubringObj._CalculatePSubring(_PType = _PType, _XWidth = _XWidth, _YWidth = _YWidth, _Width = _Width)


	PSubringObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=PSubringObj._DesignParameter)
	_fileName = 'PSubring.gds'
	testStreamFile = open('./{}'.format(_fileName), 'wb')

	tmp = PSubringObj._CreateGDSStream(PSubringObj._DesignParameter['_GDSFile']['_GDSFile'])

	tmp.write_binary_gds_stream(testStreamFile)

	testStreamFile.close()

	print ('###############      Sending to FTP Server...      ##################')

	# ftp = ftplib.FTP('141.223.22.156')
	# ftp.login('junung', 'chlwnsdnd1!')
	# #ftp.cwd('/mnt/sda/junung/OPUS/Samsung28n')
	# ftp.cwd('/mnt/sdc/junung/OPUS/TSMC65n')
	# myfile = open('PSubring.gds', 'rb')
	# ftp.storbinary('STOR PSubring.gds', myfile)
	# myfile.close()
	# ftp.close()