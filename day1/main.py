""" 
name = input("What is your name?: ")
age = input("What is your age?: ")
age = int(age) 
age = age + 1   

print(f"Hello {name}, good going")
print("Happy Birthday!!")
print(f"You are {age} years old")
"""
"""
# exercise 1 rectangle area 
 
length = float(input("enter your length: "))
width = float(input("enter your width: "))
area = length * width
print(type(area))
print(f"The area of the rectangle is {area}")

"""
# exercise 2 shopping cart program

"""

item = input("WHat item would you like to buy?: ")
price = float(input("what is the price of the item?: "))
quantity = float(input("how many items or quantity would you like to buy?: "))

Total = price * quantity
print(f"The toatl cost for the {quantity} {item}(s) is ${Total}")
"""

#X if condition else Y

#num = 2
#a = 6
#b = 8
#print("postive" if num >=0 else "negative")
#print("even" if num % 2 == 0 else "odd")
#print("a" if a > b else wqdw
#print ("a" if a < b else "b")


# password verifiction
"""
username = input("Enter your username:")
if len(username) > 12:
    print("Your user name should not contaion more that 12 ")
elif not username.find(" ") == -1:
    print(" Your username cannot contain space")
elif not username.isalpha():
    print("Your username canot contain number")
else:
    print("Welcome to the world")
"""

#credit card number printing(indexing)
#[start:end:step] colen denotes
"""
credit_num = "1234-5678-8910-1112"
print(credit_num[15:])
print(credit_num[::2])
print(credit_num[::-1])#(Reversing a str)
"""

# While looop(age checking)
"""
age = int(input("Enter your age: "))

while age < 0:
    print("your age cannot be negative")
    age = int(input("Enter your age: "))

print(f"Your are {age} years old")
"""

#while not
"""
food = input("Enter your fav food (q to quit)")

while not food == "q":
    print(f"You like {food}")
    food =  input("Enter your another fav food (q to quit)")

print("bye")
"""

#while or
"""
num = int(input("ENter a num btw 1 to 10: "))

while num < 1 or num > 10 :
    print(f" The num {num} is not valid")
    num = int(input("Enter the valid num btw 1 t0 10"))

print(f"Your num is {num}")

"""

#nested loop
"""
for x in range(3):
    for i in range(1, 10):
        print(i, end="")
    print()
"""

# 2d collections
"""
groces = [["apple", "orange", "bananna", "pineapple"],
          ["chucken", "beef", "muttton"],
          ["cucu", "carrot", "potato",]]


for collection in groces:
    for food in collection:
        print(food, end=" ")
    print()
    
    """


# Functions(section of reusABLE CODES)
"""
def asah_mus():
    print("Niyum njn thamil")
    print("Ntho ondallo")
    print("ath nta enn aroiyillao")
    
asah_mus()
"""
#(bill invoice)using fuction
"""
def bill_invoice(username, bill, due_date):
    print(f"Hello {username}")
    print(f"YOur bill amount is Rs{bill:.2f} due on {due_date} ")

bill_invoice("dith", 20.8989, "01/02")
"""

# retrun function
"""
def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def div(x, y):
    z = x / y
    return z

def mul(x, y):
    z = x * y
    return z

print(add(1,8))
print(sub(5, 9))
print( div(8, 3))
print(mul(3, 5))
""" 
#eg
"""
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first+ " "+ last

full_name = create_name("adith", "sajeev")

print(full_name)
"""

#default arguments
"""
def net_price(list_price, discount= 0.2, tax= 0.05):
    return list_price * (1 - discount) * (1 + tax)

#print(net_price(500))
print(net_price(500, 0.5, 0))
"""

#keyword argument(order 0f the arugument does not matter)
"""
def get_phone(sign, country, first , last):
    return f"{sign}{country}-{first}-{last}"

phone_num = get_phone(country=91,sign= "+", first= 85905, last= 346787)

print(phone_num)
"""

#arbitary(we can use to print a group of words or add or any thing 
#buy using the *)
#eg1
"""
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
     
print(add(1, 3, 5, 6))
"""
#eg2
"""
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Mr", "Adith", "Sajeev")

"""
#creating shipping label eg of arg and kwargs(*, **)

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")


shipping_label("Mr","Adith", "Sajeev",
                street= "Panagalukadu",
                apt= "3031",
                area= "Kadakkal",
                district= "Kollam",
                pin = "691536")












