# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:25:14 2024

@author: cherrbear

Functions dealing with removing cards from the card list and
putting them in the player_hand and dealer_hand lists, and comparing
the total value of the player_hand and dealer_hand lists to determine
if the Dealer will draw again, and the outcome of the hand
"""

import random

#INPUT player_hand and dealer_hand lists as arguments
#PROCESSING random item removed from list, assigned to player/dealer list
#OUTPUT player or dealer list with the 2 random items
def deal_hand(hand): 
    if len(hand) == 0:    
        for card in range(2): 
            card_index = random.randrange(len(my_list1))
            hand.append(my_list1.pop(card_index))
    return hand

#INPUT player/dealer_hand lists as arguments           
#PROCESSING checks for items in list, random item removed, assign to list
#OUTPUT adds random item to player/dealer, print statement if empty
def hit(x):
    if my_list1: # checks for items in list, 1 or more items it executes
        card_index = random.randrange(len(my_list1))
        x.append(my_list1.pop(card_index))
    else:
        print('Time to shuffle!')
    return x

#INPUT
#PROCESSING
#OUTPUT
def house_hand():
    if sum(dealer_hand) < 17:
        while sum(dealer_hand) < 17:
            hit(dealer_hand)
            print(f'Dealer has {sum(dealer_hand)}')
    elif sum(dealer_hand) > 21:
        print(f'Dealer busts with {sum(dealer_hand)}')        

#INPUT
#PROCESSING
#OUTPUT
def winning_hand():
    if sum(dealer_hand) > sum(player_hand):
        print(f'You have a {sum(player_hand)}, ' 
              f'dealer has a {sum(dealer_hand)}, dealer wins.')
    elif sum(dealer_hand) < sum(player_hand):
        print(f'Dealer has a {sum(dealer_hand)}, '
              f' you win with a {sum(player_hand)}')
    elif sum(dealer_hand) == sum(player_hand):
        print("A push is a win")