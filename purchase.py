import calendar
from datetime import date
from tokenize import String
from unicodedata import decimal
from card import Card

class Purchase():
    def __init__(self, day, month, year, card, amount) -> None:
        self.date = date(year, month, day)
        self.card = Card(card)
        self.amount = amount
        self.status  = False
    
    #calculates the amount and the transaction fee for this purchase
    def total (self)-> decimal:
        fee = self.amount * self.card.fee() / 100
        total = self.amount + fee
        return total

    #returns the month range in a string
    def billingCycle(self) ->String:
        days = calendar.monthrange(self.date.year, self.date.month)
        range = str(self.date.month) + "-" + str(1) + "-" + str(self.date.year) + ", "+ str(self.date.month) + "-" + str(days[1]) + "-" + str(self.date.year)
        return range

    #returns the status of the purchase
    #false means not paid off
    #set to true when payment made in the payment platform
    def getStatus(self) -> bool:
        return self.status


f =  open('data.txt', 'r')
users = f.readlines()
f.close()

print(users)
