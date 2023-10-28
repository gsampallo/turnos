import os
import logging
from datetime import datetime

from Parameters import Parameters

class Log:

    def __init__(self):
        param = Parameters()
        self.logFolder = param.get_log_folder()
        if not os.path.isdir(self.logFolder):
            os.makedirs(self.logFolder)
        logfile = f"./{self.logFolder}/{datetime.today().strftime('%Y%m%d')}.log"
        logging.basicConfig(filename=logfile, level=logging.INFO)
        logging.info("Turnos at "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def log(self,text):
        logging.info(text)
    



