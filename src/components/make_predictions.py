# Importing packages
import sys
import pandas as pd
import dagshub
import mlflow
from src.utils import convert_target_to_categorical_feature
from mlflow.tracking import MlflowClient
from src.utils import load_preprocessor_object
from src.components.config_entity import DataTransformationConfig
from src.components.config_entity import ModelURIConfig
from src.exception import CustomException


# Creating a class to make predictions using the latest model version
class MakePrediction():
    '''
    This class contains methods to make predictions using the latest model version. The class 
    contains three methods - a constructor, a method to obtain the latest model and a method
    to make predictions.
    '''
    # Creating the constructor for the class
    def __init__(self):
        '''
        This is the constructor of the MakePrediction class.
        '''
        self.preprocessor_path = DataTransformationConfig()
        self.uri_path = ModelURIConfig()
    
    # Creating a method to fetch the latest model from the model registry
    def fetch_latest_model(self):
        '''
        This method retrieves the trained model from the model registry.
        ===================================================================================
        ----------------
        Returns:
        ----------------
        model : scikit-learn model - This is the trained model from the model registry.
        ===================================================================================
        '''
        try:
            # Instantiating the dagshub client
            dagshub.init(repo_owner='abbeymaj', repo_name='placement', mlflow=True)
            
            # Getting the model URI path
            model_uri_path = self.uri_path.model_uri_path
            mlflow.set_tracking_uri(model_uri_path)
            
            # Defining the model name
            model_name = 'training_model'
            
            # Creating the client to fetch the latest model
            client = MlflowClient(tracking_uri=model_uri_path)
            
            # Fetching the latest model information
            latest_version_info = client.get_latest_versions(name=model_name)[0]
            
            # Fetching the run id for the latest model
            latest_model_source = latest_version_info.source
            
            # Loading the latest model
            model = mlflow.sklearn.load_model(latest_model_source)
            
            return model
        
        except Exception as e:
            raise CustomException(e, sys)
    
    
    # Creating a method to make predictions
    def make_predictions(self, features:pd.DataFrame):
        '''
        This method makes predictions using the feature inputs from the web page and 
        the trained model. This method also transforms the input data using the 
        preprocessor object before making the predictions.
        ============================================================================================
        -------------------
        Parameters:
        -------------------
        features : pandas dataframe - This is the feature data input received from the web page.
        
        -------------------
        Returns:
        -------------------
        preds : This is the prediction based on the input features.
        =============================================================================================
        '''
        try:
            # Fetching the preprocessor object
            preprocessor_obj = load_preprocessor_object()
            
            # Fetching the latest model
            model = self.fetch_latest_model()
            
            # Transforming the input features using the preprocessor object
            transformed_features = preprocessor_obj.transform(features)
            
            # Making predictions using the transformed features and the latest model
            results = model.predict(transformed_features)
            preds1 = int(results[0])
            
            # Converting the prediction to a string to display on the webpage
            pred_df = pd.DataFrame([preds1], columns=['placement'])
            preds = convert_target_to_categorical_feature(pred_df)

            return preds['placement'].iloc[0]
        
        except Exception as e:
            raise CustomException(e, sys)
    