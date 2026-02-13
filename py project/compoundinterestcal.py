#Coumpound intrest calculator
"""
p = 0
r = 0
t = 0

while p <= 0:
    p = float(input("Enter the intial principal bal: "))
    if p <= 0:
        print("YOur number canot be equal to 0 ot less than 0")

while r <= 0:
    r = float(input("Enter the intrest rate: "))
    if r <= 0:
        print("YOur number canot be equal to 0 ot less than 0")

while t <= 0:
    t = float(input("number of time perio elasped: "))
    if t <= 0:
        print("YOur number canot be equal to 0 ot less than 0")
   
total = round(p * pow((1 + r / 100), t), 2)
print(f"Balce after the {t} years : {total}")
"""

#folr loop

for i in range(1 , 21):
    if i == 13:
        continue
    else:
        print(i)
