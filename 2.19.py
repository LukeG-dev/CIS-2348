# Luke Gilin 1216992
juiceNum = float(input("Enter amount of lemon juice (in cups):\n"))
waterNum = float(input("Enter amount of water (in cups):\n"))
agaveNum = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(juiceNum), "cup(s) lemon juice")
print('{:.2f}'.format(waterNum), "cup(s) water")
print('{:.2f}'.format(agaveNum), "cup(s) agave nectar\n")

servingsNum = float(input("How many servings would you like to make?\n\n"))

adjValue = servingsNum/servings  # Value to adjust servings by
juiceAdj = adjValue * juiceNum
waterAdj = adjValue * waterNum
agaveAdj = adjValue * agaveNum

print("Lemonade ingredients - yields", '{:.2f}'.format(servingsNum), "servings")
print('{:.2f}'.format(juiceAdj), "cup(s) lemon juice")
print('{:.2f}'.format(waterAdj), "cup(s) water")
print('{:.2f}'.format(agaveAdj), "cup(s) agave nectar\n")

print("Lemonade ingredients - yields", '{:.2f}'.format(servingsNum), "servings")
print('{:.2f}'.format(juiceAdj/16), "gallon(s) lemon juice")
print('{:.2f}'.format(waterAdj/16), "gallon(s) water")
print('{:.2f}'.format(agaveAdj/16), "gallon(s) agave nectar")
