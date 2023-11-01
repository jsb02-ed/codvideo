def rgb2yuv():
    # Getting values and checking range [0, 1]
    def get_color(color):
        value = input(f"Input {color} value: ")
        if float(value) < 0 or float(value) > 1:
            print("Colors must be in range [0, 1]")
            value = get_color(color)
        return float(value)
    
    color_list = ["R", "G", "B"]
    R, G, B = None, None, None  # Initialize variables

    # Assign user chosen values
    for color in color_list:
        if color == "R":
            R = get_color(color)
        elif color == "G":
            G = get_color(color)
        elif color == "B":
            B = get_color(color)

    # Compute YUV
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    U = 0.493 * (B - Y)
    V = 0.877 * (R - Y)
    return Y, U, V

YUV = rgb2yuv()
print("(Y, U, V) =", YUV)