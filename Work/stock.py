class Stock :
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = shares
        self.price = float(price)
    
    @property
    def shares(self):
        return self._shares

    @property
    def cost(self) :
        '''
        this def returns the total cost of a stock, now with the property tag
        '''
        return float(self.shares * self.price)    

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('expected int')
        self._shares = value
    
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'

    #this function give back how much a share costs

    
    #this function sells shares giving a new share indication
    def sell(self, sell_shares=int):
        '''
        this def sells the shares of a stock
        '''
        self.shares -= sell_shares

class MyStock(Stock):
    def __init__(self, name, shares, price):
        super().__init__(name, shares, price)

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        real_cost = super().cost()
        return 1.25 * real_cost

class NewStock(Stock):
    def yow(self):
        print('Yow!')

