import random
import sys


GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'
WORDS = ['WORD1', 'WORD2', 'WORD3', 'WORD4', 'WORD5', 'WORD6', 'WORD7', 'WORD8', 'WORD9', 'WORD10', 'WORD11', 'WORD12']


def main():
    '''Run the hacking game.'''

    print('\nHacking Game.\n')
    print('Find the password in the computer\'s memory. You are given clues after each guess. You get four guesses.\n')
    input('Press Enter to begin...')

    game_words = get_words()
    computer_memory = get_computer_memory_string(game_words)
    secret_password = random.choice(game_words)

    print(computer_memory)
    for tries_remaining in range(4, 0, -1):
        player_move = ask_for_player_guess(game_words, tries_remaining)
        if player_move == secret_password:
            print('AC C E S S   G R A N T E D')
            return
        else:
            num_matches = num_matching_letters(secret_password, player_move)
            print('Access Denied ({}/7 correct)'.format(num_matches))
    print('Out of tries. Secret password was {}.'.format(secret_password))


def get_words():
    '''This function returns a list of 12 words that could possibly be the password.'''

    secret_password = random.choice(WORDS)
    words = [secret_password]

    while len(words) < 3:
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)

    for _ in range(500):
        if len(words) == 5:
            break

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 3:
            words.append(random_word)

    for _ in range(500):
        if len(words) == 12:
            break

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) != 0:
            words.append(random_word)

    while len(words) < 12:
        random_word = get_one_word_except(words)
        words.append(random_word)

    assert len(words) == 12
    return words


def get_one_word_except(blocklist=None):
    '''This function returns a random word from WORDS that isn't in blocklist.'''

    if blocklist is None:
        blocklist = []

    while True:
        random_word = random.choice(WORDS)
        if random_word not in blocklist:
            return random_word


def num_matching_letters(word1, word2):
    '''This function returns the number of matching letters in the two words.'''

    matches = 0
    for i in range(len(word1)-1):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def get_computer_memory_string(words):
    '''This function returns a string representing the computer memory.'''

    lines_with_words = random.sample(range(16 * 2), len(words))
    memory_address = 16 * random.randint(0, 4000)
    computer_memory = []
    next_word = 0

    for line_num in range(16):
        left_half = ''
        right_half = ''

        for _ in range(16):
            left_half += random.choice(GARBAGE_CHARS)
            right_half += random.choice(GARBAGE_CHARS)

        if line_num in lines_with_words:
            insertion_index = random.randint(0, 9)
            left_half = left_half[:insertion_index] + words[next_word] + left_half[insertion_index + 7:]
            next_word += 1

        if line_num + 16 in lines_with_words:
            insertion_index = random.randint(0, 9)
            right_half = right_half[:insertion_index] + words[next_word] + right_half[insertion_index + 7:]
            next_word += 1

        computer_memory.append('0x{:04x}  {}    0x{:04x}  {}'.format(
            memory_address, left_half, memory_address + (16 * 16), right_half))

        memory_address += 16

    return '\n'.join(computer_memory)


def ask_for_player_guess(words, tries):
    '''This function lets the player enter a password guess.'''
    while True:
        print('Enter password: ({} tries remaining)'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('That is not one of the possible passwords listed above.')
        print('Try entering "{}" or "{}".'.format(words[0], words[1]))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
