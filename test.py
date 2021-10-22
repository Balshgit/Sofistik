import asyncio
import time
from multiprocessing import Pool
# from loguru import logger
import sys, os
import random
import json
from sofistik.sofistik.utils import mirror_quad_by_y, logger


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
import json

data = {
    "10080": [(261.5, 147.0), (184.5, 102.0), (233.5, 51.0), (301.0, 77.0)],
    "10081": [(720.0, 318.0), (624.5, 265.5), (664.0, 175.0), (756.5, 239.0)]
}


data = mirror_quad_by_y(data)
logger.info(data)



