

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        emit a single row of data
        '''
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    output portfolio data in csv format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    html output formatter
    '''
    def headings(self, headers):
        print('<tr>', end=' ')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end=' ')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class formatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise formatError(f'Unknown table format {fmt}')

def print_table(object, headings, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(headings)
    for obj in object:
        rowdata = [ str(getattr(obj, heading)) for heading in headings ]
        formatter.row(rowdata)