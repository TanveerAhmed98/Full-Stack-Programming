def function_1():
    print("Did you call me")

function_1()

def function_2():
    return 98
a = function_2()
print(a)

def function_3(param):
    return param*param
b = function_3(5)
print(b)

def function_4(param1, param2, param3):
    value = param1 * param2 * param3
    return value
c = function_4(10,10,10)
print(c)

def function_5(param4):
    if (param4 % 2) == 0:
        print("The number is even")
    else:
        print("The number is odd")
function_5(48)

def function_6(s):
    i = 0;
    while (i < len(s)):
        i = i+1
    return i
print(function_6("TANVEERAHMED"))

