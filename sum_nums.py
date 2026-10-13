n = int(input("Enter a number: "))

# Döngü ile toplam hesaplama
running_sum = 0
for i in range(1, n + 1):
    running_sum += i

# Gauss formülü ile doğrudan hesaplama
sum_gauss = n * (n + 1) // 2

# Karşılaştırma ve kontrol
if running_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")