import time
import random

# Constants:
SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS',
            'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES',
         'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM',
          'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300  # 300 seconds (5 minutes) to solve the game.

# Data structures:
knownSuspectsAndItems = []
visitedPlaces = {}
currentLocation = 'TAXI'
accusedSuspects = []
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3
culprit = random.choice(SUSPECTS)

# Clue dictionary:
clues = {}


def initialize_clues():
    global clues
    for i, interviewee in enumerate(SUSPECTS):
        if interviewee in liars:
            continue

        clues[interviewee] = {}
        for item in ITEMS:
            if random.randint(0, 1) == 0:
                clues[interviewee][item] = PLACES[ITEMS.index(item)]
            else:
                clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
        for suspect in SUSPECTS:
            if random.randint(0, 1) == 0:
                clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
            else:
                clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]


def add_liar_clues():
    for liar in liars:
        liar_item_clue_index = random.randint(0, len(ITEMS) - 1)
        liar_suspect_clue_index = random.randint(0, len(SUSPECTS) - 1)
        liar_item_clue = PLACES[liar_item_clue_index]
        liar_suspect_clue = PLACES[liar_suspect_clue_index]
        clues[liar][ITEMS[liar_item_clue_index]] = liar_item_clue
        clues[liar][SUSPECTS[liar_suspect_clue_index]] = liar_suspect_clue


def display_intro():
    print('''
    You are a detective.
    A cat has gone missing.
    Your mission: Find the cat and the guilty party.

    You have only {} seconds to solve the case!
    '''.format(TIME_TO_SOLVE))
    print('While you are on your quest, type these simple one-letter commands and press Enter to do them:')
    print('M = Move to a new location')
    print('Q = Question the suspects')
    print('A = Accuse someone')
    print('S = Show the known facts')
    print('L = List the commands')
    print('C = Count the remaining accusations')
    print('X = Quit the game')


def get_command():
    return input('> ').upper().strip()


def move_to_location():
    print('You can move to these places:')
    for place in PLACES:
        print(place)
    print('To move, type the first letter of the place and press Enter.')
    moveTo = input('> ').upper()
    if moveTo in PLACE_FIRST_LETTERS:
        return PLACE_FIRST_LETTERS[moveTo]
    else:
        print('Invalid location.')
        return None


def process_command(command):
    global currentLocation

    if command == 'M':
        new_location = move_to_location()
        if new_location:
            currentLocation = new_location
            if currentLocation not in visitedPlaces:
                visitedPlaces[currentLocation] = ''
            if currentLocation == 'ZOO':
                print('You hear a distant lion roar.')
                random_item_index = random.randint(0, len(ITEMS) - 1)
                random_item = ITEMS[random_item_index]
                if random_item not in knownSuspectsAndItems:
                    print('You found', random_item)
                    visitedPlaces[currentLocation] += ' ' + random_item
            elif currentLocation == 'DUCK POND':
                print('You hear ducks quacking.')
                random_suspect_index = random.randint(0, len(SUSPECTS) - 1)
                random_suspect = SUSPECTS[random_suspect_index]
                if random_suspect not in knownSuspectsAndItems:
                    print('You found', random_suspect)
                    visitedPlaces[currentLocation] += ' ' + random_suspect
    elif command == 'Q':
        question_suspects()
    elif command == 'A':
        accuse_suspect()
    elif command == 'S':
        show_known_facts()
    elif command == 'L':
        display_commands()
    elif command == 'C':
        count_accusations()
    elif command == 'X':
        quit_game()
    else:
        print('Invalid command. Type "L" to list the available commands.')


def question_suspects():
    global currentSuspect

    print('You can question these suspects:')
    for suspect in SUSPECTS:
        print(suspect)
    print('To question, type the name of the suspect and press Enter.')
    question_suspect = input('> ').upper()
    if question_suspect in SUSPECTS:
        currentSuspect = question_suspect
        if currentSuspect in liars:
            print(currentSuspect, 'is a known liar and won\'t provide any useful clues.')
        else:
            display_clues(currentSuspect)
    else:
        print('Invalid suspect.')


def display_clues(suspect):
    print('Clues from {}:'.format(suspect))
    for item, clue in clues[suspect].items():
        print(item, ':', clue)


def accuse_suspect():
    global accusationsLeft

    if accusationsLeft <= 0:
        print('You have no accusations left.')
        return

    print('You can accuse these suspects:')
    for suspect in SUSPECTS:
        if suspect not in accusedSuspects:
            print(suspect)
    print('To accuse, type the name of the suspect and press Enter.')
    accused_suspect = input('> ').upper()
    if accused_suspect in SUSPECTS and accused_suspect not in accusedSuspects:
        accusationsLeft -= 1
        accusedSuspects.append(accused_suspect)
        if accused_suspect == culprit:
            print('Congratulations! You have correctly accused the guilty party:', culprit)
            quit_game()
        else:
            print('Sorry, that is not the guilty party.')
            if accusationsLeft > 0:
                print('You have', accusationsLeft, 'accusations left.')
            else:
                print('You have no accusations left.')
    else:
        print('Invalid suspect or already accused.')


def show_known_facts():
    print('Visited places:')
    for place, facts in visitedPlaces.items():
        print(place + ':', facts)
    print('Accused suspects:', accusedSuspects)
    print('Known clues:')
    for suspect, clue in clues.items():
        print(suspect + ':', clue)


def display_commands():
    print('M = Move to a new location')
    print('Q = Question the suspects')
    print('A = Accuse someone')
    print('S = Show the known facts')
    print('L = List the commands')
    print('C = Count the remaining accusations')
    print('X = Quit the game')


def count_accusations():
    print('Remaining accusations:', accusationsLeft)


def quit_game():
    print('Thanks for playing! Goodbye.')
    sys.exit()


def play_game():
    startTime = time.time()
    while True:
        print()
        print('Location:', currentLocation)
        print('Time remaining:', int(TIME_TO_SOLVE - (time.time() - startTime)), 'seconds')
        command = get_command()
        process_command(command)


def main():
    initialize_clues()
    add_liar_clues()
    display_intro()
    play_game()


if __name__ == '__main__':
    main()
