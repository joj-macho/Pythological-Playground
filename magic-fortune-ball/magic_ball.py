# Import modules 
import random
import time


def main():
    '''This is the main function of the program.'''    

    # Slow spaced print
    slow_print('Magic Fortune Ball!')
    print('   ___')
    print(' .\'   \'.')
    print('/       \\')
    print('|   _   |')
    print('|  (_)  |')
    print('\\       /')
    print(' \'.___.\'')
    print()
    time.sleep(0.5)
    slow_print('Ask me a Yes or No Question.')
    input('> ')

    # Display a brief reply:
    replies = [
        'Hmm... Let me consult the mystical gnome...',
        'Your question has piqued the curiosity of a thousand curious cats...',
        'I sense a disturbance in the cosmic fabric...',
        'Hold on tight, I\'m decoding the secrets of the universe...',
        'Time to stir the cauldron of knowledge...',
        'Gathered from the stars, behold the answer to your query...',
        'The wise owl has spoken, and so shall I...',
        'Warning: The answer may be too cosmic for mortal comprehension...',
        'Venture into the unknown and discover your answer...',
        'Deep within the enchanted realm, the answer emerges...',
    ]

    slow_print(random.choice(replies))

    slow_print('.' * random.randint(3, 10), 0.3)

    # Answer
    slow_print('I have an answer...', 0.05)
    time.sleep(1)
    answers = [
        'Indeed, it is written in the scrolls of destiny.',
        'Nay, for the universe scoffs at your inquiry.',
        'In due time, the cosmic forces will reveal the truth.',
        'Absolutely and without a shadow of a doubt!',
        'Mmm... the answer swirls in a cosmic smoothie of uncertainty.',
        'Ask me again after a cup of celestial tea.',
        'The mystical squirrels whisper "yes" in the ancient oak tree.',
        'Hocus pocus! The answer is a resounding "no".',
        'With a flicker of stardust, the answer is revealed: maybe.',
        'The cosmic ballet unfolds, and the answer dances with "possibly".',
        'Lo and behold! The enchanted oracle speaks: "definitely".',
        'The alignment of the cosmos hints at a most probable "yes".',
        'No mortal can fathom the answer, for it lies in the realm of absurdity.',
        'The celestial hamsters have declared it to be a resounding "maybe".',
        'The cosmic jester says, "Ask again when the moon wears a tutu".',
        'The enchanted gummy bears whisper, "It is certain".',
        'The mystical snails slide forth with a definitive "no".',
        'The ancient tarot cards reveal a nebulous "ask again later".',
        'The cosmic sloths have spoken, and their answer is "undecided".',
        'By the power vested in me by the intergalactic jellyfish, the answer is "most likely".',
    ]

    slow_print(random.choice(answers), 0.05)

    # Ask if the user wants to play again
    play_again = input('\nDo you want to ask another question? (y/n)\n> ').lower()
    if play_again == 'y':
        main()
    else:
        print('Thank you for playing! Bye.')


def slow_print(text, interval=0.04):
    '''This function slowly displays text with spaces in between letters'''
    for char in text:
        print(char , end='', flush=True)
        time.sleep(interval)
    print()


if __name__ == '__main__':
    main()

