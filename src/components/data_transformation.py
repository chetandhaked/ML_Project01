import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

# data ko transform kerene ke baad kha store kre?

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","Preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            # independent feature ka pert ker diya transform kerne ke liye 
            
            # step1 : pipeline bna usme --->> 1.) missing value hanndelling (use library : SimpleImputer)
            #                          |
            #                          |---->> transformation 
            # 
            # 
            #           
            num_feature =["writing_score","reading_score"]
            cat_feature = [
                'gender',
                'race_ethnicity',
                'lunch',
                'test_preparation_course',
            ]
            num_Pipline = Pipeline(
                    steps = [
                        ("imputer",SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler(with_mean=False))
                    ]
            )

            cat_Pipline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ("one_hot_encoder", OneHotEncoder(handle_unknown='ignore')),
                   ("scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Catagorical columns: {cat_feature}")
            logging.info(f"numerical columns: {num_feature}")

            preprocessor = ColumnTransformer(
                [
                    ("num_Pipline",num_Pipline,num_feature),
                    ('cat_Pipeline',cat_Pipline,cat_feature)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("obtaining preprocessing Object")

            preprocessing_obj = self.get_data_transformer_object()

            target_col_name = "math_score"
            num_feature =["writing_score","reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_col_name],axis=1)
            target_feature_train_df = train_df[target_col_name]

            input_feature_test_df = test_df.drop(columns=[target_col_name],axis=1)
            target_feature_test_df = test_df[target_col_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            
            logging.info(f"saved preprocessing object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj= preprocessing_obj
            )
            return(
                train_arr,
                test_arr,
                # self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            raise CustomException(e,sys)