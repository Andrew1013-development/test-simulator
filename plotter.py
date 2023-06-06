import sys
import runner
import file_remover_2
import file_sorter_2
import file_remover
import file_sorter
import file_generator
import file_seeker
#import matplotlib
from rich.console import Console
from rich.tree import Tree
from rich.progress import Progress, TextColumn, BarColumn, MofNCompleteColumn, SpinnerColumn, TimeElapsedColumn

progress_bar = Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    MofNCompleteColumn(),
    TimeElapsedColumn(),
    transient=True
)
console = Console()
__version__ = "0.12.5"

def schematic_view():
    print("Schematic view of plotter.py, a script to plot time data from runner.py")
    plotter_tree = Tree("plotter.py")
    plotter_tree.add("schematic_view()")
    plotter_tree.add("runner.py").add("runner()")
    plotter_tree.add("file_seeker.py (work in progress)")
    #plotter_tree.add("file_seeker.py").add("seeker()").add("flatten_list")
    plotter_tree.add("file_remover.py").add("remover()")
    plotter_tree.add("file_remover_2.py (work in progress)")
    console.print(plotter_tree)

def plotter(directory, debug, iterations, file_output,debug_full):
    dataset = []
    execution_time = 0
    generator_time = 0
    sorter_time = 0
    remover_time = 0
    delta_time = 0
    total_files = 0
    
    #create data file
    print("Prearing data file.....")
    f_track = open("runtime_iterations_information.txt","w+")
    f_track.truncate(0)
    print("Tracking data created.")
    #print()
    
    #write raw dataset into file
    with progress_bar as progress:
        task = progress.add_task("[blue]Executing...", total=iterations)
        progress.start_task(task)
        for i in range(1,iterations + 1):
            if debug or debug_full:
                print(f"---------------RUN NO.{i}---------------")
            temp = runner.runner(directory,debug,i,debug_full)
            dataset.append(temp)

            execution_time += temp[0]
            generator_time += temp[1]
            sorter_time += temp[2]
            remover_time += temp[3]
            delta_time += temp[4]
            total_files += temp[5]
            progress.update(task,advance=1)

            if (file_output):
                f_track.writelines([str(data) for data in temp])
                f_track.write('\n')
    f_track.close()
    
    print("----------------------------EXECUTION INFORMATION (SUMMARY)---------------------------")
    print(f"Total files sorted: {total_files} files")
    print(f"Total time to execute all 3 functions: {round(execution_time,3)} seconds")
    print(f"Individual time of each segment:")
    print(f"\tGenerator: {round(generator_time,3)} seconds ({round(generator_time / execution_time * 100,3)}% of runtime)")
    print(f"\tSorter: {round(sorter_time,3)} seconds ({round(sorter_time / execution_time * 100,3)}% of runtime)")
    print(f"\tRemover: {round(remover_time,3)} seconds ({round(remover_time / execution_time * 100,3)}% of runtime)")
    print(f"Time dilation (delta): {round(delta_time,3)} seconds ({round(delta_time / execution_time * 100,3)}% of runtime)")
    print()

    print("----------------------------EXECUTION INFORMATION (IN DETAILS)---------------------------")
    for i in range(0,iterations):
        print(f"Run No.{i+1}")
        print(f"Total files sorted: {dataset[i][5]} files")
        print(f"Total time to execute all 3 functions: {round(dataset[i][0],3)} seconds")
        print(f"Individual time of each segment:")
        print(f"\tGenerator: {round(dataset[i][1],3)} seconds ({round(dataset[i][1] / dataset[i][0] * 100,3)}% of runtime)")
        print(f"\tSorter: {round(dataset[i][2],3)} seconds ({round(dataset[i][2] / dataset[i][0] * 100,3)}% of runtime)")
        print(f"\tRemover: {round(dataset[i][3],3)} seconds ({round(dataset[i][3] / dataset[i][0] * 100,3)}% of runtime)")
        print(f"Time dilation (delta): {round(dataset[i][4],3)} seconds ({round(dataset[i][4] / dataset[i][0] * 100,3)}% of runtime)")
        print("-" * 25)

if __name__ == "__main__":
    dbg_flag = False
    dbg_full_flag = False
    fout = True
    if (len(sys.argv) == 6) :
        #6 full arguments
        test_dir = sys.argv[1]
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
        n_iters = int(sys.argv[4])
        if sys.argv[5] == "-file":
            fout = True
        elif sys.argv[5] == "-nofile":
            fout = False
        else :
            print("Invaild option for file output flag, defaulting to file output enabled.")
        
        #run until finished or Ctrl-C
        try:
            plotter(test_dir,dbg_flag,n_iters,fout,dbg_full_flag)
        except KeyboardInterrupt:
            print("Ctrl-C triggered, exiting....")
            file_remover.remover(test_dir, dbg_flag, dbg_full_flag)
            console.print_exception(show_locals=True)
            exit()
    else :
        #only 2 arguments (help / schematic / version (coming soon))
        if len(sys.argv) == 2:
            if sys.argv[1] == "schematic":
                schematic_view()
            elif sys.argv[1] == "help":
                print("""Usage:
            python3 plotter.py [dir] [debug_flag] [fulldebug_flag] [iters] [file_out]
            python3 plotter.py help/schematic/version
            
            [dir]: specifies the directory where the runner will use to store files
            [debug_flag]: tells the script whether to use short debug output
                -debug: True -> short debug output enabled
                -nodebug: False -> short debug output disabled
            [fulldebug_flag]: tells the script whether to use detailed debug output
                -fulldebug: True -> full debug output enabled.
                -nofulldebug: False -> full debug output disabled
            [iters]: specifies how many times to run runner.py with increasing "n_dates"
            [file_out] tells the script whethere to save time results into a text file
            
            help: display instructions on how to use this script
            schematic: shows schematic of this script (a test of rich.tree)
            version: shows versions of this script and its dependencies
            credits: shows credits (obviously)""")
            elif sys.argv[1] == "version":
                print(f"plotter.py version {__version__}")
                print(f"runner.py version {runner.__version__}")
                print(f"file_generator.py version {file_generator.__version__}")
                print(f"file_seeker.py version {file_seeker.__version__}")
                print(f"file_sorter.py version {file_sorter.__version__}")
                print(f"file_sorter_2.py version (in testing) {file_sorter_2.__version__}")
                print(f"file_remover.py version {file_remover.__version__}")
                print(f"file_remover_2.py version (in testing) {file_remover_2.__version__}")
            else :
                print(f"Invaild second argument '{sys.argv[1]}'.")
        else :
            print(f"Expected 5 arguments, supplied {len(sys.argv) - 1} arguments")