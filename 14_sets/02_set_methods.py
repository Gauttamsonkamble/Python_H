
s = {6 , 8, 5, 1, 3} 

print(s)

s.add(15)
s.add(30)
s.remove(3)

#s.remove(456) # if element not present in set it's throw error
s.discard(234) # this will not throw error if element not present in set

print(s)