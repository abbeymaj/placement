# Importing packages
from datetime import datetime, timezone
from src.web_components.create_app import db

# Creating a class to store the data entered by the user
class Data(db.Model): 
    '''
    This class is used to store the data entered by the user through
    the web interface.
    '''
    __tablename__ = 'data'
    
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    iq = db.Column(db.Integer, nullable=False)
    cgpa = db.Column(db.Float, nullable=False)
    communication_skills = db.Column(db.Integer, nullable=False)
    projects_completed = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    preds = db.relationship('Predictions', backref='data', lazy=True)
    
    # Creating a method to return a string representation of the class
    def __repr__(self):
        '''
        This method returns the string representation of the Data class.
        '''
        return f"Data('{self.iq}', '{self.cgpa}', '{self.communication_skills}', '{self.projects_completed}')"

# Creating a class to store the predictions made by the model
class Predictions(db.Model):
    '''
    This class is used to store the predictions made by the model.
    '''
    __tablename__ = 'predictions'
    
    pred_id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.Integer, db.ForeignKey('data.id'), nullable=False)
    prediction = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    # Creating a method to return a string representation of the class
    def __repr__(self):
        '''
        This method returns the string representation of the Predictions class.
        '''
        return f"Predictions('{self.prediction}')"
        
    