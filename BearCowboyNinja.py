# Filename: BearCowboyNinja.py
# Author: Jeff Butt
# Purpose: To simulate a game of Bear Cowboy Ninja.  In this the user will select the 
#          character.  Then the computer will randomly select the character.  Then a winner
#          will be determined.  The user will receive a point for a win and the computer will
#          receive a point for a loss.  The user will determine after each round if they want
#          to play again.  The game will continue until the user decides to quit.  
#          When the game ends the user will be provided with the frequency that each 
#          character was selected.
#--------------------------------------------------------------------------------------------

import random # imports the random library so that the computer can randomly select a character


#--------------------------------------------------------------------------------------------
# Function: getWinner(userChoice, cpuChoice)
# Purpose: Determines the winner of the game. 
# Args: userChoice (str), cpuChoice (str)
# Returns: The result of the game (str)
#--------------------------------------------------------------------------------------------
def getWinner(userChoice, cpuChoice):
    if userChoice == cpuChoice:
        return "It's a Draw!  No one wins!"
    elif (userChoice == 'bear' and cpuChoice == 'ninja') or \
         (userChoice == 'cowboy' and cpuChoice == 'bear') or \
         (userChoice == 'ninja' and cpuChoice == 'cowboy'):
        return "Congtrats.  You win!"
    else:
        return "CPU wins!"

#-----------------------------------------------------------------------------------
# Function: play()
# Purpose: To play the game.  This initiates the game, and manages the game loop
# Args: None
# Returns: None
#-----------------------------------------------------------------------------------
def play():
    choices = ['bear', 'cowboy', 'ninja'] #Choices to pick from for game
    userScore = 0 #User Score, set to 0
    computerScore = 0 #Computer Score, set to 0
    drawScore = 0 # The number of Draws set to 0

    #Dictionaries to keep track of user choice counts and cpu choice counts 
    userChoiceCounts = {choice: 0 for choice in choices} 
    cpuChoiceCounts = {choice: 0 for choice in choices}

    #Main Game Loop
    while True:
        print("\nChoose your move: (bear, cowboy, ninja)")
        userChoice = input().lower() #User input for their choice.  Moves to lowercase for consistency. 

        #Handles invalid user inputs 
        if userChoice not in choices:
            print("Invalid choice. Please choose from bear, cowboy, or ninja.")
            continue

        #Increments the user's choice
        userChoiceCounts[userChoice] += 1
      
        #Randomly selects the computer's choice
        cpuChoice = random.choice(choices)

        #Increment's the computers random choice
        cpuChoiceCounts[cpuChoice] += 1

        #Determines the winner
        result = getWinner(userChoice, cpuChoice)

        if result == "Congrats! You win!":
            userScore += 1 #Updating score for user win
        elif result == "CPU wins!":
            computerScore += 1 #Updating score for CPU win
        else:
            drawScore += 1 #Updating draw count for draws

        #Output the counts of choices made by the user and cpu after round ends
        print(f"\nYou chose: {userChoice}")
        print(f"Computer chose: {cpuChoice}")
        print(result)
        print(f"Score Stats: - You: {userScore}, Computer: {computerScore}, Tie: {drawScore}")

        end_game = False #end_game variable, to denote the end of the outer loop
        while True: #Loop to handle new round, or game exit
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again.lower() == "no" or play_again.lower() == "n":
                print("Thanks for playing!")
                end_game = True
                break #exit inner loop, end_game set to True, so it will trigger outer loop end also.  
            elif play_again.lower() == "yes" or play_again.lower() == "y":
                break #exit inner loop and play again
            else:
                print("\nInvalid input, try again") #Handle invalid input, stay in loop until fixed 
        if end_game == True:
            break #exit outer loop, end_game set to true.  

    # Print counts of choices made by user and cpu at game end.  
    print("\nChoice Counts:")
    print("User:")
    for choice, count in userChoiceCounts.items():
        print(f"{choice}: {count}")
        print("\nComputer:")
    for choice, count in cpuChoiceCounts.items():
            print(f"{choice}: {count}")
    print("\nTotal:")
    totalChoiceCounts = {choice: userChoiceCounts[choice] + cpuChoiceCounts[choice] for choice in choices}
    for choice, count in totalChoiceCounts.items():
        print(f"{choice}: {count}")

play() # Runs the game
