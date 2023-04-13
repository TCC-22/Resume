# Blackjack Project 


# Import necessary modules
import random
import os
os.system('cls')


# Create Logo
logo = """
 ____  _            _    _            _    
|  _ \| |          | |  (_)          | |   
| |_) | | __ _  ___| | ___  __ _  ___| | __
|  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   <
|____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                       _/ |                
                      |__/                 

"""


# Create card list
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Create Hand class
class Hand:

    # Create init method with empty list
    def __init__(self,user_score, computer_score):
        self.list = []
        self.user_score = user_score
        self.computer_score = computer_score
        self.statement = ""
        self.wins = 0
        self.loses = 0

    # Create hit method to append list with a card
    def hit(self):
        self.list.append(random.choice(cards))
        if sum(self.list) > 21 and 11 in self.list:
            self.list.remove(11)
            self.list.append(1)
        else:
            return


    # Create computer_deal method to append list with a card
    # Method must also append list with a '?'
    def computer_deal(self):
        self.list.append(random.choice(cards))
        self.list.append("?")

    # Create computer reveal method to pop '?'
    # Method must also append list with a card
    def computer_reveal(self):
        self.list.pop()
        self.list.append(random.choice(cards))

    # Create caluculate_hand method to calculate sum of list
    def calculate_hand(self):
        if len(self.list) == 2 and sum(self.list) == 21:
            return 0
        return sum(self.list)

    # Create print_hand method to print hand()
    def print_hand(self):
        return self.list
    
    def print_statement(self):
        return self.statement
  
    # Create user_turn method start user's turn
    def user_turn(self):
        run = True
        while run:
            print_all()
            score = self.calculate_hand()
            if score == 0 or score >= 21:
                run = False 
            else:
                hit = input("Do you want to draw another card? Type 'yes' or 'no': ").lower()
                if hit == "yes":
                    self.hit()
                else:
                    return self.list    
                
    # Create computer_turn method to start computer's turn
    def computer_turn(self):
        run = True
        while run:
            print_all()
            score = self.calculate_hand()
            if score == 0 or score >= 21:
                run = False
            elif score < 17:
                self.hit()
            else:
                return self.list
            
    # Create method to compare scores
    def compare_scores(self, user_score, computer_score):
        # If the user_score is over 21, then the user loses.
        # If the computer and user both have the same score, then it's a draw.
        # If the computer has a blackjack (0), # then the user loses. If the user has a blackjack (0), then the user wins.
        # If the computer_score is over 21, then the computer loses.
        # If none of the above, then the player with the highest score wins.   
        if user_score > 21:
            self.loses += 1
            self.statement = ("Bust, you lose!")
            # print(f"Bust, you lose!")
        elif user_score == computer_score:
            self.statement = ("Draw!")
            # print(f"Draw!")  
        elif computer_score == 0:
            self.loses += 1
            self.statement = ("Computer got blackjack, you lose!")
            # print(f"Computer got blackjack, you lose!")
        elif user_score == 0:
            self.wins += 1
            self.statement = ("Blackjack, you win")
            # print(f"Blackjack, you win")
        elif computer_score > 21:
            self.wins += 1
            self.statement = ("Computer busts, you win!")
            # print(f"Computer busts, you win!")       
        elif computer_score > user_score:
            self.loses += 1
            self.statement = ("You lose!")
            # print(f"You lose!")
        elif user_score > computer_score:
            self.wins += 1
            self.statement = ("You win!")
            # print(f"You win!") 

    # Create method to clear list and statment:
    def clear_list(self):
        self.list = []
        self.statement = ""


# Create objects
user_hand = Hand(None, None)
computer_hand = Hand(None, None)

# Create function to print the Logo, User's hand and Computer's hand
def print_all():

    os.system('cls')
    print(logo)
    print(f"User Hand: {user_hand.print_hand()}")
    print(f"Computer Hand: {computer_hand.print_hand()}")
    print(f"{user_hand.statement}")
    print(f"Wins: {user_hand.wins}")
    print(f"Loses: {user_hand.loses}\n")


def main():

    #Create game loop
    blackjack = True
    while blackjack:
        # Deal to User
        user_hand.hit()
        user_hand.hit()

        # Deal to Computer
        computer_hand.computer_deal()

        # User goes first
        user_hand.user_turn()

        # Diplay Computer's Hand
        computer_hand.computer_reveal()
        print_all()

        # Determine if user has blackjack
        if user_hand.calculate_hand() == 0:
            print_all()
        # Determine if user busts
        elif user_hand.calculate_hand() > 21:
            print_all            
        # Computer's turn
        else:
            computer_hand.computer_turn()

        # Compare scores
        user = user_hand.calculate_hand()
        computer = computer_hand.calculate_hand()
        user_hand.compare_scores(user, computer)
        print_all()

        # Ask to play again
        play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
        if play_again == "yes":
            user_hand.clear_list()
            computer_hand.clear_list()
            blackjack = True
        else:
            print("Have a nice day!")
            blackjack = False
    
    
if __name__ == "__main__":
    main()