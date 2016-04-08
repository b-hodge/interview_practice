def find_sub_arrays(A):
	i = 0
	sub_arrays = []
	while i < len(A):
		s = []
		j = 0
		while i+j < len(A) and A[i+j] >= 0:
			s.append(A[i+j])
			j += 1
		i = i+j+1
		if s:
			sub_arrays.append(s)
		#print(sub_arrays)
	return sub_arrays

A = [1, 2, 5, -7, 2, 3]
#print(find_sub_arrays(A))
sub_arrays = find_sub_arrays(A)

def get_max_sub_array(sub_arrays):
	m = 0
	r = []
	for s in sub_arrays:
		t = 0
		for a in s:
			t += a
		if t > m:
			m = t
			r = s
		if t == m:
			if len(s) > len(r):
				r = s
	return r

print(get_max_sub_array(sub_arrays))

