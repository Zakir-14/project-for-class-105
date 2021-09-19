import math
import csv
from typing import ValuesView

with open("data.csv",newline="") as f :
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):

    mean = 0 
    for values in data:
        mean+= int(values)
    
    mean = mean/len(data)
    return mean

squared_list = []
for number in data :
    a = int(number) -  mean(data)
    a = a**2
    squared_list.append(a)

sum=0
for values in squared_list:
    sum+= values

result = sum/(len(data) - 1)

standard_deviation = result**0.5

print(standard_deviation)



