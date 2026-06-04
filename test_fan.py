from fan_01 import FanOne
from fan_02 import FanTwo

bg_yellow = "\033[43m"
bg_blue = "\033[1;34m"
reset = "\033[0m"

fan_one = FanOne()
fan_one.set_fan_status(True)

fan_two = FanTwo()

print(f"{bg_yellow}Fan One:{reset}")

current_status=fan_one.get_fan_status()
if current_status:
    print(f"{bg_yellow}Fan One Status: On{reset}")
elif not current_status:
    print(f"{bg_yellow}Fan one Status: Off{reset}")

current_speed = fan_one.get_fan_speed()
if current_speed == 1:
    print(f"{bg_yellow}Fan One Speed: SLOW{reset}")
elif current_speed == 2:
    print(f"{bg_yellow}Fan One Speed: MEEDIUM{reset}")
elif current_speed == 3:
    print(f"{bg_yellow}Fan One Speed: FAST{reset}")

print(f"{bg_yellow} Fan One Radius:{fan_one.get_fan_radius()}{reset}")
print(f"{bg_yellow} Fan One Color:{fan_one.get_fan_color()}{reset}")

print(f"{bg_blue}Fan Two:{reset}")

current_status=fan_two.get_fan_status()
if current_status:
    print(f"{bg_blue}Fan Two Status: On{reset}")
elif not current_status:
    print(f"{bg_blue}Fan Two Status: Off{reset}")

current_speed = fan_two.get_fan_speed()
if current_speed == 1:
    print(f"{bg_blue}Fan Two Speed: SLOW{reset}")
elif current_speed == 2:
    print(f"{bg_blue}Fan Two Speed: MEDIUM{reset}")
elif current_speed == 3:
    print(f"{bg_blue}Fan Two Speed: FAST{reset}")

print(f"{bg_blue} Fan Two Radius:{fan_two.get_fan_radius()}{reset}")
print(f"{bg_blue} Fan Two Color:{fan_two.get_fan_color()}{reset}")

