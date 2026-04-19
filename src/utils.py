# Importing packages
import os
import sys
import json
import joblib
import pandas as pd
from pathlib import Path
from datetime import datetime
from src.components.config_entity import DataTransformationConfig
from src.exception import CustomException

# Creating a function to convert the target feature from a categorical to
# a numerical feature
def convert_target_to_numerical_feature(df:pd.DataFrame)->pd.DataFrame:
    '''
    This function takes the target feature, which is a categorical feature
    and converts it to a numerical feature.
    =========================================================================
    ------------------
    Parameters:
    ------------------
    df : pd.DataFrame - This is the DataFrame that contains the target 
    feature.
    
    ---------------
    Returns:
    ---------------
    df : pd.DataFrame - This is the DataFrame with the target feature 
    converted to a numerical feature.
    =========================================================================
    '''
    try:
        # Creating the mapping from categorical to numeric fields
        mapping = {"No":0, "Yes":1}
        
        # Changing the target feature from categorical to numerical
        df['placement'] = (df['placement'].astype(str).str.strip().map(mapping))
        
        return df
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to convert the target feature from categorical to a numerical
# feature.
def convert_target_to_categorical_feature(df:pd.DataFrame, col='placement'):
    '''
    This function takes the target feature, which is a numerical feature
    and converts it back into a categorical feature.
    =========================================================================
    ------------------
    Parameters:
    ------------------
    df : pd.DataFrame - This is the dataframe that contains the target 
    feature.
    col : str - This is the name of the target column.
    
    ---------------
    Returns:
    ---------------
    df : pd.DataFrame - This is the dataframe with the target feature 
    converted to a numerical feature.
    =========================================================================
    '''
    try:
        # Creating a mapping from numeric to categorical values
        mapping = {0:"No", 1:"Yes"}
        
        # Changing the target feature from numerical to categorical
        df[col] = df[col].map(mapping)
        
        return df
    
    except Exception as e:
        raise CustomException(e, sys)

# Creating a function to convert the column names to lower case
def convert_column_names_to_lower_case(df:pd.DataFrame) -> pd.DataFrame:
    '''
    This function takes a dataframe as input and then converts the column
    names from capital case to lower case.
    =========================================================================
    ------------------
    Parameters:
    ------------------
    df : pd.DataFrame - This is the dataframe that contains the column names
    in capital case.
    
    ---------------
    Returns:
    ---------------
    df : pd.DataFrame - This is the dataframe with the column names as lower
    case.
    =========================================================================
    '''
    try:
        # Converting column names to lower case
        df.columns = df.columns.map(lambda x: x.lower())
        return df
    
    except Exception as e:
        raise CustomException(e, sys)

# Creating a function to create the run_config folder
def create_run_config_dir():
    '''
    This function creates the run config folder. The run config folder will be
    created at the root level of the project.
    ========================================================================================
    ---------------------
    Returns:
    ---------------------
    dir_path : str - Returns the path to the run_config folder at the 
    root level of the project.
    ========================================================================================
    '''
    try:
        # Getting the absolute path of the directory containing the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Moving up two levels to reach the root of the project
        root_dir = os.path.abspath(os.path.join(script_dir, "../"))
        
        # Creating the path to the run_config folder
        dir_path = os.path.join(root_dir, 'run_config')
        os.makedirs(dir_path, exist_ok=True)
        
        return dir_path
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to store the run parameters
def save_run_params(run_params:dict, run_config_dir:str):
    '''
    This function saves the run parameters as a json file in the run_config folder. The
    function also checks if the run_config folder exists. If the folder does not exist, the
    function will create the folder.
    ========================================================================================
    ---------------------
    Parameters:
    ---------------------
    run_params : dict - This is the dictionary containing the run parameters.
    
    ---------------------
    Returns:
    ---------------------
    Saves the run parameters as a json file into the run_config folder.
    ========================================================================================
    '''
    try:
        # Creating a variable to store the current date and time
        now = datetime.now().strftime('%Y%m%d_%H-%M-%S')
        
        # Creating the path to the json file
        json_path = os.path.join(run_config_dir, f'run_params_{now}.json')
        
        # Saving the run parameters as a json file
        with open(json_path, 'w') as f_obj:
            json.dump(run_params, f_obj)
        
    except Exception as e:
        raise CustomException(e, sys)
    

# Creating a function to load the run parameters json file
def load_run_params(directory='run_config'):
    '''
    This function loads the run parameters as a json file, which is present
    in the run_config folder. 
    ========================================================================================
    ---------------------
    Parameters:
    ---------------------
    directory : str - This is the name of the directory in which the run parameters json
    file is stored.
    
    ---------------------
    Returns:
    ---------------------
    run_parameters : json - This is the run parameters json file.
    ========================================================================================
    '''
    try:
        # Creating the path to the run_config folder
        dir_path = Path.cwd() / directory
        
        # Listing all the files present in the director
        json_files = os.listdir(dir_path)
        
        # Selecting the latest file
        latest_file = None
        latest_date = None
        for file_name in json_files:
            date_str = file_name.split('_')[2].split('.')[0]
            file_date = datetime.strptime(date_str, '%Y%d%m')
            if not latest_date or file_date > latest_date:
                latest_date = file_date
                latest_file = dir_path / file_name
        
        return latest_file
    
    except Exception as e:
        raise CustomException(e, sys)

# Creating a function to read the json file
def read_json_file(file_path:str):
    '''
    This function reads a JSON file and returns the contents of the file.
    ========================================================================================
    ---------------------
    Parameters:
    ---------------------
    file_path : str - This is the path to the run parameters json file.
    
    ---------------------
    Returns:
    ---------------------
    data : json - This is the contents of the JSON file.
    =========================================================================================
    '''
    try:
        # Reading the json file
        with open(file_path, 'r') as f_obj:
            data = json.load(f_obj)
        return data
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to define the model name dynamically
def get_next_model_name(client, base_name):
    '''
    This function uses the client to fetch the latest model name, extracts the last version 
    number and then generates the next model name.
    ========================================================================================
    ---------------------
    Parameters:
    ---------------------
    client : mlflow.tracking.MlflowClient - This is the client object to interact with the 
    model registry.
    base_name : str - This is the base name of the model.
    
    ---------------------
    Returns:
    ---------------------
    next_model_name : str - This is the next model name with the latest version number.
    =========================================================================================
    '''
    try:
        # Searching for registered models
        registered_models = client.search_registered_models()
        
        # Creating a variable to store the maximum version number of a model
        max_num = 0
        
        # Defining the prefix of the model name
        prefix = f"{base_name}_"
        
        # Defining the model name
        for model in registered_models:
            if model.name.startswith(prefix):
                try:
                    num = int(model.name.split('_')[-1])
                    if num > max_num:
                        max_num = num
                except ValueError:
                    continue
                
        return f"{base_name}_{max_num + 1}"
    
    except Exception:
        return f"{base_name}_1"

# Creating a function to load the preprocessing object
def load_preprocessor_object():
    '''
    This function loads the preprocessor object from the artifacts folder. The 
    function returns the preprocessor object.
    ========================================================================================
    ---------------------
    Returns
    ---------------------
    preprocessor : object - This is the preprocessor object loaded from the artifacts folder.
    ========================================================================================
    '''
    try:
        # Getting the path for the preprocessor object
        preprocessor_config = DataTransformationConfig() 
        preprocessor_obj_path = preprocessor_config.preprocessor_obj_path
        
        # Loading the preprocessor object
        preprocessor_obj = joblib.load(preprocessor_obj_path)
        
        return preprocessor_obj
    
    except Exception as e:
        raise CustomException(e, sys)