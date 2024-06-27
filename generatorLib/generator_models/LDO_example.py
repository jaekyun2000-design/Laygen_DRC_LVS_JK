import time
import os
from generatorLib import DesignParameters
from generatorLib.generator_models.LDO_gen import LDO_top
import random

'''
********************************************************************************************************
This file is an example of an Analog LDO Layout Generator.

It has two modes: Compact mode & General mode. Each has a different input parameter range.
Additionally, you can check the generation time in the <Run> console.

Here is how it works:

- To generate your own LDO:
1. Go to the Generation Section.
2. Copy the example mode template you want to generate.
3. Use the template and input your parameters (See the checked parameter range).
4. Check the DRC checker if you want to verify DRC cleanliness (optional).
5. In Virtuoso, click "File" > "Import" > "Stream" to import the generated GDS file into the Library.

- To test the generator's reliability:
1. Go to the Test Section.
2. Remove comment mark of the mode you want to test
3. Change the number of iterations you want to execute.
4. Indent the marked section.
5. Check the DRC checker.
6. If there are no DRC errors, the console will print "DRC clean!"
********************************************************************************************************
'''

start = time.time()

''' Generation Section '''
# Examples
############### LDO (Compact mode) ################
Compact_Mode = True
# OPAmp
Amp_P0_Finger = 6
Amp_P1_Finger = 6
Amp_P2_Finger = 16
Amp_P3_Finger = 2

Amp_N0_Finger = 10
Amp_N1_Finger = 10
Amp_N2_Finger = 4
Amp_N3_Finger = 4
Amp_N4_Finger = 4

Amp_MOS_Length = 50
Amp_MOS_Width = 1000
_XVT = 'RVT'

Amp_NCAP_XWidth = 3200
Amp_NCAP_YWidth = 3300
Amp_NCAP_NumofGate = 3
Amp_NCAP_NumofRX = 4

Amp_Res_Width = 2050
Amp_Res_Length = 1050
Amp_Res_SeriesStripes = 4
Amp_Res_ParallelStripes = 1

_GuardringCOpitch = 175
_GuardringThickness = 348
_GuardringEnclosure = 56

# Pass Tr
PassTr_Finger = 29
PassTr_Length = 30
PassTr_Width = 1000
PassTr_row = 5
PassTr_col = 8
UnitHeight = None
Pass_XVT = 'RVT'

# Feedback Resistor
InsertFbRes = True
Fb_Res_Width = 3000
Fb_Res_Length = 700
Num_of_UpperRes = 2
Num_of_LowerRes = 3
SpacebtwRes_topbot = None
SpacebtwRes_rightleft = None
Fb_res_RingHeight = None
Fb_res_RingWidth = None

# Output Cap
InsertOutCap = False
OutCap_XWidth = 3000
OutCap_YWidth = 2078
OutCap_NumofGates = 5
OutCap_NumofOD = 4
OutCap_RingWidth = None
OutCap_RingHeight = None
#
# ############### LDO (General mode) ################
# Compact_Mode = False
# # OPAmp
# Amp_P0_Finger = 10
# Amp_P1_Finger = 10
# Amp_P2_Finger = 28
# Amp_P3_Finger = 2
#
# Amp_N0_Finger = 8
# Amp_N1_Finger = 8
# Amp_N2_Finger = 4
# Amp_N3_Finger = 6
# Amp_N4_Finger = 4
#
# Amp_MOS_Length = 100
# Amp_MOS_Width = 600
# _XVT = 'HVT'
#
# Amp_NCAP_XWidth = 2622
# Amp_NCAP_YWidth = 2622
# Amp_NCAP_NumofGate = 4
# Amp_NCAP_NumofRX = 16
#
# Amp_Res_Width = 1034
# Amp_Res_Length = 1500
# Amp_Res_SeriesStripes = 8
# Amp_Res_ParallelStripes = 1
#
# _GuardringCOpitch = 175
# _GuardringThickness = 348
# _GuardringEnclosure = 56
#
# # Pass Tr
# PassTr_Finger = 26
# PassTr_Length = 30
# PassTr_Width = 1100
# PassTr_row = 5
# PassTr_col = 20
# UnitHeight = None
# Pass_XVT = 'RVT'
#
# # Feedback Resistor
# InsertFbRes = False
# Fb_Res_Width = 3000
# Fb_Res_Length = 1000
# Num_of_UpperRes = 2
# Num_of_LowerRes = 3
# SpacebtwRes_topbot = None
# SpacebtwRes_rightleft = None
# Fb_res_RingHeight = None
# Fb_res_RingWidth = None
#
# # Output Cap
# InsertOutCap = False
# OutCap_XWidth = 3000
# OutCap_YWidth = 2078
# OutCap_NumofGates = 5
# OutCap_NumofOD = 4
# OutCap_RingWidth = None
# OutCap_RingHeight = None

