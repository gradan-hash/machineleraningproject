import os
import sys
from dataclass import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor,
                              GradientBoostingRegressor,
                              RandomForestRegressor,)


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KnearestNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
from src.utils import evaluate_model


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self,):
        self.model_trainer_config = ModelTrainerConfig()

        def initiate_model_trainer(self, train_array, test_array, preprocessor_path):
            try:
                logging.info("splitting trainning nd test input data")
                x_train, y_train, x_test, y_test = (
                    train_array[:, :-1],
                    train_array[:, -1],
                    test_array[:, : -1],
                    test_array[:, -1],
                )

                models = {
                    "Random forest": RandomForestRegressor(),
                    "Decision Tree": DecisionTreeRegressor(),
                    "Gradient Boosting": GradientBoostingRegressor(),
                    "Linear Regression": LinearRegressionRegressor(),
                    "K-NearestNeighbors": KNearestNeighborsRegressor(),
                    "XGBBclassifier": XGBuilderRegressor(),
                    "Catboosting Classifier ": CatBoostRegressor(verbose=False),
                    "AdaBoost classifier ": AdaBoostRegressor()
                }
                model_report: dict = evaluate_model(
                    x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test, models=models)

                # get the best model score from dict
                best_model_score = max(sorted(model_report.values()))

                # to get best model name from dict

                best_model_name = list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)
                ]

            except Exception as e:
                raise CustomException(e, sys.exc_info())
