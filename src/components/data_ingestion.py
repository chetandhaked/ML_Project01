import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import modelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv") # mera train data artificates folder main train file main save hoga in future
    test_data_path: str=os.path.join("artifacts","test.csv") 
    raw_data_path: str=os.path.join("artifacts","data.csv") 

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion methid or component")
        try:
            df=pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok= True) #actually main train data ke liye folder banana

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header = True)
            
            logging.info("train test split initiated")
            train_set,test_set = train_test_split(df,test_size = 0.2 , random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header = True)
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )    
        
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__=='__main__':
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr1, test_arr1 = data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer = modelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr1,test_arr1))




# import os
# import sys
# import pandas as pd
# from sklearn.model_selection import train_test_split

# from src.exception import CustomException
# from src.logger import logging

# # 🔹 Configuration class WITHOUT @dataclass
# class DataIngestionConfig:
#     def __init__(self):
#         self.train_data_path = os.path.join("artifacts", "train.csv")
#         self.test_data_path = os.path.join("artifacts", "test.csv")
#         self.raw_data_path = os.path.join("artifacts", "data.csv")

# # 🔹 Main Data Ingestion class
# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config = DataIngestionConfig()

#     def initiate_data_ingestion(self):
#         logging.info("Entered the data ingestion method/component")
#         try:
#             # Step 1: Read the dataset
#             df = pd.read_csv("notebook/data/stud.csv")
#             logging.info("Read the dataset as dataframe")

#             # Step 2: Create folder if it doesn't exist
#             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

#             # Step 3: Save raw data
#             df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

#             # Step 4: Train-test split
#             logging.info("Train-test split initiated")
#             train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

#             # Step 5: Save train and test data
#             train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
#             test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

#             logging.info("Data ingestion completed")

#             return (
#                 self.ingestion_config.train_data_path,
#                 self.ingestion_config.test_data_path
#             )

#         except Exception as e:
#             raise CustomException(e, sys)
