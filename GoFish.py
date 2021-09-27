from random import randint
import sys
def DrawCard(hand):
  hand = hand.append(randint(1,11))
  return hand

def Hand():
  L = []
  for i in range(5):
    L.append(randint(1,11))
  return L

def War(H1, H2):
  if int(sum(H1)) > int(sum(H2)):
    print(sum(H1), ': your points')
    print(sum(H2), ': opponent points')
    print('YOU WIN!!!')
  elif sum(H1) < sum(H2):
    print(sum(H1), ': your points')
    print(sum(H2), ': opponent points')
    print('YOU LOSE')
  elif sum(H1) == sum(H2):
    print('Draw!!!')

def GoFish(H1, H2):
  if len(H1) < 1:
       CheckPoints(H1, H2)
  H1 = Pairs(H1)
  points = 0
  print('your cards: ', H1)
  print('their cards: ', H2)
  print('choose card to fish for out of: ', len(H1), 'cards')
  choice = int(input())-1
  print('You chose: ', H1[choice])
  for H1[choice] in H2:
    print('You caught one!')
    points = points + 1
    H1.pop(choice)
    for i in range(len(H2)):
      if H2[i] == H1[choice]:
        H2.pop(i)
    AIFish(H2, H1)
  else:
      print('GO FISH')
      DrawCard(H1)
      AIFish(H2, H1)
    
def AIFish(H, H2):
  if len(H) < 1:
    CheckPoints(H, H2)
  H = Pairs(H)
  print('opponents turn.....')
  AIpoints = 0
  choice = randint(0, len(H)-1)
  print('They chose: ', H[choice])
  for H[choice] in H2:
      print('They caught one!')
      AIpoints = AIpoints + 1
      H.pop(choice)
      if H[choice] == enumerate(H2):
        H2.pop(H2.en)
      GoFish(H2, H)
  else:
      print('No Match for oppenent, GO FISH')
      DrawCard(H)
      GoFish(H2, H)
  

def CheckPoints(H, H2):
  if H > H2:
    return('YOU WIN!')
    sys.exit()
  elif H < H2:
    print('You Lose!')
    sys.exit()
  else:
    print('DRAW!')
    sys.exit() 

def Pairs(x):
  return list(dict.fromkeys(x))
    



print('**************************************')
print('************POKER_N_STUFF*************')
print('**************************************')

h1 = Hand()
h2 = Hand()

print(h1)
print(' ')
print(h2)

GoFish(h1,h2)
