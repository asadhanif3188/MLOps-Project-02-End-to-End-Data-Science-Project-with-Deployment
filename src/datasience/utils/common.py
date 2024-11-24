import os
import yaml
import json
import joblib 
from src.datasience import logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any  

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e
    
# -------------------------------------------------------------

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories from a list of paths.

    Args:
        path_to_directories (list): A list of paths to create directories.
        verbose (bool, optional): Whether to print a message for each directory created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# -------------------------------------------------------------

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to save the JSON file.
        data (dict): The dictionary to save as a JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

# -------------------------------------------------------------
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        ConfigBox: The contents of the JSON file as a ConfigBox object.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)
# -------------------------------------------------------------
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves a binary file using joblib.

    Args:
        data (Any): The data to save.
        path (Path): The path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
# -------------------------------------------------------------
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file using joblib.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data 
# -------------------------------------------------------------
# -------------------------------------------------------------
