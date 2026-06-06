# Importing packages
import sys
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.exception import CustomException

# Creating the database instance
db = SQLAlchemy()

# Creating the flask application factory
def create_app(root_dir=None):
    '''
    This function creates and configures the Flask application instance. It
    also creates the database folder and creates a URI pointing to the 
    database folder.
    ===========================================================================
    -----------------
    Parameters:
    -----------------
    root_dir: str - This is the path to the root directory of the project.
        
    -----------------
    Returns:
    -----------------
    app: Flask - This is the Flask application instance that has been created
    and configured.
    ===========================================================================
    '''
    try:
        # Creating a path to the root directory of the project
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        # Defining the template folder path
        template_dir = os.path.join(root_dir, "template")
        # Defining the path to the static folder
        static_dir = os.path.join(root_dir, "static")
        # Defining the path to the database folder
        db_dir = os.path.join(root_dir, "db")
        
        # Creating the database folder, if it does not already exist
        os.makedirs(db_dir, exist_ok=True)
        
        # Creating the app instance with the template and static folder paths
        app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
        
        # Configure SQLAlchemy with URI pointing to the database folder
        db_path = os.path.join(db_dir, "placement.db")
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        
        # Registering the database instance with the app
        db.init_app(app)

        return app
    
    except Exception as e:
        raise CustomException(e, sys)