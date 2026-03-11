#Copying methods 
#Assignment "=" (reference)
#Both variables reference same list in memory

letters = ["a","b","c"]
#letters_copy = letters
#letters.append("d")
#letters_copy.append("e")
#print("Original:",letters)
#print("Copy :",letters_copy)

#Copying without effecting original data (Shallow copy)
letters_copy =letters.copy()
letters_copy.append("f")
print(letters_copy)
print(letters)

#Deep copy - It is safest way and is completely independent 
matrix = [  
          ["a","b"],
          ["c","d"]
          ]


#matrix_copy = matrix.copy()
#matrix_copy.append(['x' ,"y"])
#matrix_copy.remove(["x","y"])
#matrix_copy.pop()
#matrix_copy[0].append("z")

#print("Original:",matrix)
#print("Copy:",matrix_copy)

#Copy() function from copy module acts same as copy method(shallow copy) 
import copy
matrix = [["a","b"],
         ["c","d"]
          ]
matrix_copy = copy.deepcopy(matrix)
matrix_copy[0].append("z")
print("Original:",matrix)
print("Copy:",matrix_copy)

#Testing is operator 

original = [  
          ["a","b"],
          ["c","d"]
          ]

#is operator - check if two variables refer to same object 
#use the is operator to check if the copies are independent 
copy1 = original
print("Same object?",copy1 is original,"\n")

copy2 = original.copy()
print("Same object?",copy2 is original,"\n")
print("Same Lists?",copy2[0] is original[0],"\n")


copy3 = copy.deepcopy(original)
print("Same object?",copy3 is original,"\n")
print("Same Lists?",copy3[0] is original[0],"\n")

copy4 = copy.copy(original)
print("Same object?",copy4 is original,"\n")
print("Same object?",copy4[0] is original[0],"\n")


#How to copy
#Avoid assignment (risky & confusing)
#use .copy() for simple , flat lists
#use copy.deepcopy() - for nested lists (completely independent lists,no shared references)





