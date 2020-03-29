"""
Author: Rishabh Madan
Problem: Implementation of the calculation of nth Fibonacci number using recursion
"""

# Head Recursion Implementation


def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    subresult1 = fib(n-1)
    subresult2 = fib(n-2)

    result = subresult2 + subresult1

    return result

# Tail recursion implementation


def fib_tail(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return fib_tail(n-1, b, a+b)


if __name__ == "__main__":
    n = int(input("Enter a number to get a Fibonacci number: "))
    print(f'{n}th Fibonacci number is {fib_tail(n)}')
