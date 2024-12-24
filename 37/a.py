#list comprehension

# doubles = []
# for x in range(1,11):
#     doubles.append(x * 2)
# print(doubles)

#doing this using list comprehension

# doubles = [x * 2 for x in range(1,11)]
# print(doubles)

# triples = [y * 3 for y in range(1,11)]
# print(triples)

# squares = [pow(x,2) for x in range(1,11)]
# print(squares)

# fruits = ["apple" , "banana" , "mango"]

# fruits = [fruit.upper() for fruit in ["apple" , "banana" , "mango"]]
# print(fruits)

# fruit_char = [fruit[0].upper() for fruit in fruits]
# print(fruit_char)

# numbers = [-1,0,2,-8,9,-6]

# positive_nums = [num for num in numbers if num >= 0]
# print(positive_nums)
# negative_nums = [num for num in numbers if num < 0]
# print(negative_nums)
# even_nums = [num for num in numbers if num % 2 == 0]
# print(even_nums)
# odd_nums = [num for num in numbers if num % 2 != 0]
# print(odd_nums)


grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade >=60]
print(passing_grades)