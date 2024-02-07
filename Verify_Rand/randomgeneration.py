import sys
import paramiko
import base64
from scp import SCPClient, SCPException
import multiprocessing as mp
from multiprocessing import Pool
from threading import Thread
from tqdm import tqdm
import os
import random

import schematic
import Slicer_test
import SRLatch_test
import FRB2
import RB2
import SlicerandSRLatchwtResistor_test

# sys.path.append('./generatorLib/generator_models/rx_project')
# from generatorLib.generator_models.rx_project import inverter_demo_20231202


class Parameter:
    def __init__(self, name: str, step: int or float, value_range: list, offset_param=None):
        self.name = name
        self.step = step
        self.value_range = value_range
        self.offset_param = offset_param

    def get_random_value(self, parm_double=False, offset=0):
        try:
            if self.step == 0 :
                return self.value_range[0] + offset
            random.seed(os.urandom(8))
            if type(self.value_range[0]) == int and type(self.value_range[1]) == int:
                if parm_double:
                    return random.randrange(self.value_range[0], int(2*self.value_range[1]-self.value_range[0]), self.step) + offset
                else:
                    return random.randrange(self.value_range[0], self.value_range[1], self.step) + offset
            else:
                if parm_double:
                    return random.uniform(self.value_range[0], 2*self.value_range[1]-self.value_range[0]) + offset
                else:
                    return random.uniform(self.value_range[0], self.value_range[1]) + offset
        except:
            print(self.name)
            print(self.step)
            print(self.value_range)


class RangeParameter(Parameter):
    def __init__(self, names: tuple, step: int or float, value_range: list):
        super().__init__(names, step, value_range)
        self.names = names

    def get_random_value(self, parm_double=False):
        random.seed(os.urandom(8))
        if type(self.value_range[0]) == int and type(self.value_range[1]) == int:
            if parm_double:
                a, b = random.sample(range(self.value_range[0], int(2*self.value_range[1]- self.value_range[0])), 2)
            else:
                a,b = random.sample(range(self.value_range[0], self.value_range[1]), 2)
            return (min(a, b), max(a, b))
        else:
            return None


class HiddenConsole:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class SSH:
    def __init__(self):
        self.connect()

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect('141.223.24.53', username='sun', password='zoemakrso1!')

    def send_file(self, local_path, remote_path):
        with SCPClient(self.ssh.get_transport()) as scp:
            scp.put(local_path, remote_path)


