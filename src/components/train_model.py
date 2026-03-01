# Importing packages
import sys
import pandas as pd
from sklearn import set_config
set_config(transform_output='pandas')
from src.components.config_entity import FeatureStoreConfig
from src.exception import CustomException

# Creating a class to train the model
class TrainModel():
    '''
    This class is used to train the model. The class has three methods - 
    the constructor, a method to split the datasets into features & targets,
    and a method to initiate the model training.
    '''
    # Creating the constructor for the TrainModel class
    def __init__(self):
        '''
        This is the constructor for the model training class. The constructor
        initializes the path to the transformed datasets and also initializes the 
        path to which the trained model will be stored (if needed).
        '''
        self.feature_config = FeatureStoreConfig()
    
    # Creating a method to split the datasets into the feature and target sets
    def create_feature_target_sets(self, train_path:str, test_path:str):
        '''
        This method creates the feature and target datasets.
        ============================================================================       
        -------------------
        Returns:
        -------------------
        X_train : pandas dataframe - The training feature set.
        y_train : pandas dataframe - The training target set.
        X_test : pandas dataframe - The test feature set.
        y_test : pandas dataframe - The test target set.
        =============================================================================
        '''
        try:
            pass
        
        except Exception as e:
            raise CustomException(e, sys)
    
    # Creating a method to initiate model training 
    def initiate_model_training(self, save_model=False, make_prediction=False):
        '''
        This method trains the model and then saves the trained model to the artifacts
        folder.
        ===================================================================================
        ------------------------
        Parameters:
        ------------------------
        save_model : bool - This determines if the model should be saved in the artifacts
        folder. The default value is False.
        
        make_prediction : bool - This determines if the model should make a prediction, 
        calculate the metric and return the metric. This will be used for testing purposes.
        The default value is False.
        
        ------------------------
        Returns:
        ------------------------
        model_path : str - This is the path to the saved model, if the model was saved.
        metric : float - This is the metric from the prediction. This will be returned
        if the user sets the make_prediction flag to True. 
        ====================================================================================
        '''
        try:
            pass
        
        except Exception as e:
            raise CustomException(e, sys)