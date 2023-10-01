X = "X"
O = "O"
EMPTY = None

board = [[X, O, X],
            [X, O, EMPTY],
            [O, O, X]]

actions = set()

for i, row in enumerate(board):
    for j, item in enumerate(row):
        if item == EMPTY:
            actions.add((i, j))

xCount = 0
oCount = 0

for row in board:
    for item in row:
        if item == X: 
            xCount += 1
        if item == O: 
            oCount += 1

if xCount <= oCount:
    print(X, "turn")
else:
    print(O, "turn")

for row in board:
    for item in row:
        if item == EMPTY:
            print("Game not over")
print("Game over")

for row in board:
    if row[0] == row[1] == row[2]:
        print("Winner is", row[0])

for i in range(3):
    if board[0][i] == board[1][i] == board[2][i]:
        print("Winner is", board[0][i])

print(actions)