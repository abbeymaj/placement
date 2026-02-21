# Importing packages
import os
import pandas as pd
import pytest
import pyfakefs as fs
from unittest.mock import MagicMock
from src.components.create_feature_store import CreateFeatureStore

# Creating a fixture to mock the pandas to_parquet method
@pytest.fixture
def mock_parquet_saver(mocker, fs):
    """
    A reusable fixture that patches pandas.to_parquet to 
    create a dummy file in pyfakefs instead of calling the C-engine.
    """
    # Using "fs" to inject into this fixture
    def _side_effect_save(path, **kwargs):
        fs.create_file(path, contents="dummy parquet data")

    # Patching the method and return the mock object
    return mocker.patch("pandas.DataFrame.to_parquet", side_effect=_side_effect_save)


# Verifying that the feature store folder can be successfully created
# and the files can be loaded
def test_create_feature_store(mocker, fs, mock_parquet_saver):
    # Creating a pair of dummy dataframes
    df_train = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    df_test = pd.DataFrame({'a': [5, 6], 'b': [7, 8]})

    # Mocking the configuration object
    mock_config = MagicMock()
    mock_config.xform_train_path = "/fake/path/train.parquet"
    mock_config.xform_test_path = "/fake/path/test.parquet"
    
    # Creating the expected call objects with the exact parameters used by the code
    expected_train = mocker.call(mock_config.xform_train_path, index=False, compression='gzip')
    expected_test = mocker.call(mock_config.xform_test_path, index=False, compression='gzip')

    # Manually injecting the mock config
    pipeline = CreateFeatureStore()
    pipeline.feature_store_config = mock_config

    # Executing the method
    train_path, test_path = pipeline.create_feature_store(df_train, df_test)

    # Running the Assertions
    assert os.path.exists("/fake/path")
    assert mock_parquet_saver.call_count == 2
    assert os.path.isfile(train_path)   
    assert os.path.isfile(test_path)