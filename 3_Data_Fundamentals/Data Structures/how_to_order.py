#Sorting
letters  = ["c","a","b","d"]
letters.sort()
letters.sort(reverse=True)
#print(letters)

matrix = [  
          ['d','e','f'],  
          ['a','z','i'],
          ['a','a','c'] 
          ]

matrix.sort()
matrix[1].sort()
#matrix.sort(reverse=True)
#print(matrix)

#Sort the data without changing the original list
letters = ["c","a","b"]
#new_list = sorted(letters,reverse =True)
#new_list =sorted(letters)
#print("Original List:",letters)
#print("Sorted List:",new_list)

#letters.reverse()
new_list = list(reversed(letters))

print("Original List",letters)
print("New List",new_list)


#How to sort()
#sort() - Sort lists (Ascending ) low -> high
#reverse = True (Descending)high -> low
#sorted - Returns new sorted list (keep original)
#reverse - flips the list
#reversed - Returns new reversed list (keep original)
