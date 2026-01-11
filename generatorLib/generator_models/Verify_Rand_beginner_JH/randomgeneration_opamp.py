import os
import numpy as np

from generatorLib.generator_models.A01_BGR_v2_ import A01_BGR_v2

print("현재 작업 디렉터리:", os.getcwd())
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
import ftplib
from datetime import datetime
import math

import schematic
import personal
# from generatorLib.generator_models import inverter_ajh_v2_2
# from generatorLib.generator_models import CTLE_20240712_test
# from generatorLib.generator_models import CTLE_20250307_test
# from generatorLib.generator_models import CTLE_20250309_test
# from generatorLib.generator_models import CTLE_20250310_test
# from generatorLib.generator_models import CTLE_20250310_test5
from generatorLib.generator_models import B00_amp_v4_using_gui
# from generatorLib.generator_models import inverter_0305_2

# sys.path.append('./generatorLib/generator_models/rx_project')
# from generatorLib.generator_models.rx_project import inverter_demo_20231202

'''BEFORE RUN THIS FILE, check README.md'''

import json  # 맨 위에 import 필요!



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
        self.ssh.connect(personal.hostname, username=personal.username, password=personal.password)

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
        self.current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        with open(f"./Verify_Rand_beginner_JH/Parameters_executed/{self.current_time}.txt", "w") as f:
            pass

    def execute_command(self, command, debug=False):
        stdin, stdout, stderr = self.ssh.ssh.exec_command(command)
        for _ in stdout.readlines():
            if debug:
                print(_)
                # pass
            else:
                pass
        for _ in stderr.readlines():
            if debug:
                print(_)
            else:
                pass
        # self.ssh.ssh.close()

    def run(self, iteration=2):
        drc_results = [False] * iteration
        lvs_results = [False] * iteration
        pex_results = [False] * iteration
        posim_results = [False] * iteration
        worker = 5
        step = iteration // worker + 1

        # Modify DRC runfile
        with open("./Verify_Rand_beginner_JH/calibre_drc.run", 'r', encoding='utf-8') as f:
            lines = f.readlines()

        lines[2] = f"LAYOUT PATH \"./{self.cell_name}.calibre.db\"\n"
        lines[3] = f"LAYOUT PRIMARY \"{self.cell_name}\"\n"
        lines[20] = f'INCLUDE "{personal.TECHDIR}/DRC/invx1_lvt_cdk/cmos28lp.drc.cal"'
        lines.append(f"\n")

        with open("./Verify_Rand_beginner_JH/calibre_drc.run", 'w', encoding='utf-8') as f:
            f.writelines(lines)

        # LVS & PEX runfile
        with open("./Verify_Rand_beginner_JH/_calibre.run_", "r", encoding='utf-8') as f:
            lines = f.readlines()

        lines[10] = f'LAYOUT PATH  "./{self.cell_name}.calibre.db"\n'
        lines[11] = f'LAYOUT PRIMARY "{self.cell_name}"\n'
        lines[14] = f'SOURCE PATH "./{self.cell_name}.src.net"\n'
        lines[15] = f'SOURCE PRIMARY "{self.cell_name}"\n'
        lines[18] = f'MASK SVDB DIRECTORY "svdb" QUERY XRC\n' # IXF NXF SLPH 추가?
        lines[20] = f'LVS REPORT "{self.cell_name}.lvs.report"\n'
        lines[22] = f'PEX NETLIST "{self.cell_name}.pex.netlist" ELDO 1 SOURCENAMES \n' # HSPICE 1 SOURCENAMES RCNAMED
        lines[23] = f'PEX REPORT "{self.cell_name}.pex.report" SOURCENAMES\n'
        lines[51] = f'source "{personal.TECHDIR}/PEX/template/calibre.run"'

        with open("./Verify_Rand_beginner_JH/_calibre.run_", "w", encoding='utf-8') as f:
            f.writelines(lines)

        # same as 'for i in range(step+1)'. tqdm for progress bar
        for i in tqdm(range(1,step+1), file=sys.stdout):
            # single parallel work('worker' works) DRC&LVS
            # i = 1,...,step
            if i == step:
                worker = iteration % worker
            if worker == 0:
                break
            for j in range(worker):
                # cds.lib 수정
                commands = [f"cd {personal.TECHDIR}; sed -i '/DEFINE {self.cell_name}_{word} /d' cds.lib" for word in range(1, worker + 1)]
                for cmd in commands:
                    self.execute_command(cmd)

                stdin, stdout, stderr = self.ssh.ssh.exec_command(f"rm -rf {personal.TECHDIR}/{self.cell_name}_{j+1}")
                word = str(j + 1)# int,float to string
                with HiddenConsole():
                    self.create_random(i, word)
                    self.send_server(word)

            # Run DRC
            commands = [(f"source {personal.TECHDIR}/setup.cshrc; cd {personal.TECHDIR}; strmin -library '{self.cell_name}_{word}' "
                         f"-strmFile '{personal.RUNDIR}/{word}/{self.cell_name}.gds', -attachTechFileOfLib 'cmos28lp' -logFile 'strmIn_{word}.log';")
                    for word in range(1, worker + 1)]
            for cmd in commands:
                self.execute_command(cmd)

            commands2 = [
                (f"source {personal.TECHDIR}/setup.cshrc; cd {personal.TECHDIR}; strmout -library '{self.cell_name}_{word}' -strmFile '{personal.RUNDIR}/{word}/{self.cell_name}.calibre.db' "
                 f"-topCell '{self.cell_name}' -view layout -runDir '{personal.RUNDIR}' -logFile 'PIPO.LOG.{self.cell_name}_{word}' "
                 f"-layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' "
                 f"-objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' "
                 f"-case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'; cd {personal.RUNDIR}/{word}; calibre -drc -hier calibre_drc.run")
                for word in range(1, worker + 1)]

            threads = []
            for command in commands2:
                # thread = Thread(target=self.execute_command, args=(command, True,))
                thread = Thread(target=self.execute_command, args=(command,))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

            print(f"\n\nStart SET{i} DRC")
            if i == step:
                drc_results[-worker:] = list(map(self.retrieve_drc, range(1, worker+1)))
            else:
                drc_results[(i-1)*worker:i*worker] = list(map(self.retrieve_drc,range(1, worker+1)))
            print(f"End SET{i} DRC")

            # Run LVS & PEX
            #print(f"\nStart SET{i} LVS & PEX")
            print(f"\nStart SET{i} LVS")
            # commands = [(f"source {personal.TECHDIR}/setup.cshrc; cd {personal.RUNDIR}/{word}; "
            #              f"calibre -lvs -hier -spice ./svdb/{self.cell_name}.sp -nowait -turbo _calibre.run_; "
            #              f"calibre -xact -3d -pdb -rcc -turbo -nowait _calibre.run_; calibre -xact -fmt -all -nowait _calibre.run_") for word in range(1, worker+1)]

            commands = [(f"source {personal.TECHDIR}/setup.cshrc; cd {personal.RUNDIR}/{word}; "
                         f"calibre -lvs -hier -spice ./svdb/{self.cell_name}.sp -nowait -turbo _calibre.run_; ") for word in range(1, worker+1)]
            # commands = [(f"source {personal.TECHDIR}/setup.cshrc; cd {personal.RUNDIR}/{word}; "
            #              f"calibre -lvs -hier -spice ./svdb/{self.cell_name}.sp -nowait -turbo _calibre.run_; "
            #              f"calibre -xact -3d -pdb -rcc -turbo -nowait _calibre.run_; calibre -xact -fmt hspice -all -nowait _calibre.run_")
            #             for word in range(1, worker + 1)]
            threads = []
            for command in commands:
                thread = Thread(target=self.execute_command, args=(command, ))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

            if i == step:
                lvs_results[-worker:] = list(map(self.retrieve_lvs, range(1, worker+1)))
            else:
                lvs_results[(i-1)*worker:i*worker] = list(map(self.retrieve_lvs, range(1, worker+1)))

            print("\n", end="")
            # if i == step:
            #     pex_results[-worker:] = list(map(self.retrieve_pex, range(1, worker + 1)))
            # else:
            #     pex_results[(i - 1) * worker:i * worker] = list(map(self.retrieve_pex, range(1, worker + 1)))
            # print(f"End SET{i} LVS & PEX")
            print(f"End SET{i} LVS")
            # # Run Posim
            # print(f"\nStart SET{i} Posim")
            #
            # # add oceanScript
            # commands = [(f"cd {personal.RUNDIR}/{word}; cp -u {personal.TECHDIR}/{self.cell_name}_oceanScript.ocn {self.cell_name}_oceanScript.ocn; "
            #              f"sed -i '3s,.*,resultsDir( \"{personal.RUNDIR}/{word}/ADEresult\"),' {self.cell_name}_oceanScript.ocn") for word in range(1, worker+1)]
            # for cmd in commands:
            #     self.execute_command(cmd)
            #
            # # commands = [(f"cd {personal.RUNDIR}/{word}; sed -i '$s,.*,x{self.cell_name} VIN VOUT VSS VDD {self.cell_name},g' {self.cell_name}.pex.netlist; "
            # #              f"sed -i '7s,.*,.subckt {self.cell_name}  VIN VOUT VSS VDD,' {self.cell_name}.pex.netlist; "
            # #              f"sed -i 's,{self.cell_name}\.pex\.netlist\.pex,{personal.RUNDIR}/{word}/{self.cell_name}\.pex\.netlist\.pex,g' {self.cell_name}.pex.netlist; "
            # #              f"sed -i 's,{self.cell_name}\.pex\.netlist\.{self.cell_name}\.pxi,{personal.RUNDIR}/{word}/{self.cell_name}\.pex\.netlist\.{self.cell_name}\.pxi,g' {self.cell_name}.pex.netlist") for word in range(1, worker+1)]
            #
            # commands = [(
            #                 f"cd {personal.RUNDIR}/{word}; sed -i '$s,.*,x{self.cell_name} VSS Voutp VDD Voutn Vinn IDS Vinp {self.cell_name},g' {self.cell_name}.pex.netlist; "
            #                 f"sed -i '7s,.*,.subckt {self.cell_name} VSS Voutp VDD Voutn Vinn IDS Vinp,' {self.cell_name}.pex.netlist; "
            #                 f"sed -i 's,{self.cell_name}\.pex\.netlist\.pex,{personal.RUNDIR}/{word}/{self.cell_name}\.pex\.netlist\.pex,g' {self.cell_name}.pex.netlist; "
            #                 f"sed -i 's,{self.cell_name}\.pex\.netlist\.{self.cell_name}\.pxi,{personal.RUNDIR}/{word}/{self.cell_name}\.pex\.netlist\.{self.cell_name}\.pxi,g' {self.cell_name}.pex.netlist; "
            #                 f"sed -i 's/\\(opppcres\\) \\([0-9.]\\+\\)/\\1 R=\\2/g' {self.cell_name}.pex.netlist"
            #                 )
            #             for word in range(1, worker + 1)]
            #
            # threads = []
            # for command in commands:
            #     thread = Thread(target=self.execute_command, args=(command, ))
            #     threads.append(thread)
            #     thread.start()
            # for thread in threads:
            #     thread.join()
            #
            # # commands = [f'source {personal.TECHDIR}/setup.cshrc; ocean -nograph -restore {personal.RUNDIR}/{word}/{self.cell_name}_oceanScript.ocn' for word in range(1, worker+1)]
            # commands = [
            #     f'source {personal.TECHDIR}/setup.cshrc; ocean -nograph -restore {personal.RUNDIR}/{word}/{self.cell_name}_oceanScript.ocn'
            #     for word in range(1, worker + 1)]
            # for cmd in commands:
            #     self.execute_command(cmd)
            #
            # if i == step:
            #     posim_results[-worker:] = list(map(self.retrieve_posim, range(1, worker + 1)))
            # else:
            #     posim_results[(i - 1) * worker:i * worker] = list(map(self.retrieve_posim, range(1, worker + 1)))
            #
            # print(f"End SET{i} Posim\n")

        # return drc_results, lvs_results, pex_results, posim_results
        # return drc_results, lvs_results, pex_results
        return drc_results, lvs_results
        # return drc_results

    # def mp_run(self, iteration):
    #     cpu_ids = [i % 4 for i in range(iteration)]
    #     with Pool(processes=4) as pool:
    #         lvs_results = list(tqdm(pool.map(self.run_worker, cpu_ids), total=iteration))

        # word = '' if worker_num == 1 else str(worker_num)
        # for i in range(self.worker_num):
        #     word = str(i+1)
        #     with HiddenConsole():
        #         self.create_layout(word)
        #         self.create_schematic(word)
        #         self.send_server(word)
        #         return self.run_lvs(word)

    # def run_worker(self, word='1'):
    #     with HiddenConsole():
    #         self.create_layout(word)
    #         self.create_schematic(word)
    #         self.send_server(word)
    #         return self.run_lvs(word)

    def create_random(self, rand_set=1, word='1'):
        rand_values = dict()
        for key, value in self.params.items():
            if value.offset_param is None:
                rand_values.update({key: value.get_random_value()})
            else:
                rand_values.update({key: value.get_random_value(offset=rand_values[value.offset_param])})
        text_data = f"iteration {rand_set}-{word}\n"
        for key, value in rand_values.items():
            text_data += f"{key}: {value}\n"

        with open(f"./Verify_Rand_beginner_JH/Parameters_executed/{self.current_time}.txt", "a") as f:
            f.write(text_data + "\n")

        with HiddenConsole():
            self.create_schematic(params=rand_values, word=word)
            self.create_layout(params=rand_values, word=word)

    def create_schematic(self, params, word='1'):
        if self.cell_name == 'inverter':
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
        elif self.cell_name == 'CTLE':
            schematic.makeCTLESche(word=word, param=params)
        elif self.cell_name == 'vpnp':
            schematic.makevpnpSche(word=word, param=params)
        elif self.cell_name == 'opamp':
            schematic.makeopampSche(word=word, param=params)
        return None

    def create_layout(self, params, word='1'):
        # if self.cell_name == 'inverter':
        if self.cell_name == 'opamp':
            # inv = inverter_ajh_v2_2.inverter(_DesignParameter=None, _Name='inverter')
            # inv = inverter_0305_2.inverter(_DesignParameter=None, _Name='inverter')
            # CTLE = CTLE_20240712_test._CTLE_20240712_test(_DesignParameter=None, _Name='CTLE')
            # CTLE = CTLE_20250307_test._CTLE_20250307_test(_DesignParameter=None, _Name='CTLE')
            # CTLE = CTLE_20250309_test._CTLE_20250309_test(_DesignParameter=None, _Name='CTLE')
            # CTLE = CTLE_20250310_test._CTLE_20250310_test(_DesignParameter=None, _Name='CTLE')
            B00_amp_v2 = B00_amp_v4_using_gui.B00_amp_v2(_DesignParameter=None, _Name='opamp')
            # inv._CalculateDesignParameter(n_gate=params.get('n_gate'), n_width=params.get('n_width'), n_length=params.get('n_length'), dummy='True',
            #                               p_gate=params.get('p_gate'), p_width=params.get('p_width'), p_length=params.get('p_length'), supply_coy=params.get('supply_coy'))
            # B00_amp_v2._CalculateDesignParameter(W=params.get('W'))
            # finger_N1_pre = params.get('finger_N1')
            # finger_N2_pre = params.get('finger_N2')
            # finger_P1_pre = params.get('finger_P1')
            # finger_P5_pre = params.get('finger_P5')
            # finger_N5_pre = params.get('finger_N5')
            # finger_N4_pre = params.get('finger_N4')
            # finger_P3_pre = params.get('finger_P3')
            # finger_P4_pre = params.get('finger_P4')
            # fingerA = ((((finger_P1_pre + finger_P5_pre) - finger_N2_pre) - finger_N5_pre) + 1)
            # fingerB = ((finger_N4_pre - finger_N5_pre) + 1)
            # fingerC = (((((finger_P1_pre + finger_P3_pre) + finger_P4_pre) + 2) - finger_N2_pre) - finger_N5_pre)
            # finger_N_Dummy2 = max(2, fingerA, fingerB, fingerC)
            # finger_P_Dummy1 = ((((finger_N2_pre + finger_N5_pre) - finger_P1_pre) - finger_P5_pre) + finger_N_Dummy2)
            # finger_N_Dummy1 = ((finger_N_Dummy2 + finger_N5_pre) - finger_N4_pre)
            # finger_P_Dummy2 = ((((((finger_N2_pre + finger_N5_pre) + finger_N_Dummy2) - finger_P1_pre) - finger_P3_pre) - finger_P4_pre) - 1)
            #
            # if (finger_P_Dummy2 + finger_P1_pre) % 2 == 0 and finger_P3_pre % 2 == 0:
            #     finger_P3_pre += 1
            #
            # if (finger_P_Dummy2 + finger_P1_pre) % 2 == 1 and finger_P3_pre % 2 == 1:
            #     finger_P3_pre += 1

            B00_amp_v2._CalculateDesignParameter(finger_N1=params.get('finger_N1'), finger_N2=params.get('finger_N2'), finger_P1=params.get('finger_P1'),  finger_P5=params.get('finger_P5'), finger_N5=params.get('finger_N5'), finger_N4=params.get('finger_N4'), finger_P3=params.get('finger_P3'),
                      finger_P4=params.get('finger_P4'),W_N=700,L=params.get('L'),Dummy=True,XVT='RVT',W_P=700,Guad_via=2,res_compensation_W=params.get('res_compensation_W'),res_compensation_L=params.get('res_compensation_L'),res_compensation_series=params.get('res_compensation_series'),NumofGate_res_com=params.get('NumofGate_res_com'),NumofRX_res_com=params.get('NumofRX_res_com'),L_cap=params.get('L_cap'),W_cap=params.get('W_cap') )
            # inv._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=inv._DesignParameter)
            B00_amp_v2._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=B00_amp_v2._DesignParameter)
            # with open(f'./inverter/inverter{word}.gds', 'wb') as f:
            #     gds_stream = inv._CreateGDSStream(inv._DesignParameter['_GDSFile']['_GDSFile'])
            #     gds_stream.write_binary_gds_stream(f)
            with open(f'./Verify_Rand_beginner_JH/opamp/opamp{word}.gds', 'wb') as f:
                gds_stream = B00_amp_v2._CreateGDSStream(B00_amp_v2._DesignParameter['_GDSFile']['_GDSFile'])
                gds_stream.write_binary_gds_stream(f)

        # Add here to run with another IP

        return None

    def send_server(self, word='1'):
        #check foler exist first
        # -p : make parent folder if not exist
        stdin, stdout, stderr = self.ssh.ssh.exec_command(f"mkdir -p {personal.RUNDIR}/{word}")
        print(stdout.readlines())

        def replace_line_text(file_path, line_number, new_text):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            if 0 < line_number <= len(lines):
                lines[line_number - 1] = new_text + '\n'

            with open(file_path, 'w') as file:
                file.writelines(lines)

        # self.ssh.send_file(f'./Verify_Rand_beginner_JH/calibre.run', f'{personal.RUNDIR}/{word}/calibre.run')
        self.ssh.send_file(f'./Verify_Rand_beginner_JH/calibre_drc.run', f'{personal.RUNDIR}/{word}/calibre_drc.run')
        self.ssh.send_file(f'./Verify_Rand_beginner_JH/_calibre.run_', f'{personal.RUNDIR}/{word}/_calibre.run_')

        self.ssh.send_file(f'./Verify_Rand_beginner_JH/{self.cell_name}/{self.cell_name}{word}.src.net', f'{personal.RUNDIR}/{word}/{self.cell_name}.src.net')
        self.ssh.send_file(f'./Verify_Rand_beginner_JH/{self.cell_name}/{self.cell_name}{word}.gds', f'{personal.RUNDIR}/{word}/{self.cell_name}.gds')

    def retrieve_drc(self, word='1'):
        test = False

        with SCPClient(self.ssh.ssh.get_transport()) as scp:
            scp.get(f'{personal.RUNDIR}/{word}/drc_summary.rpt', f'./Verify_Rand_beginner_JH/report_DRC/drc{word}.report')
        with open(f'./Verify_Rand_beginner_JH/report_DRC/drc{word}.report', 'r') as f:
            for line in f.readlines()[-2:-1]:
                if line.split()[4] != '0': # TOTAL DRC Results Generated: 0 (0)\n
                    print(f"DRC{word} FAILED. {line.split()[4]} errors occurred")
                    test = False
                    sys.exit()
                    break
                else:
                    print(f"DRC{word} PASSED.")
                    test = True
                    break
        return test

    def retrieve_lvs(self, word='1'):
        test = False

        with SCPClient(self.ssh.ssh.get_transport()) as scp:
            scp.get(f'{personal.RUNDIR}/{word}/{self.cell_name}.lvs.report', f'./Verify_Rand_beginner_JH/report_LVS/lvs{word}.report')
        with open(f'./Verify_Rand_beginner_JH/report_LVS/lvs{word}.report', 'r') as f:
            for i in f.readlines():
                if "INCORRECT" in i:
                    print(f"LVS{word} FAILED. errors occurred")
                    test = False
                    sys.exit()
                    break
                elif "CORRECT" in i:
                    print(f"LVS{word} PASSED.")
                    test = True
                    break
        return test

    def retrieve_pex(self, word='1'):
        test = False

        with SCPClient(self.ssh.ssh.get_transport()) as scp:
            scp.get(f'{personal.RUNDIR}/{word}/{self.cell_name}.pex.report', f'./Verify_Rand_beginner_JH/report_PEX/pex{word}.report')
        if os.stat(f'./Verify_Rand_beginner_JH/report_PEX/pex{word}.report').st_size != 0:
            with open(f'./Verify_Rand_beginner_JH/report_PEX/pex{word}.report') as f:
                line = f.readlines()[12]
                print(f'PEX file Creation Time : {line.split()[3]} {line.split()[4]} {line.split()[5]}')
            test = True
        else:
            print('PEX error!!!')

        return test


    def retrieve_posim(self, word='1'):
        test = False

        with SCPClient(self.ssh.ssh.get_transport()) as scp:
            # scp.get(f'{personal.RUNDIR}/{word}/VIN_tran', f'./report_posim/VIN_tran_{word}.report')
            # scp.get(f'{personal.RUNDIR}/{word}/VOUT_tran', f'./report_posim/VOUT_tran_{word}.report')
            # scp.get(f'{personal.RUNDIR}/{word}/VIN_dc', f'./report_posim/VIN_dc_{word}.report')
            # scp.get(f'{personal.RUNDIR}/{word}/VOUT_dc', f'./report_posim/VOUT_dc_{word}.report')

            # scp.get(f'{personal.RUNDIR}/{word}/graph_CTLE_AC', f'./report_posim/graph_CTLE_AC_{word}.report')
            # scp.get(f'{personal.RUNDIR}/{word}/peak_gain', f'./report_posim/peak_gain_{word}.report')
            # scp.get(f'{personal.RUNDIR}/{word}/DC_gain', f'./report_posim/DC_gain_{word}.report')
            # scp.get(f'{personal.RUNDIR}/{word}/peak_freq', f'./report_posim/peak_freq_{word}.report')
            # scp.get(f'{personal.RUNDIR}/{word}/peak_freq_dBscale', f'./report_posim/peak_freq_dBscale_{word}.report')

            scp.get(f'{personal.RUNDIR}/{word}/Voutp_AC', f'./report_posim/Voutp_AC_{word}.report')
            scp.get(f'{personal.RUNDIR}/{word}/Voutn_AC', f'./report_posim/Voutn_AC_{word}.report')

            scp.get(f'{personal.RUNDIR}/{word}/Vinp_AC', f'./report_posim/Vinp_AC_{word}.report')
            scp.get(f'{personal.RUNDIR}/{word}/Vinn_AC', f'./report_posim/Vinn_AC_{word}.report')

        # 데이터 읽어오기 함수
        def read_ac_data(filename):
            freq, value = [], []
            with open(filename, 'r') as f:
                for line in f:
                    cols = line.split()
                    if len(cols) < 2:  # 데이터가 2개 미만이면 무시
                        continue
                    try:
                        freq.append(float(cols[0]))
                        value.append(float(cols[1]))
                    except ValueError:
                        continue  # 숫자로 변환할 수 없으면 무시
            return np.array(freq), np.array(value)

        # Voutp_AC, Voutn_AC 데이터 로드
        freq, Voutp = read_ac_data(f'./report_posim/Voutp_AC_{word}.report')
        _, Voutn = read_ac_data(f'./report_posim/Voutn_AC_{word}.report')

        # Differential gain 계산 (Voutp - Voutn)
        diff_gain = Voutp - Voutn
        diff_gain_dB = 20 * np.log10(np.abs(diff_gain))

        # 1. peak_gain = ymax(diff_gain_dB)
        peak_gain = np.max(diff_gain_dB)

        # 2. DC_gain = diff_gain_dB의 첫 번째 값
        DC_gain = diff_gain_dB[0] if len(diff_gain_dB) > 0 else None

        # 3. peak_freq = 10**(xmax(diff_gain_dB))
        peak_freq_index = np.argmax(diff_gain_dB)
        peak_freq = freq[peak_freq_index]

        # 4. peak_freq_dBscale = xmax(diff_gain_dB)
        peak_freq_dBscale = np.max(np.log10(peak_freq))  # peak_freq에 로그 적용

        # 값이 정상적으로 로드되었는지 확인
        if None in [peak_gain, DC_gain, peak_freq, peak_freq_dBscale]:
            print(f"posim {word} ERROR: 데이터 파일에서 값을 읽어오지 못함\n")
            return test

        test = True

        # 공학 표기법 변환 + 소수점 5자리까지 출력
        peak_gain = "{:.5f}".format(peak_gain)
        DC_gain = "{:.5f}".format(DC_gain)
        # peak_freq = "{:.5f}".format(peak_freq)
        peak_freq_dBscale = "{:.2f}".format(peak_freq_dBscale)


        # # 공학 표기법 변환
        # peak_gain = EngineeringFormatter.engineering_format(peak_gain)
        # DC_gain = EngineeringFormatter.engineering_format(DC_gain)
        peak_freq = EngineeringFormatter.engineering_format(peak_freq)
        # peak_freq_dBscale = EngineeringFormatter.engineering_format(peak_freq_dBscale)



        # 결과 출력
        print(f'posim {word}')
        print(f'Peak Gain = {peak_gain}')
        print(f'DC Gain = {DC_gain}')
        print(f'Peak Frequency = {peak_freq} Hz')
        print(f'Peak Frequency (dB scale) = {peak_freq_dBscale} dB\n')

        # 파일에 저장
        os.makedirs("./Parameters_executed", exist_ok=True)
        with open(f"./Parameters_executed/{self.current_time}.txt", "a") as f:
            f.write(f'#{word}\n')
            f.write(f'Peak Gain = {peak_gain}\n')
            f.write(f'DC Gain = {DC_gain}\n')
            f.write(f'Peak Frequency = {peak_freq} Hz\n')
            f.write(f'Peak Frequency (dB scale) = {peak_freq_dBscale} dB\n\n')

        return test




        # # 값 초기화
        # peak_gain, DC_gain, peak_freq, peak_freq_dBscale = None, None, None, None
        #
        # # 파일에서 데이터 읽어오기
        # def read_value_from_file(filename):
        #     with open(filename, 'r') as f:
        #         for line in f:
        #             try:
        #                 return float(line.strip())  # 첫 번째 유효한 숫자를 가져옴
        #             except ValueError:
        #                 continue
        #     return None  # 값이 없으면 None 반환
        #
        # peak_gain = read_value_from_file(f'./report_posim/peak_gain_{word}.report')
        # DC_gain = read_value_from_file(f'./report_posim/DC_gain_{word}.report')
        # peak_freq = read_value_from_file(f'./report_posim/peak_freq_{word}.report')
        # peak_freq_dBscale = read_value_from_file(f'./report_posim/peak_freq_dBscale_{word}.report')
        #
        # # 값이 정상적으로 로드되었는지 확인
        # if None in [peak_gain, DC_gain, peak_freq, peak_freq_dBscale]:
        #     print(f"posim {word} ERROR: 데이터 파일에서 값을 읽어오지 못함\n")
        #     return test
        #
        # test = True
        #
        # # 값을 공학 표기법으로 변환
        # peak_gain = EngineeringFormatter.engineering_format(peak_gain)
        # DC_gain = EngineeringFormatter.engineering_format(DC_gain)
        # peak_freq = EngineeringFormatter.engineering_format(peak_freq)
        # peak_freq_dBscale = EngineeringFormatter.engineering_format(peak_freq_dBscale)
        #
        # # 결과 출력
        # print(f'posim {word}')
        # print(f'Peak Gain = {peak_gain}')
        # print(f'DC Gain = {DC_gain}')
        # print(f'Peak Frequency = {peak_freq} Hz')
        # print(f'Peak Frequency (dB scale) = {peak_freq_dBscale} Hz\n')
        #
        # # 파일에 저장
        # os.makedirs("./Parameters_executed", exist_ok=True)
        # with open(f"./Parameters_executed/{self.current_time}.txt", "a") as f:
        #     f.write(f'#{word}\n')
        #     f.write(f'Peak Gain = {peak_gain}\n')
        #     f.write(f'DC Gain = {DC_gain}\n')
        #     f.write(f'Peak Frequency = {peak_freq} Hz\n')
        #     f.write(f'Peak Frequency (dB scale) = {peak_freq_dBscale} Hz\n\n')
        #
        # return test


        #
        # with open(f'report_posim/VOUT_dc_{word}.report', 'r') as f:
        #     for line in f.readlines()[3:]:
        #         if float(line.split()[1]) <= 0.5:
        #             dc_center = "{:.2f}".format(float(line.split()[0]))
        #             break
        #
        # with open(f'report_posim/VOUT_tran_{word}.report', 'r') as f:
        #     chk = 0
        #     for i, line in enumerate(f):
        #         if i>=3:
        #             if chk==0 and float(line.split()[1]) >= 0.2:
        #                 t_rise_low = float(line.split()[0])
        #                 chk = 1
        #             elif chk==1 and float(line.split()[1]) >= 0.5:
        #                 t_rise_cen = float(line.split()[0])
        #                 chk = 2
        #             elif chk==2 and float(line.split()[1]) >= 0.8:
        #                 t_rise_high = float(line.split()[0])
        #                 chk = 3
        #
        #             elif chk == 3 and float(line.split()[1]) <= 0.8:
        #                 t_fall_high = float(line.split()[0])
        #                 chk = 4
        #             elif chk == 4 and float(line.split()[1]) <= 0.5:
        #                 t_fall_cen = float(line.split()[0])
        #                 chk = 5
        #             elif chk == 5 and float(line.split()[1]) <= 0.2:
        #                 t_fall_low = float(line.split()[0])
        #                 chk = 6
        #                 break
        #
        # if chk != 6:
        #     print(f"posim {word} ERROR\n")
        #     return test

        # test = True
        # t_rise = EngineeringFormatter.engineering_format(t_rise_high - t_rise_low)
        # t_fall = EngineeringFormatter.engineering_format(t_fall_low - t_fall_high)
        # t_phl = EngineeringFormatter.engineering_format(t_rise_cen - 5.05e-10)
        # t_plh = EngineeringFormatter.engineering_format(t_fall_cen - 10.05e-10)
        #
        # print(f'posim {word}')
        # print(f'DC center = {dc_center}V')
        # print(f't_rise = {t_rise}s')
        # print(f't_fall = {t_fall}s')
        # print(f't_prop_h2l = {t_phl}s')
        # print(f't_prop_l2h = {t_plh}s\n')
        #
        # with open(f"./Parameters_executed/{self.current_time}.txt", "a") as f:
        #     f.write(f'#{word}\n')
        #     f.write(f'DC center = {dc_center}V\n')
        #     f.write(f't_rise = {t_rise}s\n')
        #     f.write(f't_fall = {t_fall}s\n')
        #     f.write(f't_prop_h2l = {t_phl}s\n')
        #     f.write(f't_prop_l2h = {t_plh}s\n\n')
        #
        # return test

