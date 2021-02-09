# Luke Gilin
import math

wall_H = float(input("Enter wall height (feet):\n"))
wall_W = float(input("Enter wall width (feet):\n"))

wall_A = wall_H * wall_W  # Calculate wall area

print("Wall area:", '{:.0f}'.format(wall_A), "square feet")

paintNeeded = wall_A / 350  # Calculate Paint needed for wall

print("Paint needed:", '{:.2f}'.format(paintNeeded), "gallons")

cansNeeded = math.ceil(paintNeeded)  # Rounds up the paint gallons needed to the nearest integer

print("Cans needed:", cansNeeded, "can(s)\n")

paintColor = input("Choose a color to paint the wall:\n")

paintColors = {'red': 35, 'blue': 25, 'green': 23}  # create dic of paint colors and prices
colorPrice = paintColors[paintColor] * cansNeeded  # multiply number of cans by the price of that color

print('Cost of purchasing {color} paint: ${price}'.format(color=paintColor, price=colorPrice))

