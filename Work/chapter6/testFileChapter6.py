# import report
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
# portfolio = report.read_portfolio('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv')
# print(portfolio)
# print(len(portfolio))
# print(portfolio[0])
# print(portfolio[1])
# print(portfolio[0:3])
#print('IBM' in portfolio)
# print('AAPL' in portfolio)
# # finished chapter 6.1 above

# def countdown(n):
#     print('counting down from ', n)
#     while n > 0:
#         yield n
#         n -= 1

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

# def filematch(filename, substr):
#     with open(filename, 'r') as f:
#         for line in f:
#             if substr in line:
#                 yield line

# for line in open('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv'):
#     print(line, end=' ')

# print('\n \n \n ')
# for line in filematch('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv', 'IBM'):
#     print(line, end=' ')

# # everything above this is chpater 6.2 exercises
# # --------------------------------------------------------------------------------------------

# def filematch(lines, substr):
#     for line in lines:
#         if substr in line:
#             yield line

# from follow import follow
# lines = follow('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\stocklog.csv')
# ibm = filematch(lines, 'IBM')
# for line in ibm:
#     print(line)

# # exercise 6.9
# from follow import follow
# import csv
# lines = follow('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\stocklog.csv')
# rows = csv.reader(lines)
# for row in rows:
#     print(row)
from ticker import ticker

ticker('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv', 'C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\stocklog.csv', 'txt')
# ticker('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv', 'C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\stocklog.csv', 'csv')

# # above this are the exercises from 6.3
# nums = [1, 2, 3, 4, 5]
# squares = (x*x for x in nums)
# # print(squares)
# # for n in squares:
# #     print('first')
# #     print(n)
# # for n in squares:
# #     print('second')
# #     print(n)

# print(sum([x*x for x in nums]))
# print(sum(x*x for x in nums))