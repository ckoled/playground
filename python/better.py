import random

choices = {
  'rock': 0,
  'paper': 1,
  'scissors': 2
}

comp_pick = random.randint(0,2)
player_in = input('rock, paper, scissors?: ')
player_pick = choices[player_in]
print('i chose ' + choices[comp_pick][0])
if comp_pick == player_pick:
  print('draw.')
if comp_pick