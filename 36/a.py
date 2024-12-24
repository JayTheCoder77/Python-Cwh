membership operators
in and not in

word = "Apple"

letter = input("guess letter in secret word")

if letter in word :
    print("found")
else:
    print("not found")

if letter not in word :
    print("not found")
else:
    print("found")

students = {"spongebob","patrick","kermit"}

student = input("enter student name")

if student in students:
    print("present")
else:
    print("absent")

grades = {
    "Sandy":"A",
    "SPONGEBOB":"C",
    "PATRICK":"D"
}

student = input("enter student name")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")


email = "jay@gmailcom"

if "@" in email and "." in email:
    print("valid")
else:
    print("not valid")