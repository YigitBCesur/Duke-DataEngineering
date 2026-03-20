# Duke Data Engineering - Course 1 - Sequences

# 1. LIST (Değiştirilebilir / Mutable)
# Veri ekleme, çıkarma ve güncelleme yapılabilir.
my_list = ["Python", "Pandas", "Linux"]
my_list.append("SQL") 
print(f"Liste: {my_list}")

# 2. TUPLE (Değiştirilemez / Immutable)
# Tanımlandıktan sonra üzerinde değişiklik yapılamaz, daha hızlıdır.
my_tuple = ("Duke", "Data", "Engineering")
print(f"Tuple: {my_tuple}")

# 3. SET (Benzersiz / Unique)
# Tekrar eden elemanları otomatik temizler.
my_set = {1, 2, 2, 3, 3, 3} 
print(f"Set (Benzersiz): {my_set}")

# 4. DICTIONARY (Anahtar-Değer / Key-Value)
# Verileri etiketlerle saklar.
my_dict = {"Course": "Duke-DE", "Topic": "Sequences"}
print(f"Sözlük: {my_dict['Course']}")
