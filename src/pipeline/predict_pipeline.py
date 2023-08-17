import sys
import os
import pandas as pd
from src.exception import CustomException

from src.utils import load_object


class Predictpipeline:
    def __init__(self):
        pass

    def predict(self, features):

        try:
            model_path = "artifacts\model.pkl"
            preprocesssor = "artifacts\preprocesssor.pkl"

            model = load_object(file_path=model_path)
            preproccessor_path = load_object(file_path=preproccessor_path)

            data_scaled = preprocesssor.transform(features)

            preds = model.predict(data_scaled)

            return preds
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: str,
                 writing_score: str):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.Dataframe(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
