import random

booze = {
        "Booze 2": "Mr",
        "Booze 3": "Ms",
        "Booze 4": "Doc"

}

for _ in range(3):
    random_booze_gen = random.choice(list(booze.keys()))
    print(random_booze_gen)
