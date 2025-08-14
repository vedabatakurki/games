import random
import word_file
import hangman_stages

lives=6
chosen_word=random.choice(word_file.words)
print("The chosen word is:", chosen_word)  # Debugging line, can be removed later
print("Welcome to Hangman!")
# print("DEBUG:", chosen_word)  # Uncomment for debugging
print("The word has", len(chosen_word), "letters.")
display = ['_'] * len(chosen_word)
print(" ".join(display))
game_over=False
while not game_over:
    guessed_letter=input("guess a letter : ").lower()
    for position in range(len(chosen_word)):  
     letter = chosen_word[position]
     if letter==guessed_letter:
        display[position]=guessed_letter
    print(" ".join(display))
    if guessed_letter not in chosen_word:
       lives-=1
       if lives==0:
          game_over=True
          print("you lose")
    print(hangman_stages.stages[lives])
    if '_' not in display:
       game_over=True
       print("you win")




