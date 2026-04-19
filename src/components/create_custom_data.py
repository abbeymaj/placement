# Importing packages
import sys
from datetime import datetime
import pandas as pd
from src.exception import CustomException

# Creating a class to capture custom data
class CreateCustomData():
    '''
    This class is responsible for converting user entered data into a
    pandas dataframe. The class contains two methods - a class constructor
    and a method to convert the user entered data into a Pandas dataframe.
    The objective of this class is to convert user entered data into a 
    dataframe, which can then be used to make predictions.
    '''
    # Creating the contructor for the class
    def __init__(
        self,
        iq:int,
        cgpa:float,
        communication_skills:int,
        projects_completed:int
    ):
        '''
        This is the constructor for this class. It contains a list of all
        data elements, which will be entered by the user on the web
        application.
        '''
        self.iq = iq
        self.cgpa = cgpa
        self.communication_skills = communication_skills
        self.projects_completed = projects_completed
    
    # Creating the method to convert the user entered data into a Pandas
    # dataframe.
    def create_dataframe(self):
        '''
        This method takes the user entered data and converts the data into
        a Pandas dataframe. First, the method converts the user entered
        data into a Python dictionary and then uses the dictionary to convert
        the data into a dataframe.
        ========================================================================
        -------------------
        Returns:
        -------------------
        df :  Pandas DataFrame - This is the pandas dataframe with the user entered
        data.
        ========================================================================
        '''
        try:
            # Taking the current date and time
            current_date_time = datetime.now()
            
            # Converting the user entered data into a Python dictionary
            data = {
                'time': [current_date_time],
                'iq': [self.iq],
                'cgpa': [self.cgpa],
                'communication_skills': [self.communication_skills],
                'projects_completed': [self.projects_completed]
            }
            
            # Converting the data dictionary into a Pandas dataframe
            df = pd.DataFrame(data)
            
            return df
        
        except Exception as e:
            raise CustomException(e, sys)
        
        
    