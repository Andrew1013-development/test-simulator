import os
import shutil
import time

__version__ = "1.0.0"

def remover(directory, debug_short, debug_full):
    start = time.time()
    shutil.rmtree(directory,ignore_errors=False, onerror=None)
    end = time.time()
    
    if debug_short:
        print("----------------------------STAT----------------------------")
        print(f"Time taken to clean the folder: {(end-start)} seconds")
        print()

    return end-start