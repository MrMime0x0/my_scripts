import random

def generate_story():
    characters = ['John', 'Mary', 'Alex', 'Emma']
    places = ['park', 'beach', 'forest', 'city']
    actions = ['ran', 'laughed', 'sang', 'danced']
    feelings = ['happy', 'sad', 'excited', 'nervous']

    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)
    feeling = random.choice(feelings)

    story = f"Once upon a time, {character} went to the {place}. They {action} and felt {feeling}."

    return story

random_story = generate_story()
print(random_story)
