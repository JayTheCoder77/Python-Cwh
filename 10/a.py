unit = input("is the temp in celsius or farenheit")
temp = float(input("enter temperature"))

if unit == 'c':
    temp = round(temp * (9/5) + 32,2)
    print(f"temp in farenheit is {temp} F")
elif unit == 'f':
    temp = round(((temp - 32) * (5/9)),2)
    print(f"temp in celsius is {temp} C")
else :
    print(f"{unit} is invalid")