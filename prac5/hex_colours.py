

COLOR_TO_MEMBER = {"absolutezero": "#0048ba",
                   "acidGreen": "#b0bf1a",
                   "aliceblue": "#f0f8ff",
                   "amaranth": "#e52b50",
                   "alizarincrimson": "#e32636",
                   "amber": "#ffbf00",
                   "amethyst": "#9966cc",
                   "antiquewhite": "#faebd7",
                   "blueviolet": "#8a2be2",
                   "cookiekiss": "#yj1919"}

color = input("Enter color name: ").lower().strip()
while color != "":
    if color in COLOR_TO_MEMBER:
        print(color, "is", COLOR_TO_MEMBER[color])
    else:
        print("Invalid color")
    color = input("Enter color name: ").upper().strip()
else:
    print("have a nice day")