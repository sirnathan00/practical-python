import stock
a = stock.stock('GOOG', 100, 490.10)
b = stock.stock('AAPL', 50, 122.34)
c = stock.stock('IBM', 76, 91.75)
# print(a.shares)
# print(b.shares * b.price)
# print(c.shares * c.price)
# stocks =[a, b, c]
# for s in stocks:
#     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f} {s.cost():>10.2f}')

# c.sell(25)
# print(c.shares)

import fileparse
with open('C:\\Users\\natha\\OneDrive\\Desktop\\practical-python\\Work\\Data\\portfolio.csv') as lines:
    portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
portfolio = [ stock.stock(d['name'], d['shares'], d['price']) for d in portdicts]
#print(portfolio)
#print(sum([s.cost() for s in portfolio]))