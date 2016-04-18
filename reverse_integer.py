# Reverses the digits of the given integer, x
# If x is negative, keep the - sign at the beginning of the sequence
# If the reversed number can't fit in a 32-bit signed integer, return 0
# Max number in a 32-bit signed int is (2^31) - 1
def reverse_integer(x):
    negative = False
    if x < 0:
        x = int(str(x)[1:])
        negative = True

    max_val = (2**31) - 1
    x_rev = int(str(x)[::-1])
    if x_rev > max_val:
        return 0

    if negative:
        x_rev = "-" + str(x_rev)

    return x_rev