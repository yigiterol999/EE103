from secret_data import secret_number

epsilon = 0.01
step = 0.1
guess = 0.0
num_guesses = 0

while abs(guess**2 - secret_number) >= epsilon and guess**2 <= secret_number:
    guess += step
    num_guesses += 1

print("--- Approximation Metodu ---")
print(f"Sayi: {secret_number}")
print(f"Hesaplanan Karekok: {guess:.4f}")
print(f"Tahmin Sayisi: {num_guesses}")