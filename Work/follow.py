import os, time

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    import report
    
    portfolio = report.read_portfolio('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv')
    
    for line in follow('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s}{price:>10.2f}{change:>10.2f}')





# f = open('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\stocklog.csv')
# f.seek(0, os.SEEK_END)

# while True:
#     line = f.readline()
#     if line == '':
#         time.sleep(0.1)
#         continue
#     fields = line.split(',')
#     name = fields[0].strip('"')
#     price = float(fields[1])
#     change = float(fields[4])
#     if change < 0:
#         print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

# # above this was exercise 6.5 after this it is exercise 6.6 and 6.7

