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
def main():
    """ask user input colors and give numbers back"""
    color = input("Enter color name: ").lower().strip()
    while color != "":
        check_color_number(color)
        color = input("Enter color name: ").lower().strip()
    else:
        print("have a nice day")

def check_color_number(input_color):
    """check the number for a chosen color"""
    if input_color in COLOR_TO_MEMBER:
        print(input_color, "is", COLOR_TO_MEMBER[input_color])
    else:
        print("Invalid color")


main()