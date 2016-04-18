def gcd(m, n):
    if m < n:
        temp = m
        m = n
        n = temp
    # gross
    while True:
        r = m % n
        if r == 0:
            return n
        m = n
        n = r

