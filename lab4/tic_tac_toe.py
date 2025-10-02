# tic_tac_toe.py

import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("This method should be overridden by subclasses ")

class HumanPlayer(Player):
    def make_move(self, board):
        valid_move = False
        while not valid_move:
            try:
                position = int(input(f"{self.name}, enter your move (1 : 9) : ")) - 1
                if board.is_valid_move(position):
                    valid_move = True
                else:
                    print("invalid number it mus be between 1 nad 9 :")
            except ValueError:

                print("Please enter a number between 1 and 9: ")
        board.update(position, self.symbol)

class ComputerPlayer(Player):
    def make_move(self, board):
        position = random.choice(board.get_available_moves())
        board.update(position, self.symbol)
        print(f"{self.name} (Computer) has made a move at position {position + 1} ")

class Board:
    def __init__(self):
        self._grid = [' ' for _ in range(9)]

    def display(self):
        print("\n")
        for i in range(3):
            print("|".join(self._grid[i * 3 : (i+1) *3]))
            if i < 2:
                print("*****")
        print("\n")

    def update(self, position, symbol):
        self._grid[position] = symbol

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]
        for combo in winning_combinations:
            if self._grid[combo[0]] == self._grid[combo[1]] == self._grid[combo[2]] != ' ' :
                return self._grid[combo[0]]
        return None

    def is_full(self):
        return ' ' not in self._grid

    def is_valid_move(self, position):
        return self._grid[position] == ' '

    def get_available_moves(self):
        return [i for i, spot in enumerate(self._grid) if spot == ' ']

class Game:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.current_turn = 0

    def play(self):
        self.setup_game()
        while True:
            self.board.display()
            current_player = self.players[self.current_turn]
            current_player.make_move(self.board)

            winner = self.board.check_winner()
            if winner:
                self.board.display()

                print(f"Congratulations {current_player.name}, you have won!!!!!!!!!!!! /*/*/*/*/*")
                break
            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            self.switch_turns()

    def setup_game(self):
        choice = input("Do you want to play with a friend enter 1 or vs computer enter 2 => :  ")
        if choice == '1':

            name1 = input("Enter name for Player 1 (X): ")
            name2 = input("Enter name for Player 2 (O): ")
            self.players.append(HumanPlayer(name1, 'X'))    
            self.players.append(HumanPlayer(name2, 'O'))
        elif choice == '2':

            name = input("Enter your name: ")
            self.players.append(HumanPlayer(name, 'X'))
            self.players.append(ComputerPlayer("Computer", 'O'))
        else:
            
            print("Invalid choice. Please restart the game.")
            exit()

    def switch_turns(self):
        self.current_turn = (self.current_turn + 1) % 2

if __name__ == "__main__":
    game = Game()
    game.play() 