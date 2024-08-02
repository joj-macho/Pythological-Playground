import random

def main():
    '''Main function to run the Mad Libs Game.'''
    print('\nWelcome to Mad Libs!\n')

    while True:
        mad_lib()

        play_again = input('\nDo you want to create another story? (yes/no): ').lower()
        print()
        if play_again != 'yes':
            print('\nThanks for playing!')
            break

def mad_lib():
    '''Generate and print a Mad Libs story based on user input.'''
    while True:
        try:
            noun = input('Enter a noun (person, place, or thing): ').strip()
            plural_noun = input('Enter a plural noun: ').strip()
            noun2 = input('Enter another noun: ').strip()
            place = input('Enter a location (e.g., city, forest, beach): ').strip()
            adjective = input('Enter an adjective (describing word): ').strip()
            noun3 = input('Enter another noun related to the story: ').strip()

            if not noun or not plural_noun or not noun2 or not place or not adjective or not noun3:
                raise ValueError('Input cannot be empty.')

            break
        except ValueError as e:
            print('Error:', e)
            print('Please try again.\n')

    # Generate a random story from the user input
    stories = [
        'Once upon a time, in a mystical forest, there lived a brave ' + noun + ' who embarked on a quest to rescue a group of endangered ' + plural_noun + '. Along the journey, they encountered a wise ' + noun2 + ' who guided them through treacherous paths and enchanted ' + place + '. With their ' + adjective + ' courage, they vanquished the evil sorcerer and restored peace to the land.',
        'In the bustling city of ' + place + ', there was a renowned ' + noun + ' known for their extraordinary talent. They were admired by many for their dedication to helping the community and their commitment to justice. One day, they received a mysterious message asking for their help to solve a puzzling mystery involving missing ' + plural_noun + '. With their sharp wit and keen intellect, they unraveled the truth behind the disappearance and brought the culprit to justice.',
        'Deep beneath the ocean waves, there existed a hidden kingdom ruled by an ancient ' + noun + '. The kingdom was populated by majestic ' + plural_noun + ' and colorful ' + noun2 + '. However, their peaceful existence was threatened by a powerful ' + adjective + ' sea monster that terrorized the underwater realm. Determined to protect their home, a young ' + noun3 + ' embarked on a daring adventure to confront the monster and restore harmony to the seas.'
    ]
    story = random.choice(stories)

    print()
    print(story)

if __name__ == '__main__':
    main()