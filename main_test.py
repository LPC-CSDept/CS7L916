import main
import io
import sys
import re
import math
import types


def test_main_1():
    numbers = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [100, 200, 1000]]
    ret = main.getMaxSum(numbers)
    print(f'Return value is {ret}')
    assert ret == 1055


def test_main_2():
    numbers = [[1, 2, 3, 4, 5],
               [5, 4, 3, 2, 1],
               [100, 200, 300]]
    ret = main.getMaxSum(numbers)
    print(f'Return value is {ret}')
    assert ret == 310
