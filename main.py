import random

# Result table: rows = player choice, columns = computer choice
# Index: 0 = Snake, 1 = Water, 2 = Gun
# Rules: Snake drinks Water (Snake wins), Water douses Gun (Water wins), Gun kills Snake (Gun wins)
table = [
    ["Draw", "Win", "Lose"],   # Player chose Snake
    ["Lose", "Draw", "Win"],   # Player chose Water
    ["Win", "Lose", "Draw"]    # Player chose Gun
]

print("=== Snake Water Gun ===")


choices = {
    0: "Snake",
    1: "Water",
    2: "Gun"
}

wins = draws = losses = 0

while True:
    # Computer picks a random choice (0, 1, or 2)
    computer = random.randint(0, 2)

    # Show the player their options
    print("Enter your choice:")
    print("0 for Snake")
    print("1 for Water")
    print("2 for Gun\n")

    player = int(input("Your choice: "))

    if player not in [0, 1, 2]:
        print("Invalid choice!")
    else:
        print("You picked:", choices[player])
        print("Computer picked:", choices[computer])

        # Look up the result using the table
        result = table[player][computer]

        if result == "Draw":
            print("It's a DRAW!")
            draws += 1
        elif result == "Win":
            print("You WIN!")
            wins += 1
        else:
            print("You LOSE!")
            losses += 1

        # Show current score after each round
        print(f"\nScore -> Wins: {wins} | Draws: {draws} | Losses: {losses}")

        again = input("\nPlay again? (y/n): ") #y -> Yes, n -> No
        if again.lower() != 'y':
            break

# Show final score when the player quits
print("\n=== FINAL SCORE ===")
print(f"Wins:   {wins}")
print(f"Draws:  {draws}")
print(f"Losses: {losses}")
print("\nThanks for playing!")
