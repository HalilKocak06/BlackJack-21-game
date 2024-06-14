import random
from art import logo

print(logo)

# Deck of Cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def draw_card(deck):
    return random.choice(deck)

def calculate_total(hand):
    total = sum(hand)
    # Evaluate Aces to 1
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Starting Cards
player_cards = [draw_card(cards), draw_card(cards)]
dealer_cards = [draw_card(cards), draw_card(cards)]

# Show user and dealer cards
print(f"YOUR cards are : {player_cards}")
print(f"CASINO cards are : [{dealer_cards[0]}] , [hidden]")

# Calculate the total of cards
player_total = calculate_total(player_cards)
dealer_total = calculate_total(dealer_cards)

# Check the winning situation
if player_total == 21:
    print("Users win!!")
elif dealer_total == 21:
    print("Dealer wins!!")
else:
    # Ask the user want to check card
    while player_total < 21:
        action = input("Do you want to draw a card? (y/n): ")
        if action.lower() == 'y':
            new_card = draw_card(cards)
            player_cards.append(new_card)
            player_total = calculate_total(player_cards)
            print(f"New card: {new_card}, YOUR cards are now: {player_cards}")
            if player_total > 21:
                print("User loses the game: Bust!")
                break
        else:
            break
    
    
    if player_total <= 21:
        print(f"CASINO cards are : {dealer_cards}")
        while dealer_total < 17:
            new_card = draw_card(cards)
            dealer_cards.append(new_card)
            dealer_total = calculate_total(dealer_cards)
            print(f"Dealer draws: {new_card}, CASINO cards are now: {dealer_cards}")
        
        # Check the results
        if dealer_total > 21:
            print("Dealer busts! User wins!!")
        elif dealer_total >= player_total:
            print("Dealer wins!!")
        else:
            print("User wins!!")
