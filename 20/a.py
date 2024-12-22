# nested loops

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")

for r in range(rows):
    for c in range(cols):
        print(symbol,end=" ")
    print() 