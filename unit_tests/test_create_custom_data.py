# Importing packages
import pandas as pd
from src.components.create_custom_data import CreateCustomData

# Verifying that the CreateCustomData class is working as expected
def test_create_custom_data():
    # Creating a dictionary with the user entered data
    data  = {
        'iq': 90,
        'cgpa': 8.5,
        'communication_skills': 8,
        'projects_completed': 3
    }
    
    # Creating an object of the CreateCustomData class
    custom_data = CreateCustomData(**data)
    
    # Converting the data into a pandas dataframe
    df = custom_data.create_dataframe()
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert df.shape[1] == 5