''' Test Section '''
############### LDO (Compact mode) ################
# for i in range(0, 100):
#     Compact_Mode = True
#     Amp_P0_Finger = random.randint(2,30)
#     Amp_P1_Finger = Amp_P0_Finger
#     Amp_P2_Finger = random.randint(2,30)
#     Amp_P3_Finger = random.randint(2,30)
#
#     Amp_N0_Finger = random.randint(2,30)
#     Amp_N1_Finger = Amp_N0_Finger
#     Amp_N2_Finger = random.randint(2,30)
#     Amp_N3_Finger = random.randint(2,30)
#     Amp_N4_Finger = random.randint(2,30)
#
#     Amp_MOS_Length = random.randrange(50,200,2)
#     Amp_MOS_Width = random.randrange(500,1190,2)
#     _XVT = random.choice(['HVT','RVT','LVT','SLVT'])
#
#     Amp_NCAP_XWidth = random.randrange(1000,4000,2)
#     Amp_NCAP_YWidth = random.randrange(1000,4000,2)
#     Amp_NCAP_NumofGate = random.randint(1,4)
#     Amp_NCAP_NumofRX = random.randint(1,4)
#
#     Amp_Res_Width = random.randrange(1000,3000,2)
#     Amp_Res_Length = random.randrange(1000,3000,2)
#     Amp_Res_SeriesStripes = random.randint(1,6)
#     Amp_Res_ParallelStripes = 1
#
#     _GuardringCOpitch = 175
#     _GuardringThickness = 348
#     _GuardringEnclosure = 56
#
#     # Pass Tr
#     PassTr_Finger = random.randint(2, 40)
#     PassTr_Length = 30
#     PassTr_Width = random.randrange(500,1190,2)
#     PassTr_row = random.randint(1, 7)
#     PassTr_col = random.randrange(2, 10, 2)
#     UnitHeight = None
#     Pass_XVT = random.choice(['HVT','RVT','LVT','SLVT'])
#
#     # Feedback Resistor
#     InsertFbRes = random.choice([True, False])
#     Fb_Res_Width = random.randrange(1000,2000,2)
#     Fb_Res_Length = random.randrange(1000,2000,2)
#     Num_of_UpperRes = random.randrange(2,5,2)
#     Num_of_LowerRes = random.randint(Num_of_UpperRes,6)
#     # SpacebtwRes_topbot = random.randrange(400,1000,2)
#     # SpacebtwRes_rightleft = random.randrange(400,1000,2)
#     SpacebtwRes_topbot = None
#     SpacebtwRes_rightleft = None
#     Fb_res_RingHeight = None
#     Fb_res_RingWidth = None
#
#     # Output Cap
#     InsertOutCap = random.choice([True, False])
#     OutCap_XWidth = random.randrange(3000, 5000, 2)
#     OutCap_YWidth = random.randrange(3000, 5000, 2)
#     OutCap_NumofGates = random.randint(3, 4)
#     OutCap_NumofOD = random.randint(3, 4)
#     OutCap_RingWidth = None
#     OutCap_RingHeight = None
#
#     print(f"{i}nd loop")
#     print("Compact_Mode=", Compact_Mode)
#     print("Amp_P0_Finger=", Amp_P0_Finger)
#     print("Amp_P1_Finger=", Amp_P1_Finger)
#     print("Amp_P2_Finger=", Amp_P2_Finger)
#     print("Amp_P3_Finger=", Amp_P3_Finger)
#     print("Amp_N0_Finger=", Amp_N0_Finger)
#     print("Amp_N1_Finger=", Amp_N1_Finger)
#     print("Amp_N2_Finger=", Amp_N2_Finger)
#     print("Amp_N3_Finger=", Amp_N3_Finger)
#     print("Amp_N4_Finger=", Amp_N4_Finger)
#     print("Amp_MOS_Length=", Amp_MOS_Length)
#     print("Amp_MOS_Length=", Amp_MOS_Length)
#     print("Amp_MOS_Width=", Amp_MOS_Width)
#     print(f"_XVT='{_XVT}'")
#     print("Amp_NCAP_XWidth=", Amp_NCAP_XWidth)
#     print("Amp_NCAP_YWidth=", Amp_NCAP_YWidth)
#     print("Amp_NCAP_NumofGate=", Amp_NCAP_NumofGate)
#     print("Amp_NCAP_NumofRX=", Amp_NCAP_NumofRX)
#     print("Amp_Res_Width=", Amp_Res_Width)
#     print("Amp_Res_Length=", Amp_Res_Length)
#     print("Amp_Res_SeriesStripes=", Amp_Res_SeriesStripes)
#     print("Amp_Res_ParallelStripes=", Amp_Res_ParallelStripes)
#     print("_GuardringCOpitch=", _GuardringCOpitch)
#     print("_GuardringThickness=", _GuardringThickness)
#     print("_GuardringEnclosure=", _GuardringEnclosure)
#     print("PassTr_Finger=", PassTr_Finger)
#     print("PassTr_Length=", PassTr_Length)
#     print("PassTr_Width=", PassTr_Width)
#     print("PassTr_row=", PassTr_row)
#     print("PassTr_col=", PassTr_col)
#     print("UnitHeight=", UnitHeight)
#     print(f"Pass_XVT='{Pass_XVT}'")
#     print("InsertFbRes=", InsertFbRes)
#     print("Fb_Res_Width=", Fb_Res_Width)
#     print("Fb_Res_Length=", Fb_Res_Length)
#     print("Num_of_UpperRes=", Num_of_UpperRes)
#     print("Num_of_LowerRes=", Num_of_LowerRes)
#     print("SpacebtwRes_topbot=", SpacebtwRes_topbot)
#     print("SpacebtwRes_rightleft=", SpacebtwRes_rightleft)
#     print("Fb_res_RingHeight=", Fb_res_RingHeight)
#     print("Fb_res_RingWidth=", Fb_res_RingWidth)
#     print("InsertOutCap=", InsertOutCap)
#     print("OutCap_XWidth=", OutCap_XWidth)
#     print("OutCap_YWidth=", OutCap_YWidth)
#     print("OutCap_NumofGates=", OutCap_NumofGates)
#     print("OutCap_NumofOD=", OutCap_NumofOD)
#     print("OutCap_RingWidth=", OutCap_RingWidth)
#     print("OutCap_RingHeight=", OutCap_RingHeight)

