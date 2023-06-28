import sys
import platform
import subprocess
import plotly.graph_objects

platform_flag = platform.platform().split("-")[0]
__version__ = "1.0.1"

if __name__ == "__main__":    
    if len(sys.argv) == 6:
        if sys.argv[2] != "-debug":
            sys.argv[2] = "-nodebug"
        if sys.argv[3] != "-fulldebug":
            sys.argv[3] = "-nofulldebug"
        if sys.argv[5] != "-nofile":
            sys.argv[5] = "-file"
        
        if platform_flag == "Windows":
            subprocess.run("mingw32-make")
            executable_name = "runner_cpp.exe"
        else:
            subprocess.run("make")
            executable_name = "./runner_cpp.out"
        
        with open("runtime_iterations_information_cpp.txt",mode="r+") as f:
            f.truncate(0)
        
        for i in range(1,int(sys.argv[4])+1):
            print(" ".join([executable_name,sys.argv[1],sys.argv[2],sys.argv[3],str(i),sys.argv[5]]))
            cpp_process = subprocess.Popen([executable_name,sys.argv[1],sys.argv[2],sys.argv[3],str(i),sys.argv[5]],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            cpp_process_out = cpp_process.communicate()
            lines = cpp_process_out[0].strip().splitlines()
            for line in lines:
                print(line.decode("utf-8"))

        runtime_list = []
        with open("runtime_iterations_information_cpp.txt",mode="r+") as f:
            for string in f.readlines():
                runtime_list.append([float(ele) for ele in string.strip().split(",") if ele != ""]) # holy shit 1 liner
                
        fig = plotly.graph_objects.Figure(
            data = [plotly.graph_objects.Bar(x=[i for i in range(1,int(sys.argv[4])+1)] , y=[runtime_list[i][1] for i in range(0,int(sys.argv[4]))])],
            layout = plotly.graph_objects.Layout(
                title = plotly.graph_objects.layout.Title(text="test_cpp")
            )
        )
        fig.show()
    else:
        print("no plotter_helper for you")