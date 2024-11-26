from src.datasience import logger
from src.datasience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datasience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datasience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datasience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datasience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

# from src.datasience.utils.common import read_yaml
# from pathlib import Path
# ------------------------------------------------------------


# logger.info("Welcome to the custom logging data science.")

# read_yaml(path_to_yaml= Path("params.yaml"))

# ------------------------------------------------------------

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
# ------------------------------------------------------------

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation_obj = DataValidationTrainingPipeline()
    data_validation_obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
# ------------------------------------------------------------

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation_obj = DataTransformationTrainingPipeline()
    data_transformation_obj.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
# ------------------------------------------------------------

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer_obj = ModelTrainerTrainingPipeline()
    model_trainer_obj.initiate_model_trainer()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
# ------------------------------------------------------------
STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation_obj = ModelEvaluationTrainingPipeline()
    model_evaluation_obj.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
# ------------------------------------------------------------
    
