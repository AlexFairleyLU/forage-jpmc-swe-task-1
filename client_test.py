import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, (120.48+121.2)/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 119.2, (120.48+119.2)/2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
     testPricea = 100
     testPriceb = 50
     self.assertEqual(getRatio(testPricea, testPriceb), 2)
  
  def test_getRatio_calculateRatioBisZero(self):
     testPricea = 100
     testPriceb = 0
     self.assertEqual(getRatio(testPricea, testPriceb), None)
  
  def test_getRatio_calculateRatioAisZero(self):
     testPricea = 0
     testPriceb = 50
     self.assertEqual(getRatio(testPricea, testPriceb), 0)


if __name__ == '__main__':
    unittest.main()
