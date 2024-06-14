# Blackjack Game

A simple Blackjack game implemented in Python. This project demonstrates basic game logic and user interaction in a console-based application.

## Overview

Blackjack is a popular card game played in casinos. The objective is to get a hand value as close to 21 as possible without exceeding it. Players compete against the dealer.

## Features

- Random card drawing
- Basic game logic for player and dealer turns
- Handling of Aces (11 or 1 based on hand value)
- Simple text-based user interface

## How to Play

1. The game starts with the player and the dealer each being dealt two cards.
2. The player's cards and one of the dealer's cards are shown.
3. The player can choose to draw additional cards to get as close to 21 as possible.
4. If the player's total exceeds 21, they bust and lose the game.
5. After the player finishes drawing cards, the dealer draws cards until their total is at least 17.
6. The final totals are compared to determine the winner.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/blackjack-game.git
    cd blackjack-game
    ```

2. Install required packages (if any):

    ```sh
    pip install -r requirements.txt
    ```

### Running the Game

1. Run the game using Python:

    ```sh
    python blackjack.py
    ```

## Code Explanation

The main code is structured as follows:

- **Deck of Cards**: Defined as a list of values representing card ranks.
- **Functions**:
  - `draw_card(deck)`: Draws a random card from the deck.
  - `calculate_total(hand)`: Calculates the total value of a hand, adjusting for Aces.
- **Game Flow**:
  - Initial cards are dealt to the player and dealer.
  - The player can draw additional cards.
  - The dealer draws cards according to the rules.
  - The final totals are compared to determine the winner.

## Example Output

```text
Welcome to Blackjack!

YOUR cards are: [10, 7]
CASINO cards are: [9], [hidden]

Do you want to draw a card? (y/n): n

CASINO cards are: [9, 6]
Dealer draws: 5, CASINO cards are now: [9, 6, 5]

Dealer busts! User wins!!
