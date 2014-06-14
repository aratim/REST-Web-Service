from restwebservice.api.handlers import fibonacci_handler
import unittest

class TestFibonacciHandler(unittest.TestCase):

    def test_get_fibonacci_series(self):
        handler = fibonacci_handler.FibonacciHandler()
        response = handler.get_fibonacci_series(5)
        series = [0,1,1,2,3]
        self.assertEqual(response, series)
