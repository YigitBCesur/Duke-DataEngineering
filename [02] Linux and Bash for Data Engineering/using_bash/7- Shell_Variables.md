# ANA TERİMLER

## Shell Variable
A variable that exists only in the shell and stores data to be used in scripts or other processes.
*Yalnızca kabukta var olan ve komut dosyalarında veya diğer işlemlerde kullanılacak verileri depolayan bir değişken.*

```bash
# Shell Variable
food="apple"
echo $food
```

---

## Export
A command that allows a shell variable to be accessed by child shells/processes.
*Bir kabuk değişkenine alt kabuklar/işlemler tarafından erişilmesini sağlayan bir komut.*

```bash
# Export for child process access
export food="apple"
bash
echo $food
```

---

## Source
Runs a script in the current shell so any variables/aliases are available in the current environment.
*Geçerli kabukta bir komut dosyası çalıştırır, böylece tüm değişkenler/takma adlar geçerli ortamda kullanılabilir hale gelir.*

```bash
# Source to load current environment
source ./script.sh
echo $food
```

---

## Parent/Child Processes
Parent processes launch child processes and can pass variables via export.
*Ebeveyn süreçler çocuk süreçleri başlatır ve dışa aktarma yoluyla değişkenler aktarabilir.*

```bash
# Parent/Child Processes
export food="apple"
bash
echo "In child - $food"
```

### Python Example

```python
# Access shell variable in Python
import os
print(os.environ['food'])
```

---

# ÖNEMLİ NOTLAR

## 1. Değişkenler ve Görünmezlik Duvarı

Bilgisayarda bir değişken tanımladığında (örneğin `food="apple"`), bu bilgi o anki terminal penceresinin hafızasına kaydedilir. Ancak Linux'ta katı bir kural vardır: **"Alt süreçler, üst süreçlerin özel bilgilerini göremez."**

### Neden `export` Kullanıyoruz?

Diyelim ki bir terminal açtın (Ana Süreç) ve içine `food="apple"` yazdın. Sonra bu terminalin içinden bir Python kodu veya başka bir script çalıştırdın (Alt Süreç).

- Eğer sadece `food="apple"` dersen → Python bu elmayı **göremez**.
- Eğer `export food="apple"` dersen → o değişkeni "herkese açık" (global) hale getirirsin. Artık o terminalden başlattığın her şey elmayı görebilir.

---

## 2. "Source" vs "Normal Çalıştırma"

Bu ikisi arasındaki fark, bir misafirin senin evine gelip gelmemesi gibidir:

| Yöntem | Açıklama |
|---|---|
| **Normal Çalıştırma** (`bash script.sh`) | Yeni bir oda (yeni bir terminal süreci) kiralanır, script orada çalışır ve işi bitince o oda yıkılır. İçinde tanımlanan tüm değişkenler yok olur. |
| **Source Etme** (`source script.sh`) | Script senin mevcut odanda (mevcut terminalinde) çalışır. Tanımlanan değişkenler komut bittikten sonra bile terminalinde kalmaya devam eder. |

---

## Özet Senaryo

1. Terminale `isim="Yigit"` yazdın → Sadece o terminal biliyor.
2. Yeni bir terminal sekmesi açtın veya bir Python dosyası çalıştırdın → `echo $isim` boş çıkar, çünkü `export` etmedin.
3. `export isim="Yigit"` dersen → o terminalden açacağın her uygulama senin kim olduğunu bilir.

### Kısaca:

| Kavram | Tanım |
|---|---|
| **Shell** | Tercüman |
| **Variable** | Sadece o anki pencerede geçerli not |
| **Export** | Notu, o pencereden açılan her şeyin görebileceği bir duyuru panosuna asmak |
| **Source** | Notu direkt kendi defterine yazdırmak |

---

# WHAT IS SHELL VARIABLES?

Environment Variables (Ortam Değişkenleri) modern yazılım geliştirme dünyasının "gizli kahramanı"dır.

