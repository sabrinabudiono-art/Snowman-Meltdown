import random
import ascii_art

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def game_won(guessed_letters, secret_word):
    if len(secret_word) == len(guessed_letters):
        return True
    else:
        return False


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and not guess.isdigit():
            if guess in secret_word:
                guessed_letters.append(guess)
                correct_guessed_letters = set(guessed_letters)
                display_game_state(mistakes, secret_word, correct_guessed_letters)
                if game_won(correct_guessed_letters, secret_word):
                    print("Congratulations, you saved the snowman!")
                    break
            elif guess not in guessed_letters:
                mistakes += 1
                if mistakes >= 3:
                    print(f"Game Over! The word was:{secret_word}")
                    print(ascii_art.STAGES[mistakes])
                    user_input = input("Do you want to play again?(Y/N): ")
                    if user_input == "N":
                        break
                    elif user_input == "Y":
                        play_game()
                        break
                else:
                    display_game_state(mistakes, secret_word, guessed_letters)
        else:
            print("Please enter a valid input. (one letter, no numbers, not empty")
            continue