#format specifiers  {value : flags}

price1 = 3232.14159
price2 = -987.65
price3 = 12231.34

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:010}")
print(f"Price 3 is ${price3:>10}")
print(f"Price 3 is ${price3:^10}")
print(f"Price 3 is ${price3:+}")
print(f"Price 3 is ${price3:,}")
print(f"Price 3 is ${price3:+,.2f}")