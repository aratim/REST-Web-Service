import unittest
from restwebservice.api.controllers.v1 import fibonacci
from restwebservice.api.handlers import fibonacci_handler
import mock

class TestFibonacciController(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_fibonacci_get(self):
        controller = fibonacci.FibonacciController()
        handler = fibonacci_handler.FibonacciHandler()
        handler.get_fibonacci_series = mock.MagicMock
        series = [0,1,1,2,3]
        handler.get_fibonacci_series.return_value = series
        response = controller.get(5)
        self.assertEqual(response['Fibonacci series'], series) 
    
    def test_fibonacci_get_error(self):
        controller = fibonacci.FibonacciController()
        response = controller.get(-5)
        #self.assertEqual(response['Fibonacci series'], series)