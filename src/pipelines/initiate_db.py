# Importing packages
from src.web_components.create_app import create_app, db
from src.web_components.models import Data, Predictions

# Initiating the database
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database and tables created successfully!")