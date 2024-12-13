operator = input("enter + - * /")
num1 = float(input("enter 1st num"))
num2 = float(input("enter 2nd num"))


if operator == '+' :
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '*':
    print(num1*num2)
else :
    print(num1/num2)

