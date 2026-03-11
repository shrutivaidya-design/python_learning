#Logical operators used to combine multiple boolean expressions 

#print(3>1 and 5<1)
#print(3>1 and 5>1)

#print(3>1 or 5<1)

#print(3<1 or 5<1)

#Checking if system is under high pressure 
cpu_usage = 70
memore_usage = 95
#print(cpu_usage > 90 or memore_usage > 90 )

#checking user crendentials before login 
email = True
password = True

#print(email and password)


#print(3!=2)
#print(not not True)

name = ""
#print(not 0)

#Execution order () first
#Allow access if the user is logged in
#or they are a guest
#but they must not be banned 

is_user_logged_in = True
is_user_guest = True
is_user_banned = True

#print(is_user_logged_in or is_user_guest and not is_user_banned)

#print((is_user_logged_in or is_user_guest) and not is_user_banned)

#check if a user's name is not empty and the age is greater than or equal to 18
name = "shruti"
age = 20
#print(name !="" and age >=18 )

#check if the password is at least 8 characters long and does not contain any spaces 
password = " 12345abcd"
#print(len(password))
#print(len(password.lstrip()))
#nr_of_spaces = len(password) -len(password.lstrip())
 
#print(len(password) >=8 and nr_of_spaces ==0)


#check if user's email is not empty,contains '@',and ends with '.com'
email = "vshruti2812@gmail.com"
#print(email !="" and "@" in email and email.endswith(".com"))

#check if user'sname is a string,is not None,and is longer than 5 characters
name = "shruti"
#print(name != "" and type(name) != None and  len(name) > 5)

#check if user's name is admin or a moderator,and either thay are not banned or they have verified their email
user_name = "admin"
is_user_banned = False
email_verified = True

print((user_name == "admin" or user_name == "moderator") and is_user_banned or email_verified)


