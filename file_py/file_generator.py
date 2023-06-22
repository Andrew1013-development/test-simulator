import os
import shutil
import random
import time
import string
from logger import logger_module

__version__ = "1.4.1"

def random_string(length):
    result_str = ""
    for i in range(0,length):
        result_str += random.choice(string.ascii_letters)
    return result_str

def generator(directory, debug_short, dates, debug_full) -> tuple[float, int] :
    #variable
    table = {}
    total_files = 0
    file_check = [""]
    logger_module.info("generator function started")
    
    # setting up
    logger_module.info("creating test directory")
    try:
        if debug_short:
            print("Creating test folder....")
        os.makedirs(directory,exist_ok = True) #create a nested directory
    except OSError:
        logger_module.error("test folder cannot be created")
        print("Cannot create folder, exiting...")
        exit(1)

    start = time.time()
    #generating dates (will be used as folder structures)
    logger_module.info("creating file dates + amount of files in each date")
    for i in range(0,dates):
        year = random.randrange(2010,2023)
        month = random.randrange(1,12)
        day = random.randrange(1,28)
        files = random.randrange(10,1000)
        table[f"{year}{month:02d}{day:02d}"] = files
        total_files += files

    # create test files
    logger_module.info("creating test files")
    for date in table.keys():
        for file_num in range(0,table[date]):
            hour = random.randrange(0,23)
            minute = random.randrange(0,59)
            second = random.randrange(0,59)

            try:
                file_check.index(f"{date}_{hour:02d}{minute:02d}{second:02d}")
                file_dir = os.path.join(directory,f"{date}_{hour:02d}{minute:02d}{second:02d}.txt")
            except ValueError :
                file_dir = os.path.join(directory,f"{date}_{hour:02d}{minute:02d}{second:02d}_{random_string(random.randrange(1,25))}.txt")

            if debug_full:
                print(f"Creating {file_dir}")
            with open(file_dir,"w+") as f:
                f.writelines(f"{date}_{hour:02d}{minute:02d}{second:02d}")

            file_check.append(f"{date}_{hour:02d}{minute:02d}{second:02d}")
        #print(f"Created {table[date]} of date {date}")
    logger_module.info("done creating test files")
    end = time.time()

    logger_module.info("generator function stopped")

    if debug_short:
        print("--------------------STATS--------------------")
        print(f"Total dates created: {dates} dates")
        print(f"Total files created: {total_files} files")
        print(f"Time taken to generate test files: {(end-start)} seconds")
        print()

    return end-start, total_files