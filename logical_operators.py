# and operator

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or operator

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not operator

print(not(True or False or False))

num = int(input("Please enter the number :  "))
if (num % 2 == 0) and (num > 200):
    print("The number is greater than 200 and even")
else:
    print("The number is less than 200 or odd or both at a time")

 