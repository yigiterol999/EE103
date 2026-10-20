target = 0.1
f = target
binary_frac = ""
approx_result = 0.0
power = 1

while abs(approx_result - target) >= 0.00001:
    f = f * 2
    int_part = int(f)
    binary_frac += str(int_part)
    approx_result += int_part * (2 ** -power)
    f = f - int_part
    power += 1

print(f"0.{binary_frac}")