import os
import sys
import argparse

import cv2
from pathlib import Path
from app.streamer import get_image
from app.image_process import ImageProcessor
from app.config import loadConfig
from app.logger import setup_logger

# Renk Tespit Sistemi:Ortam değişkenlerini yapılandırır ve görüntü işleme sürecini başlatır.

def parse_arguments():

    parser = argparse.ArgumentParser(description="Renk Tespit Sistemi")
    parser.add_argument(
        "-i", "--image", 
        type=str, 
        required=True, 
        help="data klasöründeki işlenecek görüntünün adı (Orn: test0.jpeg)"
    )
    return parser.parse_args()


def main():
    args = parse_arguments() # Terminalden gelen verileri al
    
    BASE_DIR = Path(__file__).resolve().parent
    logger = setup_logger(BASE_DIR)
    
    config_path = BASE_DIR / "config" / "config.toml"
    config = loadConfig(config_path)

    image_path = BASE_DIR / "data" / args.image
    
    if not image_path.exists():
        logger.error(f"Hata: Belirtilen görüntü dosyası data klasöründe bulunamadı -> {image_path}")
        sys.exit(1)

    image = get_image(image_path)

    processor = ImageProcessor(config, logger)
    blue_out, green_out, red_out, yellow_out = processor.process_image(image)

    cv2.imshow("Original", image)
    cv2.imshow("Blue Filter", blue_out)
    cv2.imshow("Green Filter", green_out)
    cv2.imshow("Red Filter", red_out)
    cv2.imshow("Yellow Filter", yellow_out)

    logger.info("Işlem tamamlandı. Çıkış için aktif penceredeyken bir tuşa basınız.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()