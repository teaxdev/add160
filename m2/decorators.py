# OOP 2.4 Decorators

import time, math
class TimingDecorator():
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        start_time = time.time() 
        call_func = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return call_func
        # result = call_func

@TimingDecorator
def compute(x):
    y = math.factorial(x)
    print(f"Output: {y}")

compute(123)