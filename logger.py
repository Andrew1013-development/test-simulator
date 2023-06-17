import logging
import datetime

__version__ = "1.0.0"

current_date = str(datetime.datetime.now().date())
current_time = str(datetime.datetime.now().time())[:-7].replace(":","-")

logger_module = logging
logger_module.basicConfig(
    level=logging.DEBUG,
    filename=f"{current_date}_{current_time}_plotter.log",
    filemode="w+",
    format=f"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger_module.debug("logging file created")