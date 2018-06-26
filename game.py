def game():
  print('Select a sequence of length three consisting of the letters H (for heads) and T (for tails) and enter your choice letter by letter.')
 
  winCountU = 0
  winCountComp = 0
  gameCount = 0  
  your_choice_list = []
  computerChoiceList = []
  

  while True:
    a = raw_input('\n\nEnter the first letter of your choice:')
    if (a == 'H') or (a == 'T'):
      your_choice_list.append(a)
      break
    else:
      print('Your entry should be one of the letters: H or T')  
  
  
  while True:
    a = raw_input('Enter the second letter of your choice:')
    if (a == 'H') or (a == 'T'):
      your_choice_list.append(a)
      break
    else:
      print('Your entry should be one of the letters: H or T') 
  
  
  while True:
    a = raw_input('Enter the third letter of your choice:')
    if (a == 'H') or (a == 'T'):
      your_choice_list.append(a)
      break
    else:
      print('Your entry should be one of the letters: H or T')  
  
  a = '\n\nYou choose the sequence:'+your_choice_list[0]+your_choice_list[1]+your_choice_list[2]
  print(a)
  
  if your_choice_list[1] == 'H':
    computerChoiceList.append('T')
  
  elif your_choice_list[1] == 'T':
    computerChoiceList.append('H')
  for i in range(2):
    computerChoiceList.append(your_choice_list[i])
  
  b = '\nComputer choose the sequence:'+computerChoiceList[0]+computerChoiceList[1]+computerChoiceList[2]+'\n'
  
  print(b)
  
  while gameCount < 5:
    b = gameCount+1
    sentence = 'No of games played:'+ str(b)
    print(sentence)
    playList = []
    while True:
      while True:
        a = raw_input('\n\nToss the coin and enter H if its a head and T if its a tail:')
        if (a == 'H') or (a == 'T'):
          playList.append(a)
          break
        else:
          sentence = 'Your choice should be from the letters H or T.'
          print(sentence)
           
      if len(playList) >= 3:
        if playList[-3:] == your_choice_list:
          playList.insert(-3, '[')
          playList.append(']')  
          x = '' 
          for i in range(len(playList)):
            x+=playList[i]  
          sentence = '\n\nCongratulations, you win as your choice came up first:'+x 
          print(sentence)
          if gameCount != 4:
            sentence = '\n\nWe play again.' 
            print(sentence)
          winCountU+=1
          gameCount+=1 
          break
      
        elif playList[-3:] == computerChoiceList:
          playList.insert(-3, '[')
          playList.append(']')  
          x = '' 
          for i in range(len(playList)):
            x+=playList[i]  
          sentence = '\n\nComputer won as its choice came up first:'+x
          print(sentence)
          if gameCount != 4:
            sentence = '\n\nWe play again.'
            print(sentence)
          winCountComp+=1
          gameCount+=1
          break   
  
  if winCountComp < winCountU:
    sentence = 'Congratulations! You won as your winCount is:'+str(winCountU) +'and that of computer is:'+str(winCountComp)
    print(sentence) 
  elif winCountComp == winCountU:
    sentence = 'Congratulations! You made a draw as you won '+str(winCountU)+' times and that of computer won '+str(winCountComp)+' times.'        
    print(sentence) 
  else:
    sentence = 'Computer won the game as you won '+str(winCountU)+' times and the computer won '+str(winCountComp)+' times.'
    print(sentence)      


























