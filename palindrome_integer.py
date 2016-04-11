def isIntegerPalindrome(A):
    A = str(A)
    B = reversed(A)
    C = zip(A, B)

    for (a, b) in C:
        if a != b:
            return False
    return True
