#Quick and custom logic 
#Lambda is anonymous function (output variable =lambda input variable:expression)
multiple = lambda x: x*2
print(multiple(3))

add =lambda x,y:x+y
print(add(1,2))

#check for existence
check=lambda i:i in "Python"
print(check("z"))

substract=lambda i:i-4
print(substract(2))

#Lambda + map (Convert string to float)
#Steps:
# #Data transformation 
#Put it in lambda
#Map the function to iterator to maipulate the data 

prices =['$12.50','$9.99','$100.00']

print(list(map(lambda p:float(p.replace("$","")),prices)))

b = '$12.50'
print(type(float(b.replace("$",""))))

#lambda + filter(rule to filter data,data)

#remove all prices lower than 100
prices =[120,30,80,300]

print(list(filter(lambda p:p>=100,prices)))

students = [["Maria",85],["Kumar",90],["Max",60]]


#Keep only students with scores higher than 70

#print(list(filter(lambda row:row[1] > 70,students)))

#print(students[2][1] > 70)

#Keep only students with names starting with 'M'

print(list(filter(lambda row:row[0].startswith("M"),students)))
print(students[2][0].startswith("M"))

#Sorted + lambda (custom way to order lists)



