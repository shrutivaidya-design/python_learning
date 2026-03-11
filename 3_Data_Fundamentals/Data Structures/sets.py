
#Set - It is unordered collection of unique values
#Unordered,doesnt allow duplicates,not indexed,it is mutable
my_set = {10,30,20}
my_set.remove(20)
print(my_set)

a = {10,20,30,40}
a.add(10)
print(a)

a.update({1,2,3})
a |= {1,2}
print(a)

a.remove(3)
print(a)

a.discard(100) #if item is not there it will not throw error
print(a)

#Math methods 
a = {10,20,30,40}
b = {30,40,50,60}

#print(a.union(b))
#print(a|b)
print(a&b)
#print(a.intersection(b))

#print(a.difference(b)) return items in A which are not in B
print(a-b)

#Find non-sharing values
print(a^b)
#print(a.symmetric_difference(b))

#relationship methods 
a = {10,20}
b = {30,40,50,60}

#Inorder to do quality checks 
#If one group is fully contained in another 
print(b.issubset(a))

#Returns true when it includes all items of the other set 
print(b.issuperset(a))

#Returns true if both sets share no items (no overlapping)
print(a.isdisjoint(b))