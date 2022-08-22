# pcost.py
#
# Exercise 1.27

from email import header
from sqlite3 import Row
from wsgiref.headers import Headers


with open('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv', 'rt') as f:
    headers = next(f)
    totalcost = 0
    for line in f:
        row = line.split(',')
        print(row)
        totalcost = totalcost + (float(row[1])*float(row[2]))
        print(totalcost)
    print("Total cost ", totalcost)