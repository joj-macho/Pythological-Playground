import os
import time
import random

# Animation constants
HEIGHT = 15  # Height of the animation window
WIDTH = 30  # Width of the animation window
FRAME_DELAY = 0.1

# Screen Items ANSI Characters
BALL = '\u23FA'  # ⏺ char
HORIZONTAL_BORDER = '\u2550'  # ═ char
VERTICAL_BORDER = '\u2551'  # ║ char
TOP_LEFT_CORNER = '\u2554'  # ╔ char
TOP_RIGHT_CORNER = '\u2557'  # ╗
BOTTOM_LEFT_CORNER = '\u255A'  # ╚ char
BOTTOM_RIGHT_CORNER = '\u255D'  # ╝ char


def main():
    '''Animate bouncing ball.'''
    try:
        # Intialize ball position and velocity
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])
        ball = {
            'x': x,
            'y': y,
            'dx': dx,
            'dy': dy,
            'bounces': 0,
            'corner_bounces': 0}

        while True:
            # Create screen with borders
            screen = [[' ' for _ in range(WIDTH + 2)]
                      for _ in range(HEIGHT + 2)]
            create_border(screen)

            draw_ball(screen, ball['x'], ball['y'])

            # clear and show screen
            os.system('clear' if os.name == 'posix' else 'cls')
            print('Bouncing Ball Animation')
            for row in screen:
                print(''.join(row))

            print(f'Ball Position: ({ball["x"]}, {ball["y"]})')
            print(f'Bounces: {ball["bounces"]}', end=' | ')
            print(f'Corner Bounces: {ball["corner_bounces"]}')

            update_position(ball)
            time.sleep(FRAME_DELAY)
    except KeyboardInterrupt:
        print('\nAnimation stopped. Exiting...')


def create_border(screen):
    '''Creates a border around the screen.'''
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


def draw_ball(screen, x, y):
    '''Draws ball at its current position on screen.'''
    screen[y + 1][x + 1] = BALL


def update_position(ball):
    '''Updates the ball's position based on its velocity.'''
    x, y, dx, dy = ball['x'], ball['y'], ball['dx'], ball['dy']

    # Update x, y postions
    x += dx
    y += dy

    # Check for boundary collisions
    if x <= 0 or x >= WIDTH - 1:
        dx *= -1
        ball['bounces'] += 1
    if y <= 0 or y >= HEIGHT - 1:
        dy *= -1
        ball['bounces'] += 1

    # CHeck for corner bounces
    if (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1):
        ball['corner_bounces'] += 1

    ball['x'], ball['y'], ball['dx'], ball['dy'] = x, y, dx, dy


if __name__ == '__main__':
    main()
