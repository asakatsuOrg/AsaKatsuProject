# MOKEDEX (Beast Information Database) Project from Replit.com
# backbone code (Day 42)

print("MokéBeast - The Non-Copyright Generic Beast Battle Game")

beastInfo = {
  "beastName": None,
  "type": None,
  "specialMove": None,
  "startHP": None,
  "startMP": None
}

print()

for name, value in beastInfo.items():
  beastInfo[name] = input(f"{name}: ").strip().title()
  
if beastInfo["type"] == "Fire":
  print("\033[31m", end="")
elif beastInfo["type"] == "Water":
  print("\033[34m", end="")
elif beastInfo["type"] == "Grass":
  print("\033[32m", end="")
elif beastInfo["type"] == "Flying":
  print("\033[0m", end="")
elif beastInfo["type"] == "Psychic":
  print("\033[35m", end="")
elif beastInfo["type"] == "Ice":
  print("\033[36m", end="")
else:
  print("\033[33m", end="")

print()
print(f"""Your MokéBeast is called {beastInfo['beastName']}. It is a(n) {beastInfo['type']} type with a special move of {beastInfo['specialMove']} currently with an HP of {beastInfo['startHP']} and an MP of {beastInfo['startMP']}.
  """)

# for name, value in beastInfo.items():
  # print(f"{name:<20}: {value}")
