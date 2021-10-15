import random
import time


board_cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
moves = []

def clear_board():
    for i in range(9):
        board_cells[i] = ' '


def print_board():
    print('---------')
    print(f'| {" ".join(board_cells[:3])} |')
    print(f'| {" ".join(board_cells[3:6])} |')
    print(f'| {" ".join(board_cells[6:])} |')
    print('---------')


def enter_coordinates(row, column):
    numbers = [1, 2, 3]

    if row in numbers and column in numbers:
        return check_occupied(3 * (row - 1) + column - 1)
    else:
        print('Coordinates should be from 1 to 3!')
        return False


def make_move(index):
    return check_occupied(index)


def check_turn():
    number_of_x = board_cells.count('X')
    number_of_o = board_cells.count('O')
    turn = 'X'

    if number_of_x <= number_of_o:
        turn = 'X'
    else:
        turn = 'O'
    return turn


def check_occupied(cell_index):
    turn = check_turn()

    if board_cells[cell_index] != " ":
        print('This cell is occupied! Choose another one!')
        return False
    else:
        board_cells[cell_index] = turn
    print_board()
    return True


def check_result():
    x_wins = False
    o_wins = False
    empty_cells = 0

    diagonal_a = board_cells[::4]
    diagonal_b = board_cells[2:7:2]
    row_1 = board_cells[:3]
    row_2 = board_cells[3:6]
    row_3 = board_cells[6:]
    column_1 = board_cells[:7:3]
    column_2 = board_cells[1:8:3]
    column_3 = board_cells[2::3]

    if diagonal_a.count('X') == 3 or diagonal_b.count('X') == 3:
        x_wins = True

    if diagonal_a.count('O') == 3 or diagonal_b.count('O') == 3:
        o_wins = True

    if row_1.count('X') == 3 or row_2.count('X') == 3 or row_3.count('X') == 3:
        x_wins = True

    if row_1.count('O') == 3 or row_2.count('O') == 3 or row_3.count('O') == 3:
        o_wins = True

    if column_1.count('X') == 3 or column_2.count('X') == 3 or column_3.count('X') == 3:
        x_wins = True

    if column_1.count('O') == 3 or column_2.count('O') == 3 or column_3.count('O') == 3:
        o_wins = True

    empty_cells = board_cells.count(' ')

    if x_wins:
        print('X wins')
        return True
    elif o_wins:
        print('O wins')
        return True

    if empty_cells == 0:
        print('Draw')
        return True

    return False


def make_move_row(row):
    for i in range(3):
        if board_cells[3 * row + i] == ' ':
            make_move(3 * row + i)
            break


def make_move_column(column):
    for i in range(column, 9, 3):
        if board_cells[i] == ' ':
            make_move(i)
            break


def make_move_diagonal(diagonal):
    if board_cells[4] == ' ':
        make_move(4)
    if diagonal == 1:
        if board_cells[0] == ' ':
            make_move(0)
        else:
            make_move(8)
    else:
        if board_cells[2] == ' ':
            make_move(2)
        else:
            make_move(6)


