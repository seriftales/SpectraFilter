import cv2
from pathlib import Path

def get_image(image_path: Path):
    if not image_path.exists():
        raise FileNotFoundError(f"Kritik Hata: Görüntü dosyası bulunamadı -> {image_path}")
    
    image = cv2.imread(str(image_path))
    
    if image is None:
        raise ValueError(f"Görüntü okunamadı veya format bozuk -> {image_path}")
        
    return image