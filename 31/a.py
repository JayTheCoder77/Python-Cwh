#function


# def happy(n):
#     for i in range(n):
#         print("Happy Birthday to you!")

# num = int(input("years for happy bday"))
# happy(num)

# def display_invoice(username,amt,date):
#     print(f"Hello {username}")
#     print(f"Bill is {amt:.2f} is due {date}")

# display_invoice("Jay",23423.672,"12/12/2020")

# def add(a,b):
#     x = a + b
#     return x
# def div(a,b):
#     x = a / b
#     return x

# z = add(2,3)
# print(div(2,3))
# print(z)

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

name = create_name("jay","skillf")
print(name)