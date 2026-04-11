ALIAS - Bir komuta veya yola atıfta bulunan kısayol.
# Alias example
alias documents="cd ~/Documents"
documents # Changes to Documents directory


SOURCE - Kaynak : Geçerli kabukta bir komut dosyasını veya dosyayı yükleyin ve çalıştırın.
# Source example
source ~/.bashrc # Reloads bash config

EXPORT - Dışa Aktarma  - Alt süreçler tarafından devralınacak bir ortam değişkeni ayarlayın.
# Export example
export API_KEY="123abc" 
python script.py # script.py can access $API_KEY

Virtual Environment  -  Sanal Ortam  - Kendi paketlerine sahip, izole edilmiş bir Python ortamı.
# Virtual environment
python3 -m venv my_env
source my_env/bin/activate # Activates the environment

Plug-in - Eklenti  - İşlevselliği genişleten bir ek bileşen.
# Plugin 
source ~/.zshrc # Reloads zsh config with plugins



