import random

names = ["Jimmy", "Mem", "Timmy", "Dad", "Mr"]

for _ in range(5):
    random_name = random.choice(names)
    capitalized_name = random_name.capitalize()
    print(capitalized_name)
