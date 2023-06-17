import os
import psutil
import platform
import json

__version__ = "1.0.0"

def fetcher() -> dict[str, str]:
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
        "process_id": f"{os.getpid()}"
    }

    return sys_info

def writer(sys_info):
    f = open("system_info.json","w+")
    json_writer = json.dumps(sys_info,indent=4)
    f.write(json_writer)
    f.close()