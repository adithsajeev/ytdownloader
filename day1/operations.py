#Arthematic operations

a=10
b=5 
d=15
print (a+b) # addition
print (a-b) # subtraction
print (a*b) # multiplication
print (a/b) # division  
print (a%b) # modulus( remainder)
print (a**b) # exponentiation  (a to the power b)
print (a//b) # floor division ( quotient without the decimal part)

# comparison operations(boolean values)
print("")
print (a==b) # if a isw equal to b it will print true else false
print(a!=b)  # if a is not equal to b it will print true else false
print (a>b)  #if is a greater than b it will print true else false
print (a<b) # if a is less than b it will print true else false
print(a>=b) # if a is greater than or equal to b it will print true else false
print (a<=b) # if a is less than or equal to b it will print true else false
""" 
#assignment operations(C)
print("")
c = 10
c += 5
print(c)
a -= 3
print(a)
b *= 2  
print(b)
d /= 3
print(d)
"""
# logical operations
print("")

if (a > b and d > a):
    print(True)
else:
    print(False)

if (b > d or b > a):
    print(True)
else:   
    print(False)

print(not(a > b))

# bitwise operations
print("")

print(12 & 13) # AND
print(12 | 13) # OR
print(12 ^ 13) # XOR    
print(~12)     # NOT
print(12 << 2) # left shift 
print(12 >> 2) # right shift

# membership operations
print("")   

players = [11 , 10 , 9 , 7 , 6]
print(10 in players)  # true
print(11 not in players) # False


