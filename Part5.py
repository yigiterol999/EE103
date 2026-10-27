target = 0.1
tolerance = 0.00001

frac_binary = "0."
temp_frac = target
approx_value = 0.0
power = 0.5

while abs(approx_value - target) >= tolerance:
    temp_frac *= 2
    bit = int(temp_frac)
    frac_binary += str(bit)
    temp_frac -= bit
    
    if bit == 1:
        approx_value += power
    power /= 2

print("Approximated binary for 0.1:", frac_binary)
print("Approximated float value:", approx_value)