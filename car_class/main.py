from car import Car

car = Car(2001, "BMW M3 GTR")

print(f"""
Make: {car.get_make()}
Year: {car.get_year_model()}""")

print("Accelerating")
for i in range(5):
    car.accelerate()
    print(f"Car Speed: {car.get_speed()}")

print("Braking")
for i in range(5):
    car.brake()
    print(f"Car Speed: {car.get_speed()}")
