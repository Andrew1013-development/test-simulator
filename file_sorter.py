import os
import shutil
import time

__version__ = "1.2.0"

def sorter(directory, debug_short, debug_full): 
    #variable
    folder_name_list = []
    folder_name_prev = ""
    total_file_count = 0
    
    start = time.time()
    #fetch from filenames
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            folder_name_pres = filename[0:8]
            if (folder_name_pres != folder_name_prev):
                folder_name_list.append(f"{folder_name_pres[0:4]}-{folder_name_pres[4:6]}-{folder_name_pres[6:8]}")
                folder_name_prev = folder_name_pres
            if debug_full:
                print(os.path.join(directory,filename))
            total_file_count += 1

    #creating files
    for folder_name in folder_name_list:
        if debug_full:
            print(os.path.join(directory,folder_name))
        try:
            os.mkdir(os.path.join(directory,folder_name))
        except OSError as error:
            print(error)

    # moving files
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            old_path = os.path.join(directory,filename)
            new_path = os.path.join(directory,f"{filename[0:4]}-{filename[4:6]}-{filename[6:8]}\\{filename}")
            if debug_full:
                print(new_path)
            shutil.move(old_path,new_path)
    end = time.time()

    if debug_short:
        print("----------------------------STAT----------------------------")
        print(f"Moved {total_file_count} files")
        print(f"Total folders count: {len(folder_name_list)}")
        print(f"Time taken to sort: {(end-start)} seconds")
        print()
    
    return end-start