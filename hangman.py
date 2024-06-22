import random

words = ["Neptune", 'Jupiter', 'Saturn', 'Mercury', 'Mars', 'Earth', 'Venus']

chosen_word = random.choice(words)
display_word = ['_' for _ in chosen_word] # creat  alist of underscore
print(display_word)
attempts = 8

print(

    "welcome to Hangman"
)

while attempts > 0 and '_' in display_word:
    print("\n" +''.join(display_word))
    guess = input("Guess a letter: ").title()
    print(chosen_word)
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[index] = guess  # revealing letter
    else:
        print('the letter is not in the word!!!')
        attempts -= 1