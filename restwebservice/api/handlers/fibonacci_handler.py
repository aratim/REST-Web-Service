
class FibonacciHandler(object):

    def get_fibonacci_series(self, num):
        result = []

        for i in range(num):
            result.append(self._fibo(i))
        return result
            
    def _fibo(self, num):
        if num==0:
            return 0
        elif num==1:
            return 1
        else:
            return self._fibo(num-2) + self._fibo(num-1)
