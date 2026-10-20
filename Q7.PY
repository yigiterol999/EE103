num = 13

if num == 0:
    binary_str = "0"
else:
    remainders = ""
    temp = num
    while temp > 0:
        rem = temp % 2
        remainders += str(rem)
        temp = temp // 2
    binary_str = remainders[::-1]

print(binary_str)