class RandGen:
    def __init__(self, cell_name, worker_num=1, **kwargs):
        self.cell_name = cell_name
        self.worker_num = worker_num
        self.ssh = SSH()
        # self.create_parameters()
        self.params = dict()
        for key, val in kwargs.items():
            param = Parameter(name=key, step=val[0], value_range=val[1], offset_param=None if len(val) == 2 else val[2])
            self.params.update({key: param})

    def execute_command(self, command, debug=False):
        stdin, stdout, stderr = self.ssh.ssh.exec_command(command)
        for _ in stdout.readlines():
            if debug:
                print(_)
            else:
                pass
        for _ in stderr.readlines():
            if debug:
                print(_)
            else:
                pass

    def run(self, iteration=2):
        drc_results = [False] * iteration
        lvs_results = [False] * iteration
        worker = 10
        step = iteration // worker

        # Modify Calibre.run files
        with open("./calibre_drc.run", 'r', encoding='utf-8') as f:
            lines = f.readlines()

        lines[2] = f"LAYOUT PATH \"./{self.cell_name}.calibre.db\"\n"
        lines[3] = f"LAYOUT PRIMARY \"{self.cell_name}\"\n"

        with open("./calibre_drc.run", 'w', encoding='utf-8') as f:
            f.writelines(lines)

        with open("./calibre.run", 'r', encoding='utf-8') as f:
            lines = f.readlines()

        lines[9] = f"SOURCE PRIMARY  \"{self.cell_name}\"\n"
        lines[10] = f"SOURCE PATH     \"./{self.cell_name}.src.net\"\n"
        lines[14] = f"LAYOUT PRIMARY \"{self.cell_name}\"\n"
        lines[15] = f"LAYOUT PATH \"./{self.cell_name}.calibre.db\"\n"

        with open("./calibre.run", 'w', encoding='utf-8') as f:
            f.writelines(lines)

        for i in tqdm(range(step+1)):
            if i == step:
                worker = iteration % worker
            for j in range(worker):
                word = str(j + 1)
                with HiddenConsole():
                    self.create_random(word)
                    # self.create_layout(word)
                    # self.create_schematic(word)
                    self.send_server(word)

            # Run DRC
            commands = [f"source /mnt/sdc/junung/OPUS/Samsung28n/DRC/sourceme.l28lp; cd /mnt/sda/sun/OPUS/ss28; strmin -library '{self.cell_name}_{word}' -strmFile '/mnt/sda/sun/lvs_run/{word}/{self.cell_name}.gds', -attachTechFileOfLib 'cmos28lp' -logFile 'strmIn_{word}.log';"
                    for word in range(1, worker + 1)]
            for cmd in commands:
                self.execute_command(cmd)
            commands2 = [
                f"source /mnt/sdc/junung/OPUS/Samsung28n/DRC/sourceme.l28lp; cd /mnt/sda/sun/OPUS/ss28; strmout -library '{self.cell_name}_{word}' -strmFile '/mnt/sda/sun/lvs_run/{word}/{self.cell_name}.calibre.db' -topCell '{self.cell_name}' -view layout -runDir '/mnt/sda/sun/lvs_run' -logFile 'PIPO.LOG.{self.cell_name}_{word}' -layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'; cd /mnt/sda/sun/lvs_run/{word}; calibre -drc -hier calibre_drc.run"
                for word in range(1, worker + 1)]

            threads = []
            for command in commands2:
                thread = Thread(target=self.execute_command, args=(command,))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
            if i == step:
                drc_results[i * worker:] = list(map(self.retrieve_drc, range(1, worker + 1)))
            else:
                drc_results[i*worker:(i+1)*worker] = list(map(self.retrieve_drc, range(1, worker+1)))

            # Run LVS
            commands = [f"source /mnt/sda/sun/OPUS/ss28/sourceme_xact; cd ./lvs_run/{word}; calibre -lvs -hier calibre.run" for word in range(1, worker+1)]
            threads = []
            for command in commands:
                thread = Thread(target=self.execute_command, args=(command,))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
            # print(i*worker, (i+1)*worker)

            if i == step:
                lvs_results[i * worker:] = list(map(self.retrieve_lvs, range(1, worker + 1)))
            else:
                lvs_results[i*worker:(i+1)*worker] = list(map(self.retrieve_lvs, range(1, worker+1)))

        return drc_results, lvs_results


    def mp_run(self, iteration):
        cpu_ids = [i % 4 for i in range(iteration)]
        with Pool(processes=4) as pool:
            lvs_results = list(tqdm(pool.map(self.run_worker, cpu_ids), total=iteration))


        # word = '' if worker_num == 1 else str(worker_num)
        # for i in range(self.worker_num):
        #     word = str(i+1)
        #     with HiddenConsole():
        #         self.create_layout(word)
        #         self.create_schematic(word)
        #         self.send_server(word)
        #         return self.run_lvs(word)

    def run_worker(self, word='1'):
        with HiddenConsole():
            self.create_layout(word)
            self.create_schematic(word)
            self.send_server(word)
            return self.run_lvs(word)

    # def create_parameters(self, **kwargs):
    #     self.ngate = Parameter('n_gate', 1, [1, 10])
    #     self.pgate = Parameter('n_gate', 1, [1, 10])
    #     self.n_width = Parameter('n_width', 10, [400, 2000])
    #     self.p_width = Parameter('p_width', 10, [400, 2000])
    #     self.length = Parameter('n_length', 10, [20, 100])
    #     self.supply_coy = Parameter('supply_coy', 1, [1, 4])
    #     self.dummy = Parameter('dummy', 1, [0, 1])

    def create_random(self, word='1'):
        # ngate = self.ngate.get_random_value()
        # n_width = self.n_width.get_random_value()
        # length = self.length.get_random_value()
        # pgate = self.pgate.get_random_value()
        # p_width = self.p_width.get_random_value()
        # supply_coy = self.supply_coy.get_random_value()
        # supply_height = n_width + p_width + 100*supply_coy*2 + 600
        # dummy = self.dummy.get_random_value()
        rand_values = dict()
        for key, value in self.params.items():
            if value.offset_param is None:
                rand_values.update({key: value.get_random_value()})
            else:
                rand_values.update({key: value.get_random_value(offset=rand_values[value.offset_param])})
        print(rand_values)

        with HiddenConsole():
            self.create_schematic(params=rand_values, word=word)
            self.create_layout(params=rand_values, word=word)

        # self.create_schematic(word, ngate, n_width, length, pgate, p_width)
        # self.create_layout(word, ngate, n_width, length, pgate, p_width, supply_coy, supply_height, dummy)

    # def create_schematic(self, word='1', ngate=2, n_width=600, length=80, pgate=4, p_width=1000):
    #     nw = n_width*ngate/1000
    #     pw = p_width*pgate/1000
    #     len = length/1000
    #     with open(f'inverter{word}.src.net', 'w') as f:
    #         f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
    #         f.write('.PARAM\n')
    #         f.write('.SUBCKT inverter VDD VIN VOUT VSS\n')
    #         f.write(f'MN0 VOUT VIN VSS VSS slvtnfet w={nw}u l={len}u nf={ngate}.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #         # f.write(f'MN0 VOUT VIN VSS VSS slvtnfet w=1.2u l=0.08u nf=2.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #         f.write(f'MP0 VOUT VIN VDD VDD slvtpfet w={pw}u l={len}u nf={pgate}.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #         # f.write(f'MP0 VOUT VIN VDD VDD slvtpfet w=4.0u l=0.08u nf=4.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #         f.write('.ENDS')

    def create_schematic(self, params, word='1'):
        if self.cell_name == 'Inverter':
            schematic.makeINVSche(word=word, param=params)
        elif self.cell_name == 'ResistorBankCell':
            schematic.makeRBankCellSche(word=word, param=params)
        elif self.cell_name == 'ResistorBank':
            schematic.makeRBankSche(word=word, param=params)
        elif self.cell_name == 'SALatch':
            schematic.makeSALatchSche(word=word, param=params)
        elif self.cell_name == 'SRLatch':
            schematic.makeSRLatchSche(word=word, param=params)
        elif self.cell_name == 'Receiver':
            schematic.makeRXSche(word=word, param=params)

        return None

    def create_layout(self, params, word='1'):
        if self.cell_name == 'Inverter':
            pass
            # inv = inverter_demo_20231202.inverter()
            #     inv._CalculateDesignParameter(n_gate=ngate, n_width=n_width, n_length=length, dummy=dummy, p_gate=pgate, p_width=p_width,
            #                                   p_length=length, supply_coy=supply_coy, supply_height=supply_height)
            #     # inv._CalculateDesignParameter(n_gate=2, n_width=600, n_length=80, dummy=False, p_gate=4, p_width=1000,
            #     #                               p_length=80, supply_coy=2, supply_height=2400)
            #     inv._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=inv._DesignParameter)
            #     with open(f'inverter{word}.gds', 'wb') as f:
            #         gds_stream = inv._CreateGDSStream(inv._DesignParameter['_GDSFile']['_GDSFile'])
            #         gds_stream.write_binary_gds_stream(f)
        elif self.cell_name == 'ResistorBankCell':
            ResistorBank = RB2._ResistorBank(_DesignParameter=None, _Name='ResistorBankCell')
            ResistorBank._CalculateResistorBank(
                                                   _TransmissionGateFinger=params.get('_TransmissionGateFinger'),
                                                   _TransmissionGateChannelWidth=params.get('_TransmissionGateChannelWidth'),
                                                   _TransmissionGateChannelLength=params.get('_TransmissionGateChannelLength'),
                                                   _TransmissionGateNPRatio=params.get('_TransmissionGateNPRatio'),
                                                   _ResistorWidth=params.get('_ResistorWidth'),
                                                   _ResistorLength=params.get('_ResistorLength'),
                                                   _TransmissionGateDummy=True,
                                                   _TransmissionGateVDD2VSSHeight=None,
                                                   _TransmissionGateXVT='SLVT',
                                                   _PowerLine=False,
                                                   _ResistorMetXCO=None,
                                                   _ResistorMetYCO=2,
                                                   _PMOSSubringType=False,
                                                   _PMOSSubringXWidth=None,
                                                   _PMOSSubringYWidth=None,
                                                   _PMOSSubringWidth=170,
                                                   _NMOSSubringType=True,
                                                   _NMOSSubringXWidth=None,
                                                   _NMOSSubringYWidth=None,
                                                   _NMOSSubringWidth=170,
                                                   _TotalSubringType=True,
                                                   _TotalSubringXWidth=None,
                                                   _TotalSubringYWidth=None,
                                                   _TotalSubringWidth=170)
            ResistorBank._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ResistorBank._DesignParameter)
            with open(f'ResistorBankCell{word}.gds', 'wb') as f:
                gds_stream = ResistorBank._CreateGDSStream(ResistorBank._DesignParameter['_GDSFile']['_GDSFile'])
                gds_stream.write_binary_gds_stream(f)

        elif self.cell_name == 'ResistorBank':
            ResistorBank = FRB2._FullResistorBank(_DesignParameter=None, _Name='ResistorBank')
            ResistorBank._CalculateFullResistorBank(
                                                   _XRBNum=params.get('_XRBNum'),
                                                   _YRBNum=params.get('_YRBNum'),
                                                   _TransmissionGateFinger=params.get('_TransmissionGateFinger'),
                                                   _TransmissionGateChannelWidth=params.get('_TransmissionGateChannelWidth'),
                                                   _TransmissionGateChannelLength=params.get('_TransmissionGateChannelLength'),
                                                   _TransmissionGateNPRatio=params.get('_TransmissionGateNPRatio'),
                                                   _ResistorWidth=params.get('_ResistorWidth'),
                                                   _ResistorLength=params.get('_ResistorLength'),
                                                   _TransmissionGateDummy=True,
                                                   _TransmissionGateVDD2VSSHeight=None,
                                                   _TransmissionGateXVT='SLVT',
                                                   _PowerLine=False,
                                                   _InputLine=False,
                                                   _ResistorMetXCO=None,
                                                   _ResistorMetYCO=2,
                                                   _PMOSSubringType=False,
                                                   _PMOSSubringXWidth=None,
                                                   _PMOSSubringYWidth=None,
                                                   _PMOSSubringWidth=170,
                                                   _NMOSSubringType=True,
                                                   _NMOSSubringXWidth=None,
                                                   _NMOSSubringYWidth=None,
                                                   _NMOSSubringWidth=170,
                                                   _TotalSubringType=True,
                                                   _TotalSubringXWidth=None,
                                                   _TotalSubringYWidth=None,
                                                   _TotalSubringWidth=170)
            ResistorBank._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ResistorBank._DesignParameter)
            with open(f'ResistorBank{word}.gds', 'wb') as f:
                gds_stream = ResistorBank._CreateGDSStream(ResistorBank._DesignParameter['_GDSFile']['_GDSFile'])
                gds_stream.write_binary_gds_stream(f)

        elif self.cell_name == 'SALatch':
            SALatch = Slicer_test._Slicer(_DesignParameter=None, _Name='SALatch')
            SALatch._CalculateDesignParameter(_CLKinputPMOSFinger1 = params.get('_CLKinputPMOSFinger1'),
                                            _CLKinputPMOSFinger2 = params.get('_CLKinputPMOSFinger2'),
                                            _PMOSFinger = params.get('_PMOSFinger'),
                                            _PMOSChannelWidth = params.get('_PMOSChannelWidth'),
                                            _DATAinputNMOSFinger = params.get('_DATAinputNMOSFinger'),
                                            _NMOSFinger = params.get('_NMOSFinger'),
                                            _CLKinputNMOSFinger = params.get('_CLKinputNMOSFinger'),
                                            _NMOSChannelWidth = params.get('_NMOSChannelWidth'),
                                            _CLKinputNMOSChannelWidth = params.get('_CLKinputNMOSChannelWidth'),
                                            _ChannelLength = params.get('_ChannelLength'),
                                            _Dummy=True,
                                            _XVT = 'SLVT',
                                            _GuardringWidth = 200,
                                            _Guardring = True,
                                            _SlicerGuardringWidth = 200,
                                            _SlicerGuardring = None,
                                            _NumSupplyCOY = None,
                                            _NumSupplyCOX = None,
                                            _SupplyMet1XWidth = None,
                                            _SupplyMet1YWidth = None,
                                            _VDD2VSSHeight = None,
                                            _NumVIAPoly2Met1COX = None,
                                            _NumVIAPoly2Met1COY = None,
                                            _NumVIAMet12COX = None,
                                            _NumVIAMet12COY = None,
                                            _PowerLine = False)
            SALatch._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SALatch._DesignParameter)
            with open(f'SALatch{word}.gds', 'wb') as f:
                gds_stream = SALatch._CreateGDSStream(SALatch._DesignParameter['_GDSFile']['_GDSFile'])
                gds_stream.write_binary_gds_stream(f)

        elif self.cell_name == 'SRLatch':
            SRLatch = SRLatch_test._SRLatch(_DesignParameter=None, _Name='SRLatch')
            SRLatch._CalculateDesignParameter(_Finger1=params.get('_Finger1'),
                                            _Finger2=params.get('_Finger2'),
                                            _Finger3=params.get('_Finger3'),
                                            _Finger4=params.get('_Finger4'),

                                            _NMOSChannelWidth1=params.get('_RandWidth'),
                                            _NMOSChannelWidth2=params.get('_RandWidth'),
                                            _NMOSChannelWidth3=params.get('_RandWidth'),
                                            _NMOSChannelWidth4=params.get('_RandWidth'),
                                            _NPRatio=params.get('_NPRatio'),
                                            _PMOSChannelWidth1=params.get('_NPRatio') * params.get('_RandWidth'),
                                            _PMOSChannelWidth2=params.get('_NPRatio') * params.get('_RandWidth'),
                                            _PMOSChannelWidth3=params.get('_NPRatio') * params.get('_RandWidth'),
                                            _PMOSChannelWidth4=params.get('_NPRatio') * params.get('_RandWidth'),

                                            _ChannelLength=params.get('_ChannelLength'),

                                            _VDD2VSSHeightAtOneSide=None,
                                            _NumSupplyCoX=None,
                                            _NumSupplyCoY=None,
                                            _Dummy=True,
                                            _XVT='SLVT',
                                            _PowerLine=False)
            SRLatch._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=SRLatch._DesignParameter)
            with open(f'SRLatch{word}.gds', 'wb') as f:
                gds_stream = SRLatch._CreateGDSStream(SRLatch._DesignParameter['_GDSFile']['_GDSFile'])
                gds_stream.write_binary_gds_stream(f)

        elif self.cell_name == 'Receiver':
            Receiver = SlicerandSRLatchwtResistor_test._SlicerandSRLatchwtResistor(_DesignParameter=None, _Name='Receiver')
            Receiver._CalculateDesignParameter(
                #### Resistor Bank
                _XRBNum=params.get('_XRBNum'),
                _YRBNum=params.get('_YRBNum'),
                _TransmissionGateFinger=params.get('_TransmissionGateFinger'),
                _TransmissionGateChannelWidth=params.get('_TransmissionGateChannelWidth'),
                _TransmissionGateChannelLength=params.get('_TransmissionGateChannelLength'),
                _TransmissionGateNPRatio=params.get('_TransmissionGateNPRatio'),
                _ResistorWidth=params.get('_ResistorWidth'),
                _ResistorLength=params.get('_ResistorLength'),
                _TransmissionGateVDD2VSSHeight=None,
                _TransmissionGateXVT='SLVT',
                _TransmissionGateDummy=True,
                _PowerLine=False,
                _InputLine=False,
                _ResistorMetXCO=None,
                _ResistorMetYCO=2,
                _PMOSSubringType=False,
                _PMOSSubringXWidth=None,
                _PMOSSubringYWidth=None,
                _PMOSSubringWidth=170,
                _NMOSSubringType=True,
                _NMOSSubringXWidth=None,
                _NMOSSubringYWidth=None,
                _NMOSSubringWidth=170,
                _TotalSubringType=True,
                _TotalSubringXWidth=None,
                _TotalSubringYWidth=None,
                _TotalSubringWidth=170,
                #### SR Latch
                _SRFinger1=params.get('_SRFinger1'),
                _SRFinger2=params.get('_SRFinger2'),
                _SRFinger3=params.get('_SRFinger3'),
                _SRFinger4=params.get('_SRFinger4'),
                _SRNMOSChannelWidth1=params.get('_SRRandWidth'),
                _SRNMOSChannelWidth2=params.get('_SRRandWidth'),
                _SRNMOSChannelWidth3=params.get('_SRRandWidth'),
                _SRNMOSChannelWidth4=params.get('_SRRandWidth'),
                _SRPMOSChannelWidth1=params.get('_SRNPRatio') * params.get('_SRRandWidth'),
                _SRPMOSChannelWidth2=params.get('_SRNPRatio') * params.get('_SRRandWidth'),
                _SRPMOSChannelWidth3=params.get('_SRNPRatio') * params.get('_SRRandWidth'),
                _SRPMOSChannelWidth4=params.get('_SRNPRatio') * params.get('_SRRandWidth'),
                _SRChannelLength=params.get('_SRChannelLength'),
                _SRVDD2VSSHeightAtOneSide=None,
                _SRDummy=True,
                _SRNumSupplyCoX=None,
                _SRNumSupplyCoY=2,
                _SRSupplyMet1XWidth=None,
                _SRSupplyMet1YWidth=None,
                _SRNumViaPoly2Met1CoX=None,
                _SRNumViaPoly2Met1CoY=None,
                _SRNumViaPMOSMet12Met2CoX=None,
                _SRNumViaPMOSMet12Met2CoY=None,
                _SRNumViaNMOSMet12Met2CoX=None,
                _SRNumViaNMOSMet12Met2CoY=None,
                _SRNumViaPMOSMet22Met3CoX=None,
                _SRNumViaPMOSMet22Met3CoY=None,
                _SRNumViaNMOSMet22Met3CoX=None,
                _SRNumViaNMOSMet22Met3CoY=None,
                _SRXVT='SLVT',
                _SRPowerLine=False,
                #### Slicer
                _SLCLKinputPMOSFinger1=params.get('_SLCLKinputPMOSFinger1'),
                _SLCLKinputPMOSFinger2=params.get('_SLCLKinputPMOSFinger2'),
                _SLPMOSFinger=params.get('_SLPMOSFinger'),
                _SLPMOSChannelWidth=params.get('_SLPMOSChannelWidth'),
                _SLNMOSFinger=params.get('_SLNMOSFinger'),
                _SLDATAinputNMOSFinger=params.get('_SLDATAinputNMOSFinger'),
                _SLNMOSChannelWidth=params.get('_SLNMOSChannelWidth'),
                _SLCLKinputNMOSFinger=params.get('_SLCLKinputNMOSFinger'),
                _SLCLKinputNMOSChannelWidth=params.get('_SLCLKinputNMOSChannelWidth'),
                _SLChannelLength=params.get('_SLChannelLength'),
                _SLDummy=True,
                _SLXVT='SLVT',
                _SLGuardringWidth=200,
                _SLGuardring=True,
                _SLSlicerGuardringWidth=200,
                _SLSlicerGuardring=None,
                _SLNumSupplyCOY=None,
                _SLNumSupplyCOX=None,
                _SLSupplyMet1XWidth=None,
                _SLSupplyMet1YWidth=None,
                _SLVDD2VSSHeight=None,
                _SLNumVIAPoly2Met1COX=None,
                _SLNumVIAPoly2Met1COY=None,
                _SLNumVIAMet12COX=None,
                _SLNumVIAMet12COY=None,
                _SLPowerLine=False,
                #### Time interleaving order
                _NumberofSlicerWithSRLatch=params.get('_N'),
                #### CLK buffer Inverter
                _InvChannelWidth=params.get('_InvChannelWidth'),
                _InvChannelLength=params.get('_InvChannelLength'),
                _InvFinger=params.get('_InvFinger'),
                _InvNPRatio=params.get('_InvNPRatio'),
                _InvVDD2VSSHeight=None,
                _InvDummy=True,
                _InvNumSupplyCoX=None,
                _InvNumSupplyCoY=None,
                _InvSupplyMet1XWidth=None,
                _InvSupplyMet1YWidth=None,
                _InvNumViaPoly2Met1CoX=None,
                _InvNumViaPoly2Met1CoY=None,
                _InvNumViaPMOSMet12Met2CoX=None,
                _InvNumViaPMOSMet12Met2CoY=None,
                _InvNumViaNMOSMet12Met2CoX=None,
                _InvNumViaNMOSMet12Met2CoY=None,
                _InvXVT='SLVT',
                _InvPowerLine=False,
                _SLSRInvSupplyLineX4=False
            )
            Receiver._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Receiver._DesignParameter)
            with open(f'Receiver{word}.gds', 'wb') as f:
                gds_stream = Receiver._CreateGDSStream(Receiver._DesignParameter['_GDSFile']['_GDSFile'])
                gds_stream.write_binary_gds_stream(f)


        return None

    # def create_layout(self, word='1', ngate=2, n_width=600, length=80, pgate=4, p_width=1000, supply_coy=2, supply_height=2400, dummy=0):
    #     inv = inverter_demo_20231202.inverter()
    #     inv._CalculateDesignParameter(n_gate=ngate, n_width=n_width, n_length=length, dummy=dummy, p_gate=pgate, p_width=p_width,
    #                                   p_length=length, supply_coy=supply_coy, supply_height=supply_height)
    #     # inv._CalculateDesignParameter(n_gate=2, n_width=600, n_length=80, dummy=False, p_gate=4, p_width=1000,
    #     #                               p_length=80, supply_coy=2, supply_height=2400)
    #     inv._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=inv._DesignParameter)
    #     with open(f'inverter{word}.gds', 'wb') as f:
    #         gds_stream = inv._CreateGDSStream(inv._DesignParameter['_GDSFile']['_GDSFile'])
    #         gds_stream.write_binary_gds_stream(f)

    def send_server(self, word='1'):
        #check foler exist first
        stdin, stdout, stderr = self.ssh.ssh.exec_command(f"mkdir /mnt/sda/sun/lvs_run/{word}")
        print(stdout.readlines())

        def replace_line_text(file_path, line_number, new_text):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            if 0 < line_number <= len(lines):
                lines[line_number - 1] = new_text + '\n'

            with open(file_path, 'w') as file:
                file.writelines(lines)

        self.ssh.send_file(f'calibre.run', f'/mnt/sda/sun/lvs_run/{word}/calibre.run')
        self.ssh.send_file(f'calibre_drc.run', f'/mnt/sda/sun/lvs_run/{word}/calibre_drc.run')

        self.ssh.send_file(f'{self.cell_name}{word}.src.net', f'/mnt/sda/sun/lvs_run/{word}/{self.cell_name}.src.net')
        self.ssh.send_file(f'{self.cell_name}{word}.gds', f'/mnt/sda/sun/lvs_run/{word}/{self.cell_name}.gds')

    # def run_lvs(self, word='1', wait=True):
    #
    #     stdin, stdout, stderr = self.ssh.ssh.exec_command(f"source /mnt/sda/sun/OPUS/ss28/sourceme_xact; cd ./lvs_run/{word}; calibre -lvs -hier calibre.run")
    #     if wait:
    #         for _ in stdout.readlines():
    #             pass
    #     else:
    #         _ = stdout.readline()

    def retrieve_drc(self, word='1'):
        test = False

        with SCPClient(self.ssh.ssh.get_transport()) as scp:
            scp.get(f'/mnt/sda/sun/lvs_run/{word}/drc_summary.rpt', f'./drc{word}.report')
        with open(f'drc{word}.report', 'r') as f:
            for line in f.readlines()[-2:-1]:
                if line.split()[4] != '0': # TOTAL DRC Results Generated: 0 (0)\n
                    print("DRC FAILED")
                    test = False
                    break
                else:
                    # print("LVS PASSED")
                    test = True
                    break
        if test == False:
            with open(f'drc{word}.report', 'r') as f:
                for i in f.readlines():
                    print(i.replace('\n', ''))
        else:
            stdin, stdout, stderr = self.ssh.ssh.exec_command(f"cd /mnt/sda/sun/lvs_run/correct_DRC; ls")
            count = 0
            for _ in stdout.readlines():
                count += 1
            stdin, stdout, stderr = self.ssh.ssh.exec_command(
                f"rm -rf /mnt/sda/sun/OPUS/ss28/{self.cell_name}_{word}")
            # stdin, stdout, stderr = self.ssh.ssh.exec_command(f"rm -rf /mnt/sda/sun/lvs_run/{word}")
        return test

    def retrieve_lvs(self, word='1'):
        test = False

        with SCPClient(self.ssh.ssh.get_transport()) as scp:
            scp.get(f'/mnt/sda/sun/lvs_run/{word}/lvsprt_ca.lvs', f'./lvs{word}.report')
        with open(f'lvs{word}.report', 'r') as f:
            for i in f.readlines():
                if "INCORRECT" in i:
                    print("LVS FAILED")
                    test = False
                    break
                elif "CORRECT" in i:
                    # print("LVS PASSED")
                    test = True
                    break
        if test == False:
            with open(f'lvs{word}.report', 'r') as f:
                for i in f.readlines():
                    print(i.replace('\n', ''))
        else:
            stdin, stdout, stderr = self.ssh.ssh.exec_command(f"cd /mnt/sda/sun/lvs_run/correct; ls")
            count = 0
            for _ in stdout.readlines():
                count += 1
            stdin, stdout, stderr = self.ssh.ssh.exec_command(f"mv -f /mnt/sda/sun/lvs_run/{word} /mnt/sda/sun/lvs_run/correct/{count}_pass")
            # stdin, stdout, stderr = self.ssh.ssh.exec_command(f"rm -rf /mnt/sda/sun/lvs_run/{word}")
        return test


