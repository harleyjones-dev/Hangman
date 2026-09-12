import random

words = ["judicial", "preference", "thesis", "reckless", 
         "trivial", "leg", "meaning", "crevice"] # word list can be expanded

hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,

    """
     +---+
     |   |
    [O]  |
    /|\\  |
    / \\  |
         |
    =========
    """
] # ai was used to generate the ascii art

win = 0
lost = 0
while True:
    attempted = []

    word = words[random.randint(0,len(words)-1)] # pick a word from the wordlist
    word_array = []

    for letter in word:
        word_array.append([letter, False])

    while len(attempted) < 8:
        guess = input("Enter a word/letter guess: ").lower()

        if guess.isdigit() or not guess.isalpha() and not guess == KeyboardInterrupt: # check input is valid
            print("Invalid input, please input a letter or word!")
            continue

        is_attempted = False
        for attempt in attempted:
            if attempt == guess:
                is_attempted = True

        if is_attempted:
            print("Already attempted, enter another guess!")
            continue

        if len(guess) == 1:
            index=0
            in_word = False
            for letter in word_array:
                if guess == letter[0]:
                    letter[1] = True
                    in_word = True

            if not in_word:
                attempted.append(guess)

            revealed_word = ""
            all_true = True
            for letter in word_array:
                if letter[1] == True:
                    revealed_word += letter[0]
                else:
                    revealed_word += "?"
                    all_true = False
            print(revealed_word)

            if all_true:
                break
        elif guess == word:
            print(word)
            break
        else:
            attempted.append(guess)

        print(hangman[len(attempted) - 1])
        print(attempted)

    if len(attempted) < 8:
        print("You won!")
        win += 1
    else:
        print("Bad luck you lost!")
        lost += 1

    exit = input("Would you like to try again (yes/no): ")
    if exit.lower()[0] == "n":
        print(f"You won {win} times and lost {lost} times!")
        print("Thanks for playing")
        break