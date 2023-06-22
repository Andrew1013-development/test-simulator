# external modules / libraries
import os
import sys
import csv
import importlib.metadata
import platform
import logger
import tracemalloc
import runner
import threading
from rich.console import Console
from rich.tree import Tree
from rich.table import Table
from rich.progress import Progress, TextColumn, BarColumn, MofNCompleteColumn, SpinnerColumn, TimeElapsedColumn

# my written functions
import file_remover_2
import file_sorter_2
import file_remover
import file_sorter
import file_generator
import file_seeker
import file_copier
import telemetry
import sys_fetcher
import sys_uploader
if int(platform.python_version_tuple()[1]) < 12:
    #import matplotlib
    pass
else :
    import plotly.graph_objects

progress_bar = Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    MofNCompleteColumn(),
    TimeElapsedColumn(),
    transient=True
)
console = Console()
__version__ = "2.0.0-WIP-2"

def show_credits():
    #create table
    credit_table = Table(title="Credits",caption="Made with rich.table")
    
    #add columns
    credit_table.add_column("Author",style="green")
    credit_table.add_column("Part of codebase",style="yellow")
    credit_table.add_column("Version used in codebase",style="cyan")
    credit_table.add_column("Notes (if applicable)",style="magenta")
    
    #add rows
    credit_table.add_row("Andrew1013","plotter.py",__version__,"")
    credit_table.add_row("Andrew1013","runner.py",runner.__version__,"")
    credit_table.add_row("Andrew1013","logger.py",logger.__version__,"")
    credit_table.add_row("Andrew1013","telemetry.py",telemetry.__version__,"")
    credit_table.add_row("Andrew1013","file_generator.py",file_generator.__version__,"")
    credit_table.add_row("Andrew1013","file_sorter.py",file_sorter.__version__,"")
    credit_table.add_row("Andrew1013","file_remover.py",file_remover.__version__,"")
    credit_table.add_row("Andrew1013","sys_fetcher.py",sys_fetcher.__version__,"")
    credit_table.add_row("Andrew1013","sys_uploader.py",sys_uploader.__version__,"")
    
    credit_table.add_section()
    
    credit_table.add_row("Andrew1013","file_copier.py",file_copier.__version__,"WIP")
    credit_table.add_row("Andrew1013","file_seeker.py",file_seeker.__version__,"WIP")
    credit_table.add_row("Andrew1013","file_sorter_2.py",file_sorter_2.__version__,"WIP")
    credit_table.add_row("Andrew1013","file_remover_2.py",file_remover_2.__version__,"WIP")
    
    credit_table.add_section()
    
    credit_table.add_row("Python Software Organization","Python 3",platform.python_version(),"")
    credit_table.add_row("Textualize","[italic]Rich library[/italic]",importlib.metadata.version("rich"),"")
    credit_table.add_row("Giampaolo Rodola","[italic]psutil[/italic] Module",importlib.metadata.version("psutil"),"")
    credit_table.add_row("The MongoDB Python Team","[italic]pymongo[/italic] Module",importlib.metadata.version("pymongo"),"")
    credit_table.add_row("plotly.com","[italic]plotly[/italic] graphing library",importlib.metadata.version("plotly"),"Only supported on Python 3.12.x")
    credit_table.add_row("Kenneth Reitz","[italic]certifi[/italic] library",importlib.metadata.version("certifi"),"")
    # if int(platform.python_version_tuple()[1]) < 12:
        #credit_table.add_row("matplotlib.org","[italic]matplotlib[/italic] graphing library",importlib.metadata.version("matplotlib"),"Only supported on Python 3.11.x and below")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]os[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]sys[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]shutil[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]time[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]datetime[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]platform[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]importlib[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]tracemalloc[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]logging[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]string[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]threading[/italic] Module",platform.python_version(),"")
   
    #print table
    console.print(credit_table)
    console.print("[italic]i am dying pls send help pls[/italic]")

def path_checker(path):
    path.replace('"','')
    if path == os.path.dirname(__file__):
        return ""
    if os.path.isdir(path):
        return path
    else:
        return os.path.join(os.path.dirname(__file__),path)

def schematic_view():
    print("Schematic view of plotter.py, a script to plot time data from runner.py")
    plotter_tree = Tree("plotter.py")
    plotter_tree.add("plotter() | schematic_view() | path_checker()")
    plotter_tree.add("runner.py").add("runner()")
    plotter_tree.add("logger.py").add("logger")
    plotter_tree.add("file_seeker.py").add("seeker() | flatten_list()")
    plotter_tree.add("file_remover.py").add("remover() | reporter()")
    plotter_tree.add("file_seeker_2.py (work in progress)")
    plotter_tree.add("file_remover_2.py (work in progress)")
    plotter_tree.add("telemetry.py").add("sys_fetcher.py | sys_uploader.py").add("fetcher() | writer() | pinger() | uploader()")
    console.print(plotter_tree)

