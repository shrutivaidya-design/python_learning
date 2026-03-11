
#function is smallest reusable part of code that does one specific job
#Easy  to change
#Fast changes
#Safer(low risk)
#smaller & clean
#easy to read and understand
#modular
#colloboration 
#modularity - breaking big complex problem into smaller manageable pieces 

def greet(): #function definition 
    print("Hello")

greet() #function call

#Parameters VS Arguments 
#Parameters are names used in function definition that describe what data function expects 
#Arguments - Actual values passed in a function call that are assigned to parameters  

case_rule = "lower"
def clean_text(name): 
   cleaned = name.strip() #local variables holding processed version
   if case_rule =="lower":
      cleaned = cleaned.lower()
      print("cleaned:",cleaned)
    #print("Raw:",name) #parameters variables holding raw version 
  

#clean_text("MariA")

#Parameters VS Global VS Local variables (how long is it accessible ? where is it accessible ?)
#Global variable is created outside the function and can be used everywhere 
#Local variable is created inside the function 

def clean_text(first_name,last_name,country="N/A"): 
   first = first_name.strip().lower()
   last = last_name.strip().lower()
   country = country.strip().lower()
   full_name = first+" "+last
   
   print("Full Name:",full_name,"comes from",country)

#Positional Arguments
clean_text("Shruti","Vaidya","India")

#Keyword Arguments
clean_text(country="Germany",first_name="Maria",last_name="De")

#mixed Arguments (Positional argument follow keyword argument)
clean_text("Maria",last_name="De",country='Germany')


#default parameter (parameter without a default follow parameter with a default)
clean_text("Kumar","Suresh")


#*Args **kwargs - allows function to accept any unknown number of arguments 
#calculate the total of values 
def total(a,b):
   print(a+b)

total(1,2)


def total(*args):
   print(sum(args))


total(1,2,3,4,5,6,7)

#create user profile
def create_user(**kwargs):
   print(type(kwargs))

create_user(first_name='Mo',last_name = "Salah",age=33,country="egypt")

#*args - Positional arguments only values
#Same Type
#stored as tuple
#**kwargs - Keyword arguments (names and values)
#different type of information
#stored as dict

