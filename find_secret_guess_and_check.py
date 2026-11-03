from secret_data import secret_year

guesses = 0
found_year = None

# 0'dan 2026'ya kadar tek tek dener
for guess in range(2027):
    guesses += 1
    if guess == secret_year:
        found_year = guess
        break

print(f"Guess and Check tamamlandi!")
print(f"Bulunan yil: {found_year}")
print(f"Yapilan tahmin sayisi: {guesses}")