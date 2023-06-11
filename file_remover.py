import os
import time

__version__ = "2.1.0 | 1.0.0"

def remover(directory, debug_short, debug_full): 
    total_files = 0

    if debug_short:
        print("Fetching and removing files.....")
    for path in os.scandir(directory):
        #convert DirEntry to usable path
        path_usable = os.path.realpath(path)
        if debug_full:
            print(path_usable)
        if os.path.isfile(path_usable):
            #delete file
            os.remove(path_usable)
        else :
            #recursively search for files until isfile() -> True
            total_files += remover(path_usable,debug_short,debug_full)
    
    #remove the parent folder itself
    os.rmdir(directory)

    if debug_short:
        print(f"Removed {total_files} files.")
        print()

    return total_files

def reporter(directory, debug_short, debug_full):
    sum_of_files_removed = 0
    
    start = time.time()
    sum_of_files_removed = remover(directory,debug_short,debug_full)
    end = time.time()
    
    if debug_short or debug_full:
        print("----------------------------STAT----------------------------")
        print(f"Files deleted: {sum_of_files_removed} files")
        print(f"Time taken to clean the folder: {(end-start)} seconds")
        print()

    return end-start