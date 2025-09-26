import random


story_themes = {
    "fantasy": [
        "A {adjective} {noun} explored the {place} with magic.",
        "In the {place}, a {adjective} {noun} found a dragon.",
        "The {adjective} {noun} wandered the {place} under stars."
    ],
    "sci-fi": [
        "A {adjective} {noun} scanned the {place} with a laser.",
        "In the {place}, a {adjective} {noun} met an alien.",
        "The {adjective} {noun} flew through the {place} in a ship."
    ],
    "mystery": [
        "A {adjective} {noun} searched the {place} for clues.",
        "In the {place}, a {adjective} {noun} solved a puzzle.",
        "The {adjective} {noun} hid in the {place} at midnight."
    ]
}

while True:
    
    print("Choose a theme: fantasy, sci-fi, mystery")
    theme = input("Enter your theme: ").lower()
    while theme not in story_themes:
        print("Invalid theme! Choose: fantasy, sci-fi, mystery")
        theme = input("Enter your theme: ").lower()

   
    noun = input("Enter a noun (e.g., cat, knight, tree): ")
    adjective = input("Enter an adjective (e.g., brave, shiny, tall): ")
    place = input("Enter a place (e.g., forest, castle, river): ")

    chosen_template = random.choice(story_themes[theme])

    
    story = chosen_template.format(noun=noun, adjective=adjective, place=place)
    print("\nYour Random Story:")
    print(story)

 
    again = input("\nWant to create another story? (yes/no): ").lower()
    if again != 'yes':
        print("Thanks for playing!")
        break
