import random


story_templates = [
    "A {adjective} {noun} explored the {place} with wonder.",
    "In the {place}, a {adjective} {noun} found a hidden treasure.",
    "The {adjective} {noun} danced through the {place} at dusk.",
    "A {noun} felt {adjective} while roaming the {place}.",
    "Deep in the {place}, the {adjective} {noun} discovered a secret."
]


noun = input("Enter a noun (e.g., cat, knight, tree): ")
adjective = input("Enter an adjective (e.g., brave, shiny, tall): ")
place = input("Enter a place (e.g., forest, castle, river): ")


chosen_template = random.choice(story_templates)


story = chosen_template.format(noun=noun, adjective=adjective, place=place)


print("\nYour Random Story:")
print(story)