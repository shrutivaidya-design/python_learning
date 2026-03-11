#while loop - repeats block of code over and over as long as condition is true
#build a counter from 1 to 5

#Counter based loop
count=1 #intialization
while count<=10: #condition
    print(count)
    count+=1 #update
   
#Write a program that keeps asking user "Do you agree" until the user types "Yes"

#answer =""
#while answer!="yes":
   # answer = input("do you agree ? (yes/no) ")
#print("thank you")


#3 attempts
#yes within 3 attempts-> Glad we are on same page
#Otherwise ."3 strikes you are out!"
#If we know how many times to loop then use while condition instead of while true 

attempts = 0 #initialize
while attempts<3: #condition
    answer = input("do you agree ? (yes/no) ")
    if answer=="yes":
        print("Glad we are on same page")
        break
    attempts+=1#update
else:
    print("Otherwise 3 strikes you are out")


#Use case - Open ended (API,database,streams)
while True:
    answer = input("do you agree ? (yes/no) ") 
    if answer=="Yes":
        break
print("thank you")


#difference between for and while loop
#for loop - Loop over a fixed sequence 
#While loop - loop while a condition is true 

#for loop - Predefined condition
#while loop - build your own condition 

#for loop - no. of iteration is known
#while loop - no.of iteration is unknown

#for loop - "Processing data"
#while loop - waiting for event or trigger (building retrys or login)

#for loop - simple , clear , safe and limited
#while loop - complex,advanced , flexible,high risk of building infinite loop


