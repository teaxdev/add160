# OOP 2.4 Decorators

class TimingDecorator():
    def __init__(self, func):
        self.func = func

    def __call__(self, start_time, call_func, end_time, exec_time, result):
        self.start_time = start_time
        self.call_func = call_func
        self.end_time = end_time
        self.exec_time = exec_time
        self.result = result

@TimingDecorator
def compute(x):
    y = x^132
    print(y)

compute()