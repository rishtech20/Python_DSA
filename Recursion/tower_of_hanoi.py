"""
Author: Rishabh Madan
Problem: Tower of Hanoi using Recursion
"""


def toh(n, rod_from, rod_aux, rod_to):
    if n == 1:
        print(f"Move {n} from {rod_from} to {rod_to}")
        return

    toh(n-1, rod_from, rod_to, rod_aux)

    print(f"Move {n} from {rod_from} to {rod_to}")

    toh(n-1, rod_aux, rod_from, rod_to)


if __name__ == "__main__":
    n = input("Enter the number of the plates: ")
    toh(int(n), 'A', 'B', 'C')
