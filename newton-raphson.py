from secret_data import secret_number

epsilon = 0.01
guess = secret_number / 2.0
num_guesses = 0

while abs(guess * guess - secret_number) >= epsilon:
    # guess = guess - (guess^2 - secret_number) / (2 * guess)
    guess = guess - (guess**2 - secret_number) / (2 * guess)
    num_guesses += 1

print("--- Newton-Raphson Metodu ---")
print(f"Sayi: {secret_number}")
print(f"Hesaplanan Karekok: {guess}")
print(f"Tahmin Sayisi: {num_guesses}")