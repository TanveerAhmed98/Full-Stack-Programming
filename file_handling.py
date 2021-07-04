import os

def read_file(file_name):
    file = open(file_name, "r")
    print("file contents: \n"+file.read())
    file.close()


file = open("file.txt", "w")
file.write("Every thing was cool until you showed up")
file.close()

# reading the file in the read mode
file = open("file.txt", "r")
print("file contents: \n"+file.read())
file.close()

# adding data to the end of the file
file = open("file.txt", "a")
file.write(" but now its better")
file.close()

# lets read the file again
read_file("file.txt")

# deleting a file
os.remove("file.txt")
