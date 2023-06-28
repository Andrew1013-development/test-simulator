import os
import logging
import datetime

__version__ = "1.1.4"

cwd = os.getcwd()
os.makedirs(os.path.join(cwd,"files"),exist_ok=True)
current_date = str(datetime.datetime.now().date())
current_time = str(datetime.datetime.now().time())[:-7].replace(":","-")

logger_module = logging
logger_module.basicConfig(
    level=logging.DEBUG,
    filename=os.path.join(cwd,"files",f"{current_date}_{current_time}_plotter.log"),
    filemode="w+",
    format=f"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger_module.debug("logging file created")

telemetry_logging_module = logging
telemetry_logging_module.basicConfig(
    level = logging.DEBUG,
    filename=os.path.join(cwd,"files",f"{current_date}_{current_time}_telemetry.log"),
    filemode="w+",
    format=f"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
telemetry_logging_module.debug("telemetry logging file created")
