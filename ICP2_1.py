#Write a program, which reads weights (lbs.) of Nstudents into a list and convert these weights to kilograms in a separate list using
N = int(input("enter the number of students"))
lbs_list = []
kgs_list = []
for i in range(N):
    x = float(input("enter the weight of student in lbs"))
    lbs_list.append(x)
    x = x*0.453
    kgs_list.append(round(x,2))
print(lbs_list)
print(kgs_list)

#Write a program that returns every other char of a given string starting with first using a function named “string_alternative”
def string_alternative(x):
    return x[::2]
str = input("enter a string")
res = string_alternative(str)
print(res)

#Write a python program to find the wordcountin a file for each line and thenprint the output.Finally store the output back to the file.
fileName = input("enter your file name")
wordcount= {}
file = open(fileName,'r')
for line in file:
    words = line.split(" ")
print(words)
for words1 in words:
    count= wordcount.get(words1,0)
    wordcount[words1] = count + 1
key_list = wordcount.keys()

for word in key_list:
    print(word,wordcount[word])

