#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play = "Y"
  while play == "Y":

    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    #Ask the user if they would like to play again.
    player = input("enter choice (R/P/S): ")

    if player == "R":
      print("player chose rock")
    elif player == "S":
      print("player chose scissors")
    elif player == "P":
      print("player chose paper")
    else:
      print("invalid option")

    computer = random.choice( ["R", "P", "S"] )
    if player == computer:
      print("TIE")
      ties = ties + 1
    elif player == "R" and computer == "S":
      print("You Win!")
      wins = wins + 1
    elif player == "R" and computer == "P":
      print("You lose.")
      losses = losses + 1
    elif player == "S" and computer == "R":
      print("You lose.")
      losses = losses + 1
    elif player == "S" and computer == "P":
      print("You Win!")
      wins = wins + 1
    elif player == "P" and computer == "R":
      print("You Win!")
      wins = wins + 1
    elif player == "P" and computer == "S":
      print("You lose.")
      losses = losses + 1
      
    play= input("Play Again? Y/N: ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
