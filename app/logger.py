from loguru import logger
from pathlib import Path

def setup_logger(base_dir: Path):
    logger.remove()
    log_dir = base_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    
    log_path = log_dir / "app.log"
    logger.add(str(log_path), rotation="500 MB", mode="w")
    return logger