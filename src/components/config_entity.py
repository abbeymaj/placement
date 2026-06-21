# Importing packages
import os
from dataclasses import dataclass
from datetime import datetime

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

# Creating a class to store the trained model, if the user wants to save it
@dataclass
class TrainedModelConfig():
    '''
    This class stores the path to the trained model. The trained model will
    be stored in the artifacts folder.
    '''
    trained_model_path = os.path.join('artifacts', 'trained_model.joblib')

# Creating a class to store the model URI path
@dataclass
class ModelURIConfig():
    '''
    This class stores the path to the model URI. The model URI will be used to 
    load the model from the model registry.
    '''
    model_uri_path = 'https://dagshub.com/abbeymaj/placement.mlflow'

# Creating a class to store the database path
@dataclass
class DatabaseConfig():
    '''
    This class stores the path to the database.
    '''
    db_path:str = os.path.join('db', 'placement.db')

#Creating the class to store the path to the drift report
class DriftReportConfig():
    '''
    This class stores the path to the drift detection report.
    '''
    current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_name = current_date + '_data_drift_report.html'
    report_path = os.path.join('reports', report_name)
    
