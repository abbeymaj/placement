# Importing packages
import os
import pytest
from unittest.mock import patch, MagicMock
import requests
from src.components.config_entity import ModelURIConfig
from src.utils import create_run_config_dir

# Verifying that the model URI can be accessed and returns either
# a 200 or 401 status code
def test_model_uri_is_reachable():
    model_uri_config = ModelURIConfig()
    response = requests.get(model_uri_config.model_uri_path, timeout=5)
    assert response.status_code in [200, 401]

# Verifying that the run_config folder can be created sucessfully at the 
# root level of the project.
def test_create_run_config_dir_real_fs(tmp_path, mocker):
    # Simulating the path where the train_pipeline.py file will be located
    fake_script_path = tmp_path / "src" / "pipelines" / "train_pipeline.py"
    
    # Creating the parent directories so that the script "exists" in a 
    # valid path
    fake_script_path.parent.mkdir(parents=True)
    
    # Patching the __file__ attribute where the function lives. Since the 
    # function is in the utils.py file, we are patching the __file__ attribute
    # of the utils.py file.
    with patch('src.utils.__file__', str(fake_script_path)):
        create_run_config_dir()
        
    # Verify if the folder was created at the expected root level
    expected_dir = tmp_path / "run_config"
    assert expected_dir.exists()
    assert expected_dir.is_dir()