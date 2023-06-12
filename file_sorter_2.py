import os
import shutil
import time

__version__ = "2.3.0" #update to 2.x.x once merged


def sorter(pathlist, basepath, debug_short, debug_full): 
    #variable
    filepath_sorted = []
    folder_name_prev = ""
    folder_count = 0

    start = time.time()
    for filepath in pathlist:
        filename = os.path.basename(filepath)
        folder_name = f"{filename[0:4]}-{filename[4:6]}-{filename[6:8]}"
        if folder_name != folder_name_prev:
            dst = os.path.join(basepath,folder_name)
            os.mkdir(dst)
            shutil.move(filepath,os.path.join(dst,filename))
            folder_name_prev = folder_name
            filepath_sorted.append(os.path.join(dst,filename))
            folder_count += 1
        else :
            dst = os.path.join(basepath,folder_name,filename)
            shutil.move(filepath,dst)
            filepath_sorted.append(dst)
    end = time.time()

    if debug_short:
        print("----------------------------STAT----------------------------")
        print(f"Moved {len(filepath_sorted)} files")
        print(f"Total folders count: {folder_count}")
        print(f"Time taken to sort: {(end-start)} seconds")
        print()
    
    return end-start, filepath_sorted