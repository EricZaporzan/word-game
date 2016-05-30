import itertools
import sys


with open("words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)


def run(num_spaces, letters):
    words = list()
    perms = list(itertools.permutations(letters, num_spaces))
    for p in perms:
        if is_english_word(''.join(p)) and ''.join(p) not in words:
            words.append(''.join(p))

    return words


def is_english_word(word):
    return word.lower() in english_words

if __name__ == '__main__':
    argv = sys.argv

    if argv[1].lower() == 'help':
        print("Cheat at that '4 pics 1 word' game on your phone!")
        print("Usage: 'python words.py <number of spaces (int)> <provided letters (str)>'")
    else:
        print("Possible answers:")
        print(', \n'.join(run(int(argv[1]), str(argv[2]))))
