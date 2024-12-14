import random

def choose_word(word_list):
    return random.choice(word_list)

def update_result(word, guess, result):
    return ''.join([guess if word[i] == guess else result[i] for i in range(len(word))]) 

def play_game(word_list):
    rd_word = choose_word(word_list)
    result = '_' * len(rd_word)
    guessed_letters = set()

    while '_' in result:
        print(f"Words to Guess: {result}")
        guess = input("Guess the letter :").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in rd_word:
            result = update_result(rd_word, guess, result)
        else:
            print(f"{guess} is not in the word.")
    print(f"You Winner this is word :{rd_word}")



word_list = ["python", "jave", "askcom", "lombear", "somewall"]
play_game(word_list)
