import os
import shutil
import time

__version__ = "2.0.0" #update to 2.x.x once merged

def remover(path_list, debug_short, debug_full):
    start = time.time()
    for path in path_list:
        os.remove(path)
    end = time.time()
    
    if debug_short:
        print("----------------------------STAT----------------------------")
        print(f"Time taken to clean the folder: {(end-start)} seconds")
        print()

    return end-start