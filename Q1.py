std_num = int(input("Enter your student number: "))
print(f"Hello, my student number is {std_num}!")

name_lower = 'name'
print(name_lower.upper())
print(name_lower[::-1])

this_year = str(2026)
first_two = float(this_year[:2])
last_two = float(this_year[2:])

mysum = first_two + last_two
print(f"{mysum:.2f}")

if mysum == 46:
    print("Correct")
else:
    print("Wrong")