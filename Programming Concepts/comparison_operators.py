a = 5
b = 10

a_gt_b = a > b
print(a_gt_b)

a_lt_b = a < b
print(a_lt_b)

a_ne_b = a != b
print(a_ne_b)

a_e_b = a == b
print(a_e_b)

password = input("Please Enter the password :  ")
correct_pass = "123456"

if password == correct_pass:
    print("The password is correct")
else:
    print("The password is incorrect")


if len(password) >= 6:
    print("Nice Password")
else:
    print("Password is too short")

