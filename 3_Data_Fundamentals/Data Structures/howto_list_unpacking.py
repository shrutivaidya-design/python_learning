#Unpacking - It is opposite of packing .We unpack the items i.e take items out of the list and put it in a variable
# #use - different info require different operations 
# No. of variables = No. of values 
# Asterisk - stores rest in new list
# underscore - skip items      
person = ["Maria","28","Data Engineer","India","Delhi"]
name = person[0]
age = person[1]
role = person[2]
country = person[3]

#Order of variable should match list values 
#first item ,middle items * (left over items) , last item
name,*details,country,city = person
name,_,_,country,city = person
print(name)
print(country)
#print(name)
#print(details)
#print(city)

*details,country,city = person
print(details)
print(city)

#Rules in unpacking list in python 
numbers = [1,2,3,4,5]

#no. of variables should match no. of values if not using astrick
first,*middle,last = numbers
print(middle)
print(last)
#You can unpack any sequence (lists,tuples,strings,etc.)
numbers ='Hi'
first,*rest = numbers
print(rest)
print(first)

#Skipping items (_)underscore place underscore where you dont need variable 

person = ["Maria","28","Data Engineer","India"]
name = person[0]
age = person[1]
role = person[2]
country = person[3]

name,*_,country = person
print(name)
print(country)



