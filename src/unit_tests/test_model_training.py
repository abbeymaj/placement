# Importing packages
import pytest
import pandas as pd
from src.components.config_entity import FeatureStoreConfig

# Creating a module to provide the path to the transformed train dataset
@pytest.fixture(scope='module')
def train_set_path():
    feature_store_config = FeatureStoreConfig()
    return feature_store_config.xform_train_path