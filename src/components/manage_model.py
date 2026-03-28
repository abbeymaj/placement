# Importing packages
import sys
import dagshub
import mlflow
from datetime import datetime
from mlflow.tracking import MlflowClient
from src.utils import get_next_model_name
from src.utils import save_run_params
from src.components.config_entity import ModelURIConfig
from src.components.train_model import TrainModel
from src.exception import CustomException

# Creating a class to upload the trained model to the model registry
class UploadModelToRegistry():
    '''
    This class is used to upload the trained model to the model registry. The model
    registry, which is MLFlow, is hosted on Dagshub. The class has two methods -
    the constructor and a method to upload the trained model to the model registry.
    '''
    # Creating the constructor for the UploadModelToRegistry class
    def __init__(self):
        '''
        This is the constructor for the UploadModelToRegistry class.
        '''
        self.model_uri_config = ModelURIConfig()
    
    # Creating a method to upload the trained model to the model registry
    def upload_model_to_registry(self):
        '''
        This method trains the model and then uploads the model into the model registry.
        ==============================================================================
        ------------------------
        Returns:
        ------------------------
        model_uri : str - This is the URI of the uploaded model.
        ==============================================================================
        '''
        try:
            # Instantiating the dagshub client
            dagshub.init(repo_owner='abbeymaj', repo_name='placement', mlflow=True)
            
            # Setting the model tracking URI
            model_uri = self.model_uri_config.model_uri_path
            mlflow.set_tracking_uri(model_uri)
            
            # Creating the mlflow client
            client = MlflowClient()
            
            # Setting the model name
            base_name = 'training_model'
                        
            # Defining the run name
            time_now = datetime.now().strftime('%Y%m%d_%H-%M-%S')
            run_name = f"{base_name}_{time_now}"
            
            # Setting the experiment ID at the Global Level
            experiment_id = mlflow.set_experiment(base_name)
            
            # Initiating the model training run
            run_params = {}
            with mlflow.start_run(run_name=run_name, experiment_id=experiment_id) as run:
                # Initiating the model trainer
                trainer = TrainModel()
                # Fetching the best model
                best_model, model_params = trainer.initiate_model_training()
                # Logging the model parameters
                mlflow.log_params(model_params)
                # Logging the best model
                model_info = mlflow.sklearn.log_model(
                    sk_model=best_model,
                    artifact_path="models",
                    registered_model_name=base_name
                )
            
                # Fetching the model metadata to store in the run_params directory
                run_id = run.info.run_id
                latest_version_info = client.get_latest_versions(name=base_name, stages=['None'])[0]
                model = latest_version_info.name
                version = latest_version_info.version
                model_uri = model_info.model_uri
                
                # Storing the model metadata in the run_params dictionary
                run_params['run_id'] = run_id
                run_params['model'] = model
                run_params['version'] = version
                run_params['model_uri'] = model_uri
            
            # Saving the run params
            save_run_params(run_params)
            
            return model_uri
                
        except Exception as e:
            raise CustomException(e, sys)