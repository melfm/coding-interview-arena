"""String manipulation questions."""

import pdb


def reverse_string_py(string):

    return string[::-1]


def reverse_string(string):

    p1 = 0
    p2 = len(string) - 1

    string_chars = list(string)

    while p1 != p2:

        tmp = string_chars[p1]
        string_chars[p1] = string_chars[p2]
        string_chars[p2] = tmp

        p1 += 1
        p2 -= 1

    return ''.join(string_chars)


def is_palindrome(word):
    """ Write an algorithm that returns true/false if a
    word is a palindrome (i.e. reads the same forwards and
    backwards) e.g. car, dad, mum.
    """

    p0 = 0
    p1 = len(word) - 1

    is_palin = True

    while(p0 < p1):

        if word[p0].lower() != word[p1].lower():
            is_palin = False
            return is_palin

        p0 += 1
        p1 -= 1

    return is_palin


def return_palindrome_subset(word):
    """Return the largest possible palindrome subset.
    """
    p0 = 0
    p1 = len(word) - 1

    sub_word = []
    beg_w = []
    end_w = []

    while(p0 < p1):

        if word[p0].lower() != word[p1].lower():

            print('Palindrome subset')
            sub_word = beg_w + end_w
            sub_word = ''.join(sub_word)
            return sub_word

        beg_w.append(word[p0])
        end_w.insert(0, word[p1])

        p0 += 1
        p1 -= 1

    return word


def string_anagram_loop(string_a, string_b):
    """Write a method to decide if two strings
    are anagrams or not."""

    string_a_list = list(string_a)
    string_b_list = list(string_b)

    if len(string_a) != len(string_b):
        return False

    match_found = False

    for i in string_a_list:
        current_char_a = i
        match_found = False
        for j in string_b_list:
            current_char_b = j

            if current_char_a == current_char_b:
                match_found = True

            else:
                continue

        if not match_found:
            break

    return match_found


def string_anagram_count(string_a, string_b):
    """Decides if two strings are anagrams or not
    by keeping a char counter to compare with."""

    num_of_chars = 256
    count_a = [0] * num_of_chars
    count_b = [0] * num_of_chars

    if len(string_a) != len(string_b):
        return False

    for i in string_a:
        count_a[ord(i)] += 1

    for i in string_b:
        count_b[ord(i)] += 1

    for i in range(num_of_chars):
        if count_a[i] != count_b[i]:
            return False

    return True


def string_has_unique_chars(string):
    """Determines if a string has all unique characters.
    Note: only works for a-z.
    """

    visited_char = [0] * 256
    string_list = list(string)

    for i in string_list:
        if visited_char[ord(i)] == 0:
            # set the character char to 1
            visited_char[ord(i)] = 1

        else:
            return False

    return True


def string_has_unique_chars_v2(string):
    """Determines if a string has all unique characters,
    without using an extra data structure.
    Note: only works for a-z.
    With this you need remember: bitwise OR operator (|) sets a bit to 1.
    """

    checker = 0
    string_list = list(string)

    for i in string_list:
        ascii_val = ord(i)

        if (checker & (1 << ascii_val)) > 0:
            return False
        # Set the bit for that ascii character to 1
        checker = checker | (1 << ascii_val)

    return True


def breakup_sms(input_string, char_limit):
    # Hey Mel, your uber
    # is arriving now

    # Hey blahblahblah-long named
    # person

    split_string = input_string.split(' ')

    new_string = []

    string_so_far = ''
    character_count = 0

    for i in range(len(split_string)):
        # Grab each element and count the characters
        current_string = split_string[i]

        string_size = len(current_string)

        if string_size < char_limit:
            # Need to break the string

            mini_split = list(current_string)

            new_split = len(mini_split) / char_limit

            for j in range(new_split):

                mini_string = current_string[j]
                string_so_far += current_string + ' '

        # idea: replace contents in original list instead of extra logic

        # The extra one is for space between words
        character_count += string_size + 1

        if character_count < char_limit:

            string_so_far += current_string + ' '
            if '\n' in current_string:
                new_string.append(string_so_far)

        else:
            new_string.append(string_so_far)
            string_so_far = ''
            if current_string:
                string_so_far += current_string + ' '
            character_count = 0

    # return list of strings
    return new_string
