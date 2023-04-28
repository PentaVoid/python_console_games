#Import libraries
import time
#function with triple nested for loop, that runs next for loop if they get answer correct
def guess():
  print("You will be given 3 clues to guess a chosen animal. You have 3 tries, good luck!\n\n")
  time.sleep(2)
  animals = ['dog', 'chicken', 'spider']
  for i in range(1,-2,-1):
    answer = input("I am a mammal, have 4 legs, and come in many different breeds.\nWhat Am I:  ")
    if answer.lower() == animals[0]:
      print("\nCorrect, unto the next game!")
      for j in range(1,-2,-1):
        answer_two = input("I am a type of bird, have 2 legs, and there are over 33 billion of me.\nWhat Am I:  ")
        if answer_two == animals[1]:
          print("\nCorrect, unto the next game!")
          for v in range(1,-2,-1):
            answer_three = input("I am an arachnid, I have 8 legs, and am REALLY GROSS.\nWhat Am I:  ")
            if answer_three == animals[2]:
              print("\nCORRECT!\nYou beat the game, now go play the other ones!")
              print("Well done")
              time.sleep(2)
              return 
            elif v == -1:
              print("SO CLOSE... but you lose")
              print("Thanks for playing!")
              time.sleep(1)
              
            else:
              print(f"\nIncorrect, you have {v + 1} tries left")
              continue
        elif j == -1:
          print("\nYou lose!")
          time.sleep(2)
          return
        else:
          print(f"\nIncorrect, you have {j + 1} tries left")
          continue
    elif  i == -1:
      print("\nYou lose!")
      time.sleep(2)
      break
    else:
      print(f"\nIncorrect, you have {i + 1} tries left")
      continue