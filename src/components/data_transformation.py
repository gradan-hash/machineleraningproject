import sys
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

import os
from src.exception import CustomException
from src.logger import logging


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
  # data transformation

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_objective(self):
        try:
            numercal_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course",]
            num_pipeline = Pipeline(
                # imputer handle missing values
                steps=[
                    ("Imputer", SimpleImputer(strategy="median"))
                    ("Scaler", StandardScaler())
                ]

            )
            cat_pipeline = Pipeline(
                stepps=[
                    ("imputer", SimpleImputer(strategy="most_frequent"))
                    ("one_hot_encode", OneHotEncoder())
                    ("Scaler", StandardScaler())

                ]
            )

            logging.info("numerical column standard scaling completed")

            logging.info("categorical data column encoding completed")

            logging.info(f"categorical column: {categorical_columns}")
            logging.info(f"numerical columns : {numercal_columns}")

            # combine the 2
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numercal_columns)
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys.exc_info())


def initiate_data_transformation(self, train_path, test_path):
    try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        logging.info("Read test data completed")

        logging.info("obtaining preprocessor bjecr")

    except:
        pass
