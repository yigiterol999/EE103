num = int(input("Enter an integer to find its cube root: "))

# Sayının işaretini saklayıp pozitif değeriyle arama yapıyoruz
is_negative = num < 0
target = abs(num)

guess = 0
while guess ** 3 < target:
    guess += 1

if guess ** 3 == target:
    # Sayı negatifse küpkökü de negatiftir
    if is_negative:
        guess = -guess
    print(f"The cube root of {num} is {guess}")
else:
    print(f"{num} is not a perfect cube.")