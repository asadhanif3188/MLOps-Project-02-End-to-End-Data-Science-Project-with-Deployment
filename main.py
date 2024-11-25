from src.datasience import logger
from src.datasience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datasience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

# from src.datasience.utils.common import read_yaml
# from pathlib import Path
# ------------------------------------------------------------


# logger.info("Welcome to the custom logging data science.")

# read_yaml(path_to_yaml= Path("params.yaml"))

# ------------------------------------------------------------

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

