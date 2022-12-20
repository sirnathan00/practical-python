#this is the file parse used in chapter 3 module 6 "design discussion"

import csv

def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False) :
    '''
    this def parses a csv file into a list
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
        
#for rows in file: 
#using a for loop was apperantly incorrect and they want you to have it ass it follows after this.
#i figured out why they want it this way. it is due to the fact that te zip is individual CSV files so you needed to use multipale csv files
    rows = csv.reader(file, delimiter=delimiter)
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

def main(args):
    if len(args) != 6:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    parse_csv(args[1], args[2], args[3], args[4], args[5])

if __name__ == '__main__' :
    import sys
    main(sys.argv)
