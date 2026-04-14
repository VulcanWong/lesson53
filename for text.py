while True:
    from random import *
    a = input("rock, paper, scissors: ")
    b = choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {b}")
    if a == b:
        print("It's a tie!")
    elif (a == "rock" and b == "scissors") or (a == "paper" and b == "rock") or (a == "scissors" and b == "paper"):
        print("You win!")
    else:
        print("You lose!")
