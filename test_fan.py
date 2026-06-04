bg_yellow = "\033[43m"
bg_blue = "\033[44m"
reset = "\033[0m"

class Fan:
    def __init__(self, speed, radius, color):
        self.__speed = speed
        self.__radius = radius
        self.__color = color

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

SLOW = 1
MEDIUM = 2
FAST = 3
