import time
from functools import wraps

class Timer:
    def __init__(self, num_runs=10):
        self.num_runs = num_runs

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            for run in range(self.num_runs):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                current_run_time = (end - start)
                total_time += current_run_time
            average_time = total_time / self.num_runs
            
            print('Среднее время выполнения функции %s за %s запусков - %.5f секунд' % (func.__name__, self.num_runs, average_time))
            return func(*args, **kwargs)
        return wrapper

    def __enter__(self):
        self.t0 = time.time()
        return self

    def __exit__(self, *args, **kwargs):
        t1 = time.time()
        runtime = (t1-self.t0)
        average_time = runtime / self.num_runs
        print('Среднее время выполнения функции за %s запусков - %5f' % (self.num_runs, average_time))

#используем как декоратор
@Timer(1000)
def fibonacci_strings(a, b):
    fibonachy_list = [a, b]
    summa_chetnih = 0
    while fibonachy_list[len(fibonachy_list) - 1] < 40000:
        fibonachy_list.append(fibonachy_list[len(fibonachy_list) - 1] + fibonachy_list[len(fibonachy_list) - 2])

    print(fibonachy_list)
    print(fibonachy_list[len(fibonachy_list) - 2])

    for i in fibonachy_list:
        if i % 2 == 0:
            summa_chetnih += i
    print(summa_chetnih)

fibonacci_strings(1, 2)

#используем как контекстный менеджер
def sum_of_numder_in_interval (a, b):
    sum_ = 0
    for number_ in range (a, b+1):
        sum_ += number_
    print(sum_)

with Timer(100) as timer:
    for run_ in range(timer.num_runs):
        sum_of_numder_in_interval(1, 400)
