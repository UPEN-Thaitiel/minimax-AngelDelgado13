# Constants for the game setup
BOARD_SIZE = 3       # The Tic-Tac-Toe board is 3x3
REWARD = 10          # Score for winning the game

class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        print("¡Comienza el juego del Tic-Tac-Toe!")
        self.move_computer()  # Computer starts

        while True:
            self.move_player()
            self.move_computer()

    def print_board(self):
        for i in range(1, 10, 3):
            row = [self.board[i], self.board[i+1], self.board[i+2]]
            print(" " + " | ".join(row))
            if i < 7:
                print("---+---+---")

    def is_cell_free(self, position):
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        if self.is_cell_free(position):
            self.board[position] = player
            self.check_game_state()
        else:
            if player == self.player:
                print("¡Esa celda ya está ocupada! Intenta de nuevo.")
                self.move_player()  # Retry for human
            else:
                raise ValueError("IA intentó mover a una celda ocupada.")

    def check_game_state(self):
        self.print_board()
        if self.is_winning(self.player):
            print("¡Ganaste!")
            exit()
        elif self.is_winning(self.computer):
            print("La computadora gana.")
            exit()
        elif self.is_draw():
            print("¡Empate!")
            exit()

    def is_winning(self, player):
        # Check rows, columns, and diagonals
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],      # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],      # columns
            [1, 5, 9], [3, 5, 7]                  # diagonals
        ]
        for combo in win_combinations:
            if all(self.board[pos] == player for pos in combo):
                return True
        return False

    def is_draw(self):
        return all(self.board[pos] != ' ' for pos in self.board)

    def move_player(self):
        while True:
            try:
                position = int(input("Elige una posición (1-9): "))
                if position < 1 or position > 9:
                    print("Entrada inválida. Debe ser un número entre 1 y 9.")
                elif not self.is_cell_free(position):
                    print("La celda ya está ocupada.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Debe ser un número.")
        self.update_player_position(self.player, position)

    def move_computer(self):
        best_score = float('-inf')
        best_move = None
        for pos in self.board:
            if self.is_cell_free(pos):
                self.board[pos] = self.computer
                score = self.minimax(0, float('-inf'), float('inf'), False)
                self.board[pos] = ' '
                if score > best_score:
                    best_score = score
                    best_move = pos
        self.update_player_position(self.computer, best_move)

    def minimax(self, depth, alpha, beta, is_maximizer):
        if self.is_winning(self.computer):
            return REWARD - depth
        if self.is_winning(self.player):
            return -REWARD + depth
        if self.is_draw():
            return 0

        if is_maximizer:
            best_score = float('-inf')
            for pos in self.board:
                if self.is_cell_free(pos):
                    self.board[pos] = self.computer
                    score = self.minimax(depth + 1, alpha, beta, False)
                    self.board[pos] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        break
            return best_score
        else:
            best_score = float('inf')
            for pos in self.board:
                if self.is_cell_free(pos):
                    self.board[pos] = self.player
                    score = self.minimax(depth + 1, alpha, beta, True)
                    self.board[pos] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if alpha >= beta:
                        break
            return best_score

if __name__ == '__main__':
    board = {pos: ' ' for pos in range(1, 10)}
    game = TicTacToe(board)
    game.run()
