# spammerApp.py (soamming app using pretty printing) - fake with no actual spamming functions

import os, time

listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("LIST OF EMAIL")
  print()
  counter = 1
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter += 1
  time.sleep(1)

def sendSpam(max):
  for i in range(0, max):
    os.system("clear")
    print(f"""EMAIL {i + 1}
    
    Dearest {listOfEmail[i]},
    It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

    Love and hugs,
    Minwoo Spammington XI""")
    time.sleep(2)
    os.system("clear")

while True:
  print("SPAMMER Inc.")
  menu = input(
    "1. ADD email\n2. REMOVE email\n3. SHOW emails\n4. Get SPAMMING!\n> ")
  if menu == "1":
    email = input("EMAIL > ")
    listOfEmail.append(email)
  elif menu == "2":
    email = input("EMAIL > ")
    if email in listOfEmail:
      listOfEmail.remove(email) # no catch yet for email that doesn't exist yet (haha!)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    emailCount = len(listOfEmail)
    if emailCount == 0:
      os.system("clear")
      print("LIST OF EMAIL\n")
      print("(nothing here)")
      print()
      time.sleep(1)
    else:
      spamCount = int(input("How many emails do you want to spam?\n")) # only numbers, no catching code yet if user enters string or float
      if spamCount <= emailCount: 
        sendSpam(spamCount)
      elif spamCount > emailCount:
        print(f"You only have {emailCount} email(s) on your list.")
        time.sleep(1)
        os.system("clear")
  time.sleep(1)
  os.system("clear")
