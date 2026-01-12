import os
import numpy as np



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
# from KJH91_Projects.generatorLib.generator_models import B00_amp_v2_
# from generatorLib.generator_models import inverter_0305_2
# from KJH91_Projects.generatorLib.generator_models import BGR_V3_using_gui
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A55_TIA

# sys.path.append('./generatorLib/generator_models/rx_project')
# from generatorLib.generator_models.rx_project import inverter_demo_20231202

'''BEFORE RUN THIS FILE, check README.md'''

import json  # 맨 위에 import 필요!


class Parameter:
    def __init__(self, name: str, step=None, value_range=None, offset_param=None):
        self.name = name
        self.step = step
        self.value_range = value_range
        self.offset_param = offset_param

        # print(f"Initializing Parameter: {name}, step={step}, value_range={value_range}")

        if step is None:
            return

        if step is False:
            if not isinstance(value_range, list):
                raise ValueError(f"Candidate list must be list for {name}: {value_range}")
            return

        if isinstance(step, (int, float)):
            if step < 0:
                raise ValueError(f"Invalid step value for {name}: {step}")
            return

        raise ValueError(f"Invalid step type for {name}: {step}")

    def get_random_value(self, offset=0):
        if self.step is None:
            return self.value_range

            # 후보 리스트 랜덤 선택 (step == False)
        if self.step is False:
            random.seed(os.urandom(8))
            return random.choice(self.value_range)

            # 복사/offset (step == 0)
        if self.step == 0:
            return self.value_range[0] + offset

            # 범위 랜덤 (step > 0)
        random.seed(os.urandom(8))
        lo, hi = self.value_range[0], self.value_range[1]

        if isinstance(lo, int) and isinstance(hi, int):
            return random.randrange(lo, hi, int(self.step)) + offset
        else:
            return random.uniform(float(lo), float(hi)) + offset

        # except Exception as e:
        #     print(f"[ERROR] Error in get_random_value for {self.name}: {e}")
        #     raise
# class Parameter:
#     def __init__(self, name: str, step: int or float, value_range: list, offset_param=None):
#         self.name = name
#         self.step = step
#         self.value_range = value_range
#         self.offset_param = offset_param
#
#     def get_random_value(self, parm_double=False, offset=0):
#         try:
#             if self.step == 0 :
#                 return self.value_range[0] + offset
#             random.seed(os.urandom(8))
#             if type(self.value_range[0]) == int and type(self.value_range[1]) == int:
#                 if parm_double:
#                     return random.randrange(self.value_range[0], int(2*self.value_range[1]-self.value_range[0]), self.step) + offset
#                 else:
#                     return random.randrange(self.value_range[0], self.value_range[1], self.step) + offset
#             else:
#                 if parm_double:
#                     return random.uniform(self.value_range[0], 2*self.value_range[1]-self.value_range[0]) + offset
#                 else:
#                     return random.uniform(self.value_range[0], self.value_range[1]) + offset
#         except:
#             print(self.name)
#             print(self.step)
#             print(self.value_range)
#
#
# class RangeParameter(Parameter):
#     def __init__(self, names: tuple, step: int or float, value_range: list):
#         super().__init__(names, step, value_range)
#         self.names = names
#
#     def get_random_value(self, parm_double=False):
#         random.seed(os.urandom(8))
#         if type(self.value_range[0]) == int and type(self.value_range[1]) == int:
#             if parm_double:
#                 a, b = random.sample(range(self.value_range[0], int(2*self.value_range[1]- self.value_range[0])), 2)
#             else:
#                 a,b = random.sample(range(self.value_range[0], self.value_range[1]), 2)
#             return (min(a, b), max(a, b))
#         else:
#             return None


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
        self.ssh.connect(personal.hostname, username=personal.username, password=personal.password,port=personal.port)

    def send_file(self, local_path, remote_path):
        try:
            with SCPClient(self.ssh.get_transport()) as scp:
                scp.put(local_path, remote_path)
            print(f"File sent successfully: {local_path} -> {remote_path}")
        except Exception as e:
            print(f"Failed to send file: {local_path} -> {remote_path}")
            print(f"Error: {e}")

