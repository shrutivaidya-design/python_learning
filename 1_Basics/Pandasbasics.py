import pandas as pd
df =pd.read_csv("C:/Users/vshru/Downloads/python_learning/Python for Data Analytics/dim_customers.csv")

#print(df)

#print(df['customer_id'])

##print(df.gender)
#print(df.customer_id[24])
#print(df.marital_status)


from datasets import load_dataset
dataset =load_dataset('lukebarousse/data_jobs')
#print(dataset['train'])

df = dataset['train'].to_pandas()
#print(df)
#print(df['job_location'])


#print(df.job_country)

#print(df.tail(10))

#print(df[['job_title_short','job_location','job_type_skills']].iloc[90:95])

#print(df.iloc[90:95])

#Method 
#All column names , datatype , null/non-null info
#print(df.info())
#Provides key statistics from numerical columns 
#print(df.describe())

#distinct job titles 
#print(df.job_title_short.unique())

print(df[(df.job_title_short=='Data Analyst') &(df.salary_year_avg > 10000) ])


