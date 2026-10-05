# SpectraFilter

SpectraFilter, OpenCV ve HSV renk uzayını kullanarak girdi olarak verilen statik bir görüntüden belirli renk bantlarını  ayrıştıran ve mantıksal maskeleme  ile izole eden bir Computer Vision projesidir.

Proje, renk tespitlerini tek bir ekranda göstermek yerine her bir renk kanalını kendi izole penceresinde filtreleyerek detaylı bir spektrum analizi sunar.

## 🚀 Özellikler

* **Çoklu Spektrum Ayrıştırma:** Görüntüyü renk kanallarına böler ve her bir rengi ayrı bir filtre penceresinde gösterir 
* **Dinamik Konfigürasyon:** Renk algılama sınırları koda gömülmek yerine `config.toml` dosyasından okunur.
* **Merkezi Loglama:** Eksik veri, hatalı dosya yolu veya bozuk donanım durumunda sistem sessizce çökmek yerine `loguru` üzerinden hatayı detaylandırarak güvenli çıkış yapar.

## 🛠️ Kurulum (Ubuntu / Linux)

Sistem bağımlılıklarının çakışmaması için projenin izole bir Python sanal ortamında (venv) çalıştırılması önerilir.

1. **Depoyu Klonlayın:**
   ```bash
   git clone [https://github.com/seriftales/SpectraFilter.git](https://github.com/seriftales/SpectraFilter.git)
   cd SpectraFilter
   ```
2. **Sanal Ortam Oluşturun ve Aktif Edin:**
   ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```

3. **Gerekli Paketleri Yükleyin:**
   ```bash
    pip install -r requirements.txt
   ```

## ⚙️ Çalıştırma 

İşlemek istediğiniz görüntüleri projenin kök dizinindeki data/ klasörü içerisine yerleştirin.

Uygulamayı başlatmak için terminalden -i veya --image parametresi ile dosya adını verin:

```bash
python3 app.py --image test.jpg
```
Uygulama, belirtilen görüntüyü okur ve tespit edilen renkleri ayrı pencerelerde filtreleyerek ekrana basar.

Görüntü işleme tamamlandığında uygulamadan çıkmak için aktif pencere üzerindeyken klavyeden herhangi bir tuşa basmanız yeterlidir.

## 📁 Dizin Yapısı

```text 
SpectraFilter/
├── app/
│   ├── __init__.py          # Paketleyici
│   ├── image_process.py     # HSV dönüşümü, bitwise maskeleme ve renk filtreleme algoritmaları
│   ├── config.py            # TOML okuyucu 
│   ├── logger.py            # Loguru rotasyonlu loglama altyapısı
│   └── streamer.py          # Statik görüntü okuma ve doğrulama motoru
├── config/
│   └── config.toml          # Renklerin dinamik HSV spektrum alt/üst sınırları
├── data/
│   └── test8.jpg            # İşlenecek örnek görüntüler 
├── logs/
│   └── app.log              # Uygulama çalışma zamanı kayıtları 
├── .gitignore              
├── requirements.txt         
└── app.py                   # Entry Point
```