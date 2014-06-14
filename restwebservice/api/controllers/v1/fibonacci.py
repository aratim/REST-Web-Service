from restwebservice.api.handlers import fibonacci_handler
from pecan import expose
from pecan import rest

class FibonacciController(rest.RestController):


    MAX_NUM = 10000
    MIN_NUM = 1

    @expose('json')
    def get(self, num):
        json = {}
        handler = fibonacci_handler.FibonacciHandler()
        n = int(num)
        if n<self.MAX_NUM and n>=self.MIN_NUM:
            result = handler.get_fibonacci_series(n)
            json = {'Fibonacci series' : result}
        else:
            error = 'Number should be in the range %s-%s' %(self.MIN_NUM, self.MAX_NUM)
            json = {'Error' : error}
        return json

