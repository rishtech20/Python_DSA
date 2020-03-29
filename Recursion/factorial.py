"""
Author: Rishabh Madan
Problem: Implementation of Factorial using recursion
"""

# Head recursion implementation


def factorial(n):
    if n < 1:
        return 1

    subresult = factorial(n - 1)

    return n * subresult

# Tail recursion implementation - Better way


def factorial_head(n, result):
    if n == 1:
        return result

    return factorial_head(n-1, n * result)


if __name__ == "__main__":
    n = input("Enter the number to calculate the factorial: ")
    print(f'{n}! = {factorial(int(n))}')
