import random

choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')
    ):
        return 'You win!'
    else:
        return 'Computer wins!'

def main():
    print("Welcome to Rock-Paper-Scissors! Type 'quit' to exit.")
    while True:
        player = input('Choose rock, paper, or scissors: ').strip().lower()
        if player == 'quit':
            print('Thanks for playing!')
            break
        if player not in choices:
            print('Invalid choice. Try again.')
            continue
        computer = get_computer_choice()
        print(f'Computer chose: {computer}')
        result = determine_winner(player, computer)
        print(result)

if __name__ == '__main__':
    main()
