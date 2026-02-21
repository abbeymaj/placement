# Importing packages
import os
from dataclasses import dataclass

# Creating a class to store the path to the train and test datasets
@dataclass
class DataIngestionConfig():
    '''
    This class stores the path to the train and test datasets
    '''
    train_data_path = os.path.join('artifacts', 'train.parquet')
    test_data_path = os.path.join('artifacts', 'test.parquet')
    raw_data_path = 'https://github.com/abbeymaj80/my-ml-datasets/raw/refs/heads/master/project_datasets/placement/data.parquet'


# Creating  a class to store the path to the preprocessor object
@dataclass
class DataTransformationConfig():
    '''
    This class stores the path to the preprocessor object in the artifacts folder.
    '''
    preprocessor_obj_path = os.path.join('artifacts', 'preprocessor.joblib')

# Creating a class to store the path to the feature store
@dataclass
class FeatureStoreConfig():
    '''
    This class stores the path to the feature store.
    '''
    xform_train_path = os.path.join('feature_store', 'xform_train.parquet')
    xform_test_path = os.path.join('feature_store', 'xform_test.parquet')
