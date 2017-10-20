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
        if num_allowed_vowels(line) >= 3 and at_least_two_consecutive_chars(
                line) and not contains_naughty_strings(line):
            total += 1

    print(total)


def has_non_overlapping_pairs(word):
    for i1 in range(len(word)-1):
        for i2 in range(len(word) - 1):
            if word[i1:i1+2] == word[i2:i2+2] and abs(i1-i2)>1:
                return True
    return False


def repeat_after_one_letter(word):
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            return True
    return False


with open('input5.txt', 'r') as f:
    total = 0
    for line in f:
        if has_non_overlapping_pairs(line) and repeat_after_one_letter(line):
            total += 1

    print(total)
