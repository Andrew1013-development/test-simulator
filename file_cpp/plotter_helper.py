import sys
import platform
import subprocess
import plotly.graph_objects

platform_flag = platform.platform().split("-")[0]
__version__ = "1.0.0"

if __name__ == "__main__":    
    if sys.argv[2] == "-debug" or sys.argv[2] == "-nodebug":
        dbg_flag = True
    else:
        print("you sus")
        sys.argv[2] = "-nodebug"
    
    if sys.argv[3] == "-fulldebug" or "-nofulldebug":
        pass
    else:
        print("you sus")
        sys.argv[3] = "-nofulldebug"
    
    if platform_flag == "Windows":
        subprocess.run("mingw32-make")
        executable_name = "runner_cpp.exe"
    else:
        subprocess.run("make")
        executable_name = "./runner_cpp.out"

    for i in range (1,int(sys.argv[4])+1):
        cpp_process = subprocess.Popen([executable_name,sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        cpp_process_out = cpp_process.communicate()
        lines = cpp_process_out[0].strip().splitlines()
        for line in lines:
            print(line.decode("utf-8"))