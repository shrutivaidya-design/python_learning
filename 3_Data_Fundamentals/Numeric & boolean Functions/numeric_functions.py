#number functions 
#types 
x = "5"
print(type(x))
print(x*5)
y = int(x)
print(type(y))
print(y*3)

x = 3 #real
y = 4 #imaginary
print(complex(x,y))

#math operators 
print(2+3)
print(5-3)
print(7/2)
print(7//2) #floor division divides two numbers and rounds down 
print(4*2)
print(9%2) # remainder - used to check of number is even or odd
print(2**3) #exponentiation

#shorthand assignment 
x = 1
#x = x+2
x *=2
print(x)

#Rounding 
print(abs(2-8))

# round half to even
#Rounding numbers 
import math
price = 35.54879865
print(round(price,2)) # handy in data analysis to save space 
print(math.floor(price))

print(math.ceil(price)) # perfect for data engineering like splitting data into pages or batches 
print(math.trunc(price)) #cuts out the decimal part and keeps the whole number (no rounding)

print(int(price))

#advanced math 
print(math.sqrt(8) )
#sin() 

#Random 
# random() generates random float between 0.0 and 1.0
#randint() generates random whole number between start and end included 
#Random sampling. Create dummy data for testing 
import random
print (random.random())
print(random.randint(1,10))

#validation
x = 7.1
print(x.is_integer())

x = 70.1 #isinstance () checks if a value belongs to specific datatype 
print(isinstance(x,float))

#Generate a random integer between 1 and 100, and check if the result is an even number 
x =random.randint(1,100)
print(x)
if(x%2)==0 : 
    print("number is even :",x)




