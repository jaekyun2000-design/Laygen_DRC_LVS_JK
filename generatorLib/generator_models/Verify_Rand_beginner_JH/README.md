# Verify_Rand 사전설정 및 결과 확인

randomgeneration.py은 GUI로 parameter를 수정한 layout 생성 파일을 입력받아 cadence가 있는 linux 서버와의 연계를 통해 DRC, LVS, PEX, post-layout simulation을 자동으로 수행한다.

## 코드 실행 전 수정사항

1. GUI로 생성한 python file import 라인 추가 및 main 함수 수정. randgen.run 입력으로 총 수행 횟수 입력
    
    ```python
    from generatorLib.generator_models import inverter_GUI # 본인이 작성한 filename
    ```
    
    ```python
    if __name__=="__main__":
    
        randgen = RandGen(cell_name='inverter',
                          n_gate=(1,[1,200]), n_width=(10,[500,1200]), n_length=(10,[30,100]),
                          p_gate=(1,[1,200]), p_width=(10,[500,1200]), p_length=(10,[30,100]),
                          supply_coy=(1,[1,5]) # GUI에서 할당한 parameter의 random 범위 및 최소단위
                          )
    
        drc_result, lvs_result, pex_result, posim_result = randgen.run(200) # random 실행횟수
    
    ```
    
2. schematic 및 layout 생성 파일 및 함수 수정. GUI에서 할당한 parameter 동일하게 할당
    
    ```python
    def create_layout(self, params, word='1'):
        if self.cell_name == 'inverter':
            inv = **inverter_GUI**.inverter(_DesignParameter=None, _Name='inverter')
            inv._CalculateDesignParameter(n_gate=params.get('n_gate'), n_width=params.get('n_width'), n_length=params.get('n_length'), dummy='True',
                                          p_gate=params.get('p_gate'), p_width=params.get('p_width'), p_length=params.get('p_length'), supply_coy=params.get('supply_coy'))
            inv._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=inv._DesignParameter)
            with open(f'./inverter/inverter{word}.gds', 'wb') as f:
                gds_stream = inv._CreateGDSStream(inv._DesignParameter['_GDSFile']['_GDSFile'])
                gds_stream.write_binary_gds_stream(f)
    ```
    
    ```python
    def create_schematic(self, params, word='1'):
        if self.cell_name == 'inverter':
            schematic.makeINVSche(word=word, param=params)
    ```
    
    ```python
    # schematic.py
    # 새로운 cell이라면 cadence로 설계 후 netlist 불러와 수정
    def makeINVSche(word, param):
        n_width = param.get('n_width')
        p_width = param.get('p_width')
        n_length = param.get('n_length')
        p_length = param.get('p_length')
        n_gate = param.get('n_gate')
        p_gate = param.get('p_gate')
    
        nw = n_width * n_gate / 1000
        pw = p_width * p_gate / 1000
        n_len = n_length/1000
        p_len = p_length/1000
    
        if not os.path.exists('./inverter'):
            os.makedirs('./inverter')
        with open(f'./inverter/inverter{word}.src.net', 'w') as f:
            f.write('.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
            f.write('.PARAM\n')
            f.write('.SUBCKT inverter VDD VIN VOUT VSS\n')
            f.write(f'MN0 VOUT VIN VSS VSS slvtnfet w={nw}u l={n_len}u nf={n_gate}.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
            f.write(f'MP0 VOUT VIN VDD VDD slvtpfet w={pw}u l={p_len}u nf={p_gate}.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
            f.write('.ENDS')
    
        return None
    ```
    
3. personal.py 파일 만들어서 LayGenGUI 폴더에 저장
    
    ```python
    hostname = '141.223.24.53' # 서버 주소
    username = 'jihoon0721' # 서버 계정명
    password = 'password' # 서버 로그인 비밀번호
    TECHDIR = '/mnt/sdb/jihoon0721/OPUS/ss28nm' # setup 파일이 있는 주소
    RUNDIR = '/mnt/sdb/jihoon0721/OPUS/ss28nm/RandGen' # DRC, LVS, PEX, posim 실행 주소
    ```
    
