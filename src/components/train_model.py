# Importing packages
import sys
import pandas as pd
import joblib
from sklearn import set_config
set_config(transform_output='pandas')
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from src.utils import convert_target_to_numerical_feature
from src.components.config_entity import TrainedModelConfig
from src.components.config_entity import DataTransformationConfig
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
        self.preprocessor_config = DataTransformationConfig()
        self.feature_config = FeatureStoreConfig()
        self.trained_model_config = TrainedModelConfig()
    
    # Creating a method to split the datasets into the feature and target sets
    def create_feature_target_sets(self):
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
            # Reading the transformed datasets from the feature store
            train_data = pd.read_parquet(self.feature_config.xform_train_path)
            test_data = pd.read_parquet(self.feature_config.xform_test_path)
                        
            # Converting all features to lower case
            train_data.columns = train_data.columns.str.lower()
            test_data.columns = test_data.columns.str.lower()
            
            # Converting the target feature to a numerical feature
            train_data = convert_target_to_numerical_feature(train_data)
            test_data = convert_target_to_numerical_feature(test_data)
            
            # Splitting the train dataset into features and target sets
            X_train = train_data.copy().drop(labels=['placement'], axis=1)
            y_train = train_data['placement'].copy() 
            
            # Splitting the test dataset into features and target sets
            X_test = test_data.copy().drop(labels=['placement'], axis=1) 
            y_test = test_data['placement'].copy()
            
            return (
                X_train,
                y_train,
                X_test,
                y_test
            )
        
        except Exception as e:
            raise CustomException(e, sys)
    
    # Creating a method to initiate model training 
    def initiate_model_training(self, save_model=False, make_prediction=True):
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
            # Creating the feature and target sets
            X_train, y_train, X_test, y_test = self.create_feature_target_sets()
            
            # Creating the model object
            rf_clf = RandomForestClassifier(
                n_estimators=500,
                random_state=42,
                n_jobs=-1
            )
            
            # Fitting the training data
            rf_clf.fit(X_train, y_train)
            
            # Fetching the model parameters
            model_params = rf_clf.get_params()
            
            # Saving the model if the save_model flag is set to True
            if save_model:
                joblib.dump(rf_clf, self.trained_model_config.trained_model_path)
            
            # Making a prediction and calculating the metric if the make_prediction
            # flag is set to True
            if make_prediction:
                y_pred = rf_clf.predict(X_test)
                metric = f1_score(y_test, y_pred)
                return (
                    rf_clf,
                    model_params,
                    metric
                )
            
            return (
                rf_clf,
                model_params
            )
            
        except Exception as e:
            raise CustomException(e, sys)