# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result


# Used to ask player if they want to play again
def again():
    print("Do you want to play again?")
    playagain = input()
    if playagain == "Yes":
        game()
    else:
        print("Goodbye.")

def game():
    import random
    global h_win
    global c_win
    global rnds
    global draws
    pos = ['true', 'false']
    rng = random.choice(pos)
    winner = play_once(rng)
    if winner == 1:
        print("You win!")
        h_win += 1
        rnds += 1
        print ("The current score is HUMAN:", h_win,"and CPU:", c_win,"." \
               "Human is winning ", (h_win/rnds * 100), " percent of the time.")
        again()
    elif winner == -1:
        print("I win!")
        c_win += 1
        rnds += 1
        print ("The current score is HUMAN:", h_win,"and CPU:", c_win,"." \
               "Human is winning ", (h_win/rnds * 100), " percent of the time.")
        again()
    else:
        print("Game drawn")
        draws += 1
        rnds += 1
        print ("The current score is HUMAN:", h_win,"and CPU:", c_win,"." \
               "Human is winning ", (h_win/rnds * 100), " percent of the time.")
        again()


h_win = 0
c_win = 0
draws = 0
rnds = 0


game()
