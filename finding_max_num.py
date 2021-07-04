def find_max(array):
    largest = 0
    for x in range(0, len(array)):
        if(array[x] > largest):
            largest = array[x]
    return largest

num = [10,20,30,40,50,60]
print(find_max(num))

