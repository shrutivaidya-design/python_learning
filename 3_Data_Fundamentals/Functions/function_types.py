#action function - Designed to perform an operation in the system instead of returning values 
#printing on screen
#saving data to file or database 
#Sending email or notification if something goes wrong 
#calling api

#Task: store application log messages in a file 

def write_log(message):
   with open(r"C:\Users\vshru\Downloads\python_learning\app.log","a") as file:
       file.write(message + "\n")
      
#write_log("App stopped")


#Transformation functions - Raw data goes in , gets transformed, and returns processed data
#Changing shape of your data ,contain core business logic that manipulate the data 

#Clean email addresses and split them into username and domain 

def clean_split_email(email):
    cleaned = email.strip().lower()
    username,domain = cleaned.split("@")
    return {"username":username,"domain":domain}

#print(clean_split_email("vshruti2812@gmail.com"))

#Validation functions - Validates a condition and returns a boolean result(True or false)
#check user input valid or not
#check business logic
#check permissions (
#Protect from bad data 

#check whether the password meets minimum length of 8 characters 
def is_valid_password(password):
   return len(password)>=8

#print(is_valid_password("12345678"))


#check whether an email has basic valid format
def is_valid_email(email):
    return  "@" in email and "." in email
   
#print(is_valid_email("saragmail.com"))


#Orchestrator functions - Controls program flow by calling other functions in correct order

#We receive an email from user.

#Orchestrator function
def process_user_email(email):
    write_log("App started") 
#We must check if it is valid
#If it is not valid,we log the problem 
    if not is_valid_email(email):
        write_log(f"Invalid email received:{email}")
#If it is valid,we clean it and store structured 
    else:
        cln_email= clean_split_email(email)
        write_log(f"Processed email:{cln_email}")
    write_log("App stopped")
#And we log what happened 

email = input("Please enter your email:")
process_user_email(email)


