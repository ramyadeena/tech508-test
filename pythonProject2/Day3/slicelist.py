

mixture =[1,2,3,'one','two','three']
print(mixture)
print(mixture[1:3]) # print 2nd and 3rd item in the list
print(mixture[0:1:2]) # ::2 print every second item in the list
print(mixture[::3])
#mixture.reverse()
#print(mixture[-2:])
print((list(reversed(mixture))))
print(list(reversed(mixture[-2:]))) # print last 2 item in reversed order, three, two.

