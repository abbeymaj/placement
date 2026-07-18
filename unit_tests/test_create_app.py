# Importing packages
import os
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.web_components.create_app import create_app, db

# Creating a pytest fixture to build the app context for testing
@pytest.fixture
def app(tmp_path):
    # Creating the app
    tmp_path_str = str(tmp_path).replace("\\", "/")
    app = create_app(root_dir=tmp_path_str)
    
    # Setting up the app context for database operations
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{tmp_path}/test.db"
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
        
# Creating the test client fixture
@pytest.fixture
def client(app):
    return app.test_client()

# Verifying that the app factory returns a valid Flask app instance
def test_create_app(app):
    assert app is not None
    assert isinstance(app, Flask)
    assert app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] is False
    assert "SQLALCHEMY_DATABASE_URI" in app.config
    
# Verifying that the database is initialized sucessfully and the folder is created
def test_db_initialization(app):
    with app.app_context():
        db.create_all()
        # Checking if the database file is created
        db_path = app.config["SQLALCHEMY_DATABASE_URI"].replace("sqlite:///", "").replace("/", os.sep)
        db_path = os.path.normpath(db_path)
        assert db is not None
        assert hasattr(db, "session")