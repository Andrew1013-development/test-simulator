import os
import time

__version__ = "1.2.2"

def seeker(directory, debug_short, debug_full):
    path_list = []
    start = time.time()
    for path in os.scandir(directory):
        #convert DirEntry object to a usable path
        path_usable = os.path.realpath(path)
        if os.path.isfile(path_usable):
            #a file path is ascertained
            if debug_full:
                print(f"Seeked {path_usable}")
            path_list.append(path_usable)
        else :
            #search inside folders recursively until all is a file
            path_list_temp = seeker(path_usable,debug_short,debug_full)
            for i in range(0,len(path_list_temp)):
                path_list.append(path_list_temp[i])
    end = time.time()

    if debug_short or debug_full:
        print("----------------------------STAT----------------------------")
        print(f"Files found: {len(path_list)} files")
        print(f"Time taken to seek the entire directory: {(end-start)} seconds")
        print()
    
    return end-start, path_list 