## 1. Güvenlik ve `.gitignore` İlişkisi

API anahtarlarını veya veritabanı şifrelerini kodun içine (hardcoded) yazmak, evin anahtarını kapının üzerinde bırakmak gibidir.

**Çözüm:** Şifreyi `.env` dosyasına yazarsın. Git'e bu dosyayı yüklemezsin (`.gitignore` içinde `.env` satırı olur). Böylece kodun GitHub'da herkes tarafından görülse bile, şifreler sadece senin makinende kalır.

---

## 2. "Tab" Tuşu: En İyi Dostun

Tab tuşu terminalde sadece değişkenleri değil, dosya yollarını ve komutları da tamamlar. Bu sadece hız kazandırmaz, aynı zamanda yazım hatasını (typo) engeller. Eğer Tab'a bastığında tamamlanmıyorsa:
- Ya o değişken tanımlanmamıştır,
- Ya da bir harfi yanlış yazmışsındır.

Bu en hızlı **hata ayıklama (debug)** yöntemidir.

---

## 3. Otomasyon ve Dizine Özel Değişkenler

Belirli bir dizine geçtiğinde değişkenleri kaynaklama (source) profesyonel hayatta çok yaygındır:

- **A projesi** için Python 3.9 ve bir API anahtarı,
- **B projesi** için Python 3.11 ve farklı bir veritabanı yolu.

Bunu otomatize etmek için `direnv` gibi araçlar kullanılır. Sen o klasöre girdiğin anda sistem otomatik olarak `source .env` çalıştırır. Klasörden çıkınca değişkenler hafızadan silinir.

---

## Küçük Bir Teknik Hatırlatma (Bash vs. Zsh)

