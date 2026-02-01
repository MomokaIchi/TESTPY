
# only roulette, with safety code, infinity roop, without money calc, without popup

import sys
import random
import time

# --- Utility for safe input ---

# for int number
def safe_input_int(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        raw = input(prompt)
        raw = raw.strip()
        try:
            value = int(raw)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter an integer between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid integer.")

# for choosing word (red or black)
def safe_input_color(prompt: str) -> str:
    while True:
        raw = input(prompt)
        raw = raw.strip().lower()
        if raw in ("red", "r"):
            return "red"
        elif raw in ("black", "b"):
            return "black"
        else:
            print("Please enter 'red' (r) or 'black' (b).")

# for choosing word (yes or no)
def safe_input_yes_no(prompt: str) -> bool:
    while True:
        raw = input(prompt)
        raw = raw.strip().lower()
        if raw in ("y", "yes"):
            return True
        elif raw in ("n", "no"):
            return False
        else:
            print("Please answer with 'yes' (y) or 'no' (n).")

# for choosing word (1 or 2)
def safe_input_yes_no(prompt: str) -> bool:
    while True:
        raw = input(prompt)
        raw = raw.strip()
        if raw in (1):
            return True
        elif raw in (2):
            return False
        else:
            print("Please answer with 'yes' (y) or 'no' (n).")

# --- ゲーム ロジック ---

def welcome():
    print("Welcome to my casino.")

def quit_game():
    print("See you again.")
    sys.exit()

def roulette_player():
    print("How to bet?\n1.only color\n2.number with color\n")

    number_player = safe_input_int("Choose your number (0-36): ", 0, 36)
    color_player = safe_input_color("Choose your color (red or black): ")
    return (number_player, color_player)

def roulette_luck():
    print("Rouletting...")
    time.sleep(1.5)
    number_roulette = random.randint(0, 36)
    color_flag = random.randint(0, 1)
    color_roulette = "red" if color_flag == 0 else "black"
    print(f"The ball had fallen in {number_roulette} of {color_roulette}.")
    return (number_roulette, color_roulette)

def roulette_game_loop():
    print("Welcome to the roulette.")
    while True:
        user_number, user_color = roulette_player()
        roulette_number, roulette_color = roulette_luck()

        # 判定
        if user_number == roulette_number and user_color == roulette_color:
            print("Your number and color is correct. Congratulations!")
        elif user_number == roulette_number:
            print("Your number is correct but the color is not.")
        elif user_color == roulette_color:
            print("Your color is correct but the number is not.")
        else:
            print("You lose.")

        # 続行確認
        if safe_input_yes_no("Do you want to continue? (y/n): "):
            continue
        else:
            quit_game()

# --- START ---
if __name__ == "__main__":
    welcome()
    roulette_game_loop()