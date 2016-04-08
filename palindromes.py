def is_palindrome(s):
    lower_s = s.lower()
    i = 0
    j = len(lower_s) - 1

    while i < j:
        p1 = lower_s[i]
        p2 = lower_s[j]
        if not p1 == p2:
            return False
        i = i + 1
        j = j - 1
    return True

assert is_palindrome("dad") == True
assert is_palindrome("eahofhfohae") == True
assert is_palindrome("palindrome") == False
print ("Passed all tests.")
