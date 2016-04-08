def first_A_pascal_rows(A):
    row_accumulator = []
    last_row = [1, 0]
    row_accumulator.append(last_row[:len(last_row) - 1])
    if A==0:
        return last_row[:len(last_row) - 1]
    for a in range(1, A ):
        current_row = [0]*(a + 2)
        for i in range(0, a + 1):
            if i == 0:
                current_row[i] = 1
            else:
                current_row[i] = last_row[i] + last_row[i - 1]
        last_row = current_row
        row_accumulator.append(current_row[:len(current_row) - 1])

    return row_accumulator

print( first_A_pascal_rows(5) )

