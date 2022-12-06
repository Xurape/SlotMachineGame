import os
from random import randint
from colorama import Fore

# Credits variables
credits = base_credits = 100
minimum_credits = 10


# The positions
class Positions:
	slot1 = 0
	slot2 = 0
	slot3 = 0


# Bet stuff
bet_symbols = ["🐸", "🐵", "🐰", "🦊", "🐻", "🐼"]
bet_won = False
bet_win = 0
bet_positions = Positions()


# First message appearing when starting the program
def greetingMessage():
	print(Fore.GREEN + "\n		  Welcome to:\n")
	print("┌──────────────────────────────┐\n" +
	      "│  Xurape's first python game  │\n" +
	      "└──────────────────────────────┘\n" + Fore.YELLOW)


# Execute it
greetingMessage()

# Ask for the person's name
name = input(Fore.WHITE + "\nFirst, start by telling us your name: " +
             Fore.YELLOW + " \n> " + Fore.WHITE)

# Clear the system's screen
os.system('clear')

# Print the person's name and tell them how many credits they start with.
print(
 f"\nWelcome, {Fore.GREEN}{name}{Fore.WHITE}. You've been awarded {Fore.GREEN}{credits}{Fore.WHITE} credits to start your bets!"
)


# Tell them the instructions
def Instructions():
	print(
	 f"\nInstructions: \n{Fore.BLUE}> {Fore.WHITE}3x one of any emoji = {Fore.GREEN}20 credits\n{Fore.BLUE}> {Fore.WHITE}2x one of any emoji = {Fore.GREEN}15 credits\n{Fore.BLUE}> {Fore.WHITE}1x one of any emoji = {Fore.RED}No credits\n\n{Fore.BLUE}> {Fore.WHITE}Cost of each roll out: {Fore.RED}10 credits{Fore.WHITE}"
	)


Instructions()

# Start the game
while True:
	if credits < minimum_credits:
		os.system('clear')
		print(
		 f"\nI'm sorry {Fore.GREEN}{name}{Fore.WHITE}, you {Fore.RED}don't have{Fore.WHITE} enough credits to play again!"
		)
		break

	answer = input(
	 f"\nDo you wish to {Fore.GREEN}roll out the dice{Fore.WHITE}? {Fore.YELLOW}(Y/N){Fore.WHITE}\n{Fore.BLUE}> {Fore.WHITE}"
	).lower()

	if not answer.startswith('y'):
		print(f"\nYou {Fore.RED}cancelled{Fore.WHITE} the game!")
		break

	print(f"\nStarting the game.. {Fore.RED}(-10 credits){Fore.WHITE}\n")

	credits -= 10
	bet_won = False
	bet_win = 0

	# Generate the random emojis for positions
	bet_positions.slot1 = randint(1, len(bet_symbols) - 1)
	bet_positions.slot2 = randint(1, len(bet_symbols) - 1)
	bet_positions.slot3 = randint(1, len(bet_symbols) - 1)

	# Set the slots
	slot1 = bet_symbols[bet_positions.slot1]
	slot2 = bet_symbols[bet_positions.slot2]
	slot3 = bet_symbols[bet_positions.slot3]

	# Print the grid
	print("  ┌──────────────┐")
	print(
	 f"  │ {bet_symbols[randint(1, len(bet_symbols) - 1)]} │ {bet_symbols[randint(1, len(bet_symbols) - 1)]} │ {bet_symbols[randint(1, len(bet_symbols) - 1)]} │"
	)
	print("  ├──────────────┤")

	print(
	 f"{Fore.GREEN}>{Fore.WHITE} │ {slot1} │ {slot2} │ {slot3} │ {Fore.GREEN}<{Fore.WHITE}"
	)

	print("  ├──────────────┤")

	print(
	 f"  │ {bet_symbols[randint(1, len(bet_symbols) - 1)]} │ {bet_symbols[randint(1, len(bet_symbols) - 1)]} │ {bet_symbols[randint(1, len(bet_symbols) - 1)]} │"
	)
	print("  └──────────────┘")

	# Check for point winning
	for x in range(1, len(bet_symbols)):
		while bet_won == False:
			if bet_positions.slot1 == x and bet_positions.slot2 == x and bet_positions.slot3 == x:
				credits += 20
				print(
				 f"\n{Fore.GREEN}>{Fore.WHITE} You've won {Fore.GREEN}20 {Fore.WHITE}credits!"
				)
				bet_won = True
				bet_win += 1
				break
			elif bet_positions.slot1 == x and bet_positions.slot2 == x and bet_positions.slot3 != x:
				credits += 15
				print(
				 f"\n{Fore.GREEN}>{Fore.WHITE} You've won {Fore.GREEN}15 {Fore.WHITE}credits!"
				)
				bet_won = True
				bet_win += 1
				break
			elif bet_positions.slot1 != x and bet_positions.slot2 == x and bet_positions.slot3 == x:
				credits += 15
				print(
				 f"\n{Fore.GREEN}>{Fore.WHITE} You've won {Fore.GREEN}15 {Fore.WHITE}credits!"
				)
				bet_won = True
				bet_win += 1
				break
			elif bet_positions.slot1 == x and bet_positions.slot2 != x and bet_positions.slot3 == x:
				credits += 15
				print(
				 f"\n{Fore.GREEN}>{Fore.WHITE} You've won {Fore.GREEN}15 {Fore.WHITE}credits!"
				)
				bet_won = True
				bet_win += 1
				break
			else:
				break

	if bet_win == 0:
		print(f"\n{Fore.RED}> {Fore.WHITE}Unfornately you didn't win anything :(")
	print(f"\nCurrent balance: {Fore.GREEN}{credits}{Fore.WHITE} credits")
