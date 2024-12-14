#string indexing 

# accesing string elements

credit_number = "1234-5678-9012-9145"
# print(credit_number[:4]) #this and line below are same
# print(credit_number[0:4])

# print(credit_number[0:4:2]) start : end : step

# print(credit_number[-3])
# print(credit_number[::3])

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1]
print(credit_number)