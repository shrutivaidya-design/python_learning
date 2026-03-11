
#Looping +  Transformations + filtering  (filter is optional)
domains =["www.google.com","openai.com","localhost","WWW.DATAWITHBARAA.COM"]

#normalize domain into standard formats 
#cleaned = [d.lower().replace("www.","")  #Data transformation
           #for d in domains              #Loop
            # if "." in d ]               #filtering 

cleaned = [d for d in domains if "." in d ]
print(cleaned)

#Summary data structures 
#how to access list - 
# Indexing[0]- access single item from list
# slicing [1:2] - access multiple items from list

#how to unpack list
#In one line we are assigning multiple variables to  values in our list

#built in funcions
#Max() , Min()
#Len() - how many items do we have inside our list
#all() - check if there are any missing values 
#any() -check if atleast one true in our list

#built in methods 
#.count() - how many times item appears in list
#.index() - where exactly we can find item (position)
#in - is this item member of our list

#change our list
#.append() - to add item end of our list
#.insert(index,value) - you can put items exactly where you want by specifying index
#clear() - remove all items
#remove() - remove by specific value
#pop() - sepecify excatly which position should be removed .by default it is last

#sort
#.sort()
#.reverse()
#assignment (assign two different variables to same list)
#.copy() - (two variables poititng to different list applys for simple list
#If list is nested it will create shallow copy .So only first level is separated but child is shared 
#deepcopy() - keeps all levels isolated in real copy

#Combine
# + operator - combine two lists to generate brand new list
# extend() - expand what is there
#zip() - Its connect items from multiple lists to pairs 
#enumerate() - It adds index number to each value of the list
#map(fn,data) - It will apply data transformation for all the items in list
#filter(fn,data) -will only keep items that fullfils condition

#list comphrehension - Its like both filter and map function in one 




