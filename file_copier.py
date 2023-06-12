import os
import shutil
import time

__version__ = "1.1.0"

def copier(directory1, directory2, debug_short, debug_full):
    files_copied = 0
    
    start = time.time()
    os.mkdir(directory2)
    for filepath in os.scandir(directory1):
        src = os.path.realpath(filepath)
        path, filename = os.path.split(filepath)
        if debug_full:
            print(f"{src} -> {directory2}")
        shutil.copy2(src,os.path.join(directory2,filename))
        files_copied += 1
    end = time.time()

    if debug_short or debug_full:
        print("--------------------STATS--------------------")
        print(f"Total files copied: {files_copied} files")
        print(f"Time taken to copy test files: {(end-start)} seconds")
        print()
    
    return end - start