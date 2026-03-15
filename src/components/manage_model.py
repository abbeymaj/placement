# Importing packages
import sys
import dagshub
import mlflow
from src.components.config_entity import ModelURIConfig
from src.exception import CustomException

# Creating a class to upload the trained model to the model registry
class UploadModelToRegistry():
    '''
    This class is used to upload the trained model to the model registry. The model
    registry, which is MLFlow, is hosted on Dagshub. The class has two methods -
    the constructor and a method to upload the trained model to the model registry.
    '''
    # Creating the constructor for the UploadModelToRegistry class
    def __init__(self):
        '''
        This is the constructor for the UploadModelToRegistry class.
        '''
        pass
    
    # Creating a method to upload the trained model to the model registry
    def upload_model_to_registry(self):
        '''
        '''
        try:
            pass
        
        except Exception as e:
            raise CustomException(e, sys)