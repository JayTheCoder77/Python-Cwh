#keyword args

def hello(greeting , title , first , last):
    print(f"{greeting} {title} {first} {last}")

hello("Mr." , last ="Spongebob", first ="Squarepants",title = "Hello")

postional args are before keyword agr and default args

for x in range(1,11):
    print(x , end = " ")

print("1","2","3",sep = "-")
print("END =  IS A KEYWORD ARG")

def get_phone(country,area,first,last):
    return f"+{country}--{area}--{first}--{last}"

phone_num = get_phone(last = "7890",first = "123",area = "410",country = "1")
print(phone_num)