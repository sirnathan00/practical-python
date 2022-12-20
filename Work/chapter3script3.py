# fileparse.py
#
# Exercise 3.8
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False) :
    '''
    this def parses a csv file into a list
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
        
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
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print('failed for the row of ', row, ' \n the reason is :', e)
                    continue
            record = dict(zip(headers, row))
            records.append(record)
        
        return records

#print('\n', parse_csv('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\missing.csv', types=[str, int, float], silence_errors=False))
