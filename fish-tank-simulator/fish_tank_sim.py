import random
import sys
import time
import bext


# Set up the constants:
WIDTH, HEIGHT = bext.size()
WIDTH -= 1
NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLERS = 1
FRAMES_PER_SECOND = 4 


# Every string in a fish dictionary should be the same length.
FISH_TYPES = [
    {"right": ["><>"], "left": ["<><"]},
    {"right": [">||>"], "left": ["<||<"]},
    {"right": [">))>"], "left": ["<[[<"]},
    {"right": ["><><><"], "left": ["<><><><"]},
    {"right": ["<><))>"], "left": ["><((><"]},
    {"right": ["<><><><"], "left": ["><><><><"]},
    {"right": ["<()()<"], "left": [">)<)()>"]},
    {"right": ["><\\><"], "left": ["<//><>"]},
    {"right": ["<><()()"], "left": ["())()><"]},
    {"right": ["<><<><"], "left": ["><><>><"]},
    {"right": ["<><X><<"], "left": [">><X><><"]},
    {"right": [">||o", ">||."], "left": ["o||<", ".||<"]},
    {"right": [">))o", ">))."], "left": ["o[[<", ".[[<"]},
    {"right": [">-==>"], "left": ["<==-<"]},
    {"right": [r">\\>"], "left": ["<//<"]},
    {"right": ["><)))*>"], "left": ["<*(((><"]},
    {"right": ["}-[[[*>"], "left": ["<*]]]-{"]},
    {"right": ["]-<)))b>"], "left": ["<d(((>-["]},
    {"right": ["><XXX*>"], "left": ["<*XXX><"]},
    {
        "right": ["_.-._.-^=>", "._.-._.^=>", "-._.-._^=>", "._.-._.^=>"],
        "left": ["<=^-._.-._", "<=^.-._.-.", "<=^_.-._.-", "<=^._.-._."],
    },
]

LONGEST_FISH_LENGTH = 10

# The x and y positions where a fish runs into the edge of the screen:
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    '''This is the main function. '''

    bext.bg("black")
    bext.clear()

    FISHES = generate_fish()
    BUBBLERS = generate_bubblers()
    BUBBLES = []
    KELPS = generate_kelps()

    STEP = 1
    try:
        while True:
            simulate_aquarium(FISHES, BUBBLERS, BUBBLES, KELPS, STEP)
            draw_aquarium(FISHES, BUBBLES, KELPS)
            time.sleep(1 / FRAMES_PER_SECOND)
            clear_aquarium(FISHES, BUBBLES, KELPS)
            STEP += 1
    except KeyboardInterrupt:
        sys.exit()


def generate_fish():
    '''This function generates a list of fish dictionaries.'''

    fishes = []
    for _ in range(NUM_FISH):
        fish_type = random.choice(FISH_TYPES)
        if random.randint(0, 1) == 0:
            direction = "left"
        else:
            direction = "right"
        fish = {
            "type": fish_type,
            "x": random.randint(LEFT_EDGE, RIGHT_EDGE),
            "y": random.randint(TOP_EDGE, BOTTOM_EDGE),
            "direction": direction,
        }
        fishes.append(fish)
    return fishes


def generate_bubblers():
    '''This function generates a list of bubbler coordinates.'''

    bubblers = []
    for _ in range(NUM_BUBBLERS):
        x = random.randint(LEFT_EDGE, RIGHT_EDGE)
        y = random.randint(TOP_EDGE, BOTTOM_EDGE)
        bubblers.append((x, y))
    return bubblers


def generate_kelps():
    '''This function generates a list of kelp coordinates.'''

    kelps = []
    for _ in range(NUM_KELP):
        x = random.randint(LEFT_EDGE, RIGHT_EDGE)
        y = random.randint(TOP_EDGE, BOTTOM_EDGE)
        kelps.append((x, y))
    return kelps


def simulate_aquarium(fishes, bubblers, bubbles, kelps, step):
    '''This function moves the fish and add bubbles.'''

    for fish in fishes:
        # Check if the fish should change direction:
        if random.randint(0, 99) < 10:
            fish["direction"] = "right" if fish["direction"] == "left" else "left"

        # Move the fish:
        if fish["direction"] == "left":
            fish["x"] -= 1
            if fish["x"] < LEFT_EDGE:
                fish["x"] = RIGHT_EDGE
        elif fish["direction"] == "right":
            fish["x"] += 1
            if fish["x"] > RIGHT_EDGE:
                fish["x"] = LEFT_EDGE

    # Add bubbles:
    if step % 2 == 0:  # Every other step.
        for bubbler in bubblers:
            if random.randint(0, 99) < 33:
                bubbles.append({"x": bubbler[0], "y": bubbler[1] - 1})


def draw_aquarium(fishes, bubbles, kelps):
    '''This function draws the fish and bubbles.'''

    for fish in fishes:
        if fish["direction"] == "right":
            fish_string = fish["type"]["right"]
        elif fish["direction"] == "left":
            fish_string = fish["type"]["left"]
        for i, line in enumerate(fish_string):
            bext.goto(fish["x"], fish["y"] + i)
            print(line, end="")

    for bubble in bubbles[:]:
        bext.goto(bubble["x"], bubble["y"])
        print("o")
        bubble["y"] -= 1
        if bubble["y"] <= TOP_EDGE:
            bubbles.remove(bubble)

    for kelp in kelps:
        bext.goto(kelp[0], kelp[1])
        print("|")


def clear_aquarium(fishes, bubbles, kelps):
    '''This function clears the fish and bubbles.'''

    for fish in fishes:
        if fish["direction"] == "right":
            fish_string = fish["type"]["right"]
        elif fish["direction"] == "left":
            fish_string = fish["type"]["left"]
        for _ in range(len(fish_string)):
            bext.goto(fish["x"], fish["y"])
            print(" " * LONGEST_FISH_LENGTH)

    for bubble in bubbles:
        bext.goto(bubble["x"], bubble["y"])
        print(" ")

    for kelp in kelps:
        bext.goto(kelp[0], kelp[1])
        print(" ")


if __name__ == "__main__":
    main()
