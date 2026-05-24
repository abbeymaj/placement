# Importing packages
from src.web_components.create_app import create_app
from src.web_components.routes import main_blueprint

# Creating the flask application
app = create_app()

# Registering the routers
app.register_blueprint(main_blueprint)

# Running the flask app
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"Failed to run the flask application: {e}")