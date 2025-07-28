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


# ___________________________________________________

# # Step 1: Only directory path, NOT including file name
# LOG_DIR = os.path.join(os.getcwd(), "logs")  # Should be something like C:\Users\cheta\...\logs
# os.makedirs(LOG_DIR, exist_ok=True)  # ✅ This should create 'logs' folder

# # Step 2: Create log file with timestamp
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# # Step 3: Configure logging
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# # Step 4: Logging something
# if __name__ == '__main__':
#     logging.info("Logging has started successfully.")