import random

# Constants
OBJECT_PRONOUNS = ['her', 'him', 'them', 'it', 'us', 'me']
POSSESSIVE_PRONOUNS = ['her', 'his', 'their', 'my', 'our', 'its']
PERSONAL_PRONOUNS = ['she', 'he', 'they', 'we', 'you', 'I']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan', 'Arizona', 'Colorado', 'Washington', 'Oregon', 'New Jersey']
NOUNS = ['athlete', 'clown', 'shovel', 'paleo diet', 'doctor', 'parent', 'cat', 'dog', 'chicken', 'robot', 'video game', 'avocado', 'plastic straw', 'serial killer', 'telephone psychic', 'alien', 'dragon', 'pirate', 'unicorn', 'vampire', 'zombie']
ADJECTIVES = ['happy', 'sad', 'angry', 'funny', 'romantic', 'exciting', 'scary', 'mysterious', 'amazing', 'delicious']
VERBS = ['lose', 'gain', 'find', 'discover', 'improve', 'master', 'uncover', 'conquer', 'overcome', 'strengthen', 'enhance', 'maximize', 'minimize', 'optimize', 'boost', 'uplift', 'upskill', 'uplift', 'upgrade', 'transform']
PLACES = ['house', 'attic', 'bank deposit box', 'school', 'basement', 'workplace', 'donut shop', 'apocalypse bunker', 'beach', 'jungle', 'mountain', 'cave', 'castle']
WHEN = ['soon', 'this year', 'later today', 'right now', 'next week', 'tomorrow', 'next month', 'in a few minutes', 'eventually', 'someday']

# Click bait types
CLICKBAIT_TYPES = {
    1: 'Are {} Killing the {} Industry?',
    2: 'Without This {}, {} Could Kill You {}',
    3: 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}',
    4: "You Won't Believe What This {} {} Found in {} {}",
    5: "What {} Don't Want You To Know About {}",
    6: '{} Gift Ideas to Give Your {} From {}',
    7: '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)',
    8: "This {} {} Didn't Think Robots Would Take {} Job. {} {} Wrong.",
    9: 'The Surprising Link Between {} and {}',
    10: 'The Shocking Truth About {} Revealed',
    11: '{} Hacks You Need to Know to {} Like a Pro',
    12: '{} {} That Will Change Your Life Forever',
    13: "The Untold Secret to {} That {} Don't Want You to Know",
    14: 'This Simple {} Trick Can {} in Just {} Days',
    15: 'The Ultimate Guide to {} for {}',
    16: '{} vs {}. Which is Better?',
    17: "What {} Doesn't Want You to Know About {}",
    18: 'Why {} Are Freaking Out About {}',
    19: "You Won't Believe How Much Money {} Makes Doing {}",
    20: "The Top {} {} That You Can't Afford to Miss",
    21: 'The Shocking Reason Why {} Are {} Than {}',
    22: 'These {} {} Will Make You Question Everything You Thought You Knew About {}',
    23: 'The {} Secret to Getting More {}',
    24: 'The {} Way to {} in {}',
    25: '{} {} to {} in Just {} Minutes a Day'
}

def main():
    print('''
Clickbait Headline Generator!

This program will trick people into looking at ads.
    ''')
    # Enter number of articles to produce
    while True:
        response = input(
            'Enter a number of clickbaits headlines to generate:\n> ')
        if not response.isdecimal():
            print('Please Enter a Valid Number of clickbaits.')
        else:
            numHeadlines = int(response)
            break

    for i in range(numHeadlines):
        clickbaitType = random.randint(1, len(CLICKBAIT_TYPES))
        pronoun1 = random.choice(PERSONAL_PRONOUNS)
        pronoun2 = random.choice(OBJECT_PRONOUNS)
        possessivePronoun = random.choice(POSSESSIVE_PRONOUNS)
        state = random.choice(STATES)
        noun1 = random.choice(NOUNS)
        noun2 = random.choice(NOUNS)
        adj1 = random.choice(ADJECTIVES)
        adj2 = random.choice(ADJECTIVES)
        place = random.choice(PLACES)
        when = random.choice(WHEN)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 100)
        verb = random.choice(VERBS)


        if clickbaitType == 1:
            headline = CLICKBAIT_TYPES[1].format(noun1, noun2)
        elif clickbaitType == 2:
            headline = CLICKBAIT_TYPES[2].format(noun1, noun2, noun2, when)
        elif clickbaitType == 3:
            headline = CLICKBAIT_TYPES[3].format(noun1, pronoun1, noun2, noun2)
        elif clickbaitType == 4:
            headline = CLICKBAIT_TYPES[4].format(noun1, pronoun1, possessivePronoun, place)
        elif clickbaitType == 5:
            headline = CLICKBAIT_TYPES[5].format(noun1, noun2)
        elif clickbaitType == 6:
            headline = CLICKBAIT_TYPES[6].format(num1, noun1, state)
        elif clickbaitType == 7:
            headline = CLICKBAIT_TYPES[7].format(num1, noun1, num2)
        elif clickbaitType == 8:
            headline = CLICKBAIT_TYPES[8].format(noun1, pronoun1, pronoun2, pronoun1, pronoun2)
        elif clickbaitType == 9:
            headline = CLICKBAIT_TYPES[9].format(noun1, noun2)
        elif clickbaitType == 10:
            headline = CLICKBAIT_TYPES[10].format(noun1)
        elif clickbaitType == 11:
            headline = CLICKBAIT_TYPES[11].format(noun1, verb)
        elif clickbaitType == 12:
            headline = CLICKBAIT_TYPES[12].format(noun1, noun2)
        elif clickbaitType == 13:
            headline = CLICKBAIT_TYPES[13].format(noun1, pronoun2)
        elif clickbaitType == 14:
            headline = CLICKBAIT_TYPES[14].format(noun1, verb, num1)
        elif clickbaitType == 15:
            headline = CLICKBAIT_TYPES[15].format(noun1, noun2)
        elif clickbaitType == 16:
            headline = CLICKBAIT_TYPES[16].format(noun1, noun2)
        elif clickbaitType == 17:
            headline = CLICKBAIT_TYPES[17].format(noun1, noun2)
        elif clickbaitType == 18:
            headline = CLICKBAIT_TYPES[18].format(noun1, noun2)
        elif clickbaitType == 19:
            headline = CLICKBAIT_TYPES[19].format(noun1, verb)
        elif clickbaitType == 20:
            headline = CLICKBAIT_TYPES[20].format(num1, noun1)
        elif clickbaitType == 21:
            headline = CLICKBAIT_TYPES[21].format(noun1, verb, adj1, adj2)
        elif clickbaitType == 22:
            headline = CLICKBAIT_TYPES[22].format(num1, noun1, noun2)
        elif clickbaitType == 23:
            headline = CLICKBAIT_TYPES[23].format(adj1, noun1)
        elif clickbaitType == 24:
            headline = CLICKBAIT_TYPES[24].format(adj1, verb, num1)
        elif clickbaitType == 25:
            headline = CLICKBAIT_TYPES[25].format(adj1, noun1, verb, num1)
        
        print()
        print(headline.title())



if __name__ == '__main__':
    main()