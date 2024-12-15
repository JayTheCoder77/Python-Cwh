principle = 0
rate = 0
time = 0

while principle <= 0 :
    principle = float(input("enter prinicple amt :"))
    if principle <= 0 :
        print("principle cant be less than or equal to zero")
print(principle)

while rate <= 0 :
    rate = float(input("enter rate amt :"))
    if rate <= 0 :
        print("rate cant be less than or equal to zero")
print(rate)

while time <= 0 :
    time = int(input("enter time amt :"))
    if time <= 0 :
        print("time cant be less than or equal to zero")
print(time)


compound = principle * pow((1 + rate / 100) , time)
print(f"{principle} after {time} years with rate {rate}% is ${compound}")