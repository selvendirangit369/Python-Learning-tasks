import random

def choose_flowers():
    flowers = ['rose', 'lilly', 'jasmine', 'sunflower', 'lotus']
    return random.choice(flowers)

def display_hangman(tries):
    stages = [
        """
           ------
           
               
           |    
           |
           |
        """,
        """
           ------
           |    
           |    
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
    ]
    return stages[tries]

def play_hangman():
    flowers = choose_flowers()
    flowers_completion = "_" * len(flowers)
    guessed = False
    guessed_letters = []
    guessed_flowers = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(flowers_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in flowers:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                flowers_completion = "".join([letter if letter in guessed_letters else "_" for letter in flowers])
                print("Current word: " + flowers_completion)  # Show current word state
                if "_" not in flowers_completion:
                    guessed = True
        elif len(guess) == len(flowers) and guess.isalpha():
            if guess in guessed_flowers:
                print("You already guessed that word.")
            elif guess != flowers:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_flowers.append(guess)
            else:
                guessed = True
                flowers_completion = flowers
        else:
            print("Invalid input. Please try again.")

        print(display_hangman(tries))
        print("\n")

    if guessed:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you've run out of tries. The word was '{flowers}'.")

if __name__ == "__main__":
    play_hangman()
