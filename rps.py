from random import randint
#Rock, Paper and Scissors game
def rps():
	y = 'y'
	while y =='y' or y=='Y':
		choices = ['paper', 'rock', 'scissor']
		user_choice = raw_input('Choose either rock,paper, or scissor:')
		opponent_choice = choices[randint(0,3)]
		
		if user_choice == 'paper' and opponent_choice == 'rock':
			return 'You win!'
		elif user_choice == 'paper' and opponent_choice == 'scissor':
			return 'Your Opponent Wins!'
		elif user_choice == 'rock' and opponent_choice == 'paper':
			return 'Your Opponent Wins!'
		elif user_choice == 'scissor' and opponent_choice == 'paper':
			return 'You Win!'
		elif user_choice == 'rock' and opponent_choice == 'scissor':
			return 'You Win!'
		elif user_choice == 'scissor' and opponent_choice == 'rock':
			return 'Your Opponent Wins!'
		elif user_choice == opponent_choice:
			return "It's a Draw!"
		else:
			return 'Those are not valid choices'
		
		y = raw_input("Do you want to play again?(y or Y for yes || n or N for no):")

def main():
    print('hello world')
		
