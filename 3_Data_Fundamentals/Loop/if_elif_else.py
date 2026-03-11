#Conditional statements - check point to check conditions
#if statement - defines the first condition .If true do something otherwise do nothing 
score = 65
submitted_project = True

if score >=90 and submitted_project:
    print("A+")
elif score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
   print("C")
elif score<=60 or submitted_project:
    print("D")
else:
   print("F")


#else  statement - runs only if all previous conditions are false

#elif statement - asks a follow-up question if previous conditions are false 

#Use cases - building grading system,assigning roles to users , checking code status 

#Nested if

#independent ifs - all conditions are tested even if one is already true 

score = 100
submitted_project = True

if score >= 90:
    print("High score")
else:
    print("Low score")

if submitted_project:
    print("Project is submitted ")
else:
    print("Project is not submitted")


#Validate the quality and correctness of email values 
email ="#vshruti@gmail.com"
valid = True
#first clean string
email==email.strip()
if email=="":
    print("email cannot be empty")
    valid = False
if not("." in email and '@' in email):
    print("email must contain '.' and '@'")
    valid = False
if email.count("@")!=1:
    print("email must contain exactly one '@' symbol")
    valid = False
if not email.endswith(('.com','.org','.net')):
    print("Email must end with '.com','.org',or '.net'")
    valid = False
if len(email)>254:
    print("Email length must not be longer than 254 characters")
    valid = False
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with letter or digit" ) #isaplhanum() - checks if the string contains only letters and digits 
    valid = False
if valid:    
    print("email is valid")

#Validate the quality and correctness of passwords
password="vshruti2812@gmail.com"
email = "vshruti2812@gmail.com"
valid = True
#first clean the string
#password ==password.strip() 
nr_of_spaces=len(password) - len((password).strip())
if password=="":
    print("password cannot be empty")
    valid= False
if not(len(password)>8):
    print("password length must be atleast 8 characters")
    valid= False
if password.isupper():
    print("password must include atleast one lowercase")
    valid= False
if password.islower():
    print("password must include atleast one uppercase")
    valid= False
if password==email:
    print("Password must not be same as email")
    valid= False
if not (nr_of_spaces ==0):
    print("password must not contain any spaces")
    valid= False
if not(password[0].isalnum() and password[-1].isalnum()):
    print("password must start and end with a letter or digit") 
    valid= False
if valid:
    print("Password is valid")

