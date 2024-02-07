'''Q. Create one card for each combination of a suit and a rank.
List every combination of suit and rank in a set of 52 cards and name
the list as Deck.
Below are the lists of suits and ranks.
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
"Queen", "King", "Ace"] '''

import random
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
"King", "Ace"]
 
# Create an empty list to store the deck of cards
deck = []
# Iterate over each suit and rank to create the deck
for suit in suits:
    for rank in ranks:
   # Create a card by combining the suit and rank
        card = f"{rank} of {suit}"
# Add the card to the deck
 
        deck.append(card)

 # Print the deck of cards
for card in deck:
     print(card)
print(f"There are {len(deck)} cards in the deck.")


#Q2>Write all 52 cards from the list Deck into a file named Text1.txt.
#Display total number of lines in the file i.e.,52.

print("Dealing ...")
#hand = random.sample(deck, 5)
# Remove the dealt cards from the deck
Deck = [card for card in deck if card not in hand]
# Display the remaining cards in the deck and the player's hand
print(f"There are {len(Deck)} cards in the deck.")
print("Player has the following cards in their hand:")
print(hand)