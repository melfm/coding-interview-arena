"""String manipulation questions."""

from collections import Iterable
from collections import defaultdict


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

    while (p0 < p1):

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

    while (p0 < p1):

        if word[p0].lower() != word[p1].lower():

            # print('Palindrome subset')
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
            splitted_words = [
                current_word[i:i + char_limit]
                for i in range(0, len(current_word), char_limit)
            ]

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

    return result


def combine_and_permute(str_list):
    """Given a list of characters, generate all possible combinations.
    For instance given [a, b, c] -> [[a], [a, b], [a, b, c],
                                     [b], [b, a], [b, a, c] ... ]
    You need to find the permutation of this and then the permutation of all
    possible combinations. Also note that [a, b] != [b, a] so you want to return
    all these combinations.
    """

    def permute(data, start, combs):
        if start == len(data):
            combs.append(data)
            return

        data = list(data)
        for i in range(start, len(data)):
            data[start], data[i] = data[i], data[start]
            permute(data, start + 1, combs)
            data[start], data[i] = data[i], data[start]

    def combinate(prefix, data, perm_combs):
        data = list(data)
        # Here instead of custom permute, could also use:
        # list(itertools.permutations(data))
        permute(list(prefix), 0, perm_combs)
        for i in range(0, len(data)):
            combinate(prefix + data[i], data[i + 1:], perm_combs)

    perm_combs = []
    combinate("", str_list, perm_combs)
    return perm_combs[1:]


def combine_and_permute_order_free_str(str_list):
    """Given a list of characters, generate all possible unordered combinations.
    For instance given [a, b, c] -> ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    """

    def combinate(prefix, input_array, combos=[]):
        if input_array:
            combos.append(prefix + input_array[0])
            combinate(prefix + input_array[0], input_array[1:], combos)
            combinate(prefix, input_array[1:], combos)

    combos = []
    combinate("", str_list, combos)
    return combos


def remove_str_mask_char(input_str, str_mask):
    """Remove characters from the first string which are present
    in the second string.
    """

    str_list = input_str.lower()

    masked_str = []
    for char in str_list:
        match_found = False
        for m in str_mask:

            if char == m:
                match_found = True
                break

        if not match_found:
            masked_str.append(char)

    return ''.join(masked_str)


def remove_str_mask_char_v2(input_str, str_mask):
    """Use a hash-table instead of two loops.
    """

    input_str = input_str.lower()
    hash_table = {}
    # The values in the map are irrelevant.
    for m in str_mask:
        hash_table.update({m: 1})

    # You could also change the string in-place with a while loop
    # and a flag as when the end of string is reached, but this is
    # faster.
    new_string = ""
    for s in input_str:
        if s not in str_mask:
            new_string += s

    return new_string


def isEditDistanceOne(str1, str2):

    m = len(str1)
    n = len(str2)

    if abs(m - n) > 1: return False

    edit_count = 0

    p1 = 0
    p2 = 0

    while (p1 < m and p2 < n):

        if str1[p1] != str2[p2]:
            if edit_count == 1:
                return False

            # Decide how to increment each pointer
            if m < n:
                # One string is larger, move on that one
                # maybe you can replace one character
                p2 += 1
            if m > n:
                p1 += 1
            else:
                # Need to keep going synchronously and
                # count the number of differences
                p1 += 1
                p2 += 1

            # Already seen a conflict to increment this
            edit_count += 1
        else:
            p1 += 1
            p2 += 1

    # We might have missed a last character in one of the strings
    if p1 < m or p2 < n:
        edit_count += 1

    return edit_count == 1


def k_palindrome_rec(str, str_rev, m, n):

    # If first string is empty, we need to remove
    # all characters from the second string
    if m == 0: return n

    # The other way round of above.
    if n == 0: return m

    # If last two characters are the same, ignore the last
    # characters and get count for remaining strings
    if str[m - 1] == str_rev[n - 1]:
        return k_palindrome_rec(str, str_rev, m - 1, n - 1)

    # If they are not the same, remove from both
    # and take the min op.
    res = 1 + min(k_palindrome_rec(str, str_rev, m - 1, n),
                  (k_palindrome_rec(str, str_rev, m, n - 1)))

    return res


