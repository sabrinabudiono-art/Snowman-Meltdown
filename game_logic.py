import random
import ascii_art

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, correct_guessed_letters):
    """
    Display the snowman stage for the current number of mistakes.
    """
    print(ascii_art.STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in correct_guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def get_random_word():
    """
    Selects a random word from the list.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def game_won(correct_guessed_letters, secret_word):
    """
    returns True if the length of the correctly guessed letter set matches length of the secret word set.
    """
    if len(set(secret_word)) == len(set(correct_guessed_letters)):
        return True
    else:
        return False


def play_game():
    """
    starts the game loop.
    """
    secret_word = get_random_word()
    correct_guessed_letters = []
    mistakes = 0
    max_mistakes = 3

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, correct_guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and not guess.isdigit() and guess.isalpha():
            if guess in secret_word:
                correct_guessed_letters.append(guess)
                display_game_state(mistakes, secret_word, correct_guessed_letters)
                if game_won(correct_guessed_letters, secret_word):
                    print("Congratulations, you saved the snowman!")
                    break
            elif guess not in secret_word:
                mistakes += 1
                if mistakes == max_mistakes:
                    print(f"Game Over! The word was:{secret_word}")
                    print(ascii_art.STAGES[mistakes])
                    break
                else:
                    display_game_state(mistakes, secret_word, correct_guessed_letters)
        else:
            print("Please enter a valid input. (one letter, no numbers, not empty")
            continue
