#Iterators and iterable 
#Why do we need iterators - 
# For loop - 
# Save memory 
# speed and flexibilty (Data pipeline)

#Iterable - independent items we can loop over .Eg ["a","b"] ,"Data"
#anything which has sequence 
#Iterator is an object that helps us to do iteration 
#Iterator is process or machine that helps us to do next items

letters = ["a","b","c"]
new_list = []
for l in letters:
    new_list.append(l.lower())
   # print(new_list)
 

#Enumerate() - It will take iterable value or string value and will return postion number and value 
#enumerate is a iterator we can use it in for loop to iterate through values 
#enumerate use case - find the exact position of bad data in your list
#zip() - Combines two or more sequences into pairs (tuples)

letters = ['a',"b",'c']
numbers = [1,2,3]
print(list(zip(letters,numbers)))
#print(list(reversed(letters)))
#print(list((enumerate(letters,start=1))))
#for index,value in enumerate(letters):
   # print(index,value)

#for l in reversed(letters):
  # print(l)

for l,n in zip(letters,numbers):
    print(l,n)

#Map iterator Object 
#Map is fast,clean way to do data transformations 
letters = ["a","b","c"]

print(list(map(str.upper,letters)))

numbers = ["1","2","3"]
print(list(map(int,numbers)))


names = [" maria ","John ","kumar "]
print(list(map(str.strip,names)))

for n in map(str.strip,names):
    print(n)

#filter iterator
#filter() is perfect for cleaning up your data in data structures 
letters = ["a","",None,"c",False]

#print(list(filter(None,letters)))

print(list(filter(bool,letters)))

items =['sql','143','python','42']

print(list(filter(str.isalpha,items)))
for item in filter(str.isalpha,items):
   print(item)


