import asyncio
import time
from multiprocessing import Pool
# from loguru import logger
import sys, os
import random
import json


# logger.remove()
# logger.add(sys.stdout, colorize=True, format="{time} <green>{message}</green>", level='INFO')


# def time_execute(func):
#     def new_func(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         dt = end - begin
#         logger.info(f'{func.__name__} ended its work: in {round(dt,2)} seconds.')
#     return new_func


