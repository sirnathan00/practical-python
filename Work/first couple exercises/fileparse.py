# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',') :
    '''
    this def parses a csv file into a list
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        if types:
            types = types
        else:
            types = [str, int, float]

        records = []
        for row in rows :
            if not row:
                continue
            if indices:
                row = [ row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]

            record = dict(zip(headers, row))
            records.append(record)
        
        return records

print(parse_csv('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.dat', delimiter=' '))
