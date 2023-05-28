import random

class HungryRobotsGame:
    WIDTH = 40
    HEIGHT = 20
    NUM_ROBOTS = 10
    NUM_TELEPORTS = 2
    NUM_DEAD_ROBOTS = 2
    NUM_WALLS = 100
    EMPTY_SPACE = ' '
    PLAYER = '@'
    ROBOT = 'R'
    DEAD_ROBOT = 'X'
    WALL = '░'

    def __init__(self):
        self.board = self.get_new_board()
        self.robots = self.add_robots()
        self.player_position = self.get_random_empty_space(self.robots)
        self.teleports = self.NUM_TELEPORTS

    def start(self):
        print('''
Hungry Robots Game

You are trapped in a maze with hungry robots! You don't know why robots need to eat, but you don't want to find out. The robots are badly programmed and will move directly toward you, even if blocked by walls. You must trick the robots into crashing into each other (or dead robots) without being caught. You have a personal teleporter device, but it only has enough battery for {} trips. Keep in mind, you and robots can slip through the corners of two diagonal walls!
'''.format(self.NUM_TELEPORTS))

        input('Press Enter to begin...')

        while True:
            self.display_board()

            if len(self.robots) == 0:
                print('All the robots have crashed into each other and you')
                print('lived to tell the tale! Good job!')
                break

            self.player_position = self.ask_for_player_move()
            self.move_robots()

            if self.player_position in self.robots:
                self.display_board()
                print('You have been caught by a robot!')
                break

    def get_new_board(self):
        '''Returns a dictionary that represents the board. The keys are (x, y) tuples of integer indexes for board positions, the values are WALL, EMPTY_SPACE, or DEAD_ROBOT.'''

        board = {}

        # Create an empty board:
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                board[(x, y)] = self.EMPTY_SPACE

        # Add walls on the edges of the board:
        for x in range(self.WIDTH):
            board[(x, 0)] = self.WALL  # Make top wall.
            board[(x, self.HEIGHT - 1)] = self.WALL  # Make bottom wall.
        for y in range(self.HEIGHT):
            board[(0, y)] = self.WALL  # Make left wall.
            board[(self.WIDTH - 1, y)] = self.WALL  # Make right wall.

        # Add the random walls:
        for _ in range(self.NUM_WALLS):
            x, y = self.get_random_empty_space(board)
            board[(x, y)] = self.WALL

        # Add the starting dead robots:
        for _ in range(self.NUM_DEAD_ROBOTS):
            x, y = self.get_random_empty_space(board)
            board[(x, y)] = self.DEAD_ROBOT

        return board

    def get_random_empty_space(self, exclude_positions=[]):
        '''Return a (x, y) integer tuple of an empty space on the board.'''

        while True:
            random_x = random.randint(1, self.WIDTH - 2)
            random_y = random.randint(1, self.HEIGHT - 2)
            if self.is_empty(random_x, random_y) and (random_x, random_y) not in exclude_positions:
                break
        return (random_x, random_y)

    def is_empty(self, x, y):
        '''Return True if the (x, y) is empty on the board and there's also no robot there.'''

        return self.board[(x, y)] == self.EMPTY_SPACE

    def add_robots(self):
        '''Add NUM_ROBOTS number of robots to empty spaces on the board and return a list of these (x, y) spaces where robots are now located.'''

        robots = set()
        for _ in range(self.NUM_ROBOTS):
            x, y = self.get_random_empty_space(robots)
            robots.add((x, y))
        return robots

    def display_board(self):
        '''Display the board, robots, and player on the screen.'''

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                if self.board[(x, y)] == self.WALL:
                    print(self.WALL, end='')
                elif self.board[(x, y)] == self.DEAD_ROBOT:
                    print(self.DEAD_ROBOT, end='')
                elif (x, y) == self.player_position:
                    print(self.PLAYER, end='')
                elif (x, y) in self.robots:
                    print(self.ROBOT, end='')
                else:
                    print(self.EMPTY_SPACE, end='')
            print()

    def ask_for_player_move(self):
        '''Returns the (x, y) integer tuple of the place the player moves next, given their current location and the walls of the board.'''

        player_x, player_y = self.player_position
        q = 'Q' if self.is_empty(player_x - 1, player_y - 1) else ' '
        w = 'W' if self.is_empty(player_x + 0, player_y - 1) else ' '
        e = 'E' if self.is_empty(player_x + 1, player_y - 1) else ' '
        d = 'D' if self.is_empty(player_x + 1, player_y + 0) else ' '
        c = 'C' if self.is_empty(player_x + 1, player_y + 1) else ' '
        x = 'X' if self.is_empty(player_x + 0, player_y + 1) else ' '
        z = 'Z' if self.is_empty(player_x - 1, player_y + 1) else ' '
        a = 'A' if self.is_empty(player_x - 1, player_y + 0) else ' '
        all_moves = (q + w + e + d + c + x + a + z + 'S')

        while True:
            print('(T)eleports remaining: {}'.format(self.teleports))
            print('                    ({}) ({}) ({})'.format(q, w, e))
            print('                    ({}) (S) ({})'.format(a, d))
            print('Enter move or QUIT: ({}) ({}) ({})'.format(z, x, c))

            move = input('> ').upper()
            if move == 'QUIT':
                print('Thanks for playing!')
                sys.exit()
            elif move == 'T' and self.teleports > 0:
                self.teleports -= 1
                return self.get_random_empty_space(self.robots)
            elif move != '' and move in all_moves:
                return {
                    'Q': (player_x - 1, player_y - 1),
                    'W': (player_x + 0, player_y - 1),
                    'E': (player_x + 1, player_y - 1),
                    'D': (player_x + 1, player_y + 0),
                    'C': (player_x + 1, player_y + 1),
                    'X': (player_x + 0, player_y + 1),
                    'Z': (player_x - 1, player_y + 1),
                    'A': (player_x - 1, player_y + 0),
                    'S': (player_x, player_y),
                }[move]

    def move_robots(self):
        '''Return a list of (x, y) tuples of new robot positions after they have tried to move toward the player.'''
        player_x, player_y = self.player_position
        next_robot_positions = []

        while len(self.robots) > 0:
            robot_x, robot_y = self.robots.pop()

            if robot_x < player_x:
                move_x = 1
            elif robot_x > player_x:
                move_x = -1
            elif robot_x == player_x:
                move_x = 0

            if robot_y < player_y:
                move_y = 1
            elif robot_y > player_y:
                move_y = -1
            elif robot_y == player_y:
                move_y = 0

            if self.board[(robot_x + move_x, robot_y + move_y)] == self.WALL:
                if self.board[(robot_x + move_x, robot_y)] == self.EMPTY_SPACE:
                    move_y = 0
                elif self.board[(robot_x, robot_y + move_y)] == self.EMPTY_SPACE:
                    move_x = 0
                else:
                    move_x = 0
                    move_y = 0

            new_robot_x = robot_x + move_x
            new_robot_y = robot_y + move_y

            if (self.board[(robot_x, robot_y)] == self.DEAD_ROBOT
                    or self.board[(new_robot_x, new_robot_y)] == self.DEAD_ROBOT):
                continue

            if (new_robot_x, new_robot_y) in next_robot_positions:
                self.board[(new_robot_x, new_robot_y)] = self.DEAD_ROBOT
                next_robot_positions.remove((new_robot_x, new_robot_y))
            else:
                next_robot_positions.append((new_robot_x, new_robot_y))

        self.robots = next_robot_positions

    def play_game(self):
        '''Starts and runs the game loop.'''
        
        print('''
Hungry Robots Game

You are trapped in a maze with hungry robots! You don't know why robots need to eat, but you don't want to find out. The robots are badly programmed and will move directly toward you, even if blocked by walls. You must trick the robots into crashing into each other (or dead robots) without being caught. You have a personal teleporter device, but it only has enough battery for {} trips. Keep in mind, you and robots can slip through the corners of two diagonal walls!
'''.format(self.NUM_TELEPORTS))

        input('Press Enter to begin...')

        self.board = self.get_new_board()
        self.robots = self.add_robots()
        self.player_position = self.get_random_empty_space(self.robots)

        while True:
            self.display_board()

            if len(self.robots) == 0:
                print('All the robots have crashed into each other and you')
                print('lived to tell the tale! Good job!')
                sys.exit()

            self.player_position = self.ask_for_player_move()
            self.move_robots()

            if self.player_position in self.robots:
                self.display_board()
                print('You have been caught by a robot!')
                sys.exit()

game = HungryRobotsGame()
game.play_game()
