choices = ["bear", "cowboy", "ninja"]

def get_winner(player, cpu):
    if player == cpu:
        return "It's a tie!"
    elif (player == "bear" and cpu == "ninja") or \
         (player == "ninja" and cpu == "cowboy") or \
         (player == "cowboy" and cpu == "bear"):
        return "You win!"
    else:
        return "You lose!"
