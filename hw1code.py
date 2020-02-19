import random


class Investment:  # parent class of investments , Stock, MutualFund and Bonds
    ticker = ""
    amount = 0

    def __init__(self, ticker):
        self.ticker = ticker


class Stock(Investment):
    price = 1

    def __init__(self, price, ticker):
        super().__init__(ticker)
        self.price = price


class MutualFund(Investment):
    price = 1

    def __init__(self, ticker):
        super().__init__(ticker)
        self.price = 1


class Bond(Investment):
    facevalue = 0
    maturity = 0

    def __init__(self, facevalue, ticker, maturity):
        super().__init__(ticker)
        self.maturity = maturity
        self.facevalue = facevalue


stockDict = {Stock.ticker: [Stock.ticker, Stock.price, Stock.amount]}
fundDict = {MutualFund.ticker: [MutualFund.ticker, MutualFund.price, MutualFund.amount]}
bondDict = {Bond.ticker: [Bond.ticker, Bond.facevalue, Bond.maturity, Bond.amount]}


class Portfolio:
    cash = 0
    k = "\t" + "---HISTORY OF TRANSACTIONS---" + "\n"  # string that keeps track of all the transactions

    def __init__(self):
        self.k = "\t" + self.k + "You created a {}".format("portfolio") + "\n"

    def history(self):
        print(self.k)
        return self.k

    # when print function is called -- prints whats inside the portfolio
    def __str__(self):
        a = "Cash: ${} \n".format(self.cash)
        b = "\nStocks: "
        for key in stockDict:
            if key != "":
                b = b + stockDict[key][0] + "  " + stockDict[key][2].__str__() + "\n" + 2 * "\t"
        c = "\nMutual Funds: "
        for key in fundDict:
            if key != "":
                c = c + fundDict[key][0] + "  " + fundDict[key][2].__str__() + "\n" + 3 * "\t"
        d = "\nBonds: "
        for key in bondDict:
               if key != "":
                d = d + bondDict[key][0] + "\n" + 2 * "\t"
        return "\t" + "\n" + "---PORTFOLIO---" + "\n" + a + b + c + d

    def addCash(self, x):
        self.cash = self.cash + x
        self.k = "\t" + self.k + "Added ${} of cash. Cash balance = {} ".format(x, self.cash) + "\n"
        return self.cash

    def withdrawCash(self, x):
        self.cash = self.cash - x
        self.k = "\t" + self.k + "Withdraw ${} of cash. Cash balance = {} ".format(x, self.cash) + "\n"
        return self.cash

    def buyStock(self, amount, s):
        if type(s.price) is int:
            s.amount = s.amount + amount
            self.cash = self.cash - s.price * amount
            stockDict[s.ticker] = [s.ticker, s.price, s.amount]
            self.k = "\n" + self.k + "You bought {} shares of stock {}. Cash balance = {} ".format(amount, s.ticker,
                                                                                                   self.cash) + "\n"
        else:
            raise TypeError("You can only buy stocks if the price is an integer")  # Exception Raising

    def buyMutualFund(self, amount, m):
        m.amount = m.amount + amount
        self.cash = self.cash - m.price * amount
        fundDict[m.ticker] = [m.ticker, m.price, m.amount]
        self.k = "\n" + self.k + "You bought {} shares of mutual fund {}. Cash balance = {}".format(amount, m.ticker,
                                                                                                    self.cash) + "\n"

    def buyBond(self, b):
        self.cash = self.cash - b.facevalue
        b.amount = b.amount + 1
        bondDict[b.ticker] = [b.ticker, b.facevalue, b.maturity, b.amount]
        self.k = "\n" + self.k + "You bought {} Bond with facevalue {} and maturity {}. Cash balance = {}".format(
            b.ticker, b.facevalue, b.maturity, self.cash) + "\n"

    def sellStock(self, a, amount):
        for key in stockDict:
            if key == a and stockDict[key][2] != 0:  # stockDict[key][2] gives the amount you have of that stock
                self.cash = self.cash + random.uniform(0.5 * stockDict[key][1], 1.5 * stockDict[key][
                    1]) * amount  # stockDict[key][0] is the price of the stock
                stockDict[key][2] = stockDict[key][2] - amount
            elif key == a and stockDict[key][2] == 0:
                print("You dont have any more of this stock to sell!")
        self.k = "\n" + self.k + "You sold {} shares of stock {}. Cash balance = {}".format(amount, a, self.cash) + "\n"

    def sellMutualFund(self, a, amount):
        for key in fundDict:
            if key == a and fundDict[key][2] != 0:
                self.cash = self.cash + random.uniform(0.9, 1.2) * amount
                fundDict[key][2] = fundDict[key][2] - amount
            elif key == a and fundDict[key][2] == 0:
                print("You dont have any more of this mutual fund to sell!")
        self.k = "\n" + self.k + "You sold {} shares of mutual fund {}. Cash balance = {}".format(amount, a,
                                                                                                  self.cash) + "\n"


#    ------Testing for the application of the program------
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50)
portfolio.history()


# Bonus Part

print("\n \t \t \t \t -----BONUS PART----")
bonusportfolio =Portfolio()
bonusportfolio.addCash(200)
b1 = Bond(50, "DEF", 3)
b2 = Bond(70, "DKL", 10)
bonusportfolio.buyBond(b1)
bonusportfolio.buyBond(b2)
bonusportfolio.history()
print(bonusportfolio)