
#Membership operator -checks if a value inside another value like string,list,tuple or other sequence 
#print("o" in "Python")
#print("f" not in "Python")
print(3 not in [1,2,3])

#Security check : ensure that domain is not in banned list
domain="spam.com"
banned_domain = ["spam.com" ,"fake.org" ,"bot.net" ]
print(domain not in banned_domain)

#identity operators -Check if two variables referring to same object in memory 
#if we have multiple variables with simple values then python will create one object for them .All variables will be pointing to same object 
#If we use complex values then python will store them in different object .is operator will give false 

x =["a" ,"b","c"]
y = x

print(x==y)
print(x is y)


#Make sure email exists, and it's not empty
email = None
print(email is not None and email != "")

    

