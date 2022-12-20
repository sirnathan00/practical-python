import csv
def read_prices(filename) :
    '''
    Read prices from a csv file
    '''
    prices = {}
    with open(filename) as f :
        f_csv = csv.reader(f)
        for row in f_csv :
            prices[row[0]] = float(row[1])
    return prices

#see reportV2.py for the rest