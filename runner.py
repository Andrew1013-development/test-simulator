import sys
import time
import platform
import importlib.metadata
import logging
import file_remover_2
import file_sorter_2
import file_remover
import file_sorter
import file_generator
import file_seeker
import file_copier
from rich.console import Console
from rich.tree import Tree
from rich.table import Table

console = Console()
__version__ = "1.5.6"

def show_credits():
    #create table
    credit_table = Table(title="Credits",caption="Made with rich.table")
    
    #add columns
    credit_table.add_column("Author",style="green")
    credit_table.add_column("Part of codebase",style="yellow")
    credit_table.add_column("Version used in codebase",style="cyan")
    credit_table.add_column("Notes (if applicable)",style="magenta")

    #add rows
    credit_table.add_row("Andrew1013","runner.py",__version__,"")
    credit_table.add_row("Andrew1013","file_generator.py",file_generator.__version__,"")
    credit_table.add_row("Andrew1013","file_sorter.py",file_sorter.__version__,"")
    credit_table.add_row("Andrew1013","file_remover.py",file_remover.__version__,)
    credit_table.add_section()
    credit_table.add_row("Andrew1013","file_copier.py",file_copier.__version__,"WIP")
    credit_table.add_row("Andrew1013","file_seeker.py",file_seeker.__version__,"WIP")
    credit_table.add_row("Andrew1013","file_sorter_2.py",file_sorter_2.__version__,"WIP")
    credit_table.add_row("Andrew1013","file_remover_2.py",file_remover_2.__version__,"WIP")
    credit_table.add_section()
    credit_table.add_row("Python Software Organization","Python 3",platform.python_version(),"")
    credit_table.add_row("Textualize","[italic]Rich library[/italic]",importlib.metadata.version("rich"),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]os[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]sys[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]shutil[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]time[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]platform[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Python Standard Modules Maintainers","[italic]importlib[/italic] Module",platform.python_version(),"")
    credit_table.add_row("Plotly","[italic]Plotly[/italic] graphing library",importlib.metadata.version("plotly"),"")
    
    #print table
    console.print(credit_table)
    console.print("[italic]i am dying pls send help pls[/italic]")


def schematic_view():
    print("Schematic view of runner.py and its functions / dependencies")
    runner_tree = Tree("runner.py")
    runner_tree.add("schematic_view()")
    runner_tree.add("file_generator.py").add("generator()").add("random_string()")
    runner_tree.add("file_seeker.py (work in progress)")
    #runner_tree.add("file_seeker.py").add("seeker()").add("flatten_list()")
    runner_tree.add("file_sorter.py").add("sorter()")
    runner_tree.add("file_sorter_2.py (work-in-progress)")
    runner_tree.add("file_remover.py").add("remover()")
    runner_tree.add("file_remover_2.py (work-in-progress)")
    console.print(runner_tree)

def runner(directory, debug_short, dates, debug_full):
    if debug_short or debug_full:
        print("----------INFORMATION----------")
        print(f"testing directory: {directory}")    
        print(f"short debug flag: {debug_short}")
        print(f"full debug flag: {debug_full}")
        print(f"folders count: {dates}")
        print()
    
    #main code
    current_run = 1
    start = time.time()
    if debug_short or debug_full:
        print("----------GENERATOR RUNNING----------")
    generator_time,num_files = file_generator.generator(directory,debug_short,dates,debug_full)
    if debug_short or debug_full:
        console.log(f"Generation completed")
    if debug_short or debug_full:
        print("----------SORTER RUNNING----------")
    sorter_time = file_sorter.sorter(directory,debug_short,debug_full) 
    if debug_short or debug_full:
        console.log("Sorting completed")
    if debug_short or debug_full:
        print("----------REMOVER RUNNING----------")
    remover_time = file_remover.reporter(directory,debug_short,debug_full)
    if debug_short or debug_full:
        console.log("Removing completed")
    end = time.time()
    if debug_short or debug_full:
        console.log(f"Iteration finished after {round(end - start,3)} seconds")
    #print()
    
    execution_time = end - start
    delta_time = execution_time - (generator_time + sorter_time + remover_time)
    if debug_full or debug_short:
        print("----------------------------EXECUTION INFORMATION---------------------------")
        print(f"Total time to execute all 3 functions (runner time): {round(execution_time,3)} seconds")
        print(f"Individual time of each segment (individual function time):")
        print(f"\tGenerator: {round(generator_time,3)} seconds ({round(generator_time / (end-start) * 100,3)}% of runtime)")
        print(f"\tSorter: {round(sorter_time,3)} seconds ({round(sorter_time / (end-start) * 100,3)}% of runtime)")
        print(f"\tRemover: {round(remover_time,3)} seconds ({round(remover_time / (end-start) * 100,3)}% of runtime)")
        print(f"Time dilation (delta): {round(delta_time,3)} seconds ({round((end - start - (generator_time + sorter_time + remover_time)) / (end - start) * 100,3)}% of runtime)")
    
    #export information
    return [dates,execution_time, generator_time, sorter_time, remover_time, delta_time,num_files]

if __name__ == "__main__":
    dbg = False
    dbg_detail = False
    n_dates = 1
    
    if (len(sys.argv) == 5) : 
        #6 full arguments
        test_dir = sys.argv[1]
        if sys.argv[2] == "-debug":
            dbg = True
        elif sys.argv[2] == "-nodebug":
            dbg = False
        else :
            print("Invaild option for debug flag, defaulting to no short debug output.")
        if sys.argv[3] == "-nofulldebug":
            dbg_detail = False
        elif sys.argv[3] == "-fulldebug":
            dbg_detail = True
        else:
            print("Invaild option for detailed debug flag, defaulting to no detailed debug output.")
        if int(sys.argv[4]) > 0:
            n_dates = int(sys.argv[4])
        else :
            print("Invaild number entered, defaulting to 1")
        #run until finished or Ctrl-C
        try:
            runner(test_dir,dbg, n_dates,dbg_detail)
        except KeyboardInterrupt:
            print("Ctrl-C triggered, exiting....")
            file_remover.remover(test_dir, dbg, dbg_detail)
            console.print_exception(show_locals=True)
            exit(1)
    else :
        if len(sys.argv) == 2:
            if sys.argv[1] == "help":
                print("""Usage: 
            python3 runner.py [dir] [debug_flag] [fulldebug_flag] [n_dates]
            python3 runner.py help / schematic

            [dir]: specifies the directory where the runner will use to store files
            [debug_flag]: tells the script whether to use short debug output
                -debug: True -> short debug output enabled
                -nodebug: False -> short debug output disabled
            [fulldebug_flag]: tells the script whether to use detailed debug output
                -fulldebug: True -> full debug output enabled.
                -nofulldebug: False -> full debug output disabled
                Note: if fulldebug_flag is True but debug_flag is False, script will default revert debug_flag to True.
            [n_dates]: specifies how many "folders" to be created before sorting (used for generating test files)
            
            help: display instructions on how to use this script
            schematic: shows schematic of this script (a test of rich.tree)
            version: shows versions of this script and its dependencies
            credits: shows credits (obviously)""")
            elif sys.argv[1] == "schematic":
                schematic_view()
            elif sys.argv[1] == "version":
                print(f"runner.py version {__version__}")
                print(f"file_generator.py version {file_generator.__version__}")
                print(f"file_seeker.py version {file_seeker.__version__}")
                print(f"file_sorter.py version {file_sorter.__version__}")
                print(f"file_sorter_2.py version (in testing) {file_sorter_2.__version__}")
                print(f"file_remover.py version {file_remover.__version__}")
                print(f"file_remover_2.py version (in testing) {file_remover_2.__version__}")
            elif sys.argv[1] == "credits":
                show_credits()
            else :
                print(f"Invaild second argument '{sys.argv[1]}'.")
        else :
            print(f"Expected 4 arguments, supplied {len(sys.argv) - 1} arguments.")