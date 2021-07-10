text1 =input("Please enter the sentence: ")
text2 =input("Please enter the sentence: ")
text3 = [text1.lower(), text2.lower()]
for text in text3:
    vowels = set("aeiou")
    for character in text:
        if character in vowels :
            vowels.remove(character)
    if len(vowels) == 0:
        print("Yes vowels are found")
    else :
        print("No vowels are not found")
