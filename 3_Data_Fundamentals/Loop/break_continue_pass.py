#Break statement - It stops the loop immediately 
names = ["john","maria","","Kumar"]

for name in names:
    if name=="":
        #print("empty value detected")
        name =name.replace("","Unknown")
        pass #todo handle empty values 
    print(f'Name: {name}')

#continue statement - it skips one loop cycle without stopping whole loop
#use continue to skip bad or empty data without skipping whole loop

#pass statement - it is a placeholder where nothing happens to be changed later 

#Loop through a list of days,print only the working days,skipping the weekends 
days = ["Monday","Tuesday","Wednesday","friday","Thursday"]
weekends = ["Saturday","Sunday"]
for day in days:
    if day in weekends:
        continue
    print(f'Working Day: {day}')
      
#Scan emails to block unsafe data from entering the system 

emails = ["data@gmail.com",
         'maria@gmail.com',
         'DROP TABLE USERS;'
         'shruti@outlook.de']

for email in emails:
    if ";" in email:
        print("SQL Injection : Hacker attack")
        break
    print(f'Processing Email:{email}')