############### LDO (General mode) ################
# for i in range(0, 100):
#     Compact_Mode = False
#     Amp_P0_Finger = random.randint(6,30)
#     Amp_P1_Finger = Amp_P0_Finger
#     Amp_P2_Finger = random.randint(2,30)
#     Amp_P3_Finger = random.randint(2,30)
#
#     Amp_N0_Finger = Amp_P0_Finger
#     Amp_N1_Finger = Amp_N0_Finger
#     Amp_N2_Finger = random.randint(2,30)
#     Amp_N3_Finger = random.randint(2,30)
#     Amp_N4_Finger = random.randint(2,30)
#
#     Amp_MOS_Length = random.randrange(50,200,2)
#     Amp_MOS_Width = random.randrange(500,1190,2)
#     _XVT = random.choice(['HVT','RVT','LVT','SLVT'])
#
#     Amp_NCAP_XWidth = random.randrange(1000,4000,2)
#     Amp_NCAP_YWidth = random.randrange(1000,4000,2)
#     Amp_NCAP_NumofGate = random.randint(2,4)
#     Amp_NCAP_NumofRX = random.randint(10,20)
#
#     Amp_Res_Width = random.randrange(1000,3000,2)
#     Amp_Res_Length = random.randrange(1000,3000,2)
#     Amp_Res_SeriesStripes = random.randint(4,10)
#     Amp_Res_ParallelStripes = 1
#
#     _GuardringCOpitch = 175
#     _GuardringThickness = 348
#     _GuardringEnclosure = 56
#
#     # Pass Tr
#     PassTr_Finger = random.randint(30, 50)
#     PassTr_Length = 30
#     PassTr_Width = random.randrange(500,1190,2)
#     PassTr_row = random.randint(5, 10)
#     PassTr_col = random.randrange(10, 30, 2)
#     UnitHeight = None
#     Pass_XVT = random.choice(['HVT','RVT','LVT','SLVT'])
#
#     # Feedback Resistor
#     InsertFbRes = False
#     Fb_Res_Width = random.randrange(1000,5000,2)
#     Fb_Res_Length = random.randrange(1000,5000,2)
#     Num_of_UpperRes = random.randrange(2,8,2)
#     Num_of_LowerRes = random.randint(Num_of_UpperRes,9)
#     # SpacebtwRes_topbot = random.randrange(400,1000,2)
#     # SpacebtwRes_rightleft = random.randrange(400,1000,2)
#     SpacebtwRes_topbot = None
#     SpacebtwRes_rightleft = None
#     Fb_res_RingHeight = None
#     Fb_res_RingWidth = None
#
#     # Output Cap
#     InsertOutCap = False
#     OutCap_XWidth = random.randrange(1000, 5000, 2)
#     OutCap_YWidth = random.randrange(1000, 5000, 2)
#     OutCap_NumofGates = random.randint(1, 4)
#     OutCap_NumofOD = random.randint(1, 4)
#     OutCap_RingWidth = None
#     OutCap_RingHeight = None
#
#     print(f"{i}nd loop")
#     print("Compact_Mode=", Compact_Mode)
#     print("Amp_P0_Finger=", Amp_P0_Finger)
#     print("Amp_P1_Finger=", Amp_P1_Finger)
#     print("Amp_P2_Finger=", Amp_P2_Finger)
#     print("Amp_P3_Finger=", Amp_P3_Finger)
#     print("Amp_N0_Finger=", Amp_N0_Finger)
#     print("Amp_N1_Finger=", Amp_N1_Finger)
#     print("Amp_N2_Finger=", Amp_N2_Finger)
#     print("Amp_N3_Finger=", Amp_N3_Finger)
#     print("Amp_N4_Finger=", Amp_N4_Finger)
#     print("Amp_MOS_Length=", Amp_MOS_Length)
#     print("Amp_MOS_Length=", Amp_MOS_Length)
#     print("Amp_MOS_Width=", Amp_MOS_Width)
#     print(f"_XVT='{_XVT}'")
#     print("Amp_NCAP_XWidth=", Amp_NCAP_XWidth)
#     print("Amp_NCAP_YWidth=", Amp_NCAP_YWidth)
#     print("Amp_NCAP_NumofGate=", Amp_NCAP_NumofGate)
#     print("Amp_NCAP_NumofRX=", Amp_NCAP_NumofRX)
#     print("Amp_Res_Width=", Amp_Res_Width)
#     print("Amp_Res_Length=", Amp_Res_Length)
#     print("Amp_Res_SeriesStripes=", Amp_Res_SeriesStripes)
#     print("Amp_Res_ParallelStripes=", Amp_Res_ParallelStripes)
#     print("_GuardringCOpitch=", _GuardringCOpitch)
#     print("_GuardringThickness=", _GuardringThickness)
#     print("_GuardringEnclosure=", _GuardringEnclosure)
#     print("PassTr_Finger=", PassTr_Finger)
#     print("PassTr_Length=", PassTr_Length)
#     print("PassTr_Width=", PassTr_Width)
#     print("PassTr_row=", PassTr_row)
#     print("PassTr_col=", PassTr_col)
#     print("UnitHeight=", UnitHeight)
#     print(f"Pass_XVT='{Pass_XVT}'")
#     print("InsertFbRes=", InsertFbRes)
#     print("Fb_Res_Width=", Fb_Res_Width)
#     print("Fb_Res_Length=", Fb_Res_Length)
#     print("Num_of_UpperRes=", Num_of_UpperRes)
#     print("Num_of_LowerRes=", Num_of_LowerRes)
#     print("SpacebtwRes_topbot=", SpacebtwRes_topbot)
#     print("SpacebtwRes_rightleft=", SpacebtwRes_rightleft)
#     print("Fb_res_RingHeight=", Fb_res_RingHeight)
#     print("Fb_res_RingWidth=", Fb_res_RingWidth)
#     print("InsertOutCap=", InsertOutCap)
#     print("OutCap_XWidth=", OutCap_XWidth)
#     print("OutCap_YWidth=", OutCap_YWidth)
#     print("OutCap_NumofGates=", OutCap_NumofGates)
#     print("OutCap_NumofOD=", OutCap_NumofOD)
#     print("OutCap_RingWidth=", OutCap_RingWidth)
#     print("OutCap_RingHeight=", OutCap_RingHeight)

