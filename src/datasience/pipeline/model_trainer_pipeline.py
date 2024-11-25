from src.datasience.config.configuration import ConfigurationManager
from src.datasience.components.model_trainer import ModelTrainer
from src.datasience import logger
from pathlib import Path

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                model_trainer_config = config.get_model_trainer_config()
                model_trainer = ModelTrainer(config = model_trainer_config)
                model_trainer.train()
            else:
                raise Exception("You data schema is not valid")
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