Bash veya Zsh (Mac'lerde varsayılan) kullanman fark etmez; değişken mantığı aynıdır.

- **Bash'te:** `export food="apple"`
- **Zsh'te:** `export food="apple"` çalışır, ancak bazı gelişmiş özellikler (array tanımlama gibi) küçük farklılıklar gösterebilir.

### Pratik Örnek: Cümle İçinde Kullanım

```bash
export food="elma"
echo "Benim en sevdiğim meyve $food, çünkü $food sağlıklıdır."
```

`$food` her geçtiği yere `"elma"` değerini koyar. Yarın `"armut"` dersen, tüm cümle tek bir yerden güncellenir.

---

# Zsh (Parent Process) → Bash (Child Process): Kalıtım Süreci

## 1. Ana Kabuk (Zsh + Oh My Zsh)

İlk açılan renkli, süslü yer senin Zsh kabuğun.

- **Neden Renkli?** "Oh My Zsh" eklenti paketi terminalin her satırını özelleştiriyor; hangi klasördesin, hangi Git dalındasın hepsini görselleştiriyor.
- **Ayar Dosyası:** `/home/yigit/.zshrc`

## 2. Alt Kabuk (Bash)

`bash` yazdığında, Zsh'in içinden çıkmadan "Bana bir de Bash tercümanı aç" dedin.

- **Neden Sade?** Bash sistemde "saf" (vanilla) halde duruyor. Zsh için yapılan renkli temalar Bash'i etkilemez.
- **Ayar Dosyası:** `.bashrc`

## Aralarındaki Temel Bağlar

### A. Hiyerarşi (Baba - Evlat İlişkisi)

- Zsh → **"Baba" (Parent)**, Bash → **"Evlat" (Child)**
- `export` ile tanımlanan değişkenler Bash tarafından görülür.
- Sadece `ders="linux"` olarak tanımlanırsa Bash bunu göremez.

### B. Dosya Yolu (Path)

Her iki kabuk da aynı dosyaları görür. `/mnt/c/...` yolundaki dosyalar aynıdır, ama gösterme biçimleri farklıdır.

### C. Geçiş Köprüsü

`[INFO] Success: API keys loaded` satırı bu bağın somut kanıtı. Bash'e geçildiğinde, Bash otomatik olarak `apikeys.sh` dosyasını `source` eder.

> **Özetle:** İlk renkli ekran "Makam Odası" (Zsh), `bash` yazıp girilen yer ise "Çalışma Masası" (Bash). Masaya geçtiğinde odadaki genel kurallar (`export` edilenler) geçerli kalır, ama masanın kendi sadeliği devreye girer.

---

# Kullanım Alanları

Bash kabuğunda çevre değişkenlerinin (environment variables) kullanıldığı yaygın alanlar:

## 1. Hassas Verilerin Gizlenmesi (Secrets Management)

API anahtarları, veri tabanı şifreleri asla kodun içine yazılmaz.

```bash
export DB_PASSWORD="gizli_sifre"
```

Kodunuzu GitHub'da paylaştığınızda şifrelerinizin başkalarının eline geçmesini engeller.

## 2. Uygulama Yapılandırması (Configuration)

```bash
export ENV="production"
export LOG_LEVEL="debug"
```

Kodu hiç değiştirmeden, sadece değişkeni değiştirerek uygulamanın davranışını kontrol edebilirsiniz.

## 3. Otomasyon ve Script Yazımı

```bash
export BACKUP_DIR="/mnt/yedekler"
```

Bir yedekleme scriptinde dosya yolunu merkezi bir yerden yönetebilirsiniz.

## 4. Docker ve Bulut Sistemler

Docker konteynerleri veya Kubernetes çalıştırılırken, gerekli tüm bilgiler `export` yöntemiyle (veya `.env` dosyalarıyla) içeri aktarılır.

## 5. Veri İşleme Pipeline Hatları

Veri mühendisliği süreçlerinde:
- Hangi veri tabanına bağlanılacağı,
- Hangi tarih aralığındaki verinin çekileceği,
- Çıktı dosyasının nereye kaydedileceği

bu değişkenler üzerinden yönetilir.

---

# Python ile Kullanım

Bir **Veri Mühendisi** olarak veri tabanına bağlanma senaryosu:

## Adım 1 — Güvenlik Duvarı Oluşturmak

```bash
export DB_PASS="SüperGizliŞifre123"
```

Bu şifre sadece o anki terminal oturumunda (session) yaşar.

## Adım 2 — Kodun İçinde Kullanma

```python
import os

# Sistemden değişkeni çekiyoruz
sifre = os.getenv('DB_PASS')

print(f"Veri tabanına şu şifre ile bağlanılıyor: {sifre}")
```

Kod **"taşınabilir"** olur. Arkadaşına gönderdiğinde, o kendi terminalinde kendi şifresini `export` eder ve kod yine çalışır.

## Adım 3 — Path Yönetimi

`python` yazdığında bilgisayar programın nerede olduğunu **`$PATH`** değişkeni sayesinde bilir. Tüm çalıştırılabilir dosyaların adres listesi bu değişkende tutulur.

## Adım 4 — Proje Bazlı Ayarlar (Virtual Environments)

`(de_venv)` ibaresi sanal ortamda çalışıldığını gösterir. Bu ortamlar aktive edildiğinde arka planda otomatik olarak bazı çevre değişkenleri set edilir (örneğin `PYTHONPATH`). Bu sayede kütüphaneler birbirine karışmaz.

---

# Neden `.bashrc`?

Linux sistemlerde terminal her açıldığında bu dosyayı baştan sona okur. İçine yazdığın her `export` komutu bilgisayar tarafından "otomatik olarak çalıştırılmış" sayılır. Böylece her seferinde elle tanımlama yapmana gerek kalmaz.

**Hangi dosyayı kullanman gerektiğini öğrenmek için:**

```bash
echo $SHELL
```

| Çıktı | Kullanılacak Dosya |
|---|---|
| `/bin/bash` | `.bashrc` |
| `/bin/zsh` | `.zshrc` |
