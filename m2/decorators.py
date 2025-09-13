# OOP 2.4 Decorators

class TimingDecorator():
    def __init__(self, func, start_time, end_time):
        self.func = func
        self.start_time = start_time
        self.end_time = end_time

    def __call__(self, *args, **kwargs):
        start_time = self.start_time.time() 
        call_func = self.func(*args, **kwargs)
        end_time = self.end_time.time()
        print(f"Function {self.func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return call_func
        # result = call_func

@TimingDecorator
def compute(x):
    y = x^132
    print(y)

compute()