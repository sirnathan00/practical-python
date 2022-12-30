# def avg(x, *more):
#     return float(x+sum(more))/(1+len(more))

# print(avg(10,11))
# print(avg(3,4,5))
# print(avg(1,2,3,4,5,6))

# data = ('GOOG', 100, 490.1)

# from stock import Stock

# s= Stock(*data)
# print(s)

# data2 = { 'name': 'GOOG', 'shares': 100, 'price': 490.1}
# s2 = Stock(**data2)
# print(s2)

# import report
# port = report.read_portfolio('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\missing.csv', silence_errors=True)
# # above is chapter 7.1
# # ---------------------------------------------------------------------

# import report
# portfolio = list(report.read_portfolio('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv'))

# def stock_name(s):
#     return s.name

# # portfolio.sort(key=stock_name)
# portfolio.sort(key=lambda s: s.price)

# for s in portfolio:
#     print(s)

# # above is chapter 7.2
# # ---------------------------------------------------------------------

# from stock import Stock
# s = Stock('IBM', 50, 91.1)
# print(s.name)
# s.shares = '100'
# # above is chapter 7.3
# # -----------------------------------------------------------------------

def add(x, y):
    return x + y

def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

logged_add = logged(add)
print(logged_add)
print(logged_add(3, 4))

@logged
def sub(x, y):
    return x - y

print(sub(4, 3))

from timethis import timethis

@timethis
def countdown(n):
    while n > 0:
        n -= 1
    print('done')

countdown(100000000)