.zshrc icin Eklentiler ve kurulum adımlarınin kaynaklarını (GitHub linkleri vb.) not almak, ileride başka bir sisteme geçerken veya mevcut sistemi yeniden kurarken sana muazzam bir hız kazandırır. Bu, veri yönetiminde "reproducibility" (tekrarlanabilirlik) ilkesiyle de örtüşür.

---

# Zsh ve Oh My Zsh: Akıllı Terminal Kurulum Rehberi

Bu doküman, ham bir Linux terminalini, hata önleyici ve hızlandırıcı bir veri işleme merkezine dönüştürme adımlarını içerir.

## Bölüm 1: Altyapı ve Hazırlık

### 0. Adım: Sistem Güncelleme
Herhangi bir kuruluma başlamadan önce sistem paket listelerini güncellemek, uyumluluk sorunlarını önler.
* **Komut:** `sudo apt update && sudo apt upgrade -y`
* **Neden?** En güncel paket sürümlerine erişmek ve güvenlik yamalarını uygulamak için.

### 1. Adım: Gerekli Araçların Kurulumu
Sisteme ana motoru ve yardımcı indirme araçlarını yüklüyoruz.
* **Komut:** `sudo apt install zsh git curl -y`
* **Neden?** Zsh ana kabuğumuzdur; git eklentileri çekmek, curl ise kurulum dosyalarını indirmek içindir.

---

## Bölüm 2: Oh My Zsh ve Görsel Yapılandırma

### 2. Adım: Oh My Zsh Kurulumu
Zsh'i yönetilebilir bir çerçeveye oturtuyoruz.
* **Komut:** `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

### 3. Adım: Tema Ayarı (Agnoster)
Terminalin dizin yapısını ve durumunu net bir şekilde görmek için temayı değiştiriyoruz.
* **İşlem:** `nano ~/.zshrc` komutuyla dosyayı aç ve `ZSH_THEME="agnoster"` satırını bul/düzenle.
* **Fayda:** Mavi oklar ve okunaklı dizin yolları sağlar.

---

## Bölüm 3: Akıllı Eklentiler (Smart Plugins)

Aşağıdaki iki eklentiyi manuel olarak indiriyoruz:

### 4. Adım: zsh-autosuggestions (Otomatik Öneri)
Geçmiş komutlarınıza dayanarak gri renkte "fısıltı" şeklinde öneriler sunar.
* **Link:** `https://github.com/zsh-users/zsh-autosuggestions`
* **Kurulum:** `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`

### 5. Adım: zsh-syntax-highlighting (Sözdizimi Vurgulama)
Yazdığınız komutun doğruluğunu gerçek zamanlı olarak renklerle belirtir.
* **Link:** `https://github.com/zsh-users/zsh-syntax-highlighting`
* **Kurulum:** `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

---

## Bölüm 4: Konfigürasyon ve Otomasyon

### 6. Adım: .zshrc Dosyasını Yapılandırma
Ayarların aktif olması için dosya hiyerarşisi kritik önemdedir. `nano ~/.zshrc` içinde şu sıralamayı takip edin:

1. **ZSH Yolu:** `export ZSH="$HOME/.oh-my-zsh"`
2. **Tema:** `ZSH_THEME="agnoster"`
3. **Eklenti Listesi:** `plugins=(git z docker python extract zsh-autosuggestions zsh-syntax-highlighting)`
4. **Oh My Zsh Motoru:** `source $ZSH/oh-my-zsh.sh`
5. **Kişisel Otomasyonlar (Dosyanın sonuna):**
    * API anahtarları yükleme: `source ~/apikeys.sh`
    * Proje dizinine gitme: `cd /mnt/c/DE_Projects`
    * Sanal ortam aktivasyonu: `source ~/de_venv/bin/activate`

---

## Bölüm 5: Uygulama ve Doğrulama

### 7. Adım: Ayarları Devreye Alma
Terminali kapatıp açmadan ayarları aktif etmek için:
* **Komut:** `source ~/.zshrc` veya `exec zsh`

### Başarı Kriterleri:
* Mavi oklar görünüyorsa tema çalışıyordur.
* Yazılan komutlar renkliyse (doğruysa yeşil, yanlışsa kırmızı) highlighting çalışıyordur.
* Komutun devamında silik gri öneriler varsa autosuggestions aktiftir.

