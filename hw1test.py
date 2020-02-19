import unittest
import hw1code

class mytest(unittest.TestCase):

    def test_one(self):
        portfolio = hw1code.Portfolio()
        s = hw1code.Stock(20, "HFH")
        portfolio.buyStock(5, s)
        result = portfolio.cash
        self.assertEqual(result, -100)

    def test_two(self):
        portfolio = hw1code.Portfolio()
        portfolio.addCash(300.50)
        s = hw1code.Stock(20, "HFH")
        portfolio.buyStock(5, s)
        mf1 = hw1code.MutualFund("BRT")
        mf2 = hw1code.MutualFund("GHT")
        portfolio.buyMutualFund(10.3, mf1)
        portfolio.buyMutualFund(2, mf2)
        portfolio.sellMutualFund("BRT", 3)
        result = mf1.amount
        self.assertEqual(result, 10.3)


if __name__ == '__main__':
    unittest.main()
