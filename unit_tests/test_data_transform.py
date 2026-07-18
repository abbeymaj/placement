# Importing packages
import os
import pytest
import pandas as pd
from src.utils import convert_target_to_numerical_feature
from src.components.config_entity import DataIngestionConfig
from src.components.transform_data import TransformData
from src.utils import convert_column_names_to_lower_case

# Creating a module to provide the path to the train dataset
@pytest.fixture(scope='module')
def train_dataset():
    ingestion_config = DataIngestionConfig()
    return ingestion_config.train_data_path

# Creating a module to provide the path to the test dataset
@pytest.fixture(scope='module')
def test_dataset():
    ingestion_config = DataIngestionConfig()
    return ingestion_config.test_data_path

# Verifying that the create features method works as expected
def test_create_features(train_dataset):
    df = pd.read_parquet(train_dataset)
    transform = TransformData()
    df_mod = transform.select_features(df)
    assert df_mod is not None

# Verifying that the create features method drops the correct columns
def test_drop_features(train_dataset):
    df = pd.read_parquet(train_dataset)
    transform = TransformData()
    df_mod = transform.select_features(df)
    cols_to_drop = ['College_ID', 
                    'Prev_Sem_Result',
                    'Academic_Performance', 
                    'Internship_Experience', 
                    'Extra_Curricular_Score'
                    ]
    assert cols_to_drop not in list(df_mod.columns)

# Verifying that the column names change from capital case to lower case
def test_column_names(train_dataset):
    df = pd.read_parquet(train_dataset)
    transform = TransformData()
    df_mod = transform.select_features(df)
    expected_cols = ['iq', 'cgpa', 'communication_skills', 'projects_completed', 'placement']
    assert df_mod.columns.str.islower().all()
    assert df_mod.columns.tolist() == expected_cols

# Verifying that the target feature can be converted to numerical
def test_convert_target_to_numerical(train_dataset):
    df = pd.read_parquet(train_dataset)
    df.columns = df.columns.map(lambda x: x.lower())
    df_trgt_mod = convert_target_to_numerical_feature(df)
    assert df_trgt_mod['placement'].dtype == 'int64'

# Verifying that the preprocessor object can be created
def test_create_preprocessor_obj():
    transform = TransformData()
    processor_obj = transform.create_preprocessing_object()
    assert processor_obj is not None

# Verifying that the utility function to convert column names to lower case works as expected
def test_convert_capital_case_to_lower_case(train_dataset):
    df = pd.read_parquet(train_dataset)
    df_mod = convert_column_names_to_lower_case(df)
    assert df_mod.columns.str.islower().all()

# Verifying that the data transformation method works as expected
def test_data_transformation(train_dataset, test_dataset):
    transform = TransformData()
    train_data, test_data, preprocessor_obj = transform.initiate_data_transformation(train_dataset, test_dataset, save_object=False)
    assert train_data is not None
    assert test_data is not None
    assert preprocessor_obj is not None
    assert 'Placement' in train_data.columns
    assert 'Placement' in test_data.columns
    



