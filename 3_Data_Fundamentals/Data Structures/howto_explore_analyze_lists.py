
#Explore and analyze list using :
#functions , methods and operators 
#Analyze - min(),max(),sum(),len()
#Completeness & Existence check - all() did everything pass, any() did something pass
#Search & count - .count("A") how often somethng appears ? ,.index("A")where it appears ?
#Membership and Identity - in /not in(check if exists), is/is not (check if same objects)
#Comparison - == ,>


numbers = [1,5,5,2,6]
print("Max:",max(numbers))

print("Min:",min(numbers))

print("Sum:",sum(numbers))

print("Length:",len(numbers))

print("All:",all(numbers))

print("Any:",any([0,0,0]))
print("Any",any(["a","","c"]))

#.index method - return the position of first occurence 
print("Count:",numbers.count(5))
print("Index:",numbers.index(2))

print(6 not in numbers)

#Comparison - the first elements are compared .If they are equal ,python moves to next element 
lst1 = [5,8 ,3]
lst2 =[5,8,3]
print(lst1 is lst2)








