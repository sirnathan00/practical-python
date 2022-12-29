from follow import follow
import csv
import report, tableformat

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = conver_types(rows, [str, float, float])
    rows = make_dicts(rows, ['Name', 'Price', 'Change'])
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def conver_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    return (dict(zip(headers, row))for row in rows)
    # for row in rows:
    #     yield dict(zip(headers, row))

def filter_symbols(rows, names):
    # rows = (row for row in rows if row['name' in names])
    # yield rows
    # above this was a test
    return (row for row in rows if row['Name'] in names)
    # for row in rows:
    #     if row['Name'] in names:
    #         yield row

def ticker(portfile, logfile, fmt):
    portfile = report.read_portfolio(portfile)
    logfile = follow(logfile)
    lines = parse_stock_data(logfile)
    lines = filter_symbols(lines, portfile)
    # lines = (line for line in lines if line['Name'] in portfile)
    format = tableformat.create_formatter(fmt)
    format.headings(['Name', 'Price', 'Change'])
    for line in lines:
        format.row([ line['Name'], f"{line['Price']:10.2f}", f"{line['Change']:10.2f}"])





# if __name__ == '__main__':
#     import report
#     portfolio = report.read_portfolio('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv')
#     lines = follow('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\stocklog.csv')
#     rows = parse_stock_data(lines)
#     rows = filter_symbols(rows, portfolio)
#     for row in rows:
#         print(row)