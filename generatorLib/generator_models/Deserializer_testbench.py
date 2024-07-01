from generatorLib import DesignParameters
from generatorLib.generator_models import Deserializer1toN
import time
start = time.time()
'''''
#####################################################################
This file is an example of an 1toN Deserializer Layout Generator.

It can change the Deserializing ratio controlled by Deserializer1toN parameter 

Here is how it works:

- To generate your own Deserializer:
1. Go to the Generation Section.
2  Type the appropriate input parameter in generation Section
3. Run the code while the message(Finished) came out in log screen
4. Check the DRC checker if you want to verify DRC cleanliness (optional).
5. In Virtuoso, click "File" > "Import" > "Stream" to import the generated GDS file into the Library.

- To test the generator's reliability:
1. Go to the Test Section.
2. Remove comment mark of the mode you want to test
3. Change the number of iterations you want to execute.
4. Indent the marked section.
5. Check the DRC checker.
6. If there are no DRC errors, the console will print "DRC clean!"
#####################################################################
'''''

'''''Generation Section'''''
TG1_Finger = 1       # number of fingers of 1st Transmission Gate
TG2_Finger = 2       # number of fingers of 2nd Transmission Gate
TSI1_Finger = 1      # number of fingers of 1st Tristate Inverter
TSI2_Finger = 1      # number of fingers of 2nd Tristate Inverter
INV1_Finger = 3      # number of fingers of 1st Inverter
INV2_Finger = 1       # number of fingers of 2nd Inverter
INV3_Finger = 1       # number of fingers of 3rd Inverter
INV4_Finger = 3       # number of fingers of 4th Inverter

TG3_Finger = 2         # number of fingers of 4th Inverter
TSI3_Finger = 1        # number of fingers of 3rd Tristate Inverter
INV5_Finger = 4         # number of fingers of 5th Inverter
INV6_Finger = 4         # number of fingers of 6th Inverter
TG4_Finger = 2          # number of fingers of 4th Transmission Gate
TSI4_Finger = 1         # number of fingers of 4th Tristate Inverter
INV7_Finger = 4         # number of fingers of 7th Inverter
INV8_Finger = 4         # number of fingers of 8th Inverter
INV9_Finger = 1         # number of fingers of 9th Inverter
INV10_Finger = 1        # number of fingers of 10th Inverter

Deserialize1toN = 32    # Deserializing ratio of Deserializer (2, 4, 8, 16, 32)

np_ratio = 2            # Nmos and Pmos Width ratio (Nmos Width * np\_ratio = Pmos Width)

dummy = False           # Added Dummy cells in empty space (True or False)
ChannelLength = 30      # channel Length of mosfets
GateSpacing = 100       # horizontal space distance between polys
SDWidth = 66            # Source and Drain space in mosfets
XVT = 'SLVT'            # Threshold Voltage of mosfets ('SLVT', 'RVT', 'LVT', 'HVT')
CellHeight = 1800       # sum of height in total height of cells
SupplyRailType = 2      # supply rail type (1. rectangle via 2. square via)
TG1_NMWidth = TG2_NMWidth = TG3_NMWidth = TG4_NMWidth = TSI1_NMWidth = TSI2_NMWidth = TSI3_NMWidth = TSI4_NMWidth = INV1_NMWidth = INV2_NMWidth = INV3_NMWidth \
    = INV4_NMWidth = INV5_NMWidth = INV6_NMWidth = INV7_NMWidth = INV8_NMWidth = INV9_NMWidth = INV10_NMWidth = 200
        ## nmos channel width of mosfets
TG1_PMWidth = TG2_PMWidth = TG3_PMWidth = TG4_PMWidth = TSI1_PMWidth = TSI2_PMWidth = TSI3_PMWidth = TSI4_PMWidth = INV1_PMWidth = INV2_PMWidth = INV3_PMWidth \
    = INV4_PMWidth = INV5_PMWidth = INV6_PMWidth = INV7_PMWidth = INV8_PMWidth = INV9_PMWidth = INV10_PMWidth = TG1_NMWidth * np_ratio
        ## pmos channel width of mosfets



