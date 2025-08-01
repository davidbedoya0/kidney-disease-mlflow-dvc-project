import os 
import zipfile
import gdown 
from cnnClassifier import logger 
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion: 
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        '''
        Fetch data from the url 

        '''

        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion" , exist_ok=True)
            logger.info(f"Downloading file from {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id, zip_download_dir)
            
            logger.info(f"Downloaded data from {dataset_url} into {zip_download_dir}")

        except Exception as e:
            raise e 
        
    def extract_zip_file(self): 
        '''
        zip_file_path: str 
        Extracts the zip file into the data directory
        Function return None
        '''

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref: 
            zip_ref.extractall(unzip_path)
            