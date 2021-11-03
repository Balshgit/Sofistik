def hello():
    print("Hi")
    return "Hello World"


r1 = range(-10, -1)
r2 = range(-10, -12, -1)
r3 = range(-12, -17, -1)
r4 = range(-17, -20, -1)
to_find = -12

some_list = [r1, r2, r3, r4]


def search(item: int, list_to_check: list) -> list:
    for diapason in list_to_check:
        if item in diapason:
            return diapason

import re
ip = '192.168.88.147'
pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

if re.match(pattern, ip):
    print(True)

