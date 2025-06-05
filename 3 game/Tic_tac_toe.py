import sys

class TicTacToe:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        self.current_player = 'X'
        self.winner = None

    def _draw_board(self):
        print("\nTic Tac Toe")
        print(f"Player 1 (X) - Player 2 (O)")
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--|---|--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--|---|--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def _get_player_move(self):
        while True:
            try:
                move = int(input(f"Player {self.current_player}\nEnter a number:"))
                if 1 <= move <= 9:
                    return move - 1
                else:
                    print("Invalid number. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def _is_valid_move(self, move):
        return self.board[move] not in ['X', 'O']

    def _make_move(self, move):
        if self._is_valid_move(move):
            self.board[move] = self.current_player
            return True
        else:
            print("Invalid move. That spot is already taken.")
            return False

    def _check_win(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and \
               (self.board[combo[0]] == self.current_player):
                self.winner = self.current_player
                return True
        return False

    def _check_draw(self):
        for cell in self.board:
            if cell not in ['X', 'O']:
                return False
        return True

    def _switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while not self.winner:
            self._draw_board()
            move = self._get_player_move()
            if self._make_move(move):
                if self._check_win():
                    self._draw_board()
                    print(f"\nPlayer {self.winner} wins!")
                    break
                if self._check_draw():
                    self._draw_board()
                    print("\nIt's a draw!")
                    break
                self._switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()