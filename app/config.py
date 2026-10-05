import toml
from pathlib import Path

def loadConfig(config_file: Path):
    if not config_file.exists():
        raise FileNotFoundError(f"Kritik Hata: Yapılandırma dosyası bulunamadı -> {config_file}")
    
    with open(config_file, "r") as f:
        return toml.load(f)