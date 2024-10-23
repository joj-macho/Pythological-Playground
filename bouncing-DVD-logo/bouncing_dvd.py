import os
import time
import random

# Constants
HEIGHT = 20
WIDTH = 40
NUM_OF_LOGOS = 5
FRAME_DELAY = 0.2

# ANSI Color Codes
COLOR_RESET = '\033[0m'

LOGO_COLORS = [
    '\033[90m',  # Gray
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[97m'   # White
    ]

# Screen Items ANSI Characters
LOGO = 'DVD'
LOGO_LEN = len(LOGO)
HORIZONTAL_BORDER = '\u2550'  # ═ char
VERTICAL_BORDER = '\u2551'  # ║ char
TOP_LEFT_CORNER = '\u2554'  # ╔ char
TOP_RIGHT_CORNER = '\u2557'  # ╗
BOTTOM_LEFT_CORNER = '\u255A'  # ╚ char
BOTTOM_RIGHT_CORNER = '\u255D'  # ╝ char


def main():
    '''Animate bouncing logos.'''
    try:
        # Initialize logos with random positions, velocities, and colors
        logos = []
        for i in range(NUM_OF_LOGOS):
            x = random.randint(1, WIDTH - LOGO_LEN - 1)
            y = random.randint(1, HEIGHT - 2)
            dx = random.choice([-1, 1])
            dy = random.choice([-1, 1])
            color = LOGO_COLORS[i % len(LOGO_COLORS)]
            logos.append({'x': x, 'y': y, 'dx': dx, 'dy': dy, 'color': color,
                          'bounces': 0, 'corner_bounces': 0})

        while True:
            # Create screen with borders
            screen = [[' ' for _ in range(WIDTH + 2)]
                      for _ in range(HEIGHT + 2)]
            create_border(screen)

            # Draw logos on screen
            positions = {}
            for logo in logos:
                # Prevent overwriting of logos by checking their positions
                if (logo['x'], logo['y']) not in positions:
                    draw_logo(screen, logo['x'], logo['y'], logo['color'])
                    positions[(logo['x'], logo['y'])] = True

            os.system('clear' if os.name == 'posix' else 'cls')
            print('Bouncing DVD LOGO Animation')
            for row in screen:
                print(''.join(row))

            for i, logo in enumerate(logos):
                print(f'Logo {i+1} Position: ({logo["x"]}, {logo["y"]})')
                print(f'Bounces: {logo["bounces"]}', end=' | ')
                print(f'Corner Bounces: {logo["corner_bounces"]}')
                print('-' * (WIDTH + 2))

            for logo in logos:
                update_position(logo)

            time.sleep(FRAME_DELAY)
    except KeyboardInterrupt:
        print('\nAnimation stopped. Exiting...')


def create_border(screen):
    '''Create a border around the screen.'''
    for row in range(HEIGHT + 2):
        for col in range(WIDTH + 2):
            # Draw corners first
            if row == 0 and col == 0:
                screen[row][col] = TOP_LEFT_CORNER
            elif row == 0 and col == WIDTH + 1:
                screen[row][col] = TOP_RIGHT_CORNER
            elif row == HEIGHT + 1 and col == 0:
                screen[row][col] = BOTTOM_LEFT_CORNER
            elif row == HEIGHT + 1 and col == WIDTH + 1:
                screen[row][col] = BOTTOM_RIGHT_CORNER
            # Draw edges
            elif row == 0 or row == HEIGHT + 1:
                screen[row][col] = HORIZONTAL_BORDER
            elif col == 0 or col == WIDTH + 1:
                screen[row][col] = VERTICAL_BORDER


def draw_logo(screen, x, y, color):
    '''Draw logo at its current position on screen.'''
    for i, char in enumerate(LOGO):
        screen[y + 1][x + 1 + i] = f'{color}{char}{COLOR_RESET}'


def update_position(logo):
    '''Update the logo's position based on its velocity.'''
    x, y, dx, dy = logo['x'], logo['y'], logo['dx'], logo['dy']

    # Update position
    x += dx
    y += dy

    # Check for boundary collisions and update color if collision occurs
    if x <= 0 or x + LOGO_LEN >= WIDTH:
        dx *= -1
        logo['bounces'] += 1
        logo['color'] = random.choice(LOGO_COLORS)
    if y <= 0 or y >= HEIGHT - 1:
        dy *= -1
        logo['bounces'] += 1
        logo['color'] = random.choice(LOGO_COLORS)

    # Check for corner bounces
    if (x == 0 or x + LOGO_LEN == WIDTH) and (y == 0 or y == HEIGHT - 1):
        logo['corner_bounces'] += 1

    logo['x'], logo['y'], logo['dx'], logo['dy'] = x, y, dx, dy


if __name__ == '__main__':
    main()
