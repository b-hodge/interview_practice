# HOORAY PYTHON!!
def reverse_string_slice(s) :
	return s[::-1]

# But for real
def reverse_string(s):
    # convert to list for mutability
    s = list(s)
    head_index = 0
    tail_index = len(s) - 1
    while head_index < tail_index:
        # swap needs a temp variable
        temp = s[head_index]
        s[head_index] = s[tail_index]
        s[tail_index] = temp
        head_index += 1
        tail_index -= 1
    return ''.join(s)

print(reverse_string_slice("string"))
print(reverse_string("string"))
