import random

easy_words = ["apple","train","tiger","money","india"]
medium_words = ["python","bottle", "monkey","laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the password guessing game!")

while True:  # outer loop for replaying
    print("\nChoose difficulty level: easy, medium or hard")
    level = input('Enter difficulty: ').strip().lower()
    
    if level == "easy":
        secret = random.choice(easy_words)
    elif level == "medium":
        secret = random.choice(medium_words)
    elif level == "hard":
        secret = random.choice(hard_words)
    else:
        print("Invalid choice. Defaulting to easy level")
        secret = random.choice(easy_words)

    attempts = 0
    print("\nGuess the secret password!")

    while True:  # inner loop for guessing
        guess = input("Enter your guess: ").strip().lower()
        attempts += 1

        if guess == secret:
            print(f'🎉 Congratulations! You guessed it in {attempts} attempts')
            break

        # Generate hint
        hint = ""
        for i in range(len(secret)):
            if i < len(guess) and guess[i] == secret[i]:
                hint += guess[i]
            else:
                hint += "_"
        print("Hint: ", hint)

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break
