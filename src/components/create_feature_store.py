# Importing packages
import sys
import os
import pandas as pd
from src.components.config_entity import FeatureStoreConfig
from src.exception import CustomException

# Creating a class to create the feature store
class CreateFeatureStore():
    '''
    This class contains methods to create the feature store and then store the transformed datasets. 
    The class contains two methods - a constructor and a method to store the transformed
    datasets.
    '''
    # Creating the constructor for the feature store creation class
    def __init__(self):
        '''
        This is the constructor for the feature store creation class.
        '''
        self.feature_store_config = FeatureStoreConfig()
    
    # Creating a method to create the feature store
    def create_feature_store(self, train_data:pd.DataFrame, test_data:pd.DataFrame):
        '''
        This method creates the feature store and then stores the transformed datasets in the 
        feature store folder.
        =========================================================================================
        ----------------
        Parameters:
        ----------------
        train_path : pandas dataframe - This is the train dataset.
        test_path : pandas dataframe - This is the test dataset.
        
        ----------------
        Returns:
        ----------------
        transformed train data path : str - Returns the path to the transformed train dataset.
        transformed test data path : str - Returns the path to the transformed test dataset.
        =========================================================================================
        '''
        try:
            # Creating the feature store folder to store the transformed datasets.
            dir_path = os.path.dirname(self.feature_store_config.xform_train_path)
            os.makedirs(dir_path, exist_ok=True)
            
            # Storing the transformed datasets in the feature store folder
            train_data.to_parquet(self.feature_store_config.xform_train_path, index=False, compression='gzip')
            test_data.to_parquet(self.feature_store_config.xform_test_path, index=False, compression='gzip')
            
            return (
                self.feature_store_config.xform_train_path,
                self.feature_store_config.xform_test_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)