#Loop - control flow of program
#Repeat a block of code over and over again until a condition is met 

#for loop - go through group of items in a list one by one .Do something for each item 
#Loop variable - define a loop variable to assign the current value of the sequence 
#Sequence - List you want to iterate 
#Python iterator - an Object that lets you go through items one by one in sequence.Remembers what done .knows what next 
#Types of Sequence - list ,tuple , string ,range,dict,file
#We can also iterate through columns 


for item in range(2,10,2):
    print(f"Round: {item}")


#Use cases - load data,data preparations ,data cleansing (Transform data like cleaning data before processing)
#we use for loops to go through values and aggregate data like summing,counting and averaging 
#First cleanup and then manipulate
scores = [10,20,30,40,50,60]
total =0

for score in scores:
    total+=score
    print("Current score:",score)
print("Final score:",total)

files = [" Report.csv", "DATA.csv" , "final.TXT"]
for file in files:
    file=file.strip().lower().replace("txt","csv")
    print("Processing:",file)



 #Print 7 times table from 1 to 10 using a for loop 
print(7*1)
print(7*2)
print(7*3)
print(7*4)


for item in range(1,11):
    counter=7*item
    print("7 *",item,"=",counter)

#Print a left-aligned pyramid of stars with 6 rows using a for loop

for item in range(1,7):
    print("*" * item)

