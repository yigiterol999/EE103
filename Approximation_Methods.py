x = float(input("Enter number to find square root of: "))
epsilon = 0.01
increment = 0.0001
guess = 0.0
num_guesses = 0

# guess**2 <= x koşulu, aşırı büyüyüp sonsuz döngüye girmesini (overshoot) engeller
while abs(guess**2 - x) >= epsilon and (guess**2 <= x):
    guess += increment
    num_guesses += 1
    
    if num_guesses % 100000 == 0:
        print("Current guess =", guess)

print("Number of guesses:", num_guesses)
if abs(guess**2 - x) < epsilon:
    print(f"Approximate square root of {x} is {guess:.4f}")
else:
    print(f"Failed to find square root near {x}")