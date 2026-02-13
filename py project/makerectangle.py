rows = int(input("Enter the number of rows: "))
coloums = int(input("Enter the number of coloums: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for x in range(coloums):
        print(symbol, end="")
    
    print()