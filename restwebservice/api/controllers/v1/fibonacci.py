from pecan import expose
from pecan import rest

from restwebservice.api.handlers import fibonacci_handler
from restwebservice.api.controllers.v1 import helper
import logging

logging.basicConfig(filename='fibonacci.log',level=logging.INFO)
logger = logging.getLogger(__name__)

class FibonacciController(rest.RestController):
    """ Controller class for fibonacci series web service."""

    MAX_NUM = 10000
    MIN_NUM = 1

    @expose('json')
    def get(self, num):
        """ Returns the fibonacci series of a given length."""
        logger.log(logging.INFO, 'Inside Fibonacci controller')
        json = {}
        handler = fibonacci_handler.FibonacciHandler()
        json_helper = helper.JSONHelper()
        n = int(num)

        if n in range(self.MIN_NUM, self.MAX_NUM+1):
            result = handler.get_fibonacci_series(n)
            status = 200
            json = json_helper.jsonify_response(status, "Fibonacci Series", result)
            logger.log(logging.INFO, 'Fibonacci Series %s'  %result)
            
        else:
            error = 'Number should be in the range %s-%s' %(self.MIN_NUM, self.MAX_NUM)
            status = 422
            json = {'Error' : error}
            json = json_helper.jsonify_response(status, "Error", error)
            logger.log(logging.ERROR, error)
        return json