from threading import Lock
class RandGen:
    def __init__(self, cell_name, worker_num=1, **kwargs):
        # self.cell_name = cell_name
        # self.worker_num = worker_num
        # self.ssh = SSH()
        # # self.create_parameters()
        # self.params = dict()
        # for key, val in kwargs.items():
        #     param = Parameter(name=key, step=val[0], value_range=val[1], offset_param=None if len(val) == 2 else val[2])
        #     self.params.update({key: param})
        self.cell_name = cell_name
        self.worker_num = worker_num
        self.ssh = SSH()
        self.lock = Lock()  # 스레드 안전성을 위한 Lock
        self.params = dict()
        self.current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        os.makedirs("./Parameters_executed", exist_ok=True)

        # # # kwargs 처리
        # for key, val in kwargs.items():
        #     # 1. 단일 값 처리 (bool, str, int, float, NoneType 포함)
        #     if not isinstance(val, tuple):
        #         param = Parameter(name=key, value_range=val)
        #     else:
        #         # 2. 랜덤 후보 처리 (False, [...])
        #         if isinstance(val[0], bool) and not val[0]:
        #             param = Parameter(name=key, step=False, value_range=val[1])
        #         # 3. (step, [low, high]) 처리
        #         elif len(val) == 2 and isinstance(val[1], list):
        #             param = Parameter(name=key, step=val[0], value_range=val[1])
        #         else:
        #             raise ValueError(f"Invalid parameter format for {key}: {val}")
        #     self.params.update({key: param})

        for key, val in kwargs.items():

            # 기본: 고정값
            is_random = False

            if isinstance(val, (tuple, list)):
                # 1) 후보 랜덤: (False, [candidates])
                if len(val) == 2 and isinstance(val[0], bool) and val[0] is False and isinstance(val[1], (list, tuple)):
                    param = Parameter(name=key, step=False, value_range=list(val[1]))
                    is_random = True

                # 2) 범위 랜덤: (step, [low, high])
                elif len(val) == 2 and isinstance(val[0], (int, float)) and isinstance(val[1], (list, tuple)):
                    # low/high 둘 다 있는 경우만 "범위 랜덤"으로 인정
                    if len(val[1]) == 2 and all(isinstance(x, (int, float)) for x in val[1]):
                        param = Parameter(name=key, step=val[0], value_range=list(val[1]))
                        is_random = True

                # 3) 복사/오프셋: (step, range, "ref_key")
                elif len(val) == 3 and isinstance(val[0], (int, float)) and isinstance(val[1],
                                                                                       (list, tuple)) and isinstance(
                        val[2], str):
                    param = Parameter(name=key, step=val[0], value_range=list(val[1]), offset_param=val[2])
                    is_random = True

            # 랜덤으로 확정되지 않았으면 = 고정값(리스트 포함)으로 처리
            if not is_random:
                param = Parameter(name=key, step=None, value_range=val)

            self.params[key] = param

        self.current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        with open(rf"C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\Parameters_executed\{self.current_time}.txt", "w") as f:
            pass

    def execute_command(self, command, debug=False):
        stdin, stdout, stderr = self.ssh.ssh.exec_command(command)

        out_b = stdout.read()
        err_b = stderr.read()
        rc = stdout.channel.recv_exit_status()

        if debug:
            out = out_b.decode("utf-8", errors="replace")
            err = err_b.decode("utf-8", errors="replace")
            if out: print(out)
            if err: print(err)

        return rc

    # def execute_command(self, command, debug=False):
    #     stdin, stdout, stderr = self.ssh.ssh.exec_command(command)
    #     for _ in stdout.readlines():
    #         if debug:
    #             print(_)
    #             # pass
    #         else:
    #             pass
    #     for _ in stderr.readlines():
    #         if debug:
    #             print(_)
    #         else:
    #             pass
    #     # self.ssh.ssh.close()

    # def execute_command(self, command, debug=False):
    #     stdin, stdout, stderr = self.ssh.ssh.exec_command(command)
    #
    #     if debug:
    #         out = stdout.read().decode("utf-8", errors="replace")
    #         err = stderr.read().decode("utf-8", errors="replace")
    #         if out: print(out)
    #         if err: print(err)
    #     else:
    #         # 출력 읽지 말고 "끝날 때까지"만 기다리기
    #         stdout.channel.recv_exit_status()

    def run(self, iteration=2):
        drc_results = [False] * iteration
        lvs_results = [False] * iteration
        # pex_results = [False] * iteration
        # posim_results = [False] * iteration
        worker = 5
        step = iteration // worker + 1

        # Modify DRC runfile
        # with open(rf"C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\calibre_drc.run", 'r', encoding='utf-8') as f:
        #     lines = f.readlines()
        with open(rf"C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\_cmos28lp.drc.cal_", 'r', encoding='utf-8') as f:
            lines = f.readlines()

        lines[2] = f"LAYOUT PATH \"./{self.cell_name}.calibre.db\"\n"
        lines[3] = f"LAYOUT PRIMARY \"{self.cell_name}\"\n"
        # lines[20] = f'INCLUDE "{personal.TECHDIR}/DRC/invx1_lvt_cdk/cmos28lp.drc.cal"'
        lines.append(f"\n")

        with open(rf"C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\_cmos28lp.drc.cal_", 'w', encoding='utf-8') as f:
            f.writelines(lines)

        # LVS & PEX runfile
        with open(rf"C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\_calibre.run_", "r", encoding='utf-8') as f:
            lines = f.readlines()
        # with open(rf"C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\calibre_drc.run", 'w', encoding='utf-8') as f:
        #     f.writelines(lines)
        #
        # # LVS & PEX runfile
        # with open(rf"C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\_calibre.run_", "r", encoding='utf-8') as f:
        #     lines = f.readlines()

        lines[10] = f'LAYOUT PATH  "./{self.cell_name}.calibre.db"\n'
        lines[11] = f'LAYOUT PRIMARY "{self.cell_name}"\n'
        lines[14] = f'SOURCE PATH "./{self.cell_name}.src.net"\n'
        lines[15] = f'SOURCE PRIMARY "{self.cell_name}"\n'
        lines[18] = f'MASK SVDB DIRECTORY "svdb" QUERY XRC\n' # IXF NXF SLPH 추가?
        lines[20] = f'LVS REPORT "{self.cell_name}.lvs.report"\n'
        lines[22] = f'PEX NETLIST "{self.cell_name}.pex.netlist" ELDO 1 SOURCENAMES \n' # HSPICE 1 SOURCENAMES RCNAMED
        lines[23] = f'PEX REPORT "{self.cell_name}.pex.report" SOURCENAMES\n'
        lines[51] = f'source "/tools/PDK/ss28lpp_rf/PEX/template/calibre.run"'
        # lines[51] = f'source "{personal.TECHDIR}/PEX/template/calibre.run"'

        # with open(rf"C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\_calibre.run_", "w", encoding='utf-8') as f:
        #     f.writelines(lines)
        # with open("_calibre.run_", "w", encoding='utf-8') as f:
        #     f.writelines(lines)
        calibre_run_local = rf"C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\_calibre.run_"
        with open(calibre_run_local, "w", encoding="utf-8") as f:
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

            # durian 서버의 ss28lpp_rf
            commands2 = [
                (
                    f"source {personal.TECHDIR}/setup.cshrc; cd {personal.TECHDIR}; strmout -library '{self.cell_name}_{word}' -strmFile '{personal.RUNDIR}/{word}/{self.cell_name}.calibre.db' "
                    f"-topCell '{self.cell_name}' -view layout -runDir '{personal.RUNDIR}' -logFile 'PIPO.LOG.{self.cell_name}_{word}' "
                    f"-layerMap '/tools/PDK/ss28lpp_rf/Device/LNR28LPP_CDS_S00-V1.4.6.1/CDS/oa/cmos28lp_tech_7U1x_2T8x_1UTM_LB/cmos28lp_tech.layermap' "
                    f"-objectMap '/tools/PDK/ss28lpp_rf/Device/LNR28LPP_CDS_S00-V1.4.6.1/CDS/oa/cmos28lp_tech_7U1x_2T8x_1UTM_LB/cmos28lp_tech.objectmap' "
                    f"-case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'; cd {personal.RUNDIR}/{word}; calibre -drc -hier _cmos28lp.drc.cal_")
                for word in range(1, worker + 1)]





            # peach 서버의 ss28
            # commands2 = [
            #     (f"source {personal.TECHDIR}/setup.cshrc; cd {personal.TECHDIR}; strmout -library '{self.cell_name}_{word}' -strmFile '{personal.RUNDIR}/{word}/{self.cell_name}.calibre.db' "
            #      f"-topCell '{self.cell_name}' -view layout -runDir '{personal.RUNDIR}' -logFile 'PIPO.LOG.{self.cell_name}_{word}' "
            #      f"-layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' "
            #      f"-objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' "
            #      f"-case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'; cd {personal.RUNDIR}/{word}; calibre -turbo -drc -hier calibre_drc.run")
            #     for word in range(1, worker + 1)]

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

            # 사용하던 것
            commands = [(f"source {personal.TECHDIR}/setup.cshrc; cd {personal.RUNDIR}/{word}; "
                         f"calibre -lvs -hier -spice ./svdb/{self.cell_name}.sp -nowait -turbo _calibre.run_; ") for word in range(1, worker+1)]

            # commands = [(f"source {personal.TECHDIR}/setup.cshrc; cd {personal.RUNDIR}/{word}; "
            #              f"calibre -lvs -hier -turbo _calibre.run_ > calibre_lvs.log 2>&1; ") for word in range(1, worker+1)]

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
        # rand_values = dict()
        # shared_cache = {}
        #
        # for key, p in self.params.items():
        #     # 1) 의존/복사 파라미터 (offset_param이 있을 때)
        #     if getattr(p, "offset_param", None) is not None:
        #         ref = p.offset_param
        #         rand_values[key] = p.get_random_value(offset=rand_values[ref])
        #         continue
        #
        #     # 2) 공유 랜덤(같은 rd 객체면 동일 값)
        #     token = getattr(p, "_share_token", None)
        #     if token is not None:
        #         if token in shared_cache:
        #             rand_values[key] = shared_cache[token]
        #         else:
        #             v = p.get_random_value()
        #             shared_cache[token] = v
        #             rand_values[key] = v
        #     else:
        #         # 3) 일반 (고정값/일반 랜덤)
        #         rand_values[key] = p.get_random_value()
        rand_values = dict()
        print("Starting random value generation...")  # 시작 로그

        for key, value in self.params.items():
            try:
                # 디버깅: 초기 입력값 출력
                print(f"Key: {key}, Initial Range: {value.value_range} (Type: {type(value.value_range)})")

                if value.offset_param is None:
                    random_value = value.get_random_value()
                    # 디버깅: 선택된 랜덤 값과 초기 입력값 출력
                    print(f"Key: {key}, Random Value Selected: {random_value} (Type: {type(random_value)})")
                    rand_values.update({key: random_value})
                else:
                    random_value = value.get_random_value(offset=rand_values[value.offset_param])
                    # 디버깅: 선택된 랜덤 값과 초기 입력값 출력 (Offset 사용)
                    print(f"Key: {key}, Random Value with Offset: {random_value} (Type: {type(random_value)})")
                    print(
                        f"Key: {key}, Offset Base Value: {rand_values[value.offset_param]} (For Offset Parameter: {value.offset_param})")
                    rand_values.update({key: random_value})

            except Exception as e:
                # 단일 값 처리 중 에러 디버깅
                print(f"[ERROR] Failed to process parameter {key}: {e}")
                print(f"Initial Value Range: {value.value_range} (Type: {type(value.value_range)})")
                raise

        # 디버깅 출력: 전체 rand_values 확인
        print("Generated rand_values:")
        for key, val in rand_values.items():
            print(f"{key}: {val} (Type: {type(val)})")


        text_data = f"iteration {rand_set}-{word}\n"
        for key, value in rand_values.items():
            text_data += f"{key}: {value}\n"

        with open(rf"C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\Parameters_executed\{self.current_time}.txt", "a") as f:
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
        elif self.cell_name == 'BGR':
            schematic.makeBGRSche(word=word, param=params)
        elif self.cell_name == '_2stageamp':
            schematic.make_2stageampSche(word=word, param=params)
        elif self.cell_name == 'TIA':
            schematic.makeTIASche(word=word, param=params)
        return None

    def create_layout(self, params, word='1'):
        # if self.cell_name == 'inverter':
        if self.cell_name == 'TIA':
            # inv = inverter_ajh_v2_2.inverter(_DesignParameter=None, _Name='inverter')
            # inv = inverter_0305_2.inverter(_DesignParameter=None, _Name='inverter')
            # CTLE = CTLE_20240712_test._CTLE_20240712_test(_DesignParameter=None, _Name='CTLE')
            # CTLE = CTLE_20250307_test._CTLE_20250307_test(_DesignParameter=None, _Name='CTLE')
            # CTLE = CTLE_20250309_test._CTLE_20250309_test(_DesignParameter=None, _Name='CTLE')
            # CTLE = CTLE_20250310_test._CTLE_20250310_test(_DesignParameter=None, _Name='CTLE')
            TIA = A55_TIA._TIA_YCH(_DesignParameter=None, _Name='TIA')
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

            TIA._CalculateDesignParameter(
                # PMOS
                _op1_Tr0_PMOSNumberofGate=params.get('_op1_Tr0_PMOSNumberofGate'),
                _op1_Tr0_PMOSChannelWidth=params.get('_op1_Tr0_PMOSChannelWidth'),
                _op1_Tr0_PMOSChannellength=params.get('_op1_Tr0_PMOSChannellength'),
                _op1_Tr0_PMOSGateSpacing=params.get('_op1_Tr0_PMOSGateSpacing'),
                _op1_Tr0_PMOSSDWidth	= params.get('_op1_Tr0_PMOSSDWidth'),
                _op1_Tr0_PMOSXVT			= params.get('_op1_Tr0_PMOSXVT'),
                _op1_Tr0_PMOSPCCrit			= params.get('_op1_Tr0_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr0_PMOSSource_Via_TF= params.get('_op1_Tr0_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr0_PMOSDrain_Via_TF= params.get('_op1_Tr0_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr0_PMOSDummy= params.get('_op1_Tr0_PMOSDummy')  , # TF
                # if _PMOSDummy == True
                _op1_Tr0_PMOSDummy_length = params.get('_op1_Tr0_PMOSDummy_length'), # None/Value
                _op1_Tr0_PMOSDummy_placement = params.get('_op1_Tr0_PMOSDummy_placement'), # None/Up/Dn/

                # PMOS
                _op1_Tr1_PMOSNumberofGate=params.get('_op1_Tr1_PMOSNumberofGate'),
                _op1_Tr1_PMOSChannelWidth=params.get('_op1_Tr1_PMOSChannelWidth'),
                _op1_Tr1_PMOSChannellength=params.get('_op1_Tr1_PMOSChannellength'),
                _op1_Tr1_PMOSGateSpacing	= params.get('_op1_Tr1_PMOSGateSpacing'),
                _op1_Tr1_PMOSSDWidth			= params.get('_op1_Tr1_PMOSSDWidth'),
                _op1_Tr1_PMOSXVT				= params.get('_op1_Tr1_PMOSXVT'),
                _op1_Tr1_PMOSPCCrit				= params.get('_op1_Tr1_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr1_PMOSSource_Via_TF = params.get('_op1_Tr1_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr1_PMOSDrain_Via_TF = params.get('_op1_Tr1_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr1_PMOSDummy = params.get('_op1_Tr1_PMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr1_PMOSDummy_length = params.get('_op1_Tr1_PMOSDummy_length'), # None/Value
                _op1_Tr1_PMOSDummy_placement = params.get('_op1_Tr1_PMOSDummy_placement'), # None/'Up'/'Dn'/

                # PMOS
                _op1_Tr2_PMOSNumberofGate=params.get('_op1_Tr2_PMOSNumberofGate'),
                _op1_Tr2_PMOSChannelWidth=params.get('_op1_Tr2_PMOSChannelWidth'),
                _op1_Tr2_PMOSChannellength=params.get('_op1_Tr2_PMOSChannellength'),
                _op1_Tr2_PMOSGateSpacing	= params.get('_op1_Tr2_PMOSGateSpacing'),
                _op1_Tr2_PMOSSDWidth			= params.get('_op1_Tr2_PMOSSDWidth'),
                _op1_Tr2_PMOSXVT				= params.get('_op1_Tr2_PMOSXVT'),
                _op1_Tr2_PMOSPCCrit				= params.get('_op1_Tr2_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr2_PMOSSource_Via_TF = params.get('_op1_Tr2_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr2_PMOSDrain_Via_TF = params.get('_op1_Tr2_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr2_PMOSDummy = params.get('_op1_Tr2_PMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr2_PMOSDummy_length = params.get('_op1_Tr2_PMOSDummy_length'), # None/Value
                _op1_Tr2_PMOSDummy_placement = params.get('_op1_Tr2_PMOSDummy_placement'), # None/Up/Dn/

                # PMOS
                _op1_Tr3_PMOSNumberofGate=params.get('_op1_Tr3_PMOSNumberofGate'),
                _op1_Tr3_PMOSChannelWidth=params.get('_op1_Tr3_PMOSChannelWidth'),
                _op1_Tr3_PMOSChannellength=params.get('_op1_Tr3_PMOSChannellength'),
                _op1_Tr3_PMOSGateSpacing	= params.get('_op1_Tr3_PMOSGateSpacing'),
                _op1_Tr3_PMOSSDWidth			= params.get('_op1_Tr3_PMOSSDWidth'),
                _op1_Tr3_PMOSXVT				= params.get('_op1_Tr3_PMOSXVT'),
                _op1_Tr3_PMOSPCCrit				= params.get('_op1_Tr3_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr3_PMOSSource_Via_TF = params.get('_op1_Tr3_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr3_PMOSDrain_Via_TF = params.get('_op1_Tr3_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr3_PMOSDummy = params.get('_op1_Tr3_PMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr3_PMOSDummy_length = params.get('_op1_Tr3_PMOSDummy_length'), # None/Value
                _op1_Tr3_PMOSDummy_placement = params.get('_op1_Tr3_PMOSDummy_placement'), # None/Up/Dn/

                # PMOS
                _op1_Tr4_PMOSNumberofGate	= params.get('_op1_Tr4_PMOSNumberofGate'),
                _op1_Tr4_PMOSChannelWidth	= params.get('_op1_Tr4_PMOSChannelWidth'),
                _op1_Tr4_PMOSChannellength	= params.get('_op1_Tr4_PMOSChannellength'),
                _op1_Tr4_PMOSGateSpacing		= params.get('_op1_Tr4_PMOSGateSpacing'),
                _op1_Tr4_PMOSSDWidth			= params.get('_op1_Tr4_PMOSSDWidth'),
                _op1_Tr4_PMOSXVT				= params.get('_op1_Tr4_PMOSXVT'),
                _op1_Tr4_PMOSPCCrit				= params.get('_op1_Tr4_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr4_PMOSSource_Via_TF = params.get('_op1_Tr4_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr4_PMOSDrain_Via_TF = params.get('_op1_Tr4_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr4_PMOSDummy = params.get('_op1_Tr4_PMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr4_PMOSDummy_length = params.get('_op1_Tr4_PMOSDummy_length'), # None/Value
                _op1_Tr4_PMOSDummy_placement = params.get('_op1_Tr4_PMOSDummy_placement'), # None/Up/Dn/

                # NMOS Tr0
                _op1_Tr0_NMOSNumberofGate=params.get('_op1_Tr0_NMOSNumberofGate'),
                _op1_Tr0_NMOSChannelWidth=params.get('_op1_Tr0_NMOSChannelWidth'),
                _op1_Tr0_NMOSChannellength=params.get('_op1_Tr0_NMOSChannellength'),
                _op1_Tr0_NMOSGateSpacing=params.get('_op1_Tr0_NMOSGateSpacing'),
                _op1_Tr0_NMOSSDWidth	= params.get('_op1_Tr0_NMOSSDWidth'),
                _op1_Tr0_NMOSXVT			= params.get('_op1_Tr0_NMOSXVT'),
                _op1_Tr0_NMOSPCCrit			= params.get('_op1_Tr0_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr0_NMOSSource_Via_TF= params.get('_op1_Tr0_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr0_NMOSDrain_Via_TF= params.get('_op1_Tr0_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr0_NMOSDummy= params.get('_op1_Tr0_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr0_NMOSDummy_length = params.get('_op1_Tr0_NMOSDummy_length'), # None/Value
                _op1_Tr0_NMOSDummy_placement = params.get('_op1_Tr0_NMOSDummy_placement'), # None/'Up'/'Dn'/

                # NMOS Tr0
                _op1_Tr1_NMOSNumberofGate=params.get('_op1_Tr1_NMOSNumberofGate'),
                _op1_Tr1_NMOSChannelWidth=params.get('_op1_Tr1_NMOSChannelWidth'),
                _op1_Tr1_NMOSChannellength=params.get('_op1_Tr1_NMOSChannellength'),
                _op1_Tr1_NMOSGateSpacing	= params.get('_op1_Tr1_NMOSGateSpacing'),
                _op1_Tr1_NMOSSDWidth			= params.get('_op1_Tr1_NMOSSDWidth'),
                _op1_Tr1_NMOSXVT				= params.get('_op1_Tr1_NMOSXVT'),
                _op1_Tr1_NMOSPCCrit				= params.get('_op1_Tr1_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr1_NMOSSource_Via_TF = params.get('_op1_Tr1_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr1_NMOSDrain_Via_TF = params.get('_op1_Tr1_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr1_NMOSDummy = params.get('_op1_Tr1_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr1_NMOSDummy_length = params.get('_op1_Tr1_NMOSDummy_length'), # None/Value
                _op1_Tr1_NMOSDummy_placement = params.get('_op1_Tr1_NMOSDummy_placement'), # None/'Up'/'Dn'/

                # NMOS
                _op1_Tr2_NMOSNumberofGate=params.get('_op1_Tr2_NMOSNumberofGate'),
                _op1_Tr2_NMOSChannelWidth=params.get('_op1_Tr2_NMOSChannelWidth'),
                _op1_Tr2_NMOSChannellength=params.get('_op1_Tr2_NMOSChannellength'),
                _op1_Tr2_NMOSGateSpacing=params.get('_op1_Tr2_NMOSGateSpacing'),
                _op1_Tr2_NMOSSDWidth	= params.get('_op1_Tr2_NMOSSDWidth'),
                _op1_Tr2_NMOSXVT			= params.get('_op1_Tr2_NMOSXVT'),
                _op1_Tr2_NMOSPCCrit			= params.get('_op1_Tr2_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr2_NMOSSource_Via_TF= params.get('_op1_Tr2_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr2_NMOSDrain_Via_TF= params.get('_op1_Tr2_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr2_NMOSDummy= params.get('_op1_Tr2_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr2_NMOSDummy_length = params.get('_op1_Tr2_NMOSDummy_length'), # None/Value
                _op1_Tr2_NMOSDummy_placement = params.get('_op1_Tr2_NMOSDummy_placement'), # None/'Up'/'Dn'/

                # NMOS
                _op1_Tr3_NMOSNumberofGate=params.get('_op1_Tr3_NMOSNumberofGate'),
                _op1_Tr3_NMOSChannelWidth=params.get('_op1_Tr3_NMOSChannelWidth'),
                _op1_Tr3_NMOSChannellength=params.get('_op1_Tr3_NMOSChannellength'),
                _op1_Tr3_NMOSGateSpacing	= params.get('_op1_Tr3_NMOSGateSpacing'),
                _op1_Tr3_NMOSSDWidth			= params.get('_op1_Tr3_NMOSSDWidth'),
                _op1_Tr3_NMOSXVT				= params.get('_op1_Tr3_NMOSXVT'),
                _op1_Tr3_NMOSPCCrit				= params.get('_op1_Tr3_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr3_NMOSSource_Via_TF = params.get('_op1_Tr3_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr3_NMOSDrain_Via_TF = params.get('_op1_Tr3_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr3_NMOSDummy = params.get('_op1_Tr3_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr3_NMOSDummy_length = params.get('_op1_Tr3_NMOSDummy_length'), # None/Value
                _op1_Tr3_NMOSDummy_placement = params.get('_op1_Tr3_NMOSDummy_placement'), # None/'Up'/'Dn'/

                # NMOS Tr0
                _op1_Tr4_NMOSNumberofGate=params.get('_op1_Tr4_NMOSNumberofGate'),
                _op1_Tr4_NMOSChannelWidth=params.get('_op1_Tr4_NMOSChannelWidth'),
                _op1_Tr4_NMOSChannellength=params.get('_op1_Tr4_NMOSChannellength'),
                _op1_Tr4_NMOSGateSpacing	= params.get('_op1_Tr4_NMOSGateSpacing'),
                _op1_Tr4_NMOSSDWidth			= params.get('_op1_Tr4_NMOSSDWidth'),
                _op1_Tr4_NMOSXVT				= params.get('_op1_Tr4_NMOSXVT'),
                _op1_Tr4_NMOSPCCrit				= params.get('_op1_Tr4_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op1_Tr4_NMOSSource_Via_TF = params.get('_op1_Tr4_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op1_Tr4_NMOSDrain_Via_TF = params.get('_op1_Tr4_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op1_Tr4_NMOSDummy = params.get('_op1_Tr4_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op1_Tr4_NMOSDummy_length = params.get('_op1_Tr4_NMOSDummy_length'), # None/Value
                _op1_Tr4_NMOSDummy_placement = params.get('_op1_Tr4_NMOSDummy_placement'), # None/'Up'/'Dn'/

                _op1_NumContTop_P1P2P4 = params.get('_op1_NumContTop_P1P2P4'),
                _op1_NumContBottom_P1P2P4 = params.get('_op1_NumContBottom_P1P2P4'),
                _op1_NumContLeft_P1P2P4 = params.get('_op1_NumContLeft_P1P2P4'),
                _op1_NumContRight_P1P2P4 = params.get('_op1_NumContRight_P1P2P4'),

                # N body ring(P0P3)
                _op1_NumContTop_P0P3=params.get('_op1_NumContTop_P0P3'),
                _op1_NumContLeft_P0P3=params.get('_op1_NumContLeft_P0P3'),
                _op1_NumContRight_P0P3=params.get('_op1_NumContRight_P0P3'),

                # P body ring
                _op1_NumContTop_Pbody=params.get('_op1_NumContTop_Pbody'),
                _op1_NumContBottom_Pbody=params.get('_op1_NumContBottom_Pbody'),
                _op1_NumContLeft_Pbody=params.get('_op1_NumContLeft_Pbody'),
                _op1_NumContRight_Pbody=params.get('_op1_NumContRight_Pbody'),

                # Res0
                _op1_ResWidth_res0=params.get('_op1_ResWidth_res0'),
                _op1_ResLength_res0=params.get('_op1_ResLength_res0'),
                _op1_CONUMX_res0=params.get('_op1_CONUMX_res0'),
                _op1_CONUMY_res0=params.get('_op1_CONUMY_res0'),
                _op1_SeriesStripes_res0=params.get('_op1_SeriesStripes_res0'),
                _op1_ParallelStripes_res0=params.get('_op1_ParallelStripes_res0'),

                # Res0
                _op1_ResWidth_res1=params.get('_op1_ResWidth_res1'),
                _op1_ResLength_res1=params.get('_op1_ResLength_res1'),
                _op1_CONUMX_res1=params.get('_op1_CONUMX_res1'),
                _op1_CONUMY_res1=params.get('_op1_CONUMY_res1'),
                _op1_SeriesStripes_res1=params.get('_op1_SeriesStripes_res1'),
                _op1_ParallelStripes_res1=params.get('_op1_ParallelStripes_res1'),

                # Cap0
                _op1_Length_cap0=params.get('_op1_Length_cap0'),
                _op1_LayoutOption_cap0=params.get('_op1_LayoutOption_cap0'),
                _op1_NumFigPair_cap0=params.get('_op1_NumFigPair_cap0'),

                _op1_Array_cap0=params.get('_op1_Array_cap0'),  # number: 1xnumber
                _op1_Cbot_Ctop_metalwidth_cap0=params.get('_op1_Cbot_Ctop_metalwidth_cap0'),  # number

                # Cap1
                _op1_Length_cap1=params.get('_op1_Length_cap1'),
                _op1_LayoutOption_cap1=params.get('_op1_LayoutOption_cap1'),
                _op1_NumFigPair_cap1=params.get('_op1_NumFigPair_cap1'),

                _op1_Array_cap1=params.get('_op1_Array_cap1'),  # number: 1xnumber
                _op1_Cbot_Ctop_metalwidth_cap1=params.get('_op1_Cbot_Ctop_metalwidth_cap1'),  # number

                # PMOS
                _op2_Tr0_PMOSNumberofGate=params.get('_op2_Tr0_PMOSNumberofGate'),
                _op2_Tr0_PMOSChannelWidth=params.get('_op2_Tr0_PMOSChannelWidth'),
                _op2_Tr0_PMOSChannellength=params.get('_op2_Tr0_PMOSChannellength'),
                _op2_Tr0_PMOSGateSpacing=params.get('_op2_Tr0_PMOSGateSpacing'),
                _op2_Tr0_PMOSSDWidth=params.get('_op2_Tr0_PMOSSDWidth'),
                _op2_Tr0_PMOSXVT	= params.get('_op2_Tr0_PMOSXVT'),
                _op2_Tr0_PMOSPCCrit		= params.get('_op2_Tr0_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr0_PMOSSource_Via_TF= params.get('_op2_Tr0_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr0_PMOSDrain_Via_TF= params.get('_op2_Tr0_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr0_PMOSDummy= params.get('_op2_Tr0_PMOSDummy')  , # TF
                # if _PMOSDummy == True
                _op2_Tr0_PMOSDummy_length = params.get('_op2_Tr0_PMOSDummy_length'), # None/Value
                _op2_Tr0_PMOSDummy_placement = params.get('_op2_Tr0_PMOSDummy_placement'), # None/Up/Dn/

                # PMOS
                _op2_Tr1_PMOSNumberofGate=params.get('_op2_Tr1_PMOSNumberofGate'),
                _op2_Tr1_PMOSChannelWidth=params.get('_op2_Tr1_PMOSChannelWidth'),
                _op2_Tr1_PMOSChannellength=params.get('_op2_Tr1_PMOSChannellength'),
                _op2_Tr1_PMOSGateSpacing	= params.get('_op2_Tr1_PMOSGateSpacing'),
                _op2_Tr1_PMOSSDWidth			= params.get('_op2_Tr1_PMOSSDWidth'),
                _op2_Tr1_PMOSXVT				= params.get('_op2_Tr1_PMOSXVT'),
                _op2_Tr1_PMOSPCCrit				= params.get('_op2_Tr1_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr1_PMOSSource_Via_TF = params.get('_op2_Tr1_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr1_PMOSDrain_Via_TF = params.get('_op2_Tr1_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr1_PMOSDummy = params.get('_op2_Tr1_PMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr1_PMOSDummy_length = params.get('_op2_Tr1_PMOSDummy_length'), # None/Value
                _op2_Tr1_PMOSDummy_placement = params.get('_op2_Tr1_PMOSDummy_placement'), # None/'Up'/'Dn'/

                # PMOS
                _op2_Tr2_PMOSNumberofGate=params.get('_op2_Tr2_PMOSNumberofGate'),
                _op2_Tr2_PMOSChannelWidth=params.get('_op2_Tr2_PMOSChannelWidth'),
                _op2_Tr2_PMOSChannellength=params.get('_op2_Tr2_PMOSChannellength'),
                _op2_Tr2_PMOSGateSpacing	= params.get('_op2_Tr2_PMOSGateSpacing'),
                _op2_Tr2_PMOSSDWidth			= params.get('_op2_Tr2_PMOSSDWidth'),
                _op2_Tr2_PMOSXVT				= params.get('_op2_Tr2_PMOSXVT'),
                _op2_Tr2_PMOSPCCrit				= params.get('_op2_Tr2_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr2_PMOSSource_Via_TF = params.get('_op2_Tr2_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr2_PMOSDrain_Via_TF = params.get('_op2_Tr2_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr2_PMOSDummy = params.get('_op2_Tr2_PMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr2_PMOSDummy_length = params.get('_op2_Tr2_PMOSDummy_length'), # None/Value
                _op2_Tr2_PMOSDummy_placement = params.get('_op2_Tr2_PMOSDummy_placement'), # None/Up/Dn/

                # PMOS
                _op2_Tr3_PMOSNumberofGate=params.get('_op2_Tr3_PMOSNumberofGate'),
                _op2_Tr3_PMOSChannelWidth=params.get('_op2_Tr3_PMOSChannelWidth'),
                _op2_Tr3_PMOSChannellength=params.get('_op2_Tr3_PMOSChannellength'),
                _op2_Tr3_PMOSGateSpacing	= params.get('_op2_Tr3_PMOSGateSpacing'),
                _op2_Tr3_PMOSSDWidth			= params.get('_op2_Tr3_PMOSSDWidth'),
                _op2_Tr3_PMOSXVT				= params.get('_op2_Tr3_PMOSXVT'),
                _op2_Tr3_PMOSPCCrit				= params.get('_op2_Tr3_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr3_PMOSSource_Via_TF = params.get('_op1_Tr3_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr3_PMOSDrain_Via_TF = params.get('_op1_Tr3_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr3_PMOSDummy = params.get('_op2_Tr3_PMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr3_PMOSDummy_length = params.get('_op2_Tr3_PMOSDummy_length'), # None/Value
                _op2_Tr3_PMOSDummy_placement = params.get('_op2_Tr3_PMOSDummy_placement'), # None/Up/Dn/

                # PMOS
                _op2_Tr4_PMOSNumberofGate	= params.get('_op2_Tr4_PMOSNumberofGate'),
                _op2_Tr4_PMOSChannelWidth	= params.get('_op2_Tr4_PMOSChannelWidth'),
                _op2_Tr4_PMOSChannellength	= params.get('_op2_Tr4_PMOSChannellength'),
                _op2_Tr4_PMOSGateSpacing		= params.get('_op2_Tr4_PMOSGateSpacing'),
                _op2_Tr4_PMOSSDWidth			= params.get('_op2_Tr4_PMOSSDWidth'),
                _op2_Tr4_PMOSXVT				= params.get('_op2_Tr4_PMOSXVT'),
                _op2_Tr4_PMOSPCCrit				= params.get('_op2_Tr4_PMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr4_PMOSSource_Via_TF = params.get('_op2_Tr4_PMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr4_PMOSDrain_Via_TF = params.get('_op2_Tr4_PMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr4_PMOSDummy = params.get('_op2_Tr4_PMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr4_PMOSDummy_length = params.get('_op2_Tr4_PMOSDummy_length'), # None/Value
                _op2_Tr4_PMOSDummy_placement = params.get('_op2_Tr4_PMOSDummy_placement'), # None/Up/Dn/

                # NMOS Tr0
                _op2_Tr0_NMOSNumberofGate=params.get('_op2_Tr0_NMOSNumberofGate'),
                _op2_Tr0_NMOSChannelWidth=params.get('_op2_Tr0_NMOSChannelWidth'),
                _op2_Tr0_NMOSChannellength=params.get('_op2_Tr0_NMOSChannellength'),
                _op2_Tr0_NMOSGateSpacing=params.get('_op2_Tr0_NMOSGateSpacing'),
                _op2_Tr0_NMOSSDWidth	= params.get('_op2_Tr0_NMOSSDWidth'),
                _op2_Tr0_NMOSXVT			= params.get('_op2_Tr0_NMOSXVT'),
                _op2_Tr0_NMOSPCCrit			= params.get('_op2_Tr0_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr0_NMOSSource_Via_TF= params.get('_op2_Tr0_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr0_NMOSDrain_Via_TF= params.get('_op2_Tr0_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr0_NMOSDummy= params.get('_op2_Tr0_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr0_NMOSDummy_length = params.get('_op2_Tr0_NMOSDummy_length'), # None/Value
                _op2_Tr0_NMOSDummy_placement = params.get('_op2_Tr0_NMOSDummy_placement'), # None/'Up'/'Dn'/

                # NMOS Tr0
                _op2_Tr1_NMOSNumberofGate=params.get('_op2_Tr1_NMOSNumberofGate'),
                _op2_Tr1_NMOSChannelWidth=params.get('_op2_Tr1_NMOSChannelWidth'),
                _op2_Tr1_NMOSChannellength=params.get('_op2_Tr1_NMOSChannellength'),
                _op2_Tr1_NMOSGateSpacing	= params.get('_op2_Tr1_NMOSGateSpacing'),
                _op2_Tr1_NMOSSDWidth			= params.get('_op2_Tr1_NMOSSDWidth'),
                _op2_Tr1_NMOSXVT				= params.get('_op2_Tr1_NMOSXVT'),
                _op2_Tr1_NMOSPCCrit				= params.get('_op2_Tr1_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr1_NMOSSource_Via_TF = params.get('_op2_Tr1_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr1_NMOSDrain_Via_TF = params.get('_op2_Tr1_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr1_NMOSDummy = params.get('_op2_Tr1_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr1_NMOSDummy_length = params.get('_op2_Tr1_NMOSDummy_length'), # None/Value
                _op2_Tr1_NMOSDummy_placement = params.get('_op2_Tr1_NMOSDummy_placement'), # None/'Up'/'Dn'/

                # NMOS
                _op2_Tr2_NMOSNumberofGate=params.get('_op2_Tr2_NMOSNumberofGate'),
                _op2_Tr2_NMOSChannelWidth=params.get('_op2_Tr2_NMOSChannelWidth'),
                _op2_Tr2_NMOSChannellength=params.get('_op2_Tr2_NMOSChannellength'),
                _op2_Tr2_NMOSGateSpacing=params.get('_op2_Tr2_NMOSGateSpacing'),
                _op2_Tr2_NMOSSDWidth	= params.get('_op2_Tr2_NMOSSDWidth'),
                _op2_Tr2_NMOSXVT			= params.get('_op2_Tr2_NMOSXVT'),
                _op2_Tr2_NMOSPCCrit			= params.get('_op2_Tr2_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr2_NMOSSource_Via_TF= params.get('_op2_Tr2_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr2_NMOSDrain_Via_TF= params.get('_op2_Tr2_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr2_NMOSDummy= params.get('_op2_Tr2_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr2_NMOSDummy_length = params.get('_op2_Tr2_NMOSDummy_length'), # None/Value
                _op2_Tr2_NMOSDummy_placement = params.get('_op2_Tr2_NMOSDummy_placement'), # None/'Up'/'Dn'/

                # NMOS
                _op2_Tr3_NMOSNumberofGate=params.get('_op2_Tr3_NMOSNumberofGate'),
                _op2_Tr3_NMOSChannelWidth=params.get('_op2_Tr3_NMOSChannelWidth'),
                _op2_Tr3_NMOSChannellength=params.get('_op2_Tr3_NMOSChannellength'),
                _op2_Tr3_NMOSGateSpacing	= params.get('_op2_Tr3_NMOSGateSpacing'),
                _op2_Tr3_NMOSSDWidth			= params.get('_op2_Tr3_NMOSSDWidth'),
                _op2_Tr3_NMOSXVT				= params.get('_op2_Tr3_NMOSXVT'),
                _op2_Tr3_NMOSPCCrit				= params.get('_op2_Tr3_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr3_NMOSSource_Via_TF = params.get('_op2_Tr3_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr3_NMOSDrain_Via_TF = params.get('_op2_Tr3_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr3_NMOSDummy = params.get('_op2_Tr3_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr3_NMOSDummy_length = params.get('_op2_Tr3_NMOSDummy_length'), # None/Value
                _op2_Tr3_NMOSDummy_placement = params.get('_op2_Tr3_NMOSDummy_placement'), # None/'Up'/'Dn'/

                # NMOS Tr0
                _op2_Tr4_NMOSNumberofGate=params.get('_op2_Tr4_NMOSNumberofGate'),
                _op2_Tr4_NMOSChannelWidth=params.get('_op2_Tr4_NMOSChannelWidth'),
                _op2_Tr4_NMOSChannellength=params.get('_op2_Tr4_NMOSChannellength'),
                _op2_Tr4_NMOSGateSpacing	= params.get('_op2_Tr4_NMOSGateSpacing'),
                _op2_Tr4_NMOSSDWidth			= params.get('_op2_Tr4_NMOSSDWidth'),
                _op2_Tr4_NMOSXVT				= params.get('_op2_Tr4_NMOSXVT'),
                _op2_Tr4_NMOSPCCrit				= params.get('_op2_Tr4_NMOSPCCrit'),

                # Source_node_ViaM1M2
                _op2_Tr4_NMOSSource_Via_TF = params.get('_op2_Tr4_NMOSSource_Via_TF'),

                # Drain_node_ViaM1M2
                _op2_Tr4_NMOSDrain_Via_TF = params.get('_op2_Tr4_NMOSDrain_Via_TF'),

                # POLY dummy setting
                _op2_Tr4_NMOSDummy = params.get('_op2_Tr4_NMOSDummy'), # TF
                # if _PMOSDummy == True
                _op2_Tr4_NMOSDummy_length = params.get('_op2_Tr4_NMOSDummy_length'), # None/Value
                _op2_Tr4_NMOSDummy_placement = params.get('_op2_Tr4_NMOSDummy_placement'), # None/'Up'/'Dn'/

                _op2_NumContTop_P1P2P4 = params.get('_op2_NumContTop_P1P2P4'),
                _op2_NumContBottom_P1P2P4 = params.get('_op2_NumContBottom_P1P2P4'),
                _op2_NumContLeft_P1P2P4 = params.get('_op2_NumContLeft_P1P2P4'),
                _op2_NumContRight_P1P2P4 = params.get('_op2_NumContRight_P1P2P4'),

                # N body ring(P0P3)
                _op2_NumContTop_P0P3=params.get('_op2_NumContTop_P0P3'),
                _op2_NumContLeft_P0P3=params.get('_op2_NumContLeft_P0P3'),
                _op2_NumContRight_P0P3=params.get('_op2_NumContRight_P0P3'),

                # P body ring
                _op2_NumContTop_Pbody=params.get('_op2_NumContTop_Pbody'),
                _op2_NumContBottom_Pbody=params.get('_op2_NumContBottom_Pbody'),
                _op2_NumContLeft_Pbody=params.get('_op2_NumContLeft_Pbody'),
                _op2_NumContRight_Pbody=params.get('_op2_NumContRight_Pbody'),

                # Res0
                _op2_ResWidth_res0=params.get('_op2_ResWidth_res0'),
                _op2_ResLength_res0=params.get('_op2_ResLength_res0'),
                _op2_CONUMX_res0=params.get('_op2_CONUMX_res0'),
                _op2_CONUMY_res0=params.get('_op2_CONUMY_res0'),
                _op2_SeriesStripes_res0=params.get('_op2_SeriesStripes_res0'),
                _op2_ParallelStripes_res0=params.get('_op2_ParallelStripes_res0'),

                # Res0
                _op2_ResWidth_res1=params.get('_op2_ResWidth_res1'),
                _op2_ResLength_res1=params.get('_op2_ResLength_res1'),
                _op2_CONUMX_res1=params.get('_op2_CONUMX_res1'),
                _op2_CONUMY_res1=params.get('_op2_CONUMY_res1'),
                _op2_SeriesStripes_res1=params.get('_op2_SeriesStripes_res1'),
                _op2_ParallelStripes_res1=params.get('_op2_ParallelStripes_res1'),

                # Cap0
                _op2_Length_cap0=params.get('_op2_Length_cap0'),
                _op2_LayoutOption_cap0=params.get('_op2_LayoutOption_cap0'),
                _op2_NumFigPair_cap0=params.get('_op2_NumFigPair_cap0'),

                _op2_Array_cap0=params.get('_op2_Array_cap0'),  # number: 1xnumber
                _op2_Cbot_Ctop_metalwidth_cap0=params.get('_op2_Cbot_Ctop_metalwidth_cap0'),  # number

                # Cap1
                _op2_Length_cap1=params.get('_op2_Length_cap1'),
                _op2_LayoutOption_cap1=params.get('_op2_LayoutOption_cap1'),
                _op2_NumFigPair_cap1=params.get('_op2_NumFigPair_cap1'),

                _op2_Array_cap1=params.get('_op2_Array_cap1'),  # number: 1xnumber
                _op2_Cbot_Ctop_metalwidth_cap1=params.get('_op2_Cbot_Ctop_metalwidth_cap1'),  # number


                # ResA
                _ResWidth_resA=params.get('_ResWidth_resA'),
                _ResLength_resA=params.get('_ResLength_resA'),
                _CONUMX_resA=params.get('_CONUMX_resA'),
                _CONUMY_resA=params.get('_CONUMY_resA'),
                _SeriesStripes_resA=params.get('_SeriesStripes_resA'),
                _ParallelStripes_resA=params.get('_ParallelStripes_resA'),

                ### 2nd Feedback
                # Res_2nd
                _ResWidth_2nd=params.get('_ResWidth_2nd'),
                _ResLength_2nd=params.get('_ResLength_2nd'),
                _CONUMX_2nd=params.get('_CONUMX_2nd'),
                _CONUMY_2nd=params.get('_CONUMY_2nd'),
                _SeriesStripes_2nd=params.get('_SeriesStripes_2nd'),
                _ParallelStripes_2nd=params.get('_ParallelStripes_2nd'),
                _Res_Port1Layer=params.get('_Res_Port1Layer'),
                _Res_Port2Layer=params.get('_Res_Port2Layer'),

                # Cap_2nd
                _Length_2nd=params.get('_Length_2nd'),
                _LayoutOption_2nd=params.get('_LayoutOption_2nd'),
                _NumFigPair_2nd=params.get('_NumFigPair_2nd'),
                _Array_2nd_row=params.get('_Array_2nd_row'),
                _Array_2nd_col=params.get('_Array_2nd_col'),
                _Cbot_Ctop_metalwidth_2nd=params.get('_Cbot_Ctop_metalwidth_2nd'),

                ### 1st Feedback
                # Parallel Res
                _Par_ResWidth=params.get('_Par_ResWidth'),
                _Par_ResLength=params.get('_Par_ResLength'),
                _Par_SeriesStripes=params.get('_Par_SeriesStripes'),
                _Par_ParallelStripes=params.get('_Par_ParallelStripes'),

                # Series Res
                _Ser_ResWidth=params.get('_Ser_ResWidth'),
                _Ser_ResLength=params.get('_Ser_ResLength'),
                _Ser_SeriesStripes=params.get('_Ser_SeriesStripes'),
                _Ser_ParallelStripes=params.get('_Ser_ParallelStripes'),

                ### TG NMOS PMOS
                _TG_NumberofGate=params.get('_TG_NumberofGate'),  # number
                _TG_NMOSChannelWidth=params.get('_TG_NMOSChannelWidth'),  # number
                _TG_PMOSChannelWidth=params.get('_TG_PMOSChannelWidth'),
                _TG_Channellength=params.get('_TG_Channellength'),  # number
                _TG_XVT=params.get('_TG_XVT'),  # 'XVT' ex)SLVT LVT RVT HVT EG
                _INV_NumberofGate=params.get('_INV_NumberofGate'),
                _NMOS_Pbody_NumCont=params.get('_NMOS_Pbody_NumCont'),
                _PMOS_Nbody_NumCont=params.get('_PMOS_Nbody_NumCont'),

                _Parallel_Stack=params.get('_Parallel_Stack'),

                # Cap_1st
                _Length_1st=params.get('_Length_1st'),
                _LayoutOption_1st=params.get('_LayoutOption_1st'),
                _NumFigPair_1st=params.get('_NumFigPair_1st'),
                _Array_1st_row=params.get('_Array_1st_row'),
                _Array_1st_col=params.get('_Array_1st_col'),
                _Cbot_Ctop_metalwidth_1st=params.get('_Cbot_Ctop_metalwidth_1st'),

            )
            # _2stageamp._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=_2stageamp._DesignParameter)
            # with open(rf'C:\Users\KJB\PycharmProjects\LayGenGUI\Verify_Rand_beginner_JH\_2stageamp\_2stageamp{word}.gds', 'wb') as f:
            #     gds_stream = _2stageamp._CreateGDSStream(_2stageamp._DesignParameter['_GDSFile']['_GDSFile'])
            #     gds_stream.write_binary_gds_stream(f)
            out_gds = rf"C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\{self.cell_name}\{self.cell_name}{word}.gds"
            os.makedirs(os.path.dirname(out_gds), exist_ok=True)

            TIA._UpdateDesignParameter2GDSStructure(
                _DesignParameterInDictionary=TIA._DesignParameter
            )

            with open(out_gds, "wb") as f:
                gds_stream = TIA._CreateGDSStream(
                    TIA._DesignParameter['_GDSFile']['_GDSFile']
                )
                gds_stream.write_binary_gds_stream(f)

        return None
            # BGR._CalculateDesignParameter(finger_N1=params.get('finger_N1'), finger_N2=params.get('finger_N2'), finger_P1=params.get('finger_P1'),  finger_P5=params.get('finger_P5'), finger_N5=params.get('finger_N5'), finger_N4=params.get('finger_N4'), finger_P3=params.get('finger_P3'),
            #                               finger_P4=params.get('finger_P4'),L1=params.get('L1'),Dummy=True,XVT='RVT',Guad_via=2,W_res1=params.get('W_res1'),L_res1=params.get('L_res1'),series_res1=params.get('series_res1'),Gate_cap=params.get('Gate_cap'),RX_cap=params.get('RX_cap'),L_cap=params.get('L_cap'),W_cap=params.get('W_cap'),
            #                               finger_N6=params.get('finger_N6'), finger_N7=params.get('finger_N7'),finger_P6=params.get('finger_P6'), finger_P7=params.get('finger_P7'), finger_P8=params.get('finger_P8'),finger_P9=params.get('finger_P9'),finger_P10=params.get('finger_P10'),
            #                                L2=params.get('L2'), L3=params.get('L3'), L_res2=params.get('L_res2'),W_res2=params.get('W_res2'), series_res2=params.get('series_res2'),W_res3=params.get('W_res3'), L_Res3=params.get('L_Res3'), series_res3=params.get('series_res3'), W_pnp=2000,
            #                               pnp_stack=params.get('pnp_stack'),pnp_mid_num=params.get('pnp_mid_num'),W_N1=params.get('W_N1'),W_P1=params.get('W_P1'),W_P2=params.get('W_P2'),W_N3=params.get('W_N3'),W_P3=params.get('W_P3'))
            # # inv._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=inv._DesignParameter)
            # BGR._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=BGR._DesignParameter)
            # # with open(f'./inverter/inverter{word}.gds', 'wb') as f:
            # #     gds_stream = inv._CreateGDSStream(inv._DesignParameter['_GDSFile']['_GDSFile'])
            # #     gds_stream.write_binary_gds_stream(f)
            # with open(f'./Verify_Rand_beginner_JH/BGR/BGR{word}.gds', 'wb') as f:
            #     gds_stream = BGR._CreateGDSStream(BGR._DesignParameter['_GDSFile']['_GDSFile'])
            #     gds_stream.write_binary_gds_stream(f)

        # Add here to run with another IP


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
        self.ssh.send_file(rf'C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\_cmos28lp.drc.cal_', f'{personal.RUNDIR}/{word}/_cmos28lp.drc.cal_')
        self.ssh.send_file(rf'C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\_calibre.run_', f'{personal.RUNDIR}/{word}/_calibre.run_')

        self.ssh.send_file(rf'C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\{self.cell_name}\{self.cell_name}{word}.src.net', f'{personal.RUNDIR}/{word}/{self.cell_name}.src.net')
        self.ssh.send_file(rf'C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\{self.cell_name}\{self.cell_name}{word}.gds', f'{personal.RUNDIR}/{word}/{self.cell_name}.gds')


    def retrieve_drc(self, word='1'):
        test = False

        with SCPClient(self.ssh.ssh.get_transport()) as scp:
            scp.get(f'{personal.RUNDIR}/{word}/drc_summary.rpt', rf'C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\report_DRC\drc{word}.report')
        with open(rf'C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\report_DRC\drc{word}.report', 'r') as f:
            for line in f.readlines()[-2:-1]:
                if line.split()[4] != '0': # TOTAL DRC Results Generated: 0 (0)\n
                    print(f"DRC{word} FAILED. {line.split()[4]} errors occurred")
                    test = False
                    # sys.exit()
                    break
                else:
                    print(f"DRC{word} PASSED.")
                    test = True
                    break
        return test
    # def retrieve_drc(self, word='1'):
    #     remote_dir = f"{personal.RUNDIR}/{word}"
    #     remote_rpt = f"{remote_dir}/drc_summary.rpt"
    #
    #     #1) 서버에 파일 있는지 먼저 확인
    #     stdin, stdout, stderr = self.ssh.ssh.exec_command(
    #         f"ls -al {remote_dir} | egrep 'drc|DRC|rpt|report|log' || true")
    #     print("[REMOTE LIST]\n" + "".join(stdout.readlines()))
    #     err = "".join(stderr.readlines())
    #     if err.strip():
    #         print("[REMOTE STDERR]\n" + err)
    #
    #     stdin, stdout, stderr = self.ssh.ssh.exec_command(f"test -f {remote_rpt}; echo $?")
    #     rc = stdout.read().decode().strip()
    #
    #     if rc != "0":
    #         # report 이름이 다른 경우 찾기
    #         stdin, stdout, stderr = self.ssh.ssh.exec_command(
    #             f"find {remote_dir} -maxdepth 1 -type f \\( -name '*drc*' -o -name '*.rpt' -o -name '*report*' -o -name '*log*' \\) -print")
    #         print("[REMOTE FIND]\n" + stdout.read().decode())
    #         return False
    #
    #     # 2) 있을 때만 scp
    #     local = rf"C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\report_DRC\drc{word}.report"
    #     with SCPClient(self.ssh.ssh.get_transport()) as scp:
    #         scp.get(remote_rpt, local)
    #
    #     # 3) 파일 포맷 다양해서 robust하게 파싱(권장)
    #     with open(local, "r", errors="ignore") as f:
    #         text = f.read()
    #     if "TOTAL DRC Results Generated" in text and "0" in text.split("TOTAL DRC Results Generated")[-1][:50]:
    #         print(f"DRC{word} PASSED.")
    #         return True
    #     else:
    #         print(f"DRC{word} FAILED (check report).")
    #         return False

    # def retrieve_lvs(self, word='1'):
    #     remote_dir = f"{personal.RUNDIR}/{word}"
    #     remote_rpt = f"{remote_dir}/{self.cell_name}.lvs.report"
    #
    #     # 1) report 존재 확인
    #     stdin, stdout, stderr = self.ssh.ssh.exec_command(f"test -f {remote_rpt}; echo $?")
    #     if stdout.read().decode().strip() != "0":
    #         # 없으면 디버깅용: log / report 후보 출력
    #         stdin, stdout, stderr = self.ssh.ssh.exec_command(
    #             f"ls -al {remote_dir} | egrep 'lvs|LVS|report|log|calibre' || true; "
    #             f"echo '---'; tail -200 {remote_dir}/calibre_lvs.log 2>/dev/null || true"
    #         )
    #         print("[LVS DEBUG]\n" + stdout.read().decode(errors="ignore"))
    #         return False
    #
    #     # 2) 있을 때만 scp
    #     local = rf"C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\report_DRC\lvs{word}.report"
    #     os.makedirs(os.path.dirname(local), exist_ok=True)
    #
    #     with SCPClient(self.ssh.ssh.get_transport()) as scp:
    #         scp.get(remote_rpt, local)
    #
    #     # 3) 파싱
    #     with open(local, "r", errors="ignore") as f:
    #         for line in f:
    #             if "INCORRECT" in line:
    #                 print(f"LVS{word} FAILED.")
    #                 return False
    #             if "CORRECT" in line:
    #                 print(f"LVS{word} PASSED.")
    #                 return True
    #
    #     return False

    def retrieve_lvs(self, word='1'):
        test = False

        with SCPClient(self.ssh.ssh.get_transport()) as scp:
            scp.get(f'{personal.RUNDIR}/{word}/{self.cell_name}.lvs.report', rf'C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\report_LVS\lvs{word}.report')
        with open(rf'C:\Users\ych\PycharmProjects\Laygen_DRC_LVS_JK\generatorLib\generator_models\Verify_Rand_beginner_JH\report_LVS\lvs{word}.report', 'r') as f:
            for i in f.readlines():
                if "INCORRECT" in i:
                    print(f"LVS{word} FAILED. errors occurred")
                    test = False
                    # sys.exit() # 주석 처리하면 error에도 exit 안됨
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
            # scp.get(f'{personal.RUNDIR}/{word}/VOUT_tran', f'./report_posim/VOUT_tran_{word}.report')
            # scp.get(f'{personal.RUNDIR}/{word}/VOUT_dc', f'./report_posim/VOUT_dc_{word}.report')

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
    _TRP0_P3_N2_N3_ChannelWidth_rd =(1000,[3000,20000])
    _TRP1_P2_P4_ChannelWidth_rd = (1000,[3000,20000])
    _TRN0_N1_N4_ChannelWidth_rd = (1000,[3000,20000])

    _TR1_2_PMOSNumberofGate_rd = (1,[15,25])
    _TR0_PMOSNumberofGate_rd = (1,[2,15])
    _TR3_PMOSNumberofGate_rd = (1,[2,4])
    _TR4_PMOSNumberofGate_rd = (1,[15,25])
    _TR0_1_NMOSNumberofGate_rd = (1,[4,10])
    _TR4_NMOSNumberofGate_rd = (1,[3,10])
    _TR2_NMOSNumberofGate_rd = (1,[2,5])
    _TR3_NMOSNumberofGate_rd = (1,[2,5])

    _Res_Width_rd = (100,[500,1500])
    _Res_Length_rd = (100,[500,1500])

    _Cap_Length_rd = (1000,[5000,9000])
    _Cap_finger_rd = (2,[30,60])

    randgen = RandGen(cell_name='TIA',
                      # PMOS
                      _op1_Tr0_PMOSNumberofGate=_TR0_PMOSNumberofGate_rd,
                      _op1_Tr0_PMOSChannelWidth=_TRP0_P3_N2_N3_ChannelWidth_rd,
                      _op1_Tr0_PMOSChannellength=150,
                      _op1_Tr0_PMOSGateSpacing=None,
                      _op1_Tr0_PMOSSDWidth=None,
                      _op1_Tr0_PMOSXVT	= 'EG',
                      _op1_Tr0_PMOSPCCrit		= None,

                      # Source_node_ViaM1M2
                      _op1_Tr0_PMOSSource_Via_TF= True,

                      # Drain_node_ViaM1M2
                      _op1_Tr0_PMOSDrain_Via_TF= True,

                      # POLY dummy setting
                      _op1_Tr0_PMOSDummy= True  , # TF
                      # if _PMOSDummy == True
                      _op1_Tr0_PMOSDummy_length = None, # None/Value
                      _op1_Tr0_PMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # PMOS
                      _op1_Tr1_PMOSNumberofGate=_TR1_2_PMOSNumberofGate_rd,
                      _op1_Tr1_PMOSChannelWidth=_TRP1_P2_P4_ChannelWidth_rd,
                      _op1_Tr1_PMOSChannellength=150,
                      _op1_Tr1_PMOSGateSpacing=None,
                      _op1_Tr1_PMOSSDWith	= None,
                      _op1_Tr1_PMOSXVT			= 'EG',
                      _op1_Tr1_PMOSPCCrit			= None,

                      # Source_node_ViaM1M2
                      _op1_Tr1_PMOSSource_Via_TF= True,

                      # Drain_node_ViaM1M2
                      _op1_Tr1_PMOSDrain_Via_TF= True,

                      # POLY dummy setting
                      _op1_Tr1_PMOSDummy= True, # TF
                      # if _PMOSDummy == True
                      _op1_Tr1_PMOSDummy_length = None, # None/Value
                      _op1_Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # PMOS
                      _op1_Tr2_PMOSNumberofGate	= (0, [0], "_op1_Tr1_PMOSNumberofGate"),
                      _op1_Tr2_PMOSChannelWidth	= (0, [0], "_op1_Tr1_PMOSChannelWidth"),
                      _op1_Tr2_PMOSChannellength	= 150,
                      _op1_Tr2_PMOSGateSpacing		= None,
                      _op1_Tr2_PMOSSDWidth			= None,
                      _op1_Tr2_PMOSXVT				= 'EG',
                      _op1_Tr2_PMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op1_Tr2_PMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op1_Tr2_PMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op1_Tr2_PMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op1_Tr2_PMOSDummy_length = None, # None/Value
                      _op1_Tr2_PMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # PMOS
                      _op1_Tr3_PMOSNumberofGate=_TR3_PMOSNumberofGate_rd,
                      _op1_Tr3_PMOSChannelWidth=(0,[0],"_op1_Tr0_PMOSChannelWidth"),
                      _op1_Tr3_PMOSChannellength=150,
                      _op1_Tr3_PMOSGateSpacing=None,
                      _op1_Tr3_PMOSSDWith	= None,
                      _op1_Tr3_PMOSXVT			= 'EG',
                      _op1_Tr3_PMOSPCCrit			= None,

                      # Source_node_ViaM1M2
                      _op1_Tr3_PMOSSource_Via_TF= True,

                      # Drain_node_ViaM1M2
                      _op1_Tr3_PMOSDrain_Via_TF= True,

                      # POLY dummy setting
                      _op1_Tr3_PMOSDummy= True  , # TF
                      # if _PMOSDummy == True
                      _op1_Tr3_PMOSDummy_length = None, # None/Value
                      _op1_Tr3_PMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # PMOS
                      _op1_Tr4_PMOSNumberofGate=_TR4_PMOSNumberofGate_rd,
                      _op1_Tr4_PMOSChannelWidth=(0, [0], "_op1_Tr1_PMOSChannelWidth"),
                      _op1_Tr4_PMOSChannellength=150,
                      _op1_Tr4_PMOSGateSpacing	= None,
                      _op1_Tr4_PMOSSDWidth			= None,
                      _op1_Tr4_PMOSXVT				= 'EG',
                      _op1_Tr4_PMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op1_Tr4_PMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op1_Tr4_PMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op1_Tr4_PMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op1_Tr4_PMOSDummy_length = None, # None/Value
                      _op1_Tr4_PMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS Tr0
                      _op1_Tr0_NMOSNumberofGate=_TR0_1_NMOSNumberofGate_rd,
                      _op1_Tr0_NMOSChannelWidth=_TRN0_N1_N4_ChannelWidth_rd,
                      _op1_Tr0_NMOSChannellength=150,
                      _op1_Tr0_NMOSGateSpacing=None,
                      _op1_Tr0_NMOSSDWidth	= None,
                      _op1_Tr0_NMOSXVT			= 'EG',
                      _op1_Tr0_NMOSPCCrit			= None,

                      # Source_node_ViaM1M2
                      _op1_Tr0_NMOSSource_Via_TF= True,

                      # Drain_node_ViaM1M2
                      _op1_Tr0_NMOSDrain_Via_TF= True,

                      # POLY dummy setting
                      _op1_Tr0_NMOSDummy= True, # TF
                      # if _PMOSDummy == True
                      _op1_Tr0_NMOSDummy_length = None, # None/Value
                      _op1_Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS Tr1
                      _op1_Tr1_NMOSNumberofGate=(0, [0], "_op1_Tr0_NMOSNumberofGate"),
                      _op1_Tr1_NMOSChannelWidth=(0, [0], "_op1_Tr0_NMOSChannelWidth"),
                      _op1_Tr1_NMOSChannellength=150,
                      _op1_Tr1_NMOSGateSpacing	= None,
                      _op1_Tr1_NMOSSDWidth			= None,
                      _op1_Tr1_NMOSXVT				= 'EG',
                      _op1_Tr1_NMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op1_Tr1_NMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op1_Tr1_NMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op1_Tr1_NMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op1_Tr1_NMOSDummy_length = None, # None/Value
                      _op1_Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS
                      _op1_Tr2_NMOSNumberofGate=_TR2_NMOSNumberofGate_rd,
                      _op1_Tr2_NMOSChannelWidth=(0, [0], "_op1_Tr0_PMOSChannelWidth"),
                      _op1_Tr2_NMOSChannellength=150,
                      _op1_Tr2_NMOSGateSpacing=None,
                      _op1_Tr2_NMOSSDWidth	= None,
                      _op1_Tr2_NMOSXVT			= 'EG',
                      _op1_Tr2_NMOSPCCrit			= None,

                      # Source_node_ViaM1M2
                      _op1_Tr2_NMOSSource_Via_TF= True,

                      # Drain_node_ViaM1M2
                      _op1_Tr2_NMOSDrain_Via_TF= True,

                      # POLY dummy setting
                      _op1_Tr2_NMOSDummy= True, # TF
                      # if _PMOSDummy == True
                      _op1_Tr2_NMOSDummy_length = None, # None/Value
                      _op1_Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS
                      _op1_Tr3_NMOSNumberofGate=_TR3_NMOSNumberofGate_rd,
                      _op1_Tr3_NMOSChannelWidth=(0, [0], "_op1_Tr0_PMOSChannelWidth"),
                      _op1_Tr3_NMOSChannellength=150,
                      _op1_Tr3_NMOSGateSpacing	= None,
                      _op1_Tr3_NMOSSDWidth			= None,
                      _op1_Tr3_NMOSXVT				= 'EG',
                      _op1_Tr3_NMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op1_Tr3_NMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op1_Tr3_NMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op1_Tr3_NMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op1_Tr3_NMOSDummy_length = None, # None/Value
                      _op1_Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS Tr4
                      _op1_Tr4_NMOSNumberofGate=_TR4_NMOSNumberofGate_rd,
                      _op1_Tr4_NMOSChannelWidth=(0, [0], "_op1_Tr0_NMOSChannelWidth"),
                      _op1_Tr4_NMOSChannellength=150,
                      _op1_Tr4_NMOSGateSpacing	= None,
                      _op1_Tr4_NMOSSDWidth			= None,
                      _op1_Tr4_NMOSXVT				= 'EG',
                      _op1_Tr4_NMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op1_Tr4_NMOSSource_Via_TF = False,

                      # Drain_node_ViaM1M2
                      _op1_Tr4_NMOSDrain_Via_TF = False,

                      # POLY dummy setting
                      _op1_Tr4_NMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op1_Tr4_NMOSDummy_length = None, # None/Value
                      _op1_Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # N body ring(P1P2P4)
                      _op1_NumContTop_P1P2P4 = 3,
                      _op1_NumContBottom_P1P2P4=3,
                      _op1_NumContLeft_P1P2P4=3,
                      _op1_NumContRight_P1P2P4=3,

                      # N body ring(P0P3)
                      _op1_NumContTop_P0P3 = 3,
                      _op1_NumContLeft_P0P3 = 3,
                      _op1_NumContRight_P0P3 = 3,

                      # P body ring
                      _op1_NumContTop_Pbody = 3,
                      _op1_NumContBottom_Pbody=3,
                      _op1_NumContLeft_Pbody=3,
                      _op1_NumContRight_Pbody=3,

                      # Res0
                      _op1_ResWidth_res0 = _Res_Width_rd,
                      _op1_ResLength_res0 = _Res_Length_rd,
                      _op1_CONUMX_rs0 = None,
                      _op1_CONUMY_rs0 = None,
                      _op1_SeriesStripes_res0 = 1,
                      _op1_ParallelStripes_res0 =  1, # 고정

                      # Res1
                      _op1_ResWidth_res1=(0, [0], "_op1_ResWidth_res0"),
                      _op1_ResLength_res1=(0, [0], "_op1_ResLength_res0"),
                      _op1_CONUMX_res1=None,
                      _op1_CONUMY_res1=None,
                      _op1_SeriesStripes_res1=1,
                      _op1_ParallelStripes_res1=  1, # 고정

                      # Cap0
                      _op1_Length_cap0=_Cap_Length_rd,
                      _op1_LayoutOption_cap0 =[2, 3, 4, 5], # 고정
                      _op1_NumFigPair_cap0=_Cap_finger_rd,

                      _op1_Array_cap0=1,  # number: 1xnumber
                      _op1_Cbot_Ctop_metalwidth_cap0=500,  # number

                      # Cap1
                      _op1_Length_cap1=(0, [0], "_op1_Length_cap0"),
                      _op1_LayoutOption_cap1= [2, 3, 4, 5], # 고정
                      _op1_NumFigPair_cap1=(0, [0], "_op1_NumFigPair_cap0"),

                      _op1_Array_cap1=1,  # number: 1xnumber
                      _op1_Cbot_Ctop_metalwidth_cap1=500,  # number

                      # PMOS
                      _op2_Tr0_PMOSNumberofGate=(0,[0],"_op1_Tr0_PMOSNumberofGate"),
                      _op2_Tr0_PMOSChannelWidth=(0,[0],"_op1_Tr0_PMOSChannelWidth"),
                      _op2_Tr0_PMOSChannellength=150,
                      _op2_Tr0_PMOSGateSpacing=None,
                      _op2_Tr0_PMOSSDWidth=None,
                      _op2_Tr0_PMOSXVT='EG',
                      _op2_Tr0_PMOSPCCrit	= None,

                      # Source_node_ViaM1M2
                      _op2_Tr0_PMOSSource_Via_TF= True,

                      # Drain_node_ViaM1M2
                      _op2_Tr0_PMOSDrain_Via_TF= True,

                      # POLY dummy setting
                      _op2_Tr0_PMOSDummy= True  , # TF
                      # if _PMOSDummy == True
                      _op2_Tr0_PMOSDummy_length = None, # None/Value
                      _op2_Tr0_PMOSDummy_placement = None, # None/Up/Dn/

                      # PMOS
                      _op2_Tr1_PMOSNumberofGate=(0, [0], "_op1_Tr1_PMOSNumberofGate"),
                      _op2_Tr1_PMOSChannelWidth=(0, [0], "_op1_Tr1_PMOSChannelWidth"),
                      _op2_Tr1_PMOSChannellength=150,
                      _op2_Tr1_PMOSGateSpacing	=None ,
                      _op2_Tr1_PMOSSDWidth			= None,
                      _op2_Tr1_PMOSXVT				= 'EG',
                      _op2_Tr1_PMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op2_Tr1_PMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op2_Tr1_PMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op2_Tr1_PMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr1_PMOSDummy_length = None, # None/Value
                      _op2_Tr1_PMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # PMOS
                      _op2_Tr2_PMOSNumberofGate=(0, [0], "_op1_Tr1_PMOSNumberofGate"),
                      _op2_Tr2_PMOSChannelWidth=(0, [0], "_op1_Tr1_PMOSChannelWidth"),
                      _op2_Tr2_PMOSChannellength=150,
                      _op2_Tr2_PMOSGateSpacing	= None,
                      _op2_Tr2_PMOSSDWidth			= None,
                      _op2_Tr2_PMOSXVT				= 'EG',
                      _op2_Tr2_PMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op2_Tr2_PMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op2_Tr2_PMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op2_Tr2_PMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr2_PMOSDummy_length = None, # None/Value
                      _op2_Tr2_PMOSDummy_placement = None, # None/Up/Dn/

                      # PMOS
                      _op2_Tr3_PMOSNumberofGate=(0, [0], "_op1_Tr3_PMOSNumberofGate"),
                      _op2_Tr3_PMOSChannelWidth=(0,[0],"_op1_Tr0_PMOSChannelWidth"),
                      _op2_Tr3_PMOSChannellength=150,
                      _op2_Tr3_PMOSGateSpacing	= None,
                      _op2_Tr3_PMOSSDWidth			= None,
                      _op2_Tr3_PMOSXVT				= 'EG',
                      _op2_Tr3_PMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op2_Tr3_PMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op2_Tr3_PMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op2_Tr3_PMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr3_PMOSDummy_length = None, # None/Value
                      _op2_Tr3_PMOSDummy_placement = None, # None/Up/Dn/

                      # PMOS
                      _op2_Tr4_PMOSNumberofGate	=(0,[0],"_op1_Tr4_PMOSNumberofGate"),
                      _op2_Tr4_PMOSChannelWidth	= (0, [0], "_op1_Tr1_PMOSChannelWidth"),
                      _op2_Tr4_PMOSChannellength	= 150,
                      _op2_Tr4_PMOSGateSpacing		= None,
                      _op2_Tr4_PMOSSDWidth			= None,
                      _op2_Tr4_PMOSXVT				= 'EG',
                      _op2_Tr4_PMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op2_Tr4_PMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op2_Tr4_PMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op2_Tr4_PMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr4_PMOSDummy_length = None, # None/Value
                      _op2_Tr4_PMOSDummy_placement = None, # None/Up/Dn/

                      # NMOS Tr0
                      _op2_Tr0_NMOSNumberofGate=(0, [0], "_op1_Tr0_NMOSNumberofGate"),
                      _op2_Tr0_NMOSChannelWidth=(0, [0], "_op1_Tr0_NMOSChannelWidth"),
                      _op2_Tr0_NMOSChannellength=150,
                      _op2_Tr0_NMOSGateSpacing=None,
                      _op2_Tr0_NMOSSDWidth	= None,
                      _op2_Tr0_NMOSXVT			= 'EG',
                      _op2_Tr0_NMOSPCCrit			= None,

                      # Source_node_ViaM1M2
                      _op2_Tr0_NMOSSource_Via_TF= True,

                      # Drain_node_ViaM1M2
                      _op2_Tr0_NMOSDrain_Via_TF= True,

                      # POLY dummy setting
                      _op2_Tr0_NMOSDummy= True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr0_NMOSDummy_length = None, # None/Value
                      _op2_Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS Tr0
                      _op2_Tr1_NMOSNumberofGate=(0, [0], "_op1_Tr0_NMOSNumberofGate"),
                      _op2_Tr1_NMOSChannelWidth=(0, [0], "_op1_Tr0_NMOSChannelWidth"),
                      _op2_Tr1_NMOSChannellength=150,
                      _op2_Tr1_NMOSSDWidth	= None,
                      _op1_Tr1_NMOSSdh			= None,
                      _op2_Tr1_NMOSXVT				= 'EG',
                      _op2_Tr1_NMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op2_Tr1_NMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op2_Tr1_NMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op2_Tr1_NMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr1_NMOSDummy_length = None, # None/Value
                      _op2_Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS
                      _op2_Tr2_NMOSNumberofGate=(0, [0], "_op1_Tr2_NMOSNumberofGate"),
                      _op2_Tr2_NMOSChannelWidth=(0, [0], "_op1_Tr0_PMOSChannelWidth"),
                      _op2_Tr2_NMOSChannellength=150,
                      _op2_Tr2_NMOSGateSpacing=None,
                      _op2_Tr2_NMOSSDWidth	= None,
                      _op2_Tr2_NMOSXVT			= 'EG',
                      _op2_Tr2_NMOSPCCrit			= None,

                      # Source_node_ViaM1M2
                      _op2_Tr2_NMOSSource_Via_TF= True,

                      # Drain_node_ViaM1M2
                      _op2_Tr2_NMOSDrain_Via_TF= True,

                      # POLY dummy setting
                      _op2_Tr2_NMOSDummy= True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr2_NMOSDummy_length = None, # None/Value
                      _op2_Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS
                      _op2_Tr3_NMOSNumberofGate=(0, [0], "_op1_Tr3_NMOSNumberofGate"),
                      _op2_Tr3_NMOSChannelWidth=(0, [0], "_op1_Tr0_PMOSChannelWidth"),
                      _op2_Tr3_NMOSChannellength=150,
                      _op2_Tr3_NMOSGateSpacing	= None,
                      _op2_Tr3_NMOSSDWidth			= None,
                      _op2_Tr3_NMOSXVT				= 'EG',
                      _op2_Tr3_NMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op2_Tr3_NMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op2_Tr3_NMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op2_Tr3_NMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr3_NMOSDummy_length = None, # None/Value
                      _op2_Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      # NMOS Tr0
                      _op2_Tr4_NMOSNumberofGate=(0, [0], "_op1_Tr4_NMOSNumberofGate"),
                      _op2_Tr4_NMOSChannelWidth=(0, [0], "_op1_Tr0_NMOSChannelWidth"),
                      _op2_Tr4_NMOSChannellength=150,
                      _op2_Tr4_NMOSGateSpacing	= None,
                      _op2_Tr4_NMOSSDWidth			= None,
                      _op2_Tr4_NMOSXVT				= 'EG',
                      _op2_Tr4_NMOSPCCrit				= None,

                      # Source_node_ViaM1M2
                      _op2_Tr4_NMOSSource_Via_TF = True,

                      # Drain_node_ViaM1M2
                      _op2_Tr4_NMOSDrain_Via_TF = True,

                      # POLY dummy setting
                      _op2_Tr4_NMOSDummy = True, # TF
                      # if _PMOSDummy == True
                      _op2_Tr4_NMOSDummy_length = None, # None/Value
                      _op2_Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

                      _op2_NumContTop_P1P2P4 = 3,
                      _op2_NumContBottom_P1P2P4 = 3,
                      _op2_NumContLeft_P1P2P4 = 3,
                      _op2_NumContRight_P1P2P4 = 3,

                      # N body ring(P0P3)
                      _op2_NumContTop_P0P3=3,
                      _op2_NumContLeft_P0P3=3,
                      _op2_NumContRight_P0P3=3,

                      # P body ring
                      _op2_NumContTop_Pbody=3,
                      _op2_NumContBottom_Pbody=3,
                      _op2_NumContLeft_Pbody=3,
                      _op2_NumContRight_Pbody=3,

                      # Res0
                      _op2_ResWidth_res0=(0, [0], "_op1_ResWidth_res0"),
                      _op2_ResLength_res0=(0, [0], "_op1_ResLength_res0"),
                      _op2_CONUMX_res0=None,
                      _op2_CONUMY_res0=None,
                      _op2_SeriesStripes_res0=1,
                      _op2_ParallelStripes_res0=1,

                      # Res0
                      _op2_ResWidth_res1=(0, [0], "_op1_ResWidth_res0"),
                      _op2_ResLength_res1=(0, [0], "_op1_ResLength_res0"),
                      _op2_CONUMX_res1=None,
                      _op2_CONUMY_res1=None,
                      _op2_SeriesStripes_res1=1,
                      _op2_ParallelStripes_res1=1,

                      # Cap0
                      _op2_Length_cap0=(0, [0], "_op1_Length_cap0"),
                      _op2_LayoutOption_cap0=[2, 3, 4, 5],
                      _op2_NumFigPair_cap0=(0, [0], "_op1_NumFigPair_cap0"),

                      _op2_Array_cap0=1,  # number: 1xnumber
                      _op2_Cbot_Ctop_metalwidth_cap0=500,  # number

                      # Cap1
                      _op2_Length_cap1=(0, [0], "_op1_Length_cap0"),
                      _op2_LayoutOption_cap1=[2, 3, 4, 5],
                      _op2_NumFigPair_cap1=(0, [0], "_op1_NumFigPair_cap0"),

                      _op2_Array_cap1=1,  # number: 1xnumber
                      _op2_Cbot_Ctop_metalwidth_cap1=500,  # number


                      # ResA
                      _ResWidth_resA=(100,[1000,2000]),
                      _ResLength_resA=(100,[2000,3000]),
                      _CONUMX_resA=None,
                      _CONUMY_resA=None,
                      _SeriesStripes_resA=(2,[3,8]),
                      _ParallelStripes_resA=1,

                      ### 2nd Feedback
                      # Res_2nd
                      _ResWidth_2nd=(100,[1000,2000]),
                      _ResLength_2nd=(1000,[2000,10000]),
                      _CONUMX_2nd=None,
                      _CONUMY_2nd=None,
                      _SeriesStripes_2nd=(2,[3,10]),
                      _ParallelStripes_2nd=1,
                      _Res_Port1Layer=5,
                      _Res_Port2Layer=5,

                      # Cap_2nd
                      _Length_2nd=(1000,[8000,11000]),
                      _LayoutOption_2nd=[2,3,4],
                      _NumFigPair_2nd=(1,[10,101]),
                      _Array_2nd_row=2,
                      _Array_2nd_col=3,
                      _Cbot_Ctop_metalwidth_2nd=500,

                      ### 1st Feedback
                      # Parallel Res
                      _Par_ResWidth=(10,[160,500]),
                      _Par_ResLength=1292,
                      _Par_SeriesStripes=(1,[21,101]),
                      _Par_ParallelStripes=1,

                      # Series Res
                      _Ser_ResWidth=(10,[160,500]),
                      _Ser_ResLength=1292,
                      _Ser_SeriesStripes=(2,[20,101]),
                      _Ser_ParallelStripes=1,

                      ### TG NMOS PMOS
                      _TG_NumberofGate=(10,[50,100]),  # number
                      _TG_NMOSChannelWidth=500,  # number
                      _TG_PMOSChannelWidth=1000,
                      _TG_Channellength=150,  # number
                      _TG_XVT='EG',  # 'XVT' ex)SLVT LVT RVT HVT EG
                      _INV_NumberofGate=2,
                      _NMOS_Pbody_NumCont=2,
                      _PMOS_Nbody_NumCont=2,

                      _Parallel_Stack=(1,[2,10]),

                      # Cap_1st
                      _Length_1st=(1000,[6000,10000]),
                      _LayoutOption_1st=[2,3,4],
                      _NumFigPair_1st=(2,[10,30]),
                      _Array_1st_row=2,
                      _Array_1st_col=2,
                      _Cbot_Ctop_metalwidth_1st=500,
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
    drc_result, lvs_result = randgen.run(5)
    #drc_result= randgen.run(1)
    print(drc_result.count(False), "DRC errors")
    print(lvs_result.count(False), "LVS errors")
    #print(pex_result.count(False), "PEX errors")
    # print(posim_result.count(False), "posim errors")
