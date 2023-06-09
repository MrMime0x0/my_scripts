import random

numbers = ["1", "10", "20", "70", "89"]

for _ in range(5):
    random_numbers = random.choice(numbers)
    print(random_numbers)
