import game_logic

def main():
    game_logic.play_game()
    user_input = input("Do you want to play again?(Y/N): ")
    if user_input == "Y":
        game_logic.play_game()


if __name__ == "__main__":
    main()