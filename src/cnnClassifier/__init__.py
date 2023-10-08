#instead of importing log in mmodels form folders again and again we will keep all here in constructer file
#from here we can import models
import os
import sys
import logging #to create custom logging on top of it

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# %(asctime)s : gives current stdtime of running your project
# %(levelname)s : which types of logs want to store (info log)
# %(module)s : which module running this file 
# %(message)s : prompt messeges or error messeges

log_dir = "logs" #create log folder
log_filepath = os.path.join(log_dir,"running_logs.log") #running_logs.log file created
os.makedirs(log_dir, exist_ok=True)

#logging functionality
logging.basicConfig(
    Level = logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #want to create log file
        logging.StreamHandler(sys.stdout) #want to see in all logs my terminal as well
    ]
)
logger = logging.getLogger("cnnClassifierLogger") #logger object name "cnnClassifierLogger"
