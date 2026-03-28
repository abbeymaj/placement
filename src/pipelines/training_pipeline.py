# Importing packages
from src.utils import create_run_config_dir
from src.components.manage_model import UploadModelToRegistry

# Running the training pipeline
if __name__ == '__main__':
    
    # Creating the run_config folder
    dir_path = create_run_config_dir()
    
    # Uploading the model to the model registry and saving the model metadata
    # in the run_config folder
    model_registry = UploadModelToRegistry()
    _ = model_registry.upload_model_to_registry(dir_path)