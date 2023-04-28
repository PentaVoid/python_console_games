#Import modules and libraries
import random
import time

#Roullete function to be called based on user input
def roullete():
  print("\nARGHH, WHAT THE-")
  time.sleep(1.)
  print("\nWAKE UP PUNK!")
  time.sleep(1)
  print("\nWhere am I... argh my head hurts...")
  time.sleep(1.5)
  print("\nYou are hear to play a good game of Russian Roullete, hahahah!\nTake this gun, its already loaded with 1 bullet and there are two bullet holes, meaning a 50% chance to die HAHAHA!\nChoose which bullet hoe you will be shot with between 1 and 2, and then fire!")
  time.sleep(5)
  print("\nWHAT, NOOO I'M TOO YOUNG TO DIE!, USER ITS UP TO YOU TO SAVE ME. CHOOSE A NUMBER, AND CHOOSE WISELY!")
  time.sleep(3)
  
  
  #Runs indefinetely to allow user to keep playing game
  while True:
    user_choice = int(input("\nChoose the bullet hole between 1 and 2: " "\u001b[1m"))
    print("\u001b[0m")
    muzzle = [1, 2]
    muzzle_random = random.choice(muzzle)
    #Cheks if user choice is where muzzle is, if so, user        dies, and gives the option to play again, else lets user     play again
    if user_choice == muzzle_random:
      print("\nThe bullet is in...")
      time.sleep(2)
      print("HOLE NUMBER", muzzle_random)
      print("THE BULLET MATCHES, YOU DIE!")
      play_again = input("Would you like to play again, type y for yes an n for no(invalid input will automatically result in no): " "\u001b[1m")
      print("\u001b[0m")
      if play_again.lower() == "y":
        continue
      else:
        break  
    elif user_choice > 2:
      print("Invalid Input, try again.")
    else:
      print("\nThe bullet is in...")
      time.sleep(2)
      print("HOLE NUMBER", muzzle_random)
      print("Lucky, you live...\n")
      play_again = input("Would you like to play again, type y for yes an n for no(invalid input will automatically result in no): " "\u001b[1m")
      print("\u001b[0m")
      if play_again.lower() == "y":
        continue
      else:
        break
  