TG1_Finger_clk = TG1_Finger         # number of fingers of 1st Transmission Gate in clk
TG2_Finger_clk = TG2_Finger         # number of fingers of 2nd Transmission Gate in clk
TSI1_Finger_clk = TSI1_Finger       # number of fingers of 1st Tristate Inverter in clk
TSI2_Finger_clk = TSI2_Finger       # number of fingers of 2nd Tristate Inverter in clk
INV1_Finger_clk = INV1_Finger       # number of fingers of 1st Inverter in clk
INV2_Finger_clk = INV2_Finger       # number of fingers of 2nd Inverter in clk
INV3_Finger_clk = INV3_Finger       # number of fingers of 3rd Inverter in clk
INV4_Finger_clk = INV5_Finger       # number of fingers of 4th Inverter in clk
INV5_Finger_clk = INV6_Finger       # number of fingers of 5th Inverter in clk

'''''''Testing Section'''''''
import random
# list = [2, 4, 8, 16, 32]
# Deserialize1toN = random.choice(list)
# TG1_Finger = random.randint(1, 10)
# TG2_Finger = random.randint(1, 10)
#
# INV1_Finger = random.randint(1, 10)
# INV2_Finger = random.randint(1, 10)
# INV3_Finger = random.randint(1, 10)
# INV4_Finger = random.randint(1, 10)
#
# TG3_Finger = random.randint(1, 10)
# INV5_Finger = random.randint(1, 10)
# INV6_Finger = random.randint(1, 10)
#
# TG4_Finger = random.randint(1, 10)
#
# INV7_Finger = random.randint(1, 10)
# INV8_Finger = random.randint(1, 10)
# INV9_Finger = random.randint(1, 10)
# INV10_Finger = random.randint(1, 10)
#
# Deserialize1toN = list
#
# np_ratio =random.randint(2, 3)
# TG1_NMWidth = TG2_NMWidth = TG3_NMWidth = TG4_NMWidth = TSI1_NMWidth = TSI2_NMWidth = TSI3_NMWidth = TSI4_NMWidth = INV1_NMWidth = INV2_NMWidth = INV3_NMWidth \
#     = INV4_NMWidth = INV5_NMWidth = INV6_NMWidth = INV7_NMWidth = INV8_NMWidth = INV9_NMWidth = INV10_NMWidth =  random.randrange(200, 400, 50)
# TG1_PMWidth = TG2_PMWidth = TG3_PMWidth = TG4_PMWidth = TSI1_PMWidth = TSI2_PMWidth = TSI3_PMWidth = TSI4_PMWidth = INV1_PMWidth = INV2_PMWidth = INV3_PMWidth \
#     = INV4_PMWidth = INV5_PMWidth = INV6_PMWidth = INV7_PMWidth = INV8_PMWidth = INV9_PMWidth = INV10_PMWidth = TG1_NMWidth * np_ratio
#
# dummy = False
# ChannelLength =  random.choice([30, 40])
# GateSpacing = 100
# SDWidth = 66
# list_XVT = ['SLVT', 'RVT', 'LVT', 'HVT']
# XVT_random = random.choice(list_XVT)
# XVT = XVT_random
# CellHeight = 1800
# SupplyRailType = random.randint(1, 2)
#


# TG1_Finger_clk = TG1_Finger
# TG2_Finger_clk = TG2_Finger
# TSI1_Finger_clk = TSI1_Finger = TSI2_Finger = TSI3_Finger = TSI4_Finger = 1
# TSI2_Finger_clk = TSI2_Finger
# INV1_Finger_clk = INV1_Finger
# INV2_Finger_clk = INV2_Finger
# INV3_Finger_clk = INV3_Finger
# INV4_Finger_clk = INV5_Finger
# INV5_Finger_clk = INV6_Finger


print('#############################      Converting to GDS II File...      ##############################')

