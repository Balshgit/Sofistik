import asyncio
import time
from multiprocessing import Pool
# from loguru import logger
import sys, os
import random


# logger.remove()
# logger.add(sys.stdout, colorize=True, format="{time} <green>{message}</green>", level='INFO')


def time_execute(func):
    def new_func(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        dt = end - begin
        logger.info(f'{func.__name__} ended its work: in {round(dt,2)} seconds.')
    return new_func


#@time_execute
def counter(num: int) -> None:

    random_number = 2  # random.randint(3, 5)
    number = 3 ** (random_number * 1000000)
    logger.info(f'Event{num} ended its work! | '
                f'Last ten digits {str(number)[-10:]} | Random number was: {random_number}')
    return number

# counter(1)


@time_execute
def main():
    process = Pool(processes=2)
    calc_nums = [i for i in range(1, 3)]
    process.map(counter, calc_nums)
    process.close()


# main()
result = 100
x = 1111 & result
print(x)



