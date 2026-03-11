#Types
name = 'Shruti'
print(type(name))

age = 28
print(type(age))

#str() - converts any value to string value 
print ("Your age is "+ str(age))
print(type(age))
age = str(age)
print(type(age))

#Math 
# Use case - Validate input length
password = "123a"
print(len(password))

if len(password) < 8 :
    print("Your password is too short !")

text = """
Python is easy to learn.
Python is powerful.
Many people love Python.
"""

# count() returns  how often a word appears in the string 
# Use Case - Detect Qualtiy issues .count how many unwanted characters in my data 
print(text.count("$"))


#Transformations 
#Use case - Clean Numeric Formats (Replace commas with dots in Euro-style decimal nos.)


price = "1234,56"

print(price.replace(",","."))

phone = "74-6488-737"
print(phone.replace ("-",""))

price = "$1,2367"
print(price.replace( "$","").replace(",","."))

# Change Phone number format (Replace special characters with something else )
phone_number = "+49 (176) 123 -4567"
print(phone_number.replace("+","00").replace(" ","").replace("(176)","176").replace("-",""))

#join(concatenates) two strings into one 
first_name = "Michael"
last_name = "Scott"

full_name = first_name + "-" +  last_name
print(full_name)

# Build dynamic paths using folder and file variables 
folder = "c:/Users/vshru/"
file = "report.csv"
full_file_path = folder + file 
print(full_file_path)

# f string - modern and easy way to format and build strings . 'f' - formatted 
name = "Sam"
age = 34
is_student = False
#print("My name is "+ name + ", I am " + str(age) + "years old, and student status is " + str(is_student )+ ".")

print(f"My name is {name} , I am {age} years old , and student is {is_student} .")

print(f"2+3 = {2+3}")

print(f"{{this is me}}")

#split() - breaks string into smaller parts 
stamp = "2026-09-20"
print(stamp.split("-"))

csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))


#Repetition operator (*) -Repeats the string multiple times 
#Use Case - style your Logs .Use repeated characters to create clear sections output 
print("ha" * 3)
print("=="*4)

#Extract multiple characters from string 
# Indexing - extracts one character by position 
# and slicing 

text = "Python"

#Extract the first character
print(text[-3])

date = "20-02-2026"
year = "2026-02-20"
#print(date[6:])
#print(year[:4])


#Extract the month 
#print(date[3:5])

#Extract the day 
#print(year[8:])
print(year[-2:])


#whitespace cleanup
# strip method will remove spaces only from left and right and not in middle 
#Use Case - Detect Extra spaces - Check the length before and after strip() to find unwanted spaces 

text = " Engineering".lstrip()
#print(text)
#print(text.lstrip())

text = "Engineering ".rstrip()
#print(text)

text = " Engineering ".strip()
#print(text)

text = "###Abc###".strip("#")
#print(text)


text = "Engineering"
print(len(text))
print(len(text.strip()))

nr_of_spaces = len(text) - len(text.strip())

is_clean = len(text) == len(text.strip())

print("Number of spaces :",nr_of_spaces)
print("Is my data clean :",is_clean)

# Case Conversions 
# Use case - standardize text case 
# Clean data for matching -lowercase all text inorder to prevent case-based mismatches during search or comparison 
# Always trim and lowercase your data and search term before matching 
text = "python Programming".upper()
print(text)

search = "Email ".lower().strip()
data = "emAil".lower().strip()
print(search==data)

raw = "968-Maria, ( D@t@ Engineer ) ;; 27y "
name = raw.split("-")[1].split(",")[0].strip()
print(name)

role = raw.split("(")[1].replace("@","a").split(")")[0].strip()

print(role)


age = raw.split(";;")[1].replace("y"," years").strip()
print(age)

result = f"name : {name} | role : {role} | age : {age} "
print(result)


#Search 
# in - checks if a word exists in string 
# find () returns first postition of a word in string 
phone = "+49-176 -12345"
print(phone.startswith("+44"))

email = "shruti.gmail.com"
print(email.endswith("gmail.com"))
print("@" in email )

file = "Data.csv"
print(file.endswith(".csv"))



#Validation 
country = "USA2"
print(country.isalpha())


phone = "74884667899"
print(phone.isnumeric())

#String function Summary
#Types
#type()
#str()

#Math
#count()
#len()

#Transformation 
#replace
#split()
#repetition operator
#concatenate (join)
#lstrip()
#rstrip()
#strip()
#upper()
#lower()
#Indexing and slicing

#Search
#startswith()
#endswith()
#in

#validation 
#isaplha()
#isnumeric()

url = "https://api.company/v1/data"
print("/api" in url)

phone1 ="+48-176-12345"
phone2 = "48-732-5674"
phone3 ="0048-654-16548"

print(phone1[phone1.find("-")+1:].replace("-",""))
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

print(phone1.find("-"))
print(phone2.find("-"))







