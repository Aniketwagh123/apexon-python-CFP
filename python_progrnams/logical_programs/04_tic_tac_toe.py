import random
import time


def play(matrix, x, y, user='bot'):
    if matrix[x][y] not in ['O', 'X']:
        if user == 'bot':
            matrix[x][y] = 'O'
        else:
            matrix[x][y] = 'X'
        return True
    return False


def does_win(matrix, x, y):
    current = matrix[x][y]

    winning_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for condition in winning_conditions:
        if all(matrix[i][j] == current for i, j in condition):
            return True
    return False


def print_board(matrix):
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=' ')
        print()
    print()


def does_tie(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '.':
                return False
    return True


if __name__ == "__main__":
    matrix = [['.', '.', '.'],
              ['.', '.', '.'],
              ['.', '.', '.']]
    print()
    print('🎮 Game Start! Let the Tic Tac Toe battle begin! 🚀')
    print()

    while True:
        print_board(matrix)
        if does_tie(matrix):
            print('🤝 It\'s a tie! Well played! ⚖️')
            break

        x, y = map(int, input('👉 Your turn! Make your move. 🕹️ (format: row col): ').split())
        x -= 1
        y -= 1
        if 0 <= x < 3 and 0 <= y < 3:
            if play(matrix, x, y, "user"):
                if does_win(matrix, x, y):
                    print_board(matrix)
                    print('🎉 Congratulations! You win Tic Tac Toe! 🥳')
                    break

                print_board(matrix)

                if does_tie(matrix):
                    print('🤝 It\'s a tie! Well played! ⚖️')
                    break

                print('🤖 The bot is making its move...')
                time.sleep(1)
                while True:
                    x = random.choice([0, 1, 2])
                    y = random.choice([0, 1, 2])
                    if play(matrix, x, y):
                        break

                if does_win(matrix, x, y):
                    print_board(matrix)
                    print('😞 Sorry, you lose Tic Tac Toe. Better luck next time! 🍀')
                    break
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid move. Enter row and column between 1 and 3.")

    print()
    print('🏁 Game Over! Thanks for playing! 🏆')