# randgen = RandGen(cell_name='SALatch',
#                 _CLKinputPMOSFinger1=(1, [1, 15]),
# 		        _CLKinputPMOSFinger2=(1, [1, 15]),
# 		        _PMOSFinger=(1, [1, 15]),
#                 _PMOSChannelWidth=(2, [200, 1050]),
#                 _DATAinputNMOSFinger=(1, [3, 15]),
#                 _NMOSFinger=(1, [1, 15]),
#                 _CLKinputNMOSFinger=(1, [1, 15]),
#                 _NMOSChannelWidth=(2, [350, 1050]),
#                 _CLKinputNMOSChannelWidth=(2, [200, 1050]),
#                 _ChannelLength=(2, [30, 60]))
# randgen = RandGen(cell_name='SRLatch',
#                 _RandWidth=(2, [200, 400]),
# 		        _NPRatio=(1, [2, 3]),
# 		        _Finger1=(1, [1, 15]),
#                 _Finger2=(1, [1, 15]),
#                 _Finger3=(1, [1, 15]),
#                 _Finger4=(1, [1, 15]),
#                 _ChannelLength=(2, [30, 60]))
# randgen = RandGen(cell_name='ResistorBankCell',
#                   _TransmissionGateFinger=(1, [2, 14]),
#                   _TransmissionGateChannelWidth=(2, [200, 400]),
#                   _TransmissionGateChannelLength=(2, [30, 60]),
#                   _TransmissionGateNPRatio=(1, [2, 4]), # output 2 or 3
#                   _ResistorWidth=(2, [1000, 2000]),
#                   _ResistorLength=(2, [100, 1000], "_ResistorWidth"))
# randgen = RandGen(cell_name='ResistorBank',
#                   _XRBNum=(1, [3, 7]),
#                   _YRBNum=(1, [5, 9]),
#                   _TransmissionGateFinger=(1, [2, 14]),
#                   _TransmissionGateChannelWidth=(2, [200, 400]),
#                   _TransmissionGateChannelLength=(2, [30, 60]),
#                   _TransmissionGateNPRatio=(1, [2, 4]), # output 2 or 3
#                   _ResistorWidth=(2, [1000, 2000]),
#                   _ResistorLength=(2, [100, 1000], "_ResistorWidth"))
randgen = RandGen(cell_name='Receiver',
                _XRBNum=(1, [3, 7]),
                _YRBNum=(1, [5, 9]),
                _TransmissionGateFinger=(1, [2, 14]),
                _TransmissionGateChannelWidth=(2, [200, 400]),
                _TransmissionGateChannelLength=(2, [30, 60]),
                _TransmissionGateNPRatio=(1, [2, 4]), # output 2 or 3
                _ResistorWidth=(2, [1000, 2000]),
                _ResistorLength=(2, [100, 1000], "_ResistorWidth"),
                _SRRandWidth=(2, [200, 400]),
                _SRNPRatio=(1, [2, 4]),
                _SRFinger1=(1, [1, 15]),
                _SRFinger2=(1, [1, 15]),
                _SRFinger3=(1, [1, 15]),
                _SRFinger4=(1, [1, 15]),
                _SRChannelLength=(2, [30, 60]),
                _SLCLKinputPMOSFinger1=(1, [1, 15]),
                _SLCLKinputPMOSFinger2=(1, [1, 15]),
                _SLPMOSFinger=(1, [1, 15]),
                _SLPMOSChannelWidth=(2, [200, 1050]),
                _SLNMOSFinger=(1, [1, 15]),
                _SLDATAinputNMOSFinger=(1, [3, 15]),
                _SLNMOSChannelWidth=(2, [350, 1050]),
                _SLCLKinputNMOSFinger=(1, [1, 15]),
                _SLCLKinputNMOSChannelWidth=(2, [200, 1050]),
                _SLChannelLength=(2, [30, 60]),
                _N=(1, [1, 17]), # Time Interleaving Factor
                _InvChannelWidth=(2, [200, 400]),
                _InvChannelLength=(2, [30, 60]),
                _InvFinger=(1, [5, 16]),
                _InvNPRatio=(1, [2, 4])
                  )
drc_result, lvs_result = randgen.run(100)
print(drc_result)
print(lvs_result)
# mp = MultiPool(100)
# mp.run_workers(4)
