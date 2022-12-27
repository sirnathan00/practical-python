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

import report
portfolio = report.read_portfolio('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv')
print(portfolio)
print(len(portfolio))
print(portfolio[0])
print(portfolio[1])
print(portfolio[0:3])
print('IBM' in portfolio)
print('AAPL' in portfolio)