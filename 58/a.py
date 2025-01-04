# exception handling in python
# try -> except -> finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("ENTER NUMBERS ONLY")
except Exception:
    print("Something went wrong")
finally:
    print("do some cleanup")