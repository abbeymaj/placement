# Importing packages
import sys
import pandas as pd
import joblib
from sklearn import set_config
set_config(transform_output='pandas')
from src.exception import CustomException
from src.logger import logging

# Creating a class to transform the data before storing it in a feature store
class TransformData():
    '''
    Docstring for TransformData
    '''
    # Creating the constructor for the TransformData class
    def __init__(self):
        '''
        This is the constructor for the TransformData class.
        '''
        pass
    
    # Creating a method to transform features within the dataset
    def create_features(self):
        '''
        Docstring for create_features
        
        :param self: Description
        '''
        pass
    
    # Creating a method to create the transformation pipeline
    def create_preprocessing_pipeline(self):
        '''
        Docstring for create_preprocessing_pipeline
        
        :param self: Description
        '''
        pass
    
    # Create a method to initiate the data transformation
    def initiate_data_transformation(self):
        '''
        Docstring for initiate_data_transformation
        
        :param self: Description
        '''
        pass