num = int(input("Enter an integer to convert to binary: "))

if num == 0:
    binary_str = "0"
else:
    binary_str = ""
    temp = abs(num)
    while temp > 0:
        remainder = temp % 2
        binary_str = str(remainder) + binary_str
        temp = temp // 2
    if num < 0:
        binary_str = "-" + binary_str

print("Binary representation:", binary_str)