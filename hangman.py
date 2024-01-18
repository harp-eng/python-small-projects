import random
import os
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list =['harry','jeevan','sukhi','tooti']
display_list=[]
random_word = random.choice(word_list)
lifes=6
for x in range(0,len(random_word)):
        display_list.insert(x,'_')
        
while(lifes>0):
    matched=0
    guess_word = input('input char :')
    os.system('clear')
    for x in range(0,len(random_word)):
            if(guess_word==random_word[x]):
                display_list[x]=random_word[x]
                matched=1
    if(display_list.count('_')==0):
        print('you win')
        lifes=0
    else:
        if(matched==0):
            lifes-=1
            if(lifes==0):
                print('you lose')
                print(f"guess word : {random_word}")
        print(stages[6-lifes])
    print(display_list)
    
    