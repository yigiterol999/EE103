f = 0.375
binary_frac = ""

while f > 0:
    f = f * 2
    int_part = int(f)
    binary_frac += str(int_part)
    f = f - int_part

print(f"0.{binary_frac}")