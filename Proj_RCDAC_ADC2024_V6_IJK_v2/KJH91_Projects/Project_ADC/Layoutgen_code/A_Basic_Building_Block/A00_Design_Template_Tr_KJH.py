
TR 생성하고 Source묶고 Drain 묶고 Gate묶고 하기

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  M4, nfettw: Sref Gen.
## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
_Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH2._NmosWithDummy_KJH._ParametersForDesignCalculation)
## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
_Caculation_Parameters['_NMOSNumberofGate'] = _Tr4_NMOSNumberofGate
_Caculation_Parameters['_NMOSChannelWidth'] = _Tr4_NMOSChannelWidth
_Caculation_Parameters['_NMOSChannellength'] = _Tr4_NMOSChannellength
_Caculation_Parameters['_GateSpacing'] = _Tr4_GateSpacing
_Caculation_Parameters['_SDWidth'] = _Tr4_SDWidth
_Caculation_Parameters['_XVT'] = _Tr4_XVT
_Caculation_Parameters['_PCCrit'] = _Tr4_PCCrit
_Caculation_Parameters['_Source_Via_TF'] = _Tr4_Source_Via_TF
_Caculation_Parameters['_Drain_Via_TF'] = _Tr4_Drain_Via_TF
_Caculation_Parameters['_NMOSDummy'] = _Tr4_NMOSDummy
_Caculation_Parameters['_NMOSDummy_length'] = _Tr4_NMOSDummy_length
_Caculation_Parameters['_NMOSDummy_placement'] = _Tr4_NMOSDummy_placement

## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
self._DesignParameter['SRF_NMOS'] = self._SrefElementDeclaration(
    _DesignObj=A03_NmosWithDummy_KJH2._NmosWithDummy_KJH(_DesignParameter=None, _Name='{}:SRF_NMOS'.format(_Name)))[0]

## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
self._DesignParameter['SRF_NMOS']['_Reflect'] = [0, 0, 0]

## Define Sref Angle: ex)'_NMOS_POWER'
self._DesignParameter['SRF_NMOS']['_Angle'] = 0

## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
self._DesignParameter['SRF_NMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
self._DesignParameter['SRF_NMOS']['_XYCoordinates'] = [[0, 0]]

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr4, nfettw: Source M2 up connection
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Source M2 up connection: Vtc
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Source_Vtc_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
tmp = self.get_outter_KJH4('SRF_NMOS')
output_element = tmp['_Mostup']['index']
output_elementname = tmp['_Layercoord'][output_element[0]][1]
outter_coord = tmp['_Mostup']['coord']

self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(
    tmp1[0][0][0][0][0]['_XY_up'][1] - outter_coord[1])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Source')
self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Source')
tmpXY = []
for i in range(0, len(tmp[0])):
    ## Calculate Sref XYcoord
    ## Calculate
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    target_coord = tmp1[0][i][0][0][0]['_XY_up_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
    approaching_coord = tmp2[0][0]['_XY_down_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Source M2 up connection: Hrz
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Source_Hrz_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth : ViaYmin 기준
self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max(
    [_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Source')
self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XWidth'] = abs(
    tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

tmpXY = []
## Calculate Sref XYcoord
## Calculate
## Target_coord: _XY_type1
tmp1 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
target_coord = tmp1[0][0]['_XY_up_left']
## Approaching_coord: _XY_type2
tmp2 = self.get_param_KJH4('BND_NMOS_Source_Hrz_M2')
approaching_coord = tmp2[0][0]['_XY_down_left']
## Sref coord
tmp3 = self.get_param_KJH4('BND_NMOS_Source_Hrz_M2')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr4, nfettw: Drain M2 down connection
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Drain M2 down connection: Vtc
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
tmp = self.get_outter_KJH4('SRF_NMOS')
output_element = tmp['_Mostdown']['index']
output_elementname = tmp['_Layercoord'][output_element[0]][1]
outter_coord = tmp['_Mostdown']['coord']

self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(tmp1[0][0][0][0][0]['_XY_down'][1] - outter_coord[1])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
tmpXY = []
for i in range(0, len(tmp[0])):
    ## Calculate Sref XYcoord
    ## Calculate
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    target_coord = tmp1[0][i][0][0][0]['_XY_down_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
    approaching_coord = tmp2[0][0]['_XY_up_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Drain M2 down connection: Hrz
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth : ViaYmin 기준
self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max(
    [_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XWidth'] = abs(
    tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

tmpXY = []
## Calculate Sref XYcoord
## Calculate
## Target_coord: _XY_type1
tmp1 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
target_coord = tmp1[0][0]['_XY_down_left']
## Approaching_coord: _XY_type2
tmp2 = self.get_param_KJH4('BND_NMOS_Drain_Hrz_M2')
approaching_coord = tmp2[0][0]['_XY_up_left']
## Sref coord
tmp3 = self.get_param_KJH4('BND_NMOS_Drain_Hrz_M2')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  Tr4, nfettw: Gate Poly up connection
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Gate Poly up connection: Vtc
## Pre-defined
margin = 100

## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['POLY'][0],
    _Datatype=DesignParameters._LayerMapping['POLY'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
tmp1 = self.get_param_KJH4('BND_NMOS_Source_Hrz_M2')
tmp2 = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(
    tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_up'][1])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

## Calculate Sref XYcoord
tmpXY = []
## initialized Sref coordinate
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
## Calculate
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
for i in range(0, len(tmp[0])):
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
    target_coord = tmp1[0][i][0]['_XY_up_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
    approaching_coord = tmp2[0][0]['_XY_down_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr4, nfettw: Gate Poly up connection: Hrz
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['POLY'][0],
    _Datatype=DesignParameters._LayerMapping['POLY'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_YWidth'] = 60

## Define Boundary_element _XWidth
tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XWidth'] = abs(
    tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

## Calculate Sref XYcoord
tmpXY = []
## initialized Sref coordinate
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
## Calculate
## Target_coord: _XY_type1
tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
target_coord = tmp1[0][0]['_XY_up_left']
## Approaching_coord: _XY_type2
tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
approaching_coord = tmp2[0][0]['_XY_down_left']
## Sref coord
tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY


















Tr2개 묶기: 예를 들어 Tr1 source Tr2 source 묶기 ...
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5,Tr7,Tr9 Ptop M2 connection : Tr7 Tr9 connection
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5,Tr7,Tr9 Ptop M2 connection : Tr7 Tr9 connection: Vtc
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_Tr7Tr9_Ctop_Vtc_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
tmp1 = self.get_outter_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Hrz_M2')
tmp2 = self.get_outter_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Hrz_M2')
# tmp3 = self.get_outter_KJH4('SRF_Tr5Tr7Tr9','BND_Tr9_Source_Hrz_M2')

if (tmp1['_Mostup']['coord'] > tmp2['_Mostup']['coord']):
    tmp3 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Vtc_M2')
    tmp4 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Hrz_M2')
else:
    tmp3 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Vtc_M2')
    tmp4 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Hrz_M2')

self._DesignParameter['BND_Tr7Tr9_Ctop_Vtc_M2']['_YWidth'] = abs(tmp3[0][0][0]['_XY_down'][1] - tmp4[0][0][0]['_XY_down'][1])

## Define Boundary_element _XWidth
if (tmp1['_Mostup']['coord'] > tmp2['_Mostup']['coord']):
    tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Vtc_M2')
else:
    tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Vtc_M2')

self._DesignParameter['BND_Tr7Tr9_Ctop_Vtc_M2']['_XWidth'] = tmp[0][0][0]['_Xwidth']

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_Tr7Tr9_Ctop_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

tmpXY = []
## Calculate Sref XYcoord
## Calculate
## Target_coord: _XY_type1
if (tmp1['_Mostup']['coord'] > tmp2['_Mostup']['coord']):
    tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Vtc_M2')
    target_coord = tmp[0][-1][0]['_XY_down_left']
else:
    tmp = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Vtc_M2')
    target_coord = tmp[0][0][0]['_XY_down_left']

    ## Approaching_coord: _XY_type2
tmp2 = self.get_param_KJH4('BND_Tr7Tr9_Ctop_Vtc_M2')
approaching_coord = tmp2[0][0]['_XY_up_left']
## Sref coord
tmp3 = self.get_param_KJH4('BND_Tr7Tr9_Ctop_Vtc_M2')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_Tr7Tr9_Ctop_Vtc_M2']['_XYCoordinates'] = tmpXY
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## Tr5,Tr7,Tr9 Ptop M2 connection : Tr7 Tr9 connection: Hrz
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_Tr7Tr9_Ctop_Hrz_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
## Get_Outter : tmp['_Most--']['coord'] ex) down, left, right, up
tmp1 = self.get_outter_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Hrz_M2')
tmp2 = self.get_outter_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Hrz_M2')

if (tmp1['_Mostup']['coord'] > tmp2['_Mostup']['coord']):
    tmp4 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Hrz_M2')
else:
    tmp4 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Hrz_M2')

self._DesignParameter['BND_Tr7Tr9_Ctop_Hrz_M2']['_YWidth'] = tmp4[0][0][0]['_Ywidth']

## Define Boundary_element _XWidth
if (tmp1['_Mostup']['coord'] > tmp2['_Mostup']['coord']):
    tmp5 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Vtc_M2')
    tmp6 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Hrz_M2')
    self._DesignParameter['BND_Tr7Tr9_Ctop_Hrz_M2']['_XWidth'] = abs(
        tmp5[0][0][0]['_XY_right'][0] - tmp6[0][0][0]['_XY_left'][0])

else:
    tmp5 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr9_Source_Vtc_M2')
    tmp6 = self.get_param_KJH4('SRF_Tr5Tr7Tr9', 'BND_Tr7_Drain_Hrz_M2')
    self._DesignParameter['BND_Tr7Tr9_Ctop_Hrz_M2']['_XWidth'] = abs(
        tmp5[0][0][0]['_XY_left'][0] - tmp6[0][0][0]['_XY_right'][0])

    ## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_Tr7Tr9_Ctop_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

tmpXY = []
## Calculate Sref XYcoord
## Calculate
## Target_coord: _XY_type1
if (tmp1['_Mostup']['coord'] > tmp2['_Mostup']['coord']):
    tmp = self.get_param_KJH4('BND_Tr7Tr9_Ctop_Vtc_M2')
    target_coord = tmp[0][0]['_XY_down_right']

else:
    tmp = self.get_param_KJH4('BND_Tr7Tr9_Ctop_Vtc_M2')
    target_coord = tmp[0][0]['_XY_down_left']

    ## Approaching_coord: _XY_type2
if (tmp1['_Mostup']['coord'] > tmp2['_Mostup']['coord']):
    tmp = self.get_param_KJH4('BND_Tr7Tr9_Ctop_Hrz_M2')
    approaching_coord = tmp[0][0]['_XY_down_left']

else:
    tmp = self.get_param_KJH4('BND_Tr7Tr9_Ctop_Hrz_M2')
    approaching_coord = tmp[0][0]['_XY_down_right']

    ## Sref coord
tmp3 = self.get_param_KJH4('BND_Tr7Tr9_Ctop_Hrz_M2')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_Tr7Tr9_Ctop_Hrz_M2']['_XYCoordinates'] = tmpXY





## Nmos, Gate묶기 Source묶기 Drain묶기
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Sref Gen.
## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
_Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH3._NmosWithDummy_KJH3._ParametersForDesignCalculation)
## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
_Caculation_Parameters['_NMOSNumberofGate'] = _NMOS_NMOSNumberofGate
_Caculation_Parameters['_NMOSChannelWidth'] = _NMOS_NMOSChannelWidth
_Caculation_Parameters['_NMOSChannellength'] = _NMOS_NMOSChannellength
_Caculation_Parameters['_GateSpacing'] = _NMOS_GateSpacing
_Caculation_Parameters['_SDWidth'] = _NMOS_SDWidth
_Caculation_Parameters['_XVT'] = _NMOS_XVT
_Caculation_Parameters['_PCCrit'] = _NMOS_PCCrit
_Caculation_Parameters['_Source_Via_TF'] = _NMOS_Source_Via_TF
_Caculation_Parameters['_Drain_Via_TF'] = _NMOS_Drain_Via_TF
_Caculation_Parameters['_NMOSDummy'] = _NMOS_NMOSDummy
_Caculation_Parameters['_NMOSDummy_length'] = _NMOS_NMOSDummy_length
_Caculation_Parameters['_NMOSDummy_placement'] = _NMOS_NMOSDummy_placement

## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
self._DesignParameter['SRF_NMOS'] = self._SrefElementDeclaration(
    _DesignObj=A03_NmosWithDummy_KJH3._NmosWithDummy_KJH3(_DesignParameter=None, _Name='{}:SRF_NMOS'.format(_Name)))[0]

## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
self._DesignParameter['SRF_NMOS']['_Reflect'] = [0, 0, 0]

## Define Sref Angle: ex)'_NMOS_POWER'
self._DesignParameter['SRF_NMOS']['_Angle'] = 0

## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
self._DesignParameter['SRF_NMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
self._DesignParameter['SRF_NMOS']['_XYCoordinates'] = [[0, 0]]

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Drain Combine Upward
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Drain Vtc M2
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth : ViaYmin 기준
tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
tmp2 = self.get_param_KJH4('SRF_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(
    tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

tmpXY = []
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
for i in range(0, len(tmp[0])):
    ## Calculate Sref XYcoord
    ## Calculate
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    target_coord = tmp1[0][i][0][0][0]['_XY_up_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
    approaching_coord = tmp2[0][0]['_XY_down_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Drain Hrz M2
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth : ViaYmin 기준
self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max(
    [_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Drain')
self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XWidth'] = abs(
    tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

tmpXY = []
## Calculate Sref XYcoord
## Calculate
## Target_coord: _XY_type1
tmp1 = self.get_param_KJH4('BND_NMOS_Drain_Vtc_M2')
target_coord = tmp1[0][0]['_XY_up_left']
## Approaching_coord: _XY_type2
tmp2 = self.get_param_KJH4('BND_NMOS_Drain_Hrz_M2')
approaching_coord = tmp2[0][0]['_XY_down_left']
## Sref coord
tmp3 = self.get_param_KJH4('BND_NMOS_Drain_Hrz_M2')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Source Combine Downward
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Source Vtc M2
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Source_Vtc_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth : ViaYmin 기준
tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
tmp2 = self.get_param_KJH4('SRF_NMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(
    tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

tmpXY = []
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Source')
for i in range(0, len(tmp[0])):
    ## Calculate Sref XYcoord
    ## Calculate
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('SRF_NMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    target_coord = tmp1[0][i][0][0][0]['_XY_down_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
    approaching_coord = tmp2[0][0]['_XY_up_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Source_Vtc_M2']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Source Hrz M2
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Source_Hrz_M2'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL2'][0],
    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth : ViaYmin 기준
self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max(
    [_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_Met1Layer_Source')
self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XWidth'] = abs(
    tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

tmpXY = []
## Calculate Sref XYcoord
## Calculate
## Target_coord: _XY_type1
tmp1 = self.get_param_KJH4('BND_NMOS_Source_Vtc_M2')
target_coord = tmp1[0][0]['_XY_down_left']
## Approaching_coord: _XY_type2
tmp2 = self.get_param_KJH4('BND_NMOS_Source_Hrz_M2')
approaching_coord = tmp2[0][0]['_XY_up_left']
## Sref coord
tmp3 = self.get_param_KJH4('BND_NMOS_Source_Hrz_M2')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Source_Hrz_M2']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Poly combine
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Poly combine : Vtc
## Pre-defined
Ywidth_0 = 100

## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['POLY'][0],
    _Datatype=DesignParameters._LayerMapping['POLY'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_YWidth'] = Ywidth_0

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

## Calculate Sref XYcoord
tmpXY = []
## initialized Sref coordinate
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
## Calculate
tmp = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
for i in range(0, len(tmp[0])):
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
    target_coord = tmp1[0][i][0]['_XY_up_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
    approaching_coord = tmp2[0][0]['_XY_down_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
self._DesignParameter['BND_NMOS_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Poly combine : Hrz
## Pre-defined
Ywidth_1 = 70

## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['POLY'][0],
    _Datatype=DesignParameters._LayerMapping['POLY'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_YWidth'] = Ywidth_1

## Define Boundary_element _XWidth
tmp1 = self.get_param_KJH4('SRF_NMOS', 'BND_POLayer')
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XWidth'] = abs(
    tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

## Calculate Sref XYcoord
tmpXY = []
## initialized Sref coordinate
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
## Calculate
## Target_coord: _XY_type1
tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
target_coord = tmp1[0][0]['_XY_up_left']
## Approaching_coord: _XY_type2
tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
approaching_coord = tmp2[0][0]['_XY_up_left']
## Sref coord
tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  NMOS: Gate _ViaM0M1
## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : Metal1

## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_NMOS_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL1'][0],
    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
tmp = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
self._DesignParameter['BND_NMOS_Gate_Hrz_M1']['_YWidth'] = tmp[0][0]['_Ywidth']

## Define Boundary_element _XWidth
tmp = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
self._DesignParameter['BND_NMOS_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

## Define Boundary_element _XYCoordinates
self._DesignParameter['BND_NMOS_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

## Calculate Sref XYcoord
tmpXY = []
## initialized Sref coordinate
self._DesignParameter['BND_NMOS_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
## Calculate
## Target_coord: _XY_type1
tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
target_coord = tmp1[0][0]['_XY_down_left']
## Approaching_coord: _XY_type2
tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_M1')
approaching_coord = tmp2[0][0]['_XY_down_left']
## Sref coord
tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_M1')
Scoord = tmp3[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_NMOS_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY

## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1
## Sref generation: ViaX
## Define ViaX Parameter
_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
_Caculation_Parameters['_Layer1'] = 0
_Caculation_Parameters['_Layer2'] = 1
_Caculation_Parameters['_COX'] = None
_Caculation_Parameters['_COY'] = None

## Sref ViaX declaration
self._DesignParameter['SRF_NMOS_Gate_ViaM0M1'] = self._SrefElementDeclaration(
    _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None, _Name='{}:SRF_NMOS_Gate_ViaM0M1'.format(_Name)))[
    0]

## Define Sref Relection
self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

## Define Sref Angle
self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_Angle'] = 0

## Calcuate Overlapped XYcoord
tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_M1')
tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
_COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

## Define _COX and _COY
## Define _COX
if _COX < 2:
    _Caculation_Parameters['_COX'] = 2
    flag = 1
else:
    _Caculation_Parameters['_COX'] = _COX
    flag = 0
    ## Define _COY
_Caculation_Parameters['_COY'] = _COY

## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

## Calculate Sref XYcoord
tmpXY = []
## initialized Sref coordinate
self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
## Calculate
## Target_coord
tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_M1')
target_coord = tmp1[0][0]['_XY_cent']
## Approaching_coord
tmp2 = self.get_param_KJH4('SRF_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
approaching_coord = tmp2[0][0][0][0]['_XY_cent']
## Sref coord
tmp3 = self.get_param_KJH4('SRF_NMOS_Gate_ViaM0M1')
Scoord = tmp3[0][0]['_XY_origin']
## Calculate
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define
self._DesignParameter['SRF_NMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

if flag == 1:
    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
    ## Define Boundary_element _XWidth
    tmp1 = self.get_param_KJH4('SRF_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
    self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

    ## Define Boundary_element _XYCoordinates
    self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

    ## Calculate Sref XYcoord
    tmpXY = []
    ## initialized Sref coordinate
    self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
    ## Calculate
    ## Target_coord: _XY_type1
    ## X
    tmp1_1 = self.get_param_KJH4('SRF_NMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
    target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
    ## Y
    tmp1_2 = self.get_param_KJH4('BND_NMOS_Gate_Vtc_poly')
    target_coordy = tmp1_2[0][0]['_XY_up'][1]

    target_coord = [target_coordx, target_coordy]
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
    approaching_coord = tmp2[0][0]['_XY_up_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_NMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## NMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
    ## Define Boundary_element _XWidth
    tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
    self._DesignParameter['BND_NMOS_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0]['_Xwidth']

    ## Define Boundary_element _XYCoordinates
    tmp1 = self.get_param_KJH4('BND_NMOS_Gate_Hrz_poly')
    self._DesignParameter['BND_NMOS_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0]['_XY_down_left']]








    ## Pmos gate 묶기, source 묶기 Drain묶기
    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS
    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Sref Gen.
    ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
    _Caculation_Parameters = copy.deepcopy(A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3._ParametersForDesignCalculation)
    ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length
    _Caculation_Parameters['_PMOSNumberofGate'] = _PMOS_PMOSNumberofGate
    _Caculation_Parameters['_PMOSChannelWidth'] = _PMOS_PMOSChannelWidth
    _Caculation_Parameters['_PMOSChannellength'] = _PMOS_PMOSChannellength
    _Caculation_Parameters['_GateSpacing'] = _PMOS_GateSpacing
    _Caculation_Parameters['_SDWidth'] = _PMOS_SDWidth
    _Caculation_Parameters['_XVT'] = _PMOS_XVT
    _Caculation_Parameters['_PCCrit'] = _PMOS_PCCrit
    _Caculation_Parameters['_Source_Via_TF'] = _PMOS_Source_Via_TF
    _Caculation_Parameters['_Drain_Via_TF'] = _PMOS_Drain_Via_TF
    _Caculation_Parameters['_PMOSDummy'] = _PMOS_PMOSDummy
    _Caculation_Parameters['_PMOSDummy_length'] = _PMOS_PMOSDummy_length
    _Caculation_Parameters['_PMOSDummy_placement'] = _PMOS_PMOSDummy_placement

    ## Generate Sref: ex)self._DesignParameter['_PMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_PMOS_power_v2._PMOS_POWER( _DesignParameter=None, _Name='{}:PMOS_POWER'.format(_Name)))[0]
    self._DesignParameter['SRF_PMOS'] = self._SrefElementDeclaration(
        _DesignObj=A04_PmosWithDummy_KJH3._PmosWithDummy_KJH3(_DesignParameter=None,
                                                              _Name='{}:SRF_PMOS'.format(_Name)))[0]

    ## Define Sref Reflection: ex)self._DesignParameter['_PMOS_POWER']['_Reflect'] = [0, 0, 0]
    self._DesignParameter['SRF_PMOS']['_Reflect'] = [0, 0, 0]

    ## Define Sref Angle: ex)'_PMOS_POWER'
    self._DesignParameter['SRF_PMOS']['_Angle'] = 0

    ## Calculate Sref Layer by using Calculation_Parameter: ex)'_PMOS_POWER'
    self._DesignParameter['SRF_PMOS']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

    ## Define Sref _XYcoordinate: ex)'_PMOS_POWER'
    self._DesignParameter['SRF_PMOS']['_XYCoordinates'] = [[0, 0]]

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Combine Upward
    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Vtc M2
    ## Boundary_element Generation
    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
    self._DesignParameter['BND_PMOS_Drain_Vtc_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
    )

    ## Define Boundary_element _YWidth : ViaYmin 기준
    tmp1 = self.get_param_KJH4('SRF_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    tmp2 = self.get_param_KJH4('SRF_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(
        tmp1[0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1])

    ## Define Boundary_element _XWidth
    tmp = self.get_param_KJH4('SRF_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

    ## Define Boundary_element _XYCoordinates
    self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

    tmpXY = []
    tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Drain')
    for i in range(0, len(tmp[0])):
        ## Calculate Sref XYcoord
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        target_coord = tmp1[0][i][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_PMOS_Drain_Vtc_M2']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Drain Hrz M2
    ## Boundary_element Generation
    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
    self._DesignParameter['BND_PMOS_Drain_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
    )

    ## Define Boundary_element _YWidth : ViaYmin 기준
    self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max(
        [_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

    ## Define Boundary_element _XWidth
    tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Drain')
    self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XWidth'] = abs(
        tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

    ## Define Boundary_element _XYCoordinates
    self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

    tmpXY = []
    ## Calculate Sref XYcoord
    ## Calculate
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('BND_PMOS_Drain_Vtc_M2')
    target_coord = tmp1[0][0]['_XY_down_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_PMOS_Drain_Hrz_M2')
    approaching_coord = tmp2[0][0]['_XY_up_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_PMOS_Drain_Hrz_M2')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_PMOS_Drain_Hrz_M2']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Source Combine Downward
    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Source Vtc M2
    ## Boundary_element Generation
    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
    self._DesignParameter['BND_PMOS_Source_Vtc_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
    )

    ## Define Boundary_element _YWidth : ViaYmin 기준
    tmp1 = self.get_param_KJH4('SRF_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    tmp2 = self.get_param_KJH4('SRF_PMOS', 'SRF_Drain_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    self._DesignParameter['BND_PMOS_Source_Vtc_M2']['_YWidth'] = _DRCobj._MetalxMinSpace41 + abs(
        tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1])

    ## Define Boundary_element _XWidth
    tmp = self.get_param_KJH4('SRF_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
    self._DesignParameter['BND_PMOS_Source_Vtc_M2']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

    ## Define Boundary_element _XYCoordinates
    self._DesignParameter['BND_PMOS_Source_Vtc_M2']['_XYCoordinates'] = [[0, 0]]

    tmpXY = []
    tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Source')
    for i in range(0, len(tmp[0])):
        ## Calculate Sref XYcoord
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_PMOS', 'SRF_Source_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        target_coord = tmp1[0][i][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Source_Vtc_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Source_Vtc_M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_PMOS_Source_Vtc_M2']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Source Hrz M2
    ## Boundary_element Generation
    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
    self._DesignParameter['BND_PMOS_Source_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
    )

    ## Define Boundary_element _YWidth : ViaYmin 기준
    self._DesignParameter['BND_PMOS_Source_Hrz_M2']['_YWidth'] = _DRCobj._VIAxMinWidth + + 2 * max(
        [_DRCobj._Metal1MinEnclosureVia1, _DRCobj._MetalxMinEnclosureCO])

    ## Define Boundary_element _XWidth
    tmp = self.get_param_KJH4('SRF_PMOS', 'BND_Met1Layer_Source')
    self._DesignParameter['BND_PMOS_Source_Hrz_M2']['_XWidth'] = abs(
        tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

    ## Define Boundary_element _XYCoordinates
    self._DesignParameter['BND_PMOS_Source_Hrz_M2']['_XYCoordinates'] = [[0, 0]]

    tmpXY = []
    ## Calculate Sref XYcoord
    ## Calculate
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('BND_PMOS_Source_Vtc_M2')
    target_coord = tmp1[0][0]['_XY_up_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_PMOS_Source_Hrz_M2')
    approaching_coord = tmp2[0][0]['_XY_down_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_PMOS_Source_Hrz_M2')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_PMOS_Source_Hrz_M2']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Poly combine
    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Poly combine : Vtc
    ## Pre-defined
    Ywidth_0 = 100

    ## Boundary_element Generation
    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
    self._DesignParameter['BND_PMOS_Gate_Vtc_poly'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['POLY'][0],
        _Datatype=DesignParameters._LayerMapping['POLY'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
    )

    ## Define Boundary_element _YWidth
    self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_YWidth'] = Ywidth_0

    ## Define Boundary_element _XWidth
    tmp = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
    self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

    ## Define Boundary_element _XYCoordinates
    self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]

    ## Calculate Sref XYcoord
    tmpXY = []
    ## initialized Sref coordinate
    self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = [[0, 0]]
    ## Calculate
    tmp = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
    for i in range(0, len(tmp[0])):
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
        target_coord = tmp1[0][i][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
    self._DesignParameter['BND_PMOS_Gate_Vtc_poly']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Poly combine : Hrz
    ## Pre-defined
    Ywidth_1 = 70

    ## Boundary_element Generation
    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
    self._DesignParameter['BND_PMOS_Gate_Hrz_poly'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['POLY'][0],
        _Datatype=DesignParameters._LayerMapping['POLY'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
    )

    ## Define Boundary_element _YWidth
    self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_YWidth'] = Ywidth_1

    ## Define Boundary_element _XWidth
    tmp1 = self.get_param_KJH4('SRF_PMOS', 'BND_POLayer')
    self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XWidth'] = abs(
        tmp1[0][0][0]['_XY_left'][0] - tmp1[0][-1][0]['_XY_right'][0])

    ## Define Boundary_element _XYCoordinates
    self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

    ## Calculate Sref XYcoord
    tmpXY = []
    ## initialized Sref coordinate
    self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
    ## Calculate
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
    target_coord = tmp1[0][0]['_XY_down_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
    approaching_coord = tmp2[0][0]['_XY_down_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## ##########  PMOS: Gate _ViaM0M1
    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : Metal1

    ## Boundary_element Generation
    ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
    self._DesignParameter['BND_PMOS_Gate_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
    )

    ## Define Boundary_element _YWidth
    tmp = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
    self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_YWidth'] = tmp[0][0]['_Ywidth']

    ## Define Boundary_element _XWidth
    tmp = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
    self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XWidth'] = tmp[0][0]['_Xwidth']

    ## Define Boundary_element _XYCoordinates
    self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

    ## Calculate Sref XYcoord
    tmpXY = []
    ## initialized Sref coordinate
    self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = [[0, 0]]
    ## Calculate
    ## Target_coord: _XY_type1
    tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
    target_coord = tmp1[0][0]['_XY_down_left']
    ## Approaching_coord: _XY_type2
    tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
    approaching_coord = tmp2[0][0]['_XY_down_left']
    ## Sref coord
    tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define coordinates
    self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = tmpXY

    ## ########## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1
    ## Sref generation: ViaX
    ## Define ViaX Parameter
    _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
    _Caculation_Parameters['_Layer1'] = 0
    _Caculation_Parameters['_Layer2'] = 1
    _Caculation_Parameters['_COX'] = None
    _Caculation_Parameters['_COY'] = None

    ## Sref ViaX declaration
    self._DesignParameter['SRF_PMOS_Gate_ViaM0M1'] = self._SrefElementDeclaration(
        _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(_DesignParameter=None,
                                                    _Name='{}:SRF_PMOS_Gate_ViaM0M1'.format(_Name)))[0]

    ## Define Sref Relection
    self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

    ## Define Sref Angle
    self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_Angle'] = 0

    ## Calcuate Overlapped XYcoord
    tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
    tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
    Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[0][0])

    ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
    _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

    ## Define _COX and _COY
    ## Define _COX
    if _COX < 2:
        _Caculation_Parameters['_COX'] = 2
        flag = 1
    else:
        _Caculation_Parameters['_COX'] = _COX
        flag = 0
        ## Define _COY
    _Caculation_Parameters['_COY'] = _COY

    ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin,
    self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

    ## Calculate Sref XYcoord
    tmpXY = []
    ## initialized Sref coordinate
    self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]
    ## Calculate
    ## Target_coord
    tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_M1')
    target_coord = tmp1[0][0]['_XY_cent']
    ## Approaching_coord
    tmp2 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
    approaching_coord = tmp2[0][0][0][0]['_XY_cent']
    ## Sref coord
    tmp3 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1')
    Scoord = tmp3[0][0]['_XY_origin']
    ## Calculate
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)
    ## Define
    self._DesignParameter['SRF_PMOS_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

    if flag == 1:
        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : Poly Exten
        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XWidth'] = tmp1[0][0][0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord: _XY_type1
        ## X
        tmp1_1 = self.get_param_KJH4('SRF_PMOS_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')
        target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0]
        ## Y
        tmp1_2 = self.get_param_KJH4('BND_PMOS_Gate_Vtc_poly')
        target_coordy = tmp1_2[0][0]['_XY_up'][1]

        target_coord = [target_coordx, target_coordy]
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PMOS_Gate_Hrz_poly']['_XYCoordinates'] = tmpXY

        ## ########## ########## ########## ########## ########## ########## ########## ########## ########## PMOS: Gate _ViaM0M1 : _ViaM0M1 : M1 Exten
        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XWidth'] = tmp1[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        tmp1 = self.get_param_KJH4('BND_PMOS_Gate_Hrz_poly')
        self._DesignParameter['BND_PMOS_Gate_Hrz_M1']['_XYCoordinates'] = [tmp1[0][0]['_XY_down_left']]