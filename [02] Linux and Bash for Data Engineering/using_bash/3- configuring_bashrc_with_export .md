# 🛡️ Brave Perspectives: Data Engineering & Secret Management
> **Linux (WSL2) üzerinde güvenli veri mühendisliği altyapısı — API anahtarları yönetimi ve Python entegrasyonu için kapsamlı rehber.**

---

## 🏗️ 1. Mimari Yapı

Sistemimiz üç temel katmandan oluşur. Bu katmanlar birbirinden bağımsız çalışır, ancak birbirini tamamlar — biri olmadan diğeri işe yaramaz.

| Katman | Dosya | Görevi |
|---|---|---|
| 🔐 Hazine Sandığı | `~/apikeys.sh` | Anahtarların fiziksel olarak saklandığı güvenli bölge |
| 📢 Duyuru Merkezi | `~/.bashrc` | Her terminal açılışında anahtarları RAM'e yükleyen motor |
| 🐍 Uygulama Katmanı | Python dosyaları | Anahtarları sistem hafızasından güvenle çeken kodlar |

> **💡 Önemli Prensip:** Anahtar asla kodun içinde yazılmaz. Kod kilit, sen anahtarsın.

---

## 🔑 2. Hazine Sandığı: `apikeys.sh`

Bu dosya `/home/kullanici_adi/apikeys.sh` konumunda saklanır. Tüm API anahtarlarını buraya `export` formatında eklersin.

```bash
# -- PERSONAL API KEYS --
# Format: export ISIM="DEGER"
# Dilediğin kadar yeni anahtar ekleyebilirsin.

export MY_PROJECT_KEY="YigitBraveCesur_2026_Projects"
export WEATHER_API_KEY="buraya_hava_durumu_keyini_yaz"
export STOCK_DATA_KEY="buraya_borsa_keyini_yaz"
export ALPHA_VANTAGE_KEY="DEMO_KEY_12345"

# -- END OF KEYS --
```

> **🔒 Güvenlik Notu:** Bu dosyayı oluşturduktan sonra izinlerini kısıtla:
> ```bash
> chmod 600 ~/apikeys.sh
> ```
> Bu komut dosyayı yalnızca senin okuyabileceğin hale getirir.

---

## ⚙️ 3. Ana Kontrol Merkezi: `.bashrc` Yapılandırması

Terminal her açıldığında anahtarların otomatik yüklenmesi için `.bashrc` dosyasının **en altına** şu bloğu ekle:

```bash
# -- START OF SECRETS LOGIC --

# 1. Anahtar dosyasının yolunu tanımla
export API_KEYS_PATH="$HOME/apikeys.sh"

# 2. Dosya varsa içeri aktar, yoksa uyar
if [ -f "$API_KEYS_PATH" ]; then
    source "$API_KEYS_PATH"
    echo "[INFO] Success: API keys loaded from $API_KEYS_PATH"
else
    echo "[WARN] Error: Keys file NOT found at $API_KEYS_PATH"
fi

# -- END OF SECRETS LOGIC --

# Otomatik Proje Dizini ve Sanal Ortam
cd /mnt/c/DE_Projects
source ~/de_venv/bin/activate
```

Değişiklikleri kaydettikten sonra terminali güncelle:

```bash
source ~/.bashrc
```

---

## 🐍 4. Python ile Anahtar Çekme

Python projelerinde anahtarları `os.getenv()` metodu ile çağırırız. Anahtarı asla doğrudan koda yazmıyoruz.

### Basit Şablon

```python
import os

def initialize_system():
    key = os.getenv("MY_PROJECT_KEY")
    if key:
        print(f"✅ Sistem Başlatıldı. Anahtar bulundu.")
        return key
    else:
        print(f"❌ HATA: Anahtar yüklenemedi!")
        return None

if __name__ == "__main__":
    my_secret = initialize_system()
```

### Gelişmiş Şablon (Çoklu Anahtar + Hata Yönetimi)

```python
import os

def load_keys():
    """Sistemden tüm gerekli anahtarları yükler ve doğrular."""
    project_key = os.getenv("MY_PROJECT_KEY")
    weather_key = os.getenv("WEATHER_API_KEY")

    if not project_key:
        print("[HATA] Anahtar bulunamadı! 'source ~/.bashrc' yaptınız mı?")
        return None, None

    return project_key, weather_key

# Kullanım
my_key, weather_key = load_keys()
if my_key:
    print(f"Sistem Hazır! Kullanılan Anahtar: {my_key}")
```

> **💡 `os.getenv` vs `os.environ[]` Farkı:**
> - `os.getenv("KEY")` → Anahtar yoksa `None` döner (güvenli, hata vermez).
> - `os.environ["KEY"]` → Anahtar yoksa `KeyError` fırlatır (dikkat ister).
> İlk şablonu kullanmak genellikle daha sağlamlıdır.

