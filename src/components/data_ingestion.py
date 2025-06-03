import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.txt")
    test_data_path: str = os.path.join("artifacts", "test.txt")
    raw_data_path: str = os.path.join("artifacts", "raw.txt")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def read_single_text_file(self, file_path):
        """
        Reads Dataset.txt where each line is formatted as: resume_text,label
        Adjust delimiter if necessary (e.g., tab).
        """
        data = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        if "," in line:
                            parts = line.split(",", 1)
                            if len(parts) == 2:
                                text, label = parts
                                data.append({"text": text.strip(), "label": label.strip()})
                        else:
                            logging.warning(f"Skipping improperly formatted line: {line}")
        except Exception as e:
            raise CustomException(e, sys)
        
        return pd.DataFrame(data)

    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion method/component")
        try:
            file_path = os.path.join("data", "Dataset.txt")
            df = self.read_single_text_file(file_path)
            logging.info(f"Loaded {len(df)} samples from {file_path}")

            # Create directory if not exists
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)

            # Save raw data as txt with tab separator
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False, header=True, sep='\t')

            logging.info("Train-Test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test data as txt files (tab separated)
            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True, sep='\t')
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header=True, sep='\t')
            logging.info("Data ingestion completed successfully")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
