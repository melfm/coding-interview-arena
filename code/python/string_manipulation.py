

def reverse_string(string):

    return string[::-1]

def reverse_string_v2(string):

    p1 = 0
    p2 = len(string) - 1

    string_chars = list(string)

    while p1 != p2:

        tmp = string_chars[p1]
        string_chars[p1] = string_chars[p2]
        string_chars[p2] = tmp

        p1 += 1
        p2 -=1

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


def sort_input_alphabet(string):

    string_list = list(string)

    sorted_string = insertion_sort(string_list)

    return sorted_string

def insertion_sort(array):

    for i in range(1, len(array)):

        val = array[i]

        p_prev = i - 1
        while p_prev >=0 and val < array[p_prev]:
            array[p_prev+1] = array[p_prev]
            p_prev -= 1

        array[p_prev+1] = val

    return array
