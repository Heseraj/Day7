# This the hangman game
# it will be a review of previous lectures
#%%
word_list = ["ardvark", "baboon","camel", "Qudratullah"]
import random

chosen_word = random.choice(word_list)
display = []
dodis = []
for letter in chosen_word:
    display += "_"
print(display)

# for letter in range(chosen_word):
#     dodis += "__"
# print(dodis)

# print(f"for your help, the chose word is {chosen_word}")
#
# guess = input("please choose a letter").lower()
#
# for letter in chosen_word:
#     if guess == letter:
#         print(letter)
#     else:
#         print("_")



#%%
word_list = ["ardvark", "baboon","camel", "Qudratullah"]
import random

chosen_word = random.choice(word_list); print(chosen_word)
word_length = len(chosen_word)
print(word_length)

display = []

#when debuging, my system didn't accept "_"
for letter in chosen_word:
    display += "0"
print(display)

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("Please guess a letter! \n")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{''.join(display)}")
    if "0" not in display:
        end_of_game = True
        print("You won")

#%%
# import random
# word_list = ["ardvark", "baboon","camel", "Qudratullah"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# end_of_game = False
# lives = 6
#
# print(f"the chose word is {chosen_word}")
#
# display = []
# for i in range(chosen_word):
#     display += "_"
#
# print(display)

#
# while not end_of_game:
#     guess = input("Guess a letter").lower()
#
#     for position in len(word_length):
#         letter = chosen_word[position]
#         # print(f"current position: {position}\n current letter: {letter} \n Guessed letter: {guess}" )
#         if letter == guess:
#             display[position]= letter
#     if guess not in chosen_word:
#         lives -= 1
#         if lives != 0:
#             pass
#         else:
#             end_of_game = True
#         print("You lose")
#     print(f"{''.join(display)})")
#
#     if "_" not in display:
#         end_of_game = True
#         print("You won!")
#
    # print(stages[lives])
    

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

