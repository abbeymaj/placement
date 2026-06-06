# Importing packages
import os
from flask import Blueprint, render_template, request, jsonify
from src.web_components.create_app import db
from src.web_components.models import Data, Predictions
from src.components.create_custom_data import CreateCustomData
from src.components.make_predictions import MakePrediction

# Creating a blueprint for the routes
main_blueprint = Blueprint('main', __name__)

# Creating a function to render the home page
@main_blueprint.route('/')
def index():
    '''
    This function creates the homepage for this application.
    '''
    return render_template('index.html')

# Creating a function to make predictions using the user entered data
@main_blueprint.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    '''
    This function will display the prediction landing page, if the method
    is GET. If the method is POST, then the prediction will be returned.
    The prediction is displayed on the same page, below the form.
    '''
    # Retrieving the page to make the predictions if the method is GET
    if request.method == 'GET':
        return render_template('predict.html')
    
    # Making the prediction if the method is POST
    elif request.method == 'POST':
        # Capturing the data entered by the user
        data = CreateCustomData(
            iq = int(request.form.get('iq')),
            cgpa = float(request.form.get('cgpa')),
            communication_skills = int(request.form.get('communication_skills')),
            projects_completed = int(request.form.get('projects_completed'))
        )
        
        # Building the dataframe and then creating the data row as a 
        # dictionary to load into the database
        df = data.create_dataframe()
        row = df.iloc[0].to_dict()
        
        # Loading the row int the Data table
        data_entry = Data(
            time = row['time'],
            iq = row['iq'],
            cgpa = row['cgpa'],
            communication_skills = row['communication_skills'],
            projects_completed = row['projects_completed']
        )
        db.session.add(data_entry)
        db.session.flush()
        
        # Making a prediction using the user entered data in the 
        # dataframe. To begin with, dropping the time column
        # from the dataframe.
        df.drop(labels=['time'], axis=1, inplace=True)
        prediction = MakePrediction()
        preds1 = prediction.make_predictions(df)
        preds_int = 1 if preds1 == "Yes" else 0

        # Storing the prediction data into the Predictions table
        pred_entry = Predictions(
            data_id = data_entry.id,
            prediction = preds_int
        )
        db.session.add(pred_entry)
        db.session.commit()

        # Returning the prediction to the web application
        return render_template('predict.html', result=preds1, pred_df=df)