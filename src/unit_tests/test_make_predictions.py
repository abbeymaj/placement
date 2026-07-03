# Importing packages
import dagshub
import mlflow
from mlflow.tracking import MlflowClient
from src.utils import load_preprocessor_object
from src.components.config_entity import ModelURIConfig
from src.components.create_custom_data import CreateCustomData
from src.components.make_predictions import MakePrediction

# Verifying that the latest model version can be retrieved
def test_get_latest_model_version():
    dagshub.init(repo_owner='abbeymaj', repo_name='placement', mlflow=True)
    model_config = ModelURIConfig()
    model_uri = model_config.model_uri_path
    mlflow.set_tracking_uri(model_uri)
    model_name = 'training_model'
    client = MlflowClient(tracking_uri=model_uri)
    latest_version_info = client.get_latest_versions(name=model_name)[0]
    latest_model_name = latest_version_info.name
    latest_model_version = latest_version_info.version
    latest_model_source = latest_version_info.source
    latest_run_id = latest_version_info.run_id
    model = mlflow.sklearn.load_model(latest_model_source)
    assert latest_model_version == '4'
    assert model is not None

# Verifying that the fetch_latest_model method is working as expected
def test_fetch_latest_model():
    prediction = MakePrediction()
    model = prediction.fetch_latest_model()
    assert model is not None

# Verifying that the preprocessor object can be loaded successfully
def test_load_preprocessor_object(): 
    preprocessor_obj = load_preprocessor_object()
    assert preprocessor_obj is not None

# Verifying that the make_predictions method is working as expected
def test_make_predictions():
    # Setting mock data for this test case
    data = {
        'iq': 90,
        'cgpa': 8.5,
        'communication_skills': 8,
        'projects_completed': 3
    }
    
    # Creating an object of the CreateCustomData class
    custom_data = CreateCustomData(**data)
    
    # Converting the data into a pandas dataframe
    df = custom_data.create_dataframe()
    
    # Creating an object of the MakePrediction class
    prediction = MakePrediction()
    
    # Dropping the time feature
    df.drop('time', axis=1, inplace=True)
    
    # Making predictions suing the make_predictions method
    preds = prediction.make_predictions(df)
    
    assert preds is not None
    