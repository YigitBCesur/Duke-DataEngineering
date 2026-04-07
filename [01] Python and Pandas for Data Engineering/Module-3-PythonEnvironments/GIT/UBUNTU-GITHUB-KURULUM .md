**DUKE DATA ENGINEERING: UBUNTU & GITHUB KURULUM REHBERİ**

Bu rehber, **Yiğit Brave Cesur**'un Duke University Data Engineering
sertifika programı kapsamındaki yerel çalışma ortamı ile bulut (GitHub)
arasındaki köprüyü kurmak için hazırlanmıştır.

**1. SAHNE ARKASI: KİMLİK VE GÜVENLİK AYARLARI**

Herhangi bir kod göndermeden önce, Git'e \"bu kargolar bana ait\"
demeniz gerekir.

-   **İsim Tanımlama:** git config \--global user.name \"Yigit Brave
    Cesur\"

-   **E-posta Tanımlama:** git config \--global user.email
    \"email@adresiniz.com\"

-   **Kimlik Saklama:** Şifre/Token'ı her seferinde sormaması için: git
    config \--global credential.helper store

**2. İLK BAĞLANTI: GITHUB REPO\'SUNU YERELE ALMA (CLONE)**

Buluttaki bir projeyi bilgisayarınıza ilk kez indirmek için kullanılır.

-   **Komut:** git clone
    https://github.com/YigitBCesur/Duke-DataEngineering.git

-   **Anlamı:** Belirtilen URL\'deki tüm proje geçmişini ve dosyaları
    bilgisayarınızdaki bir klasöre kopyalar.

**3. İZOLASYON: PYTHON SANAL ORTAMI (VENV)**

Farklı projelerin kütüphanelerinin birbirine karışmaması için
oluşturulan \"korunaklı kutu\"dur.

-   **Gerekli Paketi Yükleme:** sudo apt install python3.12-venv

-   **Sanal Ortamı Oluşturma:** python3 -m venv .venv

-   **Aktif Etme:** source .venv/bin/activate

    -   *Kontrol:* Terminalin başında **(.venv)** yazısını görmelisiniz.

**4. TERMİNAL NAVİGASYONU VE DOSYA YÖNETİMİ**

-   **Klasör Oluşturma:** mkdir Klasor_Ismi

-   **Klasöre Girme:** cd Klasor_Ismi

-   **Dosya Düzenleme:** nano notes.py

    -   *(Kaydet: Ctrl+O \> Enter \| Çık: Ctrl+X)*

-   **İçerik Listeleme:** ls

-   **Üst Klasöre Çıkış:** cd ..

**5. KARGO SÜRECİ: GIT ADD, COMMIT, PUSH**

Bilgisayarınızdaki bir değişikliği GitHub'a göndermenin 3 zorunlu adımı
vardır:

1.  **git add . (Paketleme):** Bulunduğunuz klasördeki tüm yeni veya
    değişmiş dosyaları kargo kolisine koyar.

2.  **git commit -m \"Mesaj\" (Mühürleme):** Koliyi mühürler ve üzerine
    ne yaptığınızı anlatan bir etiket yapıştırır.

3.  **git push origin main (Gönderim):** Mühürlü koliyi GitHub bulutuna
    fırlatır.

    -   *Not:* Şifre sorduğunda GitHub\'dan aldığınız **Personal Access
        Token (PAT)** girilmelidir.

**6. TEMİZLİK VE HATA GİDERME**

-   **Dosya Silme:** git rm dosya_adi.py (Dosyayı hem bilgisayardan hem
    Git takibinden siler).

-   **Durum Kontrolü:** git status (Hangi dosyaların kargolanmaya hazır
    olduğunu gösterir).

**Önemli Hatırlatılışı:** Veri mühendisliğinde her zaman önce **cd** ile
doğru klasöre gidin, sonra **source .venv/bin/activate** ile kutunuzu
açın ve çalışmaya öyle başlayın.

**7. DOSYA İÇİNE YAZMA VE DÜZENLEME (NANO)**

Bir dosyanın içeriğini terminalden değiştirmek için kullanılan en hızlı
yöntemdir.

-   **Dosyayı Aç:** nano notes.py

-   **Yazma:** Açılan siyah ekrana kodlarını veya notlarını direkt
    klavyeden yazabilirsin.

