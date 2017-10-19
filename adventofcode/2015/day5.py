def num_allowed_vowels(word):
    allowed_vowels = ['a', 'o', 'u', 'e', 'i']
    total_vowels = 0
    for c in word:
        if c in allowed_vowels:
            total_vowels += 1
    return total_vowels


def at_least_two_consecutive_chars(word):
    last = ''
    for c in word:
        if c == last:
            return True
        last = c
    return False


def contains_naughty_strings(word):
    naughty_strings = ['ab', 'cd', 'pq', 'xy']
    for ns in naughty_strings:
        if ns in word:
            return True
    return False


with open('input5.txt', 'r') as f:
    total = 0
    for line in f:
        if num_allowed_vowels(line) >= 3 and at_least_two_consecutive_chars(line) and not contains_naughty_strings(line):
            total += 1

    print(total)
