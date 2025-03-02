# Day 4: Lesson 35: 100 Days of Python
# Project to create a Rock, Paper, Scissors Game

import random

# Rock, Paper, Scissors ASCII art
roc = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
pap = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scis = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

player_plays = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_plays = random.randint(0,2)

# 0 is Rock, 1 is Paper and 2 is Scissors
game_images = [roc, pap, scis]
print(game_images[player_plays])
print("Computer chose:", game_images[comp_plays], sep="\n")

def rock(com):
    '''
    Case: player chose rock
    If computer chose 0, it's a draw
    If computer chose 1, player loses
    If computer chose 2, player wins
    '''
    pl = 0
    if pl == com:
        return "It's a draw."
    if com == 1:
        return "You lose :("
    if com == 2:
        return "You win!"


def paper(com):
    '''
    Case: player chose paper
    If computer chose 0, player wins
    If computer chose 1, it's a draw
    If computer chose 2, player loses
    '''
    pl = 1
    if pl == com:
        return "It's a draw."
    if com == 0:
        return "You win!"
    if com == 2:
        return "You lose :("

def scissors(com):
    '''
    Case: player chose scissors
    If computer chose 0, player loses
    If computer chose 1, player wins
    If computer chose 2, it's a draw
    '''
    pl = 2
    if pl == com:
        return "It's a draw."
    if com == 0:
        return "You lose :("
    if com == 1:
        return "You win!"

# The Game
# 0 is Rock, 1 is Paper and 2 is Scissors
if player_plays == 0:
    print(rock(comp_plays))
elif player_plays == 1:
    print(paper(comp_plays))
elif player_plays == 2:
    print(scissors(comp_plays))
else:
    print("You typed an invalid number. You lose.")
