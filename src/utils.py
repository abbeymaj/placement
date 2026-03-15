# Importing packages
import os
import sys
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
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
    Creates the run_config folder at the root level of the project.
    ========================================================================================
    '''
    try:
        # Getting the absolute path of the directory containing the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Moving up two levels to reach the root of the project
        root_dir = os.path.abspath(os.path.join(script_dir, "../../"))
        
        # Creating the path to the run_config folder
        dir_path = os.path.join(root_dir, 'run_config')
        os.makedirs(dir_path, exist_ok=True)
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to store the run parameters
def save_run_params(run_params:dict):
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
        json_path = os.path.join('run_config', f'run_params_{now}.json')
        
        # Saving the run parameters as a json file
        with open(json_path, 'w') as f_obj:
            json.dump(run_params, f_obj)
        
    except Exception as e:
        raise CustomException(e, sys)
    
