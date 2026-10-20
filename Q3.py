s = "abcabc"
seen = ""

for char in s:
    if char not in seen:
        seen += char

print(len(seen))