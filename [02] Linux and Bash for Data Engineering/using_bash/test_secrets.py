import os

# Sistemin hafızasına (Environment) soruyoruz:
# "Hey Bash, sende MY_PROJECT_KEY adında bir veri var mı?"
secret_key = os.getenv("MY_PROJECT_KEY")

print("-" * 30)
if secret_key:
    print(f"BAŞARILI: Python anahtarı buldu!")
    print(f"Anahtar Değeri: {secret_key}")
else:
    print("HATA: Python anahtarı bulamadı. Sourcing yapmamış olabilirsin.")
print("-" * 30)
