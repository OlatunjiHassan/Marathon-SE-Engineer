import random

HANGMAN = [
    "________",
    "|      |",
    "|      o",
    "|      |",
    '|     /|\\',
    "|      |",
    '|     / \\',
]

WORDS = ["LOVE", "COMPANIONSHIP", "RESPECT", "HUSBAND", "SLEEP", "HEARTS", "FUTURE", "MINE", "FOREVER"]
# WORDS = ["AAAAAAAAAAA", "AAAAA"]
class Hangman():
    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list("_" * len(self.word_to_guess))

    def find_indexes(self, letter):
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]
    
    def is_invalid_letter(self, input_):
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)
    
    def print_game_status(self):
        print("\n")
        print("\n".join(HANGMAN[:self.failed_attempts]))
        print("\n")
        print(" ".join(self.game_progress))

    def update_progress(self, letter, indexes):
        for index in indexes:
            self.game_progress[index] = letter


    def get_user_input(self):
        user_input = input("\nPlease type a letter: ")
        return user_input.upper()
    
    def play(self):
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            if self.is_invalid_letter(user_input):
                print("The input is not a letter!")
                continue

            if user_input in self.game_progress:
                print("You have already guessed that letter")
                continue

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                if self.game_progress.count("_") == 0:
                    print("\nYay! You win!")
                    print(f"The word is: {self.word_to_guess}")
                    quit()
            else:
                self.failed_attempts += 1
        print("\nOMG! You lost!")

if __name__ == "__main__":
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()




