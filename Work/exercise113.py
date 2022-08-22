symobls = 'AAPL,IBM,MSFT,YHOO,SCO'
print(symobls[0],
symobls[1],
symobls[2],
symobls[-1],
symobls[-2])
symobls = symobls + ',GOOG'
print(symobls)
symobls= 'HPQ,' + symobls
print(symobls)
a = ('CAT' in symobls)
print(a)
print(symobls.lower())
print(symobls)
b = (symobls.find('MSFT'))
print(b)
print(symobls[13:17])
symobls = symobls.replace('SCO','DOA')
print(symobls)

#1.19
symlist = symobls.split(',')
print(symlist[0],symlist[1],symlist[-1],symlist[-2])
print(symlist)
symlist[2] = 'AIG'
print(symlist)