weight = float(input("enter weight"))
unit = input("Is the unit of ur wt in kg or pounds?")

if unit == 'K':
    weight = weight * 2.205
    unit = "LBS"
    print(f"weight is {round(weight,2)} {unit}")
elif unit == "L" :
    weight /= 2.205
    unit  = "Kg"
    print(f"weight is {round(weight,2)} {unit}")
else :
    print(f"{unit} invalid")

