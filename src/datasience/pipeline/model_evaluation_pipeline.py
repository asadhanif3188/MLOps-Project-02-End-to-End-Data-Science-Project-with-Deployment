from src.datasience.config.configuration import ConfigurationManager
from src.datasience.components.model_evaluation import ModelEvaluation
from src.datasience import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                model_evaluation_config = config.get_model_evaluation_config()
                model_evaluation = ModelEvaluation(config = model_evaluation_config)
                model_evaluation.log_into_mlflow()
            else:
                raise Exception("You data schema is not valid")
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evaluation_obj = ModelEvaluationTrainingPipeline()
        model_evaluation_obj.initiate_model_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
