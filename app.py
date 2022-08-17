def matrix_contains(matrix, val):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == val:
                return True
    return False  # gone through everything and it's not there


coord_map = {
    "a": 0,
    "b": 1,
    "c": 2
}
board_values = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
board_format = f"      1   2   3\n    -------------\n  A | {board_values[0][0]} | {board_values[0][1]} | {board_values[0][2]} |\n    |-----------|\n" \
               f"  B | {board_values[1][0]} | {board_values[1][1]} | {board_values[1][2]} |\n    |-----------|\n  C | {board_values[2][0]} | {board_values[2][1]} | {board_values[2][2]} |\n    ------------- "
turn_count = 0
state = "X"
victory = False

print("Instructions: \nType in the coordinates of your mark to place it down.\n"
      "For example, if I wanted to place my mark in the A1 square, I would input \"a1\".\n"
      "X goes first.\n")
print(board_format + "\n")

# Inputs values until the board is full or a player wins
while matrix_contains(board_values, " ") and victory == False:
    if turn_count % 2 == 0:
        print("X's turn.")
        state = "X"
    else:
        print("O's turn.")
        state = "O"

    while True:
        coords = input("Input coordinates: ").strip().lower()
        try:
            row = coord_map.get(coords[0])
            col = int(coords[1]) - 1
            if len(coords) == 2 and col < 3 and row < 3 and board_values[row][col] == " ":  # if a valid coord
                board_values[row][col] = state
                break
            else:
                print("Invalid coordinates, please re-input.")
        except:
            print("Invalid coordinates, please re-input.")

    # Check for conditions
    # Rows
    for i in range(3):
        if all(p == state for p in board_values[i]):
            print(state + " wins!")
            victory = True
            break

    # Columns
    for i in range(3):
        col = [board_values[0][i], board_values[1][i], board_values[2][i]]
        if all(p == state for p in col):
            print(state + " wins!")
            victory = True
            break

    # Diagonals
    if board_values[0][0] == state and board_values[1][1] == state and board_values[2][2] == state:
        print(state + " wins!")
        victory = True
    elif board_values[2][0] == state and board_values[1][1] == state and board_values[0][2] == state:
        print(state + " wins!")
        victory = True

    print(f"\n      1   2   3\n    -------------\n  A | {board_values[0][0]} | {board_values[0][1]} | {board_values[0][2]} |\n    |-----------|\n" \
        f"  B | {board_values[1][0]} | {board_values[1][1]} | {board_values[1][2]} |\n    |-----------|\n  C | {board_values[2][0]} | {board_values[2][1]} | {board_values[2][2]} |\n    ------------- \n")

    turn_count += 1

if victory:
    print(state + " wins!")
else:
    print("Cat's game! Better luck next time 😼")