"""
   This function checks whether the password has atleast 3 numbers, length of a password is more than or equal to 8 and
   contains atleast one uppercase and lowercase letter.

"""

def is_password_valid(password):
    l, u, d, c = 0, 0, 0, 0
    if (len(password) >= 8):
        for i in password:
            if (i.isnumeric()):
                c += 1
                if(c >=3):
                    d += 1  
            if (i.islower()):
                l+=1            
            if (i.isupper()):
                u+=1  
    if (l>=1 and u>=1 and d>=1 and l+u+c==len(password)):
        return True
    else:
        return False
        
password_check = is_password_valid("Tanveer")
print(password_check)