''' Custom LDO / Debug LDO (Place the parameters of the LDO you want to create or debug below)'''
################# LDO compact ######################### (Like this)
# Compact_Mode = True
# # OPAmp
# Amp_P0_Finger = 10
# Amp_P1_Finger = 10
# Amp_P2_Finger = 18
# Amp_P3_Finger = 4
#
# Amp_N0_Finger = 10
# Amp_N1_Finger = 10
# Amp_N2_Finger = 4
# Amp_N3_Finger = 4
# Amp_N4_Finger = 6
#
# Amp_MOS_Length = 100
# Amp_MOS_Width = 1000
# _XVT = 'HVT'
#
# Amp_NCAP_XWidth = 2500
# Amp_NCAP_YWidth = 3000
# Amp_NCAP_NumofGate = 2
# Amp_NCAP_NumofRX = 3
#
# Amp_Res_Width = 2050
# Amp_Res_Length = 1050
# Amp_Res_SeriesStripes = 4
# Amp_Res_ParallelStripes = 1
#
# _GuardringCOpitch = 175
# _GuardringThickness = 348
# _GuardringEnclosure = 56
#
# # Pass Tr
# PassTr_Finger = 29
# PassTr_Length = 30
# PassTr_Width = 1000
# PassTr_row = 5
# PassTr_col = 8
# UnitHeight = None
# Pass_XVT = 'RVT'
#
# # Feedback Resistor
# InsertFbRes = True
# Fb_Res_Width = 3000
# Fb_Res_Length = 700
# Num_of_UpperRes = 2
# Num_of_LowerRes = 3
# SpacebtwRes_topbot = None
# SpacebtwRes_rightleft = None
# Fb_res_RingHeight = None
# Fb_res_RingWidth = None
#
# # Output Cap
# InsertOutCap = False
# OutCap_XWidth = 3000
# OutCap_YWidth = 2078
# OutCap_NumofGates = 5
# OutCap_NumofOD = 4
# OutCap_RingWidth = None
# OutCap_RingHeight = None

