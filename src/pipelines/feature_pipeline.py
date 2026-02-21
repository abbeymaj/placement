# Importing packages
from src.components.data_ingestion import DataIngestion
from src.components.transform_data import TransformData
from src.components.create_feature_store import CreateFeatureStore

# Running the feature pipeline
if __name__ == '__main__':
    
    # Ingesting the data and creating the artifacts folder
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    
    # Transforming the data and creating the preprocessor object
    transform = TransformData()
    train_data, test_data, _ = transform.initiate_data_transformation(
        train_path=train_data_path, 
        test_path=test_data_path
        )
    
    # Creating the feature store and saving the transformed datasets
    # in the feature store folder
    feature_store = CreateFeatureStore()
    feature_store.create_feature_store(train_data=train_data, test_data=test_data)