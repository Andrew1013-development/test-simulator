import os
import shutil
import time
from logger import logger_module

__version__ = "1.3.1"

def copier(directory1, directory2, debug_short, debug_full) -> float:
    files_copied = 0
    logger_module.info("copier function started")
    start = time.time()
    os.makedirs(directory2)
    logger_module.info("parent directory created")
    for filepath in os.scandir(directory1):
        src = os.path.realpath(filepath)
        path, filename = os.path.split(filepath)
        dst = os.path.join(directory2, filename)
        logger_module.info("moving files from directory 1 to directory 2")
        if debug_full:
            print(f"Moving {src} -> {dst}")
        shutil.copy2(src,dst)
        files_copied += 1
    logger_module.info("done copying test files")
    end = time.time()
    logger_module.info("copier function stopped")

    if debug_short or debug_full:
        print("--------------------STATS--------------------")
        print(f"Total files copied: {files_copied} files")
        print(f"Time taken to copy test files: {(end-start)} seconds")
        print()
    
    return end - start