#! /usr/bin/python3


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board():
    """چاپ کردن برد"""
    print(40 * "_")
    j = 1
    for i in board:
        end = "  "
        if j % 3 == 0:
            end = "\n\n"
        print(f"[{i}]", end=end)
        j += 1


print("player = X\ncomputer = O")


def player_move(b):
    """گرفتن حرکت کاربر و اعمال رو برد"""
    pl_move = int(input("it's your turn!\nchoose a number between(1,9) :"))
    if 1 <= pl_move <= 9:
        if board[pl_move - 1] == "O":
            print("invalid")
            player_move(b)
        else:
            board[pl_move - 1] = "X"
    else:
        print("invalid")
        player_move(board)


def has_empty_place(bord):
    """جا خالی تو برد هست یا نه؟"""
    return bord.count("X") + bord.count("O") != 9


win_ways = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def player_winner(bord):
    """حالات برد کاربر"""
    for tuple1 in win_ways:
        if bord[tuple1[0]] == "X" and bord[tuple1[1]] == "X" and bord[tuple1[2]] == "X":
            return True


def can_comp_move(bord, m):
    """بررسی اینکه کامپیوتر میتونه حرکت کنه یا نه"""
    if board[m - 1] == "X":
        return False
    elif board[m - 1] == "O":
        return False
    return True


def can_comp_move_player(bord, m):
    """اسمش یکم عجیبه اما بجا...در حرکت کامپیوتر باید جلو برد کاربر رو بگیره برا این کار باید پیدا کنه
    حالات برد کاربر رو این تابع تو بخش دوم تابع حرکت کامپیوتر استفاده میشه"""
    if board[m - 1] == "O":
        return False
    elif board[m - 1] == "X":
        return False
    return True


computer_moving = (5, 1, 3, 7, 9, 2, 4, 6, 8)


def computer_move(bord):
    """حرکت کامپیوتر که اولا باید اگر خودش توانایی بردن رو داره ببره و اگر کاربر داره میبره جلو بردنشو بگیره و در
    نهایت طبق الگوریتم تعریف شده عمل کنه"""
    x = 0
    if copm_can_win(bord):
        print("Computer wins!")
    elif player_can_win(board):
        for a in range(1, 10):
            if can_comp_move_player(board, a) and x == 1:
                board[a - 1] = "X"
                if player_winner(board):
                    board[a - 1] = "O"
                    x += 1
                    break

                elif not player_winner(board):
                    board[a - 1] = a

    elif not copm_can_win(bord) and not player_can_win(board):
        for m in computer_moving:
            if can_comp_move(board, m):
                board[m - 1] = "O"
                break
    print_board()


# win_ways = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
def comp_win(bord):
    """حالات برد کامپیوتر"""
    for tuple2 in win_ways:
        if bord[tuple2[0]] == "O" and bord[tuple2[1]] == "O" and bord[tuple2[2]] == "O":
            return True
    return False


def copm_can_win(bord):
    """بررسی اینکه ایا جایی در برد وجود داره که اگر کامپیوتر اونجا حرکت کنه میبره یا ن"""
    for b in range(1, 10):
        if can_comp_move(board, b):
            board[b - 1] = "O"
            if comp_win(board):
                board[b - 1] = "O"
                return True
                break
            elif not comp_win(board):
                board[b - 1] = b
    return False

def player_can_win(bord):
    """این تابع در بخش دوم حرکت کامپیوتر استفاده میشه و کمک میکنه به اینکه کامپیوتر جلو بردن کاربر رو بگیره """
    for a in range(1, 10):
        if can_comp_move_player(board, a):
            board[a - 1] = "X"
            if player_winner(board):
                board[a - 1] = "O"
                return True
                break
            elif not player_winner(board):
                board[a - 1] = f"{a}"
    return False


def start_game():
    """واقعا توضیح بدم چیکار میکنه؟"""
    print_board()
    while has_empty_place(board):
        player_move(board)
        computer_move(board)
        if player_winner(board):
            print("You Win... (:")
            break
        elif comp_win(board):
            print("You Lose... ):")
            break
    print("game is over")
    play_again()


def play_again():
    """اینم مث بالایی توضیع بدم ایا؟؟"""
    a = input("Do you want to play again?(Y / N): ")
    if a.lower() == "y":
        for q in range(1, 10):
            board[q - 1] = q
        start_game()
    elif a.lower() == "n":
        print("Oh, maybe next time...")
    else:
        print("Invalid")
        play_again()


if __name__ == "__main__":
    start_game()
