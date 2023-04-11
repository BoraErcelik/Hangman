import random

word_list = ["ardvark", "baloon", "camel"]
chosen_word= random.choice(word_list)
word_lenght = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}')

display = []

for _ in range(word_lenght):
  display += "_"
print(display)

guess = input("Guess a letter: \n").lower()

for position in range(word_lenght):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter

print(display) 
