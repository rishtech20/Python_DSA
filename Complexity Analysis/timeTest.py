"""
Author: Rishabh Madan
"""
from random import randint
from random import seed
from functools import reduce
from timeit import default_timer as timer


def add_one(a):
    return 1 + a[0]


def sum(a):
    return reduce((lambda x, y: x + y), a)


def pair(a):
    pairs = []
    for i in range(len(a)):
        for j in range(len(a)):
            pairs.append((a[i], a[j]))
    return pairs


if __name__ == "__main__":
    n = int(input("Enter the size of the array to run the test: "))
    seed(0.1232418394234)
    arr = [randint(0, 10) for _ in range(n)]

    start = timer()
    add_one(arr)
    end = timer()
    print(f"add_one: {end-start}")

    start = timer()
    sum(arr)
    end = timer()
    print(f"sum: {end - start}")

    start = timer()
    pair(arr)
    end = timer()
    print(f"pair: {end - start}")