DesignParameters._Technology = 'SS28nm'
TopObj = Deserializer1toN.Deserializer1toN(_DesignParameter=None, _Name='Deserializer1toN') # Python code of converting to GDS II File
TopObj._CalculateDesignParameter(


    Deserialize1toN=Deserialize1toN,
    TG1_Finger=TG1_Finger,
    TG1_NMWidth=TG1_NMWidth,
    TG1_PMWidth=TG1_PMWidth,
    TG2_Finger=TG2_Finger,
    TG2_NMWidth=TG2_NMWidth,
    TG2_PMWidth=TG2_PMWidth,

    TSI1_Finger=TSI1_Finger,
    TSI1_NMWidth=TSI1_NMWidth,
    TSI1_PMWidth=TSI1_PMWidth,
    TSI2_Finger=TSI2_Finger,
    TSI2_NMWidth=TSI2_NMWidth,
    TSI2_PMWidth=TSI2_PMWidth,

    INV1_Finger=INV1_Finger,
    INV1_NMWidth=INV1_NMWidth,
    INV1_PMWidth=INV1_PMWidth,

    INV2_Finger=INV2_Finger,
    INV2_NMWidth=INV2_NMWidth,
    INV2_PMWidth=INV2_PMWidth,
    INV3_Finger=INV3_Finger,
    INV3_NMWidth=INV3_NMWidth,
    INV3_PMWidth=INV3_PMWidth,

    INV4_Finger=INV4_Finger,
    INV4_NMWidth=INV4_NMWidth,
    INV4_PMWidth=INV4_PMWidth,

    TG3_Finger=TG3_Finger,
    TG3_NMWidth=TG3_NMWidth,
    TG3_PMWidth=TG3_PMWidth,

    TSI3_Finger=TSI3_Finger,
    TSI3_NMWidth=TSI3_NMWidth,
    TSI3_PMWidth=TSI3_PMWidth,

    INV5_Finger=INV5_Finger,
    INV5_NMWidth=INV5_NMWidth,
    INV5_PMWidth=INV5_PMWidth,
    INV6_Finger=INV6_Finger,
    INV6_NMWidth=INV6_NMWidth,
    INV6_PMWidth=INV6_PMWidth,

    TG4_Finger=TG4_Finger,
    TG4_NMWidth=TG4_NMWidth,
    TG4_PMWidth=TG4_PMWidth,

    TSI4_Finger=TSI4_Finger,
    TSI4_NMWidth=TSI4_NMWidth,
    TSI4_PMWidth=TSI4_PMWidth,

    INV7_Finger=INV7_Finger,
    INV7_NMWidth=INV7_NMWidth,
    INV7_PMWidth=INV7_PMWidth,
    INV8_Finger=INV8_Finger,
    INV8_NMWidth=INV8_NMWidth,
    INV8_PMWidth=INV8_PMWidth,
    INV9_Finger=INV9_Finger,
    INV9_NMWidth=INV9_NMWidth,
    INV9_PMWidth=INV9_PMWidth,
    INV10_Finger=INV10_Finger,
    INV10_NMWidth=INV10_NMWidth,
    INV10_PMWidth=INV10_PMWidth,

    TG1_Finger_clk=TG1_Finger_clk,
    TG2_Finger_clk=TG2_Finger_clk,

    TSI1_Finger_clk=TSI1_Finger_clk,
    TSI2_Finger_clk=TSI2_Finger_clk,

    INV1_Finger_clk=INV1_Finger_clk,
    INV2_Finger_clk=INV2_Finger_clk,
    INV3_Finger_clk=INV3_Finger_clk,
    INV4_Finger_clk=INV4_Finger_clk,
    INV5_Finger_clk=INV5_Finger_clk,

    np_ratio=np_ratio,
    dummy=dummy,
    ChannelLength=ChannelLength,
    GateSpacing=GateSpacing,
    SDWidth=SDWidth,
    XVT=XVT,
    CellHeight=CellHeight,
    SupplyRailType=SupplyRailType)

TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
testStreamFile = open('./Deserializer1toN.gds', 'wb')                               # gds file save in testStreamFile
tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])      # Converting to GDS II File finished
tmp.write_binary_gds_stream(testStreamFile)
testStreamFile.close()                                                              # Streamfile close

print('#############################      Sending to FTP Server...      ##############################')

import ftplib                                            # import ftplib
ftp = ftplib.FTP('141.223.24.53')                        # server ip address
ftp.login('ljw95', 'dlwodn123')                          # server ID and password
ftp.cwd('/mnt/sdc/ljw95/OPUS/ss28')                      # Directory Path to save the .gds file
myfile = open('Deserializer1toN.gds', 'rb')              # gds file name and chosing read mode or write mode
ftp.storbinary('STOR Deserializer1toN.gds', myfile)
myfile.close()

print('#############################      DRC verification...      ##############################')
# import DRCchecker               # import DRCchecker.py
# a = DRCchecker.DRCchecker('ljw95','dlwodn123','/mnt/sdc/ljw95/OPUS/ss28','/mnt/sdc/ljw95/OPUS/ss28/DRC/run','Deserializer1toN','Deserializer1toN',None)
#                                         # Describe Server ID, password, Directory Path, DRC run file Path, Libraray name, Cell name
# a.DRCchecker()              ### DRC checker Code to verify a Design rule


print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
end = time.time()

print('      Finished       '.center(105, '#'))
# print("DRC Clean!!!")

print(f"{end - start:.5f} sec")
# generation_time = time.time()
# print("Generation time=",generation_time)