# Importing packages
import os
import pandas as pd
import pytest
from src.components.config_entity import DataIngestionConfig
from src.components.data_ingestion import DataIngestion


# Creating a module to provide the path to the train dataset
@pytest.fixture(scope='module')
def train_dataset_path():
    ingestion_config = DataIngestionConfig()
    return ingestion_config.train_data_path

# Creating a module to provide the path to the test dataset
@pytest.fixture(scope='module')
def test_dataset_path():
    ingestion_config = DataIngestionConfig()
    return ingestion_config.test_data_path

# Verifying that the raw dataset is available and can be read
def test_read_raw_data():
    ingestion_config = DataIngestionConfig()
    df = pd.read_parquet(ingestion_config.raw_data_path)
    assert df is not None

# Verifying that the artifacts folder was created
def test_artifacts_folder_created():
    ingestion_config = DataIngestionConfig()
    assert os.path.exists(os.path.dirname(ingestion_config.train_data_path)) is True

# Verifying that the train dataset was created
def test_train_dataset_created(train_dataset_path):
    assert os.path.exists(train_dataset_path) is True

# Verifying that the train dataset is not empty
def test_train_dataset_not_empty(train_dataset_path):
    df = pd.read_parquet(train_dataset_path)
    assert df.empty is False

# Verifying that the test dataset was created
def test_tst_dataset_created(test_dataset_path):
    assert os.path.exists(test_dataset_path) is True

# Verifying that the test dataset is not empty
def test_tst_dataset_not_empty(test_dataset_path):
    df = pd.read_parquet(test_dataset_path)
    assert df.empty is False