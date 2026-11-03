# 1) Kullanıcıdan yıl girdisi alma ve int'e çevirme
year_input = input("What year is this? ")
year = int(year_input)

# 2) Rakamları tek tek çıkarıp toplayan for döngüsü
digit_sum = 0
for ch in year_input:
    digit_sum += int(ch)

# 3) Rakam toplamını basamak sayısına bölme
average = digit_sum / len(year_input)

print(f"Rakamlar toplami: {digit_sum}")
print(f"Ortalama: {average}")