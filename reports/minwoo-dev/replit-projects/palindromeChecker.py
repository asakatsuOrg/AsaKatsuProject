"""
# DAY 59 OF THE 100 DAYS OF CODE CHALLENGE
THIS IS A BLOCK COMMENT.
This is a short program that checks whether a word entered by the user is a palindrome or not.

A palindrome is a word that reads the same both forward and backwards, e.g. racecar, civic, poop, etc.

Used concepts here are: LOOPING, SLICING, and RECURSION

Writing commments per line to make sure that I understand how each line works aka how the program runs.
Corrections are most welcome!
""" 

# 'MY' SOLUTION (haha, it's not)        # sanfoundry.com
def palindrome(word):                   # define function palindrome taking the argument 'word'
  if len(word) <= 1:                    # if length of word is equals or less than one,
    return True                         # the function will evaluate the word as a palindrome
  else:                                 # if that is not the case,
    if word[0] == word[-1]:             # if the first and last letters of the word matches,
      return palindrome(word[1:-1])     # the function gets called recursively with the sliced word (first and last letters removed)
    else:                               # into the function again, else,
      return False                      # the first and last letters don't match so it isn't a palindrome

# REPLIT SOLUTION
# def palindrome(word):
#   if len(word) <= 1:
#     return True
#   if word[0] != word[-1]:
#     return False
#   return palindrome(word[1:-1])


word = input("Is this word a palindrome? > ").strip().upper()   # program asks for user input
if palindrome(word) == True:                                    # if the input gets entered as a parameter to the func palindrom() and if true,
  print(f"The word {word} is a palindrome.")                    # the word is printed as a palindrome
else:                                                           # if not, then
  print(f"The word {word} is not a palindrome.")                # the word is printed confirming that it isn't a palindrome
