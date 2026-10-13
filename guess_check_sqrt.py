given_number = int(input("Enter an integer to find its square root: "))

# c şıkkı: Negatif sayı kontrolü
if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    guess_number = 1
    # a şıkkı: 1'den başlayıp tahminin karesi sayıya ulaşana veya aşana kadar artırma
    while guess_number ** 2 < given_number:
        guess_number += 1
    
    # b şıkkı: Tam kare olup olmadığını kontrol etme
    if guess_number ** 2 == given_number:
        print(f"The square root of {given_number} is {guess_number}")
    else:
        print(f"{given_number} is not a perfect square.")