# Values stored in lists should always have same data types
temperatures = [235,236,237,238]
print(len(temperatures))
print(temperatures)
print(temperatures[2])

# Two dimensional list

temperatures_centigrade = [[275,2],[273,0]]
print(temperatures_centigrade)
 
#print list values without square brackets
print(*temperatures)

t0,t1 = temperatures_centigrade
print(t1)
