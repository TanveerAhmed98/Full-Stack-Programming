def read_file(file_name):
    try:
        file = open(file_name, "r")
        stuff = file.read()
        print(stuff)
        file.close()
    except:
        print("There is an error in read file function")

read_file("apple.txt")

password = input("Please enter the password: ")
if len(password) < 10:
    raise Exception ("The length of a password must be greate than ten")

