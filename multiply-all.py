# Kullanıcıdan başlangıç ve bitiş değerlerini alma
start = int(input("Start number: "))
end = int(input("End number: "))

# Multiply-all-1: for döngüsü ile hesaplama
result_for = 1
for num in range(start, end + 1):
    result_for *= num

print("Result (for loop):", result_for)

# Multiply-all-2: while döngüsü ile hesaplama
result_while = 1
current = start
while current <= end:
    result_while *= current
    current += 1

print("Result (while loop):", result_while)

# Sanity Check: Sonuçları karşılaştırma
if result_for == result_while:
    print("results are same")
else:
    print("results are different")

    