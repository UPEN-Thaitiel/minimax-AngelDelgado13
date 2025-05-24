BOARD_SIZE = 3
REWARD = 10

class TicTacToe:
    def __init__(self, board):
        # Challenge 1
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        # Challenge 11
        print("¡Bienvenido al juego Tic-Tac-Toe!")
        self.move_computer()  # La computadora inicia

        while True:
            self.move_player()
            self.move_computer()

    def print_board(self):
        # Challenge 2
        for i in range(1, 10, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 7:
                print("---+---+---")

    def is_cell_free(self, position):
        # Challenge 3
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        # Challenge 4
        if self.is_cell_free(position):
            self.board[position] = player
            self.check_game_state()
        else:
            if player == self.player:
                print("Celda ocupada. Intenta de nuevo.")
                self.move_player()  # Intenta otra vez

    def is_winning(self, player):
        # Challenge 5
        wins = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],    # filas
            [1, 4, 7], [2, 5, 8], [3, 6, 9],    # columnas
            [1, 5, 9], [3, 5, 7]                # diagonales
        ]
        return any(all(self.board[pos] == player for pos in combo) for combo in wins)

    def is_draw(self):
        # Challenge 6
        return all(self.board[pos] != ' ' for pos in self.board)

    def check_game_state(self):
        # Challenge 7
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

    def move_player(self):
        # Challenge 8
        while True:
            try:
                position = int(input("Tu turno (1-9): "))
                if 1 <= position <= 9:
                    if self.is_cell_free(position):
                        break
                    else:
                        print("La celda ya está ocupada.")
                else:
                    print("Debes ingresar un número del 1 al 9.")
            except ValueError:
                print("Entrada inválida. Ingresa un número del 1 al 9.")
        self.update_player_position(self.player, position)

    def move_computer(self):
        # Challenge 9
        best_score = float('-inf')
        best_move = None
        for pos in self.board:
            if self.is_cell_free(pos):
                self.board[pos] = self.computer
                score = self.minimax(0, False)
                self.board[pos] = ' '
                if score > best_score:
                    best_score = score
                    best_move = pos
        self.update_player_position(self.computer, best_move)

    def minimax(self, depth, is_maximizer):
        # Challenge 10
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
                    score = self.minimax(depth + 1, False)
                    self.board[pos] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for pos in self.board:
                if self.is_cell_free(pos):
                    self.board[pos] = self.player
                    score = self.minimax(depth + 1, True)
                    self.board[pos] = ' '
                    best_score = min(best_score, score)
            return best_score


if __name__ == '__main__':
    # Challenge 1
    board = {pos: ' ' for pos in range(1, 10)}

    game = TicTacToe(board)

    # Challenge 11
    game.run()
