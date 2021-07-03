Student_name = input("Please enter the student name: ")
English = int(input("Please enter the marks obtained in English: "))
Maths = int(input("Please enter the marks obtained in Maths: "))
Physics = int(input("Please Enter the marks obtained in Physics: "))
Chemistry = int(input("Please Enter the marks obtained in Chemistry: "))
Computer = int(input("Please Enter the marks obtained in Computer: "))
new_list=[]
new_list.append(English)
for i in new_list:
    if (i>=90 and i<=100):
        print(Student_name + " Acheived A Grade in English ")
    elif (i>=80 and i<=89):
        print(Student_name + " Acheived B Grade in English ")
    elif(i>=70 and i<=79):
        print(Student_name + " Acheived C Grade in English ")
    elif(i>=60 and i<=69):
        print(Student_name + " Acheived D Grade in English ")
    elif(i>=50 and i<=59):
        print(Student_name + " Acheived E Grade in English ")
    elif(i>=0 and i<=49):
        print(Student_name + " Gets Failed in English ")
    else:
        print("Not a valid input ")
new_list.remove(English)
new_list.append(Maths)
for i in new_list:
    if (i>=90 and i<=100):
        print(Student_name + " Acheived A Grade in Maths ")
    elif (i>=80 and i<=89):
        print(Student_name + " Acheived B Grade in Maths")
    elif(i>=70 and i<=79):
        print(Student_name + " Acheived C Grade in Maths ")
    elif(i>=60 and i<=69):
        print(Student_name + " Acheived D Grade in Maths ")
    elif(i>=50 and i<=59):
        print(Student_name + " Acheived E Grade in Maths ")
    elif(i>=0 and i<=49):
        print(Student_name + " Gets Failed in Maths ")
    else:
        print("Not a valid input ")
new_list.remove(Maths)
new_list.append(Physics)
for i in new_list:
    if (i>=90 and i<=100):
        print(Student_name + " Acheived A Grade in Physics ")
    elif (i>=80 and i<=89):
        print(Student_name + " Acheived B Grade in Physics ")
    elif(i>=70 and i<=79):
        print(Student_name + " Acheived C Grade in Physics ")
    elif(i>=60 and i<=69):
        print(Student_name + " Acheived D Grade in Physics ")
    elif(i>=50 and i<=59):
        print(Student_name + " Acheived E Grade in Physics ")
    elif(i>=0 and i<=49):
        print(Student_name + " Gets Failed in Physics ")
    else:
        print("Not a valid input ")
new_list.remove(Physics)
new_list.append(Chemistry)
for i in new_list:
    if (i>=90 and i<=100):
        print(Student_name + " Acheived A Grade in Chemistry ")
    elif (i>=80 and i<=89):
        print(Student_name + " Acheived B Grade in Chemistry ")
    elif(i>=70 and i<=79):
        print(Student_name + " Acheived C Grade in Chemistry ")
    elif(i>=60 and i<=69):
        print(Student_name + " Acheived D Grade in Chemistry ")
    elif(i>=50 and i<=59):
        print(Student_name + " Acheived E Grade in Chemistry ")
    elif(i>=0 and i<=49):
        print(Student_name + " Gets Failed in Chemistry ")
    else:
        print("Not a valid input ")
new_list.remove(Chemistry)
new_list.append(Computer)
for i in new_list:
    if (i>=90 and i<=100):
        print(Student_name + " Acheived A Grade in Computer ")
    elif (i>=80 and i<=89):
        print(Student_name + " Acheived B Grade in Computer ")
    elif(i>=70 and i<=79):
        print(Student_name + " Acheived C Grade in Computer ")
    elif(i>=60 and i<=69):
        print(Student_name + " Acheived D Grade in Computer ")
    elif(i>=50 and i<=59):
        print(Student_name + " Acheived E Grade in Computer ")
    elif(i>=0 and i<=49):
        print(Student_name + " Gets Failed in Computer ")
    else:
        print("Not a valid input ")
obtained_marks = int(English) + int(Maths) + int(Physics) + int(Chemistry) + int(Computer)
total_marks = 500
final_percentage = int(obtained_marks) / int(total_marks) * 100
new_list.remove(Computer)
new_list.append(final_percentage)
for i in new_list:
    if (i>=90 and i<=100):
        print(Student_name + "'s Final Grade is: A  ")
    elif (i>=80 and i<=89):
        print(Student_name + "'s Final Grade is: B  ")
    elif(i>=70 and i<=79):
        print(Student_name + "'s Final Grade is: C  ")
    elif(i>=60 and i<=69):
        print(Student_name + "'s Final Grade is: D  ")
    elif(i>=50 and i<=59):
        print(Student_name + "'s Final Grade is: E  ")
    elif(i>=0 and i<=49):
        print("You Gets Failed  ")
