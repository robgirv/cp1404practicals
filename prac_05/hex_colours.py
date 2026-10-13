"""
CP1404 Prac 5: Hex Colours
"""

COLOUR_TO_HEX = {"aliceblue": "#f0f8ff", "amethyst": "#9966cc", "aqua": "#00ffff", "crimson": "#dc143c",
                 "dark byzantium": "#5d3954", "darkorchid4": "#68228b", "denim": "#1560bd", "ebony": "#555d50",
                 "emerald": "#50c878", "gold2": "#eec900"}

for colour, colour_hex in COLOUR_TO_HEX.items():
    print(f"{colour} is {colour_hex}")

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_HEX[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()
