# Importing packages
import pytest
import pandas as pd
from src.utils import convert_target_to_numerical_feature
from src.components.config_entity import FeatureStoreConfig
from src.components.train_model import TrainModel

# Creating a module to provide the path to the transformed train dataset
@pytest.fixture(scope='module')
def train_set_path():
    feature_store_config = FeatureStoreConfig()
    return feature_store_config.xform_train_path

# Verifying that the feature and target sets can be created
def test_create_feature_target_datasets(train_set_path): 
    train_data = pd.read_parquet(train_set_path)
    model_train = TrainModel()
    X_train, y_train, X_test, y_test = model_train.create_feature_target_sets()
    assert X_train is not None
    assert y_train is not None
    assert X_test is not None
    assert y_test is not None

# Verifying that the target sets are lower case
def test_all_features_lower_case(train_set_path): 
    train_data = pd.read_parquet(train_set_path)
    model_train = TrainModel()
    X_train, y_train, X_test, y_test = model_train.create_feature_target_sets()
    assert X_train.columns.str.islower().all()
    assert X_test.columns.str.islower().all()
    assert y_train.name == 'placement'
    assert y_test.name == 'placement'

def test_target_feature_is_numerical(train_set_path): 
    train_data = pd.read_parquet(train_set_path)
    model_train = TrainModel()
    X_train, y_train, X_test, y_test = model_train.create_feature_target_sets()
    assert y_train.dtype == 'int64'
    assert y_test.dtype == 'int64'
    assert y_train.isin([0, 1]).all()
    assert y_test.isin([0, 1]).all()

# Verifying that the model can be trained and a prediction can be made
def test_model_training_and_prediction(train_set_path):
    model_train = TrainModel()
    metric = model_train.initiate_model_training(make_prediction=True)
    assert metric is not None
    assert metric > 0.9