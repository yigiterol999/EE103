# 1) Değişken tanımları
x = 0.1
y = 0.2

# 2) Toplam
result = x + y

# 3) Doğrudan eşitlik kontrolü (Floating point hatasından ötürü False verir)
print("result == 0.3:", result == 0.3)

# 4) Epsilon (tolerans) ile yakınlık kontrolü (True verir)
epsilon = 1e-4
is_close = (0.3 - epsilon <= result <= 0.3 + epsilon)
print("Yeterince yakin mi?:", is_close)
