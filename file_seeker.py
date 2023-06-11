import os
import time
import itertools

__version__ = "1.0.0"


def flatten_list(big_array):
    return list(itertools.chain.from_iterable(big_array))

def seeker(directory, debug, debug_full):
    path_list = []
    for path in os.scandir(directory):
        #convert DirEntry object to a usable path
        path_usable = os.path.realpath(path)
        if os.path.isfile(path_usable):
            #a file path is ascertained
            if debug or debug_full:
                print(path_usable)
            path_list.append(path_usable)
        else :
            #search inside folders recursively until all is a file
            path_list.append(seeker(path_usable,debug,debug_full))
            flatten_list(path_list)
    
    return path_list