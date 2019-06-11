class employee:
    counter = 0
    salary_sum = 0
    def __init__(self,n,f,s,d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        employee.counter = employee.counter + 1
        employee.salary_sum = employee.salary_sum + s

    def avg_salary(self):
        average_salary= self.salary_sum/self.counter
        print("average salary is " + str(average_salary))

    def display(self):
         print("name:"+self.name, "family_name:"+self.family, "salary:"+str(self.salary), "department:"+self.department)

class fulltime_employee(employee):
    def __init__(self, n, f, s, d):
        employee.__init__(self,n,f,s,d)

    e1 = employee("karthik","katta",1000,"cs")
    e2 = employee("me","myself",2000,"cs")
    e3 = employee("ching","chong",5000,"electrical")
    e1.display()
    e2.display()
    e3.display()


e4 = fulltime_employee("keerthy","katta",2000,"civil")
e4.display()
print("number of employees:" +str(employee.counter))
employee.avg_salary(employee)





#2. Web scraping


import requests
from bs4 import BeautifulSoup
import os
html=requests.get("https://en.wikipedia.org/wiki/Deep_learning")
bsObj = BeautifulSoup(html.content, "html.parser")
print(bsObj.title.string)
for link in bsObj.find_all('a'):
    print(link.get('href'))

#3. Numpy
import numpy as np
v = np.random.randint(1,20,15)
print(v)
v[np.where(v==np.amax(v))]=0
print(v)