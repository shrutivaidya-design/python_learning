#Create a list of 1,000,000 salaries ranging from 50,000 to 150,000

import random
#print(random.randint(50000,150000))

#List comphrehension
salary_list = [
    random.randint(50000,150000) for _ in range(1_000_000)
]

#print(salary_list)


import statistics

mean_salary =statistics.mean(salary_list)
#print(mean_salary)



import time
start_time = time.time()
# Your code here
statistics.mean(salary_list)

end_time = time.time()
#print(f"Execution time in statistics for mean: {end_time - start_time:.4f} seconds")

import numpy as np
start_time = time.time()
# Your code here
np.mean(salary_list)

end_time = time.time()
#print(f"Execution time in numpy for mean: {end_time - start_time:.4f} seconds")

#Array function 
my_array=np.array([1,2,3,4,5])
#print(my_array)

#print(my_array.mean())
#print(my_array.min())

#Job Titles
job_titles =np.array(['Data Analyst','Data Engineer','Machine Learning Engineer','Data Scientist',"AI Engineer"])
print(job_titles)

#Base salaries
base_salaries =np.array([40000,70000,90000,10000,np.nan])
print(base_salaries)
# Bonus rates
bonus_rates = np.array([0.05,0.2,0.08,0.12,np.nan])
print(bonus_rates)

total_salary = base_salaries * (1+ bonus_rates)
print(total_salary)
 
print(np.nanmean(total_salary))


#print(type(np.nan))