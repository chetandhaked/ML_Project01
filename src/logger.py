import logging
import os
from datetime import datetime

# // log file creation format of 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) ## getcwd -> current working directory ., mtlb log file current directory 'src' main create hogi 'logs 'name se 
os.makedirs(logs_path,exist_ok=True) #file sari is folder main jaygi 

LOG_FILE_PATH = os.path.join(logs_path , LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    
)

