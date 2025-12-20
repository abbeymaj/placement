# Importing packages
import sys
import os
import pandas as pd
from sklearn import set_config
set_config(transform_output='pandas')
from sklearn.model_selection import train_test_split
from src.components.config_entity import DataIngestionConfig
from src.exception import CustomException
from src.logger import logging

# Creating a class to ingest the raw data and split it into a train
# and test set
class DataIngestion():
    '''
    This class is used to ingest the raw data and split the dataset into a
    train and test dataset. Both the train and test dataset are then stored
    in the artifacts folder.
    '''
    # Creating the constructor method for the class
    def __init__(self):
        '''
        This is the constructor for the data ingestion class.
        '''
        self.ingestion_config = DataIngestionConfig()
    
    # Creating a method to ingest the raw data and split it into a train and 
    # test set.
    def initiate_data_ingestion(self):
        '''
        This method will ingest the data from source, split the dataset into a train
        and test dataset. The function will also create the artifacts folder and store
        the train and test dataset in the artifacts folder.
        ====================================================================================
        ---------------
        Returns:
        ---------------
        train file path : str - This is the path to the train dataset.
        test file path : str - This is the path to the test dataset.
        ====================================================================================
        '''
        try:
            logging.info('Beginning the data ingestion process.')
            
            # Creating the artifacts folder if it does not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Reading the raw data from the source
            df = pd.read_parquet(self.ingestion_config.raw_data_path)
            
            # Split the dataset into a train and test set
            train_set, test_set = train_test_split(df, test_size=0.3, random_state=42)
            
            # Storing the train and test datasets in the artifacts folder 
            train_set.to_parquet(self.ingestion_config.train_data_path, index=False, compression='gzip')
            test_set.to_parquet(self.ingestion_config.test_data_path, index=False, compression='gzip')
            
            logging.info('Data ingestion process completed.')
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)