#change your list - add items 
#append at the end 
letters = ["a","b","c","d"]
letters.append("e")
#print(letters)

#insert at specific position

letters.insert(2,"f")
#print(letters)

#Adding 
matrix = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']
          ]

matrix.append(["x","y","z"])

#matrix.insert(0,["x","x","x"])  


matrix[0].insert(0,"z")
#print(matrix) 

#How to add
#.append() - add item at the end 
# .insert(index,value) - inserts at specific position 

#remove value by first match 
letters = ["a","c","c","d"]
#letters.clear()
#letters.remove("c")
#letters.remove("c")
removed = letters.pop(1) #default is last item (Removing and returning)
print(letters)
print(removed)


matrix = [['a','b','c'],  #Row 0
          ['d','e','f'],  #Row 1
          ['g','h','i']   #Row 2
          ]

#matrix.remove(["a","b","c"])
matrix[0].pop()
#matrix.pop()
print(matrix)

#Use - Removing old , duplicate and bad data 
#how to remove
#.clear() - remove all items 
# .remove(value) - Remove by value(first match)
# .pop(index) - Remove and return by position (default is last item)


#Update
letters = ["a","b","c"]
letters[0]="x"
print(letters)

matrix = [['a','b','c'],  #Row 0
          ['d','e','f'],  #Row 1
          ['g','h','i']   #Row 2
          ]

#matrix[-1] = ["x","y","z"]
matrix[1][1] = "-"
matrix[-1][-1] = "-"
print(matrix)

