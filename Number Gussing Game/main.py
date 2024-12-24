# Number Guessing Game
import random
import time

# Entries Handler
def entry_handler():
    invalid_entry = 0
    max_invalid_entry = 10
    while True:
        if invalid_entry < max_invalid_entry:
            print(f"\n1. Easy: Unlimited Attempts")
            print(f"2. Medium: 10 Attempts")
            print(f"3. Hard: 5 Attempts")
            print(f"0. Exit")
            entry = input("Enter which Level you want: ")
            random_number = random.randint(1, 100)
            time.sleep(1)    # # Delay For 1 Second

            # Levels Handling
            # Easy
            if entry == "1":
                print(f"Selected Level: 'Easy' with Unlimited attempts")
                game_handler(random_number, max_attempt=1000)
                break
            # Medium
            if entry == "2":
                print(f"Selected Level: 'Medium' with 10 attempts")
                game_handler(random_number, max_attempt=10)
                break
            # Hard
            if entry == "3":
                print(f"Selected Level: 'Hard' with 5 attempts")
                game_handler(random_number, max_attempt=5)
                break
            # Exit Handler
            elif entry == "0":
                print(f"Generated Random Number: {random_number}")
                print("Thank you...")
                exit()
            else:
                invalid_entry +=1
                print("\nInvalid Level Input !!")
                continue
        else:
            print("You have Reached Maximum Limit of Invalid Entry")
            print("Thank you...")
            break

def game_handler(random_number, max_attempt):
    attempts = 0
    while True:
        attempts +=1
        player_input = int(input("Enter your Guess: "))
        print(attempts, max_attempt, attempts <= max_attempt)
        time.sleep(1)    # Delay For 1 Second
        if attempts < max_attempt:
            if player_input >= 1 and player_input <= 100:
                if player_input > random_number:
                    print("Your Guess is 'Too High'")
                elif player_input < random_number:
                    print("Your Guess is 'Too Low'")
                else:
                    print(f"\nHooray You have Guessed The Number {random_number}")
                    print(f"Taken Attempts: {attempts}")
                    break
            else:
                print("\nPlease Enter a Valid Guess between '1 - 100'.")
                continue
        else:
            print("\nSorry, You have No More Attempts Left.")
            print(f"The Random Number: {random_number}")
            print("Thank You...")
            break

def main():
    # Variables
    start_num = 1
    end_num = 100
    print(f"\n{"*"*40}\nWelcome To Number Guessing Game")
    time.sleep(2)    # Delay For 2 Second
    print("Hey we have Generated a Random Number Between (1 - 100).")
    print("Try to Guess it and we will help you by some 'HINTS'.")
    print(f"{"*"*40}")

    # Entries Handler
    entry_handler()

    print(f"{"*"*40}\n")
if __name__ == "__main__":
    main()