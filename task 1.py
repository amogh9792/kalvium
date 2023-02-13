# Rock Paper Scissors program
import ast
import json


def game_outcome(player1, player2):
    if player1 == player2:
        return "Draw"
    elif player1 == "rock" and player2 == "scissors":
        return "Player 1 Wins"
    elif player1 == "scissors" and player2 == "paper":
        return "Player 1 Wins"
    elif player1 == "paper" and player2 == "rock":
        return "Player 1 Wins"
    else:
        return "Player 2 Wins"

def highest_score(player1_name, player1_score, player2_name, player2_score):
    if player1_score > player2_score:
        return f"{player1_name} has the highest score with {player1_score} points."
    elif player2_score > player1_score:
        return f"{player2_name} has the highest score with {player2_score} points."
    else:
        return "Both players have the same score."

# Store player names and scores in a dictionary
player_data = {}

# Continuously play the game until the player chooses to quit
while True:
    with open("player_data.txt", "r") as f:
        data=f.read()
    d=ast.literal_eval(data)
    print(d)
    player1 = input("Player 1, choose rock, paper, or scissors: ")
    player2 = input("Player 2, choose rock, paper, or scissors: ")

    outcome = game_outcome(player1, player2)
    print(outcome)

    # If player 1 wins, add 1 to their score
    if outcome == "Player 1 Wins":
        if "player1" in player_data:
            player_data["player1"] += 1
        else:
            player_data["player1"] = 1
    # If player 2 wins, add 1 to their score
    elif outcome == "Player 2 Wins":
        if "player2" in player_data:
            player_data["player2"] += 1
        else:
            player_data["player2"] = 1
    # No scores are added for a draw

    highest_score_message = highest_score("player1", player_data.get("player1", 0), "player2", player_data.get("player2", 0))
    print(highest_score_message)

    # Ask the player if they want to quit
    quit = input("Would you like to quit? (yes/no): ")
    if quit == "yes":
        break

# Store the player data in a file
with open("player_data.txt", "w") as f:
    f.write(str(player_data))

print("Thanks for playing!")
