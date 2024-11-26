import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name = "datasience"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_trainer.py",
    # f"src/{project_name}/components/model_evaluation.py",
    # f"src/{project_name}/components/model_pusher.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/data_ingestion_pipeline.py",
    f"src/{project_name}/pipeline/data_validation_pipeline.py",
    f"src/{project_name}/pipeline/data_transformation_pipeline.py",
    f"src/{project_name}/pipeline/model_trainer_pipeline.py",

    f"src/{project_name}/constants/__init__.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    # f"src/{project_name}/entity/artifact_entity.py",

    # f"src/{project_name}/exception/__init__.py",
    # f"src/{project_name}/logger/__init__.py",
    "Dockerfile",
    "requirements.txt",
    
    "config/config.yaml",
    
    "app.py",
    "main.py",
    "setup.py",

    "params.yaml",
    "schema.yaml",

    "research/research.ipynb",
    "templates/index.html",
    "templates/result.html",
]

# Script to create the files and directories 

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")