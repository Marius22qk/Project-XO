# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:09:49 2023

@author: mariu
"""

import random


suits = ("Hearts","Diamonds", "Spades","Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six","Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for  suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
    
class Player:
     
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
        
    def remove_one(self):
       return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type (new_cards) == type([]):
            self.all_cards.extend(new_cards)
            #list of multiple card objects
        else:
            self.all_cards.append(new_cards)
            #for asingle card object
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    

#GAME_SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on = True

round_num = 0

while game_on:
    
    round_num += 1
    print(f"Round{round_num}")
          

    if len(player_one.all_cards) == 0:
         print("Player One, out of cards! Player two wins!")
         game_on = False
         break
     
    if len(player_two.all_cards) == 0:
         print("Player two, out of cards! Player one wins!")
         game_on = False
         break
     
    # Start a new round
    
    player_one.cards = []
    player_one.cards.append(player_one.remove_one())
    
    player_two.cards = []
    player_two.cards.append(player_two.remove_one())
    
    # While at_war
    
    at_war = True
    
    while at_war:
        
        if player_one.cards[-1].value > player_two.cards[-1].value:
            player_one.add_cards(player_one.cards)
            player_one.add_cards(player_two.cards)
            
            at_war = False
            
        elif player_one.cards[-1].value < player_two.cards[-1].value:
            player_two.add_cards(player_one.cards)
            player_two.add_cards(player_two.cards)
            
            at_war = False
            
        else:
            print("WAR!")
            
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("Player two wins!")
                game_on = False
                break
            
            if len(player_two.all_cards) < 5:
                print("Player two unable to declare war")
                print("Player one wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one.cards.append(player_one.remove_one())
                    player_two.cards.append(player_two.remove_one())
            

