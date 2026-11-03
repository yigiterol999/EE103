def binary_convertor(num):
    if num == 0:
        return "0"
    
    binary_str = ""
    n = num
    
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str  # Kalanlar tersten dizilir
        n = n // 2
        
    return binary_str


if __name__ == "__main__":
    # Test (PDF'teki 13 örneği: çıktı '1101' olmalı)
    test_val = 13
    print(f"{test_val} sayisinin binary karsiligi: {binary_convertor(test_val)}")
    