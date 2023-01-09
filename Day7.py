# This the hangman game
# it will be a review of previous lectures

#%%

import random
from hangman_words import word_list
from hangman_art import stages, logo
import replit

#be careful to define the module in actual environment
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
print(word_length)

display = []

#when debuging, my system didn't accept "_"
for letter in chosen_word:
    display += "*"
print(display)

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("Please guess a letter! \n")
    replit.clear()
    if guess in display:
        print("you've already chosen this letter!")
        lives = lives
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"your guessed letter was {guess} but it is not in the chosen word \n "
              f"you lose one lives and only have {lives} left.")
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"the chosen word was {chosen_word}")

    print(f"{''.join(display)}")
    if "*" not in display:
        end_of_game = True
        print("You won")
    print(stages[lives])
    

#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%

