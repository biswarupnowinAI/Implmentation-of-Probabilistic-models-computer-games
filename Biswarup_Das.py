


def play_game():
  import game as p
  print('\n\n*****************************************************************************\nDescription of the game you\'ll play in each of the 5 turns:\n\nTake a coin and denote heads by H and tails by T. Select a sequence of length three as you wish, consisting of heads (denoted H) and tails (denoted T), e.g. your choice could be HHT or TTH or HHH or TTT etc.The computer will ask you to enter your choice. The computer will then make its own choice of a sequence of length three with heads and tails.\n\nStart the game:\n\nYou toss the coin. If its heads, you enter H, if its tails, you enter T. Then again you toss the coin and enter what comes up and go on doing this, thereby getting a series of heads and tails e.g. HHTTHHTTTH......\n\n\nWinning rule:\nYou win (and the game stops) the moment you see the sequence of length three which you have selected, occuring side by side, in this series of H\'s and T\'s. The computer wins if the same happens with its choice.\n\nFor your convenience, the computer will keep a track of the occurences of heads and tails as you go on tossing, and it will point out the moment there is a match. In case you think this is a trick, well its not! Keep track of heads and tails yourself if you like, should you choose not to trust the computer on this!\n\nPLEASE TOSS THE COIN PROPERLY, ELSE IT WONT\'T BE RANDOM REALLY! \n********************************************************************************')

  while True:
    a = raw_input('\n\nPress Y to continue and N to quit:')

    if (a == 'Y') or (a == 'y'):
      p.game()
      break
    elif (a == 'N') or (a == 'n'):
      print('Thank you for your time!')
      break 
    else:
      print('Please enter a valid choice.')
 
sentence = '*****************************************************************************\n\nThis is to demonstrate that given the best choice you could make, the computer could make a choice even better! Here we go:\n\nYou\'ll play a purely random game with the computer, five times.\nAfter 5 turns, we will count how many times you won the game and the same for the computer. Whoever\'s count is more, wins!\n\nYou will have an edge over the computer when you start in the sense that its you who will make the first choice and also you\'ll be in charge of bringing in randomness in the game as well through tossing a coin, as will be explained later.\n\nHere\'s the challenge: If its really played randomly, you can never win over the computer even if you are making the game random yourself!\n********************************************************************************'
print(sentence)

while True:
  a = raw_input('\n\n\nPress Y to continue or N to quit:')

  if (a == 'y') or (a == 'Y'):
    play_game()
    break

  elif (a == 'n') or (a == 'N'):
    print('\n\nThanks for your time!')
    break
  else:
    print('\nPlease enter a valid choice.')


