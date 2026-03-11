#Else in loop
#Runs a block of code when loop finishes naturally.Loop completed without breaks 

items =[1,2,3,4,5]
for item in items:
    if item >6:
        break
    print(item)
else:
    print("Loop is completed")

#Combine else with break inorder to have real usage of else statements 
#else statement will run only if the loop is not interrupted 

#Find out if there are even numbers 
numbers = [1,3,4,5,7]
for number in numbers:
    if number%2==0:
        print(f"Number is even :{number}")
        break
else:
    print("All numbers are odd")

#Check for missing values in list 
names = ["Kamara","Meera","None","Michael"]

for name in names:
    if name ==None:
        print("Missing value found")
        break
else:
    print("All names are available")

#Data qualtiy checks and qualtiy assurance 

#Check if all files are csv files 
files = ["data1.csv","Report.txt","reprt.pdf"]

for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not csv file")
        break
else:
    print("All files are csv")

#check whether any filename appears more than once 
#Print duplicate found" if a duplicate exists,otherwise print "All files are unique"

 
file_list =[
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'data2.csv',
    'data.csv']

for i in range(len(file_list)):
    if file_list[i] in file_list[1+i:]:
        print("duplicate found")
        break
else:
    print("All files are unique")
