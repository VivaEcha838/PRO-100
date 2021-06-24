class ATM():
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        
    def cashWithdrawal (self):
        print("Cash has been withdrawn")

    
    def receivedMoney(self):
        print("You have received the money")

    def calcMoneyOwed(self, monthly, years):
        mileage = monthly*years
        print(mileage)

Jaking = ATM("165748475", "89765")
Telly = ATM("140847587", "74836")


Jaking.cashWithdrawal()
Telly.calcMoneyOwed(675,8)
