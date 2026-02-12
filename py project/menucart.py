#working with dictonary


menu = {"pizza" : 200,
        "fries" : 100,
        "burger": 90,
        "eggpuffs" : 20,
        "roll": 25,
        "water": 20,
        "soda": 20,
        "popcorn": 100}

cart = []

total = 0
print("MENU")

for key, value in menu.items():
    print(f"{key:10} : Rs {value:.2f}")

print()

while True: 
    food = input("Enter the items you need (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()


print(f"Your total amount for the selected items is Rs {total}")
        


