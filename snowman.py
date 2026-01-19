import game_logic

def play_again():
    while True:
        user_input = input("Do you want to play again?(Y/N): ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            return False
        else:
            print("Please enter a valid answer!")
            continue

def main():
    while True:
        game_logic.play_game()
        if not play_again():
            break



if __name__ == "__main__":
    main()