"""
Author: Rishabh Madan
Problem: To reverse a string
"""

# Head recursion implementation


def rev_string(str):
    str_len = len(str)

    if str_len < 1:
        return str

    rev_substring = rev_string(str[1:])
    temp = str[0]

    reversed_string = rev_substring + temp

    return reversed_string


if __name__ == "__main__":
    str = input("Enter a string: ")
    print(f"The reversed string is '{rev_string(str)}'")
