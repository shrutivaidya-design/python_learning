#Inline if statements (Ternary operator)- Instead of writing multiple ifs we can use inline if statements (Quick Logic)

score = 50
#if score>=90:
   # print("A")
#elif score>=80:
   # print("B")
#else:
    #print("F")

grade = ("A" if score>=90 
         else "B" 
         if score>=80 
         else "F")
print(grade)    


#case match - evaluate a value against multiple values .run the code for the first match 
#convert country names into 2-letter abbreviations 
country ="USA"
if country == "United States":
    print("US")
elif country =="India":
    print("IN")
elif country=="Egypt":
    print("EG")
elif country=="Germany":
    print('DE')
else:
    print("Unknown country")

match country:
    case "United States"|"USA":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown country")

#Conditional statements summary
#if statements - Use it inorder to build the first condition 
#elif - Adds a followup question if previous condition was false
#else - "fallback" if all previous condtions are false
#standalone if - if this true ,do this otherwise nothing 
#if else - either execute this or that
#if-elif-else - Choose one from many .(Branching)
#Nested if - step-by-step decisions (Layered tree)
#Independent if - checklist mode(all conditions must be checked and nothing skipped)
#in-line if statement -Quick,short and simple check 
#match case -Pattern matcher (Match one exact value to multiple options)




