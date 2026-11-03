from secret_data import secret_number

epsilon = 0.01
low = 0.0
high = max(1.0, float(secret_number))
guess = (low + high) / 2.0
num_guesses = 0

while abs(guess**2 - secret_number) >= epsilon:
    if guess**2 < secret_number:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    num_guesses += 1

print("--- Bisection Search Metodu ---")
print(f"Sayi: {secret_number}")
print(f"Hesaplanan Karekok: {guess:.4f}")
print(f"Tahmin Sayisi: {num_guesses}")