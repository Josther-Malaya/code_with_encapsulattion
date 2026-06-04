from pet import Pet
bg_yellow = "\033[1;33m"
bg_green = "\033[1;32m"
bg_red = "\033[1;31m"
bg_reset = "\033[0;0m"

input_name = input("Enter the name of your pet: ")

while True:
    try:
        input_age = int(input("Enter the age of your pet: "))
        break
    except ValueError:
        print("A valid age should be a number")
    else:
        continue

input_animal_type = input("Enter the type of your pet: ")

my_pet = Pet(input_name,input_age,input_animal_type)
my_pet.get_name()
my_pet.get_age()
my_pet.get_animal_type()

print(f"The name of your pet is {bg_yellow}{my_pet.get_name()}{bg_reset} ")
print(f"His/her age is {bg_green}{my_pet.get_age()}{bg_reset} ")
print(f"The animal type is: {bg_red}{my_pet.get_animal_type()}{bg_reset} ")


