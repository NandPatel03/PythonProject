import random
from collections import defaultdict

print ("2.4")
def initialize_deck():
  deck=[]
  face=['Ace','Deuce','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
  suit=['Hearts','Diamonds','Clubs','Spades']
  for i in suit:
    for j in face:
      deck.append((j,i))
  random.shuffle(deck)
  return deck

print ("2.5")
cards = {"Deuce":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10,"Jack":11, "Queen":12, "King":13, "A":14}

def is_straight_flush(hand):
  if is_flush(hand) and is_straight(hand):
      return True
  else:
      return False

def is_four_of_a_kind(hand):
  five_cards = [i[0] for i in hand]
  cards_counts = defaultdict(lambda:0)
  for v in five_cards:
    cards_counts[v]+=1
  if sorted(cards_counts.values()) == [1,4]:
    return True
  return False

def is_full_house(hand):
  five_cards = [i[0] for i in hand]
  cards_counts = defaultdict(lambda:0)
  for v in five_cards:
    cards_counts[v]+=1
  if sorted(cards_counts.values()) == [2,3]:
    return True
  return False

def is_flush(hand):
  suits = [i[1] for i in hand]
  if len(set(suits))==1:
      return True
  else:
      return False

def is_straight(hand):
  five_cards = [i[0] for i in hand]
  cards_counts = defaultdict(lambda:0)
  for v in five_cards:
    cards_counts[v] += 1
  rank_values = [cards[i] for i in five_cards]
  value_range = max(rank_values) - min(rank_values)
  if len(set(cards_counts.values())) == 1 and (value_range==4):
      return True
  else:
      if set(five_cards) == set(["A", "2", "3", "4", "5"]):
          return True
      return False

def is_three_of_a_kind(hand):
  five_cards = [i[0] for i in hand]
  cards_counts = defaultdict(lambda:0)
  for v in five_cards:
      cards_counts[v]+=1
  if set(cards_counts.values()) == set([3,1]):
      return True
  else:
      return False
def is_two_pair(hand):
    five_cards = [i[0] for i in hand]
    cards_counts = defaultdict(lambda:0)
    for v in five_cards:
      cards_counts[v]+=1
    if sorted(cards_counts.values())==[1,2,2]:
        return True
    else:
        return False
def is_pair(hand):
    five_cards = [i[0] for i in hand]
    cards_counts = defaultdict(lambda:0)
    for v in five_cards:
        cards_counts[v]+=1
    if 2 in cards_counts.values():
        return True
    else:
        return False

def check_hand(hand):
    if is_straight_flush(hand):
      return 9
    if is_four_of_a_kind(hand):
      return 8
    if is_full_house(hand):
      return 7
    if is_flush(hand):
      return 6
    if is_straight(hand):
      return 5
    if is_three_of_a_kind(hand):
      return 4
    if is_two_pair(hand):
      return 3
    if is_pair(hand):
      return 2
    return 1

print ("2.6")

hand_dict = {9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}
def play(hand1,hand2):
  hand1_rank=check_hand(hand1)
  hand2_rank =check_hand(hand2)
  if hand1_rank>hand2_rank:
    print(f'\nhand 1 wins\n \n{hand1}\n  {hand_dict[hand1_rank]}')
  else:
    print(f'\nhand 2 wins \n \n{hand2} \n {hand_dict[hand2_rank]}')

deck=initialize_deck()
hand1=[('Jack','Hearts'),('Ten','Hearts'),('Nine','Hearts'),('Eight','Hearts'),('Seven','Hearts')]
hand2=[('Five','Hearts'),('Six','Spades'),('Seven','Clubs'),('Eight','Diamonds'),('Nine','Hearts')]
play(hand1,hand2)
hand=set(hand1+hand2)
for i in hand:
  deck.remove(i)
