import sys
import random
import time
import bext

# Animation Constants
WIDTH, HEIGHT = bext.size()  # Get the console size
WIDTH -= 1  # Reduce width by 1 to fit within screen boundaries

# DVD logo set-up
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries
COLOR = 'color'
X_POSITION = 'x'
Y_POSITION = 'y'
DIRECTION = 'direction'

def main():
    '''Main function to run the bouncing DVD logos animation.'''
    # Start by clearing the console
    bext.clear()

    logos = generate_logos(NUMBER_OF_LOGOS)
    corner_bounces = 0

    while True:
        # Animate each logo object
        for logo in logos:
            bext.goto(logo[X_POSITION], logo[Y_POSITION])
            print('   ', end='')

            bounce_direction = logo[DIRECTION]

            if handle_bounce(logo):
                corner_bounces += 1

            # Change logo color on direction change
            if logo[DIRECTION] != bounce_direction:
                logo[COLOR] = random.choice(COLORS)

            # Move the logo's position based on direction
            if logo[DIRECTION] == UP_RIGHT:
                logo[X_POSITION] += 2
                logo[Y_POSITION] -= 1
            elif logo[DIRECTION] == UP_LEFT:
                logo[X_POSITION] -= 2
                logo[Y_POSITION] -= 1
            elif logo[DIRECTION] == DOWN_RIGHT:
                logo[X_POSITION] += 2
                logo[Y_POSITION] += 1
            elif logo[DIRECTION] == DOWN_LEFT:
                logo[X_POSITION] -= 2
                logo[Y_POSITION] += 1

        # Display corner bounce count and logos
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', corner_bounces, end='')

        for logo in logos:
            bext.goto(logo[X_POSITION], logo[Y_POSITION])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)

def generate_logos(number_of_logos):
    '''Generate a list of logo dictionaries with random positions and directions.'''
    logos = []
    for _ in range(number_of_logos):
        logo = {
            COLOR: random.choice(COLORS),
            X_POSITION: random.randint(1, WIDTH - 4),
            Y_POSITION: random.randint(1, HEIGHT - 4),
            DIRECTION: random.choice(DIRECTIONS)
        }
        if logo[X_POSITION] % 2 == 1:
            # Make sure X_POSITION is even so it can hit the corner.
            logo[X_POSITION] -= 1
        logos.append(logo)
    return logos

def handle_bounce(logo):
    '''Handles logo bouncing logic.'''
    # Check if logo hits the corners and update direction accordingly
    if logo[X_POSITION] == 0 and logo[Y_POSITION] == 0:
        logo[DIRECTION] = DOWN_RIGHT
        return True
    elif logo[X_POSITION] == 0 and logo[Y_POSITION] == HEIGHT - 1:
        logo[DIRECTION] = UP_RIGHT
        return True
    elif logo[X_POSITION] == WIDTH - 3 and logo[Y_POSITION] == 0:
        logo[DIRECTION] = DOWN_LEFT
        return True
    elif logo[X_POSITION] == WIDTH - 3 and logo[Y_POSITION] == HEIGHT - 1:
        logo[DIRECTION] = UP_LEFT
        return True

    # Handle other edge cases and direction changes
    elif logo[X_POSITION] == 0 and logo[DIRECTION] == UP_LEFT:
        logo[DIRECTION] = UP_RIGHT
    elif logo[X_POSITION] == 0 and logo[DIRECTION] == DOWN_LEFT:
        logo[DIRECTION] = DOWN_RIGHT

    elif logo[X_POSITION] == WIDTH - 3 and logo[DIRECTION] == UP_RIGHT:
        logo[DIRECTION] = UP_LEFT
    elif logo[X_POSITION] == WIDTH - 3 and logo[DIRECTION] == DOWN_RIGHT:
        logo[DIRECTION] = DOWN_LEFT

    elif logo[Y_POSITION] == 0 and logo[DIRECTION] == UP_LEFT:
        logo[DIRECTION] = DOWN_LEFT
    elif logo[Y_POSITION] == 0 and logo[DIRECTION] == UP_RIGHT:
        logo[DIRECTION] = DOWN_RIGHT

    elif logo[Y_POSITION] == HEIGHT - 1 and logo[DIRECTION] == DOWN_LEFT:
        logo[DIRECTION] = UP_LEFT
    elif logo[Y_POSITION] == HEIGHT - 1 and logo[DIRECTION] == DOWN_RIGHT:
        logo[DIRECTION] = UP_RIGHT

    return False

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Bye!')
        sys.exit()
