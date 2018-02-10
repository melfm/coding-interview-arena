
def reverse_string(string):

    return string[::-1]


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
