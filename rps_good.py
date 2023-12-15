import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to Rock, Paper, Scissors.')

        self.moves = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
        self.valid_moves = list(self.moves.keys())
        self.user_score = 0
        self.ai_score = 0

    def play_game(self):
        user_move = input('Rock, Paper, or Scissors? >> ').lower()

        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        elif user_move not in self.valid_moves:
            print('Invalid move. Please respond with either Rock, Paper, or Scissors.')
            return

        ai_move = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        winner = self.check_move(user_move, ai_move)

        if winner == 'user':
            self.user_score += 1
        elif winner == 'ai':
            self.ai_score += 1

        print(f'User Score: {self.user_score}  AI Score: {self.ai_score}')

    def display_moves(self, user_move, ai_move):
        print('----')
        print(f'Your move: {self.moves[user_move]}')
        print(f"AI move: {self.moves[ai_move]}")
        print('----')

    def check_move(self, user_move, ai_move):
        if user_move == ai_move:
            print('It\'s a tie!')
            return 'tie'
        elif (user_move == 'rock' and ai_move == 'scissors') or (user_move == 'paper' and ai_move == 'rock') or (user_move == 'scissors' and ai_move == 'paper'):
            print('You Win!!!')
            return 'user'
        else:
            print('You lose! Hahaha')
            return 'ai'

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
