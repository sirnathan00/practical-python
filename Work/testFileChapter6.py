import report
# x = [1,2,3]

# it = x.__iter__()
# print(it)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

##first part is the first par of exercise 6.1 basicly
# f = open('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv')
# print(f.__iter__())
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# report.portfolio_report('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv', 'C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\prices.csv', 'txt')
# import pcost
# print(pcost.portfolio_cost('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv'))

# # exercise 6.2 above this

# import report
portfolio = report.read_portfolio('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv')
# print(portfolio)
# print(len(portfolio))
# print(portfolio[0])
# print(portfolio[1])
# print(portfolio[0:3])
print('IBM' in portfolio)
# print('AAPL' in portfolio)
# # finished chapter 6.1 above

def countdown(n):
    print('counting down from ', n)
    while n > 0:
        yield n
        n -= 1

# x = countdown(10)
# print(x)
# print(x.__next__())
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# # above this is the litrature for chapter 6.2

def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line

for line in open('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv'):
    print(line, end=' ')

print('\n \n \n ')
for line in filematch('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv', 'IBM'):
    print(line, end=' ')