def computer_move(level):
    turn = check_turn()
    legal_moves = []

    if turn == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    for z in range(9):
        if board_cells[z] == ' ':
            legal_moves.append(z)

    if level == 'easy':
        print('Making move level "easy"')
        move = random.choice(legal_moves)
        make_move(move)
    elif level == 'medium':
        print('Making move level "medium"')
        diagonal_a = board_cells[::4]
        diagonal_b = board_cells[2:7:2]
        row_1 = board_cells[:3]
        row_2 = board_cells[3:6]
        row_3 = board_cells[6:]
        column_1 = board_cells[:7:3]
        column_2 = board_cells[1:8:3]
        column_3 = board_cells[2::3]

        if diagonal_a.count(turn) == 2 and diagonal_a.count(' '):
            make_move_diagonal(1)
        elif diagonal_b.count(turn) == 2 and diagonal_b.count(' '):
            make_move_diagonal(2)
        elif row_1.count(turn) == 2 and row_1.count(' '):
            make_move_row(0)
        elif row_2.count(turn) == 2 and row_2.count(' '):
            make_move_row(1)
        elif row_3.count(turn) == 2 and row_3.count(' '):
            make_move_row(2)
        elif column_1.count(turn) == 2 and column_1.count(' '):
            make_move_column(0)
        elif column_2.count(turn) == 2 and column_2.count(' '):
            make_move_column(1)
        elif column_3.count(turn) == 2 and column_3.count(' '):
            make_move_column(2)
        elif diagonal_a.count(opponent) == 2 and diagonal_a.count(' '):
            make_move_diagonal(1)
        elif diagonal_b.count(opponent) == 2 and diagonal_b.count(' '):
            make_move_diagonal(2)
        elif row_1.count(opponent) == 2 and row_1.count(' '):
            make_move_row(0)
        elif row_2.count(opponent) == 2 and row_2.count(' '):
            make_move_row(1)
        elif row_3.count(opponent) == 2 and row_3.count(' '):
            make_move_row(2)
        elif column_1.count(opponent) == 2 and column_1.count(' '):
            make_move_column(0)
        elif column_2.count(opponent) == 2 and column_2.count(' '):
            make_move_column(1)
        elif column_3.count(opponent) == 2 and column_3.count(' '):
            make_move_column(2)
        else:
            move = random.choice(legal_moves)
            make_move(move)
    elif level == 'hard':
        print('Making move level "hard"')
        if turn == 'X':
            score = -2
        else:
            score = 2
        move = -1

        for i in range(len(board_cells)):
            if board_cells[i] == " ":
                if turn == 'X':
                    board_cells[i] = turn
                    curr_score = minimax(board_cells, False)
                    board_cells[i] = " "
                    if curr_score > score:
                        score = curr_score
                        move = i
                else:
                    board_cells[i] = turn
                    curr_score = minimax(board_cells, True)
                    board_cells[i] = " "
                    if curr_score < score:
                        score = curr_score
                        move = i
        make_move(move)


def minimax(new_board, is_this_ais_turn):
    if winning(new_board, 'X'):
        return 1
    elif winning(new_board, 'O'):
        return -1
    elif check_draw(new_board):
        return 0

    if is_this_ais_turn:
        score = -2 
        for i in range(len(new_board)):
            if new_board[i] == " ":
                new_board[i] = 'X'
                curr_score = minimax(new_board, False)
                new_board[i] = " "
                score = max(score, curr_score)
        return score
    else:
        score = 2
        for i in range(len(new_board)):
            if new_board[i] == " ":
                new_board[i] = 'O'
                curr_score = minimax(new_board, True)
                new_board[i] = " "
                score = min(score, curr_score)
        return score


def winning(board, player):
    if (
            (board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False


def check_draw(board):
    return board.count(' ') == 0


commands = ['start', 'exit', 'easy', 'medium', 'hard', 'user']
command = ''
while command != 'exit':
    clear_board()
    time.sleep(1)
    print('Input command: ')
    command = input().split()
    if command[0] == 'exit':
        break
    if len(command) == 3 and command[0] == 'start' and command[1] in commands and command[2] in commands:
        if command[1] == 'easy' and command[2] == 'easy':
            # clear_board()
            while True:
                if check_result():
                    break
                computer_move('easy')
        elif command[1] == 'medium' and command[2] == 'medium':
            # clear_board()
            while True:
                if check_result():
                    break
                computer_move('medium')
        elif command[1] == 'hard' and command[2] == 'hard':
            while True:
                if check_result():
                    break
                computer_move('hard')
        elif command[1] == 'user' and command[2] == 'user':
            # clear_board()
            print_board()
            while True:
                if check_result():
                    break
                try:
                    coordinates_input = input('Enter the coordinates: ').split()
                    if len(coordinates_input) != 2:
                        raise Exception
                    x = int(coordinates_input[0])
                    y = int(coordinates_input[1])
                    is_move_good = enter_coordinates(x, y)
                except Exception:
                    print('You should enter numbers!')
        else:
            # clear_board()
            print_board()
            computer_first = False
            play_level = command[1]
            if command[1] == 'easy' or command[1] == 'medium' or command[1] == 'hard':
                computer_first = True
            else:
                play_level = command[2]
            while True:
                if check_result():
                    break
                try:
                    if computer_first:
                        computer_first = False
                        computer_move(play_level)
                    coordinates_input = input('Enter the coordinates: ').split()
                    if len(coordinates_input) != 2:
                        raise Exception
                    x = int(coordinates_input[0])
                    y = int(coordinates_input[1])
                    is_move_good = enter_coordinates(x, y)
                    if is_move_good:
                        if check_result():
                            break
                        else:
                            computer_move(play_level)
                except Exception:
                    print('You should enter numbers!')
    else:
        print('Bad parameters!')