def k_palindrome(input_str, k):
    """
    A k-palindrome is a string which transforms into a palindrome
    on removing at most k characters.
    Given a string and int K, print YES or NO
    S can be large 20,000 characters
    0<=k<=30
    The time complexity of this sol exponential.
    In worst case, we may end up doing O(2n) operations.
    Ideally O(N*K) complexity. Edit-Distance algorithm without this
    k removal, would be O(N^2).
    """
    reversed_str = input_str[::-1]
    l = len(input_str)
    return (k_palindrome_rec(input_str, reversed_str, l, l) <= k * 2)

def longest_unique_substring(str_input):
    """ Question and other solutions:
    https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
    """
    p1 = 0
    p2 = 1

    n = len(str_input)
    max_sub = ''
    all_subs = []

    window = defaultdict()

    while p2 <= n:
        if p2 != n:
            p1_character = str_input[p1]
            p2_character = str_input[p2]
            window[p1_character] = 1
        if not p2_character in window.keys():
            window[p2_character] = 1
            p2 +=1
        else:
            current_sub = str_input[p1:p2]
            if len(max_sub) <= len(current_sub):
                max_sub = current_sub
                all_subs.append(max_sub)
            # reset window
            window = {}
            p1 = p1 + 1
            p2 = p1 + 1

    max_len = len(max(all_subs, key=len))
    return [state for state in all_subs if len(state) == max_len]

def longest_unique_substring_v2(str_input):

    n = len(str_input)

    if n == 0: return n

    p1 = 0
    p2 = 0
    window = defaultdict(int)
    max_sub = ''
    all_subs = [max_sub]

    while p2 < n:
        # slide the window forward
        p2_character = str_input[p2]
        window[p2_character] += 1
        p2 += 1

        # if a duplicate char appears, drop it off from left(p1)
        # to make them unique again
        while window[p2_character] > 1:
            window[str_input[p1]] -=1
            p1 += 1
        curr_sub = str_input[p1:p2]
        if len(curr_sub) > len(max_sub):
            all_subs = []
            max_sub = curr_sub
            all_subs.append(max_sub)
        elif len(curr_sub) == len(max_sub):
            # keep both
            max_sub = curr_sub
            all_subs.append(max_sub)

    return all_subs


def remove_duplicate_char_order(str):
    """ Given a string s, remove duplicate letters so that every
    letter appears once and only once. You must make sure your
    result is  the smallest in lexicographical order
    among all possible results.

    This question seems easy at first, but actually the order
    preserving logic makes it harder. The question is not phrased
    very well.
    """

    last_occurrence = {}
    stack = []

    # Keep the unique characters first
    for i in range(len(str)):
        last_occurrence[str[i]] = i

    # Order matters
    # If its not in the stack, we want to push it
    # But it also has to be lexicographically smaller
    # than other elements in the stack.
    for i in range(len(str)):
        if str[i] not in stack:
            while(stack and stack[-1] > str[i] and last_occurrence[stack[-1]] > i):
                stack.pop()
            stack.append(str[i])

    return ''.join(stack)


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    """https://leetcode.com/problems/interleaving-string/
    Apparently my implementation fails on the second test-case
    on leetcode, but I didn't understand why.
    """

    def construct_dict(str):
        char_dict = {}

        for char in str:
            if not char in char_dict:
                # if its a new item
                char_dict[char] = 1
            else:
                occurence = char_dict[char]
                occurence += 1
                char_dict[char] = occurence
        return char_dict

    input_dict = construct_dict(s1 + s2)
    output_dict = construct_dict(s3)

    interleave_match = True
    for key_char_s_in in input_dict:
        for key_char_s_out in output_dict:
            if key_char_s_in == key_char_s_out:
                if input_dict[key_char_s_in] != output_dict[key_char_s_out]:
                    interleave_match = False
                    return interleave_match
    return interleave_match
