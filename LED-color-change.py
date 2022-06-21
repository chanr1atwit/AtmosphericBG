import random

class Color:

    def __init__(self, r, g, b):
        self.r = min(r, 255)
        self.g = min(g, 255)
        self.b = min(b, 255)

    @classmethod
    def interpolate(colors, color1, color2, val):
        r = int((color2.r - color1.r) * val + color1.r)
        g = int((color2.g - color1.g) * val + color1.g)
        b = int((color2.b - color1.b) * val + color1.b)
        return colors(r, g, b)
    
    @classmethod
    def white(colors):
        return colors(255, 255, 255)

    @classmethod
    def black(colors):
        return colors(0, 0, 0)

    @classmethod
    def red(colors):
        return colors(255, 0, 0)

    @classmethod
    def green(colors):
        return colors(0, 255, 0)

    @classmethod
    def blue(colors):
        return colors(0, 0, 255)

    @classmethod
    def cyan(colors):
        return colors(0, 255, 255)

    @classmethod
    def yellow(colors):
        return colors(255, 255, 0)

    @classmethod
    def magenta(colors):
        return colors(255, 0, 255)

    @classmethod
    def setColors(colors):
        i = setColor.randint(0,7)
        return {
            '0': colors.white(),
            '1': colors.black(),
            '2': colors.red(),
            '3': colors.green(),
            '4': colors.blue(),
            '5': colors.cyan(),
            '6': colors.yellow(),
            '7': colors.magenta()
        }[str(i)]
    


