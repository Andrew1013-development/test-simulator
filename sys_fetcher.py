import os
import psutil
import platform
import json

__version__ = "1.0.0 | 1.0.1"

def fetcher() -> dict[str, str]:
    sys_id = ""
    sys_info = {
        "platform": platform.platform().replace("-"," "),
        "processor": platform.processor(),
        "architecture": platform.machine(),
        "cpu_cores": f"{psutil.cpu_count(logical=False)}",
        "cpu_frequency": f"{psutil.cpu_freq().max} MHz",
        "ram": f"{round(psutil.virtual_memory().total / 1024 ** 2,3)} MB",
        "python_implementation": platform.python_implementation(),
        "python_version": platform.python_version(),
        "python_complier": platform.python_compiler(),
        "python_buildinfo": platform.python_build(),
        "process_id": f"{os.getpid()}",
    }

    sys_id += str(hex(int(sys_info["python_version"][:-2].replace(".","")))).removeprefix("0x")
    sys_id += str(hex(int(round(float(sys_info["cpu_frequency"][:-4]) / 1000,0)))).removeprefix("0x")
    sys_id += str(hex(int(round(float(sys_info["cpu_frequency"][:-4]) % 1000,0)))).removeprefix("0x")
    sys_id += str(hex(int(round(float(sys_info["ram"][:-3]) / 1000,0)))).removeprefix("0x")
    sys_id += str(hex(int(round(float(sys_info["ram"][:-3]) % 1000,0)))).removeprefix("0x")

    sys_info["system_id"] = sys_id

    return sys_info

def writer(sys_info):
    cwd = os.getcwd()
    json_path = os.path.join(cwd,"system_info.json")
    f = open(json_path,"w+")
    json_writer = json.dumps(sys_info,indent=4)
    f.write(json_writer)
    f.close()