def plotter(directory, debug, debug_full, iterations, file_output):
    dataset = []
    iters = 0
    execution_time = 0
    execution_time_list = []
    generator_time = 0
    generator_time_list = []
    sorter_time = 0
    sorter_time_list = []
    remover_time = 0
    remover_time_list = []
    delta_time = 0
    delta_time_list = []
    total_files = 0
    total_files_list = []
    #create data file
    print("Prearing data file.....")
    f_track = open("runtime_iterations_information.txt","w+")
    f_track.truncate(0)
    print("Tracking data file created.")
    logger.logger_module.debug("runtime_iterations_information.txt created")
    #print()
    
    #write raw dataset into file
    with progress_bar as progress:
        task = progress.add_task("[blue]Executing...", total=iterations)
        progress.start_task(task)
        for i in range(1,iterations + 1):
            if debug or debug_full:
                print(f"---------------RUN NO.{i}---------------")
            logger.logger_module.debug(f"run no.{i} started")
            temp = runner.runner(directory,debug,i,debug_full)
            dataset.append(temp)

            execution_time += temp[1]
            execution_time_list.append(temp[1])
            generator_time += temp[2]
            generator_time_list.append(temp[2])
            sorter_time += temp[3]
            sorter_time_list.append(temp[3])
            remover_time += temp[4]
            remover_time_list.append(temp[4])
            delta_time += temp[5]
            delta_time_list.append(temp[5])
            total_files += temp[6]
            total_files_list.append(temp[6])
            progress.update(task,advance=1)

            if (file_output):
                f_track.writelines(",".join([str(data) for data in temp]))
                f_track.write('\n')
                logger.logger_module.debug(f"written run no.{i}'s times into runtime_iterations_information.txt")
            logger.logger_module.debug(f"run no.{i} finished")
    f_track.close()
    logger.logger_module.debug("done writing to runtime_iterations_information.txt")
    print()
    
    print("----------------------------EXECUTION INFORMATION (SUMMARY)---------------------------")
    print(f"Total files sorted: {total_files} files")
    print(f"Total time to execute all 3 functions: {round(execution_time,3)} seconds")
    print(f"Individual time of each segment:")
    print(f"\tGenerator: {round(generator_time,3)} seconds ({round(generator_time / execution_time * 100,3)}% of runtime)")
    print(f"\tSorter: {round(sorter_time,3)} seconds ({round(sorter_time / execution_time * 100,3)}% of runtime)")
    print(f"\tRemover: {round(remover_time,3)} seconds ({round(remover_time / execution_time * 100,3)}% of runtime)")
    print(f"Time dilation (delta): {round(delta_time,3)} seconds ({round(delta_time / execution_time * 100,3)}% of runtime)")
    print()

    if debug or debug_full:
        print("----------------------------EXECUTION INFORMATION (IN DETAILS)---------------------------")
        for i in range(0,iterations):
            print(f"Run No.{i+1}")
            print(f"Total files sorted: {dataset[i][6]} files")
            print(f"Total time to execute all 3 functions: {round(dataset[i][1],3)} seconds")
            print(f"Individual time of each segment:")
            print(f"\tGenerator: {round(dataset[i][2],3)} seconds ({round(dataset[i][2] / dataset[i][1] * 100,3)}% of runtime)")
            print(f"\tSorter: {round(dataset[i][3],3)} seconds ({round(dataset[i][3] / dataset[i][1] * 100,3)}% of runtime)")
            print(f"\tRemover: {round(dataset[i][4],3)} seconds ({round(dataset[i][4] / dataset[i][1] * 100,3)}% of runtime)")
            print(f"Time dilation (delta): {round(dataset[i][5],3)} seconds ({round(dataset[i][5] / dataset[i][1] * 100,3)}% of runtime)")
            print("-" * 25)
        print()

    #plotting code
    print("Plotting is not ready for Python 3.11.x and below in this version of plotter.py, exporting to .csv file....")
    with open("runtime_stats.csv",mode="w+",newline="") as csv_file:
        logger.logger_module.debug("runtime_stats.csv created")
        csv_file.truncate(0)
        plot_csv = csv.writer(csv_file,delimiter=",")
        #plot_csv.writerow([f"test result date and time: {current_date_time.strftime("%d/%m/%Y %H:%M:%S")}"])
        plot_csv.writerow(["n_time","execution_time","generator_time","sorter_time","remover_time","delta_time","n_files"])
        logger.logger_module.debug("writing to runtime_stats.csv")
        for datarow in dataset:
            plot_csv.writerow(datarow)
    print("Exported runtime statistics to CSV file.")
    logger.logger_module.debug("done writing to runtime_stats.csv")
    
    if int(platform.python_version_tuple()[1]) >= 12:
        fig = plotly.graph_objects.Figure(
            data = [plotly.graph_objects.Bar(x=[i for i in range(1,n_iters+1)] , y=execution_time_list)],
            layout = plotly.graph_objects.Layout(
                title = plotly.graph_objects.layout.Title(text="test")
            )
        )
        fig.show()
    

