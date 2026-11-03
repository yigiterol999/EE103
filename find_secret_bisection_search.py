from secret_data import secret_year

num_guesses = 0
low = 0
high = 2026
guess = (low + high) // 2

while guess != secret_year:
    num_guesses += 1
    if guess < secret_year:
        low = guess + 1
    else:
        high = guess - 1
    
    guess = (low + high) // 2

# Son doğru eşleşme adımı
num_guesses += 1

print(f"Bisection Search tamamlandi!")
print(f"Bulunan yil: {guess}")
print(f"Yapilan tahmin sayisi: {num_guesses}")