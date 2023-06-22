import os
import time
from logger import logger_module

__version__ = "2.3.1 | 1.2.1"

def remover(directory, debug_short, debug_full): 
    total_files = 0

    logger_module.info("remover function started")
    logger_module.info("removing files")
    for path in os.scandir(directory):
        #convert DirEntry to usable path
        path_usable = os.path.realpath(path)
        if debug_full:
            print(f"Scanned {path_usable}")
        if os.path.isfile(path_usable):
            #delete file
            if debug_full:
                print(f"Deleting {path_usable}")
            os.remove(path_usable)
            total_files += 1
        else :
            #recursively search for files until isfile() -> True
            total_files += remover(path_usable,debug_short,debug_full)
    logger_module.info("done removing files")
    
    #remove the parent folder itself
    os.rmdir(directory)
    logger_module.info("remover function stopped")
    
    return total_files

def reporter(directory, debug_short, debug_full) -> float:
    sum_of_files_removed = 0
    
    logger_module.info("reporter function started")
    start = time.time()
    sum_of_files_removed = remover(directory,debug_short,debug_full)
    end = time.time()
    logger_module.info("reporter function stopped")
    
    if debug_short or debug_full:
        print("----------------------------STAT----------------------------")
        print(f"Files deleted: {sum_of_files_removed} files")
        print(f"Time taken to clean the folder: {(end-start)} seconds")
        print()

    return end-start