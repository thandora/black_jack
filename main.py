############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

##D The deck is unlimited in size. 
##D There are no jokers. 
##D The Jack/Queen/King all count as 10.
##D The the Ace can count as 11 or 1.
##D Use the following list as the deck of cards:
##D cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
##D The cards in the list have equal probability of being drawn.
##D Cards are not removed from the deck as they are drawn.
##D The computer is the dealer.
from art import logo
import random
print(logo)

#Create sets of decks. In the form of:
#[boolean, [deck_1], ..,[deck_n]]
#Boolean is True if infinite deck. Only true at n_decks == 0.
def create_deck(n_decks: int):
    '''Creates n_decks number of decks. If n_decks = 0, create 1 infinite deck 
    '''
    sets_deck = []

    #If user chooses 0, create an "infinite" deck. Denoted by True in sets_deck[0].
    if not n_decks:
        sets_deck.append(True)
        sets_deck.append([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    #If user chooses n > 0, create a n number of decks. 
    else:
        sets_deck.append(False)
        for _ in range(n_decks):
            sets_deck.append([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
            # sets_deck.append([1, 2])

    return sets_deck


def draw_cards(n: int, decks: list):
    '''Returns a list of n cards, and remaining of the deck inputted.
    '''

    drawed_cards = []
    n_decks = len(decks) - 1
    
    is_deck_infinite = None
    if decks[0] == True:
        is_deck_infinite = True
    else:
        is_deck_infinite = False
    
    #Draw n cards and remove from deck.
    for _ in range(0, n):

        #Select random index for choosing deck. 
        #Starts at 1 since 0 is for determining deck is finite or not.
        random_deck_index = random.randint(1, n_decks)
        selected_deck = decks[random_deck_index]

        deck_size = len(selected_deck) - 1

        #Randomly select a deck from currently available decks.
        random_card_index = random.randint(0, deck_size)

        if is_deck_infinite:
            selected_card = random.sample(selected_deck, 1)
        else:
            selected_card = selected_deck.pop(random_card_index)
            deck_size -= 1

        #Remove empty decks.
        # for i, deck in enumerate(decks):
        
        if decks[random_deck_index] == []: #Dont use deck == False to check for 
            decks.pop(random_deck_index)   #empty lists since index 0 is a boolean.
            n_decks -= 1 #Update number of decks

        drawed_cards.append(selected_card)


    return drawed_cards, decks


#Sum of hand (blackjack)
def hand_score(hand: list):

    hand_sum = sum(hand)

    #Note that 11 can either be 1 or 11.
    for _ in range(hand.count(11)):
        if hand_sum > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)
            hand_sum = sum(hand)

    return sum(hand)



#Git test 213
#######################################
# decks = create_deck(2)
# my_cards, my_decks = draw_cards(3 , my_decks)
# your_cards = draw_cards(3, my_decks)[0]
# print(my_cards, your_cards)
# print(hand_score(my_cards), hand_score(your_cards))
#######################################
continue_playing = True

#Create a deck and deal
n_of_decks = 1
decks = create_deck(n_of_decks)
player_cards = []
dealer_cards = []

    

intro_once = True

while continue_playing:
    print(f"\n\n{decks}\n\n")
    #Start with new hand.
    player_cards = []
    dealer_cards = []

    user_continue_choice = ""
    #Message at start.
    if intro_once:
        while user_continue_choice not in ["y", "n"]:
            user_continue_choice = input("Welcome to Las Dolina! \
Do you want to play Black Jack? (y / n): ").lower()
        intro_once = False

    #Message after 1st run.
    else:
        while user_continue_choice not in ["y", "n"]:
            user_continue_choice = input("Do you want to play again? (y / n): ").lower()

    if user_continue_choice == "n":
        break

    #Simulate 1 by 1 dealing (might be useful for future console display)
    for _ in range(2): 
        try:
            drawed_card, decks = draw_cards(1, decks)
        except: #Repopulate decks
            decks = create_deck(n_of_decks)
            drawed_card, decks = draw_cards(1, decks)
        player_cards.append(drawed_card[0])

        try:
            drawed_card, decks = draw_cards(1, decks)
        except: #Repopulate decks
            decks = create_deck(n_of_decks)
            drawed_card, decks = draw_cards(1, decks)
        dealer_cards.append(drawed_card[0])
        

        
    
    #Show player and dealer's card.
    player_score = hand_score(player_cards)
    print(f"Your cards are {player_cards}, [{player_score}].")
    print(f"Dealer")
    # user_draw_choice = input("Draw a card?")
    
    
    
    #TODO Implement "check if enough cards are on deck"-inator on draw.
    
    #Draw cards 2 cards for player and dealer. Also updates currect decks
    # my_cards, decks = draw_cards(2, decks)
    # dealer_cards, decks = draw_cards(2, decks)
    

































##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