if __name__ == "__main__":
    dbg_flag = False
    dbg_full_flag = False
    tlm_flag = True
    fout = True
    n_iters = 1

    if len(sys.argv) == 6:
        #6 full arguments
        test_dir = path_checker(sys.argv[1])
        if test_dir == "":
            print("Invaild test directory specified, test directory should not be the same as script directory.")
            print(f"Script directory: {os.path.dirname(__file__)}")
            exit(1)
        if sys.argv[2] == "-debug": 
            dbg_flag = True
        if sys.argv[2] == "-nodebug":
            dbg_flag = False
        else :
            print("Invaild option for debug flag, defaulting to no debug output.")
        if sys.argv[3] == "-nofulldebug":
            dbg_detail = False
        elif sys.argv[3] == "-fulldebug":
            dbg_detail = True
        else:
            print("Invaild option for detailed debug flag, defaulting to no detailed debug output.")
        if int(sys.argv[4]) > 0:
            n_iters = int(sys.argv[4])
        else :
            print("Invaild number entered, defaulting to 1")
        if sys.argv[5] == "-file":
            fout = True
        elif sys.argv[5] == "-nofile":
            fout = False
        else :
            print("Invaild option for file output flag, defaulting to file output enabled.")
        if sys.argv[6] != "-notelemetry":
            tlm_flag = False
        else:
            pass

        #run until finished or Ctrl-C
        tracemalloc.start()
        try:
            #plotter(test_dir,dbg_flag,n_iters,fout,dbg_full_flag)
            
            # create 2 threads of execution
            main_process = threading.Thread(target=plotter,args=(test_dir,dbg_flag,dbg_full_flag,n_iters,fout,))
            telemetry_process = threading.Thread(target=telemetry.telemetry,args=(dbg_flag,dbg_full_flag,))
            # start execution
            main_process.start()
            if tlm_flag:
                telemetry_process.start()
                # join up the 2 threads
                main_process.join()
                telemetry_process.join()
            
            current_mem, peak_mem = tracemalloc.get_traced_memory()
            print(f"Peak memory used: {round(peak_mem / (1024 ** 2),3)} MB")
            tracemalloc.stop()
        except KeyboardInterrupt:
            print("Ctrl-C triggered, exiting....")
            file_remover.remover(test_dir, dbg_flag, dbg_full_flag)
            logger.logger_module.error("execution halted unexpectedly")
            console.print_exception(show_locals=True)
            current_mem, peak_mem = tracemalloc.get_traced_memory()
            print(f"Peak memory usage: {round(peak_mem / (1024 ** 2),3) }MB")
            tracemalloc.stop()
            exit(1) #specify errorneous exit
            
    else :
        #only 2 arguments (help / schematic / version (coming soon))
        if len(sys.argv) == 2:
            if sys.argv[1] == "schematic":
                schematic_view()
            elif sys.argv[1] == "help":
                print("""Usage:
            python3 plotter.py [dir] [debug_flag] [fulldebug_flag] [iters] [file_out] [telemetry_flag]
            python3 plotter.py credits/help/schematic/version
            
            [dir]: specifies the directory where the runner will use to store files
            [debug_flag]: tells the script whether to use short debug output
                -debug: True -> short debug output enabled
                -nodebug: False -> short debug output disabled
            [fulldebug_flag]: tells the script whether to use detailed debug output
                -fulldebug: True -> full debug output enabled.
                -nofulldebug: False -> full debug output disabled
                Note: if fulldebug_flag is True but debug_flag is False, script will default revert debug_flag to True.
            [iters]: specifies how many times to run runner.py with increasing "n_dates"
            [file_out] tells the script whether to save time results into a text file
            [telemetry_flag] tells the script whether to collect system information and upload it to a database
                -notelemetry: False -> telemetry disabled
            
            help: display instructions on how to use this script
            schematic: shows schematic of this script (a test of rich.tree)
            version: shows versions of this script and its dependencies
            credits: shows credits (obviously)""")
            elif sys.argv[1] == "version":
                print(f"plotter.py version {__version__}")
                print(f"runner.py version {runner.__version__}")
                print(f"telemetry.py version {telemetry.__version__}")
                print(f"logger.py version {logger.__version__}")
                print(f"file_generator.py version {file_generator.__version__}")
                print(f"file_seeker.py version {file_seeker.__version__}")
                print(f"file_sorter.py version {file_sorter.__version__}")
                print(f"file_sorter_2.py version (in testing) {file_sorter_2.__version__}")
                print(f"file_remover.py version {file_remover.__version__}")
                print(f"file_remover_2.py version (in testing) {file_remover_2.__version__}")
                print(f"sys_fetcher.py version {sys_fetcher.__version__}")
                print(f"sys_uploader.py version {sys_uploader.__version__}")
            elif sys.argv[1] == "credits":
                show_credits()
            else :
                print(f"Invaild second argument '{sys.argv[1]}'.")
                logger.logger_module.error("invaild second argument entered")
        else :
            print(f"Expected 5 arguments, supplied {len(sys.argv) - 1} arguments")
            logger.logger_module.error("not enough arguments to continue execution")