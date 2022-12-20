# pcost.py
#
# Exercise 1.27

from email import header
from sqlite3 import Row
from wsgiref.headers import Headers
import csv


with open('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv', 'rt') as f:
    headers = next(f)
    totalcost = 0
    for line in f:
        row = line.split(',')
        print(row)
        totalcost = totalcost + (float(row[1])*float(row[2]))
        print(totalcost)
    print("Total cost ", totalcost)

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    totalcost = 0
    for row in rows:
        print(row)
        try:
            totalcost = totalcost + (float(row[1])*float(row[2]))
        except:
            print('something went wrong') 
            continue
    f.close()
    return totalcost
