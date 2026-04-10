Terminaldeki bu profesyonel dönüşümü, işlerini otomatize edecek 
ve bizi bir "Power User" yapacak özel Bash script teknikleriasagidadir. 

Özellikle Veri Bilimi ve MLOps süreçlerinde işine yarayacak, 
"bilenle bilmeyeni ayıran" o özel komutları ve durumları bizim için bir rehber haline getirdim.

---

# Bash Scripting: Özel Teknikleri

Bu rehber, sıradan komutların ötesinde, hata yönetimini güçlendiren ve terminalde hız kazandıran ileri seviye Bash tekniklerini içerir.

## 1. Altın Kural: "Safety First" (Hata Yönetimi)
Script yazarken en başına mutlaka şu "sihirli" satırı eklemelisin. Bu, scriptin hata yaptığında sessizce devam etmesini engeller.

```bash
#!/bin/bash
set -euo pipefail
```
* **`-e`:** Bir komut hata verirse scripti anında durdurur.
* **`-u`:** Tanımlanmamış bir değişken kullanırsan scripti durdurur.
* **`-o pipefail`:** Boru hattındaki (`|`) bir komut hata verirse, tüm hattı hatalı sayar.

---

## 2. Akıllı Değişken Durumları (Parameter Expansion)
Değişkenlerle çalışırken sadece `$` kullanmak yerine şu "kıvrak" yöntemleri kullanabilirsin:

* **Varsayılan Değer Atama:** Eğer `USER_NAME` boşsa "Guest" değerini kullan.
    ```bash
    echo "Merhaba ${USER_NAME:-Guest}"
    ```
* **Dosya Uzantısını Atma:** `dosya.csv` içinden sadece `dosya` kısmını al.
    ```bash
    FILENAME="data.csv"
    echo ${FILENAME%.*}  # Çıktı: data
    ```
* **Dosya Adını Alma (Path'i Atma):** Tam yoldan sadece dosya ismini çek.
    ```bash
    FULLPATH="/mnt/c/DE_Projects/data.csv"
    echo ${FULLPATH##*/}  # Çıktı: data.csv
    ```

---

## 3. "Dry Run" Modu (Deneme Sürüşü)
Scriptin gerçekten bir şeyleri silmeden veya değiştirmeden önce ne yapacağını görmek için harika bir taktiktir.

```bash
DRY_RUN=true

function execute_task() {
    if [ "$DRY_RUN" = true ]; then
        echo "[DRY-RUN] Şu komut çalıştırılacaktı: $1"
    else
        eval $1
    fi
}

execute_task "rm -rf old_data_folder"
```

---

## 4. Aliases (Hız Kazandıran Kısayollar)
`.zshrc` dosyana ekleyebileceğin, günlük hayatı kolaylaştıran özel kısayollar:

| Alias | Komut | Açıklama |
| :--- | :--- | :--- |
| `..` | `cd ..` | Bir üst dizine çık |
| `...` | `cd ../..` | İki üst dizine çık |
| `myip` | `curl ifconfig.me` | Dış IP adresini öğren |
| `ports` | `netstat -tulanp` | Açık portları gör |
| `size` | `du -sh *` | Klasörlerin boyutunu gör |

---

## 5. Çıktıları Hem Ekrana Hem Dosyaya Yazma (`tee`)
Veri projelerinde log tutmak hayat kurtarır.
```bash
python train_model.py | tee training.log
```
*Bu komut sayesinde çıktıyı hem terminalden canlı izlersin hem de aynı anda `training.log` dosyasına kaydedersin.*

---

## 6. Geçici Dosya Yönetimi (`mktemp`)
Scriptlerinde geçici veriler tutman gerekiyorsa, çöp bırakmamak için bunu kullan:

```bash
TEMP_FILE=$(mktemp)
echo "Geçici veri burada" > "$TEMP_FILE"

# İşlem bitince silmek için "trap" kullan (Sihirli komuttur!)
trap "rm -f $TEMP_FILE" EXIT
```

---

## 7. Şık Çıktılar İçin Renk Kodları
Terminalde uyarıları veya başarı mesajlarını "Agnoster" tadında renklendirebilirsin:

```bash
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color (Rengi Sıfırla)

echo -e "${GREEN}[OK]${NC} Veri seti başarıyla yüklendi."
echo -e "${RED}[HATA]${NC} API bağlantısı kurulamadı!"
```

---

### MLOps İçin Bir İpucu:
Bash scriptlerini genelde Python scriptlerini tetiklemek (`orchestration`) için kullanırız. 
Örneğin; önce sanal ortamı açan, sonra veriyi çeken, 
en son modeli eğiten tek bir `run_all.sh` dosyası, yaratacagin yeni bir proje icindeki en büyük yardımcın olur.
 (mesela benim  **Project INDIEGRID** )

