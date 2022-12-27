from stock import Stock, NewStock

# # print(s.__dict__)
# # print(Stock.__dict__)
# # print(s.__class__)
# goog = Stock('GOOG', 100, 490.1)
# ibm = Stock('IBM', 50, 91.23)
# # print(goog.__dict__)
# # print(ibm.__dict__)
# goog.date = '6/11/2007'
# # print(goog.__dict__)
# # print(ibm.__dict__)
# goog.__dict__['time'] = '9:45am'
# # print(goog.time)
# # print(goog.cost())
# # print(ibm.cost())
# # print(str(Stock.__dict__['cost'](goog)))
# # print(str(Stock.__dict__['cost'](ibm)))
# Stock.foo = 42
# # print(goog.foo, ibm.foo)
# # print(goog.__dict__)
# s = goog.sell
# # print(s)
# s(25)
# # print(s)
# # print(s.__func__)
# # print(s.__self__)
# s.__func__(s.__self__, 25)
# # print(goog.shares)

# n = NewStock('ACME', 50, 123.45)
# # print(n.cost())
# # n.yow()
# # print(NewStock.__bases__)
# # print(NewStock.__mro__)

# # for cls in n.__class__.__mro__:
# #     if 'cost' in cls.__dict__:
# #         print(cls)
# #         break

# # print(cls.__dict__['cost'])
    
# s = Stock('IBM', 50, 91.1)
# print(s.shares)
# s.shares = 75
# print(s.shares)

# p = Stock('Test',  100, 'test')
s = Stock('GOOG', 100, 490.1)
print(s.cost)

# a= s.cost
# print(a)

s.price= 385.15
print(s.price)
s.prices = 410.2
