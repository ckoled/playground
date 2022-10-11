# import math

# g = 2**18
# g_sqrt = math.floor(math.sqrt(g))
# found = False
# for i in reversed(range((g//2)+1)):
#   for j in range(g_sqrt):
#     if i*j == g:
#       print(str(i))
#       print(str(j))
#       exit(0)

import random

options = {
  'rock': 0,
  'paper': 1,
  'scissors': 2
}

while True:
  com_pick = random.randint(0,2)
  player_pick = options[input('rock, paper, or scissors?: ')]

  print('i chose ' + list(options)[com_pick])
  if com_pick == player_pick:
    print('its a tie!')
  elif com_pick-1 == player_pick or (com_pick+1 < 0 and player_pick==2):
    print('you lose hahahaha!')
  else:
    print('you win this time!')