import os
from dotenv import load_dotenv
import sys_fetcher
import sys_uploader
from logger import logger_module

__version__ = "1.0.0"

username = "dontbesus"
password = "vb9jsbkAfXww3uc0"
cluster_name = "cluster0"

def telemetry(debug_short, debug_full):
    if debug_short:
        print("Collecting system info....")
    system_info = sys_fetcher.fetcher()
    if debug_short:
        print("Writing to .json file....")
    sys_fetcher.writer(system_info)
    if debug_short:
        print("Uploading to MongoDB....")
    database_link = sys_uploader.pinger(username, password, cluster_name)
    sys_uploader.uploader(database_link, system_info)

if __name__ == "__main__":
    print("Collecting telemetry data....")
    telemetry(True, True)