# Importing packages
import os
import sys
import pandas as pd
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
    df : pd.DataFrame - This is the dataframe that contains the target 
    feature.
    
    ---------------
    Returns:
    ---------------
    df : pd.DataFrame - This is the dataframe with the target feature 
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
    
