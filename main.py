
from functools import reduce


def getMaxSum(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    maxsum = lambda x, y: x + max(y)
    # maxsum = lambda x, y: x + y

    # ret = reduce(maxsum, map(max, numbers))
    ret = reduce(maxsum, numbers, 0)
    return ret


def main():
    mylist = [[1, 2, 3, 4, 5],
              [10, 20, 30, 40, 50],
              [100, 200, 1000]
              ]
    # mylist = [1, 2, 3]
    ret = getMaxSum(mylist)
    print(f'Return value is {ret}')


if __name__ == '__main__':
    main()