''' Indent from here (Only when test reliability) '''
print('#############################      Converting to GDS II File...      ##############################')
DesignParameters._Technology = 'SS28nm'
TopObj = LDO_top._LDO(_DesignParameter=None, _Name='_LDO')
TopObj._CalculateDesignParameter(
    Compact_Mode=Compact_Mode,
    Amp_P0_Finger=Amp_P0_Finger,
    Amp_P1_Finger=Amp_P1_Finger,
    Amp_P2_Finger=Amp_P2_Finger,
    Amp_P3_Finger=Amp_P3_Finger,

    Amp_N0_Finger=Amp_N0_Finger,
    Amp_N1_Finger=Amp_N1_Finger,
    Amp_N2_Finger=Amp_N2_Finger,
    Amp_N3_Finger=Amp_N3_Finger,
    Amp_N4_Finger=Amp_N4_Finger,

    Amp_MOS_Length=Amp_MOS_Length,
    Amp_MOS_Width=Amp_MOS_Width,
    _XVT=_XVT,

    Amp_NCAP_XWidth=Amp_NCAP_XWidth,
    Amp_NCAP_YWidth=Amp_NCAP_YWidth,
    Amp_NCAP_NumofGate=Amp_NCAP_NumofGate,
    Amp_NCAP_NumofRX=Amp_NCAP_NumofRX,

    Amp_Res_Width=Amp_Res_Width,
    Amp_Res_Length=Amp_Res_Length,
    Amp_Res_SeriesStripes=Amp_Res_SeriesStripes,
    Amp_Res_ParallelStripes=Amp_Res_ParallelStripes,

    _GuardringCOpitch=_GuardringCOpitch,
    _GuardringThickness=_GuardringThickness,
    _GuardringEnclosure=_GuardringEnclosure,

    PassTr_Finger=PassTr_Finger,
    PassTr_Length=PassTr_Length,
    PassTr_Width=PassTr_Width,
    PassTr_row=PassTr_row,
    PassTr_col=PassTr_col,
    UnitHeight=UnitHeight,
    Pass_XVT=Pass_XVT,

    InsertFbRes=InsertFbRes,
    Fb_Res_Width=Fb_Res_Width,
    Fb_Res_Length=Fb_Res_Length,
    Num_of_UpperRes=Num_of_UpperRes,
    Num_of_LowerRes=Num_of_LowerRes,
    SpacebtwRes_topbot=SpacebtwRes_topbot,
    SpacebtwRes_rightleft=SpacebtwRes_rightleft,
    Fb_res_RingHeight=Fb_res_RingHeight,
    Fb_res_RingWidth=Fb_res_RingWidth,

    InsertOutCap=InsertOutCap,
    OutCap_XWidth=OutCap_XWidth,
    OutCap_YWidth=OutCap_YWidth,
    OutCap_NumofGates=OutCap_NumofGates,
    OutCap_NumofOD=OutCap_NumofOD,
    OutCap_RingWidth=OutCap_RingWidth,
    OutCap_RingHeight=OutCap_RingHeight
)
TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
testStreamFile = open('./_LDO.gds', 'wb')
tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
tmp.write_binary_gds_stream(testStreamFile)
testStreamFile.close()

gds_gen_time = time.time()

print('#############################      Sending to FTP Server...      ##############################')

import ftplib

ftp = ftplib.FTP('141.223.24.53')
ftp.login('userID', 'userPW')
ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
myfile = open('./_LDO.gds', 'rb')
ftp.storbinary('STOR _LDO.gds', myfile)
myfile.close()

send_time = time.time()
''' Indent up to here (Only when test reliability) '''

    # ''' DRC Checker '''
    # from generatorLib.generator_models import DRCchecker
    # a = DRCchecker.DRCchecker('smlim96','min753531','/mnt/sdc/smlim96/OPUS/ss28',
    #                           '/mnt/sdc/smlim96/OPUS/ss28/DRC/run','_LDOdrccheck','_LDO',None)
    # a.DRCchecker()
    # print("DRC Clean!!")

drc_check_time = time.time()
print(f"GDS file generation time = {gds_gen_time - start:.5f} sec")
print(f"File transfer time = {send_time - gds_gen_time:.5f} sec")
print(f"DRC Check time = {drc_check_time - send_time:.5f} sec")
print(f"Total time = {drc_check_time - start:.5f} sec")
