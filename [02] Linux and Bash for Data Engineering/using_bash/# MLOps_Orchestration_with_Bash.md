# MLOps Orchestration: Bash ile Süreç Yönetimi

Bu rehber, veri bilimi ve makine öğrenmesi projelerinde manuel adımları otomatize ederek "tekrarlanabilirlik" (reproducibility) sağlamak için Bash scriptlerinin nasıl bir orkestra şefi gibi kullanılacağını açıklar.

## 1. Orkestrasyon Nedir?
MLOps bağlamında orkestrasyon; veri çekme, temizleme, model eğitimi ve sonuçların kaydedilmesi gibi birbirinden bağımsız çalışan görevlerin belirli bir sıra ve mantık çerçevesinde tek bir merkezden yönetilmesidir.



## 2. Neden Bash Script Kullanmalıyız?
* **Yapıştırıcı Görevini Görür:** Farklı Python scriptlerini, sistem komutlarını ve ortam ayarlarını birbirine bağlar.
* **Hata Yönetimi:** Bir adım başarısız olursa tüm süreci durdurarak hatalı model eğitimini engeller.
* **Zaman Tasarrufu:** Her seferinde sanal ortamı açmak veya dizin değiştirmek gibi tekrarlayan işleri otomatikleştirir.

---

## 3. Örnek Bir Orkestrasyon Dosyası (`run_pipeline.sh`)

Aşağıdaki script, senin kurduğun profesyonel yapıyı (sanal ortam, API anahtarları, dizin yapısı) kullanarak tam bir iş akışı sunar:

```bash
#!/bin/bash

# --- GÜVENLİK AYARLARI ---
set -euo pipefail  # Hata durumunda dur, tanımsız değişkeni engelle.

# --- ADIM 0: ÇEVRESEL AYARLAR ---
echo ">>> Ortam hazırlanıyor..."
source ~/apikeys.sh              # API anahtarlarını yükle
source ~/de_venv/bin/activate     # Sanal ortamı aktif et
cd /mnt/c/DE_Projects            # Proje dizinine geç

# --- ADIM 1: VERİ TOPLAMA ---
echo ">>> Veri çekme işlemi başlatıldı..."
python src/data_ingestion.py --source "solar_api"

# --- ADIM 2: VERİ TEMİZLEME (Opsiyonel Kontrol) ---
if [ -f "data/raw/latest_data.csv" ]; then
    echo ">>> Veri bulundu, ön işleme geçiliyor..."
    python src/preprocess.py
else
    echo "!!! HATA: Ham veri dosyası bulunamadı."
    exit 1
fi

# --- ADIM 3: MODEL EĞİTİMİ ---
echo ">>> Model eğitimi başlatılıyor..."
python src/train_model.py | tee logs/training_$(date +%F).log

# --- ADIM 4: TEMİZLİK VE RAPORLAMA ---
deactivate
echo ">>> İşlem başarıyla tamamlandı: $(date)"
```

---

## 4. Kritik Orkestrasyon Komutları

| Durum | Komut / Yapı | Amaç |
| :--- | :--- | :--- |
| **Koşullu Çalıştırma** | `komut1 && komut2` | 1. başarılıysa 2.'yi çalıştır. |
| **Veya Çalıştırma** | `komut1 || komut2` | 1. başarısız olursa 2.'yi çalıştır. |
| **Loglama** | `komut \| tee output.log` | Çıktıyı hem ekrana bas hem dosyaya yaz. |
| **Zamanlama** | `crontab -e` | Scripti her gece 03:00'te otomatik çalıştır. |

---

## 5. "Pattern Archaeologist" İçin Stratejik Notlar
* **Veri İzleri:** Scriptine ekleyeceğin loglama sistemleri, sistemdeki "trace"leri (izleri) takip etmeni kolaylaştırır.
* **Project INDIEGRID Uyumu:** Bu script yapısı, solar enerji verilerini çeken cihazlar ile bu verileri analiz eden Python kodların arasındaki köprüdür.
* **Bağımsızlık:** Bu otomasyon sayesinde terminaldeki o "mavi ok" dünyası, sen başında olmasan bile senin adına veri kazmaya devam eder.

---

Bu `.md` dosyası, kurduğun o akıllı terminalin gerçek gücünü nasıl kullanacağını gösteren bir yol haritasıdır.