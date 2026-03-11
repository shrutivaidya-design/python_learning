#Nested for loop - a loop inside another loop



for x in range (3): #outerloop
    for y in range(2): #innerloop
        for z in range(2):
            print(f"({x},{y},{z})")


#Crossing or combining data (combine each value from first list with other values of other list)

colours =["red","blue","green"]
sizes = ["S","M","L"]


for colour in colours:
    for size in sizes:
        print(f"{colour}- size {size}")

#Navigate hierarchy 
years = ["2026","2027"]
months = ["Jan","Feb"]
days = range(1,30)
 
for y in years:
    for m in months:
       for d in days:
          print(f"report.{y}.{m}.{d}.csv")

#Navigate through table and columns 
tables = ["customers","products","orders","prices"]
columns = ["id","create_date"]
for t in tables:
   for c in columns:
       print(f"Select count(*) from {t} where {c} IS NULL")
      

#Navigate through containers , folders and files in azure 
