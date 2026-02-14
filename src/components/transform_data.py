# Importing packages
import sys
import pandas as pd
import joblib
from sklearn import set_config
set_config(transform_output='pandas')
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from src.components.config_entity import DataIngestionConfig, DataTransformationConfig
from src.utils import convert_target_to_numerical_feature
from src.exception import CustomException
from src.logger import logging

# Creating a class to transform the data before storing it in a feature store
class TransformData():
    '''
    This class transforms the raw data and prepares the data for storage in the
    feature store. The class has three methods in addition to the constructor - a method
    to select features, a method to create the preprocessor object and a method to 
    initiate the data transformation process.
    '''
    # Creating the constructor for the TransformData class
    def __init__(self):
        '''
        This is the constructor for the TransformData class.
        '''
        self.data_ingestion_config = DataIngestionConfig()
        self.preprocessor_config = DataTransformationConfig()
    
    # Creating a method to transform features within the dataset
    def select_features(self, df:pd.DataFrame)->pd.DataFrame:
        '''
        This method will create the total score feature. The method takes a pandas dataframe
        as input and returns a pandas dataframe with the new feature. In addition, the method
        will drop the columns that are not required for the model.
        ========================================================================================
        ------------------
        Parameters:
        ------------------
        df : pd.DataFrame - This is the dataframe that will be used to create the new feature.
        
        ------------------
        Returns:
        ------------------
        df : pd.DataFrame - This is the dataframe with the new feature.
        ========================================================================================
        '''
        try:         
            # Dropping columns that are not required for the model
            cols_to_drop = ['College_ID', 
                            'Prev_Sem_Result',
                            'Academic_Performance', 
                            'Internship_Experience', 
                            'Extra_Curricular_Score'
                            ]
            df.drop(labels=cols_to_drop, axis=1, inplace=True)
            
            # Changing the name of the columns from Capital Case to Lower case
            df.columns = df.columns.map(lambda x: x.lower())
            
            return df
        
        except Exception as e:
            raise CustomException(e, sys)
    
    # Creating a method to create the transformation pipeline
    def create_preprocessing_object(self):
        '''
        This method constructs the preprocessor object, using scikit-learn's 
        ColumnTransformer pipeline and returns the created preprocessor object.
        ==================================================================================
        ---------------
        Returns:
        ---------------
        preprocessor_obj : scikit-learn ColumnTransformer pipeline - This is the 
        preprocessor object to transform the data.
        ==================================================================================
        '''
        try:
            # Creating the preprocessor object
            preprocessor_obj = Pipeline(
                steps=[
                    ('poly', PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)),
                    ('std', RobustScaler())
                ]
            )
            
            return preprocessor_obj
        
        except Exception as e:
            raise CustomException(e, sys)
    
    # Create a method to initiate the data transformation
    def initiate_data_transformation(self, save_object=True):
        '''
        This method initiates the data transformation process. The method accepts the
        train data path and the test data path, transforms the data and returns the 
        transformed data as well as the preprocessor object.
        ===================================================================================
        ---------------
        Parameters:
        ---------------
        save_object : bool - This is a flag to indicate whether (or not) to save the 
        preprocessor object.
        
        ---------------
        Returns:
        ---------------
        train_arr : Pandas Dataframe - This is the transformed train dataset.
        test_arr : Pandas Dataframe - This is the transformed test dataset.
        preprocessor_obj : scikit-learn ColumnTransformer pipeline - This is the 
        preprocessor object to transform the data.
        ====================================================================================
        '''
        try:
            # Reading the train and test sets from the artifacts folder
            train_data = pd.read_parquet(self.data_ingestion_config.train_data_path)
            test_data = pd.read_parquet(self.data_ingestion_config.test_data_path)
            
            # Separating the train data into a feature set and target set
            train_features = train_data.copy().drop(labels=['Placement'], axis=1)
            train_target = train_data['Placement'].copy()
            
            # Separating the test data into a feature set and target set
            test_features = test_data.copy().drop(labels=['Placement'], axis=1)
            test_target = test_data['Placement'].copy()
            
            # Keeping only the relevant features from the train and test sets
            train_features_sub = self.select_features(train_features)
            test_features_sub = self.select_features(test_features)
            
            # Instantiating the preprocessor object
            preprocessor_obj = self.create_preprocessing_object()
            
            # Transforming the train and test sets using the preprocessor object
            train_arr = preprocessor_obj.fit_transform(train_features_sub)
            test_arr = preprocessor_obj.transform(test_features_sub)
            
            # Combining the train array and the train target
            train_dataset = pd.concat([train_arr, train_target], axis=1)
            
            # Combining the test array and the test target
            test_dataset = pd.concat([test_arr, test_target], axis=1)
            
            # Saving the preprocessor object to the artifacts folder if save_object 
            # is true
            if save_object:
                joblib.dump(preprocessor_obj, self.preprocessor_config.preprocessor_obj_path)
            
            return (
                train_dataset,
                test_dataset,
                preprocessor_obj
            )
        
        except Exception as e:
            raise CustomException(e, sys)