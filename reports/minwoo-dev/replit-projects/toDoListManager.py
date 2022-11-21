import os, time

myToDoList = []

def changeColor(color):
  if color == "red":
    return ("\033[31m")
  elif color == "green":
    return ("\033[32m")
  elif color == "yellow":
    return ("\033[33m")
  elif color == "blue":
    return ("\033[34m")
  elif color == "purple":
    return ("\033[35m")
  elif color == "cyan":
    return ("\033[36m")
  else:
    return ("\033[0m")

def changeEffect(effect):
  if effect == "bold":
    return ("\033[1m")
  else:
    return ("\033[0m")

def printList():
  print()
  print(f"{changeColor('green')}TO-DO LIST{changeColor('reset')}")
  for item in myToDoList:
    print(item)
  print()

def addToList():
  print()
  item = input("What do you want to add? \n")
  if item in myToDoList:
    print()
    print(
      f"Item {changeColor('blue')}{item}{changeColor('reset')} already exists!"
    )
    print("Try again!")
    time.sleep(2)
    os.system("clear")
  else:
    myToDoList.append(item)
    print()
  time.sleep(1)
  os.system("clear")

def removeFromList():
  print()
  item = input("Which item have you completed? \n")
  if item in myToDoList:
    print()
    confirm = input("Are you sure you want to remove this? \n").lower()
    if confirm == "yes":
      myToDoList.remove(item)
      print()
      print(
        f"You have completed {changeColor('cyan')}{item}{changeColor('reset')}. Item has been removed."
      )
      print()
      time.sleep(3)
      os.system("clear")
    else:
      os.system("clear")
  else:
    print()
    print(
      f"Item {changeColor('yellow')}{item}{changeColor('reset')} was not on your todo list."
    )
    print()
    time.sleep(3)
    os.system("clear")

def viewList():
  listEmpty = len(myToDoList)
  if listEmpty == 0:
    print()
    message = "** Your TODO LIST is EMPTY. **"
    print(f"{changeColor('red')}{message}{changeColor('reset')}")
    print()
    time.sleep(2)
    os.system("clear")
  else:
    printList()
    time.sleep(5)
    os.system("clear")

def editList():
  print()
  item = input("Which item do you want to change? \n")
  if item in myToDoList:
    print()
    confirm = input("Are you sure you want to change this? \n").lower()
    if confirm == "yes":
      print()
      changeTo = input("What do you want it to change to? \n")
      for index in range(0, len(myToDoList)):
        if myToDoList[index] == item:
          myToDoList[index] = changeTo
      print()
      time.sleep(3)
      os.system("clear")
    else:
      os.system("clear")
  else:
    print()
    print(
      f"Item {changeColor('yellow')}{item}{changeColor('reset')} was not on your todo list."
    )
    print()
    time.sleep(3)
    os.system("clear")

def clearList():
  print()
  confirm = input("Are you sure you want to clear your list? \n").lower()
  if confirm == "yes":
    print()
    print(
      f"{changeColor('green')}Your todo list has been cleared successfully.{changeColor('reset')}"
    )
    time.sleep(2)
    os.system("clear")
  else:
    os.system("clear")

while True:
  titleText = f"{changeColor('green')}{changeEffect('bold')}MY TO-DO LIST MANAGER{changeEffect('reset')}{changeColor('reset')}"
  print(f"{titleText}")

  menuText = f"Do you want to {changeColor('green')}VIEW{changeColor('reset')}, {changeColor('green')}ADD{changeColor('reset')}, {changeColor('green')}EDIT{changeColor('reset')}, {changeColor('green')}REMOVE{changeColor('reset')} or {changeColor('cyan')}DELETE{changeColor('reset')} your todo list? \n"
  menu = input(f"{menuText}").lower()

  if menu == "add":
    addToList()
  elif menu == "view":
    viewList()
  elif menu == "edit":
    editList()
  elif menu == "remove":
    removeFromList()
  elif menu == "delete":
    myToDoList = []
    clearList()
  else:
    os.system("clear")
