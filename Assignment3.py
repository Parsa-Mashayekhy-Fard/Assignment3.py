import random

print("Hello Darkness my old friend...")
print("KING Dice is here")
print("In this game, you can toss a dice. if you got number 6 you're able to roll 2 times again ")

def roll_dice():
    return random.randint(1, 6)

def main():
    total_tosses = 0
    
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        total_tosses += 1
        
        print(f"You rolled a {result}!")

        if result == 6:
            print("Congratulations! You get two extra tosses!")
            for _ in range(2):
                input("Press Enter for the extra toss...")
                result = roll_dice()
                total_tosses += 1
                print(f"You rolled a {result}!")
        
        choice = input("Do you want to roll again? (yes/no): ").lower()
        if choice != 'yes':
            break

    print(f"Game Over! You rolled the dice {total_tosses} times.")

if __name__ == "__main__":
    main()