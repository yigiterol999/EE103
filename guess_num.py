from secret_number import secretNum

attempts = 0

while True:
    guess = int(input("Guess the secret number: "))
    attempts += 1

    if guess < secretNum:
        print("Too low")
    elif guess > secretNum:
        print("Too high")
    else:
        print("Same as the secret")
        break
    if(attempts == 5):
        break

if attempts == 5 and guess != secretNum:
    while True:
        print("Oh! Noooooo...")