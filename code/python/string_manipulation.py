"""String manipulation questions."""

from collections import Iterable


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


def breakup_sentence(input_string, char_limit):
    """Given a sentence, break it up into sub-sentences where
    the length of each sub-sentence, character-wise, is below
    the 'char_limit'.

    Note: This solution loops the list "twice" to identify words
    that go over the character limit.
    """

    splitted_string = input_string.split(' ')
    new_sentences = []

    composed_string = ''
    character_count = 0

    split_size = len(splitted_string)

    new_splitted_string = []
    for i in range(split_size):
        # Grab each word and count the characters
        current_word = splitted_string[i]

        # Check the size of the word
        word_size = len(current_word)

        if word_size > char_limit:
            # Need to break the string down further
            splitted_words = [current_word[i:i+char_limit]
                              for i in range(0, len(current_word), char_limit)]

            splitted_string[i] = splitted_words
            flattened = flatten(splitted_string)
            for word in flattened:
                new_splitted_string.append(word)

    # If new splits were not needed, use the old list
    if not new_splitted_string:
        new_splitted_string = splitted_string

    split_size = len(new_splitted_string)
    for i in range(split_size):
        # Grab each word and count the characters
        current_word = new_splitted_string[i]

        # Check the size of the word
        word_size = len(current_word)

        if character_count + word_size < char_limit:

            composed_string += current_word + ' '
            character_count += word_size + 1

        else:
            # Remove the extra space in the end of the sentence.
            composed_string = composed_string[:-1]
            new_sentences.append(composed_string)
            composed_string = ''
            if current_word:
                composed_string += current_word + ' '
                # Edge case - when the string size is the size of
                # the limit. This is safe to do because the words
                # should have already been broken up to the correct size.
                if len(composed_string) >= char_limit:
                    composed_string = composed_string[:-1]
                    new_sentences.append(composed_string)
                    composed_string = ''
            character_count = 0

    if composed_string:
        composed_string = composed_string[:-1]
        new_sentences.append(composed_string)

    return new_sentences


def flatten(coll):
    """Helper function used in 'breakup_sentence' to flatten
    a nested list of strings.
    """
    for i in coll:
        if isinstance(i, Iterable) and not isinstance(i, str):
            for subc in flatten(i):
                yield subc
        else:
            yield i


def find_matching_brackets(input_string):
    """Given a string of brackets, find the longest matching
    brackets. For instance '()(())' -> 4
    """

    input_array = str(input_string)
    char_stack = []
    result = 0
    for i in range(len(input_array)):
        if input_array[i] == '(':
            char_stack.append(i)
        elif input_array[i] == ')':
            if char_stack:
                char_stack.pop()
                if len(char_stack) != 0:
                    # If stack is not empty, find the length of current valid
                    # substring by taking difference between current index and
                    # top of the stack.
                    result = max(result, i - char_stack[-1])
                else:
                    # If stack is empty, push current index as base for next
                    # valid substring. Think of this as when you calculate the
                    # max above, you would subtract last index from the index
                    # just before when you saw the first '('.
                    char_stack.append(i)

    # Count both the opening and closing brackets
    return result
