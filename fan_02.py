class FanTwo:
    bg_blue = "\033[1;34m"
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self,fan_speed=2,fan_status=False,fan_radius=5, fan_color = "blue"):
        super().__init__(fan_speed,fan_status,fan_radius,fan_color)
my_fan=FanTwo()
