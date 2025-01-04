# decorators in python

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("sprinkles  🍦")
        func(*args,**kwargs)
    return wrapper

# if we remove wrapper function it will call the add sprinkles function so wrapper is necessary

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("added fudge 🍦")
        func(*args,**kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_icecream(flavor):
    print(f"{flavor} icecream 🍦")

get_icecream("Mango")