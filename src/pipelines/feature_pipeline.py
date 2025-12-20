# Importing packages
from src.components.data_ingestion import DataIngestion

# Running the feature pipeline
if __name__ == '__main__':
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()