import os
import pandas as pd
from src.datasience import logger
from sklearn.model_selection import train_test_split
from src.datasience.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # We can add different data transformation techniques such as Scaler, PCA and all
    # We can perform all kinds of EDA in the ML cycle here before passing this data to the model

    # I am only adding train_test_splitting because this data is already cleaned 

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

