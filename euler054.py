#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
import time
import sys
import os

start = time.clock()

"""
https://github.com/SpecialK/SpecialKEval

Created by Kenneth J. Shackleton on 14 June 2011.
Copyright (c) 2011 Ringo Limited.
All rights reserved.
"""

DECK_SIZE = 52

INDEX_OF_SEVEN_OF_SPADES = 32
INDEX_OF_EIGHT_OF_CLUBS = 31

NUMBER_OF_SUITS = 4
NUMBER_OF_FACES = 13

SPADE = 0
HEART = 1
DIAMOND = 8
CLUB = 57

TWO_FIVE = 0
THREE_FIVE = 1
FOUR_FIVE = 5
FIVE_FIVE = 22
SIX_FIVE = 94
SEVEN_FIVE = 312
EIGHT_FIVE = 992
NINE_FIVE = 2422
TEN_FIVE = 5624
JACK_FIVE = 12522
QUEEN_FIVE = 19998
KING_FIVE = 43258
ACE_FIVE = 79415

TWO_FLUSH = 1
THREE_FLUSH = 2
FOUR_FLUSH = 4
FIVE_FLUSH = 8
SIX_FLUSH = 16
SEVEN_FLUSH = 32
EIGHT_FLUSH = 64
NINE_FLUSH = (EIGHT_FLUSH+SEVEN_FLUSH+SIX_FLUSH+FIVE_FLUSH+FOUR_FLUSH+THREE_FLUSH+TWO_FLUSH+1)  #128
TEN_FLUSH = (NINE_FLUSH+EIGHT_FLUSH+SEVEN_FLUSH+SIX_FLUSH+FIVE_FLUSH+FOUR_FLUSH+THREE_FLUSH+1)  #255
JACK_FLUSH = (TEN_FLUSH+NINE_FLUSH+EIGHT_FLUSH+SEVEN_FLUSH+SIX_FLUSH+FIVE_FLUSH+FOUR_FLUSH+1)   #508
QUEEN_FLUSH = (JACK_FLUSH+TEN_FLUSH+NINE_FLUSH+EIGHT_FLUSH+SEVEN_FLUSH+SIX_FLUSH+FIVE_FLUSH+1)  #1012
KING_FLUSH = (QUEEN_FLUSH+JACK_FLUSH+TEN_FLUSH+NINE_FLUSH+EIGHT_FLUSH+SEVEN_FLUSH+SIX_FLUSH+1)  #2016
ACE_FLUSH = (KING_FLUSH+QUEEN_FLUSH+JACK_FLUSH+TEN_FLUSH+NINE_FLUSH+EIGHT_FLUSH+SEVEN_FLUSH+1)  #4016

#_SEVEN tag suppressed
TWO = 0
THREE = 1
FOUR = 5
FIVE = 22
SIX = 98
SEVEN = 453
EIGHT = 2031
NINE = 8698
TEN = 22854
JACK = 83661
QUEEN = 262349
KING = 636345
ACE = 1479181
#end of _SEVEN tag suppressed

MAX_FIVE_NONFLUSH_KEY_INT = ((4*ACE_FIVE)+KING_FIVE)
MAX_FIVE_FLUSH_KEY_INT = (ACE_FLUSH+KING_FLUSH+QUEEN_FLUSH+JACK_FLUSH+TEN_FLUSH)
MAX_SEVEN_FLUSH_KEY_INT = (ACE_FLUSH+KING_FLUSH+QUEEN_FLUSH+JACK_FLUSH+TEN_FLUSH+NINE_FLUSH+EIGHT_FLUSH)
MAX_NONFLUSH_KEY_INT = ((4*ACE)+(3*KING))

MAX_FLUSH_CHECK_SUM = (7*CLUB)

L_WON = -1
R_WON = 1
DRAW = 0

CIRCUMFERENCE_FIVE = 187853
CIRCUMFERENCE_SEVEN = 4565145
#/////////
#//The following are used with NSAssert for
#//debugging, ignored by release mode
RANK_OF_A_WORST_HAND = 0
RANK_OF_A_BEST_HAND = 7462
RANK_OF_WORST_FLUSH = 5864
RANK_OF_BEST_NON_STRAIGHT_FLUSH = 7140
RANK_OF_WORST_STRAIGHT = 5854
RANK_OF_BEST_STRAIGHT = 5863
RANK_OF_WORST_STRAIGHT_FLUSH = 7453
RANK_OF_BEST_STRAIGHT_FLUSH = RANK_OF_A_BEST_HAND

