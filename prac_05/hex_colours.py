COLOUR_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blue": "#0000ff",
    "brown": "#a52a2a"
}

colour_name = input("Enter colour name: ").lower()

while colour_name != "":
    try:
        print(COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()