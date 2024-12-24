# args and **kwargs
# arbitrary args

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#         print(arg)
#     return f"total : {total}"
    
# print(add(10,9,2,3))

# def display_name(*args):
#     for arg in args:
#         print(arg,end = " ")

# display_name("Dr","Spongebob" , "III" , "Squarepants")

# def address(**kwargs):
#     print(type(kwargs))
#     for value in kwargs.values():
#         print(value)
#     for key in kwargs.keys():
#         print(key)

# address(street = "fake af street",city = "mumbai",state="maharastra",zip="40004",)

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end = " ")
    for value in kwargs.values():
        print(value,end = " ")
    print(f"{kwargs.get('street')} {kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr","Spongebob" , "III" , "Squarepants",street = "fake af street",city = "mumbai",state="maharastra",zip="40004",)

#args then kwargs wont work the other way round