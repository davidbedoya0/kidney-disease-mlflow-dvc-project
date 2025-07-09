from dataclasses import dataclass
from pathlib import Path

# dataclass is a class that is used to create a data class
# froze = True significa que la clase es inmutable, es decir, no se puede modificar sus atributos
# dataclass es util para crear clases que se usan para almacenar datos ya que no se necesita definir el constructor
@dataclass(frozen=True)
class DataIngestionConfig: 
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path