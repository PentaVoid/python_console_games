#Import modules and libraries
import pyfiglet
import time
from rps import rps
from roullete import roullete
from guess import guess

from termcolor import colored

#Specialized text
cpt_text = pyfiglet.figlet_format("GAME HUB",
                                  font="standard",
                                  justify="center")

print(colored(cpt_text, 'red'))

cpt_text_name = pyfiglet.figlet_format("By Ayo", font="standard", justify="center", width=50, )

print(colored(cpt_text_name, 'blue'))
time.sleep(2)

#Human verification - Checks if user enters correct password, else crashes program if they fail twice
print("\u001b[1m"
      "HUMAN VERIFICATION"
      "\u001b[0m")
print("The password to play is "
      "\u001b[1m" + str(513) + "\u001b[1m")
print("\u001b[0m")
for i in range(2, -1, -1):
  try:
    password = int(
      input(f"\nEnter Password, you have {i} tries to do so: "
            "\u001b[1m"))
    print("\u001b[0m")
    if password == 513:
      print("\u001b[1m"
            "HUMAN VERIFICATION AUTHENTICATED..."
            "\u001b[0m")
      time.sleep(1)
      break
  except ValueError:
      if i <= 1:
        print("\u001b[1m" "Human verification failed, program will self destruct in.." "\u001b[0m")
        time.sleep(0.5)
        print("5")
        time.sleep(0.5)
        print("4")
        time.sleep(0.5)
        print("3")
        time.sleep(0.5)
        print("2")
        time.sleep(0.5)
        print("1")
        time.sleep(0.5)
        print("BYE!")
        quit()
      else:
        print("\nOops!  That was not a valid number.  Try again...")
      continue
  if password == 513:
    break
  
  elif i == 1:
    print("Human verification failed, program will self destruct in..")
    time.sleep(0.5)
    print("5")
    time.sleep(0.5)
    print("4")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("BYE!")
    quit()
  else:
    print("Incorrect, try again..")
    continue

#Allows user to choose what game they want to play infinetely
while True:
  print(
    "\n\n\nHere is a list of the possible games to play. To choose one, simply type the corresponding digit:\n\n1. Rock Paper Scissors\n2. Russian Roullete\n3. Animal Guesser\n\nType any other number or key to exit\n")
  choose_game = input("choice: "
    "\u001b[1m")
  print("\u001b[0m")

  #Checks if user chooses game, or quits, and runs based on   that input
  if choose_game == "1":
    print("\nChosen Game: Rock Paper Scissors\n\n\n")
    time.sleep(1)
    rps()
  elif choose_game == "2":
    print("Chosen Game: Russian Roullette\n\n\n")
    time.sleep(2)
    roullete()
  elif choose_game == "3":
    print("Chosen Game: Animal Guesser\n\n\n")
    time.sleep(2)
    guess()

  else:
    print("\n\n\nThanks for playing my games!")
    time.sleep(1)
    print("Have a great day!!!")
    print(
      "\nInfo:\n\nLibraries Used:\nPyfiglet for fancy text\nTime library for delayed text\nRandom Library for randomizing computer choice\nTerm Color for adding color to text"
    )
    break
