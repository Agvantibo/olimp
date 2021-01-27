class color:
    r = 0
    g = 0
    b = 0

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def to_hex(self):
        return '#'+code(abs(int(self.r)))+code(abs(int(self.g)))+code(abs(int(self.b)))

    def to_tuple(self):
        return (int(self.r), int(self.g), int(self.b))


#made by dima savchenko at 23:36 1.12.2020
#Павел Александрович: увидите это- знайте, мой код!

def digit(x):
    if x <= 9:
        return str(x)
    elif x == 10:
        return 'a'
    elif x == 11:
        return 'b'
    elif x == 12:
        return 'c'
    elif x == 13:
        return 'd'
    elif x == 14:
        return 'e'
    elif x == 15:
        return 'f'
    else:
        return 'f'


def real_color(r, g, b):
    minimal = min([r, g, b])
    return r - minimal, g - minimal, b - minimal,minimal


def code(x):
    a = x // 16
    b = x % 16
    return digit(int(a)) + digit(int(b))


def color_code(r, g, b):
    return '#'+code(r)+code(g)+code(b)

def gradient(starter_color, finale_color, length):
    deltas = color(starter_color.r - finale_color.r,
    starter_color.g - finale_color.g, starter_color.b - finale_color.b)
    scales = color(deltas.r / length, deltas.g / length, deltas.b / length)
    midcolor = starter_color
    for i in range(length):
        midcolor.r += scales.r
        midcolor.g += scales.g
        midcolor.b += scales.b
        print(midcolor.to_hex())
        yield midcolor.to_hex()
