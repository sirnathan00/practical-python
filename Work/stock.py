class stock :
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)

    #this function give back how much a share costs
    def cost(self) :
        '''
        this def returns the total cost of a stock
        '''
        return float(self.shares * self.price)
    
    #this function sells shares giving a new share indication
    def sell(self, sell_shares=int):
        '''
        this def sells the shares of a stock
        '''
        self.shares -= sell_shares