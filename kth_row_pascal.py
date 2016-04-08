def Ath_row_pascal(A):
    last_row = [1, 0]
    if A==0:
        return last_row[:len(last_row) - 1]
    for a in range(1, A + 1):
        current_row = [0]*(a + 2)
        for i in range(0, a + 1):
            if i == 0:
                current_row[i] = 1
            else:
                current_row[i] = last_row[i] + last_row[i - 1]
        last_row = current_row
    return current_row[:len(current_row) - 1]

print(Ath_row_pascal(0))
print(Ath_row_pascal(1))
print(Ath_row_pascal(2))
print(Ath_row_pascal(3))
print(Ath_row_pascal(4))
print(Ath_row_pascal(5))
