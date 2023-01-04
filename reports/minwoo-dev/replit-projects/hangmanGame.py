# THIS IS A BACKBONE OF A HANGMAN GAME FROM DAY 39 IN REPLIT
# I want to add ASCII art to this but haven't done it yet. Will revamp this soon.

import random, os, time

wordList = [
  "conglomerate", "reality", "brevity", "persistence", "apropos", "scientific",
  "definition", "transportation", "genius", "program"
]
pickedLetter = []
tries = 6

chosenWord = random.choice(wordList)

while True:
  time.sleep(3)
  os.system("clear")
  letter = input("ENTER A LETTER > ").lower()

  if letter in pickedLetter:
    print("You already entered that one!")
    continue

  pickedLetter.append(letter)

  if letter in chosenWord:
    print()
    print("You guessed a correct letter!")
  else:
    print()
    print("Nope, it's not in the word!")
    tries -= 1

  allLetters = True
  print()
  for i in chosenWord:
    if i in pickedLetter:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print()
    print(f"You won with {tries} left!")
    break

  if tries <= 0:
    print()
    print(f"You ran out of lives! The answer was {chosenWord}")
    break
  else:
    print()
    print(f"Only {tries} left!")

