"""
Author: Rishabh Madan
Problem: To determine if a given String is a Palindrome or not using recursion
"""


def isPalindrome(str, s, e):
    str_len = len(str)

    if str_len == 1 or str_len == 0:
        return 1
    elif s != e:
        return 0

    return isPalindrome(str[1:str_len-1], str[1], str[str_len-2])


if __name__ == "__main__":
    str = input("Enter a String: ")
    print(
        f'{str} is {"a Palindrome" if isPalindrome(str, str[0], str[len(str) - 1]) == 1 else "not a Palindrome"}')
