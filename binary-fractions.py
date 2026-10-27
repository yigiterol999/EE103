num = float(input("Enter a fraction number (e.g. 13.375): "))

# Tam kısmı ayırıp binary'e çevirme
int_part = int(num)
frac_part = num - int_part

if int_part == 0:
    int_binary = "0"
else:
    int_binary = ""
    temp_int = int_part
    while temp_int > 0:
        int_binary = str(temp_int % 2) + int_binary
        temp_int = temp_int // 2

# Kesirli kısmı 2 ile çarparak çevirme
frac_binary = ""
temp_frac = frac_part
while temp_frac > 0:
    temp_frac *= 2
    bit = int(temp_frac)
    frac_binary += str(bit)
    temp_frac -= bit

if frac_binary == "":
    frac_binary = "0"

print("Binary representation:", f"{int_binary}.{frac_binary}")