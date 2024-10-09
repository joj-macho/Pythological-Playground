import random

# Bait list
headline_starters = [
    'You Won\'t Believe',
    'This Is Why',
    'The Secret To',
    'How',
    'Why',
    'Why Everyone is Talking About',
    '10 Reasons Why',
    'How to Instantly Improve',
    'The Shocking Truth About',
    'The Ultimate Guide To',
    'This Simple Trick For',
    'What Happens When',
    'The Surprising Benefits Of'
]

headline_subjects = [
    'Losing Weight',
    'Making Money',
    'Getting Fit',
    'Being Happy',
    'Saving Money',
    'Finding Love',
    'Your Health',
    'This Simple Trick',
    'Improving Your Health',
    'Boosting Your Career',
    'The Latest Technology',
    'Becoming Smarter',
    'This Common Mistake',
    'Reducing Stress'
]

headline_endings = [
    'Will Change Your Life',
    'Doctors Don\'t Want You To Know',
    'Celebrities Use',
    'You Need To Try',
    'Will Amaze You',
    'You Shouldn\'t Miss This',
    'Is More Important Than You Think',
    'Is The Best Decision You\'ll Make',
    'Is The Key To Success',
    'And How It Affects You',
    'Is A Game Changer',
    'Experts Are Raving About'
]


def main():
    '''Generate and display clickbait headlines.'''
    print('Clickbait Headline Generator\n')

    while True:
        response = input('Enter number of headlines or (q)uit to exit:\n> ')
        if response.strip().lower() in ('q', 'quit'):
            print('Bye!')
            break

        try:
            num_headlines = int(response)
            if num_headlines < 1:
                raise ValueError('Number of headlines must be a > 0.')

            print(f'\nGenerating {num_headlines} clickbait headlines:\n')
            for _ in range(num_headlines):
                print(generate_headline())

        except ValueError as e:
            print(f'Invalid input: {e}\n')


def generate_headline():
    '''Generates a random clickbait headline.'''
    starter = random.choice(headline_starters)
    subject = random.choice(headline_subjects)
    ending = random.choice(headline_endings)
    return f'{starter} {subject} {ending}'


if __name__ == '__main__':
    main()