-   **Kaydetme (Save):** Ctrl + O tuşlarına bas, ardından altta çıkan
    dosya ismini onaylamak için **Enter**\'a bas.

-   **Çıkış (Exit):** Ctrl + X tuşuna basarak tekrar komut satırına dön.

**8. YAZILAN KODU ÇALIŞTIRMA (TEST)**

Yazdığın Python kodunun hata verip vermediğini kontrol etmek için:

-   **Komut:** python3 notes.py

-   **Not:** Eğer bir hata alırsan, nano ile tekrar içine girip yazım
    hatası olup olmadığını kontrol etmelisin.

**9. SON ADIM: GITHUB\'I GÜNCELLEME**

Dosyanın içini doldurup kaydettikten sonra, bu değişikliği GitHub\'daki
depona yansıtmak için \"Kargo Üçlüsü\"nü çalıştır:

1.  git add .

2.  git commit -m \"notes.py içeriği güncellendi\"

3.  git push origin main

**Brave İpucu:** Eğer git push yaptıktan sonra terminalde hata almazsan
ve \"Everything up-to-date\" veya başarılı bir gönderim mesajı görürsen,
tarayıcından GitHub sayfasına girip notes.py dosyasına tıkladığında
yazdığın kodların orada olduğunu göreceksin.

  ------------------------------------------------------------------------
  **Komut**      **Anlamı**       **Kullanım Amacı**
  -------------- ---------------- ----------------------------------------
  **pwd**        Print Working    \"Neredeyim?\" sorusuna cevap verir.
                 Directory        Bulunduğun tam yolu gösterir.

  **ls**         List             Klasörün içindeki dosyaları listeler.

  **ls -la**     List All         Gizli dosyalar (örn: .git, .venv) dahil
                                  her şeyi detaylı gösterir.

  **cd           Change Directory Belirtilen klasörün içine girer.
  \<klasör\>**                    

  **cd ..**      Parent Directory **Bir üst klasöre** geri döner.

  **cd \~**      Home             Seni doğrudan ana (Ev) dizinine götürür.

  **cd -**       Previous         En son hangi klasördeysen oraya geri
                                  zıplar (Geri butonu gibi).

  **mkdir        Make Directory   Yeni bir klasör oluşturur.
  \<ad\>**                        

  **touch        Touch            Yeni ve boş bir dosya oluşturur (örn:
  \<ad\>**                        touch notes.py).

  **rm           Remove           Dosyayı siler. (**Dikkat:** Çöp kutusuna
  \<dosya\>**                     gitmez, kalıcı siler!)

  **rm -rf       Recursive Force  Bir klasörü ve içindeki her şeyi zorla
  \<klasör\>**                    siler.

  **mv \<eski\>  Move / Rename    Dosyayı taşır veya ismini değiştirir.
  \<yeni\>**                      

  **clear**      Clear            Terminal ekranını temizler (ya da Ctrl +
                                  L).
  ------------------------------------------------------------------------

**⌨️ YAZIM HIZLANDIRAN \"BRAVE\" İPUÇLARI**

Terminalde kod yazarken bu kısayollar sana ciddi zaman kazandırır:

-   **TAB Tuşu (En Önemlisi):** Bir klasör veya dosya isminin ilk birkaç
    harfini yazıp TABa basarsan terminal ismi otomatik tamamlar. Hata
    yapmanı önler.

-   **Yukarı/Aşağı Ok Tuşları:** Daha önce yazdığın komutlar arasında
    gezinmeni sağlar. Aynı şeyi tekrar yazmak yerine oklarla bulup
    Entera bas.

-   **Ctrl + C:** Çalışan bir işlemi (veya yanlış yazdığın bir satırı)
    anında iptal eder.

-   **history:** Yazdığın tüm eski komutları listeler.

**📝 NANO EDİTÖR KISAYOLLARI (KOD YAZARKEN)**

nano notes.py ile dosyanın içine girdiğinde:

-   **Ctrl + O**: Dosyayı kaydeder (Write Out).

-   **Enter**: Kayıt ismini onaylar.

-   **Ctrl + X**: Editörden çıkar.

-   **Ctrl + K**: Satırı komple siler (Kes).

-   **Ctrl + U**: Silinen satırı geri yapıştır.