---

## 🚀 5. Gerçek Proje: Bitcoin Fiyat Takipçisi

Altyapıyı test etmek için `CoinGecko` API'sinden gerçek zamanlı Bitcoin fiyatı çeken bir proje yapalım. Bu API ücretsizdir ve kayıt gerektirmez.

### Adım 1: Sahte Anahtar Ekle (Test İçin)

```bash
nano ~/apikeys.sh
```

En alta şu satırı ekle, kaydet ve çık (`Ctrl+O` → `Enter` → `Ctrl+X`):

```bash
export ALPHA_VANTAGE_KEY="DEMO_KEY_12345"
```

Sonra terminali tazele:

```bash
source ~/.bashrc
```

### Adım 2: Python Dosyasını Oluştur

```bash
nano /mnt/c/DE_Projects/get_market_data.py
```

İçine şu kodu yapıştır:

```python
import os
import requests  # Hata verirse: pip install requests

def fetch_crypto_price():
    # 1. GİZLİ ANAHTARI SİSTEMDEN ÇEK
    api_key = os.getenv("ALPHA_VANTAGE_KEY")

    # 2. API ADRESİ
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    print(f"[INFO] Anahtar durumu: {'TAMAM' if api_key else 'EKSİK'}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # HTTP hata kodlarını yakala
        data = response.json()
        price = data['bitcoin']['usd']
        print("-" * 35)
        print(f"  Brave Market Tracker v1.0")
        print(f"  Anlık Bitcoin Fiyatı: ${price:,}")
        print("-" * 35)
    except requests.exceptions.Timeout:
        print("[HATA] Sunucu yanıt vermedi (timeout).")
    except Exception as e:
        print(f"[HATA] Veri çekilemedi: {e}")

if __name__ == "__main__":
    fetch_crypto_price()
```

### Adım 3: Çalıştır

```bash
pip install requests
python get_market_data.py
```

> **🏆 Bu kodda ne öğrendik?**
> 1. **Secret Management:** Anahtar kodun içinde değil, Linux'un güvenli bölgesinde.
> 2. **Request Handling:** İnternetten gerçek bir sunucuya bağlanıp JSON veri çektik.
> 3. **Data Parsing:** Karmaşık JSON verisinden ihtiyacımız olan tek rakamı süzdük.
> 4. **Error Handling:** `timeout` ve genel hataları ayrı ayrı yakaladık.

---

## 🗺️ 6. Yeni Anahtar Ekleme: Altın Rota

Yeni bir API anahtarı her eklediğinde bu üç adımı izle:

```bash
# 1. Anahtarı dosyaya ekle
nano ~/apikeys.sh
# → "export YENI_ANAHTAR="degeri_buraya" satırını ekle, kaydet.

# 2. Terminali tazele
source ~/.bashrc

# 3. Doğrula
echo $YENI_ANAHTAR
```

Python'da kullanmak için:

```python
yeni_deger = os.getenv("YENI_ANAHTAR")
```

---

## 🛑 7. Güvenlik Kuralları (Kritik)

Bu kuralları bir kez okumak değil, alışkanlık haline getirmek gerekir.

- **`.gitignore`'a ekle:** `apikeys.sh` dosyasını mutlaka `.gitignore`'a ekle.
  ```bash
  echo "apikeys.sh" >> .gitignore
  ```
- **GitHub'a asla yükleme:** Bu dosya hiçbir zaman halka açık bir platforma gitmemelidir.
- **İzin kısıtla:** `chmod 600 ~/apikeys.sh` ile başkalarının okuyamamasını sağla.
- **Anahtarı rotate et:** Bir anahtarın sızdığından şüpheleniyorsan, hemen API sağlayıcısından yeni bir anahtar üret ve eskisini iptal et.

> **🔥 Altın Kural:** "Kod kilit, anahtar sensin."

---

## 📌 Hızlı Komut Referansı

| Amaç | Komut |
|---|---|
| Anahtar dosyasını düzenle | `nano ~/apikeys.sh` |
| Terminal ayarlarını düzenle | `nano ~/.bashrc` |
| Değişiklikleri uygula | `source ~/.bashrc` |
| Anahtarı test et | `echo $MY_PROJECT_KEY` |
| Dosya iznini kısıtla | `chmod 600 ~/apikeys.sh` |
| Sanal ortamı aktif et | `source ~/de_venv/bin/activate` |

---

*Bu doküman, iki ayrı seans notunun birleştirilmesi ve genişletilmesiyle oluşturulmuştur. Proje SHKE — Brave Perspectives Data Engineering Altyapısı.*
