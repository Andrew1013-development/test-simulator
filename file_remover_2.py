import os
import shutil
import time

__version__ = "2.2.1" #update to 2.x.x once merged

def remover(path_list, base_path, debug_short, debug_full) -> float:
    start = time.time()
    for path in path_list:
        if debug_full:
            print(path)
        os.remove(path)
    
    for folderpath in os.scandir(base_path):
        os.rmdir(os.path.realpath(folderpath))
    os.rmdir(base_path)
    end = time.time()

    if debug_short or debug_full:
        print("----------------------------STAT----------------------------")
        print(f"Files deleted: {len(path_list)} files")
        print(f"Time taken to clean the folder: {(end-start)} seconds")
        print()

    return end - start