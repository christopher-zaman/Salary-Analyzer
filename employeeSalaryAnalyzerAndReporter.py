# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Open the file, use csv reader, skip 1st row.
import csv
f = open("Employee_Salaries_-_2016.csv")
rows = csv.reader(f)
next(rows)   

# Create a class
class employeeInfo:
    gender = ""
    salary = 0
    title = ""
    
# Create a empty list to append all data    
employee = []

#Iterate through the rows, sort columns
for col in rows:
    e = employeeInfo()
    e.gender = col[1]
    e.salary = col[2]
    e.salary = e.salary.strip("$") # remove $
    e.salary = float(e.salary) # Parse as a float
    e.title = col[9]
    employee.append(e) #append all data to employee list
      
# Min & Max functions, sum count and average      
def feature1(employee):
    mymin = 999999
    mymax = -99999
    total = 0
    count = 0
    for i in employee:
        if i.salary < mymin:
            mymin = i.salary
        if i.salary > mymax:
            mymax = i.salary
        total = total + i.salary 
        count = count + 1
    print("Max: $" + str(mymin))
    print("Min: $" + str(mymax))
    print("Avg: $" + str(total / count) + "\n")
    
# Male and Female salary averages
def feature2(employee):
    maleCount = 0
    femaleCount = 0
    maleTotal = 0
    femaleTotal = 0
    for i in employee:
        if i.gender == "M":
            maleCount = maleCount + 1
            maleTotal = maleTotal + i.salary
        elif i.gender == "F":
            femaleCount = femaleCount + 1
            femaleTotal = femaleTotal + i.salary
    print("Male Avg: $" + str(maleTotal/maleCount))
    print("Female Avg: $" + str(femaleTotal/femaleCount) + "\n")
    
#Highest paid Position       
def feature3(employee):
    mymax = -999999
    title = ""
    for i in employee:            
        if i.salary > mymax:
            mymax = i.salary
            title = i.title            
    print("Highest paid position is " + title + " with highest salary of $" + str(mymax) + "\n")
    
# Loop to display menu continuously
while True:
    print("Salary Analyzer")
    print("===============")
    print("1- Overall Max/Min/Average Salary")
    print("2- Average Salary by Gender")
    print("3- Highest paid Position")
    print("0- Exit")
    choice = int(input("Choose (1 to 3): "))
   
    if choice == 1:
        feature1(employee)     
        
    elif choice == 2:    
        feature2(employee)           
        
    elif choice == 3:
        feature3(employee)
    
    elif choice == 0:
        print("Thank you for using Salary Analyzer")
        break