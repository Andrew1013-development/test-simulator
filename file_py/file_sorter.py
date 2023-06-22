import os
import shutil
import time
from logger import logger_module

__version__ = "1.3.1"

def sorter(directory, debug_short, debug_full) -> float: 
    #variable
    folder_name_list = []
    folder_name_prev = ""
    total_file_count = 0
    logger_module.info("sorter function started")    
    start = time.time()
    logger_module.info("fetching files to sort")
    #fetch from filenames
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            folder_name_pres = filename[0:8]
            if (folder_name_pres != folder_name_prev):
                folder_name_list.append(f"{folder_name_pres[0:4]}-{folder_name_pres[4:6]}-{folder_name_pres[6:8]}")
                folder_name_prev = folder_name_pres
            total_file_count += 1
    logger_module.info("done fetching files to sort")

    #creating folders
    logger_module.info("creating sorting folders")
    for folder_name in folder_name_list:
        if debug_full:
            print(f"Creating {os.path.join(directory,folder_name)}")
        try:
            os.makedirs(os.path.join(directory,folder_name),exist_ok=True)
        except OSError:
            logger_module.error("cannot create sorting folders")
            print("Cannot create sorting directories")
            exit(1)
    logger_module.info("done creating sorting folders")

    # moving files
    logger_module.info("moving files to their proper location")
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            old_path = os.path.join(directory,filename)
            new_path = os.path.join(directory,f"{filename[0:4]}-{filename[4:6]}-{filename[6:8]}\\{filename}")
            if debug_full:
                print(f"Moving {old_path} to new_path")
            shutil.move(old_path,new_path)
    logger_module.info("done moving files to their proper location")
    end = time.time()
    logger_module.info("sorter function stopped.")
    if debug_short:
        print("----------------------------STAT----------------------------")
        print(f"Moved {total_file_count} files")
        print(f"Total folders count: {len(folder_name_list)}")
        print(f"Time taken to sort: {(end-start)} seconds")
        print()
    
    return end-start
