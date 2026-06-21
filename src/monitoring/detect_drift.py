# Importing packages
import sys
import os
import pandas as pd
from datetime import datetime, timezone
from evidently import Dataset, DataDefinition, Report, BinaryClassification
from evidently.presets import DataDriftPreset
from src.utils import read_sql_data
from src.components.config_entity import DatabaseConfig
from src.components.config_entity import DriftReportConfig
from src.components.config_entity import DataIngestionConfig
from src.exception import CustomException

# Creating a class to detect data drift with features and targets
class DetectDataDrift():
    '''
    This class is used to detect drifts in both features and targets. The class
    will also use the Evidently package to create a report on the drift.
    '''
    # Creating the constructor for the class
    def __init__(self):
        '''
        This is the constructor for the class. It will initialize the database
        configuration and the drift report configuration.
        '''
        self.ingestion_config = DataIngestionConfig()
        self.db_config = DatabaseConfig()
        self.report_config = DriftReportConfig()
    
    # Creating a method to read the data from the database
    def read_data_from_db(self):
        '''
        This method reads the data from the data and predictions tables in the database.
        The class will use the read_sql_data function from the utils module to read the data.
        '''
        try:
            # Reading the data from the data table
            data_df = read_sql_data(table='data')
            
            # Reading the data from the predictions table
            preds_df = read_sql_data(table='predictions')
            
            # Merging both datasets
            merged_df = data_df.merge(preds_df, left_on='id', right_on='data_id', how='left')
            
            # Defining the columns to keep
            cols_to_keep = [
                'iq',
                'cgpa',
                'communication_skills',
                'projects_completed',
                'prediction'
            ]
            
            # Keeping the required columns only
            merged_df = merged_df[cols_to_keep]
            
            # Renaming the prediction column to the target name
            merged_df.rename(columns={'prediction': 'placement'}, inplace=True)
            
            return merged_df
        
        except Exception as e:
            raise CustomException(e, sys)
    
    # Creating a method to run the data drift detection
    def detect_data_drift(self, save_report: bool = True):
        '''
        This method runs the data drift detection using the Evidently package. It will create a report
        and save the report in the "reports" folder. The report will be returned as a html file.
        '''
        try:
            # Reading the data from the training dataset and only keeping the required columns
            train_df = pd.read_parquet(self.ingestion_config.train_data_path)
            train_df.columns = train_df.columns.str.lower()
            cols_to_keep = [
                'iq',
                'cgpa',
                'communication_skills',
                'projects_completed',
                'placement'
            ]
            train_df = train_df[cols_to_keep]
            
            # Reading the data from the database
            db_df = self.read_data_from_db()
            
            # Defining the schema for the data
            schema = DataDefinition(
                numerical_columns=['iq', 'cgpa', 'communication_skills', 'projects_completed'],
                classification=[BinaryClassification(target='placement', prediction_labels=[0,1])]
            )
            
            # Creating the dataset objects for the training data and database data
            train_data = Dataset.from_pandas(train_df, data_definition=schema)
            db_data = Dataset.from_pandas(db_df, data_definition=schema)
            
            # Creating the report with data drift preset
            report = Report(
                metrics=[DataDriftPreset()]
            )
            
            # Running the report 
            my_eval = report.run(
                reference_data=train_data,
                current_data=db_data
            )
            
            # Saving the report to the reports folder
            if save_report:
                my_eval.save_html(self.report_config.report_path)
            
        
        except Exception as e:
            raise CustomException(e, sys)
    
    # Creating a method to run the data drift detection.
    def run_data_drift_detection(self):
        '''
        This method runs the data drift detection. It will call the detect_data_drift method
        to run the data drift detection. 
        '''
        try:
            # Taking the current time in UTC timezone
            current_time = datetime.now(timezone.utc)
            
            # Running the drift detection on scheduled time
            if 1 <= current_time.day <= 7:
                self.detect_data_drift(save_report=True)
            
            else:
                print("Data drift detection is not schedule to run at this time.")
        
        except Exception as e:
            raise CustomException(e, sys)
