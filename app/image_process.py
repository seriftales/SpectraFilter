
import cv2
import numpy as np

# Görüntü İşleme Motoru:Verilen RGB görüntüyü HSV formatına çevirerek yapılandırma dosyasındaki sınırlara göre mantıksal maskeleme işlemleri uygular.
class ImageProcessor:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger  

    def process_image(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        colors = self.config['colors']

        # Mavi
        blue_lower = np.array(colors['blue_lower'], dtype=np.uint8)
        blue_upper = np.array(colors['blue_upper'], dtype=np.uint8)
        blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
        blue_output = cv2.bitwise_and(image, image, mask=blue_mask)
        blue_pixels = np.count_nonzero(blue_mask)

        # Yeşil
        green_lower = np.array(colors['green_lower'], dtype=np.uint8)
        green_upper = np.array(colors['green_upper'], dtype=np.uint8)
        green_mask = cv2.inRange(hsv, green_lower, green_upper)
        green_output = cv2.bitwise_and(image, image, mask=green_mask)
        green_pixels = np.count_nonzero(green_mask)

        # Kırmızı 
        red_lower1 = np.array(colors['red_lower1'], dtype=np.uint8)
        red_upper1 = np.array(colors['red_upper1'], dtype=np.uint8)
        red_lower2 = np.array(colors['red_lower2'], dtype=np.uint8)
        red_upper2 = np.array(colors['red_upper2'], dtype=np.uint8)
        red_mask = cv2.bitwise_or(
            cv2.inRange(hsv, red_lower1, red_upper1),
            cv2.inRange(hsv, red_lower2, red_upper2)
        )
        red_output = cv2.bitwise_and(image, image, mask=red_mask)
        red_pixels = np.count_nonzero(red_mask)

        # Sarı
        yellow_lower = np.array(colors['yellow_lower'], dtype=np.uint8)
        yellow_upper = np.array(colors['yellow_upper'], dtype=np.uint8)
        yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
        yellow_output = cv2.bitwise_and(image, image, mask=yellow_mask)
        yellow_pixels = np.count_nonzero(yellow_mask)

        if np.any(blue_mask):
            self.logger.success(f"Mavi tespit edildi. Piksel: {blue_pixels}")
        else:
            self.logger.info("Mavi tespit edilemedi.")

        if np.any(green_mask):
            self.logger.success(f"Yesil tespit edildi. Piksel: {green_pixels}")
        else:
            self.logger.info("Yesil tespit edilemedi.")

        if np.any(red_mask):
            self.logger.success(f"Kirmizi tespit edildi. Piksel: {red_pixels}")
        else:
            self.logger.info("Kirmizi tespit edilemedi.")

        if np.any(yellow_mask):
            self.logger.success(f"Sari tespit edildi. Piksel: {yellow_pixels}")
        else:
            self.logger.info("Sari tespit edilemedi.")

        return blue_output, green_output, red_output, yellow_output