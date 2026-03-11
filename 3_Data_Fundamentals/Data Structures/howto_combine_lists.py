#Combining 
letters = ["a","b","c","d"]
numbers =[1,2,3,4,5]
new_list = [letters,numbers]
#print(new_list)
comb = letters + numbers 
#print(comb)

comb = letters * 2
#print(comb)


#extend doesnt create a new list;it expands the original one.
letters = ["a","b","c"]
numbers = [1,2,3,4]
numbers.extend(letters)
print(numbers)

#combing using zip() - Pairing 
#You can pair list with string value 
letters = ["a","b","c","d"]
numbers = [1,2,3,4]
combine=list(zip(letters,numbers ,"hi"))
print(combine)

#Pair customers with their IDs (build relationship between two different lists )
ids = [101,102,106]
name =['Ali','sara','john']

print(list(zip(ids,name)))

#how to combine 
# + - simplest way to combine 
# Nested list but keep them seperated 
# .extend() - extend list by another one whithout creating new one 
#zip() - Pairing (tuple in a list)



