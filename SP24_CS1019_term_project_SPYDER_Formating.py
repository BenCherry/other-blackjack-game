import random
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:52:56 2024

@author: CherrBear

Needs more testing / a main function to run everyhting from

NEED TO UPDATE DOCSTRINGS

"""


deck_1 = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]

player_hand = []  # creates empty player list to store cards
dealer_hand = []


def deal_hand(hand):
    """
    Start the hand giving 2 cards.

    Args:
        a (list): The empty player or dealer_hand list.

    Returns:
        list: List with 2 random values from deck_1.
    """
    if len(hand) == 0:
        for card in range(2):
            card_index = random.randrange(len(deck_1))
            hand.append(deck_1.pop(card_index))
    return hand


def hit(player_or_dealer):
    """"
    Draw a random 'card' from deck_1 and adds it to player/dealer list.

    Args:
        a (list): player / dealer_hand list.

    Returns:
        list: Value from deck_1 appended to player/dealer list.
    """
    if deck_1:  # checks for items in list, 1 or more items it executes
        card_index = random.randrange(len(deck_1))
        player_or_dealer.append(deck_1.pop(card_index))
    else:
        print('Time to shuffle!\n')
    return player_or_dealer


def player():
    """
    NEEDS DOCSTRING
    """
    while sum(player_hand) < 21:
        hand_signal = input('Press "H" to hit, or any key to stay: \n')
        if hand_signal == 'h':
            hit(player_hand)
            if player_count() is True:
                break
            print(f'You hit for a total of: {sum(player_hand)}\n')
            #if player_count() is True:
                #break
        elif hand_signal != 'h':
            print(f'You stay with {sum(player_hand)}\n')
            break


def player_count():
    """
    NEEDS DOCSTRING
    """
    bust = False
    if sum(player_hand) > 21:
        bust = True
    return bust


def house_hand():
    """
    Determine if the dealer draws more cards or stays.

    Args:
        a (none) None.

    Return:
        list: Finished dealer_hand list.
    """
    while sum(dealer_hand) < 17:
        if player_count is True:  # Skip dealer draw if player_hand > 21
            break
        hit(dealer_hand)
        print(f'Dealer hits for a total of: {sum(dealer_hand)}\n')
        if dealer_count() is True:
            break


def dealer_count():
    """
    NEEDS DOCSTRING
    """
    bust = False
    if sum(dealer_hand) > 21:
        bust = True
    return bust


def winning_hand():
    """
    Compare the hands and returns the result (win / lose/ push).

    Args:
        a (none): None.

    Returns:
        str: Prints the winner.
    """
    if dealer_count() is True:
        print(f'Dealer busts with: {sum(dealer_hand)} '
              f'Player wins with: {sum(player_hand)}\n')
    elif player_count() is True:
        print(f'You bust with: {sum(player_hand)}\n')

    elif sum(dealer_hand) < sum(player_hand):
        print(f'Dealer has a {sum(dealer_hand)}, '
              f' you win with a {sum(player_hand)}\n')
    elif sum(dealer_hand) > sum(player_hand):
        print(f'Dealer wins with a {sum(dealer_hand)}\n')
    elif sum(dealer_hand) == sum(player_hand):
        print("A push is a win\n")


def main():
    """
    NEEDS DOCSTRING
    """
    deal_hand(player_hand)
    print(f'You have: {sum(player_hand)}\n')
    deal_hand(dealer_hand)
    print(f'Dealer shows: {dealer_hand[0]}\n')  # Show dealer first card only
    player()
    house_hand()
    winning_hand()
main()