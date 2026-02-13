# weight converter

weight = float(input("Enter your weight:"))
unit = input("Enter the unit (Kg/L):")

if unit == "Kg":
    result = weight * 2.205
    print(f"Your weight in  pound is {round (result, 2)} lbs")
elif unit == "L":
    result = weight / 2.205
    print(f"Your weight in Kiilogram is {round (result, 2)} kgs")