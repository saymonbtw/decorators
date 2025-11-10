def print_field(board: list) -> None:
    print("\nИгровое поле:")
    print("   1   2   3")
    for i, row in enumerate(board, start=1):
        print(i, " " + " | ".join(row))
        if i < 3:
            print("  ---+---+---")
    print()


def has_won(board: list, mark: str) -> bool:
    n = len(board)

    if any(all(elem == mark for elem in row) for row in board):
        return True

    if any(all(board[r][c] == mark for r in range(n)) for c in range(n)):
        return True

    if all(board[i][i] == mark for i in range(n)):
        return True

    if all(board[i][n - 1 - i] == mark for i in range(n)):
        return True

    return False


x_player = input("Имя игрока за крестики -> ")
o_player = input("Имя игрока за нолики -> ")

playing_field = [[" " for _ in range(3)] for _ in range(3)]

def has_free_points(board: list) -> bool:
    if any(any(elem == " " for elem in row) for row in board):
        return True
    return False

current_player = x_player
current_sing = "X"
move = 1
while not(has_won(playing_field, "X")) and not(has_won(playing_field, "O")) and has_free_points(playing_field):

    if move % 2 != 0:
        current_player = x_player
        current_sing = "X"
    else:
        current_player = o_player
        current_sing = "O"

    print_field(playing_field)
    print(f"{current_player} ходит знаком {current_sing}")

    while True:
        x, y = list(map(int, input("Введите координаты x и y для хода через пробел -> ").split()))
        if not(1 <= x <= 3 and 1 <= y <= 3):
            print("Координаты должны быть от 1 до 3!")
            continue

        if playing_field[x - 1][y - 1] != " ":
            print("Место занято!")
            continue

        break

    playing_field[x - 1][y - 1] = current_sing

    move += 1

if has_won(playing_field, "X"):
    print(f"\nВыиграл {x_player}!")
    print_field(playing_field)
elif has_won(playing_field, "O"):
    print(f"\nВыиграл {o_player}!")
    print_field(playing_field)
else:
    print(f"\nНичья!")
    print_field(playing_field)
