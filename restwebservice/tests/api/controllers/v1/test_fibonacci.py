import mock
import unittest

from restwebservice.api.controllers.v1 import fibonacci
from restwebservice.api.handlers import fibonacci_handler


class TestFibonacciController(unittest.TestCase):

    def test_fibonacci_get(self):
        controller = fibonacci.FibonacciController()
        handler = fibonacci_handler.FibonacciHandler()
        handler.get_fibonacci_series = mock.MagicMock
        series = [0,1,1,2,3]
        handler.get_fibonacci_series.return_value = series
        response = controller.get(5)
        self.assertEqual(response['body']['Fibonacci Series'], series)

    def test_fibonacci_get_error(self):
        controller = fibonacci.FibonacciController()
        response = controller.get(-5)
        err = 'Number should be in the range 1-10000'
        self.assertEqual(response['body']['Error'], err)
