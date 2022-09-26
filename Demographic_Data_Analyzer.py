import pandas as pd
import numpy as np



table = pd.read_csv("adult.data.csv")

# How many people of each race are represented in this dataset?
count_race = table["race"].value_counts()
print (count_race.head()) 

# What is the average age of men?
men_data = table[table.sex == "Male"]
print (np.mean(men_data["age"]))

# What is the percentage of people who have a Bachelor's degree?
bach = table[table.education == "Bachelors"]
print ((len(bach) / len(table))*100)
 
# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
adv_edu = table[(table.education == "Bachelors")  |  (table.education == "Masters")  |  (table.education == "Doctorate") ]
more_50K = adv_edu[adv_edu.salary == ">50K"]
print ((len(more_50K) / len(adv_edu))*100)

# What percentage of people without advanced education make more than 50K?
nonadv_edu = table[(table.education != "Bachelors")  &  (table.education != "Masters")  &  (table.education != "Doctorate")]
nonadv_more_50K = nonadv_edu[nonadv_edu.salary == ">50K"]
print ((len(nonadv_more_50K) / len(nonadv_edu))*100)

# What is the minimum number of hours a person works per week?
print (np.min(table["hours-per-week"]))

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
table.rename(columns={"hours-per-week" : "hours_per_week"}, inplace=True)
hours = table[table.hours_per_week == 1]
more_than50K =  hours[hours.salary == ">50K"]
print ((len(more_than50K) / len(hours))*100)

# What country has the highest percentage of people that earn >50K and what is that percentage?
table.rename(columns={"native-country" : "country"}, inplace=True)
more_50K = table[table.salary == ">50K"]
count_country = more_50K["country"].value_counts()
print ((count_country["United-States"] / len(more_50K))*100)

# Identify the most popular occupation for those who earn >50K in India.
more_50K_India = table[(table.salary == ">50K") & (table.country == "India")]
occup_Ind = more_50K_India["occupation"].value_counts()
print (occup_Ind.idxmax())
