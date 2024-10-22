import random
import time


def main():
    '''Get your fortune .'''
    slow_print('Magic Fortune Ball!')
    print()
    time.sleep(0.5)
    while True:
        slow_print('Ask me a Yes or No Question...')
        response = input('Enter (q)uit to exit.\n> ').strip()
        if response.lower() in ('q', 'quit'):
            print('Exiting program...Bye!')
            break

        # Let me think on it replies
        replies = [
            'Hold on... I\'m tuning into the astral frequencies...',
            'The ancient spirits are whispering... give me a moment.',
            'Gathered from the stars, behold the answer to your query...',
            'The wise owl has spoken, and so shall I...',
            'The moonlight reveals a hazy vision... let me interpret.',
            'One moment... I\'m channeling the wisdom of the ages.',
            'The oracle\'s eye opens... your answer is coming.',
            'I\'m consulting the mystic tarot... patience, seeker.'
        ]

        print()
        slow_print(random.choice(replies))
        print()
        slow_print('.' * random.randint(3, 10), 0.3)
        print()

        # Final outcome
        slow_print('I have an answer...', 0.05)
        time.sleep(1)
        answers = [
            'Indeed, it is written in the scrolls of destiny.',
            'Nay, for the universe scoffs at your inquiry.',
            'The stars whisper... but they\'re not quite sure.',
            'Absolutely and without a shadow of a doubt!',
            'I see a glimmer... but it\'s faint. It might not happen.',
            'The cosmic balance wavers... could go either way.',
            'Hocus pocus! The answer is a resounding "no".',
            'The spirits are divided on this... it\'s a tricky one.',
            'I sense a possibility... but don\'t count on it just yet.',
            'The runes are uncertain... proceed with caution.',
            'The oracle\'s vision is hazy... things could change.',
            'The spirits are whispering... "not impossible, but not easy."',
            'The stars align, but they\'re not all in agreement.',
            'I consulted the celestial beings... and they shrugged.',
            'The enchanted crystal shines bright... your wish shall come '
            'true!',
            'The spririts nod in approval... it\'s a definite "yes!"',
        ]

        slow_print(random.choice(answers), 0.05)
        print()


def slow_print(text, interval=0.04):
    '''Slowly display text with spaces in between letters'''
    for char in text:
        print(char, end='', flush=True)
        time.sleep(interval)
    print()


if __name__ == '__main__':
    main()
