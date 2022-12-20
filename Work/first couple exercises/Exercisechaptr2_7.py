import csv
import math


def types_def(filename) :
    types = [str, int, float]
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)
    # print(row)
    # print(row[1])
    # print(types[1](row[1]))
    # print(types[2](row[2]))
    #print(types[1](row[1])*types[2](row[2]))
    r = []
    for row in rows :
        r.append(list(zip(types, row)))
    converted = [func(val) for func, val in zip(types, row)]
    
 
    
    # converted obave should do the same as the one below
    #for func, val in zip(types,row) :
    #    converted.append(func(val))
    print('this is exercise 2.25 _____')
    print(converted)
    print(headers)
    print(dict(zip(headers, converted)))
    print({ name: func(val) for name, func, val in zip(headers, types, row)})
    
#types_def('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv')

def exercise(filename) :
    types = [str, float, str, str, float, float, float, float, int]
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)
    #print(headers)
    #print(row)
    converted = [func(val) for func, val in zip(types, row)]
    #below is a method to do it for every row
    # converted = []
    # for row in rows :
    #     for func, val in zip(types,row) :
    #         converted.append(func(val))
    # #print(converted)
    record = dict(zip(headers,converted))
    print(record)

#exercise('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\dowstocks.csv')
