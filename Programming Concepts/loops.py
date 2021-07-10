# while loop

a = 0
while a < 11:
    print("a = "+str(a))
    a = a+1
while True:
    print("Loop ends here")
    break


# for loop

for b in range(1,12,2):
    print(b)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for c in numbers:
    print(c)

d = 0
while d < len(numbers):
    print(numbers[d])
    d = d +1

dictionary = {
    "name" : "jacky",
     "state" : "stable",
     "performance" : .89
}

for e in dictionary:
    print(dictionary[e])

