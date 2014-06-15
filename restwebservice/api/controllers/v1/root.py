from pecan import expose, request
from webob.exc import status_map
from restwebservice.api.controllers.v1 import fibonacci

class RootController(object):

    fibonacci = fibonacci.FibonacciController()
    
    @expose('json')
    def index(self):
        msg = "Welcome to REST Web service"
        return msg

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
