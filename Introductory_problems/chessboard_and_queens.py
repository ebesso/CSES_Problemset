chessboard = []

for i in range(8):
    row = list(input())
    parsed_row = []
    for j in range(8):
        if row[j] == '.':
            parsed_row.append(True)
        else:
            parsed_row.append(False)
    chessboard.append(parsed_row)

occupied_columns = [False] * 8
occupied_rows = [False] * 8
occupied_diags_1 = set()
occupied_diags_2 = set()

def rec(n, r): 
    if n == 8:
        return 1
    if r > 7:
        return 0
    count = 0
    for j in range(8):
        if chessboard[r][j] and not occupied_rows[r] and not occupied_columns[j] and r - j not in occupied_diags_1 and j + r not in occupied_diags_2:
            occupied_rows[r] = True
            occupied_columns[j] = True
            occupied_diags_1.add(r - j)
            occupied_diags_2.add(j + r)
            count += rec(n + 1, r + 1)
            occupied_rows[r] = False
            occupied_columns[j] = False 
            occupied_diags_1.remove(r - j)
            occupied_diags_2.remove(j + r)
                
    return count
    
print(rec(0, 0))
