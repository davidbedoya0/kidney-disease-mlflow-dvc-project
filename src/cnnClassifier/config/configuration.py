from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager: 
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # se crea el directorio de artefactos si no existe
        create_directories([self.config.artifact_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:

        # se obtiene la configuracion de la ingestion de datos desde el archivo de configuracion config/config.yaml 
        config = self.config.data_ingestion

        # se crea el directorio de la ingestion de datos si no existe
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config