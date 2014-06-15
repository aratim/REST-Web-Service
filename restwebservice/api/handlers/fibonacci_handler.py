

class FibonacciHandler(object):
    """ Handler class for fibonacci series web service."""

    fib_table = {}
    fib_table[0] = 0
    fib_table[1] = 1

    def get_fibonacci_series(self, num):
        """ Generates the fibonacci series of a given length."""

        result = []
        for i in range(num):
            result.append(self._fibo(i))
        return result

    def _fibo(self, num):
        """ Recursive function which uses dynamic programming"""

        if num in self.fib_table:
            return self.fib_table[num]
        else:
            self.fib_table[num] = self._fibo(num-1) + self._fibo(num-2)
            return self.fib_table[num]
