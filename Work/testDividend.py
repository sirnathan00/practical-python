
from decimal import ROUND_DOWN

import math
def buyback(price,dividend,amountStock) :
    for i in range(40) :
        temp = amountStock * dividend/price
        temp = math.floor(temp)
        amountStock = amountStock+temp
        temp2 = amountStock * dividend
        value = amountStock * price
        print('after', i + 1, 'cycles \n the amount of stock you have is', amountStock, '\n this pays you', temp2 ,'per cycle \n', 'the stock is worth', value, '\n')

def reverse(div,price,payout) :
    factor = 1 + div/price
    for i in range(40) :
        amount = payout/div
        temp = math.floor(amount)
        temp2 = temp / factor
        amount= math.floor(temp2)
        payout = amount*div
        value = amount * price
        print('after ', 40-i, 'cycles','\n the payout is', payout, '\n the amount of stocks is', amount, '\n the stock is worth', value, '\n')


reverse(0.46,30,2000)
buyback(30,0.46,2349)


