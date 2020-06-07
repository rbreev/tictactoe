def print_board():
    global fields
    print(f"""---------
| {fields[0][2]} {fields[1][2]} {fields[2][2]} |
| {fields[0][1]} {fields[1][1]} {fields[2][1]} |
| {fields[0][0]} {fields[1][0]} {fields[2][0]} |
---------""")


def transfer_coordinates(coordinates):
    if coordinates == [1, 1]:
        return [0, 0]
    elif coordinates == [1, 2]:
        return [0, 1]
    elif coordinates == [1, 3]:
        return [0, 2]
    elif coordinates == [2, 1]:
        return [1, 0]
    elif coordinates == [2, 2]:
        return [1, 1]
    elif coordinates == [2, 3]:
        return [1, 2]
    elif coordinates == [3, 1]:
        return [2, 0]
    elif coordinates == [3, 2]:
        return [2, 1]
    elif coordinates == [3, 3]:
        return [2, 2]


def input_coordinates():
    global fields
    global step
    while True:
        coordinates = input("Enter the coordinates: ").split()
        try:
            coordinates = [int(i) for i in coordinates]
        except ValueError:
            print("You should enter numbers!")
            continue
        if len(coordinates) != 2:
            print("Please input two coordinates")
            continue
        elif coordinates[0] > 3 or coordinates[1] > 3 or coordinates[0] < 1 or coordinates[1] < 1:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            coordinates = transfer_coordinates(coordinates)
            if fields[coordinates[0]][coordinates[1]] == "X" or fields[coordinates[0]][coordinates[1]] == "O":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                if step % 2 == 0:
                    fields[coordinates[0]][coordinates[1]] = "O"
                    step += 1
                    break
                else:
                    fields[coordinates[0]][coordinates[1]] = "X"
                    step += 1
                    break


def result():
    global fields
    global step
    win_x = 0
    win_o = 0
    count_space = sum(x.count(" ") for x in fields)
    # columns
    for i in range(3):
        if fields[0][i] == fields[1][i] == fields[2][i] != " ":
            if fields[0][i] == "X":
                win_x += 1
            elif fields[0][i] == "O":
                win_o += 1
    # rows
    for i in range(3):
        if fields[i][0] == fields[i][1] == fields[i][2] != " ":
            if fields[i][0] == "X":
                win_x += 1
            elif fields[i][0] == "O":
                win_o += 1
    # diagonals
    if fields[0][0] == fields[1][1] == fields[2][2] != " ":
        if fields[0][0] == "X":
            win_x += 1
        elif fields[0][0] == "O":
            win_o += 1
    if fields[0][2] == fields[1][1] == fields[2][0] != " ":
        if fields[0][2] == "X":
            win_x += 1
        elif fields[0][2] == "O":
            win_o += 1

    if win_x == 1 and win_o == 0:
        print("X wins")
        return "end"
    elif win_x == 0 and win_o == 1:
        print("O wins")
        return "end"
    elif count_space == 0 and win_x == 0 and win_o == 0:
        print("Draw")
        return "end"
    elif count_space != 0 and win_x == 0 and win_o == 0:
        print()


fields = [[" " for i in range(3)] for j in range(3)]
step = 1
status = ""
print_board()
while True:
    input_coordinates()
    print_board()
    status = result()
    if status == "end":
        break
    continue