4. 서버에서 Testbench 만든 후 oceanScript 생성 및 수정 후 {cell_name}_oceanScript.ocn 이름으로 RUNDIR 내 각 폴더(e.g. RandGen/1/)에 저장 (추후 자동으로 ocean 파일 옮기도록 수정 예정)
    
    ```c
    // inverter_oceanScript.ocn
    
    simulator( 'spectre )
    design(	 "/mnt/sdb/jihoon0721/simulation/Test_inverter/spectre/schematic/netlist/netlist")
    resultsDir( "/mnt/sdb/jihoon0721/OPUS/ss28nm/RandGen/1/ADEresult" ) // 각 폴더별 수정
    path( "/mnt/sdb/jihoon0721/OPUS/ss28nm" )
    modelFile( 
        '("/home/PDK/ss28nm/LN28LPP_Spectre_S00-V2.1.0.1/Spectre/LN28LPP_Spectre.lib" "nn")
    )
    stimulusFile( ?xlate nil
        "/mnt/sdb/jihoon0721/OPUS/ss28nm/RandGen/1/inverter.pex.netlist"// 각 폴더별 수정
    )
    analysis('dc ?saveOppoint t  ?lin "100" )
    analysis('tran ?stop "2n"  )
    desVar(	  "vin" 0	)
    temp( 27 ) 
    run()
    // run() 아래 plot 지우고 각 폴더별 수정
    VIN_tran = vtime('tran "/VIN")
    VOUT_tran = vtime('tran "/VOUT")
    VIN_dc = v("/VIN" ?result "dc")
    VOUT_dc = v("/VOUT" ?result "dc")
    
    ocnPrint( ?output "/mnt/sdb/jihoon0721/OPUS/ss28nm/RandGen/1/VIN_tran" VIN_tran ?numberNotation 'scientific ?from 0.3n ?to 1.2n ?step 0.1p)
    ocnPrint( ?output "/mnt/sdb/jihoon0721/OPUS/ss28nm/RandGen/1/VOUT_tran" VOUT_tran ?numberNotation 'scientific ?from 0.3n ?to 1.2n ?step 0.1p)
    ocnPrint( ?output "/mnt/sdb/jihoon0721/OPUS/ss28nm/RandGen/1/VIN_dc" VIN_dc ?numberNotation 'scientific)
    ocnPrint( ?output "/mnt/sdb/jihoon0721/OPUS/ss28nm/RandGen/1/VOUT_dc" VOUT_dc ?numberNotation 'scientific)
    exit()
    ```
    

## 코드 실행 결과

1. 코드를 수행하면 DRC, LVS, PEX를 자동으로 수행하여 에러 발생 여부를 출력한다. DRC의 경우 에러 갯수를 확인할 수 있으며, LVS는 통과 여부만, PEX는 pex netlist 생성 시간을 통해 추출 여부를 확인할 수 있다.
    
    ```python
    Start SET1 DRC
    DRC1 PASSED.
    DRC2 PASSED.
    DRC3 PASSED.
    DRC4 PASSED.
    DRC5 PASSED.
    End SET1 DRC
    
    Start SET1 LVS & PEX
    LVS1 PASSED.
    LVS2 PASSED.
    LVS3 PASSED.
    LVS4 PASSED.
    LVS5 PASSED.
    
    PEX file Creation Time : Mar 13 21:06:50
    PEX file Creation Time : Mar 13 21:06:49
    PEX file Creation Time : Mar 13 21:06:50
    PEX file Creation Time : Mar 13 21:06:49
    PEX file Creation Time : Mar 13 21:06:49
    End SET1 LVS & PEX
    ```
    
2. post-layout simulation의 경우 설계한 Testbench 와 동일한 simulation을 수행하여 report_posim에 결과를 text 형태로 저장한다. 이를 불러와 retrieve_posim을 통해 propagation delay 등의 계산을 수행한다. 다른 형태의 값을 추출하고 싶다면 해당 함수를 수정하면 된다.
    
    ```python
    Start SET1 Posim
    posim 1
    DC center = 0.54V
    t_rise = 2.5ps
    t_fall = 8.9ps
    t_prop_h2l = 5.1ps
    t_prop_l2h = 13.3ps
    
    ...
    
    End SET1 Posim
    ```
    
3. Random하게 설정한 parameter에 대한 기록은 Parameters_executed 폴더 내에서 확인할 수 있다. 파일명은 코드를 실행한 시간이다.
    
    ```python
    iteration 1-1
    n_gate: 12
    n_width: 590
    n_length: 90
    p_gate: 106
    p_width: 980
    p_length: 70
    supply_coy: 4
    
    ...
    
    iteration 1-5
    n_gate: 81
    n_width: 1120
    n_length: 50
    p_gate: 74
    p_width: 1130
    p_length: 80
    supply_coy: 3
    
    #1
    DC center = 0.54V
    t_rise = 2.5ps
    t_fall = 8.9ps
    t_prop_h2l = 5.1ps
    t_prop_l2h = 13.3ps
    
    ...
    ```