KEY_COUNT = 53924
NON_FLUSH_KEY_COUNT = 49205
FLUSH_KEY_COUNT = 4719
#/////////

#Used in flush checking. These must be distinct from each of the suits.
UNVERIFIED = -2
NOT_A_FLUSH = -1
#/////////

#Bit masks
SUIT_BIT_MASK = 511
NON_FLUSH_BIT_SHIFT = 9
#/////////

"""
FiveEval.py

Created by Kenneth J. Shackleton on 14 June 2011.
Copyright (c) 2011 Ringo Limited.
All rights reserved.
"""

class FiveEval :
    
    def __init__(self) :
        
        self.rankArray = [0] * (MAX_FIVE_NONFLUSH_KEY_INT + 1)
        self.flushRankArray = [0] * (MAX_FIVE_FLUSH_KEY_INT + 1)
        self.deckcardsFace = [0] * DECK_SIZE
        self.deckcardsFlush = [0] * DECK_SIZE
        self.deckcardsSuit = [0] * DECK_SIZE
        
        face = [TWO_FIVE, THREE_FIVE, FOUR_FIVE,
                FIVE_FIVE, SIX_FIVE, SEVEN_FIVE,
                EIGHT_FIVE, NINE_FIVE, TEN_FIVE,
                JACK_FIVE, QUEEN_FIVE, KING_FIVE,
                ACE_FIVE]
                
        faceFlush = [TWO_FLUSH, THREE_FLUSH,
                     FOUR_FLUSH, FIVE_FLUSH,
                     SIX_FLUSH, SEVEN_FLUSH,
                     EIGHT_FLUSH, NINE_FLUSH,
                     TEN_FLUSH, JACK_FLUSH,
                     QUEEN_FLUSH, KING_FLUSH,
                     ACE_FLUSH]
                        
        for n in range(NUMBER_OF_FACES) :
            
            self.deckcardsSuit[4*n] = SPADE
            self.deckcardsSuit[4*n + 1] = HEART
            self.deckcardsSuit[4*n + 2] = DIAMOND
            self.deckcardsSuit[4*n + 3] = CLUB

            self.deckcardsFace[4*n] = face[12 - n]
            self.deckcardsFace[4*n + 1] = face[12 - n]
            self.deckcardsFace[4*n + 2] = face[12 - n]
            self.deckcardsFace[4*n + 3] = face[12 - n]
            
            self.deckcardsFlush[4*n] = faceFlush[12 - n]
            self.deckcardsFlush[4*n + 1] = faceFlush[12 - n]
            self.deckcardsFlush[4*n + 2] = faceFlush[12 - n]
            self.deckcardsFlush[4*n + 3] = faceFlush[12 - n]
        
        # n increments as rank.
        n = 0
        
        # High card.
        for i in range(5, NUMBER_OF_FACES) :
            for j in range(3, i) :
                for k in range(2, j) :
                    for l in range(1, k) :
                        # No straights
                        for m in range(0, l) :
                            if not (i - m == 4 or (i == 12 and j == 3 and k == 2 and l == 1 and m == 0)) :
                                n += 1
                                self.rankArray[face[i] + face[j] + face[k] + face[l] + face[m]] = n
                                
        # Pair.
        for i in range(0, NUMBER_OF_FACES) :
            for j in range(2, NUMBER_OF_FACES) :
                for k in range(1, j) :
                    for l in range(0, k) :
                        if i != j and i != k and i != l :
                            n += 1
                            self.rankArray[(2*face[i]) + face[j] + face[k] + face[l]] = n

        # Two pair.
        for i in range(1, NUMBER_OF_FACES) :
            for j in range(0, i) :
                for k in range(0, NUMBER_OF_FACES) :
                    # No fullhouse
                    if k != i and k != j :
                        n += 1
                        self.rankArray[(2*face[i]) + (2*face[j]) + face[k]] = n     
        
        # Triple.
        for i in range(0, NUMBER_OF_FACES) :
            for j in range(1, NUMBER_OF_FACES) :
                for k in range(0, j) :
                    # No quad
                    if i != j and i != k :
                        n += 1
                        self.rankArray[(3*face[i]) + face[j] + face[k]] = n
                        
        # Low straight non-flush.
        n += 1
        self.rankArray[face[12] + face[0] + face[1] + face[2] + face[3]] = n

        # Usual straight non-flush.
        for i in range(0, 9) :
            n += 1
            self.rankArray[face[i] + face[i+1] + face[i+2] + face[i+3] + face[i+4]] = n

        # Flush not a straight.
        for i in range(5, NUMBER_OF_FACES) :
            for j in range(3, i) :
                for k in range(2, j) :
                    for l in range(1, k) :
                        for m in range(0, l) :
                            if not (i - m == 4 or (i == 12 and j == 3 and k == 2 and l == 1 and m == 0)) :
                                n += 1
                                self.flushRankArray[faceFlush[i] + faceFlush[j] + faceFlush[k] + faceFlush[l] + faceFlush[m]] = n       

        # Full house.
        for i in range(0, NUMBER_OF_FACES) :
            for j in range(0, NUMBER_OF_FACES) :
                if i != j :
                    n += 1
                    self.rankArray[(3*face[i]) + (2*face[j])] = n       

        # Quad.
        for i in range(0, NUMBER_OF_FACES) :
            for j in range(0, NUMBER_OF_FACES) :
                if i != j :
                    n += 1
                    self.rankArray[(4*face[i]) + face[j]] = n

        # Low straight flush.
        n += 1
        self.flushRankArray[faceFlush[0] + faceFlush[1] + faceFlush[2] + faceFlush[3] + faceFlush[12]] = n;
        
        # Usual straight flush.
        for i in range(0, 9) :
            n += 1
            self.flushRankArray[faceFlush[i] + faceFlush[i+1] + faceFlush[i+2] + faceFlush[i+3] + faceFlush[i+4]] = n
                
        return

    def getRankOfFive(self, card_1, card_2, card_3, card_4, card_5) :
        if (self.deckcardsSuit[card_1] == self.deckcardsSuit[card_2] and
            self.deckcardsSuit[card_1] == self.deckcardsSuit[card_3] and
            self.deckcardsSuit[card_1] == self.deckcardsSuit[card_4] and
            self.deckcardsSuit[card_1] == self.deckcardsSuit[card_5]) :
                    
            return self.flushRankArray[self.deckcardsFlush[card_1] +
                                       self.deckcardsFlush[card_2] +
                                       self.deckcardsFlush[card_3] +
                                       self.deckcardsFlush[card_4] +
                                       self.deckcardsFlush[card_5]]
        
        else :
                        
            return self.rankArray[self.deckcardsFace[card_1] +
                                  self.deckcardsFace[card_2] +
                                  self.deckcardsFace[card_3] +
                                  self.deckcardsFace[card_4] +
                                  self.deckcardsFace[card_5]]
        
        return -1
        
    def getRankOfSeven(self, CARD1, CARD2, CARD3, CARD4, CARD5, CARD6, CARD7) :
        seven_cards = [CARD1, CARD2, CARD3, CARD4, CARD5, CARD6, CARD7]
        five_temp = [0] * 5
        BEST_RANK_SO_FAR = 0
        CURRENT_RANK = 0
        m = 0
        
        for i in range(1, 7) :
            for j in range(0, i) :
                m = 0
                for k in range(0, 7) :
                    if k != i and k != j :
                        five_temp[m] = seven_cards[k]
                        m += 1
                        
                CURRENT_RANK = self.getRankOfFive(five_temp[0], five_temp[1], five_temp[2], five_temp[3], five_temp[4])
                if BEST_RANK_SO_FAR < CURRENT_RANK :
                    BEST_RANK_SO_FAR = CURRENT_RANK
                
        return BEST_RANK_SO_FAR

poker = []
with open('poker.txt', 'r') as f:
    for l in f:
        cards = l.split()
        poker.append([cards[:5], cards[5:]])

# Converts to SpecialKEval format
faces = {
    'A': 0,
    'K': 4,
    'Q': 8,
    'J': 12,
    'T': 16,
    '9': 20,
    '8': 24,
    '7': 28,
    '6': 32,
    '5': 36,
    '4': 40,
    '3': 44,
    '2': 48
}
suits = {
    'S': 0,
    'H': 1,
    'D': 2,
    'C': 3
}
def convert_card(c):
    return faces[c[0]]+suits[c[1]]

eva = FiveEval()
p1w = 0
for v in poker:
    cards = []
    for i in v[0]:
        cards.append(convert_card(i))
    p1 = eva.getRankOfFive(cards[0], cards[1], cards[2], cards[3], cards[4])
    cards = []
    for i in v[1]:
        cards.append(convert_card(i))
    p2 = eva.getRankOfFive(cards[0], cards[1], cards[2], cards[3], cards[4])
    if p1 > p2:
        p1w += 1

print p1w

print time.clock()-start
