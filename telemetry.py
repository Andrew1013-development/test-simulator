import os
from dotenv import load_dotenv
import sys_fetcher
import sys_uploader
from logger import telemetry_logging_module

__version__ = "1.1.0"

username = "dontbesus"
password = "vb9jsbkAfXww3uc0"
cluster_name = "cluster0"

def telemetry(debug_short, debug_full):
    telemetry_logging_module.info("telemetry function started")
    telemetry_logging_module.info("fetching system info")
    if debug_short:
        print("Collecting system info....")
    system_info = sys_fetcher.fetcher()
    telemetry_logging_module.info("done fetching system info")
    telemetry_logging_module.info("writing to json file")
    if debug_short:
        print("Writing to .json file....")
    sys_fetcher.writer(system_info)
    telemetry_logging_module.info("done writing to json file")
    telemetry_logging_module.info("pinging database with username and password")
    if debug_short:
        print("Uploading to MongoDB....")
    database_link = sys_uploader.pinger(username, password, cluster_name, debug_short, debug_full)
    telemetry_logging_module.info("uploading system info to database")
    sys_uploader.uploader(database_link, system_info, debug_short, debug_full)
    telemetry_logging_module.info("done uploading system info to database")