class EngineeringFormatter:
    @staticmethod
    def engineering_format(number):
        suffixes = ['f', 'p', 'n', 'u', 'm', '', 'k', 'M', 'G', 'T', 'P', 'E']
        if number == 0:
            return '0'

        magnitude = 5
        while abs(number) >= 1000 and magnitude < len(suffixes) - 1:
            magnitude += 1
            number /= 1000.0
        while abs(number) <= 1e-3 and magnitude > 0:
            magnitude -= 1
            number *= 1000.0
        if abs(number) < 1:
            magnitude -= 1
            number *= 1000.0

        return '{:.1f}{}'.format(number, suffixes[magnitude])


def save_params_to_json(randgen: RandGen, filename="params.json"):
    param_dict = dict()
    for key, param in randgen.params.items():
        param_dict[key] = {
            "step": param.step,
            "value_range": param.value_range,
            "offset_param": param.offset_param
        }

    with open(filename, "w") as f:
        json.dump(param_dict, f, indent=4)


if __name__=="__main__":

    # randgen = RandGen(cell_name='inverter',
    #                   n_gate=(1,[1,10]), n_width=(10,[500,1200]), n_length=(10,[30,100]),
    #                   p_gate=(1,[1,10]), p_width=(10,[500,1200]), p_length=(10,[30,100]),
    #                   supply_coy=(1,[1,5])
    #                   )

    randgen = RandGen(cell_name='opamp',
                      finger_N1=(1,[2,11]), finger_N2=(1,[1,11]), finger_P1=(1,[1,11]),  finger_P5=(1,[1,11]), finger_N5=(1,[1,11]), finger_N4=(1,[1,11]),
                      finger_P4=(1,[1,11]), L=(10,[30,40]), finger_P3=(1,[1,21]), NumofGate_res_com=(1,[1,11]),NumofRX_res_com=(1,[1,4]), res_compensation_series=(1,[1,5]),L_cap=(100,[1300,3000]),W_cap=(100,[1300,3000]),
                      res_compensation_L=(500,(500,3000)),res_compensation_W=(500,(500,2000))

                      )

    # recomend L is small -> finger_N5 > 1
    # save_params_to_json(randgen)
    #
    # with open("params.json", "r") as f:
    #     raw_params = json.load(f)
    #
    # inputparams = dict()
    # for key, val in raw_params.items():
    #     step = val["step"]
    #     value_range = val["value_range"]
    #     offset_param = val["offset_param"]
    #
    #     if offset_param is None:
    #         inputparams[key] = (step, value_range)
    #     else:
    #         inputparams[key] = (step, value_range, offset_param)
    #
    # randgen = RandGen(cell_name='CTLE', **inputparams)

    #drc_result, lvs_result, pex_result, posim_result = randgen.run(10)
    #drc_result, lvs_result, pex_result = randgen.run(10)
    drc_result, lvs_result = randgen.run(100)
    #drc_result= randgen.run(1)
    print(drc_result.count(False), "DRC errors")
    print(lvs_result.count(False), "LVS errors")
    #print(pex_result.count(False), "PEX errors")
    # print(posim_result.count(False), "posim errors")
