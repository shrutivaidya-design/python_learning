
#Dictionay lets you store different types of related informations in key value pairs 

#Ordered,values allow duplicates (keys must be unique),not indexed,mutable
my_dict ={'a':10,
        'b':20,
        'c':20,
        'd':40
}

print(my_dict['b']) #not indexed (access any value using key)

my_dict["c"] = "a"
print(my_dict)


#dict methods 
user ={"id":1,"age":30 ,"city":"Berlin"}

#Access
#print(user["name"])

#Missing key returns none or default value .
print(user.get("name","Unknown"))

#Checks 
print("age" in user)
print("name" not in user)

#View Objects
#items() - when you need key and value together for looping ,transforming ,building new dicts,comparing and more.
print(user.keys())
print(user.values())
print(user.items())

#for looping 
user ={"id":1,"age":30 ,"city":"Berlin"}

#for u in user:
    #print(u,user[u])

for key,value in user.items():
    print(key,value)

#Add,remove,update 

user["name"] = "John"
user["age"] = 55
user.update({"age":40,"city":"Paris"})
print(user)
user.pop("age")
age = user.pop("salary","Not found")
print("Removed item:",age)

user.popitem()
print(user)

#Creation 
user ={"name":None,
       "age":None,
       "id":None,
       "city":None}
#fromkeys() - builds a new dictionary where all the keys get the same default value 
user =dict.fromkeys(["name","age","id","city"],None)
print(user)


#Create new dict
#Keep only pairs with string values 
#Convert values to uppercase
#elegant and short solution !
user ={"id":1,"name":"John",age:30 ,"city":"Berlin"}

user_str = {
    k.upper():v.lower()
    for k,v in user.items()
    if isinstance(v,str)
    #Filter
}
 
print(user_str)

#Use Case : API or Database record 
#Returned records are stored as dictionaries where column names are keys and row value are the dictionary values 

#Mapping to friendly values 
#Great for converting technical codes into friendly labels 
#Mapping abbreviations into full readable names 
#Storing environment variables and configuration (store system settings like host,port and usernames in one clean place)
#ETL and pipeline settings.Great for storing run parameters and controlling how your ETL pipeline loads data
#Metadata structure of your data 


