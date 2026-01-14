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

def is_done(guessed_letters, secret_word):
    for letter in guessed_letters:
        if letter in secret_word and len(secret_word) == len(guessed_letters):
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
                my_set = set(guessed_letters)
                display_game_state(mistakes, secret_word, my_set)
                if is_done(my_set, secret_word):
                    print("Congratulations, you saved the snowman!")
                    break
            elif guess not in guessed_letters:
                mistakes += 1
                if mistakes >= 3:
                    print(f"Game Over! The word was:{secret_word}")
                    break
                else:
                    display_game_state(mistakes, secret_word, guessed_letters)
        else:
            print("Please enter a valid input. (one letter, no numbers, not empty")
            continue